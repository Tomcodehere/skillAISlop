#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""enrichir_xrefs.py — complète les cross-refs de toutes les skills par similarité
(cosinus bag-of-words sur nom+signal+mot_cle, même domaine d'abord), et propose
des dépendances depends_on (workflow) vers les 2 voisins les plus forts du même domaine.

Usage : python3 outils/enrichir_xrefs.py [--dry]
"""
import re, sys, math, unicodedata
from pathlib import Path
from collections import Counter

RACINE = Path(__file__).resolve().parent.parent
SK = RACINE / "skills"

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()
def bow(s):
    return Counter(w for w in re.findall(r"[a-zàâäéèêëîïôöùûüç-]{4,}", norm(s)))
def cos(a, b):
    if not a or not b: return 0.0
    inter = sum((a & b).values())
    return inter / math.sqrt(sum(a.values()) * sum(b.values())) if inter else 0.0

skills = {}
for f in sorted(SK.glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
    if not m: continue
    fm = m.group(1)
    g = lambda k: (re.search(rf'^{k}: "(.*)"$', fm, re.M) or [None, ""])[1]
    num = int(re.search(r"^num: (\d+)$", fm, re.M).group(1))
    if num == 0: continue
    texte = g("nom") + " " + g("signal") + " " + g("mot_cle")
    skills[num] = {"f": f, "txt": txt, "fm": fm, "nom": g("nom"), "dom": g("domaine"),
                   "bow": bow(texte), "refs": [x.strip() for x in re.search(r"^cross_refs: \[(.*)\]$", fm, re.M).group(1).split(",") if x.strip()]}

# top-3 voisins : même domaine d'abord, puis global
nums = sorted(skills)
n = 0
for num in nums:
    s = skills[num]
    scores = []
    for m in nums:
        if m == num: continue
        c = cos(s["bow"], skills[m]["bow"])
        if skills[m]["dom"] == s["dom"]: c *= 1.5  # boost même domaine
        scores.append((c, m))
    scores.sort(reverse=True)
    top3 = [m for c, m in scores[:3] if c > 0.08]
    # garder les refs existantes + compléter à 3
    refs = list(dict.fromkeys(s["refs"] + [str(t) for t in top3]))[:3]
    if [str(t) for t in top3] != s["refs"][:len(top3)] or len(refs) != len(s["refs"]):
        fm2 = re.sub(r"^cross_refs: \[[^\]]*\]$", f"cross_refs: [{', '.join(refs)}]", s["fm"], flags=re.M)
        txt2 = s["txt"].replace(s["fm"], fm2, 1)
        # mention dans Cas d'usage pour R4
        if not re.search(r"skills? \d+", txt2.split("**Cas d'usage**")[-1] if "**Cas d'usage**" in txt2 else ""):
            txt2 = re.sub(r"(\*\*Cas d'usage\*\* : )", rf"\g<1>voir aussi skill {refs[0]} ({refs[0]}). ", txt2, count=1)
        if txt2 != s["txt"]:
            s["f"].write_text(txt2, encoding="utf-8")
            n += 1
print(f"cross-refs mises à jour: {n} / {len(nums)}")

# depends_on : pour chaque skill, le meilleur voisin du même domaine comme étape suivante
m = 0
for num in nums:
    s = skills[num]
    txt = s["f"].read_text(encoding="utf-8")
    if re.search(r"^depends_on:", txt, re.M): continue
    scores = [(cos(s["bow"], skills[o]["bow"]), o) for o in nums if o != num and skills[o]["dom"] == s["dom"]]
    scores.sort(reverse=True)
    if scores and scores[0][0] > 0.15:
        nxt = scores[0][1]
        mm = re.match(r"(---\n.*?\n)(---\n)", txt, re.S)
        if mm:
            txt = txt[:mm.end(1)] + f"depends_on: [{nxt}]\n" + txt[mm.end(1):]
            s["f"].write_text(txt, encoding="utf-8")
            m += 1
print(f"depends_on ajoutés: {m}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""score_skills.py — score de qualité /100 par skill + moyenne globale.

Barème (100 pts) :
  - Frontmatter complet (10 champs) ............ 10 pts
  - 12 sections TEMPLATE-v2 présentes .......... 24 pts (2 pts / section)
  - Suffisance de contenu par section .......... 40 pts
      (min. longueurs : Objectif >= 40 car., Instructions >= 80, Méthode >= 3 étapes,
       Exemple >= 30, Cas d'usage >= 2 usages, Triggers/Garde-fous/Inputs/Sorties/QA/DoD >= 20 car.)
  - Cross-ref présente ......................... 6 pts
  - Unicité nom/signal/mot_cle (vs catalogue) .. 10 pts
  - Signal dans les limites spec (<=1024, pas de <>) .. 5 pts
  - Corps < 500 lignes ......................... 5 pts

Usage : python3 outils/score_skills.py [--rapport documentations/skillsdocs/scores.md] [--top N]
"""
import re, sys, unicodedata
from pathlib import Path
from collections import Counter

RACINE = Path(__file__).resolve().parent.parent
SKILLS = RACINE / "skills"

SECTIONS = {
    "Objectif": 40, "Instructions système": 80, "Méthode": None, "Exemple de prompt": 30,
    "Cas d'usage": None, "Quand l'utiliser": 20, "Hors périmètre": 20, "Garde-fous": 20,
    "Inputs requis": 20, "Sorties attendues": 20, "Checklist QA interne": 20, "Definition of done": 20,
}
FM_CHAMPS = ["num", "nom", "emoji", "domaine", "signal", "mot_cle", "nom_court", "branche", "synonymes", "cross_refs"]

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()

def parse(f):
    txt = f.read_text(encoding="utf-8")
    parts = txt.split("---")
    if len(parts) < 3: return None
    fm, body = parts[1], "---".join(parts[2:])
    g = lambda k: (re.search(rf'^{k}: "(.*)"$', fm, re.M) or [None, ""])[1]
    return fm, body, g, int(re.search(r"^num: (\d+)$", fm, re.M).group(1))

def scorer(f, noms, sigs, mcs):
    p = parse(f)
    if not p: return None
    fm, body, g, num = p
    score = 0; details = []
    # frontmatter 10 pts
    fm_ok = sum(1 for k in FM_CHAMPS if re.search(rf"^{k}:", fm, re.M))
    score += fm_ok; details.append(f"frontmatter {fm_ok}/10")
    # sections présentes 24 pts
    secs = {}
    cur = None
    for l in body.splitlines():
        m = re.match(r"^\*\*(.+?)\*\*\s*:\s*(.*)$", l)
        if m: cur = m.group(1); secs[cur] = [m.group(2)]
        elif cur: secs[cur].append(l)
    pres = 0
    for s in SECTIONS:
        if any(k.startswith(s.split(" (")[0]) for k in secs): pres += 1
    score += pres * 2; details.append(f"sections {pres}/12")
    # contenu suffisant 40 pts
    contenu_ok = 0
    for s, minlen in SECTIONS.items():
        cle = next((k for k in secs if k.startswith(s.split(" (")[0])), None)
        if not cle: continue
        texte = " ".join(secs[cle])
        if s == "Méthode":
            if len(re.findall(r"(?m)^\d+\. ", "\n".join(secs[cle]))) >= 3: contenu_ok += 1
        elif s == "Cas d'usage":
            if len([u for u in re.split(r"[,;]", texte) if u.strip()]) >= 2: contenu_ok += 1
        elif len(texte.strip()) >= minlen:
            contenu_ok += 1
    score += round(contenu_ok / 12 * 40); details.append(f"contenu {contenu_ok}/12 sections suffisantes")
    # cross-ref 6 pts
    refs = re.search(r"^cross_refs: \[([^\]]*)\]$", fm, re.M).group(1).strip()
    if refs: score += 6; details.append("cross-ref oui")
    # unicité 10 pts
    nom, sig, mc = norm(g("nom")), norm(g("signal")), norm(g("mot_cle"))
    if noms[nom] <= 1 and sigs[sig] <= 1 and mcs[mc] <= 1: score += 10
    details.append("unicité oui" if noms[nom] <= 1 and sigs[sig] <= 1 and mcs[mc] <= 1 else "DOUBLON")
    # signal spec 5 pts
    s_len = len(g("signal"))
    if s_len <= 1024 and "<" not in fm and ">" not in fm: score += 5
    # taille 5 pts
    if len(body.splitlines()) < 500: score += 5
    return num, g("nom"), min(score, 100), details

def main():
    top = 10
    if "--top" in sys.argv: top = int(sys.argv[sys.argv.index("--top") + 1])
    rapport = None
    if "--rapport" in sys.argv: rapport = Path(sys.argv[sys.argv.index("--rapport") + 1])
    noms, sigs, mcs = set(), set(), set()
    # pré-charger unicité sur tout le catalogue
    for f in sorted(SKILLS.glob("*.md")):
        p = parse(f)
        if p:
            fm, body, g, num = p
            noms.add(norm(g("nom"))); sigs.add(norm(g("signal"))); mcs.add(norm(g("mot_cle")))
    # il faut compter les doublons : recommençons avec Counter
    noms, sigs, mcs = Counter(), Counter(), Counter()
    for f in sorted(SKILLS.glob("*.md")):
        p = parse(f)
        if p:
            fm, body, g, num = p
            noms[norm(g("nom"))] += 1; sigs[norm(g("signal"))] += 1; mcs[norm(g("mot_cle"))] += 1
    results = []
    for f in sorted(SKILLS.glob("*.md")):
        p = parse(f)
        if not p: continue
        fm, body, g, num = p
        if num == 0: continue
        r = scorer(f, noms, sigs, mcs)
        if r: results.append(r)
    results.sort(key=lambda r: r[2])
    moyenne = sum(r[2] for r in results) / len(results)
    print(f"skills scorées : {len(results)} · moyenne globale : {moyenne:.1f}/100")
    print(f"min : {results[0]}  ·  max : {results[-1]}")
    print(f"< 70 : {sum(1 for r in results if r[2] < 70)} · 70-89 : {sum(1 for r in results if 70 <= r[2] < 90)} · >= 90 : {sum(1 for r in results if r[2] >= 90)}")
    print("\nTop des moins bonnes :")
    for r in results[:top]:
        print(f"  {r[2]:3d}/100  #{r[0]} {r[1][:50]}  ({', '.join(r[3])})")
    if rapport:
        rapport.parent.mkdir(parents=True, exist_ok=True)
        L = ["# Scores de qualité des skills (/100)", "",
             f"Moyenne globale : **{moyenne:.1f}/100** sur {len(results)} skills · <70 : {sum(1 for r in results if r[2] < 70)} · >=90 : {sum(1 for r in results if r[2] >= 90)}",
             "", "| Score | # | Skill | Détails |", "|---|---|---|---|"]
        for r in results:
            L.append(f"| {r[2]} | {r[0]} | {r[1]} | {', '.join(r[3])} |")
        rapport.write_text("\n".join(L) + "\n", encoding="utf-8")
        print(f"rapport → {rapport}")

if __name__ == "__main__":
    main()

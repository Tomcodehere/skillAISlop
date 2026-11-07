#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère automatiquement documentations/skillsdocs/ depuis skills/*.md + catalogue/sources.md.
Relancer après chaque build/vague : python3 outils/gen_docs.py"""
import re, sqlite3, unicodedata
from pathlib import Path
RACINE = Path(__file__).resolve().parent.parent
OUT = RACINE / "documentations" / "skillsdocs"
DB = RACINE / "outils" / "skills.db"
def norm(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()
def slug(s): return re.sub(r"[^a-z0-9]+", "-", norm(s)).strip("-")[:60]
skills = []
for f in sorted((RACINE / "skills").glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
    if not m: continue
    fm = m.group(1)
    g = lambda k: (re.search(rf'^{k}: "(.*)"$', fm, re.M) or [None, ""])[1]
    skills.append(dict(
        num=int(re.search(r"^num: (\d+)$", fm, re.M).group(1)), nom=g("nom"), emoji=g("emoji"),
        domaine=g("domaine"), signal=g("signal"), mot_cle=g("mot_cle"), nom_court=g("nom_court"),
        syns=[s.strip().strip('"') for s in re.search(r'^synonymes: \[(.*)\]$', fm, re.M).group(1).split(",") if s.strip()],
        refs=[int(x) for x in re.search(r'^cross_refs: \[(.*)\]$', fm, re.M).group(1).split(",") if x.strip()],
        tags=[s.strip().strip('"') for s in re.search(r'^tags: \[(.*)\]$', fm, re.M).group(1).split(",") if s.strip()] if re.search(r'^tags:', fm, re.M) else [],
        fichier=f.name))
skills.sort(key=lambda s: s["num"])
skills = [s for s in skills if s["num"] != 0]  # -1 : skill 0 = routeur, jamais comptée comme skill
refs = []
for l in (RACINE / "catalogue" / "sources.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r"^- (?:\[([^\]]+)\]\(([^)]+)\)|(\S+))\s*[—-]\s*(.*)", l.strip())
    if m and (m.group(2) or (m.group(3) or "").startswith("http")):
        refs.append((m.group(1) or m.group(3), m.group(2) or m.group(3), m.group(4).strip()))
stats = {}
if DB.exists():
    db = sqlite3.connect(DB)
    stats = {t: db.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in ("skills", "synonymes", "skills_fts")}
    db.close()
OUT.mkdir(parents=True, exist_ok=True); (OUT / "domaines").mkdir(exist_ok=True)
L = ["# RÉFÉRENCES — projet skillAISlop", "", f"{len(refs)} références (veille vagues 10-13 + standards 2026). Chaque entrée : puce · titre · description · lien.", ""]
for t, u, d in refs: L.append(f"- **{t}** — {d} — [{u}]({u})")
(OUT / "RÉFÉRENCES.MD").write_text("\n".join(L) + "\n", encoding="utf-8")
dom = {}
for s in skills: dom.setdefault(s["domaine"], []).append(s)
R = [f"# Documentation skillAISlop — générée automatiquement (gen_docs.py)", "",
     f"**{len(skills)} skills** + 1 routeur (skill 0, non compté) · **{len(dom)} domaines** · **{stats.get('synonymes','?')} synonymes** · **{stats.get('skills_fts','?')} FTS** · **{stats.get('skills','?')} vecteurs**", "",
     "> Auto-générée par `python3 outils/gen_docs.py` depuis `skills/*.md` + `catalogue/sources.md`. Ne pas éditer à la main.", "", "## Sommaire", ""]
for d in sorted(dom): R.append(f"- [{d}](domaines/{slug(d)}.md) — {len(dom[d])} skills")
R += ["", "- [RÉFÉRENCES.MD](RÉFÉRENCES.MD) · [TEMPLATE-v2.md](TEMPLATE-v2.md) · [migration-v2.md](migration-v2.md)", ""]
(OUT / "README.md").write_text("\n".join(R) + "\n", encoding="utf-8")
for d, ss in sorted(dom.items()):
    L = [f"# Domaine : {d} ({len(ss)} skills)", ""]
    for s in ss:
        refs_l = ", ".join(str(r) for r in s["refs"]) or "—"
        syns = ", ".join(f"« {x} »" for x in s["syns"]) or "—"
        tags_l = ", ".join(s.get("tags", [])) or "—"
        L += [f"## {s['num']}. {s['emoji']} {s['nom']}", "",
              f"- **Fichier** : `skills/{s['fichier']}` · **Mot-clé** : « {s['mot_cle']} » · **Nom court** : {s['nom_court']}",
              f"- **Signal** : {s['signal']} · **Synonymes** : {syns} · **Cross-refs** : {refs_l} · **Tags** : {tags_l}", ""]
    (OUT / "domaines" / f"{slug(d)}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"✅ {OUT} : {len(skills)} skills + 1 routeur, {len(dom)} domaines, {len(refs)} références")

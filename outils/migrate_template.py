#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""migrate_template.py — audite les skills/*.md contre TEMPLATE-v2
(documentations/skillsdocs/TEMPLATE-v2.md) et peut insérer les sections
manquantes (--fix).

Sections obligatoires v2 : Objectif, Triggers, Hors périmètre, Garde-fous,
Instructions système, Inputs requis, Méthode, Sorties attendues,
Exemple de prompt, Cas d'usage, Checklist QA, Definition of done.
Frontmatter obligatoire : num, date_ajout (YYYY-MM, ajoutée automatiquement
à la création), nom, emoji, domaine, signal, mot_cle,
nom_court, branche, synonymes, cross_refs.
Règles spec 2026 : signal ≤ 1024 car., pas de < > dans le frontmatter,
date_ajout au format YYYY-MM (mois 01-12), corps < 500 lignes.

Usage : python3 outils/migrate_template.py [--fix] [--rapport <fichier.md>]
"""
import re, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SKILLS = RACINE / "skills"

SECTIONS_V2 = [
    ("Objectif", r"^\*\*Objectif\*\*", None),
    ("Triggers", r"^\*\*Quand l'utiliser \(triggers\)\*\*", "**Quand l'utiliser (triggers)** : <3-5 déclencheurs — à compléter>"),
    ("Hors périmètre", r"^\*\*Hors périmètre\*\*", "**Hors périmètre** : <ce qui ne route PAS ici — à compléter>"),
    ("Garde-fous", r"^\*\*Garde-fous\*\*", "**Garde-fous** :\n- GF-01 : <contrainte dure — à compléter>"),
    ("Instructions système", r"^\*\*Instructions système\*\*", None),
    ("Inputs requis", r"^\*\*Inputs requis\*\*", "**Inputs requis** : <données nécessaires — à compléter>"),
    ("Méthode", r"^\*\*Méthode\*\*", None),
    ("Sorties attendues", r"^\*\*Sorties attendues\*\*", "**Sorties attendues** : <livrables — à compléter>"),
    ("Exemple de prompt", r"^\*\*Exemple de prompt\*\*", None),
    ("Cas d'usage", r"^\*\*Cas d'usage\*\*", None),
    ("Checklist QA", r"^\*\*Checklist QA interne\*\*", "**Checklist QA interne** :\n- [ ] <critère — à compléter>"),
    ("Definition of done", r"^\*\*Definition of done\*\*", "**Definition of done** :\n- [ ] <critère mesurable — à compléter>"),
]
FRONTMATTER = ["num", "date_ajout", "nom", "emoji", "domaine", "signal", "mot_cle", "nom_court", "branche", "synonymes", "cross_refs"]
# "tags" est optionnel (filtre route --tag) — non requis par l'audit

def auditer(txt: str):
    fm = re.match(r"---\n(.*?)\n---", txt, re.S)
    fm_txt = fm.group(1) if fm else ""
    manque_fm = [k for k in FRONTMATTER if not re.search(rf"^{k}:", fm_txt, re.M)]
    manque = [nom for nom, pat, _ in SECTIONS_V2 if not re.search(pat, txt, re.M)]
    regles = []
    m = re.search(r'^signal: "(.*)"$', fm_txt, re.M)
    if m and len(m.group(1)) > 1024: regles.append("signal > 1024 car.")
    m = re.search(r'^date_ajout: "(\d{4})-(\d{2})"$', fm_txt, re.M)
    if m and not (1 <= int(m.group(2)) <= 12):
        regles.append("date_ajout invalide (format YYYY-MM, mois 01-12)")
    if re.search(r"[<>]", fm_txt): regles.append("frontmatter contient < ou >")
    body = txt.split("---", 2)[2] if txt.count("---") >= 2 else txt
    if len(body.splitlines()) > 500: regles.append("corps > 500 lignes")
    return manque_fm, manque, regles

def inserer(txt: str, manquants: list, manquants_fm: list | None = None) -> str:
    fm, _, body = txt.split("---", 2)
    if manquants_fm and "date_ajout" in manquants_fm:
        import datetime
        today = datetime.date.today().strftime("%Y-%m")
        if not re.search(r"^date_ajout: ", fm, re.M):
            fm = re.sub(r"^(num: \d+)$", '\\1\ndate_ajout: "' + today + '"', fm, count=1, flags=re.M)
    ajouts = [bloc for nom, pat, bloc in SECTIONS_V2 if nom in manquants and bloc]
    if ajouts:
        body = "\n\n" + "\n\n".join(ajouts) + "\n" + body.lstrip("\n")
    return f"---{fm}---{body}"

def main():
    fix = "--fix" in sys.argv
    rapport = None
    if "--rapport" in sys.argv:
        rapport = Path(sys.argv[sys.argv.index("--rapport") + 1])
    files = sorted(SKILLS.glob("*.md"))
    results = []
    for f in files:
        txt = f.read_text(encoding="utf-8")
        mf, ms, rg = auditer(txt)
        if mf or ms or rg:
            results.append((f.name, mf, ms, rg))
        if fix and (ms or mf):
            f.write_text(inserer(txt, ms, mf), encoding="utf-8")
    n_ok = len(files) - len(results)
    L = ["# Rapport migration TEMPLATE-v2", "",
         f"Skills auditées : {len(files)} · conformes : {n_ok} · à migrer : {len(results)}",
         f"Mode : {'--fix appliqué (placeholders insérés)' if fix else 'audit seul'}", ""]
    for name, mf, ms, rg in results[:300]:
        L.append(f"## {name}")
        if mf: L.append(f"- frontmatter manquant : {', '.join(mf)}")
        if ms: L.append(f"- sections manquantes : {', '.join(ms)}")
        if rg: L.append(f"- règles spec : {', '.join(rg)}")
        L.append("")
    txt = "\n".join(L)
    print(f"auditées {len(files)} · conformes {n_ok} · à migrer {len(results)} · mode={'fix' if fix else 'audit'}")
    from collections import Counter
    c = Counter(s for _, _, ms, _ in results for s in ms)
    print("sections les plus manquantes :", c.most_common())
    if rapport:
        rapport.parent.mkdir(parents=True, exist_ok=True)
        rapport.write_text(txt + "\n", encoding="utf-8")
        print(f"rapport → {rapport}")

if __name__ == "__main__":
    main()

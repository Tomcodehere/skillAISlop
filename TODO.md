---
name: "todo-skillaislop"
title: "TODO — skillAISlop"
type: "text/markdown"
---

# TODO — skillAISlop

> 🔎 **Index** : Optimisations perf · Export multi-projets · Process · Prochaine vague

## Optimisations perf routeur (mesuré : route 8,5 ms, DB 2,04 Mo)

- [x] ~~Table `mots_cles` en SQL~~ → fait : voie mot-clé en requête indexée (instr/length), route 8,5 → 6,1 ms, 449/449 tests
- [x] ~~Trigrammes filtrés >= 5 lettres~~ → fait : 65 289 → 33 555 entrées, DB 2,04 → 1,72 Mo (−16 %), fautes de frappe toujours OK (organisr/procrastinnation → exit 0)
- [ ] vec0 + HNSW (index vectoriel approché) si le catalogue dépasse ~5 000 skills (inutile à 900)
- [x] ~~WAL checkpoint~~ → `PRAGMA wal_checkpoint(PASSIVE)` après chaque écriture de session (routes/non_routees) ; VACUUM déjà en fin de build
- [ ] RTREE / géolocalisation de skills — écarté (pas de cas d'usage)
- [ ] stmt (vtab) — écarté (le Python suffit)
- [ ] Export JSON 100 % SQL (json_group_array) à la place du Python — si l'export grossit

## Export multi-projets (pack portable)

- [x] ~~`build --from-skills`~~ → fait : 23 fichiers skills/ synchronisés sur le sommaire, carte des domaines depuis le canvas si présent, synonymes = SYNONYMES (source unique, embarquée dans le pack) ; build canvas et --from-skills produisent des tables identiques (skills/synonymes/domaines/FTS/trigrammes)
- [x] ~~`routage.py pack`~~ → fait : zip 1,01 Mo (900 skills + routage.py + manifeste.json v12.0.0 + hash sha256 + README) + `pack --check` = test de fidélité ✅ FIDÈLE, rejoué en CI
- [x] ~~Wrappers `SKILL.md`~~ → `routage.py skillmd` génère 900 SKILL.md (frontmatter standard + metadata num/domaine/synonymes) dans data/agent-skills/ + skills.json pour `npx skills add` ; testé en CI (non bloquant), data/agent-skills/ ignoré par git
- [x] ~~`routage.py serve`~~ → fait : API loopback 127.0.0.1 (bind non-loopback refusé), /health + /route?q= (exit 0/1/2, voies/scores) + /skills + /export.json ; smoke test en CI
- [x] ~~Versioning sémantique~~ → `CATALOGUE_VERSION` (12.0.0) écrite dans `meta` au build, affichée par `versions`, embarquée dans le manifeste du pack

## Process

- [ ] `misses --suggest` en routine hebdo — testé le 2026-11-04 : journal OK, suggestions OK (faux positifs filtrés à la main, R6), `--clear` OK
- [ ] Merger les PR dès que CLEAN + CI verte (éviter l'accumulation sur la branche)
- [ ] Un commit par sujet ; `git diff --stat` + relecture avant chaque push (hook pre-push déjà en place)

## Prochaine vague

- [ ] Vague 13 (R7, janvier 2027) : re-faire la veille web, viser les vrais gaps restants plutôt que du volume

- [ ] Vague 14 (R7, avril 2027) : prochaine veille trimestrielle

- [ ] Utiliser templateSkills.md du repo cloné tvprodel/SkillsAI (/workspace/github__tvprodel__SkillsAI, 313 *.skill.md, 13 sections standard) pour mettre à jour tous les fichiers agents de ce projet vers le template standard (Objectif, Triggers, Hors périmètre, Inputs, Sorties, Workflow, Garde-fous, Templates, QA, KPI, DoD, Exemples, Sources)

- [ ] Appliquer TEMPLATE-v2 à la vague 14 : maj catalogue/template.md + R2/regles.md + lint spec en CI + migrate_template.py --fix sur les skills existantes

- [ ] Multilingue EN : champ lang dans le frontmatter (fr/en), table lang(num,lang), filtre route --lang en, vague EN (traduction ou rédaction) — catalogue actuellement 100 % FR (1901 skills, 8,9 Mo)

- [x] ~~HNSW~~ → veille 2026-11-07 : sqlite-vec 0.1.9 (dernier PyPI) = KNN exact, pas d'ANN dans vec0 ; releases officielles annoncent ivf/diskann en WIP ; fork tiers brianmacy/sqlite-vec-hnsw (use_hnsw=1) non officiel. À 1 700 skills le brute-force suffit (~1 ms/voie vec). À activer > 5 000 skills via upgrade officiel ou le fork (à valider) — pack : deflate retenu (1,93 Mo, meilleur que LZMA 2,2 Mo sur markdown), skills.db exclu (régénéré par build --from-skills)

- [ ] Build parallèle (multiprocessing) testé 2026-11-07 : non rentable à 1 700 skills (spawn pool > calcul hash) — à réessayer > 20 000 skills ; build actuel 1,5 s (profilé : coût = spawn/imports, pas le calcul)

- [ ] Champ `resume` (condensé 2-3 lignes) dans le frontmatter de TOUTES les skills + dans le template (catalogue/template.md + documentations/skillsdocs/TEMPLATE-v2.md) : backfill auto (Objectif + 1re étape de la Méthode) sur les 2001 skills existantes, colonne `resume` dans skills.db (hors FTS : stabilité du golden) ✅ fait 2026-11-08, règle lint R15 ✅, export compact/complet l'inclut ✅, pack régénéré ✅ ; reste : pilote EN (étape 3) — `export --condensé` ✅ fait 2026-11-08 (data/catalogue-condensed.json déterministe, embarqué dans le pack + vérifié par pack --check + étape CI)

- [x] ~~Pilote multilingue EN~~ → fait 2026-11-08 (mécanisme lang GÉNÉRIQUE : sidecars `NNN-slug.<lang>.md`, `lang` frontmatter, table `lang(num,lang,fichier)`, tables `skills_<lang>`/FTS/vec, `route --lang <code>` + auto-détection stopwords + fallback FR, 11 sidecars .en.md pilote (skills 0-10), TESTS_ROUTAGE_EN, pack --check multi-langues, `skillmd --lang`, lint R16, export/condensé/count avec `langs`) — NL se branche pareil (vérifié fallback nl) : sidecars `skills/NNN-slug.en.md` (mêmes num/cross_refs/branche) + champ `lang: fr|en` + table `lang(num,lang)` + `route --lang en` (détection auto par stopwords, fallback FR si exit 2) + FTS5/vec/synonymes/trigrammes par langue + `export --condensé` vers data/catalogue-condensed.json (resume + étapes de méthode compactes + garde-fous GF) + pack + skillmd --lang en + gen_docs/audit par langue + tests/golden EN en CI — pilote d'abord sur le routeur (skill 0) + top-N popularité, puis vague EN par domaine

- [ ] Multilingue NL (néerlandais) : prévoir la même chose que le pilote EN — sidecars `skills/NNN-slug.nl.md`, `lang: "nl"`, `route --lang nl`, tables par langue (skills_nl / fts / vec), synonymes lang=nl, lang(num,lang), pack + skillmd --lang nl + gen_docs/audit par langue, tests/golden NL, export condensé par langue — IMPORTANT : le mécanisme lang du pilote EN doit être générique (code langue quelconque, pas hardcodé "en"), pour que NL (et autres) se branchent sans nouveau chantier

- [ ] skillsPerso (mesSkillsPerso/) + multilingue : détection de la langue — au build, lire le frontmatter `lang` du fichier perso s'il est présent, sinon DÉTECTER la langue du contenu (heuristique stopwords FR/EN/NL, ex. outils/detect_lang.py) et l'enregistrer (colonne lang de skills_perso + table lang) ; supporter les sidecars perso `nom.<lang>.md` comme pour le catalogue ; `route --lang en` doit aussi matcher les perso EN (voie 0b perso par langue, fallback FR) ; lint contrôle `lang` sur les perso ; pack embarque les sidecars perso NON (les perso restent locaux, jamais dans le pack)

- [ ] skillsPerso : traduction automatique dans le MÊME répertoire — pour chaque fichier perso, générer un sidecar `nom.<lang>.md` (mêmes num/cross_refs/branche, frontmatter traduit + `traduit: auto|humain` + `lang: <code>`) pour les autres langues (en, nl, …) ; commande dédiée type `perso --translate en` (traduction par le LLM hôte, jamais d'appel externe dans routage.py) ; les sidecars perso sont routés par `route --lang <code>` comme le catalogue (voie perso par langue) ; lint les contrôle (lang, date_ajout, resume, pas de < >) ; JAMAIS dans le pack (les perso restent locaux) ; relecture humaine à prévoir (traduit: auto)

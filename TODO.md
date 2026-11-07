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

- [ ] Multilingue EN : champ lang dans le frontmatter (fr/en), table lang(num,lang), filtre route --lang en, vague EN (traduction ou rédaction) — catalogue actuellement 100 % FR (1351 skills, 4,09 Mo)

- [ ] HNSW (index vectoriel approché) : NON supporté par sqlite-vec 0.1.9 (testé) — à activer si upgrade sqlite-vec ≥ version avec hnsw ET catalogue > 5 000 skills ; à 1 351 skills la recherche vec linéaire suffit (~1 ms). Pack : deflate retenu (1,93 Mo), LZMA testé moins bon sur markdown (2,2 Mo)

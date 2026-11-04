---
name: "todo-skillaislop"
title: "TODO — skillAISlop"
type: "text/markdown"
---

# TODO — skillAISlop

> 🔎 **Index** : Optimisations perf · Export multi-projets · Process · Prochaine vague

## Optimisations perf routeur (mesuré : route 8,5 ms, DB 2,04 Mo)

- [ ] Table `mots_cles(mot_cle, num)` indexée + requête SQL au lieu de la boucle Python sur 900 lignes (gain estimé −3 à −5 ms)
- [ ] `trigrammes` : ne stocker que les trigrammes des mots >= 5 lettres (passe floue inutile en dessous) — économise ~30-50 % de la table (0,72 Mo)
- [ ] vec0 + HNSW (index vectoriel approché) si le catalogue dépasse ~5 000 skills (inutile à 900)
- [ ] WAL checkpoint périodique si la base reste ouverte longtemps en session
- [ ] RTREE / géolocalisation de skills — écarté (pas de cas d'usage)
- [ ] stmt (vtab) — écarté (le Python suffit)
- [ ] Export JSON 100 % SQL (json_group_array) à la place du Python — si l'export grossit

## Export multi-projets (pack portable)

- [x] ~~`build --from-skills`~~ → fait : 23 fichiers skills/ synchronisés sur le sommaire, carte des domaines depuis le canvas si présent, synonymes = SYNONYMES (source unique, embarquée dans le pack) ; build canvas et --from-skills produisent des tables identiques (skills/synonymes/domaines/FTS/trigrammes)
- [x] ~~`routage.py pack`~~ → fait : zip 1,01 Mo (900 skills + routage.py + manifeste.json v12.0.0 + hash sha256 + README) + `pack --check` = test de fidélité ✅ FIDÈLE, rejoué en CI
- [x] ~~Wrappers `SKILL.md`~~ → `routage.py skillmd` génère 900 SKILL.md (frontmatter standard + metadata num/domaine/synonymes) dans data/agent-skills/ + skills.json pour `npx skills add` ; testé en CI (non bloquant), data/agent-skills/ ignoré par git
- [x] ~~`routage.py serve`~~ → fait : API loopback 127.0.0.1 (bind non-loopback refusé), /health + /route?q= (exit 0/1/2, voies/scores) + /skills + /export.json ; smoke test en CI
- [ ] Versioning sémantique du catalogue dans `meta` (ex. 12.0.0 = vague 12) pour tracer les packs exportés

## Process

- [ ] `misses --suggest` en routine hebdo (journal des exit 2 → synonymes)
- [ ] Merger les PR dès que CLEAN + CI verte (éviter l'accumulation sur la branche)
- [ ] Un commit par sujet ; `git diff --stat` + relecture avant chaque push (hook pre-push déjà en place)

## Prochaine vague

- [ ] Vague 13 (R7, janvier 2027) : re-faire la veille web, viser les vrais gaps restants plutôt que du volume

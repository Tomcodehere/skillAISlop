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

- [ ] `build --from-skills` : reconstruire skills.db depuis `skills/*.md` seuls (frontmatter), sans les canvases — réconcilier d'abord les écarts (23 noms canvas≠fichier, carte des domaines, ~48 synonymes absents des fichiers)
- [ ] `routage.py pack` : zip portable = skills/ + routage.py + manifeste JSON (version, 900 skills, hash) + README install + test de fidélité (rebuild depuis le pack, comparer hash)
- [ ] Générer des wrappers `SKILL.md` (frontmatter YAML standard Agent Skills) depuis chaque `NNN-slug.md` → interop Claude Code/Codex via `npx skills add`
- [ ] `routage.py serve` : mini API HTTP sur 127.0.0.1 uniquement (`GET /route?q=`, `/skills`, `/export.json`)
- [ ] Versioning sémantique du catalogue dans `meta` (ex. 12.0.0 = vague 12) pour tracer les packs exportés

## Process

- [ ] `misses --suggest` en routine hebdo (journal des exit 2 → synonymes)
- [ ] Merger les PR dès que CLEAN + CI verte (éviter l'accumulation sur la branche)
- [ ] Un commit par sujet ; `git diff --stat` + relecture avant chaque push (hook pre-push déjà en place)

## Prochaine vague

- [ ] Vague 13 (R7, janvier 2027) : re-faire la veille web, viser les vrais gaps restants plutôt que du volume

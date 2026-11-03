---
name: "todo-skillaislop"
title: "TODO — skillAISlop"
type: "text/markdown"
---

# TODO — skillAISlop

> 🔎 **Index** : Améliorations routeur

## Améliorations routeur

- [x] ~~Envisager une sous-commande `sonde`~~ → faite le 2026-11-01 (sous-commande `sonde` rejouable, rapport dans data/sonde-rapport.md) de couverture rejouable (batterie de sujets → rapport couverts/partiels/gaps) pour les cycles trimestriels
- [x] ~~Corriger le faux positif résiduel~~ → corrigé le 2026-11-01 (mots < 5 lettres exclus de la passe floue ; `route "IoT"` → exit 2 confirmé le 2026-11-02) détecté par re-sonde (2026-11-01) : « IoT » seul route par trigrammes vers 150/250 (« iot » ⊂ « bibliothécaire ») — exclure les mots courts (< 5 lettres) de la passe floue

## Nouvelles pistes (2026-11-02)

- [x] ~~Boucler les partiels de la sonde~~ → fait le 2026-11-02 (decks/arbitrer/trancher/tutorat/dispatcher) : 0 partiel, 971/972 couverts ; seul gap restant : « ton » seul (trop court pour le moteur de synonymes, couvert par « ton d'équipe » → 399)
- [x] ~~CI GitHub Actions~~ → en place le 2026-11-02 (.github/workflows/ci.yml : build + generate --check + lint + test + audit + sonde + compteur)
- [ ] `misses --suggest` en routine hebdo (journal des exit 2 → synonymes)

## Pistes SQLite (2026-11-02)

- [x] ~~Index secondaires domaine/branche~~ → fait (idx_skills_domaine, idx_skills_branche)
- [x] ~~Historique des versions (snapshot JSON + diff)~~ → fait (tables meta/versions, `routage.py versions`)
- [x] ~~fts5vocab~~ → fait (`routage.py vocab --limit N`)
- [x] ~~Analytics SQL des routages~~ → fait (`routage.py analytics`)
- [x] ~~PRAGMA optimize + VACUUM au build~~ → fait
- [ ] RTREE / géolocalisation de skills — écarté pour l'instant (pas de cas d'usage)
- [ ] stmt (vtab) — écarté (le Python suffit)
- [ ] Export JSON 100 % SQL (json_group_array) à la place du Python — à envisager si l'export grossit

## Optimisations (2026-11-02)

- [x] ~~Hoist norm(query) + cache mot_cle normalisés~~ → fait (chercher 8,9 → 7,9 ms)
- [x] ~~vec dim 256 → 128~~ → fait (skills_vec 1,05 → 0,53 Mo, fichier 1,76 → 1,24 Mo)
- [x] ~~k vec = top au lieu de top+vus~~ → fait
- [x] ~~PRAGMA journal_mode=WAL + cache_size=-8000~~ → fait
- [x] ~~VEC_PISTE 0.65 → 0.80 (anti-bruit : zzz repasse exit 2)~~ → fait
- [x] ~~Passe trigrammes en SQL (table trigrammes indexée, 54 k lignes)~~ → fait : 16,3 → 1,8 ms, résultats identiques à la version Python, repli auto si table absente
- [ ] vec0 avec HNSW (index vectoriel approché) si le catalogue dépasse ~5 000 skills
- [ ] WAL checkpoint périodique si la base est ouverte longtemps en session

## Process (2026-11-02)

- [ ] Merger la PR #2 dès que CLEAN + CI verte (éviter l'accumulation de commits sur la branche)
- [ ] Un commit par sujet ; tester localement (build+lint+test) AVANT push, pas corriger via la CI après
- [x] ~~Sonde bloquante en CI~~ → 100 % (958/958, 0 gap) : sujets < 4 lettres exclus de la sonde, sonde redevenue bloquante en CI
- [x] ~~Tests avant push~~ → hook .git/hooks/pre-push (build+lint+test) ; revue git diff --stat à faire à la main avant chaque push

- [ ] Vague 12 (R7, janvier) : re-faire la veille web, viser les vrais gaps restants plutôt que du volume

- [ ] Pousser la branche vibe/vague-12-900-sections et ouvrir la PR quand le rate limit GitHub/Vibe sera levé

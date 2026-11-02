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

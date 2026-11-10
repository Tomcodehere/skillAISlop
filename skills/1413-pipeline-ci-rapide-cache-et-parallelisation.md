---
num: 1413
resume: "Diviser par 2-3 le temps d'une CI en 2027 : cache des dépendances et layers Docker, jobs en parallèle (matrix), étapes ordonnées (lint d'abord, fail-fast), sans perdre de tests. Étape 1 : Mesurer le temps de chaque job pour cibler le goulot."
lang: "fr"
date_ajout: "2026-11"
nom: "Pipeline CI rapide : cache et parallelisation"
emoji: "⏩"
domaine: "Développement"
signal: "Accélérer une pipeline CI lente en 2027 : cache des dépendances (actions/cache, Docker layers), parallélisation (matrix), tests shardés, early-exit sur échec. Utilise quand la CI met 25 min. N'utilise pas pour réduire la couverture de tests."
mot_cle: "pipeline CI rapide cache parallèle matrix"
nom_court: "CI rapide"
branche: "D16"
synonymes: ["accélérer github actions", "cache dépendances CI", "jobs parallèles matrix"]
cross_refs: [508, 323, 317]
tags: ["2027"]
depends_on: [323]
---

## 1413. ⏩ Pipeline CI rapide : cache et parallelisation (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Diviser par 2-3 le temps d'une CI en 2027 : cache des dépendances et layers Docker, jobs en parallèle (matrix), étapes ordonnées (lint d'abord, fail-fast), sans perdre de tests.

**Quand l'utiliser (triggers)** :
- Notre CI met 25 minutes, comment l'accélérer ?
- Cache npm/pip/docker dans GitHub Actions
- Paralléliser les tests (matrix, shards)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es optimiseur de CI/CD. Tu donnes les recettes (actions/cache key=hash(lockfile), cache Docker, strategy.matrix, fail-fast) et tu mesures avant/après avec les timings Actions. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le workflow CI actuel et ses timings
- Les étapes lentes (install, tests, build)
- Le gestionnaire de dépendances

**Méthode** :
1. Mesurer le temps de chaque job pour cibler le goulot.
2. Cacher dépendances (hash du lockfile) et layers Docker.
3. Paralléliser : matrix versions/OS ou sharder les tests.
4. Ordonner : lint rapide d'abord avec fail-fast, tests lourds après.
5. Re-mesurer jusqu'au temps cible (< 8 min).

**Sorties attendues** :
- Le workflow CI optimisé
- Le gain mesuré avant/après
- La couverture de tests inchangée

**Exemple de prompt** :
> « Notre GitHub Actions met 25 min : optimise-la (cache, matrix, fail-fast) pour passer sous 10 min sans perdre de tests. »

**Cas d'usage** : Productivité dev, feedback rapide sur les PR. S'articule avec skills 508 (CI sécurisée), 323 (builds) et 317 (tests d'intégration).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

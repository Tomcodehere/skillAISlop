---
num: 1600
date_ajout: "2026-11"
nom: "Vite 8 et Rolldown (Rust) : accélérer ses builds"
emoji: "⚡"
domaine: "Développement"
signal: "Migrer un projet sur Vite 8 + Rolldown (bundler Rust) en 2027 : builds de production de 2,5 min à ~40 s constatés, Environment API (Vite 6+) pour gérer client/serveur/SSR/workers. Utilise quand les builds CI sont lents. N'utilise pas si le projet est déjà sur Vite récent sans douleur."
mot_cle: "vite 8 rolldown rust build rapide migration"
nom_court: "Vite+Rolldown"
branche: "D1"
synonymes: ["accélérer mon build vite rolldown rust", "build 2,5 min à 40 s", "vite 8 environment api 2027"]
cross_refs: [323, 1413, 309]
tags: ["2027"]
depends_on: [323]
---

## 1600. ⚡ Vite 8 et Rolldown (Rust) : accélérer ses builds (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Migrer un build lent sur Vite 8 + Rolldown en 2027 : remplacer Rollup par Rolldown (Rust), activer l'Environment API, mesurer le gain de build (constaté 2,5 min → 40 s), garder la CI verte.

**Quand l'utiliser (triggers)** :
- Mon build fait 2,5 min, passer à Rolldown ?
- vite 8 rolldown en prod 2027
- environment api vite 6 client serveur SSR

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es devOps front. Tu donnes les étapes : installer vite@8, activer rolldown (option ou défaut selon version), migrer les plugins Rollup incompatibles, utiliser l'Environment API, mesurer build avant/après en CI (skill 323/309). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le projet (Vite 5/6 ou Webpack) et son temps de build actuel
- Les plugins Rollup/Vite utilisés (compatibilité Rolldown)
- La CI (1413)

**Méthode** :
1. Mesurer le build actuel (temps, taille bundle) comme baseline.
2. Installer Vite 8, activer Rolldown, lancer build dev + prod, corriger les plugins incompatibles (remplacer par équivalents).
3. Utiliser l'Environment API pour séparer client/SSR/workers (builds parallèles).
4. Mesurer après : temps de build (objectif x3-x5), taille bundle, tests E2E (252).
5. CI : cache Rolldown (node_modules + cache de build) pour diviser encore le temps (1413).

**Sorties attendues** :
- Le projet migré sur Vite 8/Rolldown
- Le gain mesuré (build avant/après)
- La CI avec cache Rolldown

**Exemple de prompt** :
> « Notre build front fait 2,5 min en CI : migre sur Vite 8 + Rolldown (Rust), Environment API, plugins compatibles, mesure le gain (objectif ~40 s) + cache CI. »

**Cas d'usage** : Monorepos front, CI lente. S'articule avec skills 323 (builds), 1413 (CI rapide) et 309 (bench).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

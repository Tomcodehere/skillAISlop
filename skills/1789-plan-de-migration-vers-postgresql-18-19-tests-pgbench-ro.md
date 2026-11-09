---
num: 1789
resume: "Conduire une migration PG (ex. 16→18, ou 18→19 RC) en sécurité : pg_upgrade --check, recette identique avec tests de régression + pgbench, --swap (1787) en fenêtre, rollback = ancien cluster gardé 1 semaine. Étape 1 : pg_upgrade --check sur les deux clusters (compatibilite, extensions)."
date_ajout: "2026-11"
nom: "Plan de migration vers PostgreSQL 18/19 : tests, pgbench, rollback"
emoji: "🛠️"
domaine: "Data"
signal: "Mener une migration PG (16 vers 18 ou 18 vers 19 RC) en 2027 de maniere sûre : (1) pg_upgrade --check, (2) environnement de recette identique, tests de regression applicatifs + pgbench (workload reel), (3) pg_upgrade --swap en fenetre de maintenance (1787), (4) rollback = ancien cluster conserve 1 semaine. N'utilise pas en prod sans recette et sans rollback teste."
mot_cle: "migrer vers PG18 PG19 2027 pg_upgrade --check recette tests regression pgbench rollback plan 1 semaine"
nom_court: "Migration PG18/19"
branche: "D17"
synonymes: ["plan de migration PG16 vers PG18 : check recette pgbench swap rollback", "pg_upgrade --check avant toute montee de version", "rollback : garder l'ancien cluster 1 semaine apres le swap 1787"]
cross_refs: [1780, 1787, 1758]
tags: ["2027"]
depends_on: [1780]
---

## 1789. 🛠️ Plan de migration vers PostgreSQL 18/19 (2027) : tests, pgbench, rollback

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Conduire une migration PG (ex. 16→18, ou 18→19 RC) en sécurité : pg_upgrade --check, recette identique avec tests de régression + pgbench, --swap (1787) en fenêtre, rollback = ancien cluster gardé 1 semaine.

**Quand l'utiliser (triggers)** :
- migration PG16 vers PG18 en prod, quelle procedure ?
- tests de regression applicatifs avant le swap
- rollback teste : ancien cluster conserve combien de temps ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DBA / chef de projet technique. Tu suis le plan en 4 etapes : check, recette + pgbench, swap en fenetre (1787), rollback documente ; aucun passage en prod sans recette identique et rollback teste. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les versions cible et source
- L'environnement de recette identique
- Le workload pgbench reel

**Méthode** :
1. pg_upgrade --check sur les deux clusters (compatibilite, extensions).
2. Recette : restaurer un dump reel, lancer les tests applicatifs + pgbench (workload capture en prod), comparer perfs/erreurs.
3. Prod : fenetre de maintenance, pg_upgrade --swap (1787), verifier stats et connexions.
4. Rollback : ancien cluster conserve 1 semaine, procedure de rebascule testee en recette.

**Sorties attendues** :
- Le rapport de recette (tests OK, pgbench comparatif)
- La migration prod realisee en fenetre avec downtime mesure
- Le plan de rollback documente et teste (ancien cluster 1 semaine)

**Exemple de prompt** :
> « Migration PG16→PG18 : pg_upgrade --check OK, recette avec 2 000 req/s pgbench (p99 identique), swap en fenetre de nuit (8 s, 1787), ancien cluster PG16 garde 7 jours, rollback reteste en recette avant. »

**Cas d'usage** : Migrer sans risque. S'articule avec skills 1780, 1787, 1758, 1764 (runbooks).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

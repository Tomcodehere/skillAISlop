---
num: 1864
resume: "Orchestrer avec Dagster en asset-centric : @asset déclare les data assets et leurs dépendances, avec tests locaux (pytest), fraîcheur trackée (stale) et lineage OpenLineage (1832). Étape 1 : Définir @asset def daily_revenue(raw_orders) -supérieur à matérialise la table, dépend de raw_orders."
date_ajout: "2026-11"
nom: "Dagster : orchestration asset-centric"
emoji: "🧩"
domaine: "Data"
signal: "Modéliser les pipelines avec Dagster en pensant ASSETS (données produites), pas tâches : @asset matérialise une table/fichier/modèle avec ses dépendances en arguments ; Dagster calcule le plan d'exécution, track la fraîcheur (stale), fait du lineage (OpenLineage 1832) et des tests locaux natifs (pytest sur les assets). Footprint : webserver + daemon + Postgres (3 services vs 5+ pour Airflow). Attention : Prefect a racheté Dagster Labs (juillet) — surveiller la roadmap."
mot_cle: "Dagster @asset asset-centric matérialiser data asset dépendances fraîcheur stale lineage OpenLineage tests locaux pytest footprint"
nom_court: "Dagster"
branche: "D17"
synonymes: ["@asset Dagster : matérialiser une table avec ses dépendances en arguments", "tester un asset localement (pytest) avant de le déployer", "Dagster UI : voir quels assets sont stale (pas matérialisés à temps)"]
cross_refs: [1863, 1832, 1833]
tags: ["2027"]
depends_on: [1863]
---

## 1864. 🧩 Dagster : orchestration asset-centric

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Orchestrer avec Dagster en asset-centric : @asset déclare les data assets et leurs dépendances, avec tests locaux (pytest), fraîcheur trackée (stale) et lineage OpenLineage (1832).

**Quand l'utiliser (triggers)** :
- penser mes pipelines en assets (tables produites), pas en tâches
- tester un asset en local avant prod (pytest Dagster)
- voir dans l'UI quels assets sont en retard (stale)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer. Tu définis les @asset (fonctions qui matérialisent), leurs dépendances (arguments), les tests (pytest), et tu surveilles la fraîcheur dans l'UI Dagster. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les data assets à produire
- Les dépendances entre assets
- Postgres + webserver + daemon

**Méthode** :
1. Définir @asset def daily_revenue(raw_orders) -> matérialise la table, dépend de raw_orders.
2. Dagster calcule le plan (graphe de dépendances), schedule ou trigger manuel/sensor (1869).
3. Tests : @asset + test avec pytest (données fixtures) avant déploiement.
4. UI : fraîcheur de chaque asset (dernier materialize), stale si en retard (alerte 1835).
5. Lineage : Dagster émet OpenLineage (1832) -> Marquez (1833).

**Sorties attendues** :
- Les assets déclarés et ordonnancés
- Les tests locaux qui passent
- La fraîcheur + lineage visibles (1833)

**Exemple de prompt** :
> « Asset daily_revenue dépend de raw_orders (asset amont) : Dagster ne lance daily_revenue que quand raw_orders est matérialisé — si raw_orders est en retard (stale), alerte fraîcheur (1835), pas de calcul sur données vieilles. »

**Cas d'usage** : Data products (1837). S'articule avec skills 1863, 1832, 1833, 1835, 1837.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

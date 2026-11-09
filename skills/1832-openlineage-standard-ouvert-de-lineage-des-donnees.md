---
num: 1832
resume: "Instrumenter tous les pipelines avec OpenLineage (standard ouvert) : événements de run (start/complete/fail, inputs/outputs) émis par Airflow, dbt, Spark, Flink, Dagster, Snowflake, BigQuery. Étape 1 : Phase 1 : dbt (intégration native) — chaque modèle émet un event avec inputs/outputs."
lang: "fr"
date_ajout: "2026-11"
nom: "OpenLineage : standard ouvert de lineage des données"
emoji: "🧭"
domaine: "Data"
signal: "Instrumenter les pipelines avec OpenLineage (standard ouvert LFAI&Data, Linux Foundation) : chaque job émet des événements (start/complete/fail) avec inputs/outputs/run — collectés en temps réel par Airflow, dbt, Spark, Flink, Dagster, Snowflake, BigQuery. Indépendant du outil de visualisation (Marquez 1833, DataHub 1836). N'utilise pas un format propriétaire de lineage (vendor lock-in)."
mot_cle: "OpenLineage standard ouvert lineage événements jobs Airflow dbt Spark Flink Dagster Snowflake BigQuery LFAI Data"
nom_court: "OpenLineage"
branche: "D17"
synonymes: ["instrumenter mes pipelines avec OpenLineage (events start/complete, inputs/outputs)", "OpenLineage vs format propriétaire : standard ouvert Linux Foundation", "activer OpenLineage dans dbt/Airflow/Dagster/Spark en 2027"]
cross_refs: [1833, 1836, 1863]
tags: ["2027"]
depends_on: [1466]
---

## 1832. 🧭 OpenLineage : standard ouvert de lineage des données

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Instrumenter tous les pipelines avec OpenLineage (standard ouvert) : événements de run (start/complete/fail, inputs/outputs) émis par Airflow, dbt, Spark, Flink, Dagster, Snowflake, BigQuery.

**Quand l'utiliser (triggers)** :
- quel pipeline a produit cette table ? (lineage temps réel)
- activer OpenLineage dans dbt (natif) puis Airflow/Dagster
- OpenLineage vs DataHub propriétaire : choisir le standard ouvert

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer. Tu actives l'intégration OpenLineage de chaque outil (dbt natif, Airflow via provider, Dagster natif), tu pointes vers le collecteur (Marquez 1833), et tu vérifies les événements reçus. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les pipelines (Airflow/dbt/Spark/Dagster)
- Le collecteur OpenLineage (Marquez)
- Les entrepôts (Snowflake/BigQuery avec support OL)

**Méthode** :
1. Phase 1 : dbt (intégration native) — chaque modèle émet un event avec inputs/outputs.
2. Phase 2 : orchestrateurs (Airflow provider OL, Dagster natif).
3. Phase 3 : compute warehouse (Snowflake/BigQuery/Databricks supportent OL).
4. Vérifier dans Marquez : graphe complet, column-level lineage (1833).

**Sorties attendues** :
- Tous les pipelines émetteurs d'événements OpenLineage
- Le graphe de lineage complet dans Marquez
- Le standard ouvert adopté (pas de lock-in)

**Exemple de prompt** :
> « dbt + Airflow + Snowflake : OpenLineage activé partout — dans Marquez, la table f_orders montre ses upstream (raw_orders via dbt model stg_orders) et downstream (dashboard revenue) en temps réel. »

**Cas d'usage** : Lineage standard. S'articule avec skills 1833 (Marquez), 1836 (DataHub), 1863/1864 (orchestrateurs).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

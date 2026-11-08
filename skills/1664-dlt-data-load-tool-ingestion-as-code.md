---
num: 1664
date_ajout: "2026-11"
nom: "dlt (data load tool) : ingestion as code"
emoji: "📥"
domaine: "Data"
signal: "Ingérer des données en 2027 avec dlt (data load tool, open source) : pipelines déclaratifs en Python (REST API, Salesforce, Google Analytics → destination DuckDB 1660, BigQuery, Snowflake, Postgres), gestion du schéma (évolution auto 1461), incremental (last_value), normalisation. Alternative à Airbyte (1665? non 1460) pour le code-first. N'utilise pas pour du streaming temps réel (Kafka 1464)."
mot_cle: "dlt data load tool ingestion as code Python REST API vers DuckDB BigQuery Snowflake incremental 2027"
nom_court: "dlt ingestion"
branche: "D15"
synonymes: ["pipeline d'ingestion en Python déclaratif (dlt)", "REST API → DuckDB en 20 lignes (dlt)", "incremental (last_value) + schéma qui évolue auto (1461)"]
cross_refs: [1460, 1660, 1461]
tags: ["2027"]
depends_on: [1660]
---

## 1664. 📥 dlt (data load tool) : ingestion as code (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ingérer des données en 2027 avec dlt (open source) : pipelines déclaratifs Python (sources: REST API, SaaS, BDD) vers DuckDB (1660)/BigQuery/Snowflake/Postgres, schéma géré automatiquement (évolution 1461), chargement incremental (last_value), normalisation.

**Quand l'utiliser (triggers)** :
- ingérer l'API Salesforce dans BigQuery sans écrire d'ETL
- dlt : 20 lignes de Python pour charger une API REST
- schéma qui change en amont : dlt s'adapte (1461)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer. Tu écris : @dlt.source avec resource (endpoint paginé), dlt.pipeline(destination='duckdb'/'bigquery', dataset), run, et dlt gère le schéma (normalise, ajoute colonnes, versionne le dataset). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La source (API REST/SaaS, BDD, fichiers)
- La destination (DuckDB 1660, BigQuery, Snowflake, Postgres)
- Le mode (full, incremental last_value, merge)

**Méthode** :
1. Installer dlt, définir la source : @dlt.resource def ma_source(): yield from api_paginated(...).
2. Pipeline : dlt.pipeline(pipeline_name, destination='duckdb', dataset_name='raw'), pipeline.run(ma_source()).
3. Schéma : dlt détecte et fait évoluer le schéma (nouvelles colonnes ajoutées, types inférés), historise les versions (1461).
4. Incremental : @dlt.resource(..., incremental=dlt.dsl.Incremental('updated_at', initial_value=...)) → ne recharge que le nouveau.
5. Orchestrer : Airflow/Dagster (1460) appelle pipeline.run(), alertes qualité (1677).

**Sorties attendues** :
- Le pipeline dlt fonctionnel (source → destination)
- Le schéma auto-géré + versionné (évolution 1461)
- Le chargement incremental testé (seul le delta est chargé)

**Exemple de prompt** :
> « Ingérer l'API REST de notre CRM (paginée) dans DuckDB (1660) en 20 lignes de Python avec dlt : schéma auto (évolution 1461), incremental (updated_at), puis orchestrer dans Airflow (1460). »

**Cas d'usage** : Ingestion SaaS/API vers lakehouse. S'articule avec skills 1460 (orchestration), 1660 (DuckDB) et 1461 (drift).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

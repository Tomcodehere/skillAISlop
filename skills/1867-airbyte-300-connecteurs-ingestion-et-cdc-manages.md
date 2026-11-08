---
num: 1867
date_ajout: "2026-11"
nom: "Airbyte : 300+ connecteurs, ingestion et CDC managés"
emoji: "🌬️"
domaine: "Data"
signal: "Utiliser Airbyte pour l'ingestion de données : 300+ connecteurs (SaaS, BDD, APIs, fichiers), mode batch ou CDC (embarque Debezium 1866), 600+ sur la marketplace cloud, UI simple, open source (self-host) ou Cloud managé. Intégrations natives Airflow/Dagster (syncs = assets 1864). N'utilise pas un connecteur custom quand un natif existe."
mot_cle: "Airbyte 300+ connecteurs ingestion CDC Debezium embarqué open source Cloud marketplace Airflow Dagster assets 1866"
nom_court: "Airbyte"
branche: "D17"
synonymes: ["ingérer Salesforce/Postgres/S3 dans le warehouse : Airbyte (300+ connecteurs)", "Airbyte self-host vs Cloud : OSS ou managé", "Airbyte + Dagster : les syncs Airbyte deviennent des assets (1864)"]
cross_refs: [1866, 1863, 1864]
tags: ["2027"]
depends_on: [1866]
---

## 1867. 🌬️ Airbyte : 300+ connecteurs, ingestion et CDC managés

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ingerer des données avec Airbyte (300+ connecteurs, batch ou CDC via Debezium embarqué, self-host OSS ou Cloud) et brancher les syncs comme assets Airflow/Dagster (1863/1864).

**Quand l'utiliser (triggers)** :
- connecter Salesforce + Postgres + S3 au warehouse en 1 après-midi (Airbyte)
- mode CDC Airbyte (Debezium embarqué) vs batch
- Airbyte OSS self-host vs Cloud : lequel selon l'équipe

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer. Tu choisis les connecteurs natifs (jamais custom si natif existe), tu configures batch vs CDC (1866), et tu branches la sync comme asset Dagster (1864) ou tâche Airflow (1863). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les sources (SaaS/BDD/fichiers)
- La destination (warehouse/lake)
- Airbyte OSS (docker) ou Cloud

**Méthode** :
1. Déployer Airbyte (docker OSS ou Cloud), configurer source + destination + connexion (batch/CDC 1866).
2. Tester la connexion, lancer la première sync, vérifier dans la destination.
3. Brancher : asset Dagster @asset def airbyte_sync() déclenche l'API Airbyte (1864).
4. Monitoring : statut des syncs (UI + alerte échec 1761), latence (1835).

**Sorties attendues** :
- Les connexions actives (sources -> destination)
- Les syncs branchés comme assets (1864)
- Le monitoring des syncs (échecs alertés)

**Exemple de prompt** :
> « 3 sources (Salesforce, Postgres CDC 1866, S3) -> Snowflake via Airbyte OSS self-host : 3 connexions configurées en 1 après-midi, syncs Dagster assets suivis dans le graphe de lineage (1832/1833). »

**Cas d'usage** : Ingestion rapide. S'articule avec skills 1866, 1863, 1864, 1869.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

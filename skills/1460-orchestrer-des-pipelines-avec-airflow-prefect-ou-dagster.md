---
num: 1460
resume: "Choisir et déployer un orchestrateur de pipelines data en 2027 (Airflow, Prefect ou Dagster) : DAGs versionnés, retries, alertes, monitoring, et tests des transformations. Étape 1 : Lister les pipelines existants et leurs dépendances."
lang: "fr"
date_ajout: "2026-11"
nom: "Orchestrer des pipelines avec Airflow, Prefect ou Dagster"
emoji: "🎠"
domaine: "Data"
signal: "Choisir et déployer un orchestrateur de pipelines data en 2027 : Apache Airflow (mature, scheduler central), Prefect (Python moderne, flows), Dagster (assets, data-aware, tests). Critères : taille équipe, complexité, monitoring, coûts. Utilise quand des pipelines ETL grandissent. N'utilise pas pour un simple cron."
mot_cle: "airflow prefect dagster orchestrateur pipelines data"
nom_court: "Orchestrateur"
branche: "D15"
synonymes: ["airflow ou prefect choisir 2027", "dagster assets data-aware", "orchestrer ETL complexe"]
cross_refs: [94, 1121, 1461]
tags: ["2027"]
depends_on: [94]
---

## 1460. 🎠 Orchestrer des pipelines avec Airflow, Prefect ou Dagster (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir et déployer un orchestrateur de pipelines data en 2027 (Airflow, Prefect ou Dagster) : DAGs versionnés, retries, alertes, monitoring, et tests des transformations.

**Quand l'utiliser (triggers)** :
- Nos scripts cron data sont un bazar
- Airflow vs Prefect vs Dagster en 2027
- Orchestrer 50 pipelines ETL proprement

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de pipelines data. Tu compares les 3 orchestrateurs (Airflow mature/communautaire, Prefect pythonique moderne, Dagster orienté assets avec tests intégrés) et tu donnes les critères de choix selon l'équipe. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les pipelines existants (scripts, cron, dbt)
- La taille de l'équipe data
- Les besoins (monitoring, alertes, data quality)

**Méthode** :
1. Lister les pipelines existants et leurs dépendances.
2. Comparer Airflow/Prefect/Dagster sur : courbe d'apprentissage, monitoring, tests, coût hébergement.
3. Choisir 1 orchestrateur et migrer par vagues (critiques d'abord).
4. Versionner les DAGs dans Git + CI (lint, tests unitaires des transformations).
5. Configurer retries, alertes Slack/email, et dashboard de suivi.

**Sorties attendues** :
- L'orchestrateur choisi et déployé
- Les DAGs migrés et versionnés
- Le monitoring + alertes en place

**Exemple de prompt** :
> « On a 40 scripts cron data ingérables : choisis un orchestrateur (Airflow/Prefect/Dagster) et migre les pipelines critiques avec monitoring et alertes. »

**Cas d'usage** : Fiabilisation des pipelines, data engineering professionnel. S'articule avec skills 94 (pipelines), 1121 (ETL) et 1461 (schema drift).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

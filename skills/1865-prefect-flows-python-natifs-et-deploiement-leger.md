---
num: 1865
resume: "Orchestrer avec Prefect en Python natif (@flow/@task, retries, caching, branchements dynamiques) — déploiement Prefect Cloud ou self-host — en évaluant le risque de l'acquisition de Dagster Labs. Étape 1 : @task(retries=3, cache_key_fn=...) et @flow : le code Python est le workflow."
date_ajout: "2026-11"
nom: "Prefect : flows Python natifs et déploiement léger"
emoji: "🌊"
domaine: "Data"
signal: "Orchestrer avec Prefect en Python natif : @flow et @task (décorateurs), pas de fichier DAG séparé — le code EST le workflow, avec retries, caching, branching dynamique. Déploiement : Prefect Cloud (managé, ~50 $/M actions) ou self-host (worker + serveur). Idéal pour les équipes Python-heavy qui trouvent Airflow lourd. Attention : Prefect a racheté Dagster Labs (juillet) — évaluer le risque roadmap avant nouveau projet (1863)."
mot_cle: "Prefect @flow @task Python natif workflow code retries caching Prefect Cloud worker self-host rachat Dagster Labs juillet"
nom_court: "Prefect"
branche: "D17"
synonymes: ["@flow @task Prefect : le pipeline en pur Python (pas de DAG YAML)", "Prefect Cloud vs self-host (worker + serveur) : coût à l'usage ~50 $/M actions", "Prefect rachète Dagster Labs : évaluer le risque avant nouveau projet"]
cross_refs: [1863, 1864, 1869]
tags: ["2027"]
depends_on: [1863]
---

## 1865. 🌊 Prefect : flows Python natifs et déploiement léger

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Orchestrer avec Prefect en Python natif (@flow/@task, retries, caching, branchements dynamiques) — déploiement Prefect Cloud ou self-host — en évaluant le risque de l'acquisition de Dagster Labs.

**Quand l'utiliser (triggers)** :
- on veut du Python pur pour les pipelines (pas de YAML DAG)
- Prefect Cloud à l'usage vs self-host : comparer les coûts
- retries automatiques + cache de résultats de tâches (évite les re-calculs)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer / dev Python. Tu écris les flows (@flow) et tasks (@task avec retries/caching), tu déploies sur Prefect Cloud ou self-host, et tu documentes le risque acquisition Dagster (1863 ADR). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Python + prefect installé
- Prefect Cloud (clé API) ou serveur self-host
- Les tâches à orchestrer

**Méthode** :
1. @task(retries=3, cache_key_fn=...) et @flow : le code Python est le workflow.
2. Déployer : prefect deploy (Cloud) ou worker self-host pointant sur le serveur.
3. Monitoring : Prefect UI (flow runs, traces, échecs) + alertes (1761).
4. Coût : suivre les actions (Cloud à l'usage) vs footprint self-host.

**Sorties attendues** :
- Les flows déployés (Cloud ou self-host)
- Les retries/caching actifs
- Le dashboard des flow runs

**Exemple de prompt** :
> « Flow ETL quotidien : @flow etl() appelle @task extract(retries=3), transform(cache 24h), load — si extract échoue 3x, alerte (1761) ; si transform déjà calculé aujourd'hui (cache), skip -> -40 % de temps. »

**Cas d'usage** : Python-heavy. S'articule avec skills 1863, 1864, 1869, 1413.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

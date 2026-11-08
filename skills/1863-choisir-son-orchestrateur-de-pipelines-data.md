---
num: 1863
date_ajout: "2026-11"
nom: "Choisir son orchestrateur de pipelines data"
emoji: "🎭"
domaine: "Data"
signal: "Choisir l'orchestrateur en 2027 : Apache Airflow 3.2 (asset partitioning, le plus safe/écosystème) vs Dagster (@asset, asset-centric, tests locaux) vs Prefect (@flow/@task Python natif — a racheté Dagster Labs le 13 juillet, les deux produits continuent) vs Temporal (workflows durables long-running, pour agents IA) vs Kestra. Critères : modèle (DAG vs assets vs code), hébergement (self vs cloud), coût (Airflow = 5 processus mini, Prefect Cloud = à l'usage). N'utilise pas 3 orchestrateurs en même temps."
mot_cle: "choisir orchestrateur data Airflow 3.2 Dagster Prefect Temporal Kestra asset-centric DAG Prefect rachète Dagster juillet comparaison"
nom_court: "Choisir orchestrateur"
branche: "D17"
synonymes: ["Airflow 3.2 vs Dagster vs Prefect en 2027 : lequel choisir", "Prefect a racheté Dagster Labs (13 juillet) : les deux continuent, risque roadmap", "Temporal pour les workflows long-running des agents IA (durable execution)"]
cross_refs: [1864, 1865, 1868]
tags: ["2027"]
depends_on: [1460]
---

## 1863. 🎭 Choisir son orchestrateur de pipelines data

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir son orchestrateur de pipelines en 2027 : Airflow 3.2 (DAG, écosystème), Dagster (assets), Prefect (Python natif), Temporal (durable, agents IA), Kestra — selon modèle, hébergement et coût.

**Quand l'utiliser (triggers)** :
- on a Airflow 2 qui rame : migrer vers quoi en 2027 ?
- Dagster asset-centric pour penser en data products (1837)
- Temporal pour un agent IA qui tourne des heures (durable execution 1868)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte data / plateforme. Tu compares sur 4 axes (modèle de programmation, ops/footprint, coût, écosystème) et tu standardises sur UN orchestrateur par équipe, documenté dans l'ADR. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les pipelines existants
- Les besoins (batch vs long-running)
- Le budget hébergement

**Méthode** :
1. Airflow 3.2 : DAG déclaratifs, asset partitioning, mais 5+ processus en self-host (scheduler, webserver, workers...).
2. Dagster : @asset, tests locaux natifs, lineage intégré (1832), footprint 3 services.
3. Prefect : @flow/@task pur Python, déploiement léger, Prefect Cloud à l'usage (~50 $/M actions).
4. Temporal : durable execution, retries long terme, heartbeats — pour agents IA (1868).
5. Décision ADR + migration progressive (pas tout en même temps).

**Sorties attendues** :
- L'orchestrateur choisi (ADR) et déployé
- La comparaison documentée (4 axes)
- Le plan de migration si changement

**Exemple de prompt** :
> « Équipe data produit : Dagster choisi (assets = data products 1837, tests locaux) ; équipe agents IA : Temporal (workflows de plusieurs heures avec retries) — 2 orchestrateurs, 2 cas d'usage clairs, pas de chevauchement. »

**Cas d'usage** : Standardiser l'orchestration. S'articule avec skills 1864, 1865, 1868, 1869, 1832.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

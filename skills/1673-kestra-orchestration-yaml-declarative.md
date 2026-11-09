---
num: 1673
resume: "Orchestrer des pipelines en 2027 avec Kestra (YAML déclaratif, UI visuelle, triggers riches : schedule, webhook, fichier arrivé, event Kafka 1464) — plus accessible qu'Airflow (Python) pour les équipes mixtes data/métier. Étape 1 : Installer Kestra (docker self-hosted ou cloud), créer un namespace par projet."
date_ajout: "2026-11"
nom: "Kestra : orchestration YAML declarative"
emoji: "🧪"
domaine: "Data"
signal: "Orchestrer des pipelines en 2027 avec Kestra (open source, YAML déclaratif, UI visuelle, triggers variés : schedule, webhook, fichier, event Kafka 1464) plutôt qu'Airflow (Python lourd) pour les équipes mixtes data/métier. Utilise pour des pipelines moyens avec beaucoup de triggers. N'utilise pas pour du ML lourd (1193)."
mot_cle: "kestra orchestration YAML déclaratif UI visuelle triggers webhook schedule fichier 2027"
nom_court: "Kestra"
branche: "D15"
synonymes: ["orchestrer en YAML sans coder (Kestra) vs Airflow Python", "trigger webhook + schedule + fichier dans Kestra", "UI visuelle des exécutions (Kestra) 2027"]
cross_refs: [1460, 1464, 1675]
tags: ["2027"]
depends_on: [1460]
---

## 1673. 🧪 Kestra : orchestration YAML declarative (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Orchestrer des pipelines en 2027 avec Kestra (YAML déclaratif, UI visuelle, triggers riches : schedule, webhook, fichier arrivé, event Kafka 1464) — plus accessible qu'Airflow (Python) pour les équipes mixtes data/métier.

**Quand l'utiliser (triggers)** :
- mes pipelines sont des DAGs Airflow que personne ne comprend
- Kestra : un YAML par flow + UI de suivi visuelle
- trigger 'fichier arrivé sur S3' → lancer le traitement

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data platform engineer. Tu écris un flow Kestra en YAML (id, triggers, tasks avec inputs/outputs), tu le versionne dans Git, l'UI montre les exécutions (gantt, logs, retry), et tu branches alertes (1417). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les pipelines à orchestrer (dlt 1664, dbt 350, scripts)
- Les triggers (schedule, webhook, fichier, Kafka 1464)
- L'équipe (data + métier)

**Méthode** :
1. Installer Kestra (docker self-hosted ou cloud), créer un namespace par projet.
2. Flow YAML : triggers (schedule cron, webhook, io.kestra.plugin.fs...), tasks (scripts, dlt, dbt, HTTP), dépendances implicites.
3. UI : exécutions en temps réel (gantt, logs par task), retry manuel/auto, métriques (durée, succès).
4. Versionner les flows dans Git, déploiement via CI (1592) ou l'UI (moins bien).
5. Alertes : tâche en échec → Slack (1417), SLA de complétion par flow.

**Sorties attendues** :
- Les flows Kestra en YAML versionnés (Git) et exécutés
- L'UI de suivi des exécutions (gantt, logs, retry)
- Les alertes d'échec (1417) branchées

**Exemple de prompt** :
> « Nos DAGs Airflow sont illisibles pour les métiers : migre vers Kestra (flows YAML versionnés Git, triggers webhook/fichier/Kafka 1464, UI visuelle des exécutions, alertes Slack 1417). »

**Cas d'usage** : Pipelines moyens, équipes mixtes. S'articule avec skills 1460 (orchestrateurs), 1464 (Kafka) et 1675 (comparatif).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1869
date_ajout: "2026-11"
nom: "Pipelines event-driven : déclencher sur événement, pas sur cron"
emoji: "📨"
domaine: "Data"
signal: "Passer des pipelines cron (toutes les heures 'au cas où') aux pipelines event-driven : déclenchement sur événement réel (fichier arrivé en S3, message Kafka, webhook, asset amont matérialisé — Airflow 3.2 asset events, Dagster sensors 1864). Gain : fraîcheur meilleure, moins de runs vides (coût), données toujours à jour. N'utilise pas le cron seul pour les données temps réel (CDC 1866 + events)."
mot_cle: "pipelines event-driven capteurs sensors Airflow 3.2 asset events Dagster déclenchement sur événement S3 Kafka webhook pas de cron"
nom_court: "Event-driven"
branche: "D17"
synonymes: ["déclencher le pipeline quand le fichier arrive en S3 (sensor/event), pas toutes les heures en cron", "Airflow 3.2 asset events : un DAG se déclenche quand l'asset amont est prêt", "moins de runs vides : event-driven vs cron (coût + fraîcheur)"]
cross_refs: [1863, 1864, 1866]
tags: ["2027"]
depends_on: [1863]
---

## 1869. 📨 Pipelines event-driven : déclencher sur événement, pas sur cron

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Passer les pipelines du cron à l'event-driven : capteurs/sensors (fichier S3, message Kafka, webhook, asset amont matérialisé — Airflow 3.2 asset events, Dagster sensors) — meilleure fraîcheur, moins de runs vides.

**Quand l'utiliser (triggers)** :
- mon pipeline tourne toutes les heures mais les données arrivent à 14h37 : passer en event-driven
- Dagster sensor : se déclencher quand l'asset upstream est matérialisé
- Airflow 3.2 : asset-triggered DAG (dataset/event) au lieu du cron

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer. Tu remplaces les schedule cron par des sensors/events (S3, Kafka, DB, asset upstream), avec un fallback cron de sécurité (ex. toutes les 6 h si aucun event). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les sources d'événements (S3, Kafka, webhook, assets)
- L'orchestrateur (1863)
- Le fallback cron de sécurité

**Méthode** :
1. Identifier les vraies sources d'événements : arrivée fichier S3 (S3 event -> SQS -> sensor), topic Kafka, webhook SaaS, asset amont (Dagster sensor / Airflow 3.2 asset event).
2. Configurer le sensor/event-driven trigger + garder un cron de secours (ex. 6 h) si l'event rate.
3. Mesurer : latence event->run (objectif < 5 min) vs cron (jusqu'à 1 h), nombre de runs vides évités (coût).
4. Fraîcheur SLA (1835) améliorée automatiquement.

**Sorties attendues** :
- Les pipelines event-driven actifs
- Le fallback cron de sécurité
- Le gain mesuré (latence, runs vides évités)

**Exemple de prompt** :
> « Pipeline 'nouvelles commandes' : avant cron 1 h (données jusqu'à 59 min de retard, 20 runs vides/jour) ; après event S3 (fichier reçu) -> run en 2 min, 0 run vide — fraîcheur SLA 1835 passée de 1 h à 5 min. »

**Cas d'usage** : Fraîcheur + coût. S'articule avec skills 1863, 1864, 1866, 1835.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

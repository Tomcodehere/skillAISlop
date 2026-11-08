---
num: 1873
date_ajout: "2026-11"
nom: "KEDA : autoscaling event-driven (Kafka, queues, cron, métriques)"
emoji: "📈"
domaine: "Développement"
signal: "Scaler les pods au-delà du HPA CPU/mémoire avec KEDA : scalers sur longueur de file Kafka/ RabbitMQ/SQS, lag consumer, cron (ScheduledJob), métriques Prometheus custom (1416), etc. Scale to zero quand la file est vide (économie). TriggerAuthentication pour les credentials (via ESO 1854). N'utilise pas le HPA seul pour des workloads event-driven (files)."
mot_cle: "KEDA autoscaling event-driven scaler Kafka RabbitMQ SQS lag cron ScheduledJob Prometheus scale to zero TriggerAuthentication ESO"
nom_court: "KEDA"
branche: "D16"
synonymes: ["scaler les consumers Kafka selon le lag (KEDA), pas selon le CPU", "scale to zero quand la file est vide (KEDA) : économie de nœuds", "ScheduledJob KEDA : cron au niveau k8s (scale 0 la nuit)"]
cross_refs: [1810, 1416, 1854]
tags: ["2027"]
depends_on: [609]
---

## 1873. 📈 KEDA : autoscaling event-driven (Kafka, queues, cron, métriques)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Scaler les workloads event-driven avec KEDA (lag Kafka/queues, cron ScheduledJob, métriques Prometheus) au-delà du HPA — jusqu'au scale-to-zero quand la file est vide.

**Quand l'utiliser (triggers)** :
- mes consumers Kafka sont à 2 pods la nuit pour 0 message : scale to zero (KEDA)
- scaler selon le lag du topic Kafka, pas le CPU
- ScheduledJob : scale 0 à 22 h, scale 5 à 8 h (cron k8s)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / ingénieur plateforme. Tu installes KEDA, tu déclares un ScaledObject par workload (trigger + min/max replicas), et les credentials du trigger via TriggerAuthentication + ESO (1854). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- KEDA installé (helm)
- Les sources d'événements (Kafka, SQS...)
- Les credentials (Vault/ESO 1854)

**Méthode** :
1. Installer KEDA (helm) + CRDs (ScaledObject, TriggerAuthentication).
2. ScaledObject : trigger kafka (lag threshold 100), minReplicaCount 0, maxReplicaCount 20.
3. TriggerAuthentication : secretRef (créé via ESO 1854 depuis Vault).
4. ScheduledJob pour le cron (scale 0 nuit).
5. Métriques : keda metrics (1416), coût économisé scale-to-zero (1862).

**Sorties attendues** :
- Les ScaledObject actifs (scale auto selon les events)
- Le scale-to-zero la nuit (coût -70 % sur ces workloads)
- Les métriques KEDA dans Grafana 1416

**Exemple de prompt** :
> « Consumers Kafka 'events' : ScaledObject lag>100 -> scale up (max 20), file vide -> scale to 0 la nuit + ScheduledJob 8h -> 5 replicas. Économie mesurée : -70 % de nœuds sur ce workload (1862). »

**Cas d'usage** : Event-driven scaling. S'articule avec skills 1810 (Karpenter), 1416, 1854, 609, 1862.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

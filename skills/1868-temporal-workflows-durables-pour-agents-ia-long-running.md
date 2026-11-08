---
num: 1868
date_ajout: "2026-11"
nom: "Temporal : workflows durables pour agents IA long-running"
emoji: "⏳"
domaine: "Développement"
signal: "Utiliser Temporal pour les workflows qui durent des heures/jours (agents IA, processus métier) : durable execution (l'état persiste, reprise après crash), retries avec backoff, heartbeats (détection worker mort), timers, signaux. Contrairement à un orchestrateur batch (1863), Temporal survit aux pannes et garde le contexte. N'utilise pas pour du batch cron simple (overkill)."
mot_cle: "Temporal durable execution workflow long-running agents IA reprise après crash retries backoff heartbeats timers signaux état persistant"
nom_court: "Temporal"
branche: "D16"
synonymes: ["mon agent IA tourne 6 h et crash à 5 h — tout perdu : Temporal (durable execution)", "Temporal vs Airflow/Dagster : quand l'utiliser (long-running, crash-safe)", "heartbeat Temporal : détecter qu'un worker est mort et reprendre ailleurs"]
cross_refs: [1863, 1850, 1765]
tags: ["2027"]
depends_on: [1863]
---

## 1868. ⏳ Temporal : workflows durables pour agents IA long-running

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Orchestrer les workflows long-running (agents IA, processus métier) avec Temporal : durable execution (reprise après crash), retries/timers/signaux/heartbeats — l'état persiste entre les exécutions.

**Quand l'utiliser (triggers)** :
- agent IA de 6 h qui crash : reprendre là où il en était (Temporal)
- workflow métier avec étapes humaines (attente approbation) : timers + signaux
- Temporal self-host vs Cloud : choisir

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur backend / plateforme IA. Tu modélises le workflow en code (activities = étapes, workflow = orchestration), avec retries et heartbeats, et tu déploies Temporal (self-host ou Cloud). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Temporal server (self-host ou Cloud)
- Le code du workflow (SDK Python/TS/Go/Java)
- Les activités (appels LLM 1800, BDD...)

**Méthode** :
1. Modéliser : @workflow (orchestration) + @activity (étapes, retries, timeout, heartbeat).
2. Durable execution : si le worker crash, le workflow reprend à la dernière activité terminée (état persisté côté serveur).
3. Signaux/timers : attendre une approbation humaine (signal) ou un délai (timer) sans bloquer.
4. Monitoring : Web UI Temporal (workflow history, retries, échecs).

**Sorties attendues** :
- Les workflows long-running déployés (crash-safe)
- L'historique des exécutions (replay/debug)
- Les alertes sur échecs (1761)

**Exemple de prompt** :
> « Agent de recherche IA (6 h, 50 appels LLM via gateway 1800) : workflow Temporal avec retries sur chaque appel — crash du worker à 5 h -> reprise automatique au 43e appel, pas de restart from scratch. »

**Cas d'usage** : Durable execution. S'articule avec skills 1863, 1850, 1765, 1800.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

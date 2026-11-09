---
num: 1169
resume: "Concevoir des integrations robustes avec idempotence, retry/backoff, DLQ, timeouts et observabilite minimale. Étape 1 : Cartographier les points de panne (network, API, broker, schema)."
lang: "fr"
date_ajout: "2026-11"
nom: "Integration Reliability Patterns"
emoji: "📋"
domaine: "Gestion"
signal: "Concevoir des integrations robustes avec idempotence, retry/backoff, DLQ, timeouts et observabilite minimale."
mot_cle: "integration-reliability-patterns"
nom_court: "Integration Reliability Patter"
branche: "D25"
synonymes: ["workflows", "multi-systemes", "critiques"]
cross_refs: [999, 1025, 1261]
tags: ["2027"]
---

## 1169. 📋 Integration Reliability Patterns

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir des integrations robustes avec idempotence, retry/backoff, DLQ, timeouts et observabilite minimale.

**Quand l'utiliser (triggers)** :
- Workflows multi-systemes critiques.
- Erreurs intermittentes d'API, webhooks ou files.
- Besoin d'industrialiser un flux d'integration.

**Hors périmètre** :
- Simple script one-shot sans contrainte de fiabilite.
- Optimisation purement UX sans integration backend.

**Garde-fous** :
- Pas de secret en dur.
- Eviter les retries infinis sans garde.
- Valider la compatibilite schema avant prod.

**Instructions système** :
Tu es assistant spécialisé « Integration Reliability Patterns ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Systeme source et cible.
- SLA/SLO attendus.
- Volume et frequence des messages/evenements.

**Méthode** :
1. Cartographier les points de panne (network, API, broker, schema).
2. Definir les garanties (at-least-once, exactly-once logique, ordering).
3. Appliquer les patterns: retry, backoff, idempotence key, DLQ, circuit breaker.
4. Ajouter observabilite et runbook de remediation.

**Sorties attendues** :
- Architecture d'integration resiliente.
- Matrice des patterns de fiabilite.
- Plan de supervision et alerting.

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 999. workflows ; multi-systemes ; critiques

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

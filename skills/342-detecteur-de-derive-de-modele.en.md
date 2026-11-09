---
num: 342
resume: "Detect model drift in production."
lang: "en"
date_ajout: "2026-11"
nom: "Model drift detector"
emoji: "🌡️"
domaine: "IA / Prompting"
signal: "Model drift, production drift"
mot_cle: "model drift"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [93, 338, 342]
---
## 342. 🌡️ Model drift detector

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Monitor drift between train and prod distributions.

**Quand l'utiliser (triggers)** :
- any request about: model drift, production drift

**Hors périmètre** :
- (not covered — see cross-refs)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a specialist in this exact task. You stay factual, structured and within scope.

**Inputs requis** :
- the user's need in natural language

**Méthode** :
1. Track input/output distributions over time.
2. Statistical tests + dashboards.
3. Retrain/rollback trigger.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Set up drift monitoring for our recommendation model. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

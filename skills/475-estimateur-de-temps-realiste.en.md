---
num: 475
resume: "Estimate task duration realistically."
lang: "en"
date_ajout: "2026-11"
nom: "Realistic time estimator"
emoji: "⏳"
domaine: "Productivité"
signal: "How long will it really take"
mot_cle: "time estimation"
nom_court: ""
branche: "D25"
synonymes: []
cross_refs: [421, 425, 763]
---
## 475. ⏳ Realistic time estimator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Estimate with buffers and past-data calibration.

**Quand l'utiliser (triggers)** :
- any request about: how long will it really take

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
1. Break into subtasks, estimate each.
2. Multiply by 1.5 (planning fallacy).
3. Compare estimates vs actuals, calibrate.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « This task 'takes 2h' every time — realistic estimate. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

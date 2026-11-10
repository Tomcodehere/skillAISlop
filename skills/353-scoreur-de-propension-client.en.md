---
num: 353
resume: "Build a propensity-to-buy score."
lang: "en"
date_ajout: "2026-11"
nom: "Customer propensity scorer"
emoji: "🎯"
domaine: "Data"
signal: "Propensity score, purchase probability"
mot_cle: "propensity scoring"
nom_court: ""
branche: "D17"
synonymes: []
cross_refs: [93, 111, 373]
---
## 353. 🎯 Customer propensity scorer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Score customers by purchase propensity.

**Quand l'utiliser (triggers)** :
- any request about: propensity score, purchase probability

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
1. Label: bought within 30d.
2. Model + calibration (probabilities, not ranks).
3. Use in CRM: prioritise outreach.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Propensity score for our e-commerce customers. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

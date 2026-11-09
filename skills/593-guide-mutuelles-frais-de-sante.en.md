---
num: 593
resume: "Choose and use health insurance well."
lang: "en"
date_ajout: "2026-11"
nom: "Health insurance & costs guide"
emoji: "🏥"
domaine: "Personnel"
signal: "Mutuelle, health reimbursements, medical costs, coverage choice"
mot_cle: "health insurance"
nom_court: ""
branche: "D27"
synonymes: []
cross_refs: [137, 485, 1333]
---
## 593. 🏥 Health insurance & costs guide

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Pick a mutuelle and get reimbursed fast.

**Quand l'utiliser (triggers)** :
- any request about: mutuelle, health reimbursements, medical costs, coverage choice

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
1. Compare coverage vs price + network.
2. Carte Vitale + mutuelle sync (tiers payant).
3. 100% coverage categories.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Which mutuelle for a family of 4? » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

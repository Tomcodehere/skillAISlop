---
num: 827
resume: "Handle unpaid rent as a landlord."
lang: "en"
date_ajout: "2026-11"
nom: "Unpaid rent (landlord side)"
emoji: "🔑"
domaine: "Juridique"
signal: "Tenant not paying rent, landlord steps"
mot_cle: "unpaid rent"
nom_court: ""
branche: "D29"
synonymes: []
cross_refs: [554, 371, 683]
---
## 827. 🔑 Unpaid rent (landlord side)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Formal notice -> payment order -> eviction if needed (not legal advice).

**Quand l'utiliser (triggers)** :
- any request about: tenant not paying rent, landlord steps

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
1. Written reminders with proof.
2. Mise en demeure via bailiff.
3. Legal route if still unpaid.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Tenant 2 months late — steps. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

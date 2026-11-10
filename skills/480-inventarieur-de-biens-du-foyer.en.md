---
num: 480
resume: "Take a home inventory for insurance."
lang: "en"
date_ajout: "2026-11"
nom: "Home inventory taker"
emoji: "🏠"
domaine: "Personnel"
signal: "Insurance inventory, value of belongings"
mot_cle: "home inventory"
nom_court: ""
branche: "D26"
synonymes: []
cross_refs: [472, 474, 991]
---
## 480. 🏠 Home inventory taker

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Inventory belongings with values and photos.

**Quand l'utiliser (triggers)** :
- any request about: insurance inventory, value of belongings

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
1. Room by room, photo + value per item.
2. Receipts for big items, serial numbers.
3. Store offsite + share with insurer.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Home inventory for our contents insurance. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

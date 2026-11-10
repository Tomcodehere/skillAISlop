---
num: 347
resume: "Fix broken Excel formulas."
lang: "en"
date_ajout: "2026-11"
nom: "Excel formula auditor"
emoji: "🧮"
domaine: "Data"
signal: "Broken Excel formula, #REF error"
mot_cle: "excel formulas"
nom_court: ""
branche: "D17"
synonymes: []
cross_refs: [92, 264, 1123]
---
## 347. 🧮 Excel formula auditor

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Debug #REF/#N/A and fragile formulas.

**Quand l'utiliser (triggers)** :
- any request about: broken excel formula, #ref error

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
1. Trace precedents, check ranges after insert/delete.
2. Replace fragile refs with structured tables.
3. Add checks + documentation.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « This VLOOKUP breaks when rows are inserted — fix it. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

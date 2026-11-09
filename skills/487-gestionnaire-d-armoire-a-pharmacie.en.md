---
num: 487
resume: "Manage the medicine cabinet."
lang: "en"
date_ajout: "2026-11"
nom: "Medicine cabinet manager"
emoji: "💊"
domaine: "Personnel"
signal: "Medication expiry, first-aid kit"
mot_cle: "medicine cabinet"
nom_court: ""
branche: "D26"
synonymes: []
cross_refs: [477, 485, 478]
---
## 487. 💊 Medicine cabinet manager

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Check expiries, restock the first-aid kit.

**Quand l'utiliser (triggers)** :
- any request about: medication expiry, first-aid kit

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
1. Audit expiries twice a year.
2. Basics: painkillers, antiseptic, plasters, thermometer.
3. Disposal of expired meds at pharmacy.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Clean out our medicine cabinet. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

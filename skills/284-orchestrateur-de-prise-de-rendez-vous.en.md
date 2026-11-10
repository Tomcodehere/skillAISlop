---
num: 284
resume: "Find a meeting slot across timezones."
lang: "en"
date_ajout: "2026-11"
nom: "Meeting scheduler orchestrator"
emoji: "📅"
domaine: "Productivité"
signal: "Find a slot for several people, multi-timezone"
mot_cle: "meeting scheduling"
nom_court: ""
branche: "D25"
synonymes: []
cross_refs: [72, 209, 670]
---
## 284. 📅 Meeting scheduler orchestrator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Propose 3 slots that work for everyone.

**Quand l'utiliser (triggers)** :
- any request about: find a slot for several people, multi-timezone

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
1. Collect availability + timezones.
2. Overlap windows + working hours.
3. Send the invite with agenda.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Find a 1h slot for 5 people across Paris, NYC and Tokyo. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

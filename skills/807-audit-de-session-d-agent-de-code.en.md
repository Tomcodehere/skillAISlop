---
num: 807
resume: "Audit what a coding agent did."
lang: "en"
date_ajout: "2026-11"
nom: "Coding agent session audit"
emoji: "🔍"
domaine: "Data & IA"
signal: "Audit a coding agent session"
mot_cle: "session audit"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [713, 694, 601]
---
## 807. 🔍 Coding agent session audit

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Review diffs, tests, drift before merge (see 601, 330).

**Quand l'utiliser (triggers)** :
- any request about: audit a coding agent session

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
1. Read the full diff + test results.
2. Check scope vs the brief.
3. Write the review note.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Audit this agent's PR before merge. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

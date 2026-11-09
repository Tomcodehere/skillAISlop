---
num: 251
resume: "Write a session handoff note."
lang: "en"
date_ajout: "2026-11"
nom: "Session handoff writer"
emoji: "📨"
domaine: "IA / Prompting"
signal: "Session handoff, resuming after context break"
mot_cle: "session handoff"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [209, 236, 601]
---
## 251. 📨 Session handoff writer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Write a handoff that lets the next session resume fast.

**Quand l'utiliser (triggers)** :
- any request about: session handoff, resuming after context break

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
1. State the goal + where we are.
2. Decisions made + open questions.
3. Next 3 steps + files touched.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Handoff note for this refactor session at 80% done. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

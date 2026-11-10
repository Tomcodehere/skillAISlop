---
num: 378
resume: "Clean a raw transcript into readable text."
lang: "en"
date_ajout: "2026-11"
nom: "Transcript cleaner"
emoji: "🧹"
domaine: "Rédaction"
signal: "Clean a transcript, interview verbatim"
mot_cle: "transcript cleaning"
nom_court: ""
branche: "D18"
synonymes: []
cross_refs: [134, 355, 388]
---
## 378. 🧹 Transcript cleaner

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Clean a verbatim: fillers, timestamps, speakers.

**Quand l'utiliser (triggers)** :
- any request about: clean a transcript, interview verbatim

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
1. Remove 'um/euh', false starts, keep meaning.
2. Mark speakers + timestamps if needed.
3. Two versions: verbatim / edited.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Clean this 1h interview transcript for the blog. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

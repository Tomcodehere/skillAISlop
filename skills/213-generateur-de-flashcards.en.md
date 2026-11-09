---
num: 213
resume: "Generate effective flashcards."
lang: "en"
date_ajout: "2026-11"
nom: "Flashcard generator"
emoji: "🃏"
domaine: "Apprentissage"
signal: "Flashcards, revision cards"
mot_cle: "flashcards"
nom_court: ""
branche: "D26"
synonymes: []
cross_refs: [40, 41, 580]
---
## 213. 🃏 Flashcard generator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Generate flashcards that stick (active recall).

**Quand l'utiliser (triggers)** :
- any request about: flashcards, revision cards

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
1. Extract key Q/A pairs.
2. One idea per card, cloze where useful.
3. Export to Anki/Quizlet format.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Flashcards for the 50 terms of this marketing glossary. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 817
resume: "Iterate prompts in dialogue."
lang: "en"
date_ajout: "2026-11"
nom: "Iterative prompt engineering (dialogue, not one-shot)"
emoji: "💬"
domaine: "IA / Prompting"
signal: "Iterative prompting, dialogue not one-shot"
mot_cle: "iterative prompting"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [737, 338, 945]
---
## 817. 💬 Iterative prompt engineering (dialogue, not one-shot)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Refine turn by turn; keep what works (see 598, 237).

**Quand l'utiliser (triggers)** :
- any request about: iterative prompting, dialogue not one-shot

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
1. Give feedback per output.
2. One change at a time.
3. Save the winning prompt.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Improve this prompt over 3 turns. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

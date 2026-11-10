---
num: 310
resume: "Generate edge cases and fuzz inputs."
lang: "en"
date_ajout: "2026-11"
nom: "Edge-case & fuzzing generator"
emoji: "🎯"
domaine: "Développement"
signal: "Fuzzing, invalid input, code edge case"
mot_cle: "fuzzing edge cases"
nom_court: ""
branche: "D16"
synonymes: []
cross_refs: [67, 317, 9]
---
## 310. 🎯 Edge-case & fuzzing generator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Find edge cases with fuzzing + property tests.

**Quand l'utiliser (triggers)** :
- any request about: fuzzing, invalid input, code edge case

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
1. List boundary values per input.
2. Property-based tests (hypothesis...).
3. Fuzz with random/mutated inputs.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Fuzz our JSON parser with malformed inputs. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

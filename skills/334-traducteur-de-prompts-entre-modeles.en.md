---
num: 334
resume: "Port a prompt between models."
lang: "en"
date_ajout: "2026-11"
nom: "Cross-model prompt translator"
emoji: "🔀"
domaine: "IA / Prompting"
signal: "Port a prompt to another model"
mot_cle: "prompt porting"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [17, 338, 237]
---
## 334. 🔀 Cross-model prompt translator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Adapt a prompt from model A to model B.

**Quand l'utiliser (triggers)** :
- any request about: port a prompt to another model

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
1. Identify model-specific quirks (delimiters, roles).
2. Rewrite instructions in the target's idiom.
3. Eval both on the same cases.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Port this Claude prompt to a Llama 4 local model. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

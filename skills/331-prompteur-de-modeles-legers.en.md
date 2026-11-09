---
num: 331
resume: "Get good results from a small/on-device model."
lang: "en"
date_ajout: "2026-11"
nom: "Lightweight model prompter"
emoji: "🐥"
domaine: "IA / Prompting"
signal: "Lightweight model, small model, on-device"
mot_cle: "lightweight models"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [100, 265, 903]
---
## 331. 🐥 Lightweight model prompter

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Prompt a small model effectively (it has less context).

**Quand l'utiliser (triggers)** :
- any request about: lightweight model, small model, on-device

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
1. Shorter, denser prompts; few-shot minimal.
2. Structured output schema to compensate.
3. Measure quality vs the big model.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Adapt this summarisation prompt for a 3B on-device model. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

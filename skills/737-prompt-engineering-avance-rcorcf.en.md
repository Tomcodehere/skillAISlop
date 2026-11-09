---
num: 737
resume: "Structure prompts with RCORCF."
lang: "en"
date_ajout: "2026-11"
nom: "Advanced prompt engineering (RCORCF)"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Structure a prompt: role, context, objective, resources, constraints, format"
mot_cle: "structured prompt"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [17, 334, 817]
---
## 737. 🧠 Advanced prompt engineering (RCORCF)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Role-Context-Objective-Resources-Constraints-Format.

**Quand l'utiliser (triggers)** :
- any request about: structure a prompt: role, context, objective, resources, constraints, format

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
1. Fill each RCORCF slot.
2. Add one example (few-shot).
3. Eval and iterate (598).

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Rewrite this prompt with RCORCF. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

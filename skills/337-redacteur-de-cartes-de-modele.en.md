---
num: 337
resume: "Write a model card."
lang: "en"
date_ajout: "2026-11"
nom: "Model card writer"
emoji: "🪪"
domaine: "IA / Prompting"
signal: "Model card, document a model"
mot_cle: "model cards"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [97, 332, 342]
---
## 337. 🪪 Model card writer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Document a model: intended use, limits, evals, ethics.

**Quand l'utiliser (triggers)** :
- any request about: model card, document a model

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
1. Model details + training data summary.
2. Intended use + out-of-scope uses.
3. Evaluation results + known limitations.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Model card for our internal support classifier. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

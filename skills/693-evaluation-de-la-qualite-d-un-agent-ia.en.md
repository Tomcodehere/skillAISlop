---
num: 693
resume: "Evaluate an AI agent properly."
lang: "en"
date_ajout: "2026-11"
nom: "AI agent quality evaluation"
emoji: "✅"
domaine: "Data & IA"
signal: "Evaluate an AI agent, evals, test set, LLM quality metrics, golden dataset"
mot_cle: "agent evals"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [97, 333, 819]
---
## 693. ✅ AI agent quality evaluation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Build an eval suite with a golden dataset.

**Quand l'utiliser (triggers)** :
- any request about: evaluate an ai agent, evals, test set, llm quality metrics, golden dataset

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
1. 50-200 golden cases with rubrics.
2. Automated scorers + LLM-judge calibrated.
3. Gate releases on eval regression.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Eval suite for our support agent. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

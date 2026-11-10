---
num: 738
resume: "Get step-by-step reasoning."
lang: "en"
date_ajout: "2026-11"
nom: "Chain-of-thought & step-by-step reasoning"
emoji: "🪜"
domaine: "IA / Prompting"
signal: "Make the AI reason step by step, CoT, decompose a complex problem"
mot_cle: "chain of thought"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [11, 21, 1064]
---
## 738. 🪜 Chain-of-thought & step-by-step reasoning

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ask for reasoning before the answer.

**Quand l'utiliser (triggers)** :
- any request about: make the ai reason step by step, cot, decompose a complex problem

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
1. 'Think step by step' + format.
2. Decompose the problem first.
3. Verify each step (700).

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Solve this logic puzzle step by step. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 333
resume: "Choose the right model from benchmarks."
lang: "en"
date_ajout: "2026-11"
nom: "Model benchmark explorer"
emoji: "🏆"
domaine: "IA / Prompting"
signal: "Choose a model, leaderboard, model benchmark"
mot_cle: "model benchmarks"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [97, 265, 689]
---
## 333. 🏆 Model benchmark explorer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Pick a model using public leaderboards + own evals.

**Quand l'utiliser (triggers)** :
- any request about: choose a model, leaderboard, model benchmark

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
1. Shortlist 3 models by leaderboard task fit.
2. Run them on YOUR 20-case eval set.
3. Decide on quality/cost/latency.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Which open model for French legal summarisation under 4k€/month? » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

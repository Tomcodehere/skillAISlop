---
num: 689
resume: "Choose the right LLM per use case."
lang: "en"
date_ajout: "2026-11"
nom: "Choosing an LLM & model comparison"
emoji: "🤖"
domaine: "IA / Prompting"
signal: "Choose an LLM, compare models (GPT, Claude, Gemini, Mistral, open source), cost per token"
mot_cle: "choose llm"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [331, 333, 265]
---
## 689. 🤖 Choosing an LLM & model comparison

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Compare models on quality/cost/latency/privacy.

**Quand l'utiliser (triggers)** :
- any request about: choose an llm, compare models (gpt, claude, gemini, mistral, open source), cost per token

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
1. Shortlist by task (coding, long doc, FR...).
2. Benchmark on YOUR cases, not leaderboards.
3. Open weights if data privacy matters.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Best model for French legal docs under 2k€/month. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

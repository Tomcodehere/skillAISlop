---
num: 332
resume: "Force strict JSON/structured output."
lang: "en"
date_ajout: "2026-11"
nom: "Output schema guardian"
emoji: "🎛️"
domaine: "IA / Prompting"
signal: "Strict JSON output, structured output"
mot_cle: "structured output json"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [99, 338, 321]
---
## 332. 🎛️ Output schema guardian

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Constrain the model to valid JSON via schema.

**Quand l'utiliser (triggers)** :
- any request about: strict json output, structured output

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
1. Define the JSON schema (required, types).
2. Use structured output / grammar mode.
3. Validate + retry on parse failure.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « The model must always return {score: 1-5, reason: string}. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

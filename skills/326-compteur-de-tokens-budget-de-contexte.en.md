---
num: 326
resume: "Count tokens and fit the context budget."
lang: "en"
date_ajout: "2026-11"
nom: "Token budget accountant"
emoji: "🪙"
domaine: "IA / Prompting"
signal: "Token budget, context overflow"
mot_cle: "token budget"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [236, 265, 455]
---
## 326. 🪙 Token budget accountant

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Measure tokens and stay within the context window.

**Quand l'utiliser (triggers)** :
- any request about: token budget, context overflow

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
1. Count per message (tiktoken-style).
2. Trim/summarise oldest, keep system+recent.
3. Alert before overflow.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Our chat exceeds 128k tokens — budget it. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

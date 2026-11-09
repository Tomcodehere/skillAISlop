---
num: 719
resume: "Get ultra-concise AI replies."
lang: "en"
date_ajout: "2026-11"
nom: "Caveman mode: ultra-concise replies"
emoji: "🪨"
domaine: "IA / Prompting"
signal: "Short answers, caveman mode, straight to the point, fewer tokens"
mot_cle: "caveman mode"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [327, 694, 945]
---
## 719. 🪨 Caveman mode: ultra-concise replies

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Caveman mode: bullets, no fluff, save tokens.

**Quand l'utiliser (triggers)** :
- any request about: short answers, caveman mode, straight to the point, fewer tokens

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
1. Prompt: 'answer in max 5 bullets, no intro'.
2. Use for quick lookups.
3. Combine with 327 for long outputs.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Caveman-mode summary of this doc. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

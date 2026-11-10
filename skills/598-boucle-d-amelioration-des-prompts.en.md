---
num: 598
resume: "Iterate prompts with a feedback loop."
lang: "en"
date_ajout: "2026-11"
nom: "Prompt improvement loop"
emoji: "🔁"
domaine: "IA / Prompting"
signal: "Continuous prompt improvement, iteration, feedback"
mot_cle: "prompt iteration"
nom_court: ""
branche: "D30"
synonymes: []
cross_refs: [17, 338, 237]
---
## 598. 🔁 Prompt improvement loop

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Improve a prompt systematically.

**Quand l'utiliser (triggers)** :
- any request about: continuous prompt improvement, iteration, feedback

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
1. Collect failure examples (eval set).
2. Change one variable, measure.
3. Keep the version that wins + log it.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Our support prompt fails 15% — improvement loop. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 733
resume: "Run a proper A/B test."
lang: "en"
date_ajout: "2026-11"
nom: "A/B tests & experimentation"
emoji: "🧪"
domaine: "Produit"
signal: "Launch an A/B test, user experiment, compare variants, statistical significance"
mot_cle: "ab test"
nom_court: ""
branche: "D22"
synonymes: []
cross_refs: [110, 179, 735]
---
## 733. 🧪 A/B tests & experimentation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Hypothesis, MDE, sample size, decision rule (see 110).

**Quand l'utiliser (triggers)** :
- any request about: launch an a/b test, user experiment, compare variants, statistical significance

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
1. One variable, one metric.
2. Power analysis first.
3. Ship winner, log learnings.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « A/B test the new CTA color. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 304
resume: "Ship behind feature flags with a kill switch."
lang: "en"
date_ajout: "2026-11"
nom: "Feature flag manager"
emoji: "🚩"
domaine: "Développement"
signal: "Feature flag, progressive rollout, kill switch"
mot_cle: "feature flags"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [110, 163, 301]
---
## 304. 🚩 Feature flag manager

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rollout a feature progressively with flags.

**Quand l'utiliser (triggers)** :
- any request about: feature flag, progressive rollout, kill switch

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
1. One flag per feature, default off.
2. Rollout % + monitoring + kill switch.
3. Remove the flag when 100% stable.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Roll out the new checkout to 5% of users. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

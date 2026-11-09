---
num: 307
resume: "Plan a safe dependency upgrade."
lang: "en"
date_ajout: "2026-11"
nom: "Dependency upgrade planner"
emoji: "⬆️"
domaine: "Développement"
signal: "Upgrade a dependency, risky upgrade"
mot_cle: "dependency upgrades"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [86, 267, 255]
---
## 307. ⬆️ Dependency upgrade planner

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Upgrade a dependency without breaking prod.

**Quand l'utiliser (triggers)** :
- any request about: upgrade a dependency, risky upgrade

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
1. Read the changelog for breaking changes.
2. Upgrade one dep at a time, tests green.
3. Lockfile review + rollback plan.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Upgrade React 17 -> 18 in our app. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

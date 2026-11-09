---
num: 303
resume: "Version releases with SemVer."
lang: "en"
date_ajout: "2026-11"
nom: "Semantic versioning keeper"
emoji: "🏷️"
domaine: "Développement"
signal: "SemVer, version number, breaking change"
mot_cle: "semver versioning"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [129, 183, 604]
---
## 303. 🏷️ Semantic versioning keeper

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Decide MAJOR.MINOR.PATCH and write the changelog.

**Quand l'utiliser (triggers)** :
- any request about: semver, version number, breaking change

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
1. Classify each change (breaking/feat/fix).
2. Bump accordingly + changelog.
3. Tag the release.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « We're at 2.3.1 and this PR removes an endpoint. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

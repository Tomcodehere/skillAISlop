---
num: 315
resume: "Find the commit that introduced a regression."
lang: "en"
date_ajout: "2026-11"
nom: "Regression hunter (git bisect)"
emoji: "🔍"
domaine: "Développement"
signal: "Regression, git bisect, find the guilty commit"
mot_cle: "git bisect"
nom_court: ""
branche: "D16"
synonymes: []
cross_refs: [20, 310, 338]
---
## 315. 🔍 Regression hunter (git bisect)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Bisect a regression to the guilty commit.

**Quand l'utiliser (triggers)** :
- any request about: regression, git bisect, find the guilty commit

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
1. git bisect start/good/bad + a test script.
2. Automate the check per commit.
3. Fix + add the regression test.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « The bug appeared between v2.1 and v2.4 — bisect it. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 508
resume: "Harden the CI/CD pipeline."
lang: "en"
date_ajout: "2026-11"
nom: "CI/CD pipeline hardener"
emoji: "🔧"
domaine: "Sécurité"
signal: "CI/CD pipeline, supply chain, signed artifacts"
mot_cle: "cicd security"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [267, 306, 372]
---
## 508. 🔧 CI/CD pipeline hardener

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Secure the pipeline: pinned actions, signed artifacts, secrets.

**Quand l'utiliser (triggers)** :
- any request about: ci/cd pipeline, supply chain, signed artifacts

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
1. Pin actions by SHA, review third-party actions.
2. Secrets in the vault, masked in logs.
3. Sign + verify artifacts (cosign).

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Harden our GitHub Actions pipelines. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

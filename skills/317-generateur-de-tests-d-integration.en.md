---
num: 317
resume: "Write integration tests for service contracts."
lang: "en"
date_ajout: "2026-11"
nom: "Integration test generator"
emoji: "🧩"
domaine: "Développement"
signal: "Integration test, contract between services"
mot_cle: "integration tests"
nom_court: ""
branche: "D16"
synonymes: []
cross_refs: [67, 252, 255]
---
## 317. 🧩 Integration test generator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Test the contract between two services.

**Quand l'utiliser (triggers)** :
- any request about: integration test, contract between services

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
1. Contract tests (Pact-style) or testcontainers.
2. Cover happy path + error + timeout.
3. Run in CI, not just locally.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Integration tests for our API <-> billing service. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

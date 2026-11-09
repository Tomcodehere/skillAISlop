---
num: 67
resume: "Generate meaningful unit tests for a piece of code."
lang: "en"
date_ajout: "2026-11"
nom: "Unit test generator"
emoji: "🧪"
domaine: "Développement"
signal: "Unit tests, TDD, coverage"
mot_cle: "unit tests tdd"
nom_court: "Test generator"
branche: "D12"
synonymes: []
cross_refs: [21, 63, 317]
---
## 67. 🧪 Unit test generator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Generate meaningful unit tests (TDD-friendly) for a piece of code.

**Quand l'utiliser (triggers)** :
- add tests to untested code
- integration/e2e tests

**Hors périmètre** :
- (not covered — see cross-refs)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a test engineer. You identify the behaviours (not lines), write tests with Arrange-Act-Assert, cover edge cases and errors, and report the coverage delta.

**Inputs requis** :
- the code + the framework

**Méthode** :
1. Identify behaviours and edge cases.
2. Write AAA tests.
3. Measure coverage delta.

**Sorties attendues** :
- test suite + coverage report

**Exemple de prompt** :
> « « Unit tests for this Python payment-validation function. » »

**Cas d'usage** : Code quality, CI. Chains with 20.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

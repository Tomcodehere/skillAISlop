---
num: 822
resume: "Generate tests from docs/specs."
lang: "en"
date_ajout: "2026-11"
nom: "Doc-to-test generation"
emoji: "🧪"
domaine: "Développement"
signal: "Generate tests from documentation"
mot_cle: "doc to test"
nom_court: ""
branche: "D12"
synonymes: []
cross_refs: [302, 543, 67]
---
## 822. 🧪 Doc-to-test generation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Extract behaviours from docs -> test cases (see 67, 605).

**Quand l'utiliser (triggers)** :
- any request about: generate tests from documentation

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
1. Parse the spec for rules/examples.
2. Generate test cases per rule.
3. Human review + run in CI.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Tests from this API spec. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

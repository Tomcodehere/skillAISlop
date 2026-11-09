---
num: 83
resume: "Transpile/migrate code between languages safely."
lang: "en"
date_ajout: "2026-11"
nom: "Code transpiler"
emoji: "🔃"
domaine: "Développement"
signal: "Code transpilation, language migration"
mot_cle: "code transpiler"
nom_court: "Transpiler"
branche: "D15"
synonymes: []
cross_refs: [9, 86, 85]
---
## 83. 🔃 Code transpiler

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Transpile code from one language to another with verification.

**Quand l'utiliser (triggers)** :
- migrate a codebase language or framework

**Hors périmètre** :
- refactoring within a language (skill 80)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a migration engineer. You map constructs 1:1, transpile, then verify with the original test suite ported over + differential testing on samples before cutover.

**Inputs requis** :
- the source code + target language + test suite

**Méthode** :
1. Map constructs, transpile.
2. Port tests, run differential tests.
3. Cutover plan.

**Sorties attendues** :
- transpiled code + verification report

**Exemple de prompt** :
> « « Migrate this 20k-line JS frontend to TypeScript. » »

**Cas d'usage** : Modernisation. Chains with 80.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

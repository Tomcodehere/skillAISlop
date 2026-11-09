---
num: 321
resume: "Run zero-downtime schema migrations."
lang: "en"
date_ajout: "2026-11"
nom: "Database schema migrator"
emoji: "🗄️"
domaine: "Développement"
signal: "Schema migration, zero-downtime DB"
mot_cle: "schema migrations"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [86, 318, 542]
---
## 321. 🗄️ Database schema migrator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Migrate a schema without downtime.

**Quand l'utiliser (triggers)** :
- any request about: schema migration, zero-downtime db

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
1. Expand-contract: add column nullable first.
2. Backfill, then constraints.
3. Rollback plan tested.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Add a NOT NULL column to a 50M-row table safely. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

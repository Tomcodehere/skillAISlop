---
num: 318
resume: "Optimise a slow SQL query."
lang: "en"
date_ajout: "2026-11"
nom: "Slow SQL query optimiser"
emoji: "🐢"
domaine: "Développement"
signal: "Slow SQL query, execution plan, index"
mot_cle: "sql optimisation"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [69, 321, 1229]
---
## 318. 🐢 Slow SQL query optimiser

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Read the EXPLAIN plan and fix the query.

**Quand l'utiliser (triggers)** :
- any request about: slow sql query, execution plan, index

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
1. EXPLAIN ANALYZE the query.
2. Add/adjust indexes, rewrite joins.
3. Verify with before/after timings.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « This join takes 8s on 2M rows — optimise it. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 261
resume: "Test that skills trigger correctly."
lang: "en"
date_ajout: "2026-11"
nom: "Skill trigger tester"
emoji: "⭐"
domaine: "IA / Prompting"
signal: "Trigger testing, skill routing matrix"
mot_cle: "skill trigger tests"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [97, 262, 325]
---
## 261. ⭐ Skill trigger tester

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Build a trigger matrix: query -> expected skill.

**Quand l'utiliser (triggers)** :
- any request about: trigger testing, skill routing matrix

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
1. List the queries per skill.
2. Run the router, check the winner.
3. Fix synonyms/signals on misses.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Test that 'how do I cook pasta' routes to the recipes skill. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

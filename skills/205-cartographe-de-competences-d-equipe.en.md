---
num: 205
resume: "Map the team's skills in a matrix."
lang: "en"
date_ajout: "2026-11"
nom: "Team skills mapper"
emoji: "🗺️"
domaine: "RH & formation"
signal: "Team skills mapping"
mot_cle: "skills matrix"
nom_court: ""
branche: "D24"
synonymes: []
cross_refs: [201, 204, 428]
---
## 205. 🗺️ Team skills mapper

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Build a skills matrix to spot gaps.

**Quand l'utiliser (triggers)** :
- any request about: team skills mapping

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
1. List the skills needed per role.
2. Self + manager assessment (1-4).
3. Heatmap + training plan per gap.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Skills matrix for our 8-person platform team. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

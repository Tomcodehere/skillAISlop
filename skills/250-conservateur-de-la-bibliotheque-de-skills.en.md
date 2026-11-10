---
num: 250
resume: "Maintain and evolve the skill library."
lang: "en"
date_ajout: "2026-11"
nom: "Skill library curator"
emoji: "🎩"
domaine: "Routage"
signal: "Evolve the catalogue, add a skill"
mot_cle: "skill library curator"
nom_court: ""
branche: "D26"
synonymes: []
cross_refs: [0, 38, 97]
---
## 250. 🎩 Skill library curator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Add/enrich a skill in the catalogue following the rules.

**Quand l'utiliser (triggers)** :
- any request about: evolve the catalogue, add a skill

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
1. Check duplicates (R6) against the catalogue.
2. Write per the official template + route it (R3).
3. Run lint/test/audit + log in DONE.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Add a skill about prompt injection testing to our library. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

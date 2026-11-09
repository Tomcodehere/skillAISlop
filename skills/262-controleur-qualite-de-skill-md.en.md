---
num: 262
resume: "Audit a SKILL.md for quality."
lang: "en"
date_ajout: "2026-11"
nom: "SKILL.md quality controller"
emoji: "👨‍⚖️"
domaine: "IA / Prompting"
signal: "SKILL.md audit, skill quality"
mot_cle: "skill.md quality"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [38, 250, 716]
---
## 262. 👨‍⚖️ SKILL.md quality controller

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Review a SKILL.md against the quality checklist.

**Quand l'utiliser (triggers)** :
- any request about: skill.md audit, skill quality

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
1. Check frontmatter + sections + triggers.
2. Check examples are concrete + guardrails.
3. Score + fix list.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Review this SKILL.md before we publish it. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

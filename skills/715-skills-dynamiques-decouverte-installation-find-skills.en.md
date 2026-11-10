---
num: 715
resume: "Discover and install skills safely."
lang: "en"
date_ajout: "2026-11"
nom: "Dynamic skills: discover & install (find-skills)"
emoji: "🧩"
domaine: "Data & IA"
signal: "Find and install an agent skill, find-skills, skills.sh, npx skills"
mot_cle: "find skills"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [38, 325, 905]
---
## 715. 🧩 Dynamic skills: discover & install (find-skills)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Find-skills + vet before install (716, 325).

**Quand l'utiliser (triggers)** :
- any request about: find and install an agent skill, find-skills, skills.sh, npx skills

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
1. skills.sh / npx skills search.
2. Audit the SKILL.md (716) before installing.
3. Sandbox + least privilege.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Find a skill for PDF extraction and install it. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

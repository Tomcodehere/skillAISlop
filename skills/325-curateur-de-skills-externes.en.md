---
num: 325
resume: "Curate external skills safely."
lang: "en"
date_ajout: "2026-11"
nom: "External skills curator"
emoji: "🧰"
domaine: "IA / Prompting"
signal: "Install an external skill, skills registry"
mot_cle: "external skills"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [194, 262, 261]
---
## 325. 🧰 External skills curator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Vet and install an external skill.

**Quand l'utiliser (triggers)** :
- any request about: install an external skill, skills registry

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
1. Check source/reputation + licence.
2. Read the SKILL.md fully (prompt-injection check).
3. Install in an isolated scope + test.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Vet and install the 'pdf-extract' skill from GitHub. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

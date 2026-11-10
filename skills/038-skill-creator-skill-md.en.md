---
num: 38
resume: "Create a SKILL.md skill package (Agent Skills standard)."
lang: "en"
date_ajout: "2026-11"
nom: "🧩 Skill creator (SKILL.md)"
emoji: "🧩"
domaine: "Data & IA"
signal: "Create a SKILL.md skill package"
mot_cle: "skill creator skill.md"
nom_court: "Skill creator"
branche: "D4"
synonymes: []
cross_refs: [17, 37, 716]
---
## 38. 🧩 Skill creator (SKILL.md)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Create a SKILL.md skill package following the Agent Skills standard.

**Quand l'utiliser (triggers)** :
- package a capability as an installable skill

**Hors périmètre** :
- editing the catalogue itself (skill 0 / conservateur)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a skill packager. You produce the folder: SKILL.md with standard frontmatter (name, description) + the body sections, a skills.json entry, and validate with `npx skills add` dry-run; you follow the official template exactly.

**Inputs requis** :
- the capability to package + target agent

**Méthode** :
1. Write SKILL.md per the standard frontmatter.
2. Body sections per the template.
3. skills.json entry + install dry-run.

**Sorties attendues** :
- the skill folder, installable

**Exemple de prompt** :
> « « Package our PDF-extraction capability as a SKILL.md for Claude Code. » »

**Cas d'usage** : Agent Skills distribution. Chains with skill 0.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

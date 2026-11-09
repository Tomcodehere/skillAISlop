---
num: 716
resume: "Audit a skill before installing it."
lang: "en"
date_ajout: "2026-11"
nom: "SKILL.md security audit"
emoji: "🛡️"
domaine: "Sécurité"
signal: "Audit a skill before installing, check a SKILL.md, malicious skill, permissions"
mot_cle: "skill audit"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [262, 195, 905]
---
## 716. 🛡️ SKILL.md security audit

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Read the SKILL.md fully: exfiltration, prompts, perms.

**Quand l'utiliser (triggers)** :
- any request about: audit a skill before installing, check a skill.md, malicious skill, permissions

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
1. Check for hidden instructions / data exfiltration.
2. Permissions requested vs needed.
3. Install in a sandbox; monitor.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Audit this SKILL.md from GitHub before npx skills add. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

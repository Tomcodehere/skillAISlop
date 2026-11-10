---
num: 324
resume: "Write a robust shell script."
lang: "en"
date_ajout: "2026-11"
nom: "Robust CLI script writer"
emoji: "🐚"
domaine: "Développement"
signal: "Robust shell script, strict mode, error handling"
mot_cle: "shell scripts"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [199, 269, 384]
---
## 324. 🐚 Robust CLI script writer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Write a bash script that fails safely.

**Quand l'utiliser (triggers)** :
- any request about: robust shell script, strict mode, error handling

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
1. set -euo pipefail + trap on error.
2. Usage/help, arg validation, idempotent.
3. Log to stderr, meaningful exit codes.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « A deploy script that can be re-run safely. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

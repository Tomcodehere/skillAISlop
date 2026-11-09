---
num: 503
resume: "Secure (and clean) a CMS."
lang: "en"
date_ajout: "2026-11"
nom: "WordPress & CMS securer"
emoji: "🔒"
domaine: "Sécurité"
signal: "Hacked WordPress/CMS, plugins"
mot_cle: "cms security"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [447, 505, 818]
---
## 503. 🔒 WordPress & CMS securer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Harden WordPress: updates, plugins, access, backups.

**Quand l'utiliser (triggers)** :
- any request about: hacked wordpress/cms, plugins

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
1. Update core/plugins/theme, remove unused.
2. 2FA + limit login attempts + rename wp-admin.
3. Backups offsite + malware scan.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Our WordPress site got hacked — clean and secure it. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

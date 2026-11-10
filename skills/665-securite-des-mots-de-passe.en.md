---
num: 665
resume: "Secure your passwords and accounts."
lang: "en"
date_ajout: "2026-11"
nom: "Password security"
emoji: "🔐"
domaine: "Sécurité"
signal: "Passwords, password manager, 2FA, MFA, account hacking, data leak"
mot_cle: "passwords"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [501, 506, 1337]
---
## 665. 🔐 Password security

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Password hygiene: manager + unique + 2FA.

**Quand l'utiliser (triggers)** :
- any request about: passwords, password manager, 2fa, mfa, account hacking, data leak

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
1. Password manager (Bitwarden/1Password...), unique per site.
2. 2FA everywhere (app/passkey > SMS).
3. Check breaches (HIBP), rotate on leak.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « My account was hacked — secure everything. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

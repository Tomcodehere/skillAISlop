---
num: 306
resume: "Handle secrets safely."
lang: "en"
date_ajout: "2026-11"
nom: "Secrets & keyring manager"
emoji: "🔐"
domaine: "Développement"
signal: "Store a secret, key rotation, vault"
mot_cle: "secrets vault"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [70, 197, 301]
---
## 306. 🔐 Secrets & keyring manager

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Store and rotate secrets properly.

**Quand l'utiliser (triggers)** :
- any request about: store a secret, key rotation, vault

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
1. Never in git; use a vault/secret manager.
2. Rotation schedule + audit log.
3. Local dev: .env gitignored + template.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Set up Vault for our API keys with 90-day rotation. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 502
resume: "Harden HTTP headers and cookies."
lang: "en"
date_ajout: "2026-11"
nom: "HTTP headers & cookies hardener"
emoji: "🛡️"
domaine: "Sécurité"
signal: "HTTP headers, CSP, cookies, CORS"
mot_cle: "http headers csp"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [70, 501, 508]
---
## 502. 🛡️ HTTP headers & cookies hardener

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Set CSP, HSTS, Secure/HttpOnly cookies, CORS.

**Quand l'utiliser (triggers)** :
- any request about: http headers, csp, cookies, cors

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
1. CSP without unsafe-inline, HSTS, cookie flags.
2. CORS: explicit origins, credentials carefully.
3. Verify with securityheaders.com + tests.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Harden the headers of our marketing site. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

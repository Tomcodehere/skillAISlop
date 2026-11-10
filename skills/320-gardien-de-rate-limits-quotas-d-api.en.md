---
num: 320
resume: "Implement rate limiting on an API."
lang: "en"
date_ajout: "2026-11"
nom: "API rate limit & quota guardian"
emoji: "🚧"
domaine: "Développement"
signal: "Rate limit, API quota, 429 error"
mot_cle: "rate limiting"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [79, 322, 20]
---
## 320. 🚧 API rate limit & quota guardian

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Add rate limits with clear 429 responses.

**Quand l'utiliser (triggers)** :
- any request about: rate limit, api quota, 429 error

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
1. Token bucket per key/IP.
2. Headers: limit, remaining, retry-after.
3. Monitor + alert on saturation.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Add rate limiting: 100 req/min per API key. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

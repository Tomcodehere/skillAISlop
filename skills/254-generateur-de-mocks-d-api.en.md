---
num: 254
resume: "Generate API mocks from an OpenAPI contract."
lang: "en"
date_ajout: "2026-11"
nom: "API mock generator"
emoji: "🎭"
domaine: "Développement"
signal: "API mock, fixtures from an OpenAPI contract"
mot_cle: "api mocks"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [87, 178, 317]
---
## 254. 🎭 API mock generator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Generate realistic mock fixtures from the spec.

**Quand l'utiliser (triggers)** :
- any request about: api mock, fixtures from an openapi contract

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
1. Parse the OpenAPI schemas.
2. Generate example payloads per endpoint.
3. Serve with a mock server (Prism...).

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Mocks for our payments API for the mobile team. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

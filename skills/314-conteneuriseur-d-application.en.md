---
num: 314
resume: "Containerise an application."
lang: "en"
date_ajout: "2026-11"
nom: "Application containeriser"
emoji: "🐳"
domaine: "Développement"
signal: "Dockerfile, containerise an app"
mot_cle: "docker container"
nom_court: ""
branche: "D16"
synonymes: []
cross_refs: [82, 305, 1035]
---
## 314. 🐳 Application containeriser

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Write a production-grade Dockerfile.

**Quand l'utiliser (triggers)** :
- any request about: dockerfile, containerise an app

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
1. Multi-stage build, non-root user.
2. .dockerignore + healthcheck.
3. Scan the image for CVEs.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Dockerfile for our Node API, image under 150MB. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

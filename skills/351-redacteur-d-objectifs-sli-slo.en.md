---
num: 351
resume: "Write SLOs that are achievable and useful."
lang: "en"
date_ajout: "2026-11"
nom: "SLI/SLO writer"
emoji: "🎯"
domaine: "Data"
signal: "SLO, availability commitment"
mot_cle: "sli slo"
nom_court: ""
branche: "D17"
synonymes: []
cross_refs: [199, 431, 238]
---
## 351. 🎯 SLI/SLO writer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Define SLIs and set SLOs with error budgets.

**Quand l'utiliser (triggers)** :
- any request about: slo, availability commitment

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
1. Pick the user-facing SLI (latency, availability).
2. SLO from historical performance + user need.
3. Error budget policy: freeze vs ship.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « SLO for our API: 99.9% availability, p95 < 300ms. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

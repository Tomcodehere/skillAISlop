---
num: 826
resume: "Sell a property well."
lang: "en"
date_ajout: "2026-11"
nom: "Selling real estate"
emoji: "🏠"
domaine: "Finance"
signal: "Sell a property"
mot_cle: "sell property"
nom_court: ""
branche: "D29"
synonymes: []
cross_refs: [675, 45, 992]
---
## 826. 🏠 Selling real estate

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Price with market data, stage it, pick the agent (see 675).

**Quand l'utiliser (triggers)** :
- any request about: sell a property

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
1. Comparable sales per m².
2. Home staging + photos.
3. Negotiate offers; check buyer financing.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Sell my apartment in Lyon. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 474
resume: "Track warranties and repairs."
lang: "en"
date_ajout: "2026-11"
nom: "Warranty & repair tracker"
emoji: "🛠️"
domaine: "Personnel"
signal: "Warranty, after-sales service, repair quote"
mot_cle: "warranties repairs"
nom_court: ""
branche: "D26"
synonymes: []
cross_refs: [479, 480, 654]
---
## 474. 🛠️ Warranty & repair tracker

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Never lose a warranty: register + receipts + dates.

**Quand l'utiliser (triggers)** :
- any request about: warranty, after-sales service, repair quote

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
1. Register products + warranty end dates.
2. Store receipts + photos of serial numbers.
3. Alerts 1 month before expiry.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Warranty tracker for all our appliances. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

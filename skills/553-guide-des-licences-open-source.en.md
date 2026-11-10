---
num: 553
resume: "Pick and comply with open-source licences."
lang: "en"
date_ajout: "2026-11"
nom: "Open source licence guide"
emoji: "⚖️"
domaine: "Juridique"
signal: "Open source licence, MIT, GPL, dependency compliance"
mot_cle: "oss licences"
nom_court: ""
branche: "D29"
synonymes: []
cross_refs: [88, 267, 752]
---
## 553. ⚖️ Open source licence guide

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choose a licence + check dependency licences.

**Quand l'utiliser (triggers)** :
- any request about: open source licence, mit, gpl, dependency compliance

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
1. MIT/Apache for permissive; GPL if copyleft needed.
2. Scan deps (license-checker) + keep NOTICE.
3. Legal review for AGPL/proprietary mix.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Which licence for our internal tool we may open-source? » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 870
resume: "Spot a fake/scam property listing."
lang: "en"
date_ajout: "2026-11"
nom: "Verifying a property listing"
emoji: "🔎"
domaine: "Recherche"
signal: "Check a real-estate ad for scams"
mot_cle: "listing check"
nom_court: ""
branche: "D17"
synonymes: []
cross_refs: [826, 709, 962]
---
## 870. 🔎 Verifying a property listing

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Reverse image search, price vs market, no upfront payment (see 530, 675).

**Quand l'utiliser (triggers)** :
- any request about: check a real-estate ad for scams

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
1. Reverse-search the photos.
2. Price too good = red flag.
3. Never pay a 'reservation fee' before visiting.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Is this apartment ad a scam? » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

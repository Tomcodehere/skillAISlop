---
num: 656
resume: "Prepare a trip end to end."
lang: "en"
date_ajout: "2026-11"
nom: "Trip preparation"
emoji: "✈️"
domaine: "Personnel"
signal: "Prepare a trip, itinerary, luggage, accommodation, flight, passport, visa, vaccines, travel insurance"
mot_cle: "trip prep"
nom_court: ""
branche: "D26"
synonymes: []
cross_refs: [42, 476, 988]
---
## 656. ✈️ Trip preparation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Trip checklist: documents, health, packing, bookings.

**Quand l'utiliser (triggers)** :
- any request about: prepare a trip, itinerary, luggage, accommodation, flight, passport, visa, vaccines, travel insurance

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
1. Passport validity + visa per country.
2. Vaccines + insurance + copies of docs.
3. Packing list by category + weight limits.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Trip to Japan in 2 months — checklist. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

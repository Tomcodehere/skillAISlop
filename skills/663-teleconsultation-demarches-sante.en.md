---
num: 663
resume: "Use teleconsultation properly."
lang: "en"
date_ajout: "2026-11"
nom: "Teleconsultation & health admin"
emoji: "🩺"
domaine: "Personnel"
signal: "Teleconsultation, online doctor, e-prescription, medical file"
mot_cle: "teleconsultation"
nom_court: ""
branche: "D27"
synonymes: []
cross_refs: [485, 624, 1331]
---
## 663. 🩺 Teleconsultation & health admin

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Online health steps: consult, prescription, file.

**Quand l'utiliser (triggers)** :
- any request about: teleconsultation, online doctor, e-prescription, medical file

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
1. Choose an approved platform/doctor.
2. Have your Carte Vitale + history ready.
3. E-prescription goes to the pharmacy.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Renew my prescription online. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

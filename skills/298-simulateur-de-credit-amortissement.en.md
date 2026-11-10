---
num: 298
resume: "Simulate and compare loans."
lang: "en"
date_ajout: "2026-11"
nom: "Loan & amortisation simulator"
emoji: "🏦"
domaine: "Finance"
signal: "Amortisation table, APR, compare two loans"
mot_cle: "loan amortisation"
nom_court: ""
branche: "D21"
synonymes: []
cross_refs: [43, 227, 966]
---
## 298. 🏦 Loan & amortisation simulator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Build the amortisation table and compare offers.

**Quand l'utiliser (triggers)** :
- any request about: amortisation table, apr, compare two loans

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
1. Inputs: amount, rate, duration, insurance.
2. Monthly payment + total cost + APR.
3. Compare 2 offers + early repayment impact.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Compare a 200k€ loan at 3.2% vs 3.5% over 20 years. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

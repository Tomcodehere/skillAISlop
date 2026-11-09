---
num: 641
resume: "Read and check a payslip."
lang: "en"
date_ajout: "2026-11"
nom: "Payslip reader"
emoji: "💶"
domaine: "Finance"
signal: "Payslip, salary, net pay, contributions, gross, net social, withholding tax"
mot_cle: "payslip"
nom_court: ""
branche: "D29"
synonymes: []
cross_refs: [294, 588, 973]
---
## 641. 💶 Payslip reader

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Decode your payslip line by line.

**Quand l'utiliser (triggers)** :
- any request about: payslip, salary, net pay, contributions, gross, net social, withholding tax

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
1. Gross -> net social -> net (withholding).
2. Check the main lines: base, overtime, benefits.
3. Anomaly = ask HR/payroll.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Explain this payslip to me. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

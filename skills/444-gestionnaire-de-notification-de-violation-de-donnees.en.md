---
num: 444
resume: "Handle a data breach notification (72h CNIL)."
lang: "en"
date_ajout: "2026-11"
nom: "Data breach notifier"
emoji: "🚨"
domaine: "Juridique"
signal: "Data breach, notify the authority"
mot_cle: "breach notification"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [235, 441, 189]
---
## 444. 🚨 Data breach notifier

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Notify a breach within 72h with the required content.

**Quand l'utiliser (triggers)** :
- any request about: data breach, notify the authority

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
1. Assess the risk to individuals.
2. Notify CNIL within 72h + document.
3. Notify individuals if high risk (not legal advice).

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « We found exposed customer emails — breach process. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

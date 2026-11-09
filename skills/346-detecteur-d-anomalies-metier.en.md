---
num: 346
resume: "Detect and explain business anomalies."
lang: "en"
date_ajout: "2026-11"
nom: "Business anomaly detector"
emoji: "🚨"
domaine: "Data"
signal: "Business anomaly, unexplained spike"
mot_cle: "anomaly detection"
nom_court: ""
branche: "D17"
synonymes: []
cross_refs: [109, 191, 92]
---
## 346. 🚨 Business anomaly detector

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Find anomalies and explain the likely cause.

**Quand l'utiliser (triggers)** :
- any request about: business anomaly, unexplained spike

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
1. Baseline + expected range per metric.
2. Flag outliers + segment drill-down.
3. Correlate with launches/changes.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Revenue spiked 40% Tuesday — anomaly report. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 345
resume: "Forecast a time series with seasonality."
lang: "en"
date_ajout: "2026-11"
nom: "Time series forecaster"
emoji: "📈"
domaine: "Data"
signal: "Seasonality, time series forecast"
mot_cle: "time series forecasting"
nom_court: ""
branche: "D17"
synonymes: []
cross_refs: [93, 170, 372]
---
## 345. 📈 Time series forecaster

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Forecast with trend + seasonality + uncertainty.

**Quand l'utiliser (triggers)** :
- any request about: seasonality, time series forecast

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
1. Decompose trend/seasonality/residual.
2. Model (ARIMA/Prophet/ETS) + validation (backtest).
3. Report with prediction intervals.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Forecast weekly sales for next quarter with CIs. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

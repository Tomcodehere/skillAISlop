---
num: 338
resume: "Detect prompt regressions between versions."
lang: "en"
date_ajout: "2026-11"
nom: "Prompt regression watcher"
emoji: "📉"
domaine: "IA / Prompting"
signal: "Prompt regression, compare two versions"
mot_cle: "prompt regression"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [97, 334, 237]
---
## 338. 📉 Prompt regression watcher

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Compare prompt v1 vs v2 on a fixed eval set.

**Quand l'utiliser (triggers)** :
- any request about: prompt regression, compare two versions

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
1. Freeze a 50-case golden set.
2. Run both versions, diff outputs.
3. Ship only if no regression on critical cases.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Did prompt v2 regress on our summarisation evals? » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

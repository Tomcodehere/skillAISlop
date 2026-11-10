---
num: 259
resume: "Orchestrate multiple agents."
lang: "en"
date_ajout: "2026-11"
nom: "Multi-agent orchestrator"
emoji: "🤹"
domaine: "IA / Prompting"
signal: "Multi-agent system, agent handoff"
mot_cle: "multi-agent orchestration"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [100, 224, 1027]
---
## 259. 🤹 Multi-agent orchestrator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Design a multi-agent pipeline with clean handoffs.

**Quand l'utiliser (triggers)** :
- any request about: multi-agent system, agent handoff

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
1. One role per agent + its tools.
2. Handoff protocol: structured output.
3. Supervisor + loop limit + logs.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Orchestrate research -> draft -> review agents for reports. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

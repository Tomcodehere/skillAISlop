---
num: 330
resume: "Instrument an agent with tracing."
lang: "en"
date_ajout: "2026-11"
nom: "Agent observer (tracing)"
emoji: "👁️"
domaine: "IA / Prompting"
signal: "Trace an agent, agent execution log"
mot_cle: "agent tracing"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [97, 256, 330]
---
## 330. 👁️ Agent observer (tracing)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Trace an agent run end to end.

**Quand l'utiliser (triggers)** :
- any request about: trace an agent, agent execution log

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
1. Log every step: input, tool calls, output, tokens, cost.
2. Span/parent structure for multi-agent.
3. Dashboard + anomaly alerts.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Trace our support agent's runs for debugging. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

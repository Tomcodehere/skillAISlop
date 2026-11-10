---
num: 615
resume: "Build an agent self-improvement loop."
lang: "en"
date_ajout: "2026-11"
nom: "Agent self-improvement loop"
emoji: "🔄"
domaine: "IA / Prompting"
signal: "Agent self-improvement, persistent lessons, operating rules"
mot_cle: "agent self-improvement"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [38, 260, 335]
---
## 615. 🔄 Agent self-improvement loop

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Let an agent learn from its mistakes safely.

**Quand l'utiliser (triggers)** :
- any request about: agent self-improvement, persistent lessons, operating rules

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
1. Log failures with cause.
2. Distil into rules added to the system prompt.
3. Human review of new rules.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Self-improvement loop for our support agent. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

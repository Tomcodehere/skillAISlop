---
num: 711
resume: "Wire agent-to-agent communication (A2A)."
lang: "en"
date_ajout: "2026-11"
nom: "A2A & agent-to-agent communication"
emoji: "🔗"
domaine: "IA / Prompting"
signal: "A2A protocol, agent-to-agent, make two AI agents talk, Agent Card, delegation"
mot_cle: "a2a protocol"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [77, 259, 330]
---
## 711. 🔗 A2A & agent-to-agent communication

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : A2A: Agent Cards + tasks + delegation.

**Quand l'utiliser (triggers)** :
- any request about: a2a protocol, agent-to-agent, make two ai agents talk, agent card, delegation

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
1. Each agent exposes an Agent Card (capabilities).
2. Tasks with state; delegate, don't dump context.
3. Auth between agents + audit.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Let our research agent call our writer agent. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

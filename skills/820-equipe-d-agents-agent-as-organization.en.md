---
num: 820
resume: "Run a team of agents."
lang: "en"
date_ajout: "2026-11"
nom: "Agent team ('agent-as-organization')"
emoji: "🏢"
domaine: "IA / Prompting"
signal: "Team of agents, agent-as-organization"
mot_cle: "agent team"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [712, 259, 577]
---
## 820. 🏢 Agent team ('agent-as-organization')

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Roles + handoffs + shared memory (see 259, 712).

**Quand l'utiliser (triggers)** :
- any request about: team of agents, agent-as-organization

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
1. One role per agent + tools.
2. Structured handoffs.
3. Supervisor + budget + logs.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Agent org for content production. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

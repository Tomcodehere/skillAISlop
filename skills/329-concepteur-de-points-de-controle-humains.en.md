---
num: 329
resume: "Design human checkpoints for an agent."
lang: "en"
date_ajout: "2026-11"
nom: "Human checkpoint designer"
emoji: "🧑‍⚖️"
domaine: "IA / Prompting"
signal: "Human approval, validation before agent action"
mot_cle: "human in the loop"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [194, 197, 288]
---
## 329. 🧑‍⚖️ Human checkpoint designer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Decide what needs human approval.

**Quand l'utiliser (triggers)** :
- any request about: human approval, validation before agent action

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
1. Risk-based: money, external comms, destructive.
2. Approval UI + audit trail.
3. Auto-approve low-risk with sampling.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Checkpoints for our purchasing agent. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

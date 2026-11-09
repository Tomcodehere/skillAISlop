---
num: 821
resume: "Automate PR reviews with an agent."
lang: "en"
date_ajout: "2026-11"
nom: "Automated PR review by agent"
emoji: "👀"
domaine: "Développement"
signal: "Agent PR review"
mot_cle: "pr review agent"
nom_court: ""
branche: "D12"
synonymes: []
cross_refs: [10, 68, 925]
---
## 821. 👀 Automated PR review by agent

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Agent checks: tests, style, security, size (see 10, 807).

**Quand l'utiliser (triggers)** :
- any request about: agent pr review

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
1. CI runs the agent on each PR.
2. Comments, not merge.
3. Human approves merge.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Auto-review setup for our repo. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

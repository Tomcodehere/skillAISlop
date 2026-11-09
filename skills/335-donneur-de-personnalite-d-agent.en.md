---
num: 335
resume: "Give an agent a consistent personality."
lang: "en"
date_ajout: "2026-11"
nom: "Agent personality giver"
emoji: "🎭"
domaine: "IA / Prompting"
signal: "Agent personality, assistant tone"
mot_cle: "agent personality"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [33, 34, 288]
---
## 335. 🎭 Agent personality giver

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Define an agent persona that stays in character.

**Quand l'utiliser (triggers)** :
- any request about: agent personality, assistant tone

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
1. 3-5 traits + what it never does.
2. Example dialogues in the system prompt.
3. Test edge cases stay in character.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Personality for our support bot: warm but concise, never promises refunds. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

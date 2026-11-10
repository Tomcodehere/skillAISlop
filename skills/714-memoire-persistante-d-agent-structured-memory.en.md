---
num: 714
resume: "Give an agent structured persistent memory."
lang: "en"
date_ajout: "2026-11"
nom: "Structured agent memory"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Structured agent memory, semantic memory, persistent user preferences"
mot_cle: "structured memory"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [260, 615, 802]
---
## 714. 🧠 Structured agent memory

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Memory: facts/preferences/decisions, retrievable.

**Quand l'utiliser (triggers)** :
- any request about: structured agent memory, semantic memory, persistent user preferences

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
1. Store with embeddings + metadata.
2. Forget/archive old entries (decay).
3. User can inspect/delete (695).

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Memory design for our assistant (see 260). » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

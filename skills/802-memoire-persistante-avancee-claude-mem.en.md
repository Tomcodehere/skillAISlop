---
num: 802
resume: "Give an agent durable memory."
lang: "en"
date_ajout: "2026-11"
nom: "Advanced persistent memory (claude-mem)"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Advanced persistent memory"
mot_cle: "persistent memory"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [714, 260, 615]
---
## 802. 🧠 Advanced persistent memory (claude-mem)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Structured memory + decay + user control (see 260, 714).

**Quand l'utiliser (triggers)** :
- any request about: advanced persistent memory

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
1. Store facts/decisions with embeddings.
2. Retrieval on relevance.
3. User can inspect/delete.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Memory system for our assistant. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

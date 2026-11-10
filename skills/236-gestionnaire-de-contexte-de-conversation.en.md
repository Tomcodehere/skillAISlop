---
num: 236
resume: "Manage long-conversation context."
lang: "en"
date_ajout: "2026-11"
nom: "Conversation context manager"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Long conversation context, compaction"
mot_cle: "context management"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [17, 237, 326]
---
## 236. 🧠 Conversation context manager

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Keep a long conversation coherent: summarise, anchor, compact.

**Quand l'utiliser (triggers)** :
- any request about: long conversation context, compaction

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
1. Pin the key facts/decisions at the top.
2. Summarise every N messages.
3. Re-anchor the goal when drifting.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « This chat is 200 messages long — compact it without losing decisions. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

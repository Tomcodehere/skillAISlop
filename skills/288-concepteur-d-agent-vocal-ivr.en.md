---
num: 288
resume: "Design a phone IVR / voice agent."
lang: "en"
date_ajout: "2026-11"
nom: "Voice IVR agent designer"
emoji: "🎺"
domaine: "IA / Prompting"
signal: "Voice agent, IVR, phone call tree"
mot_cle: "voice ivr agent"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [66, 154, 808]
---
## 288. 🎺 Voice IVR agent designer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Design a voice bot: call tree, ASR/NLU, TTS.

**Quand l'utiliser (triggers)** :
- any request about: voice agent, ivr, phone call tree

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
1. Call flow: greet, intent, routes.
2. Fallback to human + hours.
3. Test with real calls + latency budget.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « IVR for our hotline: booking vs support vs sales. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

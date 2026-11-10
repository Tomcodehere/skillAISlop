---
num: 808
resume: "Build a voice agent with local models."
lang: "en"
date_ajout: "2026-11"
nom: "Voice agent & local voice"
emoji: "🎙️"
domaine: "IA / Prompting"
signal: "Voice agent, local TTS/STT"
mot_cle: "voice agent"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [288, 154, 335]
---
## 808. 🎙️ Voice agent & local voice

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : STT + LLM + local TTS for privacy (see 154, 288).

**Quand l'utiliser (triggers)** :
- any request about: voice agent, local tts/stt

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
1. Local STT (whisper) + TTS (piper).
2. Low latency pipeline.
3. Privacy: nothing leaves the device.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Voice assistant for our kiosk, offline. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

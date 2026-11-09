---
num: 158
resume: "Transcribe and time-align subtitles."
lang: "en"
date_ajout: "2026-11"
nom: "Subtitle writer"
emoji: "📑"
domaine: "Créativité"
signal: "Subtitles, aligned transcription"
mot_cle: "subtitles transcription"
nom_court: ""
branche: "D19"
synonymes: []
cross_refs: [24, 156, 378]
---
## 158. 📑 Subtitle writer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Produce accurate, well-timed subtitles (SRT/VTT).

**Quand l'utiliser (triggers)** :
- any request about: subtitles, aligned transcription

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
1. Transcribe with speaker diarisation.
2. Time-align to audio.
3. Check reading speed (cps).

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Subtitles for this 12-min interview video, SRT, max 42 chars/line. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

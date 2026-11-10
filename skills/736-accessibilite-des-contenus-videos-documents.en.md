---
num: 736
resume: "Make content accessible."
lang: "en"
date_ajout: "2026-11"
nom: "Content accessibility (videos, docs)"
emoji: "♿"
domaine: "Design"
signal: "Subtitle a video, make a document accessible, transcription, alt-text, accessible PDF"
mot_cle: "accessible content"
nom_court: ""
branche: "D22"
synonymes: []
cross_refs: [158, 686, 454]
---
## 736. ♿ Content accessibility (videos, docs)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Captions, alt-text, tagged PDFs, contrast.

**Quand l'utiliser (triggers)** :
- any request about: subtitle a video, make a document accessible, transcription, alt-text, accessible pdf

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
1. Auto-captions then human-check.
2. Alt-text per image.
3. PDF tagged + reading order.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Make our webinar recording accessible. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

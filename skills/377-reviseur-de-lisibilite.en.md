---
num: 377
resume: "Improve a text's readability."
lang: "en"
date_ajout: "2026-11"
nom: "Readability reviser"
emoji: "📖"
domaine: "Rédaction"
signal: "Reading level, sentence too long"
mot_cle: "readability"
nom_court: ""
branche: "D18"
synonymes: []
cross_refs: [281, 401, 327]
---
## 377. 📖 Readability reviser

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Make a text readable: short sentences, plain words.

**Quand l'utiliser (triggers)** :
- any request about: reading level, sentence too long

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
1. Measure readability score.
2. Split long sentences, cut filler, active voice.
3. Re-measure + keep meaning.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « This legal notice is unreadable — simplify it. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 327
resume: "Compress a verbose AI output."
lang: "en"
date_ajout: "2026-11"
nom: "AI response compressor"
emoji: "🗜️"
domaine: "IA / Prompting"
signal: "Response too long, compress the output"
mot_cle: "output compression"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [5, 100, 719]
---
## 327. 🗜️ AI response compressor

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Get the same info in fewer tokens.

**Quand l'utiliser (triggers)** :
- any request about: response too long, compress the output

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
1. Ask for bullet list / JSON / table.
2. Set a hard output limit.
3. Two-pass: draft then compress.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Summarise this 50-page transcript in 10 bullets. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

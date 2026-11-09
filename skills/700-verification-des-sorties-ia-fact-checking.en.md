---
num: 700
resume: "Fact-check AI outputs before using them."
lang: "en"
date_ajout: "2026-11"
nom: "AI output fact-checking"
emoji: "🔍"
domaine: "IA / Prompting"
signal: "Verify an AI answer, fact-check, detect hallucinations, check AI sources"
mot_cle: "fact-check ai"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [37, 18, 944]
---
## 700. 🔍 AI output fact-checking

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Verify AI claims: sources, dates, cross-check.

**Quand l'utiliser (triggers)** :
- any request about: verify an ai answer, fact-check, detect hallucinations, check ai sources

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
1. Ask for sources; open them.
2. Cross-check key facts with 2 independent sources.
3. Hallucination tells: over-specific fake citations.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Fact-check this AI summary of a study. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 692
resume: "Secure prompts against injection."
lang: "en"
date_ajout: "2026-11"
nom: "Prompt security & injection"
emoji: "🛡️"
domaine: "Sécurité"
signal: "Prompt injection, jailbreak, data leak via prompt, secure an AI agent, guardrails"
mot_cle: "prompt injection"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [195, 37, 818]
---
## 692. 🛡️ Prompt security & injection

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Defend against prompt injection (see 195, 37).

**Quand l'utiliser (triggers)** :
- any request about: prompt injection, jailbreak, data leak via prompt, secure an ai agent, guardrails

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
1. Delimiters + privilege separation + output filtering.
2. Canary strings, red-team (37) before shipping.
3. Never put secrets in the prompt.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Harden our agent against injection attacks. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

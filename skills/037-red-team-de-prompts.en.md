---
num: 37
resume: "Red-team a prompt: find failure modes and jailbreaks before production."
lang: "en"
date_ajout: "2026-11"
nom: "🛡️ Prompt red-team"
emoji: "🛡️"
domaine: "Data & IA"
signal: "Red-team, prompt flaw, jailbreak"
mot_cle: "prompt red-team jailbreak"
nom_court: "Red-team"
branche: "D4"
synonymes: []
cross_refs: [237, 17, 338]
---
## 37. 🛡️ Prompt red-team

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Red-team a prompt: find failure modes and jailbreaks before production.

**Quand l'utiliser (triggers)** :
- secure a system prompt before shipping

**Hors périmètre** :
- pentest of the whole app (skill 504)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a prompt security researcher. You generate 20 attack attempts (extraction, injection, jailbreak, role-play), classify each result (blocked/partial/leaked), and propose hardening: delimiters, output filtering, canary strings.

**Inputs requis** :
- the system prompt to test + the model

**Méthode** :
1. Generate 20 attack attempts.
2. Classify results.
3. Propose hardening measures.

**Sorties attendues** :
- attack report + hardening list

**Exemple de prompt** :
> « « Red-team this customer-support system prompt against data extraction. » »

**Cas d'usage** : LLM app security. Chains with 692.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

---
num: 839
resume: "Spot spear phishing and report it."
lang: "en"
date_ajout: "2026-11"
nom: "Spear phishing & reporting"
emoji: "🎯"
domaine: "Sécurité"
signal: "Spear phishing, targeted attack, report it"
mot_cle: "spear phishing"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [685, 757, 509]
---
## 839. 🎯 Spear phishing & reporting

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Hyper-personalised = more dangerous; verify out-of-band (see 685, 824).

**Quand l'utiliser (triggers)** :
- any request about: spear phishing, targeted attack, report it

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
1. Check sender domain carefully.
2. Verify the request by another channel.
3. Report to IT + 33700 if financial.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « This email knows my project name — phishing? » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

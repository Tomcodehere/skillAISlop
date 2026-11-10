---
num: 754
resume: "Respond to a security incident."
lang: "en"
date_ajout: "2026-11"
nom: "Security incident response"
emoji: "🚨"
domaine: "Sécurité"
signal: "Respond to a cyberattack, incident procedure, playbook, CNIL notification"
mot_cle: "incident response"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [256, 441, 199]
---
## 754. 🚨 Security incident response

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Contain, eradicate, recover + notify if personal data (444, 199).

**Quand l'utiliser (triggers)** :
- any request about: respond to a cyberattack, incident procedure, playbook, cnil notification

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
1. Isolate affected systems.
2. Preserve logs (441).
3. Notify CNIL in 72h if data breach + comms (696).

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Ransomware on the file server — response. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

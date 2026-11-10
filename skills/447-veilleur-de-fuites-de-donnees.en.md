---
num: 447
resume: "Monitor for leaked credentials/data."
lang: "en"
date_ajout: "2026-11"
nom: "Data leak watcher"
emoji: "🔎"
domaine: "Sécurité"
signal: "Exposed data, leaked credentials"
mot_cle: "data leak monitoring"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [440, 444, 95]
---
## 447. 🔎 Data leak watcher

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Watch for our domain in breaches and leaks.

**Quand l'utiliser (triggers)** :
- any request about: exposed data, leaked credentials

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
1. HIBP domain check + dark-web monitoring.
2. Alert on new exposures of our domain.
3. Reset + 2FA + rotate on hit.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Set up leak monitoring for our company domain. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

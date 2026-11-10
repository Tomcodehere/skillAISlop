---
num: 664
resume: "Do admin procedures online."
lang: "en"
date_ajout: "2026-11"
nom: "Online admin procedures"
emoji: "🖥️"
domaine: "Bureau"
signal: "Online admin, ANTS, ameli, impots.gouv, CAF, Pôle emploi"
mot_cle: "admin online"
nom_court: ""
branche: "D25"
synonymes: []
cross_refs: [217, 581, 955]
---
## 664. 🖥️ Online admin procedures

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Navigate gov portals: accounts, documents, deadlines.

**Quand l'utiliser (triggers)** :
- any request about: online admin, ants, ameli, impots.gouv, caf, pôle emploi

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
1. One account per portal, 2FA on.
2. Upload scans (PDF/JPG) beforehand.
3. Save every acknowledgement of receipt.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Renew my carte grise online (ANTS). » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

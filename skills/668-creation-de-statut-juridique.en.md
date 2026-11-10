---
num: 668
resume: "Choose the right legal status."
lang: "en"
date_ajout: "2026-11"
nom: "Legal status creation"
emoji: "🏢"
domaine: "Gestion"
signal: "Choose legal status: SASU, EURL, auto-entrepreneur, sole trader, company creation"
mot_cle: "legal status"
nom_court: ""
branche: "D29"
synonymes: []
cross_refs: [562, 588, 16]
---
## 668. 🏢 Legal status creation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Compare statuses: liability, tax, social (not legal/tax advice).

**Quand l'utiliser (triggers)** :
- any request about: choose legal status: sasu, eurl, auto-entrepreneur, sole trader, company creation

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
1. Liability: sole trader vs company (SASU/EURL/SARL).
2. Tax: IR vs IS; social: TNS vs assimilé salarié.
3. Register + bank + accounting setup.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « SASU vs auto-entrepreneur for a consultant. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

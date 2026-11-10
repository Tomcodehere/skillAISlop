---
num: 119
resume: "Turn a guide into a FAQ."
lang: "en"
date_ajout: "2026-11"
nom: "FAQ generator"
emoji: "❓"
domaine: "Rédaction"
signal: "FAQ from a guide"
mot_cle: "faq generator"
nom_court: "FAQ writer"
branche: "D18"
synonymes: []
cross_refs: [56, 130, 254]
---
## 119. ❓ FAQ generator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Turn any guide into a useful FAQ.

**Quand l'utiliser (triggers)** :
- FAQ page from existing docs

**Hors périmètre** :
- (not covered — see cross-refs)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a support writer. You extract the real questions users ask, write plain answers, order by frequency, and link each answer to the source section.

**Inputs requis** :
- the guide/docs + past support tickets

**Méthode** :
1. Extract real questions.
2. Plain answers linked to source.
3. Order by frequency.

**Sorties attendues** :
- the FAQ

**Exemple de prompt** :
> « « FAQ from our 20-page onboarding guide + 100 support tickets. » »

**Cas d'usage** : Support sites, docs. Chains with 56.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

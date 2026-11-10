---
num: 505
resume: "Schedule patches by risk."
lang: "en"
date_ajout: "2026-11"
nom: "Patch & CVE scheduler"
emoji: "🩹"
domaine: "Sécurité"
signal: "Patches, CVE, remediation plan"
mot_cle: "patch management"
nom_court: ""
branche: "D23"
synonymes: []
cross_refs: [267, 507, 454]
---
## 505. 🩹 Patch & CVE scheduler

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Prioritise CVEs by exploitability + exposure.

**Quand l'utiliser (triggers)** :
- any request about: patches, cve, remediation plan

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
1. Inventory assets + versions.
2. CVSS + EPSS scoring, internet-facing first.
3. Patch windows + rollback + verify.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « We have 30 unpatched CVEs — remediation plan. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

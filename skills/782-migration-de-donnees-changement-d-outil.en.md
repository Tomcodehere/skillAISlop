---
num: 782
resume: "Migrate data between tools safely."
lang: "en"
date_ajout: "2026-11"
nom: "Data migration & tool switch"
emoji: "🚚"
domaine: "Data"
signal: "Migrate data from one tool to another, export/import, software change"
mot_cle: "data migration"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [462, 92, 95]
---
## 782. 🚚 Data migration & tool switch

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Export -> map -> import -> verify counts (see 86, 354).

**Quand l'utiliser (triggers)** :
- any request about: migrate data from one tool to another, export/import, software change

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
1. Export full data + attachments.
2. Field mapping doc.
3. Test import on a copy, verify.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Migrate 5 years of Notion to Confluence. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

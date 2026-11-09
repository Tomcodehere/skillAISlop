---
num: 268
resume: "Work with PDFs: extract, merge, OCR."
lang: "en"
date_ajout: "2026-11"
nom: "PDF wrangler"
emoji: "✂️"
domaine: "Bureau"
signal: "Extract table from PDF, merge PDFs, OCR"
mot_cle: "pdf tools"
nom_court: ""
branche: "D18"
synonymes: []
cross_refs: [5, 115, 107]
---
## 268. ✂️ PDF wrangler

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Extract/merge/OCR PDFs reliably.

**Quand l'utiliser (triggers)** :
- any request about: extract table from pdf, merge pdfs, ocr

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
1. Try text layer first, OCR if scanned.
2. Extract tables to CSV with layout check.
3. Merge/split + compress.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Extract the invoice table from this scanned PDF to CSV. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

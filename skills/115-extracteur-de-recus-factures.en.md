---
num: 115
resume: "Extract expenses from receipts and invoices."
lang: "en"
date_ajout: "2026-11"
nom: "Receipt & invoice extractor"
emoji: "🧾"
domaine: "Bureau"
signal: "Receipts and invoices, expense extraction"
mot_cle: "receipts invoices"
nom_court: "Expense extractor"
branche: "D17"
synonymes: []
cross_refs: [27, 43, 543]
---
## 115. 🧾 Receipt & invoice extractor

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Extract structured expense data from receipts/invoices.

**Quand l'utiliser (triggers)** :
- digitise my expenses

**Hors périmètre** :
- (not covered — see cross-refs)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are an accounting assistant. You extract per document: date, vendor, amount, VAT, category — into a clean table/CSV, flagging low-confidence fields for review.

**Inputs requis** :
- the receipt/invoice images or PDFs

**Méthode** :
1. Extract fields per document.
2. Clean table/CSV output.
3. Flag low-confidence fields.

**Sorties attendues** :
- expense table/CSV

**Exemple de prompt** :
> « « Extract these 23 restaurant receipts into a CSV for my accountant. » »

**Cas d'usage** : Expense reports, accounting. Chains with 43.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

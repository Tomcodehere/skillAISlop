---
num: 725
resume: "Ask questions grounded in your own documents."
lang: "en"
date_ajout: "2026-11"
nom: "NotebookLM & source-grounded answers"
emoji: "📓"
domaine: "Recherche"
signal: "NotebookLM, answers grounded only in my documents, personal RAG over PDFs"
mot_cle: "notebooklm"
nom_court: ""
branche: "D17"
synonymes: []
cross_refs: [102, 690, 944]
---
## 725. 📓 NotebookLM & source-grounded answers

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Upload sources, get cited answers only from them.

**Quand l'utiliser (triggers)** :
- any request about: notebooklm, answers grounded only in my documents, personal rag over pdfs

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
1. Upload the PDFs/docs.
2. Ask; answers cite the sources.
3. Check citations yourself (700).

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Summarise these 10 papers with citations. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

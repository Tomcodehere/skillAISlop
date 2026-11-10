---
num: 690
resume: "Build a RAG over your documents."
lang: "en"
date_ajout: "2026-11"
nom: "RAG & augmented retrieval"
emoji: "🔎"
domaine: "Data & IA"
signal: "RAG, retrieval-augmented generation, internal knowledge base, document indexing, semantic search, embeddings"
mot_cle: "rag"
nom_court: ""
branche: "D14"
synonymes: []
cross_refs: [98, 266, 784]
---
## 690. 🔎 RAG & augmented retrieval

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : RAG: chunk, embed, retrieve, cite.

**Quand l'utiliser (triggers)** :
- any request about: rag, retrieval-augmented generation, internal knowledge base, document indexing, semantic search, embeddings

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
1. Chunk with overlap, metadata per chunk.
2. Vector store + hybrid search + rerank.
3. Always cite sources; eval faithfulness.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « RAG over our 5k internal docs with citations. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

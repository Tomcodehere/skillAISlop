---
num: 721
resume: "Turn a corpus into a knowledge graph."
lang: "en"
date_ajout: "2026-11"
nom: "Graphify: corpus to knowledge graph"
emoji: "🕸️"
domaine: "Data & IA"
signal: "Turn documents into a knowledge graph"
mot_cle: "knowledge graph"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [287, 95, 114]
---
## 721. 🕸️ Graphify: corpus to knowledge graph

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Extract entities + relations from documents.

**Quand l'utiliser (triggers)** :
- any request about: turn documents into a knowledge graph

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
1. Extract entities/relations per doc (LLM).
2. Build the graph (Neo4j/networkx).
3. Query + visualise the graph.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Graph our 200 research papers. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

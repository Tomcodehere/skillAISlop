---
num: 1478
nom: "GraphRAG : interroger un graphe de connaissances (2027)"
emoji: "🕸️"
domaine: "Data & IA"
signal: "Construire un GraphRAG en 2027 : extraire entités et relations d'un corpus (LLM + NER) dans un graphe (Neo4j, Kuzu, NetworkX), requêter en Cypher/Gremlin ou via le LLM (text2cypher), combiner avec du vectoriel. Utilise quand les réponses nécessitent des relations multi-sauts (qui a travaillé avec qui, chaîne logistique). N'utilise pas si un RAG classique suffit."
mot_cle: "graphrag neo4j kuzu graphe connaissances text2cypher entités relations"
nom_court: "GraphRAG"
branche: "D14"
synonymes: ["extraire graphe de connaissances corpus", "Neo4j ou Kuzu 2027", "requêtes multi-sauts RAG graphe"]
cross_refs: [721, 690, 1477]
tags: ["2027"]
depends_on: [721]
---

## 1478. 🕸️ GraphRAG : interroger un graphe de connaissances (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire un GraphRAG en 2027 : extraction LLM des entités/relations du corpus dans un graphe (Neo4j/Kuzu), requêtes multi-sauts (Cypher via text2cypher ou parcours de graphe), combiné au retrieval vectoriel.

**Quand l'utiliser (triggers)** :
- 'Qui a décidé de X et pourquoi, lié à Y ?' — RAG classique échoue
- Extraire un graphe de connaissances d'un corpus
- Neo4j ou Kuzu pour le GraphRAG ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte GraphRAG. Tu décris le pipeline (chunking → LLM extrait entités+relations avec schéma d'ontologie → graphe Neo4j/Kuzu → requêtes : vectoriel pour le contexte + graphe pour les relations multi-sauts, réponse citée). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le corpus (docs internes, contrats, emails)
- L'ontologie (types d'entités/relations du domaine)
- Le moteur de graphe (Neo4j, Kuzu embarqué, AWS Neptune)

**Méthode** :
1. Définir l'ontologie (entités : Personne, Contrat, Projet... ; relations : signé, dépend_de...).
2. Extraire par chunk avec un LLM (prompt strict JSON) → nœuds et arêtes, dédupliquer.
3. Charger dans Neo4j/Kuzu, indexer les noms (full-text) + embeddings sur les nœuds.
4. Requêter : retrieval vectoriel (contexte) + parcours de graphe (relations) ou text2cypher.
5. Générer la réponse avec citations (doc + nœud du graphe). Évaluer sur 30 questions multi-sauts.

**Sorties attendues** :
- Le graphe de connaissances construit (entités + relations)
- La chaîne de requête hybride (vectoriel + graphe)
- L'eval sur 30 questions multi-sauts vs RAG classique

**Exemple de prompt** :
> « On veut répondre à 'quels contrats dépendent du fournisseur X et quels risques ?' : construis un GraphRAG (extraction LLM → Neo4j → requêtes multi-sauts + vectoriel). »

**Cas d'usage** : Due diligence, renseignement, conformité, recherche interne complexe. S'articule avec skills 721 (Graphify), 690 (RAG) et 1477 (hybride).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

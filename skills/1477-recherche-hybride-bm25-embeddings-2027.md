---
num: 1477
date_ajout: "2026-11"
nom: "Recherche hybride BM25 + embeddings (2027)"
emoji: "🔍"
domaine: "Data & IA"
signal: "Combiner recherche lexicale (BM25) et sémantique (embeddings) en 2027 pour un meilleur retrieval : BM25 attrape les termes exacts (codes, noms propres), les embeddings le sens ; fusion par RRF ou score pondéré. Utilise quand le RAG pur vectoriel rate les requêtes précises. N'utilise pas si le lexical seul suffit."
mot_cle: "recherche hybride BM25 embeddings RRF fusion retrieval"
nom_court: "Hybride BM25+vec"
branche: "D14"
synonymes: ["BM25 plus embeddings combinés", "fusion RRF scores retrieval", "RAG hybride lexical sémantique"]
cross_refs: [690, 1443, 1444]
tags: ["2027"]
depends_on: [690]
---

## 1477. 🔍 Recherche hybride BM25 + embeddings (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Améliorer le retrieval d'un RAG en 2027 en hybride : BM25 (termes exacts, codes, ids) + embeddings (sens), fusion des scores (RRF k=60 ou pondération 0.3/0.7), évalué sur un golden set de requêtes.

**Quand l'utiliser (triggers)** :
- Mon RAG rate les requêtes avec des codes/noms exacts
- Combiner BM25 et vectoriel
- RRF fusion des scores retrieval

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte retrieval hybride. Tu expliques pourquoi chaque voie échoue seule (vectoriel rate 'ERREUR-4021', BM25 rate la paraphrase), la fusion RRF (rank-based, robuste) ou pondérée, et l'eval top-k avant/après sur 50 requêtes. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le corpus indexé (vectoriel seul aujourd'hui ?)
- Les requêtes utilisateurs problématiques
- L'outil (Weaviate, Vespa, Qdrant, pgvector + pg_bm25)

**Méthode** :
1. Indexer le corpus en double : embeddings (1443) + index BM25 (pg_bm25, Vespa, Weaviate).
2. Requête : lancer les 2 recherches (top-20 chacune).
3. Fusionner : RRF (k=60) ou score pondéré (0.3 lexical + 0.7 sémantique).
4. Évaluer : top-5 hit rate hybride vs vectoriel seul sur 50 requêtes réelles.
5. Ajuster les poids selon le domaine (technique = plus de lexical).

**Sorties attendues** :
- L'index hybride (BM25 + embeddings) en place
- La stratégie de fusion (RRF/pondérée) retenue
- Le hit rate avant/après (amélioration mesurée)

**Exemple de prompt** :
> « Notre RAG juridique rate les requêtes avec références d'articles exactes ('L. 1234-5') : passe en hybride BM25 + embeddings (fusion RRF, eval sur 50 requêtes). »

**Cas d'usage** : RAG technique/juridique, e-commerce (codes produits). S'articule avec skills 690 (RAG), 1443 (embeddings) et 1444 (chunking).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

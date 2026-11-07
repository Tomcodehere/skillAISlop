---
num: 1679
date_ajout: "2026-11"
nom: "Choisir sa vector DB : pgvector, Qdrant, Milvus, Weaviate, LanceDB"
emoji: "🧮"
domaine: "Data & IA"
signal: "Choisir sa base vectorielle en 2027 selon le volume et le déploiement : pgvector (déjà Postgres 1229, sous 1M vecteurs, zéro infra) ; Qdrant/Milvus/Weaviate (dédié, supérieur à 10M vecteurs, filtres riches, HNSW) ; LanceDB (embarqué/fichier, multimodal 1671) ; Pinecone/Weaviate cloud (managé, cher). Critères : volume, filtres metadata, self-host vs cloud, coût. N'utilise pas si sous 100k vecteurs (pgvector suffit)."
mot_cle: "choisir vector DB 2027 pgvector Qdrant Milvus Weaviate LanceDB volume filtres HNSW"
nom_court: "Choisir vector DB"
branche: "D14"
synonymes: ["pgvector suffit sous 1M de vecteurs (déjà dans Postgres 1229)", "Qdrant ou Milvus pour 100M vecteurs avec filtres metadata", "LanceDB embarqué pour l'edge/offline (1671)"]
cross_refs: [1443, 1477, 1662]
tags: ["2027"]
depends_on: [1443]
---

## 1679. 🧮 Choisir sa vector DB en 2027 : pgvector, Qdrant, Milvus, Weaviate, LanceDB (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir sa vector DB en 2027 : pgvector (dans Postgres, < 1M vecteurs, zéro infra), Qdrant/Milvus/Weaviate (dédié, gros volume, filtres, HNSW), LanceDB (embarqué 1671), cloud managé (Pinecone) — selon volume, filtres, self-host et coût.

**Quand l'utiliser (triggers)** :
- on a 500k embeddings dans Postgres pgvector, ça rame
- Qdrant vs Milvus vs Weaviate en 2027 comparatif
- LanceDB embarqué sur mobile (1671) sans serveur

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte RAG infra. Tu fais la matrice : volume (100k → pgvector OK ; 10M+ → dédié Qdrant/Milvus), filtres metadata (Qdrant/Milvus forts), déploiement (self-host vs cloud Pinecone/Weaviate), coût (self-host ~ VPS, cloud au vecteur/requête). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le volume de vecteurs et la croissance prévue
- Les besoins de filtres (métadonnées) et hybrides (1477)
- Self-host vs cloud managé + budget

**Méthode** :
1. pgvector : si Postgres déjà là (1229) et volume < 1M vecteurs, index HNSW, zéro infra ajoutée.
2. Qdrant : Rust, rapide, filtres riches, self-host facile (docker 1411), bon compromis 2027.
3. Milvus : très gros volume (100M+), distribué, k8s (609). Weaviate : GraphQL, hybride natif.
4. LanceDB : embarqué/fichier (1671), offline, multimodal — pas pour du multi-users serveur.
5. Cloud (Pinecone, Weaviate Cloud) : zéro ops mais coût au volume + données chez eux (souveraineté 1633).
6. POC : 1M vecteurs, requête hybride (1477) + filtres, mesurer p99 latence et coût.

**Sorties attendues** :
- La matrice de choix + la vector DB retenue (POC latence p99 mesurée)
- L'index HNSW configuré
- Le plan de migration si croissance x10 prévue

**Exemple de prompt** :
> « Notre RAG a 800k embeddings dans pgvector (Postgres) et rame à 800 ms : matrice de choix 2027 (pgvector/Qdrant/Milvus/LanceDB), POC à 1M vecteurs avec filtres (1477), on retient Qdrant (p99 < 100 ms). »

**Cas d'usage** : Tout RAG/vector search. S'articule avec skills 1443 (embeddings), 1477 (hybride), 1662 (Iceberg) et 1671 (LanceDB).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

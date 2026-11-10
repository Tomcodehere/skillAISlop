---
num: 1444
resume: "Optimiser le chunking d'un corpus RAG en 2027 : chunks de 200-500 tokens avec overlap 10-20 %, découpage sémantique (titres/paragraphes) ou hiérarchique, métadonnées par chunk, validé par un eval de retrieval. Étape 1 : Évaluer le chunking actuel : top-5 hit rate sur 50 requêtes réelles."
lang: "fr"
date_ajout: "2026-11"
nom: "Chunking avance pour le RAG"
emoji: "✂️"
domaine: "IA / Prompting"
signal: "Choisir la stratégie de chunking d'un corpus pour un RAG en 2027 : taille (200-500 tokens), recouvrement (overlap 10-20 %), découpage sémantique (titres, paragraphes), chunking hiérarchique (résumé parent), métadonnées par chunk. Utilise quand la qualité du retrieval est insuffisante. N'utilise pas sans mesurer (eval retrieval)."
mot_cle: "chunking RAG overlap sémantique hiérarchique 200-500 tokens"
nom_court: "Chunking avancé"
branche: "D14"
synonymes: ["découper documents pour RAG", "overlap 20% chunking", "chunking hiérarchique résumé parent"]
cross_refs: [690, 1477, 1443]
tags: ["2027"]
depends_on: [690]
---

## 1444. ✂️ Chunking avance pour le RAG (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Optimiser le chunking d'un corpus RAG en 2027 : chunks de 200-500 tokens avec overlap 10-20 %, découpage sémantique (titres/paragraphes) ou hiérarchique, métadonnées par chunk, validé par un eval de retrieval.

**Quand l'utiliser (triggers)** :
- Mon RAG retrouve les mauvais passages
- Taille de chunk 200 ou 800 tokens ?
- Chunking sémantique vs fixe

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte RAG (chunking). Tu compares fixe vs sémantique vs hiérarchique (parent résumé + chunks fins), tu donnes l'overlap 10-20 %, et tu exiges un eval retrieval (top-k hit rate) avant/après sur 50 requêtes. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le corpus (PDF, HTML, markdown)
- La stratégie actuelle et son score retrieval
- Les requêtes types des utilisateurs

**Méthode** :
1. Évaluer le chunking actuel : top-5 hit rate sur 50 requêtes réelles.
2. Tester 3 stratégies : fixe 400 tokens/overlap 50, sémantique (paragraphes), hiérarchique (résumé parent).
3. Ajouter les métadonnées par chunk (titre, page, date) pour le filtrage.
4. Re-mesurer le hit rate et la pertinence (skill 1397).
5. Choisir la meilleure stratégie et la documenter.

**Sorties attendues** :
- La stratégie de chunking retenue
- Le hit rate avant/après
- Les métadonnées ajoutées par chunk

**Exemple de prompt** :
> « Mon RAG juridique répond à côté : optimise le chunking (fixe vs sémantique vs hiérarchique, overlap, métadonnées) avec un eval retrieval sur 50 requêtes. »

**Cas d'usage** : Tout RAG. S'articule avec skills 690 (RAG), 1477 (hybride BM25+dense) et 1443 (embeddings).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

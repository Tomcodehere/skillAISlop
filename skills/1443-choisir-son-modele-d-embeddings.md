---
num: 1443
date_ajout: "2026-11"
nom: "Choisir son modele d'embeddings"
emoji: "🔢"
domaine: "IA / Prompting"
signal: "Choisir un modèle d'embeddings en 2027 selon le cas d'usage : multilingue (E5, multilingual-e5), code (codebert,voyage-code), juridique/médical spécialisé, dimension (384 vs 1024 vs 3072), coût, MTEB benchmark. Utilise quand on construit un RAG ou une recherche sémantique. N'utilise pas pour la génération."
mot_cle: "choisir modèle embeddings MTEB dimension multilingue"
nom_court: "Embeddings"
branche: "D14"
synonymes: ["quel modèle embedding 2027", "MTEB benchmark embeddings", "dimension 384 ou 3072"]
cross_refs: [690, 1477, 1442]
tags: ["2027"]
depends_on: [690]
---

## 1443. 🔢 Choisir son modele d'embeddings (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir le bon modèle d'embeddings en 2027 pour un RAG/recherche sémantique : comparer sur le MTEB (multilingue, code, domaine), la dimension (coût stockage), et valider sur ses propres données (retrieval eval).

**Quand l'utiliser (triggers)** :
- Quel modèle d'embeddings choisir en 2027 ?
- E5 vs OpenAI ada vs voyage : comparatif
- Benchmarker les embeddings sur mes données

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte retrieval. Tu cites les familles (multilingual-e5, BGE, OpenAI text-embedding-3, Voyage, Cohere) avec leurs dimensions, tu insistes sur le benchmark MTEB + un eval retrieval sur 50 vraies requêtes du domaine. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La langue (FR seul ou multilingue ?)
- Le domaine (général, code, juridique, médical)
- Le volume (coût stockage = dim × nb vecteurs)

**Méthode** :
1. Lister 3-5 modèles candidats selon langue/domaine (MTEB leaderboard).
2. Benchmarker sur 50 requêtes réelles du projet (top-5 hit rate).
3. Comparer dimension/coût (384 dim suffit souvent en FR) et latence.
4. Choisir le meilleur compromis qualité/coût.
5. Re-benchmarker à chaque changement de modèle majeur.

**Sorties attendues** :
- Le modèle d'embeddings retenu (justifié)
- Le score retrieval sur les 50 requêtes
- Le calcul coût stockage (dim × volume)

**Exemple de prompt** :
> « Je construis un RAG juridique en français : quel modèle d'embeddings choisir en 2027 (MTEB, benchmark sur 50 vraies requêtes, coût stockage) ? »

**Cas d'usage** : RAG, recherche sémantique, cache sémantique, clustering. S'articule avec skills 690 (RAG), 1477 (hybride) et 1442 (cache).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

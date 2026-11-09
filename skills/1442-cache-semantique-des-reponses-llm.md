---
num: 1442
resume: "Mettre en place un cache sémantique LLM en 2027 : embedder la requête entrante, si similarité supérieure à 0,95 avec une requête cachée, renvoyer la réponse en cache (économie de tokens et latence). Étape 1 : Embedder chaque requête entrante (modèle léger)."
date_ajout: "2026-11"
nom: "Cache semantique des reponses LLM"
emoji: "💾"
domaine: "IA / Prompting"
signal: "Mettre en cache sémantique les réponses LLM en 2027 : si une requête est sémantiquement proche d'une précédente (similarité embeddings au-dessus du seuil, ex. 0,95), renvoyer la réponse cachée au lieu de réinférer. Utilise quand beaucoup de requêtes similaires. N'utilise pas si la fraîcheur est critique."
mot_cle: "cache sémantique réponses LLM similarité embeddings seuil"
nom_court: "Cache sémantique"
branche: "D14"
synonymes: ["réponses LLM en cache sémantique", "requêtes similaires même réponse", "éviter réinférer questions proches"]
cross_refs: [1164, 1443, 694]
tags: ["2027"]
depends_on: [1443]
---

## 1442. 💾 Cache semantique des reponses LLM (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place un cache sémantique LLM en 2027 : embedder la requête entrante, si similarité supérieure à 0,95 avec une requête cachée, renvoyer la réponse en cache (économie de tokens et latence).

**Quand l'utiliser (triggers)** :
- Les users posent 100 fois la même question reformulée
- Cache sémantique des réponses LLM
- seuil similarité 0,95 cache

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de cache LLM. Tu expliques le flow (embed requête → recherche vectorielle dans le cache → si cosinus supérieur à 0,95, renvoyer la réponse cachée + TTL), le choix du modèle d'embedding, et le risque de staleness. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'historique des requêtes/réponses (à cacher)
- Le modèle d'embedding (skill 1443)
- Le seuil de similarité et le TTL

**Méthode** :
1. Embedder chaque requête entrante (modèle léger).
2. Rechercher dans le vector store du cache (requêtes passées + réponses).
3. Si similarité supérieure à 0,95 : renvoyer la réponse cachée (log 'cache hit').
4. Sinon : inférence normale puis stocker requête+réponse dans le cache (avec TTL).
5. Surveiller le hit rate et la fraîcheur (TTL ex. 24 h pour du factuel).

**Sorties attendues** :
- Le cache sémantique opérationnel
- Le hit rate et l'économie de tokens mesurés
- Le seuil et TTL retenus

**Exemple de prompt** :
> « Notre support IA reçoit 500 questions similaires/jour : mets un cache sémantique (embeddings, seuil 0,95, TTL 24 h) pour diviser la facture LLM. »

**Cas d'usage** : Support, FAQ, chatbots à fort volume. S'articule avec skills 1164 (cache inférence), 1443 (embeddings) et 694 (coût tokens).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

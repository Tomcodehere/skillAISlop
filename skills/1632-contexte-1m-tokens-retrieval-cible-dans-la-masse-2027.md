---
num: 1632
date_ajout: "2026-11"
nom: "Contexte 1M tokens : retrieval cible dans la masse (2027)"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Exploiter les contextes 1M tokens des modèles 2027 sans les noyer : ne PAS tout mettre (lost in the middle 1430), mais indexer le corpus (embeddings 1443) et injecter seulement les k passages pertinents (retrieval) + la question en début/fin. Utilise pour codebases/contrats entiers. N'utilise pas pour une conversation courte."
mot_cle: "contexte 1M tokens retrieval ciblé k passages embeddings injecter 2027"
nom_court: "1M retrieval"
branche: "D14"
synonymes: ["j'ai 1M de tokens de contexte, quoi y mettre", "lost in the middle : ne pas tout charger", "retrieval : injecter seulement les k passages pertinents"]
cross_refs: [1430, 1443, 1444]
tags: ["2027"]
depends_on: [1430]
---

## 1632. 🧠 Contexte 1M tokens : retrieval cible dans la masse (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Exploiter un contexte de 1M tokens en 2027 sans effet lost-in-the-middle (1430) : indexer le corpus en embeddings (1443), récupérer les k=5-10 passages les plus pertinents, les injecter avec la question en début/fin de contexte.

**Quand l'utiliser (triggers)** :
- je mets toute la codebase dans le contexte et le LLM répond à côté
- 1M tokens : retrieval ciblé plutôt que tout charger
- question en début et fin de contexte (primauté/récence)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte RAG massif. Tu fais : indexer le corpus (chunking 1444 + embeddings 1443) dans un vector store, à la requête récupérer top-k (k=5-10), construire le contexte = [système] + [passages récupérés avec source] + [question] en début ET fin. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le gros corpus (codebase, contrats, docs)
- Le modèle 1M tokens
- La requête utilisateur

**Méthode** :
1. Indexer : chunking sémantique (1444), embeddings (1443), stockés avec métadonnées (fichier, ligne).
2. Requête : embedder la question, top-k=8 passages (similarité), rerank optionnel (cross-encoder).
3. Construire le contexte : instruction système en tête, puis les passages avec marqueurs [fichier:ligne], puis la question répétée en fin (récence).
4. Ne jamais remplir les 1M : laisser de la marge (le modèle raisonne mieux avec 50-200k utiles qu'avec 1M de bruit).
5. Évaluer : précision des réponses vs RAG classique (1397) sur 50 questions.

**Sorties attendues** :
- Le pipeline retrieval sur 1M tokens (top-k injecté)
- La preuve anti-lost-in-the-middle (question début+fin)
- L'eval précision vs chargement total

**Exemple de prompt** :
> « Je charge toute ma codebase (800k tokens) dans le contexte et le LLM répond à côté : passe en retrieval (embeddings, top-8 passages + question en début/fin) dans la fenêtre 1M. »

**Cas d'usage** : Codebases entières, due diligence, contrats longs. S'articule avec skills 1430 (contexte long), 1443 (embeddings) et 1444 (chunking).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

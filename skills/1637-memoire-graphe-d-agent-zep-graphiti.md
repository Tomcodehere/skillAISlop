---
num: 1637
resume: "Équiper un agent d'une mémoire graphe en 2027 (Zep/Graphiti) : entités, relations, épisodes datés dans un graphe temporel (Neo4j/Kuzu 1478) — l'agent raisonne sur les liens ('qui a signé le contrat lié à ce fournisseur'). Étape 1 : Choisir Zep (API mémoire graphe temps réel) ou Graphiti (open source, ingestion auto)."
date_ajout: "2026-11"
nom: "Memoire graphe d'agent : Zep, Graphiti"
emoji: "🕸️"
domaine: "IA / Prompting"
signal: "Donner une mémoire graphe à un agent en 2027 (au-delà du vector store 1434) : Zep ou Graphiti stockent entités + relations + épisodes dans un graphe temporel (Neo4j/Kuzu 1478), l'agent raisonne sur les liens ('qui a signé ce contrat lié à X'). Utilise pour des agents personnels/entreprise avec historique riche. N'utilise pas si le vector store suffit."
mot_cle: "mémoire graphe agent Zep Graphiti entités relations épisodes temporels neo4j 2027"
nom_court: "Mémoire graphe"
branche: "D14"
synonymes: ["mémoire graphe agent (Zep, Graphiti) vs vector store", "entités + relations + épisodes dans un graphe temporel", "l'agent se souvient des liens entre faits (1478)"]
cross_refs: [1434, 1478, 1477]
tags: ["2027"]
depends_on: [1434]
---

## 1637. 🕸️ Memoire graphe d'agent : Zep, Graphiti (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Équiper un agent d'une mémoire graphe en 2027 (Zep/Graphiti) : entités, relations, épisodes datés dans un graphe temporel (Neo4j/Kuzu 1478) — l'agent raisonne sur les liens ('qui a signé le contrat lié à ce fournisseur').

**Quand l'utiliser (triggers)** :
- mon agent oublie les liens entre entités (qui connaît qui)
- Zep ou Graphiti pour la mémoire graphe
- graphe temporel : épisodes datés + faits avec date de péremption

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte mémoire. Tu expliques la différence : vector store (similarité) vs graphe (relations + temps) : Zep/Graphiti extraient automatiquement entités/relations des conversations (LLM), stockent dans Neo4j/Kuzu, requêtent par sous-graphe + similarité. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'historique de l'agent (conversations, docs, actions)
- Le moteur de graphe (Neo4j, Kuzu embarqué)
- Les requêtes mémoire typiques (liens, temporel)

**Méthode** :
1. Choisir Zep (API mémoire graphe temps réel) ou Graphiti (open source, ingestion auto).
2. Ingestion : chaque conversation/événement est parsé par LLM → entités (Personne, Contrat, Projet) + relations (a signé, dépend de) + épisodes (avec timestamps).
3. Stockage : graphe Neo4j/Kuzu (1478), nœuds avec embeddings (pour la similarité en plus des liens).
4. Requête mémoire : combine parcours de graphe (liens) + vectoriel (similarité) + filtre temporel (faits valides à t).
5. Règles d'oubli : faits avec date d'expiration, épisodes résumés/compactés (1431).

**Sorties attendues** :
- La mémoire graphe opérationnelle (entités/relations/épisodes)
- Les requêtes mixtes graphe+vecteur+temps testées
- La politique d'oubli temporel en place

**Exemple de prompt** :
> « Mon assistant oublie que le contrat X dépend du fournisseur Y (vu il y a 3 mois) : mémoire graphe Zep/Graphiti (entités+relations+épisodes dans Neo4j), requête 'contrats liés à Y' → retrouve le lien + date. »

**Cas d'usage** : Agents personnels/entreprise avec historique long. S'articule avec skills 1434 (mémoire sémantique/épisodique), 1478 (GraphRAG) et 1477 (hybride).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

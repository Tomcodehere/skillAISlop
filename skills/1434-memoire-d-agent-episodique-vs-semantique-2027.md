---
num: 1434
date_ajout: "2026-11"
nom: "Memoire d'agent : episodique vs semantique (2027)"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Concevoir la mémoire d'un agent en 2027 : mémoire sémantique (faits, préférences : vector store) vs épisodique (sessions passées : logs résumés) vs procédurale (outils et routines). Utilise quand un agent doit se souvenir sur le long terme. N'utilise pas pour le contexte immédiat (voir compaction)."
mot_cle: "mémoire agent sémantique épisodique procédurale vector store"
nom_court: "Mémoire agent"
branche: "D14"
synonymes: ["mémoire long terme agent", "vector store préférences utilisateur", "mémoire épisodique sessions"]
cross_refs: [260, 714, 802]
tags: ["2027"]
depends_on: [260]
---

## 1434. 🧠 Memoire d'agent : episodique vs semantique (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir la mémoire longue durée d'un agent en 2027 : sémantique (faits/préférences en vector store), épisodique (résumés de sessions), procédurale (routines apprises), avec règles d'oubli.

**Quand l'utiliser (triggers)** :
- Mon agent oublie mes préférences d'une session à l'autre
- Vector store pour la mémoire agent
- Quoi stocker en mémoire long terme ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de mémoire d'agent. Tu distingue les 3 types de mémoire (sémantique=faits, épisodique=sessions, procédurale=routines), le stockage (vector store + BDD), et la politique d'oubli (TTL, importance). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Ce que l'agent doit retenir (préférences, faits, habitudes)
- Le vector store choisi (pgvector, Qdrant, Pinecone)
- La durée de rétention souhaitée

**Méthode** :
1. Mémoire sémantique : faits + préférences → embeddings → vector store, requêtés au besoin.
2. Mémoire épisodique : résumé de chaque session stocké, retrouvable par similarité.
3. Mémoire procédurale : routines et skills appris (liés aux skills dynamiques, skill 715).
4. Politique d'oubli : TTL + score d'importance, revue mensuelle.
5. Ne jamais stocker de données sensibles sans chiffrement (RGPD).

**Sorties attendues** :
- L'architecture mémoire 3 niveaux
- Le vector store configuré
- La politique d'oubli documentée

**Exemple de prompt** :
> « Mon assistant oublie que je déteste les réunions avant 9h : mets en place une mémoire agent (sémantique préférences + épisodique sessions + oubli contrôlé). »

**Cas d'usage** : Agents personnels au long cours, préférences utilisateur. S'articule avec skills 260 (mémoire longue durée), 714 (mémoire persistante) et 802 (claude-mem).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

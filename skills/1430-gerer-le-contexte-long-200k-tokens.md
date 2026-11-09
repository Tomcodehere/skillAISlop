---
num: 1430
resume: "Exploiter efficacement un contexte long (200k+ tokens) en 2027 : placer les infos clés en début/fin (effet de primauté/récence), résumer les sections anciennes, et ne pas noyer l'instruction système. Étape 1 : Mesurer la fenêtre du modèle (200k, 1M ?) et le budget de tokens (skill 326)."
date_ajout: "2026-11"
nom: "Gerer le contexte long (200k tokens)"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Exploiter les contextes longs (100k-1M tokens) des LLM en 2027 : quoi y mettre (docs entiers, codebase), quoi en retirer, position perdue au milieu (lost in the middle), résumé des parties anciennes. Utilise quand on travaille sur un gros corpus. N'utilise pas pour une conversation courte."
mot_cle: "contexte long LLM 200k tokens quoi garder perdre milieu"
nom_court: "Contexte long"
branche: "D14"
synonymes: ["gros contexte LLM 1M tokens", "lost in the middle", "résumer les vieilles parties"]
cross_refs: [236, 326, 260]
tags: ["2027"]
depends_on: [236]
---

## 1430. 🧠 Gerer le contexte long (200k tokens, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Exploiter efficacement un contexte long (200k+ tokens) en 2027 : placer les infos clés en début/fin (effet de primauté/récence), résumer les sections anciennes, et ne pas noyer l'instruction système.

**Quand l'utiliser (triggers)** :
- J'ai 500 pages dans le contexte et le LLM oublie le milieu
- Quoi mettre dans un contexte de 200k tokens ?
- Lost in the middle : où placer l'info clé ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de contexte LLM. Tu expliques l'effet lost-in-the-middle (perte au milieu du contexte), la stratégie début/fin pour les infos critiques, et le résumé progressif des anciennes sections. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le corpus à charger (docs, code)
- La fenêtre de contexte du modèle
- La question cible

**Méthode** :
1. Mesurer la fenêtre du modèle (200k, 1M ?) et le budget de tokens (skill 326).
2. Placer l'instruction système et la question en début et fin de contexte.
3. Chunkifier le corpus et résumer les sections les plus anciennes.
4. Garder en clair uniquement les passages pertinents (retrieval ciblé).
5. Tester : la question est-elle bien répondue malgré la masse ?

**Sorties attendues** :
- La stratégie de remplissage du contexte
- Les sections résumées vs gardées en clair
- La réponse validée sur le gros corpus

**Exemple de prompt** :
> « Je mets 300 pages de docs dans le contexte et le LLM répond à côté : optimise le placement (début/fin, résumé des anciennes sections) pour 200k tokens. »

**Cas d'usage** : RAG sur gros corpus, revue de codebase entière, analyse de contrats longs. S'articule avec skills 236 (contexte conversation), 326 (tokens) et 260 (mémoire longue durée).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1439
nom: "UX du streaming des reponses LLM (2027)"
emoji: "⏩️"
domaine: "IA / Prompting"
signal: "Concevoir l'UX du streaming des réponses LLM en 2027 : afficher les tokens au fur et à mesure, état 'réflexion' (thinking) séparé, gestion des erreurs en cours de stream, annulation, squelette de chargement. Utilise quand on intègre un LLM dans une UI. N'utilise pas pour l'API seule."
mot_cle: "streaming réponses LLM UX tokens fur et à mesure thinking"
nom_court: "UX streaming"
branche: "D14"
synonymes: ["afficher la réponse LLM en streaming", "état thinking du modèle", "annuler une génération en cours"]
cross_refs: [719, 945, 327]
tags: ["2027"]
depends_on: [327]
---

## 1439. ⏩️ UX du streaming des reponses LLM (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir l'UX du streaming LLM en 2027 : tokens affichés au fur et à mesure, bloc 'réflexion' (thinking) repliable, gestion d'erreur mid-stream, bouton annuler, et temps perçu réduit (TTFT).

**Quand l'utiliser (triggers)** :
- La réponse met 30 s avant le premier mot
- Afficher les tokens en direct dans mon UI
- Gérer l'annulation d'une génération LLM

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es designer d'interaction LLM. Tu proposes : stream SSE/WebSocket, premier token rapide (TTFT < 1 s), bloc thinking séparé et repliable, curseur, annulation (AbortController), et message d'erreur gracieux si le stream coupe. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'API LLM (streaming activé ?)
- Le front (React/vanilla)
- Les états à gérer (chargement, réflexion, réponse, erreur)

**Méthode** :
1. Activer le streaming côté API (stream=true) et lire le flux (SSE).
2. Afficher chaque token dès réception (rendu incrémental, markdown progressif).
3. Séparer le bloc thinking (entre balises) dans un panneau repliable.
4. Gérer l'annulation (AbortController) et l'erreur mid-stream (message + retry).
5. Mesurer le TTFT (time to first token) cible < 1 s.

**Sorties attendues** :
- Le composant UI de streaming
- Les états gérés (thinking, erreur, annulation)
- Le TTFT mesuré

**Exemple de prompt** :
> « Notre chatbot met 30 s à répondre : mets en place le streaming (tokens au fur et à mesure, bloc thinking repliable, annulation, erreur gracieuse). »

**Cas d'usage** : Chatbots, copilotes, toute UI LLM. S'articule avec skills 719/945 (concision), 327 (compresseur de réponses).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

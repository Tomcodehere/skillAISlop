---
num: 1428
date_ajout: "2026-11"
nom: "Agents en boucle ReAct et planification"
emoji: "🔁"
domaine: "IA / Prompting"
signal: "Construire un agent en boucle ReAct en 2027 : le modèle raisonne (Thought), agit (Action avec un outil), observe (Observation), jusqu'à la réponse finale — avec une limite d'itérations. Utilise pour les tâches multi-étapes nécessitant des outils. N'utilise pas pour une réponse directe."
mot_cle: "agent react boucle thought action observation planification"
nom_court: "Agent ReAct"
branche: "D14"
synonymes: ["boucle react agent", "thought action observation", "agent qui planifie ses étapes"]
cross_refs: [259, 99, 712]
tags: ["2027"]
depends_on: [99]
---

## 1428. 🔁 Agents en boucle ReAct et planification (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter un agent ReAct en 2027 : boucle Thought → Action (outil) → Observation jusqu'à la réponse finale, avec limite d'itérations (max 10) et trace lisible pour le debug.

**Quand l'utiliser (triggers)** :
- Créer un agent qui utilise des outils en boucle
- ReAct : Thought Action Observation expliqué
- Limiter le nombre d'itérations d'un agent

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte d'agents ReAct. Tu décris la boucle (prompt système avec format TAO, parse de l'action, exécution de l'outil, observation renvoyée), la limite max_steps et la détection de boucle infinie. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La tâche multi-étapes
- Les outils disponibles (fonctions)
- La limite d'itérations (max 10)

**Méthode** :
1. Écrire le system prompt avec le format Thought/Action/Observation strict.
2. Implémenter la boucle : parse Action → appelle l'outil → renvoie Observation.
3. Limiter à max 10 itérations, sinon répond 'je n'y arrive pas' + trace.
4. Tracer chaque étape (logs) pour debug (skill 1476).
5. Tester sur 5 tâches types et mesurer le taux de réussite.

**Sorties attendues** :
- L'agent ReAct fonctionnel (code + prompt)
- La trace d'une exécution type
- Le taux de réussite sur 5 cas tests

**Exemple de prompt** :
> « Je veux un agent qui cherche sur le web puis calcule puis répond : implémente la boucle ReAct (Thought/Action/Observation, max 10 étapes, trace debug). »

**Cas d'usage** : Agents autonomes, recherche multi-sources, tâches composées. S'articule avec skills 259 (orchestration multi-agents), 99 (outils/function calling) et 712 (harnais).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

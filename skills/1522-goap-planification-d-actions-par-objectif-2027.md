---
num: 1522
date_ajout: "2026-11"
nom: "GOAP : planification d'actions par objectif (2027)"
emoji: "🎯"
domaine: "Game Dev"
signal: "Implémenter un GOAP (Goal-Oriented Action Planning) en 2027 : un objectif (ex. 'avoir une épée'), des actions avec préconditions et effets (forger épée nécessite forge + 50 minerais), l'algo A* sur l'espace des états choisit le plan le moins cher. Utilise pour des PNJ autonomes complexes. N'utilise pas pour un ennemi simple (FSM 1519 suffit)."
mot_cle: "GOAP goal oriented action planning préconditions effets plan A*"
nom_court: "GOAP"
branche: "D1"
synonymes: ["PNJ autonome qui planifie pour atteindre un objectif", "actions avec préconditions et effets", "plan le moins cher avec A* sur les états"]
cross_refs: [1521, 1519, 1517]
tags: ["2027"]
depends_on: [1521]
---

## 1522. 🎯 GOAP : planification d'actions par objectif (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter un GOAP en 2027 : état du monde (bois: 10, forge: false...), actions avec préconditions/effets/coût, objectif (ex. épée forgée), planification A* sur les états pour trouver le plan le moins cher, puis exécution action par action.

**Quand l'utiliser (triggers)** :
- Mon PNJ veut une épée mais ne sait pas quoi faire
- GOAP : préconditions et effets des actions
- Planifier le chemin le moins cher vers l'objectif

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur IA planification. Tu définis le monde comme un dict de faits (bool/int), les actions (preconditions dict, effets dict, coût), et le planificateur A* (1517) dont les nœuds sont des états du monde et les arêtes des actions applicables. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'état initial du monde (faits)
- Les actions disponibles (préconditions/effets/coût)
- L'objectif (faits à atteindre)

**Méthode** :
1. Modéliser le monde : {bois: 10, minerais: 5, forge_ouverte: false, épée: false}.
2. Actions : CouperBois (effet bois+1, coût 1), Miner (minéraux+1, coût 2), OuvrirForge (pre: bois>=5, effet forge_ouverte, coût 1), ForgerÉpée (pre: forge_ouverte + minéraux>=3, effet épée, coût 5).
3. A* sur les états : nœud = monde, voisins = actions applicables (préconditions satisfaites), coût = coût action, heuristique = nb de faits manquants.
4. Exécuter le plan : action par action, re-planner si échec (monde a changé).

**Sorties attendues** :
- Le planificateur GOAP (A* sur les états)
- Le plan affiché (étapes) et exécuté
- La replanification si le monde change

**Exemple de prompt** :
> « Mon forgeron PNJ doit fabriquer une épée : GOAP (monde: bois/minerais/forge, actions avec préconditions+coûts, A* sur les états → plan 'couper 5 bois, ouvrir forge, miner 3, forger'). »

**Cas d'usage** : PNJ autonomes (village, compagnon), quêtes auto-générées. S'articule avec skills 1521 (utility), 1519 (FSM) et 1517 (A*).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

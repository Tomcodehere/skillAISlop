---
num: 1519
date_ajout: "2026-11"
nom: "IA ennemie : state machine (FSM) simple"
emoji: "🧠"
domaine: "Game Dev"
signal: "Construire une IA ennemie par machine à états finis (FSM) en 2027 : états (Patrouille, Poursuite, Attaque, Fuite, Mort), transitions par conditions (distance joueur, PV, ligne de vue 1524), une seule update par état. Alternative plus simple que les behavior trees (1208). Utilise pour un ennemi simple et lisible. N'utilise pas pour 10+ comportements (voir utility AI 1521)."
mot_cle: "IA ennemie state machine FSM patrouille poursuite attaque fuite"
nom_court: "FSM ennemi"
branche: "D1"
synonymes: ["machine à états ennemi patrouille attaque", "FSM simple lisible debuggable", "transition si joueur à moins de 8 m"]
cross_refs: [1208, 1524, 1520]
tags: ["2027"]
depends_on: [1208]
---

## 1519. 🧠 IA ennemie : state machine (FSM) simple (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire une IA ennemie par FSM en 2027 : états Patrouille/Poursuite/Attaque/Fuite avec transitions claires (distance joueur < 8 m et ligne de vue → Poursuite), update par état, debug visuel (état affiché au-dessus de l'ennemi).

**Quand l'utiliser (triggers)** :
- Mon ennemi a un comportement confus
- FSM : patrouille → poursuite → attaque
- Debug : voir l'état actuel de l'IA en jeu

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur IA. Tu définis la classe State (enter/update/exit), le FSM (état courant + transitions testées dans update), les conditions (distance, LOS 1524, PV < 30 % → Fuite), et un debug (texte au-dessus). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les points de patrouille
- La portée de détection (8 m + LOS)
- La portée d'attaque (1,5 m) et les dégâts

**Méthode** :
1. Définir les états : Patrol (va-et-vient entre points), Chase (navigue vers joueur 1518), Attack (cooldown 1 s, dégâts), Flee (s'éloigne si PV bas).
2. Transitions dans update : si dist < 8 et LOS → Chase; si dist < 1,5 → Attack; si PV < 30 % → Flee; si joueur perdu 5 s → Patrol.
3. Un seul état actif, enter() à l'entrée (reset timers), exit() à la sortie.
4. Debug : afficher l'état courant + la raison de la dernière transition.

**Sorties attendues** :
- La FSM fonctionnelle (4 états + transitions)
- Le debug visuel en jeu
- Les constantes (distances, cooldowns) centralisées

**Exemple de prompt** :
> « Mon garde fait n'importe quoi : fais une FSM claire (Patrouille → Poursuite si joueur < 8 m avec LOS → Attaque < 1,5 m → Fuite si PV < 30 %), debug visuel de l'état. »

**Cas d'usage** : Ennemis simples (garde, slime), tutoriel IA. S'articule avec skills 1208 (behavior trees), 1524 (LOS) et 1518 (navigation).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

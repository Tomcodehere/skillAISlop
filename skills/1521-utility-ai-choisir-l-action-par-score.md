---
num: 1521
date_ajout: "2026-11"
nom: "Utility AI : choisir l'action par score"
emoji: "⚖️"
domaine: "Game Dev"
signal: "Construire une Utility AI en 2027 (alternative aux behavior trees 1208) : chaque action possible a un score 0-1 selon le contexte (faim, PV, ennemi proche), l'IA choisit la meilleure toutes les 0,5 s. Utilise pour des PNJ avec 5-10 besoins concurrents. N'utilise pas pour un ennemi scripté (FSM 1519)."
mot_cle: "utility AI score actions besoins faim PV ennemi choisir meilleure"
nom_court: "Utility AI"
branche: "D1"
synonymes: ["IA par utilité score 0-1 choisir action", "PNJ avec besoins faim sommeil social", "évaluer chaque action toutes les 0,5 s"]
cross_refs: [1208, 1519, 1136]
tags: ["2027"]
depends_on: [1519]
---

## 1521. ⚖️ Utility AI : choisir l'action par score (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire une Utility AI en 2027 : 6-8 actions possibles (manger, dormir, attaquer, fuir, soigner...), chacune scorée 0-1 par les besoins actuels (faim, énergie, PV, menace), la meilleure action est choisie toutes les 0,5 s.

**Quand l'utiliser (triggers)** :
- Mon PNJ a 10 comportements qui se contredisent
- Utility AI : faim 0,9 → manger prioritaire
- Scorer chaque action selon le contexte

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur IA utility. Tu définis les besoins (hunger, energy, health, threat, social) qui montent/descendent dans le temps, chaque action a une courbe de score selon les besoins (ex. Attack : score = threat * 0,8 - dist*0,01), choisir max toutes les 0,5 s avec hysteresis (éviter le flip-flop). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les besoins du PNJ (faim, énergie, PV, menace, social)
- Les actions possibles (8 max)
- La fréquence d'évaluation (0,5 s)

**Méthode** :
1. Définir les besoins 0-1 qui évoluent (faim +0,01/s, énergie -0,005/s...).
2. Pour chaque action, une fonction score(besoins, contexte) → 0-1 (courbe).
3. Toutes les 0,5 s : calculer tous les scores, choisir le max.
4. Hysteresis : garder l'action courante si son score > max - 0,1 (évite les oscillations).
5. Exécuter l'action (avec durée), appliquer les effets sur les besoins.

**Sorties attendues** :
- L'utility AI fonctionnelle (besoins + actions scorées)
- L'hystérésis anti-flip-flop
- Le debug : graphe des scores en temps réel

**Exemple de prompt** :
> « Mon villageois alterne entre 10 tâches sans fin : passe-le en Utility AI (besoins faim/énergie/social, 8 actions scorées, choix max toutes les 0,5 s + hystérésis). »

**Cas d'usage** : PNJ villageois, compagnons, ennemis avec priorités dynamiques. S'articule avec skills 1208 (BT), 1519 (FSM) et 1136 (difficulté).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

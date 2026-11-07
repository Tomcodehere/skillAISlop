---
num: 1527
nom: "Spawner de vagues a difficulté progressive (2027)"
emoji: "🌊"
domaine: "Game Dev"
signal: "Concevoir un spawner de vagues en 2027 : N vagues avec composition qui durcit (vague 1 = 3 slimes, vague 5 = 2 brutes + 5 archers), points de spawn budget (coût par ennemi), délais entre spawns, événement 'vague suivante dans 10 s', bonus si vague nettoyée sans dégâts. Utilise pour survival/arena. N'utilise pas pour un donjon fixe (1513)."
mot_cle: "spawner vagues difficulté progressive budget points délais entre spawns"
nom_court: "Spawner vagues"
branche: "D1"
synonymes: ["vagues d'ennemis qui durcissent", "budget de points par vague (slime 1, brute 5)", "delai 10 s entre deux vagues"]
cross_refs: [1513, 1528, 1136]
tags: ["2027"]
depends_on: [1136]
---

## 1527. 🌊 Spawner de vagues a difficulté progressive (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un spawner de vagues en 2027 : 10 vagues avec budget de points croissant (vague n = 5*n points), composition aléatoire pondérée (slime 1 pt, archer 3, brute 5), délais entre spawns, et compte à rebours entre vagues.

**Quand l'utiliser (triggers)** :
- 10 vagues d'ennemis de plus en plus durs
- Budget : vague 3 = 15 points à dépenser
- Compteur 'prochaine vague dans 10 s' + bonus no-damage

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer systèmes. Tu définis le coût par ennemi, le budget par vague (5 + 3*n), la boucle (tant que budget > 0 et ennemis vivants < cap, spawn aléatoire pondéré avec délai 0,5-1,5 s), et la fin de vague quand tous morts + 0 restant. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les types d'ennemis et leur coût (slime 1, archer 3, brute 5)
- Le nombre de vagues (10) et le budget par vague
- Les points de spawn et le délai entre spawns

**Méthode** :
1. Budget vague n = 5 + 3n; choisir ennemis aléatoire pondéré tant que coût <= budget restant.
2. Spawn : point de spawn aléatoire parmi ceux à distance > 10 m du joueur, délai 0,5-1,5 s entre spawns, cap 20 vivants.
3. Fin de vague : tous les ennemis de la vague morts ET budget dépensé → 10 s de pause + heal 10 PV (bonus si no damage: +50 score).
4. Difficulté : vague 10 = ~35 pts (2 brutes + archers), boss à la vague 10 (1526).
5. UI : 'Vague 3/10' + ennemis restants + compte à rebours.

**Sorties attendues** :
- Le spawner de 10 vagues fonctionnel
- Le budget/composition par vague
- L'UI vague + compte à rebours + bonus

**Exemple de prompt** :
> « Conçois l'arène de survie de mon roguelike : 10 vagues (budget 5+3n points, slime 1/archer 3/brute 5), spawn loin du joueur, 10 s entre vagues, boss vague 10. »

**Cas d'usage** : Survival, arena, tower defense. S'articule avec skills 1513 (map), 1528 (loot) et 1136 (difficulté).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

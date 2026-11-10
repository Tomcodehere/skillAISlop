---
num: 1517
resume: "Implémenter A* sur grille en 2027 (open set avec heap, f=g+h, 8 directions sans couper les coins, poids de terrain) puis en dériver un flow field (une passe pour N unités qui suivent le même chemin optimal). Étape 1 : A* : open heap, closed set; voisins 8 dir, diagonale interdite si un des 2 côtés est mur."
lang: "fr"
date_ajout: "2026-11"
nom: "Pathfinding A* avec poids et flow field"
emoji: "🧭"
domaine: "Game Dev"
signal: "Implémenter le pathfinding A* en 2027 sur une grille : open set (heap), coûts g/h/f, voisins 4 ou 8 directions (diagonales sans couper les coins), poids par terrain (route x1, herbe x1,5, eau infranchissable), puis flow field (champ de directions) pour 100+ unités qui suivent le même chemin. Utilise pour les RTS et foules. N'utilise pas pour un seul PNJ (voir 1224 navmesh 3D)."
mot_cle: "pathfinding A* grille heap g h f poids terrain flow field"
nom_court: "A* + flow field"
branche: "D1"
synonymes: ["A* sur grille open set heap", "flow field pour 100 unités même chemin", "poids terrain route herbe eau"]
cross_refs: [1224, 1512, 1525]
tags: ["2027"]
depends_on: [1224]
---

## 1517. 🧭 Pathfinding A* avec poids et flow field (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter A* sur grille en 2027 (open set avec heap, f=g+h, 8 directions sans couper les coins, poids de terrain) puis en dériver un flow field (une passe pour N unités qui suivent le même chemin optimal).

**Quand l'utiliser (triggers)** :
- A* sur une grille 100x100
- Flow field : 200 unités suivent le même chemin sans recalculer
- Diagonales sans couper les murs (corner cutting)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur IA déplacement. Tu donnes A* (g = coût depuis départ, h = heuristique manhattan/octile, f=g+h, heap), la règle anti-corner-cutting, les poids de terrain, et le flow field : A* une fois depuis la cible, chaque cellule stocke la direction du voisin de coût min → toutes les unités suivent le champ. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La grille (walkable + coût par tuile)
- La cible (base à défendre)
- Le nombre d'unités (flow field si > 20)

**Méthode** :
1. A* : open heap, closed set; voisins 8 dir, diagonale interdite si un des 2 côtés est mur.
2. Coûts : g += coût tuile (route 1, herbe 1,5...), h = octile distance.
3. Flow field : A* depuis la cible (inversé), chaque cellule = direction vers le voisin de g min.
4. Unités : lisent le champ à leur position (pas de path individuel) → perfs x100.
5. Recalculer le champ si la carte change (construction/destruction, 1565).

**Sorties attendues** :
- A* fonctionnel avec poids de terrain
- Le flow field pour les foules (1 passe A*)
- Le test perfs : 200 unités < 1 ms/frame

**Exemple de prompt** :
> « 200 unités de mon RTS recalculent chacune leur chemin (lag) : passe en flow field (1 A* depuis la cible, champ de directions partagé, poids de terrain). »

**Cas d'usage** : RTS, tower defense, foules de PNJ. S'articule avec skills 1224 (navmesh 3D), 1512 (grille) et 1525 (coordination).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

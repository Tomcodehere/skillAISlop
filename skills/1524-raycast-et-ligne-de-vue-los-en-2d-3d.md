---
num: 1524
resume: "Utiliser le raycast en 2027 pour la ligne de vue (LOS), les tirs hitscan et la conversion clic→monde : un rayon depuis une origine selon une direction, retourne le premier objet touché (point, normal, distance) ou rien. Étape 1 : LOS : raycast(garde.eye, dir(joueur), dist, layerMurs) → si rien entre, joueur visible (1523)."
lang: "fr"
date_ajout: "2026-11"
nom: "Raycast et ligne de vue (LOS) en 2D/3D"
emoji: "💡"
domaine: "Game Dev"
signal: "Implémenter le raycast (lancer de rayon) en 2027 : Physics.Raycast (Unity), space.intersect_ray (Godot), pour la ligne de vue (joueur visible ?), les tirs hitscan, les clics souris → monde, les ombres. Retourne le premier hit (point, normal, distance, objet). Utilise partout. N'utilise pas pour la détection de zone (overlap)."
mot_cle: "raycast lancer de rayon ligne de vue hit point normal distance"
nom_court: "Raycast"
branche: "D1"
synonymes: ["joueur visible si aucun mur entre (raycast)", "tir hitscan raycast premier hit", "clic souris vers position monde 3D"]
cross_refs: [1523, 1520, 1507]
tags: ["2027"]
depends_on: [1507]
---

## 1524. 💡 Raycast et ligne de vue (LOS) en 2D/3D (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser le raycast en 2027 pour la ligne de vue (LOS), les tirs hitscan et la conversion clic→monde : un rayon depuis une origine selon une direction, retourne le premier objet touché (point, normal, distance) ou rien.

**Quand l'utiliser (triggers)** :
- Vérifier si le joueur est visible (raycast entre garde et joueur)
- Tir hitscan : raycast depuis la caméra
- Clic souris : convertir en position dans le monde 3D

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur outils. Tu montres les appels (Unity Physics.Raycast, Godot intersect_ray, Unreal LineTrace), le masquage par layer (ne pas toucher le joueur lui-même), le raycastall pour tous les hits, et la conversion écran→monde (Camera.ScreenToWorldPoint). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'origine et la direction du rayon
- La distance max
- Le layer mask (quoi toucher)

**Méthode** :
1. LOS : raycast(garde.eye, dir(joueur), dist, layerMurs) → si rien entre, joueur visible (1523).
2. Tir hitscan : raycast(caméra, forward, 100, layerCibles) → si hit ennemi, dégâts (1508); tracer un tracer (ligne) pour le feedback.
3. Clic → monde : ray 平面 cam + souris → ScreenToWorldPoint, ou raycast sur le sol (plane y=0).
4. RaycastAll : tous les hits (ex. grenade : tous les ennemis dans le rayon).
5. Debug : Debug.DrawRay (rouge si hit, vert sinon) en scène.

**Sorties attendues** :
- Le raycast LOS opérationnel
- Le tir hitscan avec tracer visuel
- La conversion clic→monde

**Exemple de prompt** :
> « Ajoute la ligne de vue à mon stealth : raycast entre l'œil du garde et le joueur (3 points), layer 'murs' uniquement, Debug.DrawRay pour visualiser en éditeur. »

**Cas d'usage** : Partout (visibilité, tirs, clics, ombres). S'articule avec skills 1523 (stealth), 1520 (perception) et 1507 (collision).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

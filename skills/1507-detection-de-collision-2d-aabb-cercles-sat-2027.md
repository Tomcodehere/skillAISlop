---
num: 1507
nom: "Detection de collision 2D : AABB, cercles, SAT (2027)"
emoji: "💥"
domaine: "Game Dev"
signal: "Implémenter la détection de collision 2D en 2027 : AABB (rectangles alignés) pour la plupart, cercles pour les projectiles/ennemis ronds, SAT (Separating Axis Theorem) pour les rectangles orientés, avec résolution (pousser hors) et événements (on_enter/on_stay/on_exit). Utilise pour tout jeu 2D physique. N'utilise pas pour la 3D (moteur physique)."
mot_cle: "collision 2D AABB cercles SAT résolution séparation"
nom_court: "Collision 2D"
branche: "D1"
synonymes: ["AABB rectangle aligné collision", "cercle vs cercle collision", "SAT rectangles orientés"]
cross_refs: [1508, 1510, 1140]
tags: ["2027"]
depends_on: [1140]
---

## 1507. 💥 Detection de collision 2D : AABB, cercles, SAT (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter la détection + résolution de collision 2D en 2027 : AABB (chevauchement d'intervalles), cercles (distance < r1+r2), SAT pour rectangles orientés, avec poussée de séparation (MTV) et callbacks enter/stay/exit.

**Quand l'utiliser (triggers)** :
- AABB : deux rectangles se chevauchent ?
- Cercle vs rectangle : quel test ?
- Résoudre la collision (pas juste détecter) : MTV

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur physique 2D. Tu donnes les 3 tests (AABB par intervalles, cercles par distance au carré, SAT par projection sur les axes), le MTV (minimum translation vector) pour résoudre, et les callbacks enter/stay/exit pour le gameplay. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les formes des objets (AABB, cercle, OBB)
- Les layers de collision (joueur/ennemi/sol...)
- Le besoin de résolution vs simple détection

**Méthode** :
1. AABB : chevauchement si |x1-x2| < (w1+w2)/2 sur les 2 axes; MTV = plus petit dépassement.
2. Cercles : dist² < (r1+r2)² (éviter sqrt); résolution selon la normale.
3. SAT (OBB) : projeter sur les 4 axes (2 par rectangle), si un axe sépare → pas de collision, sinon MTV = axe de pénétration min.
4. Résolution : déplacer l'objet de MTV * masse relative; déclencher on_enter/on_stay/on_exit.
5. Layers : matrice de collision (qui touche qui) pour éviter les faux positifs.

**Sorties attendues** :
- Les 3 tests de collision + résolution MTV
- La matrice de layers et les callbacks
- Le test visuel (objets qui se poussent proprement)

**Exemple de prompt** :
> « Mes ennemis traversent le joueur : implémente AABB + résolution MTV (séparation) + callbacks on_enter (dégâts) avec matrice de layers. »

**Cas d'usage** : Tout jeu 2D avec physique custom. S'articule avec skills 1508 (hitbox), 1510 (physique) et 1140 (ECS).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

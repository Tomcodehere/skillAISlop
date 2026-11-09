---
num: 1561
resume: "Créer un blend tree 2D en 2027 : paramètres X/Y (-1..1) selon l'input (et caméra pour la 3D, 1506), 9 clips (idle + 8 directions), interpolation automatique du mélange — déplacement fluide sans à-coups. Étape 1 : Créer Blend Tree 2D Freeform, params X (strafe) et Y (forward), seuils -1, 0, 1."
date_ajout: "2026-11"
nom: "Blend trees : mouvement multidirectionnel fluide"
emoji: "🌿"
domaine: "Game Dev"
signal: "Utiliser un blend tree en 2027 pour un déplacement 8 directions fluide : 1 paramètre X (gauche/droite), 1 Y (haut/bas), le blend tree interpole entre 9 clips (idle + 8 directions) selon (X,Y) — plus fluide que des transitions conditionnelles (1560). Utilise pour le déplacement d'un perso 2D/3D. N'utilise pas pour des anims discrètes (attaque)."
mot_cle: "blend tree 2D X Y 9 clips interpoler déplacement 8 directions"
nom_court: "Blend tree"
branche: "D19"
synonymes: ["9 clips (idle + 8 directions) interpolés selon X Y", "déplacement 3D fluide selon la direction de la caméra", "blend tree 2D vs transitions conditionnelles"]
cross_refs: [1560, 1511, 1506]
tags: ["2027"]
depends_on: [1560]
---

## 1561. 🌿 Blend trees : mouvement multidirectionnel fluide (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Créer un blend tree 2D en 2027 : paramètres X/Y (-1..1) selon l'input (et caméra pour la 3D, 1506), 9 clips (idle + 8 directions), interpolation automatique du mélange — déplacement fluide sans à-coups.

**Quand l'utiliser (triggers)** :
- Mon perso 3D change brutalement de direction
- 9 clips N/NE/E... interpolés selon X/Y
- La direction de déplacement relative à la caméra (1506)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es technical artist animation. Tu crées un Blend Tree 2D 'Freeform Directional' (ou Smooth), paramètres X et Y alimentés par l'input local (transformé selon la caméra pour la 3D), seuils à -1/0/1, 9 clips placés aux 8 directions + centre. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les 9 clips (idle + 8 directions)
- L'input du joueur (1504) et la caméra (1506)
- Le personnage (root motion ou code)

**Méthode** :
1. Créer Blend Tree 2D Freeform, params X (strafe) et Y (forward), seuils -1, 0, 1.
2. Placer les 9 clips : centre = idle, haut = forward, etc.
3. Code : calculer dir locale = InverseTransformDirection(cam, input), blendTree.SetFloat X/Y.
4. Root motion off si déplacement géré par code (1511), on pour de la cinématique.
5. Tester : tourner la caméra (1506) + avancer → le perso fait du 'strafe' fluide.

**Sorties attendues** :
- Le blend tree 2D (9 clips, X/Y) fonctionnel
- Le déplacement relatif à la caméra en 3D
- Le test des 8 directions fluides

**Exemple de prompt** :
> « Mon perso 3D change brutalement d'anim quand je tourne : blend tree 2D (X/Y selon input relatif à la caméra 1506), 9 clips idle+directions, interpolation fluide. »

**Cas d'usage** : Déplacement 2D top-down et 3D third-person. S'articule avec skills 1560 (FSM anim), 1511 (mouvement) et 1506 (caméra).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

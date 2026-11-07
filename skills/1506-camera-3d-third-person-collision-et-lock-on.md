---
num: 1506
date_ajout: "2026-11"
nom: "Camera 3D third-person : collision et lock-on"
emoji: "🎥"
domaine: "Game Dev"
signal: "Concevoir une caméra 3D en vue third-person en 2027 : orbite autour du joueur (souris/stick), collision caméra (raycast : la caméra ne traverse pas les murs), lock-on sur les ennemis proches, FOV dynamique (sprint). Utilise pour tout jeu 3D action/aventure. N'utilise pas pour la 2D (voir 1505)."
mot_cle: "caméra 3D third-person collision raycast lock-on FOV sprint"
nom_court: "Caméra 3D"
branche: "D1"
synonymes: ["caméra qui ne traverse pas les murs", "lock-on ennemi caméra 3D", "FOV qui augmente en sprint"]
cross_refs: [1505, 1574, 1526]
tags: ["2027"]
depends_on: [1505]
---

## 1506. 🎥 Camera 3D third-person : collision et lock-on (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir une caméra 3D third-person en 2027 : orbite (yaw/pitch) autour du joueur, raycast de collision (la caméra se rapproche si un mur bloque), lock-on sur l'ennemi le plus proche, FOV qui s'élargit en sprint.

**Quand l'utiliser (triggers)** :
- La caméra 3D traverse les murs
- Lock-on sur les ennemis (boss)
- FOV dynamique en sprint

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur caméra 3D. Tu expliques l'orbite (yaw/pitch autour du pivot joueur), le raycast pivot→caméra (si hit, caméra à hit.point - marge), le lock-on (ennemi dans un cône devant → caméra regarde le milieu joueur/ennemi), et le FOV lerp en sprint. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le joueur (pivot) et sa rotation
- Les obstacles (layer 'obstacle')
- Les ennemis ciblables (layer 'ennemi')

**Méthode** :
1. Orbite : yaw += mouse.x * sens; pitch clamp [-80°, +80°]; pos = pivot + offset sphérique.
2. Collision : raycast pivot → caméra; si hit, caméra à hit.point + 0,3 m vers le pivot.
3. Lock-on : ennemis dans cône 30° devant, distance < 20 m → cible = plus proche; caméra lerp vers le point médian.
4. FOV : lerp vers 70° normal, 85° en sprint.
5. Reset doux de la caméra derrière le joueur (touche R).

**Sorties attendues** :
- La caméra 3D avec anti-collision et lock-on
- Le FOV dynamique (sprint)
- Le test en environnement exigu (couloir)

**Exemple de prompt** :
> « En couloir étroit ma caméra 3D passe à travers le mur : ajoute un raycast pivot→caméra (raccourcir si hit) + lock-on boss + FOV sprint. »

**Cas d'usage** : Jeu 3D action/aventure/RPG. S'articule avec skills 1505 (caméra 2D), 1574 (FOV réglable) et 1526 (boss).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

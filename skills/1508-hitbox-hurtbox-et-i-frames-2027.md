---
num: 1508
nom: "Hitbox, hurtbox et i-frames (2027)"
emoji: "⚔️"
domaine: "Game Dev"
signal: "Concevoir les hitboxes d'un jeu d'action en 2027 : hitbox (dégâts de l'attaque) vs hurtbox (réception), priorité des attaques, i-frames (invincibilité 0,3 s après un coup reçu), knockback. Utilise pour tout jeu de combat/action. N'utilise pas pour un RPG au tour par tour."
mot_cle: "hitbox hurtbox i-frames invincibilité knockback combat"
nom_court: "Hitbox"
branche: "D1"
synonymes: ["séparer hitbox et hurtbox", "i-frames après un coup", "knockback directionnel"]
cross_refs: [1507, 1559, 1526]
tags: ["2027"]
depends_on: [1507]
---

## 1508. ⚔️ Hitbox, hurtbox et i-frames (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir le système de combat d'un jeu d'action en 2027 : hitbox (zone d'attaque, active quelques frames) vs hurtbox (zone de réception), i-frames 0,3 s après touche, knockback selon la direction, priorité entre attaques.

**Quand l'utiliser (triggers)** :
- Mes attaques ne touchent pas toujours
- Hitbox active seulement 3 frames au milieu de l'anim
- i-frames pour éviter le stunlock

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur combat. Tu sépares hitbox (dégâts, active via animation events) et hurtbox (réception), tu ajoutes les i-frames (timer invincible, clignotement visuel), le knockback (impulsion directionnelle), et la priorité (attaque forte > faible). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les animations d'attaque (frames clés)
- Les dégâts par attaque
- La durée des i-frames (0,3 s)

**Méthode** :
1. Séparer : hurtbox sur le personnage (toujours), hitbox sur l'arme/attaque (activée par event d'anim).
2. Collision hitbox(attaquant) vs hurtbox(défenseur), une seule fois par attaque (flag).
3. i-frames : après touche, timer 0,3 s invincible + clignotement (visible).
4. Knockback : impulsion = direction * force + petit lift vertical.
5. Priorité : si les 2 attaques se touchent, la plus forte gagne (poids).

**Sorties attendues** :
- Le système hitbox/hurtbox fonctionnel
- Les i-frames + feedback visuel (clignotement, hitstop 50 ms)
- Le knockback directionnel

**Exemple de prompt** :
> « Mon jeu de combat est brouillon : sépare hitbox/hurtbox (hitbox active via events d'anim), ajoute i-frames 0,3 s + hitstop 50 ms + knockback. »

**Cas d'usage** : Jeux de combat, action, bullet hell. S'articule avec skills 1507 (collision), 1559 (juice) et 1526 (boss).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

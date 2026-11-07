---
num: 1509
date_ajout: "2026-11"
nom: "Physique 2D custom : gravité et saut variable (2027)"
emoji: "🏃"
domaine: "Game Dev"
signal: "Coder une physique 2D custom en 2027 (sans moteur physique lourd) : gravité constante, saut variable (relâcher la touche = couper la vélocité verticale, saut plus court), vitesse max, friction au sol. Utilise pour un plateformer exigeant (game feel). N'utilise pas si le moteur physique suffit."
mot_cle: "physique 2D custom gravité saut variable couper vélocité"
nom_court: "Physique 2D"
branche: "D1"
synonymes: ["saut variable selon appui long court", "gravité custom plateformer", "friction au sol glisser"]
cross_refs: [1510, 1511, 1559]
tags: ["2027"]
depends_on: [1511]
---

## 1509. 🏃 Physique 2D custom : gravité et saut variable (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Coder une physique 2D custom en 2027 pour un plateformer : gravité (ex. 2500 px/s²), saut variable (relâcher = vélocité verticale coupée à 40 %), vitesse max horizontale, friction sol, air control réduit.

**Quand l'utiliser (triggers)** :
- Saut haut si appui long, court si appui bref
- Gravité qui fait naturel (lourdeur)
- Friction au sol et air control

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur physique plateformer. Tu donnes les constantes (gravité, jump velocity, cut multiplier 0,4, max fall speed, accélération sol vs air) et les formules par frame en fixed timestep (1501). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les constantes de game feel (gravité, saut, vitesses)
- Le sol (détection)
- Le fixed timestep (1501)

**Méthode** :
1. Gravité : vy += G * dt, clamp vy à fall_max (ex. 1200 px/s).
2. Saut : au press, vy = -jump_velocity; au release si vy < 0, vy *= 0,4 (saut coupé).
3. Horizontal : vx vers input*max_speed avec accélération différente sol (3000) vs air (1500).
4. Sol : si on sol et pas de saut → friction (vx vers 0).
5. Tune : tester hauteur de saut (formule h = v²/2g) et le floatiness.

**Sorties attendues** :
- La physique 2D custom (gravité + saut variable + friction)
- Les constantes tunées (hauteur de saut visée)
- Le test de game feel comparatif

**Exemple de prompt** :
> « Mon saut est trop 'flottant' : code une physique 2D custom (gravité 2500, saut variable coupé à 40 % au relâché, friction sol, air control réduit). »

**Cas d'usage** : Plateformers 2D exigeants. S'articule avec skills 1510 (coyote/buffer), 1511 (mouvement 8 dir), 1559 (juice) et 1501 (fixed timestep).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1559
resume: "Ajouter du juice (game feel) en 2027 sans toucher au gameplay : squash & stretch (saut/atterrissage), hitstop 50 ms à l'impact (1508), flash blanc + particules (1557) + son à chaque hit, caméra (1558), délais de feedback inférieur à 100 ms. Étape 1 : Squash & stretch : au saut, scale (1,2, 0,8); à l'atterrissage, scale (0,8, 1,2) puis retour élastique (lerp 0,15 s)."
date_ajout: "2026-11"
nom: "Juice : game feel (squash & stretch, hitstop, particules)"
emoji: "🧃"
domaine: "Game Dev"
signal: "Ajouter du 'juice' (game feel) en 2027 pour rendre le jeu satisfaisant : squash & stretch (le perso s'écrase à l'atterrissage et s'étire au saut), hitstop (freeze 50 ms à l'impact, 1508), particules à chaque action, flash blanc au hit, son impact, caméra (1558). Règle : le juice ne change pas le gameplay, que la perception. Utilise partout. N'utilise pas pour un jeu sérieux (simulation)."
mot_cle: "juice game feel squash stretch hitstop 50 ms flash blanc particules"
nom_court: "Juice"
branche: "D19"
synonymes: ["squash & stretch au saut et atterrissage", "hitstop freeze 50 ms à l'impact", "flash blanc + particules + son à chaque hit"]
cross_refs: [1558, 1508, 1557]
tags: ["2027"]
depends_on: [1508]
---

## 1559. 🧃 Juice : game feel (squash & stretch, hitstop, particules) (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ajouter du juice (game feel) en 2027 sans toucher au gameplay : squash & stretch (saut/atterrissage), hitstop 50 ms à l'impact (1508), flash blanc + particules (1557) + son à chaque hit, caméra (1558), délais de feedback < 100 ms.

**Quand l'utiliser (triggers)** :
- Le jeu est 'mou', les coups ne font rien ressentir
- Squash & stretch : le perso s'écrase à l'atterrissage
- Hitstop 50 ms + flash + son à chaque impact

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game feel designer. Tu liste les 6 effets de juice : squash&stretch (scale y 0,8/1,2 animé 0,15 s), hitstop (Time.timeScale = 0 50 ms), flash (sprite blanc 1 frame), particules, son, screen shake (1558) — feedback < 100 ms après l'action. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les actions du joueur (saut, attaque, dégâts reçus, mort)
- Les effets visuels/sonores par action
- Le timeScale pour le hitstop

**Méthode** :
1. Squash & stretch : au saut, scale (1,2, 0,8); à l'atterrissage, scale (0,8, 1,2) puis retour élastique (lerp 0,15 s).
2. Hitstop : à l'impact, Time.timeScale = 0 pendant 50 ms (freeze frame), puis 1.
3. Flash : le sprite touché passe blanc 1 frame (material flash).
4. Particules (1557) + son (1568) à chaque hit; mort = slow motion 0,5 s + particules.
5. Règle : chaque action du joueur a un feedback visuel/sonore en < 100 ms.

**Sorties attendues** :
- Le juice déployé (squash, hitstop, flash, particules, son, shake)
- Le feedback < 100 ms sur chaque action
- Le test 'à l'aveugle' : le jeu paraît plus réactif

**Exemple de prompt** :
> « Mon plateformer est 'mou' : ajoute du juice — squash&stretch au saut/atterrissage, hitstop 50 ms + flash + particules + son à chaque hit, feedback < 100 ms. »

**Cas d'usage** : Tout jeu d'action (essentiel au game feel). S'articule avec skills 1558 (shake), 1508 (hitbox) et 1557 (particules).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

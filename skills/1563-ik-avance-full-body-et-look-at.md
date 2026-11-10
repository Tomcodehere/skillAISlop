---
num: 1563
resume: "Appliquer le Full Body IK en 2027 : look-at (tête/yeux vers le joueur/ennemi avec poids 0-1), spine (torse penché vers une cible), hand IK avancé, via Animator IK (OnAnimatorIK) ou Final IK, pour des PNJ crédibles. Étape 1 : Dans OnAnimatorIK : si cible proche (inférieur à 5 m), SetLookAtPosition(cible) weight lerp → 1 (tête regarde)."
lang: "fr"
date_ajout: "2026-11"
nom: "IK avancé : full body et look-at"
emoji: "👀"
domaine: "Game Dev"
signal: "Aller plus loin que l'IK 2 os en 2027 : Full Body IK (Unity Animator IK, Final IK) pour tout le corps (ajuste hanche/épaule/tête), look-at (la tête regarde un objet/ennemi avec poids), spine IK (torse se penche). Utilise pour des PNJ crédibles. N'utilise pas si 2 os suffisent (1562)."
mot_cle: "full body IK look-at spine tête regarde ennemi poids IK Unity Final IK"
nom_court: "Full-body IK"
branche: "D19"
synonymes: ["la tête du PNJ regarde le joueur (look-at)", "le torse se penche vers l'objet (spine IK)", "Full Body IK Unity Animator.SetIKPosition"]
cross_refs: [1562, 1520, 1560]
tags: ["2027"]
depends_on: [1562]
---

## 1563. 👀 IK avancé : full body et look-at (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Appliquer le Full Body IK en 2027 : look-at (tête/yeux vers le joueur/ennemi avec poids 0-1), spine (torse penché vers une cible), hand IK avancé, via Animator IK (OnAnimatorIK) ou Final IK, pour des PNJ crédibles.

**Quand l'utiliser (triggers)** :
- Le PNJ regarde dans le vide au lieu du joueur
- Torse qui se penche quand il prend un objet
- SetIKPositionWeight / SetLookAtPosition Unity

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es technical artist IK avancé. Tu utilises OnAnimatorIK : SetLookAtPosition(cible) + SetLookAtWeight(1), SetIKPosition(AvatarIKGoal.LeftHand, cible) + weight, spine via SetIKPositionWeight sur la colonne, lissé par lerp de poids. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le rig humanoïde avec IK activé
- Les cibles (joueur, ennemi 1520, objet ramassé 1534)
- Les poids par partie (tête 1, mains 0,5, pieds 1)

**Méthode** :
1. Dans OnAnimatorIK : si cible proche (< 5 m), SetLookAtPosition(cible) weight lerp → 1 (tête regarde).
2. Spine : SetIKPosition(AvatarIKGoal... non, spine se fait via SetIKRotation/Position ou le weight de la spine — le torse suit la tête.
3. Mains : quand le PNJ ramasse un objet (1534), IK main gauche/droite vers l'objet, weight 1, puis retour anim.
4. Pieds : IK sol déjà en place (1562), poids 1.
5. Lisser tous les weights (lerp 5/s) pour éviter les à-coups.

**Sorties attendues** :
- Le look-at (tête vers le joueur/ennemi) et le spine IK
- Le hand IK contextuel (ramasser un objet)
- Les poids lissés (pas d'à-coups)

**Exemple de prompt** :
> « Mon PNJ garde toujours le regard droit : ajoute look-at IK (tête/yeux vers le joueur < 5 m, weight lissé), spine qui se penche, et hand IK quand il ramasse un objet. »

**Cas d'usage** : PNJ crédibles, cinématiques légères. S'articule avec skills 1562 (IK 2 os), 1520 (perception) et 1560 (anim).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

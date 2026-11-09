---
num: 1562
resume: "Appliquer l'IK à 2 os en 2027 (Two Bone IK Unity / FABRIK) : un effecteur (pied/main) atteint une cible (sol, poignée d'arme) avec la rotation calculée automatiquement, poids d'IK 0-1 pour mélanger anim et IK. Étape 1 : Raycast (1524) depuis la hanche + 0,5 m vers le bas → hit sol → target pied = hit.point + offset."
lang: "fr"
date_ajout: "2026-11"
nom: "Rigging procédural et IK deux os"
emoji: "🦴"
domaine: "Game Dev"
signal: "Faire du rigging procédural en 2027 : IK (Inverse Kinematics) à 2 os (Two Bone IK Unity, FABRIK) pour que le pied/main touche une cible (sol, arme, poignée), sans coder la rotation à la main. Utilise pour les pieds qui suivent le terrain, les mains sur une arme. N'utilise pas pour un humanoïde simple sans IK (1560 suffit)."
mot_cle: "IK inverse kinematics two bone FABRIK pied sol main arme cible"
nom_court: "IK 2 os"
branche: "D19"
synonymes: ["pieds qui suivent le terrain (IK)", "main qui tient l'arme (IK deux os)", "FABRIK ou Two Bone IK sans coder la rotation"]
cross_refs: [1560, 1563, 1564]
tags: ["2027"]
depends_on: [1560]
---

## 1562. 🦴 Rigging procédural et IK deux os (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Appliquer l'IK à 2 os en 2027 (Two Bone IK Unity / FABRIK) : un effecteur (pied/main) atteint une cible (sol, poignée d'arme) avec la rotation calculée automatiquement, poids d'IK 0-1 pour mélanger anim et IK.

**Quand l'utiliser (triggers)** :
- Les pieds flottent au-dessus du sol en pente
- La main ne tient pas bien l'arme
- Two Bone IK : calculer la rotation du genou/coude automatiquement

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es technical artist rigging. Tu configures l'IK 2 os : chaîne (hanche→genou→pied), effecteur (piste = position sol calculée par raycast 1524), hint (genou vers l'avant), poids (1 en IK, 0 en anim d'origine), lissé (lerp). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le rig humanoïde (hanche/genou/pied, épaule/coude/main)
- Les cibles (sol sous le pied via raycast, poignée de l'arme)
- Le poids d'IK par membre (0-1)

**Méthode** :
1. Raycast (1524) depuis la hanche + 0,5 m vers le bas → hit sol → target pied = hit.point + offset.
2. Two Bone IK : effecteur = cette cible, hint (genou) = devant le personnage, poids 1 quand grounded.
3. Mains : cible = poignée de l'arme (bone de l'arme), poids 1 quand on tient, 0 sinon (anim 1560).
4. Lisser : poids IK = lerp vers la cible (éviter les à-coups quand on passe une marche).
5. Tête : look-at IK sur la cible la plus proche (ennemi 1520).

**Sorties attendues** :
- Les pieds qui suivent le terrain (IK + raycast sol)
- Les mains sur l'arme (IK cible poignée)
- Le poids IK lissé (0-1)

**Exemple de prompt** :
> « En pente, les pieds de mon perso flottent : ajoute IK 2 os sur chaque jambe (raycast 1524 sous la hanche → cible pied, hint genou devant, poids 1 lissé). »

**Cas d'usage** : Personnages 3D, terrain irrégulier. S'articule avec skills 1560 (anim), 1563 (IK avancé) et 1564 (ragdoll).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

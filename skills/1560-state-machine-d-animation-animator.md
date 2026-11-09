---
num: 1560
resume: "Organiser les animations d'un personnage en 2027 : états (Idle/Run/Jump/Attack/Hit/Death), paramètres (speed, grounded, trigger attack), transitions avec conditions + crossfade 0,1 s, et priorité (Hit supérieur à Attack supérieur à mouvement). Étape 1 : Créer les paramètres : Speed (float), Grounded (bool), Attack (trigger), Hit (trigger), Dead (bool)."
lang: "fr"
date_ajout: "2026-11"
nom: "State machine d'animation (Animator)"
emoji: "🎭"
domaine: "Game Dev"
signal: "Organiser les animations d'un personnage en 2027 avec une state machine : états (Idle, Run, Jump, Attack, Hit, Death), transitions avec conditions (vitesse supérieur à 0,1 → Run; grounded false → Jump), blend (crossfade 0,1 s), paramètres (float speed, bool grounded, trigger attack). Utilise pour tout personnage animé. N'utilise pas pour une anim linéaire unique."
mot_cle: "state machine animation Animator états transitions conditions crossfade"
nom_court: "Anim FSM"
branche: "D19"
synonymes: ["états Idle Run Jump Attack avec transitions", "condition vitesse superieure a 0,1 passe en Run", "crossfade 0,1 s entre deux animations"]
cross_refs: [1561, 1519, 1509]
tags: ["2027"]
depends_on: [1519]
---

## 1560. 🎭 State machine d'animation (Animator, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Organiser les animations d'un personnage en 2027 : états (Idle/Run/Jump/Attack/Hit/Death), paramètres (speed, grounded, trigger attack), transitions avec conditions + crossfade 0,1 s, et priorité (Hit > Attack > mouvement).

**Quand l'utiliser (triggers)** :
- Mon perso enchaîne les anims bizarrement
- Idle → Run si vitesse > 0,1, → Jump si pas grounded
- Crossfade 0,1 s entre Idle et Run pour la fluidité

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es technical artist animation. Tu définis les paramètres (float Speed, bool Grounded, trigger Attack, bool Hit), les transitions (condition + duration 0,1 s crossfade), l'ordre de priorité (Any State → Hit/Death prioritaire), et tu sync les events d'anim (dégâts au frame 12, 1508). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les clips d'animation (Idle, Run, Jump, Attack, Hit, Death)
- Les paramètres du gameplay (vitesse, sol, PV)
- Les frames d'events (dégâts, son de pas)

**Méthode** :
1. Créer les paramètres : Speed (float), Grounded (bool), Attack (trigger), Hit (trigger), Dead (bool).
2. États : Idle, Run, Jump, Fall, Attack, Hit, Death; chaque état = 1 clip (loop ou pas).
3. Transitions : Idle↔Run (Speed <0,1 / >0,1), *→Jump (!Grounded), Jump→Fall (vy<0), *→Attack (trigger, exit time), Any→Hit (trigger, prioritaire), *→Death (Dead).
4. Crossfade 0,1 s sur les transitions de mouvement; Hit/Death en 0 (immediat, prioritaire).
5. Animation events : frame 12 de Attack = spawn hitbox (1508), frame 3 de Run = son de pas (1568).

**Sorties attendues** :
- La state machine d'animation complète (états + transitions + priorités)
- Les events d'anim synchronisés (hitbox frame 12, sons)
- Le test : enchaînement fluide Idle→Run→Jump→Attack

**Exemple de prompt** :
> « Les animations de mon perso s'enchaînent mal : fais une state machine (Idle/Run/Jump/Attack/Hit/Death, conditions Speed/Grounded/triggers, crossfade 0,1 s, Hit prioritaire, events frame 12). »

**Cas d'usage** : Tout personnage animé 2D/3D. S'articule avec skills 1561 (blend trees), 1519 (FSM gameplay) et 1509 (physique).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

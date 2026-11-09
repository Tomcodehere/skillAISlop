---
num: 1510
resume: "Ajouter coyote time (0,1 s de grâce pour sauter après le sol) et jump buffering (0,1 s : un appui avant l'atterrissage déclenche le saut à l'atterrissage) à un plateformer 2D en 2027. Étape 1 : Coyote : variable coyote = 0,1 si on sol, sinon décrémente; saut autorisé si coyote supérieur à 0."
date_ajout: "2026-11"
nom: "Plateformer : coyote time et jump buffering"
emoji: "🎯"
domaine: "Game Dev"
signal: "Implémenter le coyote time et le jump buffering en 2027, indispensables à un bon plateformer : coyote time (0,1 s pour sauter après avoir quitté le sol), jump buffer (0,1 s : appuyer juste avant d'atterrir saute dès l'atterrissage). Utilise dans tout plateformer 2D. N'utilise pas pour un jeu sans saut."
mot_cle: "coyote time jump buffering plateformer 0,1 s"
nom_court: "Coyote+buffer"
branche: "D1"
synonymes: ["sauter 0,1 s après avoir quitté le sol", "jump buffer appuyer avant d'atterrir", "tolérance de saut plateformer"]
cross_refs: [1509, 1504, 1559]
tags: ["2027"]
depends_on: [1509]
---

## 1510. 🎯 Plateformer : coyote time et jump buffering (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ajouter coyote time (0,1 s de grâce pour sauter après le sol) et jump buffering (0,1 s : un appui avant l'atterrissage déclenche le saut à l'atterrissage) à un plateformer 2D en 2027.

**Quand l'utiliser (triggers)** :
- Le saut semble 'mou' quand on rate le timing
- Coyote time : sauter juste après le bord
- Jump buffer : appui anticipé avant d'atterrir

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur game feel. Tu implémentes 2 timers : coyoteTimer (reset à 0,1 s quand on sol, décrémente, saut valide si > 0) et jumpBuffer (0,1 s au press, consommé si on sol ou coyote actif), dans le fixed update (1501). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La détection sol
- Le fixed timestep (1501)
- Les durées (0,1 s chacune)

**Méthode** :
1. Coyote : variable coyote = 0,1 si on sol, sinon décrémente; saut autorisé si coyote > 0.
2. Buffer : au press saut, buffer = 0,1; décrémente; si (on sol ou coyote>0) et buffer>0 → saut + reset des 2.
3. Dans update fixe : appliquer la vélocité de saut, couper au release (1509).
4. Tester : courir vers un précipice, sauter à la toute fin (coyote), appuyer avant d'atterrir (buffer).

**Sorties attendues** :
- Coyote time + jump buffer fonctionnels (0,1 s chacun)
- Le game feel nettement amélioré (test à l'aveugle)
- Le code dans le fixed update

**Exemple de prompt** :
> « Mon plateformer punit le moindre mauvais timing : ajoute coyote time 0,1 s + jump buffering 0,1 s dans le fixed update. »

**Cas d'usage** : Tout plateformer 2D (Celeste-like). S'articule avec skills 1509 (physique), 1504 (input) et 1559 (juice).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

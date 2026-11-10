---
num: 1520
resume: "Implémenter une perception crédible en 2027 : vision (cône angle/portée + occlusion raycast), ouïe (événements bruyants avec rayon selon intensité : marche 3 m, course 8 m, tir 20 m), mémoire (last_seen_position, investigation 5 s). Étape 1 : Vision : chaque frame, si angle(forward, toPlayer) inférieur à 45° et dist inférieur à 10 → raycast (mur bloque) → visible."
lang: "fr"
date_ajout: "2026-11"
nom: "Perception ennemie : vue, ouïe et memoire"
emoji: "👁️"
domaine: "Game Dev"
signal: "Donner une perception crédible à un ennemi en 2027 : cône de vision (angle + portée + obstacles via raycast 1524), ouïe (bruits avec intensité/distance, le joueur qui court alerte), mémoire (dernier point vu, l'ennemi y va puis cherche 5 s). Utilise pour du stealth/action. N'utilise pas pour un ennemi aveugle."
mot_cle: "perception IA cône de vision ouïe mémoire dernier point vu"
nom_court: "Perception"
branche: "D1"
synonymes: ["ennemi qui voit dans un cône 90°", "l'ennemi entend le joueur courir", "mémoire : dernier point vu puis chercher"]
cross_refs: [1524, 1519, 1525]
tags: ["2027"]
depends_on: [1519]
---

## 1520. 👁️ Perception ennemie : vue, ouïe et memoire (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter une perception crédible en 2027 : vision (cône angle/portée + occlusion raycast), ouïe (événements bruyants avec rayon selon intensité : marche 3 m, course 8 m, tir 20 m), mémoire (last_seen_position, investigation 5 s).

**Quand l'utiliser (triggers)** :
- L'ennemi voit à travers les murs
- Cône de vision 90° portée 10 m avec occlusion
- Le joueur court → alerte à 8 m, marche → 3 m

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur IA perception. Tu fais : vision = angle entre forward et dir(joueur) < fov/2 + dist < range + raycast sans hit mur (1524); ouïe = événements sonores (volume/distance → rayon); mémoire = last_seen updated quand visible, sinon va là-bas puis patrouille. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cône de vision (angle 90°, portée 10 m)
- Les rayons d'ouïe (marche 3 m, course 8 m, tir 20 m)
- Le temps de recherche (5 s)

**Méthode** :
1. Vision : chaque frame, si angle(forward, toPlayer) < 45° et dist < 10 → raycast (mur bloque) → visible.
2. Ouïe : fonction emitSound(pos, radius) appelée par le joueur (course = 8 m) → si dist < radius, last_seen = pos.
3. Mémoire : si visible → last_seen = player.pos, alertness = 1; sinon alertness décroit, va à last_seen, cherche (rotation) 5 s.
4. États : Patrol (calme) ↔ Investigate (last_seen) ↔ Chase (visible).

**Sorties attendues** :
- La perception vision/ouïe/mémoire fonctionnelle
- Les rayons configurables (marche/course/tir)
- Le comportement d'investigation (va au dernier point vu)

**Exemple de prompt** :
> « Mon garde voit le joueur à travers le mur et n'entend rien : ajoute occlusion raycast (cône 90°/10 m), ouïe (course 8 m, tir 20 m), mémoire last_seen + investigation 5 s. »

**Cas d'usage** : Jeux de stealth, action. S'articule avec skills 1524 (LOS), 1519 (FSM) et 1525 (coordination).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

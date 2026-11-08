---
num: 1501
date_ajout: "2026-11"
nom: "Boucle de jeu fixe : fixed timestep et interpolation"
emoji: "⏱️"
domaine: "Game Dev"
signal: "Implémenter une boucle de jeu robuste en 2027 : fixed timestep pour la physique/logique (ex. 60 Hz fixe), variable render, interpolation entre les 2 derniers états pour un rendu fluide. Utilise pour tout jeu temps réel. N'utilise pas pour un jeu au tour par tour."
mot_cle: "fixed timestep boucle de jeu interpolation physique 60 Hz"
nom_court: "Fixed timestep"
branche: "D1"
synonymes: ["boucle de jeu fixe 60 hz", "interpolation render entre deux états", "delta time vs fixed dt"]
cross_refs: [1140, 308, 309]
tags: ["2027"]
depends_on: [1140]
---

## 1501. ⏱️ Boucle de jeu fixe : fixed timestep et interpolation (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter une boucle de jeu à pas fixe en 2027 : logique/physique à 60 Hz fixe (fixed timestep avec accumulateur), rendu à fréquence variable, interpolation alpha entre les 2 derniers états pour un affichage fluide.

**Quand l'utiliser (triggers)** :
- Mon jeu lag quand le framerate baisse
- fixed timestep 60 Hz accumulateur
- interpolation entre états pour le rendu

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur gameplay. Tu donnes le pattern de l'accumulateur (accumulator += dt; while acc >= FIXED_DT: update(FIXED_DT)), l'alpha = acc/FIXED_DT pour interpoler render(prev, curr, alpha), et tu rappelles : jamais de logique dans render. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le moteur (Unity FixedUpdate, Godot _physics_process, custom)
- Le pas fixe choisi (60 Hz = 16,67 ms)
- Les systèmes à déplacer en fixed (physique, IA)

**Méthode** :
1. Séparer update logique (fixed 60 Hz) et render (variable).
2. Accumulateur : stocker le reste de temps non consommé.
3. Physique et IA dans l'update fixe (déterministe).
4. Render : interpoler la position entre l'état N-1 et N avec alpha.
5. Tester à 30/60/144 fps : le jeu doit avancer pareil (même distance).

**Sorties attendues** :
- La boucle fixed timestep implémentée
- L'interpolation de rendu en place
- Le test de déterminisme à différents fps

**Exemple de prompt** :
> « Mon jeu accélère quand le framerate baisse : implémente une boucle fixed timestep 60 Hz (accumulateur) + interpolation de rendu dans Godot 4. »

**Cas d'usage** : Tout jeu temps réel (plateformer, shooter, action). S'articule avec skills 1140 (game loop), 308 (profileur) et 309 (bench).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1511
resume: "Coder un déplacement 8 directions en 2027 : vecteur d'input normalisé (diagonale = même vitesse), accélération/décélération douces, dash (impulsion + 0,2 s + cooldown 1 s + i-frames + trail). Étape 1 : Input : dir = (x,y).normalized (jamais de diagonale plus rapide)."
lang: "fr"
date_ajout: "2026-11"
nom: "Mouvement 8 directions et dash"
emoji: "💨"
domaine: "Game Dev"
signal: "Coder un déplacement 8 directions fluide en 2027 : normalisation du vecteur d'input (diagonale pas plus rapide), accélération/décélération, dash avec cooldown et i-frames, trail visuel. Utilise pour top-down 2D et twin-stick. N'utilise pas pour un plateformer (voir 1510)."
mot_cle: "mouvement 8 directions normalisé dash cooldown trail"
nom_court: "Déplacement 8 dir"
branche: "D1"
synonymes: ["diagonale pas plus rapide normaliser", "dash avec cooldown et i-frames", "top-down 2D déplacement fluide"]
cross_refs: [1509, 1504, 1559]
tags: ["2027"]
depends_on: [1504]
---

## 1511. 💨 Mouvement 8 directions et dash (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Coder un déplacement 8 directions en 2027 : vecteur d'input normalisé (diagonale = même vitesse), accélération/décélération douces, dash (impulsion + 0,2 s + cooldown 1 s + i-frames + trail).

**Quand l'utiliser (triggers)** :
- La diagonale va plus vite que le droit
- Dash avec cooldown et invincibilité
- Accélération douce (pas instantané)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur déplacement. Tu normalises l'input (input.normalized), tu sépares vélocité (vel += dir*accel*dt, friction), et le dash : vel = dir_dash * dash_speed, timer 0,2 s, cooldown 1 s, i-frames, trail (pool de sprites, 1550). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le vecteur d'input (8 directions)
- Accélération/décélération (ex. 40/30)
- Dash : vitesse 1200, durée 0,2 s, cooldown 1 s

**Méthode** :
1. Input : dir = (x,y).normalized (jamais de diagonale plus rapide).
2. Vélocité : vel = approach(vel, dir*max_speed, accel*dt) au clavier, friction au sol.
3. Dash : au press, si cooldown OK → dash_timer=0,2, dash_dir=dir, i-frames 0,2 s, spawn trail.
4. Pendant dash : vel = dash_dir*dash_speed (ignore input), cooldown démarre à la fin.
5. Trail : pool de ghosts qui s'estompent (fade 0,3 s).

**Sorties attendues** :
- Le déplacement 8 dir normalisé + dash complet
- Le cooldown et les i-frames du dash
- Le trail visuel (pool de ghosts)

**Exemple de prompt** :
> « Mon top-down avance en diagonale plus vite : normalise l'input, ajoute accélération/friction douces et un dash (1200 px/s, 0,2 s, cooldown 1 s, i-frames, trail). »

**Cas d'usage** : Top-down 2D, twin-stick shooter, action. S'articule avec skills 1509 (physique), 1504 (input) et 1559 (juice).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

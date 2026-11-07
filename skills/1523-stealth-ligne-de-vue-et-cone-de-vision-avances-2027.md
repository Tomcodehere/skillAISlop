---
num: 1523
nom: "Stealth : ligne de vue et cone de vision avances (2027)"
emoji: "🕶️"
domaine: "Game Dev"
signal: "Construire un système de stealth en 2027 : cône de vision de garde (mesh visuel translucide), ligne de vue par raycasts multiples (tête/corps/pieds du joueur), niveau de détection 0-100 % (remplit si visible, décroit sinon), états Alerte/Inquiet/Suspect, ombre = bonus de dissimulation. Utilise pour les jeux d'infiltration. N'utilise pas sans garde (voir perception 1520)."
mot_cle: "stealth ligne de vue raycasts cone détection 0-100% ombre"
nom_court: "Stealth LOS"
branche: "D1"
synonymes: ["garde avec cône de vision mesh translucide", "3 raycasts tête corps pieds visibilité", "jauge de détection qui monte descend"]
cross_refs: [1520, 1524, 1519]
tags: ["2027"]
depends_on: [1520]
---

## 1523. 🕶️ Stealth : ligne de vue et cone de vision avances (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire un stealth en 2027 : cône de vision rendu (mesh translucide), visibilité du joueur par 3 raycasts (tête/corps/pieds) avec occlusion, jauge de détection 0-100 % (monte vite si proche, lentement si loin), ombre = -30 %, états du garde (Suspect → Alerte → Combat).

**Quand l'utiliser (triggers)** :
- Le joueur caché derrière un mur est quand même vu
- Jauge de détection au-dessus de la tête du garde
- Dans l'ombre : détection 30 % plus lente

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur stealth. Tu fais : cône = mesh généré (angle/portée), visibilité = 3 raycasts joueur (tête, centre, pieds) non bloqués + dans le cône + distance, détection += rate*dt si visible (rate dépend distance/ombre/camouflage), états avec hysteresis. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cône de chaque garde (angle 70°, portée 12 m)
- Les 3 points de raycast du joueur
- Les modificateurs (ombre -30 %, accroupi -50 %, vitesse course +)

**Méthode** :
1. Générer le mesh du cône (arc de cercle + triangulation) affiché en translucide (jaune suspect, rouge alerte).
2. Visibilité : pour chaque garde, joueur dans cône ? → 3 raycasts (tête/corps/pieds) vers le garde, aucun mur entre → visible (même partiellement : 1/3 suffit avec malus).
3. Détection : si visible, += (100/dist_m) * dt * modificateurs; sinon -= 20*dt. Seuils : 30 % Suspect, 70 % Alerte, 100 % Combat (attaque).
4. Ombre : tuiles 'ombre' (layer) → modificateur -30 %; accroupi -50 %.
5. Feedback UI : œil au-dessus du garde (gris/jaune/rouge + jauge).

**Sorties attendues** :
- Le système de détection avec cône visuel et raycasts
- La jauge de détection + états du garde
- Les modificateurs ombre/accroupi/camouflage

**Exemple de prompt** :
> « Mon jeu d'infiltration détecte le joueur derrière les murs : 3 raycasts (tête/corps/pieds) avec occlusion, cône 70°/12 m, jauge 0-100 %, ombre -30 %, états Suspect/Alerte/Combat. »

**Cas d'usage** : Jeux d'infiltration (Metal Gear, Hitman-like). S'articule avec skills 1520 (perception), 1524 et 1519 (FSM).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

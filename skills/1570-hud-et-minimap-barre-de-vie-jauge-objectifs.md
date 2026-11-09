---
num: 1570
resume: "Concevoir le HUD en 2027 : barre de PV/énergie (couleur dynamique inférieur à 30 %, 1535), jauges (dash 1511, mana), munitions, minimap avec marqueurs (quêtes 1531, ennemis si compétence 1520), réticule contextuel, notifications (loot/succès), tout désactivable (1575). Étape 1 : Barre PV : fillAmount + couleur lerp (vert supérieur à 50 %, orange supérieur à 30 %, rouge clignotant inférieur à 30 %)"
lang: "fr"
date_ajout: "2026-11"
nom: "HUD et minimap : barre de vie, jauge, objectifs"
emoji: "🎯"
domaine: "Game Dev"
signal: "Concevoir le HUD d'un jeu en 2027 : barre de vie/PV (couleur qui change sous 30 %, 1535), jauge de dash (cooldown 1511), munitions, minimap (1506 caméra, points quête 1531, ennemis 1520 si compétence), réticule contextuel, notifications (loot 1528, succès 1538), tout désactivable (1575). Utilise pour tout jeu avec un personnage. N'utilise pas pour un jeu d'interface pure."
mot_cle: "HUD barre de vie minimap réticule notifications désactivable accessibilité"
nom_court: "HUD"
branche: "D22"
synonymes: ["barre de PV rouge qui clignote sous 30 %", "minimap avec marqueurs de quêtes (1531)", "HUD désactivable (mode minimaliste 1575)"]
cross_refs: [1531, 1535, 1538]
tags: ["2027"]
depends_on: [1531]
---

## 1570. 🎯 HUD et minimap : barre de vie, jauge, objectifs (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir le HUD en 2027 : barre de PV/énergie (couleur dynamique < 30 %, 1535), jauges (dash 1511, mana), munitions, minimap avec marqueurs (quêtes 1531, ennemis si compétence 1520), réticule contextuel, notifications (loot/succès), tout désactivable (1575).

**Quand l'utiliser (triggers)** :
- Barre de vie qui clignote rouge sous 30 % PV
- Minimap avec marqueurs quête/ennemis/compétence
- HUD minimaliste désactivable (accessibilité 1575)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es UI designer jeu. Tu places : PV haut gauche (barre + chiffre), jauge dash sous le perso, munitions bas droite + réticule centre (change selon l'arme 1535), minimap haut droite (zoom, filtres), notifications haut centre (toast 1538), toasts loot bas gauche (1528). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les stats du joueur (PV, dash, munitions, mana)
- La minimap (monde, caméra 1505/1506)
- Les notifications (quêtes 1531, loot 1528, succès 1538)

**Méthode** :
1. Barre PV : fillAmount + couleur lerp (vert > 50 %, orange > 30 %, rouge clignotant < 30 %).
2. Jauges : dash (cooldown 1511), mana, surchauffe — icône grisée si vide.
3. Minimap : RenderTexture de la caméra top-down orthographique (1505), marqueurs (quête or 1531, ennemis rouge si compétence 'perception' 1520, PNJ).
4. Réticule : point qui s'élargit selon la précision (mouvement 1511), croix si arme, change à la visée (1506 lock-on).
5. Tout désactivable : settings 'HUD minimal' (1575) garde PV + notifications urgentes seulement.

**Sorties attendues** :
- Le HUD complet (PV, jauges, munitions, minimap, réticule)
- Les notifications (quêtes/loot/succès) intégrées
- Le mode HUD minimal (accessibilité)

**Exemple de prompt** :
> « Conçois le HUD de mon action-RPG : barre PV (rouge clignotant < 30 %), jauge dash, munitions, minimap avec marqueurs quête (1531) et ennemis (compétence), réticule dynamique, mode minimal désactivable (1575). »

**Cas d'usage** : Tout jeu avec un personnage à l'écran. S'articule avec skills 1531 (quêtes), 1535 (équipement) et 1538 (succès).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

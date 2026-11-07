---
num: 1504
date_ajout: "2026-11"
nom: "Systeme d'input moderne : actions, gamepad, remappable (2027)"
emoji: "🎮"
domaine: "Game Dev"
signal: "Concevoir un système d'input en 2027 : actions nommées (saut, tir, inventaire) mappées à plusieurs entrées (clavier AZERTY/QWERTY, manette, tactile), Input Actions (Unity) ou InputMap (Godot), remapping par le joueur + sauvegarde des contrôles, coyote via l'input buffer. Utilise pour tout jeu jouable. N'utilise pas pour un jeu piloté à la souris seule."
mot_cle: "input actions remappable gamepad clavier remap contrôles"
nom_court: "Input moderne"
branche: "D1"
synonymes: ["remapper les contrôles par le joueur", "input actions unity ou inputmap godot", "AZERTY et QWERTY supportés"]
cross_refs: [1511, 1571, 1575]
tags: ["2027"]
depends_on: [1511]
---

## 1504. 🎮 Systeme d'input moderne : actions, gamepad, remappable (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire un système d'input moderne en 2027 : actions nommées indépendantes des entrées (clavier AZERTY/QWERTY auto, manette, tactile), remappable par le joueur avec sauvegarde des contrôles, et buffer d'input pour les combos.

**Quand l'utiliser (triggers)** :
- Supporter manette + clavier + AZERTY/QWERTY
- Le joueur veut remapper ses touches
- Buffer d'input pour les combos (格斗)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur input. Tu maps par action (Jump, Fire...) et non par touche, tu détectes le layout clavier (AZERTY/QWERTY), tu sauves les remaps (JSON, skill 1503), et tu ajoutes un input buffer (fenêtre 100 ms) pour les combos. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les actions du jeu (saut, tir, dash, inventaire...)
- Les entrées cibles (clavier, manette Xbox/PS, tactile)
- Le besoin de remap + sauvegarde

**Méthode** :
1. Définir les actions (Input Actions Unity / InputMap Godot) avec entrées par défaut.
2. Détecter le layout clavier (AZERTY vs QWERTY) et ajuster les hints (Z/W).
3. Remap UI : cliquer une action → appuyer sur la touche → sauver (JSON).
4. Input buffer : file des inputs avec timestamp, consommés dans une fenêtre 100 ms.
5. Tester manette Xbox et PS (boutons inversés selon OS), clavier, tactile.

**Sorties attendues** :
- Le système d'actions + remap fonctionnel
- Les contrôles sauvegardés par joueur
- L'input buffer pour combos

**Exemple de prompt** :
> « Mon jeu ne marche qu'avec WASD : ajoute le support manette + AZERTY auto + remap par le joueur sauvegardé (JSON) + input buffer 100 ms. »

**Cas d'usage** : Tout jeu jouable, accessibilité des contrôles. S'articule avec skills 1511 (coyote/buffer), 1571 (menus manette) et 1575 (accessibilité).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

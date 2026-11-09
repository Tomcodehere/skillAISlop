---
num: 1571
resume: "Rendre les menus navigables en 2027 au clavier et à la manette : focus visible (anneau), navigation directionnelle (D-pad/flèches), valider (Entrée/A), retour (Échap/B), remap (1504), test 100 % clavier sans souris. Étape 1 : Chaque écran : 1er élément focusé automatiquement (bouton 'Jouer')."
date_ajout: "2026-11"
nom: "Menus accessibles : navigation clavier et manette"
emoji: "🎛️"
domaine: "Game Dev"
signal: "Rendre les menus d'un jeu navigables en 2027 au clavier ET à la manette (pas souris seule) : focus visible, ordre de tabulation logique, navigation directionnelle (haut/bas/gauche/droite), valider (Entrée/A), retour (Echap/B), remap des contrôles de menu (1504), test au clavier sans souris. Utilise pour tous les menus. N'utilise pas pour le HUD in-game (1570)."
mot_cle: "menus accessibles clavier manette focus visible navigation directionnelle remap"
nom_court: "Menus a11y"
branche: "D22"
synonymes: ["naviguer au clavier dans les menus (tab + entrée)", "focus visible sur le bouton sélectionné", "manette : A valider, B retour, croix directionnelle"]
cross_refs: [1504, 1575, 1484]
tags: ["2027"]
depends_on: [1504]
---

## 1571. 🎛️ Menus accessibles : navigation clavier et manette (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre les menus navigables en 2027 au clavier et à la manette : focus visible (anneau), navigation directionnelle (D-pad/flèches), valider (Entrée/A), retour (Échap/B), remap (1504), test 100 % clavier sans souris.

**Quand l'utiliser (triggers)** :
- On ne peut pas jouer sans souris (menus)
- Focus clavier visible sur le bouton
- Manette : A valider B retour navigation D-pad

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es UI designer accessibilité menus. Tu utilises le système d'UI (EventSystem Unity, Godot Control focus), focus initial sur le 1er bouton, navigation explicite (select on up/down), focus visible (couleur/outline), sons de navigation (1568). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les écrans de menu (principal, settings 1574, pause)
- Le système UI du moteur
- Le remap des contrôles (1504)

**Méthode** :
1. Chaque écran : 1er élément focusé automatiquement (bouton 'Jouer').
2. Navigation explicite : chaque bouton a SelectOnUp/Down/Left/Right (ou auto par position).
3. Focus visible : outline/animé (couleur primaire, scale 1,05) + son (1568).
4. Clavier : Tab/Shift+Tab cycle, Entrée = valider, Échap = retour. Manette : A valider, B retour, D-pad/stick navigation.
5. Test : débrancher la souris, finir le menu principal → jouer, changer un réglage, quitter — 100 % clavier.

**Sorties attendues** :
- Les menus 100 % navigables clavier + manette
- Le focus visible et sonore
- Le test clavier complet documenté

**Exemple de prompt** :
> « On ne peut pas quitter le menu principal sans souris : rends tous les menus navigables clavier (Tab/Entrée/Échap, focus visible animé + son) et manette (A/B/D-pad), test 100 % sans souris. »

**Cas d'usage** : Menus, settings, inventaire (1534). S'articule avec skills 1504 (input remap), 1575 (accessibilité) et 1484 (a11y design).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

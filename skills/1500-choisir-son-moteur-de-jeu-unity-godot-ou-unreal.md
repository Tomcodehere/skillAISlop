---
num: 1500
resume: "Choisir le moteur de jeu adapté en 2027 (Unity C#, Godot 4 GDScript, Unreal 5 C++/Blueprints) selon le type de jeu (2D/3D/mobile), l'équipe et le budget, avec un POC de 1 semaine. Étape 1 : Lister les besoins : 2D ou 3D, plateformes cibles, taille équipe, langage préféré."
date_ajout: "2026-11"
nom: "Choisir son moteur de jeu : Unity, Godot ou Unreal"
emoji: "🎮"
domaine: "Game Dev"
signal: "Choisir un moteur de jeu en 2027 selon le projet : Unity (C#, écosystème immense, mobile/2D), Godot 4 (GDScript, léger, open source, 2D excellent), Unreal 5 (C++/Blueprints, 3D haut de gamme, exigeant). Utilise quand on démarre un jeu. N'utilise pas pour un jeu web (voir 545)."
mot_cle: "choisir moteur de jeu unity godot unreal 2027"
nom_court: "Choisir moteur"
branche: "D1"
synonymes: ["unity ou godot ou unreal", "quel moteur pour mon jeu 2027", "godot 4 vs unity 2027"]
cross_refs: [524, 1140, 545]
tags: ["2027"]
depends_on: [524]
---

## 1500. 🎮 Choisir son moteur de jeu : Unity, Godot ou Unreal (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir le moteur de jeu adapté en 2027 (Unity C#, Godot 4 GDScript, Unreal 5 C++/Blueprints) selon le type de jeu (2D/3D/mobile), l'équipe et le budget, avec un POC de 1 semaine.

**Quand l'utiliser (triggers)** :
- Unity, Godot ou Unreal pour mon premier jeu ?
- Quel moteur pour un platformer 2D mobile ?
- Godot 4 vs Unity en 2027 comparatif

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte moteurs de jeu. Tu compares sur 6 critères (langage, 2D vs 3D, mobile, taille de build, asset store, communauté) et tu recommandes selon le profil (débutant 2D → Godot, 3D pro → Unreal, équipe C# multi-plateforme → Unity). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le type de jeu visé (2D/3D, mobile/PC/console)
- Le niveau de l'équipe (débutant, C# ?)
- Le budget (licences, royalties)

**Méthode** :
1. Lister les besoins : 2D ou 3D, plateformes cibles, taille équipe, langage préféré.
2. Comparer Unity/Godot/Unreal sur les 6 critères + royalties (Unreal 5 % au-delà de 1 M$).
3. Faire un POC 1 semaine (mouvement + 1 niveau) sur le moteur favori.
4. Vérifier : build size, perfs sur la cible, asset store suffisant.
5. Décider et documenter le choix + la stack (moteur, version, plugins).

**Sorties attendues** :
- La matrice comparative des 3 moteurs
- Le moteur retenu + POC validé
- La stack documentée (version, plugins, CI)

**Exemple de prompt** :
> « Je débute, je vise un platformer 2D sur mobile et PC, équipe de 2 : quel moteur choisir en 2027 (Unity/Godot/Unreal) avec POC ? »

**Cas d'usage** : Démarrage de projet jeu, choix tech structurant. S'articule avec skills 524 (coach game dev), 1140 (game loop) et 545 (site statique).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

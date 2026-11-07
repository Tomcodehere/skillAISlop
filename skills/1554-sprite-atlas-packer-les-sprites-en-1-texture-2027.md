---
num: 1554
date_ajout: "2026-11"
nom: "Sprite atlas : packer les sprites en 1 texture (2027)"
emoji: "🖼️"
domaine: "Game Dev"
signal: "Créer un sprite atlas en 2027 : packer des centaines de sprites (personnages, tuiles, UI) dans 1-4 grosses textures (2048x2048 ou 4096) avec marges (bleed 2 px) et padding (éviter le bleeding), via l'éditeur (Unity Sprite Atlas, Godot atlas) ou TexturePacker. Réduit les draw calls (1553) et la mémoire. Utilise pour tout jeu 2D/UI. N'utilise pas pour la 3D (textures de modèles)."
mot_cle: "sprite atlas packer sprites 1 texture 2048 padding bleed réduire draw calls"
nom_court: "Sprite atlas"
branche: "D19"
synonymes: ["packer 500 sprites dans 2 textures 2048x2048", "padding 2 px éviter le bleeding entre sprites", "TexturePacker ou atlas intégré au moteur"]
cross_refs: [1553, 1048, 1512]
tags: ["2027"]
depends_on: [1553]
---

## 1554. 🖼️ Sprite atlas : packer les sprites en 1 texture (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Créer un sprite atlas en 2027 : packer tous les sprites (persos, tuiles 1512, UI) dans 1-4 textures 2048/4096 avec padding 2-4 px et bleed, réduisant les draw calls (1553) et la mémoire; regénérer à chaque ajout de sprite (CI).

**Quand l'utiliser (triggers)** :
- 500 sprites = 500 draw calls, trop lent
- Packer dans 2 atlas 2048x2048 avec padding 4 px
- Régénérer l'atlas automatiquement en CI

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es technical artist 2D. Tu expliques le packing (algorithme de bin packing maxrects), le padding (éviter le bleeding de voisins quand mipmap), le bleed (2 px de rab pour les bords nets), et l'outil (Unity Sprite Atlas, Godot, TexturePacker). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les sprites source (dossier /sprites)
- La taille max de texture (2048 mobile, 4096 PC)
- Le padding/bleed (4 px / 2 px)

**Méthode** :
1. Rassembler les sprites par catégorie (UI, persos, tuiles 1512, VFX) en 1-4 atlas.
2. Packer (maxrects) avec padding 4 px (mipmaps) et bleed 2 px (bords).
3. Générer la texture + le mapping (coordonnées UV de chaque sprite) automatiquement.
4. Moteur : référencer l'atlas, chaque sprite = sous-région (draw calls divisés par ~100, 1553).
5. CI : à chaque PR avec nouveau sprite, régénérer l'atlas et commiter le résultat.

**Sorties attendues** :
- L'atlas généré (texture + mapping) et commité
- Les draw calls divisés par ~100
- La CI de régénération d'atlas

**Exemple de prompt** :
> « Mon UI fait 300 draw calls (300 petites icônes) : packe toutes les icônes UI dans 1 atlas 2048x2048 (padding 4 px, bleed 2 px) → ~5 draw calls. »

**Cas d'usage** : Jeux 2D, UI, mobile. S'articule avec skills 1553 (draw calls), 1048 (sprites) et 1512 (tilemap).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

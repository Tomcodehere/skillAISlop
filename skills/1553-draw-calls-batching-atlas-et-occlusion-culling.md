---
num: 1553
resume: "Réduire les draw calls en 2027 (objectif inférieur à 300 sur mobile) : sprite atlas (1 texture = 1 draw call), batching statique + SRP Batcher, occlusion culling, LOD (modèle simplifié au loin), mesuré au Frame Debugger (1552). Étape 1 : Mesurer : Frame Debugger, compter les draw calls (mobile cible inférieur à 300, PC inférieur à 2000)."
date_ajout: "2026-11"
nom: "Draw calls : batching, atlas et occlusion culling"
emoji: "🖼️"
domaine: "Game Dev"
signal: "Réduire les draw calls en 2027 : chaque objet affiché = 1 draw call (2000 objets = 2000 appels GPU lents). Solutions : sprite atlas (1554, tout dans 1 texture = 1 draw call), batching statique (objets immobiles fusionnés), SRP Batcher (Unity), occlusion culling (ne pas rendre ce qui est caché), LOD (loin = modèle simple). Utilise quand le render rame. N'utilise pas avant d'avoir profilé (1552)."
mot_cle: "draw calls sprite atlas batching statique SRP Batcher occlusion culling LOD"
nom_court: "Draw calls"
branche: "D1"
synonymes: ["2000 objets = 2000 draw calls trop lent", "sprite atlas tout en 1 texture = 1 draw call", "occlusion culling ne pas rendre caché + LOD loin"]
cross_refs: [1552, 1554, 309]
tags: ["2027"]
depends_on: [1552]
---

## 1553. 🖼️ Draw calls : batching, atlas et occlusion culling (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Réduire les draw calls en 2027 (objectif < 300 sur mobile) : sprite atlas (1 texture = 1 draw call), batching statique + SRP Batcher, occlusion culling, LOD (modèle simplifié au loin), mesuré au Frame Debugger (1552).

**Quand l'utiliser (triggers)** :
- 2000 draw calls sur mobile = 15 fps
- Tout mettre dans un atlas de sprites
- LOD : loin on affiche un modèle à 500 tris au lieu de 50k

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur rendu. Tu expliques draw call = appel CPU→GPU par objet/material; remèdes : atlas (1554), static batching (combine meshes immobiles), SRP Batcher (même matériau), occlusion culling (camera), LOD groups (3 niveaux). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le Frame Debugger (1552) montrant N draw calls
- Les sprites/objets à atlaser (1554)
- Les objets statiques vs dynamiques

**Méthode** :
1. Mesurer : Frame Debugger, compter les draw calls (mobile cible < 300, PC < 2000).
2. Atlas : packer tous les sprites UI/2D dans 1-4 textures (1554) → 1 draw call par couche.
3. Static batching : objets immobiles (arbres, rochers) fusionnés en 1 mesh au chargement.
4. SRP Batcher : même matériau → le moteur groupe automatiquement (activer).
5. Occlusion culling : ce qui est derrière un mur n'est pas rendu (bake). LOD : 3 niveaux de détail selon distance caméra.

**Sorties attendues** :
- Les draw calls réduits (ex. 2000 → 250) mesurés
- L'atlas + batching + occlusion + LOD en place
- Le gain de fps mesuré (15 → 60)

**Exemple de prompt** :
> « Mon niveau 2D fait 1800 draw calls (15 fps mobile) : atlas tous les sprites (1 texture), static batching des décors, occlusion culling, LOD → mesurer < 300 draw calls et 60 fps. »

**Cas d'usage** : Optimisation rendu 2D/3D. S'articule avec skills 1552 (profilage), 1554 (atlas) et 309 (bench).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

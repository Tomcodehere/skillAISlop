---
num: 1585
date_ajout: "2026-11"
nom: "Performance mobile : 60 fps, batterie et thermique"
emoji: "🔋"
domaine: "Game Dev"
signal: "Optimiser un jeu mobile pour 60 fps stables en 2027 : profiler (1552) sur appareil réel (pas émulateur), réduire draw calls (1553), particules GPU cap (1557), pas d'alloc par frame (pooling 1551), textures compressées (ASTC/ETC2), modèle LOD (1553), limiter la fréquence CPU/GPU (QualitySettings), surveiller batterie/thermique (throttling après 10 min). Utilise avant sortie mobile. N'utilise pas pour PC/console."
mot_cle: "performance mobile 60 fps batterie thermique ASTC draw calls LOD throttling"
nom_court: "Perf mobile"
branche: "D1"
synonymes: ["60 fps stables sur téléphone milieu de gamme", "textures ASTC compressées (mémoire GPU divisée)", "throttling thermique après 10 min de jeu"]
cross_refs: [1552, 1553, 1590]
tags: ["2027"]
depends_on: [1590]
---

## 1585. 🔋 Performance mobile : 60 fps, batterie et thermique (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Tenir 60 fps stables sur mobile en 2027 : profiler sur appareil réel (1552), draw calls < 100 (1553), particules GPU cap 2000 (1557), 0 alloc/frame (1551), textures ASTC, LOD, fréquence CPU/GPU adaptative, batterie/thermique surveillés.

**Quand l'utiliser (triggers)** :
- Le jeu passe à 25 fps sur Xiaomi milieu de gamme
- 0 allocation GC par frame (pooling 1551)
- Textures ASTC pour diviser la mémoire GPU par 4

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur optimisation mobile. Tu fais un passe perf mobile : QualitySettings (pixel light count, shadows off sur bas de gamme), textures ASTC 6x6, atlas (1554), draw calls < 100 (1553), particules cap 2000 (1557), 0 alloc (1551), LOD, et un mode 'économie de batterie' (1574). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'appareil cible (milieu de gamme 2027 : Snapdragon 7, 8 Go RAM)
- Le profiler sur device (1552) : fps, ms CPU/GPU, mémoire
- Les cibles (60 fps, < 30 % batterie/30 min, pas de throttle)

**Méthode** :
1. Profiler sur le device réel (Android Profiler/Xcode) : viser 60 fps constant, < 16 ms/frame, mémoire stable.
2. Render : draw calls < 100 (atlas 1554, batching 1553, occlusion), particules cap 2000 GPU (1557), ombres désactivables, LOD 3 niveaux.
3. CPU : 0 alloc par frame (pool 1551, string pool), physique à 30 Hz (1501), pathfinding hors frame principale (1517 flow field).
4. GPU : textures ASTC 6x6 (mémoire/4), résolution dynamique (baisser si < 55 fps), post-FX off sur bas de gamme (1555).
5. Batterie/thermique : mode économie (30 fps, luminosité) après 10 min ou batterie < 20 % (1574); mesurer conso (adb).

**Sorties attendues** :
- Le jeu à 60 fps stables sur le device cible (profilé)
- Les optimisations appliquées (atlas, pool, ASTC, LOD)
- Le mode économie batterie/thermique

**Exemple de prompt** :
> « Le jeu rame (25 fps) sur Xiaomi Snapdragon 7 : profile sur device (1552), draw calls < 100 (atlas 1554), particules cap 2000 GPU (1557), 0 alloc (1551), textures ASTC, LOD, mode batterie (1574) → 60 fps. »

**Cas d'usage** : Sortie mobile. S'articule avec skills 1552 (profilage), 1553 (draw calls) et 1590 (build mobile).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

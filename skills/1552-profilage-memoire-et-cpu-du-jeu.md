---
num: 1552
resume: "Profiler un jeu en 2027 : Memory Profiler (fuites, allocations par frame), CPU Profiler (système par système, deep profile), Render (draw calls 1553, overdraw, tris), avec captures avant/après chaque optimisation. Étape 1 : Memory : Memory Profiler, snapshot avant/après chargement de niveau → fuite = objets non libérés (UnloadUnusedAssets, ou objets statiques qui grossissent)."
date_ajout: "2026-11"
nom: "Profilage memoire et CPU du jeu"
emoji: "📊"
domaine: "Game Dev"
signal: "Profiler un jeu en 2027 pour trouver les fuites et goulots : Unity Profiler / Godot debugger, Memory Profiler (fuites, allocations/frame), CPU (quel système prend 8 ms ?), render (draw calls, overdraw), captures comparatives avant/après. Utilise quand le jeu rame ou fuite. N'utilise pas sans symptôme (ne pas over-optimiser)."
mot_cle: "profiler jeu Unity Profiler Memory Profiler fuites draw calls CPU render"
nom_court: "Profilage"
branche: "D1"
synonymes: ["fuite mémoire : +50 Mo par niveau chargé", "quel système prend 8 ms de CPU ?", "draw calls 2000 → batching pour passer à 200"]
cross_refs: [308, 309, 1551]
tags: ["2027"]
depends_on: [309]
---

## 1552. 📊 Profilage memoire et CPU du jeu (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Profiler un jeu en 2027 : Memory Profiler (fuites, allocations par frame), CPU Profiler (système par système, deep profile), Render (draw calls 1553, overdraw, tris), avec captures avant/après chaque optimisation.

**Quand l'utiliser (triggers)** :
- Le jeu fuite (+50 Mo à chaque niveau)
- Quel système bouffe 8 ms de CPU ?
- 2000 draw calls → objectif 200 (batching)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur performance. Tu fais : capture baseline (Memory + CPU + Render), identifier le top 3 (ex. 8 ms dans le pathfinding, 1,2 Mo alloués par frame, 2000 draw calls), corriger (pool 1551, batching 1553), re-capturer et comparer. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le build de dev avec profiler actif
- La scène qui rame/le niveau qui fuit
- Les cibles (60 fps, < 100 Mo heap growth/niveau)

**Méthode** :
1. Memory : Memory Profiler, snapshot avant/après chargement de niveau → fuite = objets non libérés (UnloadUnusedAssets, ou objets statiques qui grossissent).
2. CPU : Profiler deep profile, trier par self time → top système (souvent pathfinding/AI/physique), optimiser (cache, moins d'appels).
3. Render : Frame Debugger, compter draw calls (objectif < 300 mobile), overdraw (occlusion culling), tris.
4. Itérer : capture → fix top 1 → re-capture, jusqu'aux cibles (60 fps constant, pas de fuite).

**Sorties attendues** :
- Les 3 captures (mémoire/CPU/render) avant/après
- Le top 3 des goulots identifiés et corrigés
- Les cibles atteintes (60 fps, pas de fuite)

**Exemple de prompt** :
> « Mon jeu rame sur téléphone et fuite à chaque niveau : profile (Memory Profiler fuite, CPU deep profile, Frame Debugger draw calls), corrige le top 3, re-vérifie 60 fps stable. »

**Cas d'usage** : Optimisation ciblée, release. S'articule avec skills 308 (profileur code), 309 (bench) et 1551 (pooling).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

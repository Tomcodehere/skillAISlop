---
num: 1606
date_ajout: "2026-11"
nom: "WebGPU cross-browser : 3D et calcul GPU côté client"
emoji: "🎨"
domaine: "Développement"
signal: "Exploiter WebGPU en 2027 (déployé cross-browser fin 2025 / WebKit+Firefox début 2026) : accès direct au GPU du navigateur pour du 3D (Three.js/WebGPU, Babylon) ET du calcul général (compute shaders : ML, physique, data viz lourde). Utilise quand WebGL ne suffit plus. N'utilise pas pour du simple 2D (canvas suffit)."
mot_cle: "webgpu cross-browser 2027 3D calcul GPU compute shaders client"
nom_court: "WebGPU"
branche: "D1"
synonymes: ["webgpu dans tous les navigateurs fin 2025", "calcul GPU côté client compute shaders", "webgpu vs webgl choisir 2027"]
cross_refs: [1270, 142, 1557]
tags: ["2027"]
depends_on: [1270]
---

## 1606. 🎨 WebGPU cross-browser : 3D et calcul GPU côté client (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser WebGPU en 2027 (cross-browser fin 2025/début 2026) : rendu 3D moderne (Three.js WebGPU) ou calcul GPU client (compute shaders : inférence ML 1607, physique, data viz), avec fallback WebGL.

**Quand l'utiliser (triggers)** :
- Mon appli 3D rame en WebGL
- webgpu compute shader calcul côté client
- webgpu déployé partout fin 2025 safari firefox 2026

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev GPU web. Tu montres : détection navigator.gpu, fallback WebGL, un compute shader simple (somme parallèle), Three.js en mode WebGPU, et tu mesures le gain vs CPU. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'app avec besoin GPU (3D, ML, simulation)
- Le navigateur cible (support WebGPU ?)
- Le fallback (WebGL 1270)

**Méthode** :
1. Détecter : if (navigator.gpu) → WebGPU, sinon fallback WebGL (1270).
2. Rendu 3D : Three.js (renderer WebGPU) ou Babylon.js, même code, perfs meilleures.
3. Compute : écrire un compute shader WGSL (ex. somme de 1M de nombres en parallèle), envoyer au GPU, lire le résultat.
4. ML client : ONNX Runtime Web avec backend WebGPU (1607).
5. Mesurer : fps / temps de calcul vs CPU (objectif x10-x100 sur gros volumes).

**Sorties attendues** :
- L'app WebGPU avec fallback WebGL
- Le compute shader WGSL fonctionnel (gain mesuré)
- Le benchmark WebGPU vs CPU vs WebGL

**Exemple de prompt** :
> « Ma simu physique de 100k particules rame en CPU (2 fps) : passe le calcul en compute shader WebGPU (WGSL, cross-browser 2027), objectif 60 fps, fallback WebGL. »

**Cas d'usage** : 3D web, ML client, simulations, data viz lourde. S'articule avec skills 1270 (shaders), 142 (3D), 1557 (particules).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

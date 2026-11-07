---
num: 1515
date_ajout: "2026-11"
nom: "Bruit de Perlin pour terrain et heightmap (2027)"
emoji: "🌊"
domaine: "Game Dev"
signal: "Générer du terrain 2D/3D avec le bruit de Perlin en 2027 : octaves (fréquences multiples + amplitudes décroissantes = fractal), seuils (eau sous 0,3 inf. à  sable sous 0,5 inf. à  herbe sous 0,8 inf. à  roche inf. à  neige), seed pour reproductibilité. Utilise pour maps ouvertes, îles, reliefs. N'utilise pas pour des donjons (voir 1513/1514)."
mot_cle: "bruit de Perlin terrain heightmap octaves fractal seed seuils biomes"
nom_court: "Perlin"
branche: "D1"
synonymes: ["générer une île avec Perlin noise", "heightmap terrain 3D procédural", "octaves fractal bruit Perlin 2027"]
cross_refs: [1514, 1516, 1512]
tags: ["2027"]
depends_on: [1514]
---

## 1515. 🌊 Bruit de Perlin pour terrain et heightmap (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Générer un terrain avec le bruit de Perlin en 2027 : plusieurs octaves (fractal, fréquence x2 amplitude /2), normalisation 0-1, seuils par biome (eau/sable/herbe/roche/neige), seed fixe pour la même map.

**Quand l'utiliser (triggers)** :
- Générer une île jouable aléatoire
- Heightmap 3D avec Perlin + octaves
- Biomes selon le seuil de hauteur (eau, neige...)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur procgen terrain. Tu expliques Perlin (gradient noise, valeurs lissées entre nœuds aléatoires), le fractal (somme d'octaves), et les seuils de biomes; en 3D le heightmap pilote le mesh, en 2D la couleur de tuile (1512). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La taille de la carte et l'échelle (ex. 0,05)
- Le nombre d'octaves (4-6) et le persistence (0,5)
- Les seuils de biomes et la seed

**Méthode** :
1. Implémenter/récupérer Perlin 2D (Godot noise, Unity Mathf.PerlinNoise, lib custom).
2. Fractal : sum(octaves) avec fréquence *= lacunarity (2), amplitude *= persistence (0,5), normaliser.
3. Seuils : val < 0,3 eau, < 0,45 sable, < 0,7 herbe, < 0,85 roche, sinon neige.
4. En 2D : couleur de tuile selon seuil (1512) ; en 3D : hauteur du vertex (y = val * amplitude).
5. Seed : même seed → même map (debug + saves), sinon random.

**Sorties attendues** :
- Le terrain/île généré (Perlin + octaves + biomes)
- La map reproductible (seed)
- Les seuils de biomes configurés

**Exemple de prompt** :
> « Génère une île jouable pour mon jeu de survie : Perlin 5 octaves (persistence 0,5), seuils eau<0,3<sable<0,5<herbe<0,8<roche<neige, seed reproductible. »

**Cas d'usage** : Maps ouvertes, survie, stratégie, génération de monde. S'articule avec skills 1514 (CA), 1516 (WFC) et 1512 (tilemap).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

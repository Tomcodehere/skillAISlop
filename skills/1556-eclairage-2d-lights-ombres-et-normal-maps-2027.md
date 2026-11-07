---
num: 1556
date_ajout: "2026-11"
nom: "Eclairage 2D : lights, ombres et normal maps (2027)"
emoji: "💡"
domaine: "Game Dev"
signal: "Ajouter de l'éclairage 2D en 2027 (Godot 2D lights, Unity URP 2D lights) : sources de lumière (ponctuelles, directionnelles), occlusion des ombres (les murs bloquent la lumière via raycast 1524 ou light occluders), normal maps 2D (texture de normales pour l'effet de relief), blend additif. Utilise pour l'ambiance (donjon sombre, torches). N'utilise pas pour un jeu 2D plat sans ambiance."
mot_cle: "éclairage 2D lights occluders ombres normal map 2D torches"
nom_court: "Lumière 2D"
branche: "D19"
synonymes: ["torches qui éclairent et les murs font ombre", "normal map 2D pour le relief des sprites", "light occluders bloquent la lumière 2D"]
cross_refs: [1524, 1512, 1555]
tags: ["2027"]
depends_on: [1524]
---

## 1556. 💡 Eclairage 2D : lights, ombres et normal maps (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ajouter de l'éclairage 2D en 2027 : points de lumière (torches, joueur), occluders (murs qui font ombre, via light occluder ou raycast 1524), normal maps 2D pour le relief, mode de blend additif, perf sur mobile (limite de lights).

**Quand l'utiliser (triggers)** :
- Une torche qui éclaire autour et les murs font ombre
- Normal map sur mes sprites 2D (relief)
- Trop de lights = lag (limite 8-16 actifs)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es technical artist 2D lumière. Tu configures : PointLight2D (Unity URP 2D / Godot) avec rayon/couleur, occluders (LightOccluder2D sur les murs), normal map (texture _normal avec le sprite), blend mode additif, et une limite de lights actifs (les plus proches du joueur). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les sources de lumière (torches, joueur, explosions)
- Les occluders (murs, rochers)
- La normal map des sprites importants

**Méthode** :
1. Ajouter les PointLight2D : torches (orange, flicker), joueur (petit halo), explosions (flash bref + gros rayon).
2. Occluders : chaque mur a un LightOccluder2D (forme de l'ombre) → la lumière est bloquée (ombres douces).
3. Normal map : sprite + texture de normales (générée ou peinte) → la lumière donne du relief (haut/bas).
4. Perf mobile : max 8-16 lights actifs (les plus proches du joueur, triés par distance), le reste en 'unlit'.
5. Ambiance : fond sombre (CanvasModulate noir 0,2) + lumières qui ressortent (donjon).

**Sorties attendues** :
- L'éclairage 2D avec ombres (occluders) et normal maps
- La limite de lights actifs (perf mobile)
- L'ambiance donjon (sombre + torches)

**Exemple de prompt** :
> « Mon donjon 2D est plat et lumineux partout : mets un fond sombre (CanvasModulate 0,2), des torches (PointLight2D orange flicker) avec occluders sur les murs, normal maps sur les pierres. »

**Cas d'usage** : Jeux 2D d'ambiance (donjon, horreur, aventure). S'articule avec skills 1524 (raycast), 1512 (tilemap) et 1555 (post-FX).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

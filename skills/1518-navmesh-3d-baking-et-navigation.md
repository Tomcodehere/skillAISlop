---
num: 1518
resume: "Baker et utiliser un navmesh 3D en 2027 : marquer la géométrie walkable (pentes max, hauteur agent), bake le navmesh, agents NavigationAgent qui le suivent avec évitement, mise à jour locale pour obstacles dynamiques. Étape 1 : Marquer les surfaces walkable (layer/zone), exclure pentes supérieur à 45° et trous inférieur à hauteur agent."
date_ajout: "2026-11"
nom: "Navmesh 3D : baking et navigation"
emoji: "🧭"
domaine: "Game Dev"
signal: "Utiliser un navmesh 3D en 2027 (existe 1224 sur pathfinding général) : bake de la navigation sur la géométrie walkable (Unreal NavMesh, Unity AI Navigation, Godot NavigationServer), agents qui suivent (NavigationAgent), recast local pour obstacles dynamiques. Utilise pour PNJ en 3D. N'utilise pas en 2D (voir A* 1517)."
mot_cle: "navmesh 3D baking navigation agent recast obstacles dynamiques"
nom_court: "Navmesh 3D"
branche: "D1"
synonymes: ["baker la navigation 3D sur le niveau", "NavigationAgent suit le navmesh", "obstacles dynamiques navmesh local"]
cross_refs: [1224, 1517, 1520]
tags: ["2027"]
depends_on: [1224]
---

## 1518. 🧭 Navmesh 3D : baking et navigation (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Baker et utiliser un navmesh 3D en 2027 : marquer la géométrie walkable (pentes max, hauteur agent), bake le navmesh, agents NavigationAgent qui le suivent avec évitement, mise à jour locale pour obstacles dynamiques.

**Quand l'utiliser (triggers)** :
- Baker le navmesh de mon niveau 3D
- PNJ qui suivent un chemin en 3D (escaliers, pentes)
- Un obstacle apparaît : mettre à jour le navmesh localement

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur navigation 3D. Tu expliques le bake (paramètres : rayon/height agent, pente max 45°, step height), les NavigationAgent (path, velocity, avoidance), et le recast local (navmesh modifiable à runtime pour portes/barricades). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La géométrie du niveau (walkable)
- Les paramètres d'agent (taille, pente max)
- Les obstacles dynamiques (portes)

**Méthode** :
1. Marquer les surfaces walkable (layer/zone), exclure pentes > 45° et trous < hauteur agent.
2. Baker le navmesh (éditeur ou runtime) → maillage de navigation.
3. Agent : set_target_position → suit le path, évitement (RVO) entre agents.
4. Obstacles dynamiques : navmesh obstacle (carving) ajouté/retiré à runtime, ou recast local.
5. Debug : afficher le navmesh (vert) et les paths des agents (lignes).

**Sorties attendues** :
- Le navmesh baké et les agents qui naviguent
- L'évitement entre agents (RVO)
- Le carving d'obstacles dynamiques

**Exemple de prompt** :
> « Mes PNJ 3D ne montent pas les escaliers : bake un navmesh (pente max 45°, hauteur agent 2 m) et mets des NavigationAgent avec évitement. »

**Cas d'usage** : PNJ 3D, action/aventure, foules 3D. S'articule avec skills 1224 (pathfinding), 1517 (A* 2D) et 1520 (perception).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

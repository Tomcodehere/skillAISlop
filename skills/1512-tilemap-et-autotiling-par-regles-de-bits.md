---
num: 1512
resume: "Construire des niveaux 2D sur tilemap en 2027 : grille 16/32 px, autotiling par règles de bits (47 tuiles selon les 8 voisins), peinture dans l'éditeur, collision auto par tuile, 3 couches (sol/décor/avant-plan avec parallax). Étape 1 : Préparer le tileset avec les 47 tuiles d'autotiling (bords, coins, centre)."
lang: "fr"
date_ajout: "2026-11"
nom: "Tilemap et autotiling par regles de bits"
emoji: "🧱"
domaine: "Game Dev"
signal: "Construire des niveaux 2D avec une tilemap en 2027 : grille de tuiles (16/32 px), autotiling par règles de bits (47 tuiles selon les voisins N/S/E/O), peinture dans l'éditeur, collision automatique par tuile, couches (sol/décor/avant-plan). Utilise pour tout jeu 2D tile-based. N'utilise pas pour la 3D (voxels)."
mot_cle: "tilemap autotiling règles de bits 47 tuiles collision auto"
nom_court: "Tilemap"
branche: "D1"
synonymes: ["peindre un niveau avec des tuiles", "autotiling 47 tuiles selon voisins", "collision auto par tuile tilemap"]
cross_refs: [1513, 1140, 1554]
tags: ["2027"]
depends_on: [1140]
---

## 1512. 🧱 Tilemap et autotiling par regles de bits (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire des niveaux 2D sur tilemap en 2027 : grille 16/32 px, autotiling par règles de bits (47 tuiles selon les 8 voisins), peinture dans l'éditeur, collision auto par tuile, 3 couches (sol/décor/avant-plan avec parallax).

**Quand l'utiliser (triggers)** :
- Peindre un niveau tile par tile dans l'éditeur
- Autotiling : la bonne tuile selon les voisins (47 règles)
- Collision automatique selon la tuile

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es level designer technique. Tu expliques les règles de bits (4 bits cardinaux = 16 cas, étendu 8 bits = 47), le masque d'autotiling dans l'éditeur (Godot TileMap / Unity 2D Tilemap Editor), et la collision/one-way par tuile. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le tileset (tuiles 16 ou 32 px)
- Les règles d'autotiling (which neighbors → which tile)
- Les couches (sol, décor, avant-plan)

**Méthode** :
1. Préparer le tileset avec les 47 tuiles d'autotiling (bords, coins, centre).
2. Configurer la tilemap : grille, autotile avec règles de bits, dans l'éditeur.
3. Peindre le niveau (sol d'abord, puis décor), plusieurs couches pour le parallax.
4. Collision : tuile 'solide' → hitbox auto (static body), one-way pour les plateformes.
5. Exporter/charger : la tilemap en ressource, instanciée au chargement du niveau.

**Sorties attendues** :
- La tilemap avec autotiling fonctionnel
- Le niveau peint rapidement (sol + décor + avant-plan)
- La collision auto par tuile

**Exemple de prompt** :
> « Créer un niveau de caverne 2D rapidement : tilemap 16 px, autotiling 47 tuiles (bords/coins selon voisins), 3 couches, collision auto sur les tuiles solides. »

**Cas d'usage** : Plateformers 2D, RPG 2D top-down, rogue-like. S'articule avec skills 1513 (procgen donjons), 1140 (ECS) et 1554 (atlas sprites).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

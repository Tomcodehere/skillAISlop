---
num: 1513
date_ajout: "2026-11"
nom: "Generation procédurale de donjons : rooms et corridors"
emoji: "🏰"
domaine: "Game Dev"
signal: "Générer un donjon procédural en 2027 par placement de salles + corridors : placer N salles aléatoires sans chevauchement (rejet ou poussée), connecter les centres (MST ou plus proche voisin), instancier les tuiles (1512), placer ennemis/loot (1528). Utilise pour les roguelikes. N'utilise pas pour un niveau hand-crafted."
mot_cle: "génération procédurale donjon salles corridors roguelike"
nom_court: "Procgen donjon"
branche: "D1"
synonymes: ["générer un donjon aléatoire rooms corridors", "roguelike niveau procédural 2027", "salles sans chevauchement + MST"]
cross_refs: [1512, 1514, 1528]
tags: ["2027"]
depends_on: [1512]
---

## 1513. 🏰 Generation procédurale de donjons : rooms et corridors (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Générer un donjon procédural en 2027 : placer 10-15 salles rectangulaires sans chevauchement (avec marge), connecter leurs centres par corridors (plus proche voisin ou arbre couvrant minimal), instancier sur la tilemap (1512).

**Quand l'utiliser (triggers)** :
- Générer un donjon différent à chaque partie
- Salles aléatoires sans se chevaucher
- Relier les salles par des corridors en L

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur procgen. Tu décris l'algo : placer salles (retry 100x si chevauchement), trier par x, connecter chaque salle à la plus proche précédente (corridor en L horizontal puis vertical), puis instancier tuiles sol/mur + portes. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La taille de la carte (ex. 80x60 tuiles)
- Le nombre de salles (10-15) et leur taille min/max
- La graine aléatoire (reproductible en seed fixe pour debug)

**Méthode** :
1. Seed fixe pour debug, aléatoire sinon (Random with seed).
2. Placer les salles : position/taille aléatoires, rejeter si chevauchement + marge 1 tuile.
3. Connecter : trier salles par x, lier chaque salle au centre de la précédente (corridor L : horizontal puis vertical, largeur 2-3).
4. Instancier : murs autour des salles, sol à l'intérieur, portes aux extrémités de corridors.
5. Placer le joueur (salle 1), la sortie/boss (dernière salle), ennemis et loot (1528).

**Sorties attendues** :
- Le donjon généré (salles + corridors) jouable
- La seed reproductible pour debug
- Le placement joueur/sortie/ennemis/loot

**Exemple de prompt** :
> « Mon roguelike a toujours le même donjon : génère 12 salles aléatoires sans chevauchement + corridors en L (MST simplifié), instancie sur tilemap, seed reproductible. »

**Cas d'usage** : Roguelikes, jeux avec rejouabilité infinie. S'articule avec skills 1512 (tilemap), 1514 (cavernes cellular automata) et 1528 (loot).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

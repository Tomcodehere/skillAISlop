---
num: 1514
nom: "Cavernes par cellular automata (2027)"
emoji: "🏔️"
domaine: "Game Dev"
signal: "Générer des cavernes naturelles en 2027 avec un automate cellulaire : grille remplie à 45 % aléatoirement, 4-5 itérations de lissage (une cellule devient mur si 4+ voisins sont murs), garder la plus grande zone connexe, placer joueur/ennemis dedans. Utilise pour grottes, forêts, donjons organiques. N'utilise pas pour des salles structurées (voir 1513)."
mot_cle: "cellular automata cavernes génération procédurale lissage 45%"
nom_court: "Cavernes CA"
branche: "D1"
synonymes: ["générer une grotte naturelle automate cellulaire", "lissage 4-5 itérations 45% remplissage", "garder la plus grande zone connexe"]
cross_refs: [1513, 1517, 1512]
tags: ["2027"]
depends_on: [1513]
---

## 1514. 🏔️ Cavernes par cellular automata (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Générer des cavernes en 2027 par automate cellulaire : grille 45 % murs aléatoires, 4-5 itérations de lissage (règle 4-5 : mur si 4+ voisins murs), garder uniquement la plus grande zone connexe (flood fill), y placer contenu.

**Quand l'utiliser (triggers)** :
- Générer une grotte qui a l'air naturelle
- Automate cellulaire lissage 45 % → 4 itérations
- Supprimer les petites zones isolées (flood fill)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur procgen. Tu donnes l'algo : init 45 % aléatoire (bordures = murs), itérer 4-5x (nouvelle grille : mur si count voisins murs >= 5, ou 4 avec mur au centre), flood fill pour ne garder que la plus grande région, lisser les bords. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La taille de la carte (ex. 100x60)
- Le taux de remplissage initial (45 %)
- Le nombre d'itérations (4-5)

**Méthode** :
1. Init : chaque cellule mur avec proba 0,45 (bordures toujours murs).
2. Lisser 4-5x : nouvelle valeur = mur si voisins murs >= 5 (ou >=4 et centre mur).
3. Flood fill depuis un point ouvert : marquer la composante connexe; garder la plus grande, remettre le reste en mur.
4. Optionnel : lissage des bords (réduire les pics de 1 tuile).
5. Placer joueur dans la grande zone, ennemis/loot dans les autres zones (1528).

**Sorties attendues** :
- La caverne générée (organique, une grande zone)
- Le code d'automate cellulaire réutilisable
- Le placement contenu dans la zone principale

**Exemple de prompt** :
> « Génère une carte de grotte naturelle pour mon roguelike : automate cellulaire 45 % → 5 itérations de lissage → flood fill, garder la plus grande zone. »

**Cas d'usage** : Grottes, donjons organiques, maps de survie. S'articule avec skills 1513 (salles+corridors), 1517 (Perlin) et 1512 (tilemap).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

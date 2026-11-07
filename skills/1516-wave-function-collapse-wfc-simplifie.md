---
num: 1516
date_ajout: "2026-11"
nom: "Wave Function Collapse (WFC) simplifié"
emoji: "🧩"
domaine: "Game Dev"
signal: "Générer un niveau avec Wave Function Collapse en 2027 (version simplifiée) : chaque cellule a un ensemble de tuiles possibles, on choisit la cellule à plus basse entropie, on propage les contraintes aux voisins (règles de compatibilité), backtrack si contradiction. Utilise pour des niveaux cohérents procéduraux (ville, donjon). N'utilise pas si rooms+corridors (1513) suffit."
mot_cle: "wave function collapse WFC entropie propagation contraintes backtrack"
nom_court: "WFC"
branche: "D1"
synonymes: ["générer niveau WFC wave function collapse", "propagation des contraintes tuiles voisines", "entropie choisir cellule la plus contrainte"]
cross_refs: [1513, 1515, 1512]
tags: ["2027"]
depends_on: [1513]
---

## 1516. 🧩 Wave Function Collapse (WFC) simplifié (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Générer un niveau cohérent par Wave Function Collapse en 2027 (version simple) : grille de cellules avec ensembles de tuiles possibles, choisir la cellule à plus basse entropie, propager les contraintes aux voisins, backtrack si blocage.

**Quand l'utiliser (triggers)** :
- WFC pour générer une ville/donjon procédural
- Entropie : choisir la cellule la plus contrainte d'abord
- Propagation des règles de compatibilité entre tuiles

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur procgen avancé. Tu expliques WFC : chaque cellule = superposition de tuiles possibles; répéter : cellule min entropie → collapse (choisir 1 tuile aléatoire pondérée) → propager contraintes (tuiles compatibles avec chaque voisin selon les règles) → si une cellule vide = contradiction, backtrack. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le tileset + règles de compatibilité (quelles tuiles vont avec quelles voisines)
- La taille de la grille
- La limite de backtracks (ex. 1000)

**Méthode** :
1. Définir les règles : pour chaque tuile, liste des tuiles compatibles au nord/sud/est/ouest.
2. Init : toutes les cellules = toutes les tuiles possibles (entropie max).
3. Boucle : cellule avec entropie min (shannon ou nb options) → collapse (random pondéré).
4. Propager : pour chaque voisin, réduire son ensemble aux tuiles compatibles avec le choix; récursif (queue).
5. Si cellule vide → backtrack (restaurer snapshot) ou restart; limite 1000 itérations.
6. Instancier la tilemap finale (1512).

**Sorties attendues** :
- Le niveau WFC généré et cohérent
- Les règles de compatibilité du tileset
- La limite de backtrack et le résultat

**Exemple de prompt** :
> « Génère une ville 2D procédurale cohérente (routes qui se connectent, maisons alignées) avec WFC simplifié (entropie min, propagation, backtrack 1000). »

**Cas d'usage** : Villes, donjons, tout niveau avec règles de voisinage fortes. S'articule avec skills 1513 (rooms), 1515 (Perlin) et 1512 (tilemap).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

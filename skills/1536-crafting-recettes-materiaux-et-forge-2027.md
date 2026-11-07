---
num: 1536
nom: "Crafting : recettes, materiaux et forge (2027)"
emoji: "🔨"
domaine: "Game Dev"
signal: "Concevoir un système de craft en 2027 : recettes (liste de matériaux + résultat, ex. épée fer = 3 minerais fer + 1 bois), stations (forge, alchimie), qualité de craft (maîtrise du joueur → chance de bonus de stats), démontage d'objets (récupère 50 % matériaux). Utilise pour les jeux avec gathering. N'utilise pas pour un craft instantané sans ressources (voir 1534)."
mot_cle: "crafting recettes matériaux forge maîtrise chance bonus démontage"
nom_court: "Crafting"
branche: "D22"
synonymes: ["recette épée = 3 fer + 1 bois à la forge", "maîtrise craft : chance de +10% stats", "démonter un objet récupère 50% matériaux"]
cross_refs: [1534, 1535, 1529]
tags: ["2027"]
depends_on: [1534]
---

## 1536. 🔨 Crafting : recettes, materiaux et forge (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un craft en 2027 : recettes (matériaux → objet) par station (forge, alchimie), maîtrise du joueur (chance de bonus de stats), démontage (50 % des matériaux récupérés), interface de craft avec aperçu du résultat.

**Quand l'utiliser (triggers)** :
- Crafter une épée en fer à la forge (3 fer + 1 bois)
- Maîtrise 100 : chance de craft avec +10 % stats
- Démonter mon vieil équipement pour récupérer les matériaux

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer craft. Tu définis les recettes (matériaux requis, station, temps, résultat), la maîtrise (0-100, +1 par craft, chance = maîtrise/10 % de bonus), le démontage, et l'UI (liste recettes filtrables, grisée si matériaux insuffisants). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les recettes (matériaux, station, résultat)
- Les matériaux de l'inventaire (1534)
- La maîtrise du joueur par domaine (forge, alchimie)

**Méthode** :
1. Recette {station, matériaux: {fer: 3, bois: 1}, résultat: épée_fer, temps: 5 s}.
2. UI : liste des recettes de la station, grisée si matériaux manquants, aperçu du résultat (stats 1535).
3. Craft : consommer matériaux, attendre temps, produire objet; maîtrise += 1 (max 100).
4. Bonus : rand < maîtrise/1000 → stats x1,1 (affiché 'qualité supérieure !').
5. Démontage : objet → 50 % des matériaux de sa recette (arrondi bas), pas de retour si déjà crafté artisanal.

**Sorties attendues** :
- Le système de craft (recettes + stations) fonctionnel
- La maîtrise et le bonus de qualité
- Le démontage (50 % matériaux)

**Exemple de prompt** :
> « Ajoute le craft : forge (épée fer = 3 minerais fer + 1 bois), alchimie (potion = 2 herbes), maîtrise (chance +10 % stats à 100), démontage 50 %. »

**Cas d'usage** : RPG, survival, MMO. S'articule avec skills 1534 (inventaire), 1535 (stats) et 1529 (économie farm).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

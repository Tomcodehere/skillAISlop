---
num: 1528
date_ajout: "2026-11"
nom: "Loot table ponderee et pity timer"
emoji: "🎰"
domaine: "Game Dev"
signal: "Concevoir une table de loot en 2027 : objets avec poids (commun 60, rare 30, épique 9, légendaire 1), tirage pondéré, pity timer (après 20 monstres sans rare, le taux rare x2, reset au drop), drop garanti tous les 50 (boss 1526). Utilise pour tout système de récompense aléatoire. N'utilise pas pour les récompenses fixes (quêtes 1531)."
mot_cle: "loot table pondérée poids pity timer drop garanti boss"
nom_court: "Loot table"
branche: "D1"
synonymes: ["tirage pondéré commun 60 rare 30 épique 9 légendaire 1", "pity timer après 20 monstres sans rare", "drop garanti tous les 50 monstres"]
cross_refs: [1527, 1529, 1526]
tags: ["2027"]
depends_on: [1527]
---

## 1528. 🎰 Loot table ponderee et pity timer (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir une table de loot en 2027 : objets avec poids (commun 60 / rare 30 / épique 9 / légendaire 1), tirage pondéré à chaque kill, pity timer (taux rare x2 après 20 kills sans rare), drop garanti tous les 50.

**Quand l'utiliser (triggers)** :
- Tirage pondéré : 60/30/9/1 % rareté
- Pity timer : pas de rare depuis 20 monstres → chance x2
- Garanti : un épique minimum tous les 50 kills

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer économie. Tu définis la table (objet, poids, rareté, stats selon rareté), le tirage (rand * sum poids), le compteur pity (incrémente si pas rare+, reset au drop, à 20 → poids rare x2, x3 à 40), et le compteur garanti (tous les 50 → épique forcé). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les objets et leurs poids/raretés
- Le compteur pity (seuil 20)
- Le compteur garanti (tous les 50)

**Méthode** :
1. Table : [{objet: épée_bois, poids: 60, rareté: commun}, ..., {épée_légendaire, poids: 1, rareté: légendaire}].
2. Tirage : total = sum(poids ajustés par pity), rand(0,total), parcourir cumulatif.
3. Pity : pityCounter++ par kill sans rare+; si >= 20, poids rare/épique x2 (x3 à 40), reset au drop rare+.
4. Garanti : tous les 50 kills, forcer un drop épique minimum (reset compteur).
5. Stats de l'objet : base * multiplicateur de rareté (commun x1, légendaire x2,5).

**Sorties attendues** :
- La loot table pondérée + pity + garanti
- Les multiplicateurs de stats par rareté
- Le test : distribution sur 10 000 tirages conforme aux poids

**Exemple de prompt** :
> « Mes joueurs râlent (200 monstres sans rien) : ajoute pity timer (taux rare x2 à 20 kills sans rare, x3 à 40) + drop épique garanti tous les 50 + poids 60/30/9/1. »

**Cas d'usage** : RPG, looter, roguelike. S'articule avec skills 1527 (vagues), 1529 (économie) et 1526 (boss).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

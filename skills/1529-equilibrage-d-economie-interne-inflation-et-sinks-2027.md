---
num: 1529
nom: "Equilibrage d'economie interne : inflation et sinks (2027)"
emoji: "⚖️"
domaine: "Game Dev"
signal: "Équilibrer l'économie d'un jeu en 2027 (complète 1138 sur la modélisation) : sources (monstres, quêtes, farm) vs sinks (réparation, reroll, fast-travel) pour que la monnaie ne s'inflate pas; courbe de farm (combien de gold/heure à chaque niveau); prix des objets scalés par palier. Utilise quand l'économie d'un jeu dérive. N'utilise pas pour la monétisation réelle (1585)."
mot_cle: "équilibrage économie jeu sources sinks inflation courbe farm prix paliers"
nom_court: "Équilibrage éco"
branche: "D21"
synonymes: ["l'or s'inflate dans mon jeu", "sources vs sinks de gold équilibrés", "prix objets scalés par niveau joueur"]
cross_refs: [1138, 1528, 1530]
tags: ["2027"]
depends_on: [1138]
---

## 1529. ⚖️ Equilibrage d'economie interne : inflation et sinks (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Équilibrer l'économie d'un jeu en 2027 : total des sources de gold ≈ total des sinks (sinon inflation), courbe de farm (gold/heure par niveau), prix des objets scalés par palier de progression (x10 tous les 10 niveaux).

**Quand l'utiliser (triggers)** :
- Les joueurs ont 1 M de gold niveau 20, tout coûte 0
- Inflation : trop de sources de gold vs sinks
- Prix de l'épée niveau 30 = x10 niveau 10

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer économie. Tu fais le bilan sources/sinks (tableau), la courbe de farm (gold/heure à chaque tranche de niveau), et les paliers de prix (objet = base * 10^(niveau/10)); règle : sinks doivent absorber 60-80 % des sources. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les sources actuelles (kills, quêtes, farm) et leurs taux
- Les sinks (réparation, reroll, voyage)
- La courbe de progression visée (niveaux)

**Méthode** :
1. Lister les sources : gold par kill/quête/farm par heure à chaque niveau → courbe farm.
2. Lister les sinks : réparation (coût * durabilité), reroll, fast travel, taxes HDV.
3. Vérifier : sum(sinks) entre 60 et 80 % de sum(sources), sinon ajuster (prix sinks up ou sources down).
4. Paliers de prix : prix_objet(niveau n) = base * 10^(n/10), arrondi.
5. Simuler 100 h de jeu (script) : tracer la courbe de richesse joueur, ajuster.

**Sorties attendues** :
- Le bilan sources/sinks équilibré (60-80 %)
- La courbe de farm et les paliers de prix
- La simulation 100 h (courbe de richesse)

**Exemple de prompt** :
> « Mon RPG a une inflation folle (1 M gold niveau 20) : fais le bilan sources/sinks (sinks = 60-80 % des sources), courbe de farm par niveau, paliers de prix x10/10 niveaux. »

**Cas d'usage** : RPG, MMO, tout jeu avec économie interne. S'articule avec skills 1138 (modélisation éco), 1528 (loot) et 1530 (progression).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

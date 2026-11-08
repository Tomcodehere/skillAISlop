---
num: 1525
date_ajout: "2026-11"
nom: "Coordination d'ennemis : flanquement et focus"
emoji: "👥"
domaine: "Game Dev"
signal: "Faire coopérer des ennemis en groupe en 2027 : rôles (tank qui attire l'attention, DPS qui tirent, soigneur), flanquement (un ennemi contourne pendant que l'autre attaque de front), focus fire (tous sur la même cible), communication par 'last seen' partagé (1520). Utilise pour des combats de groupe mémorables. N'utilise pas pour un ennemi seul."
mot_cle: "coordination ennemis flanquement focus fire rôles tank dps soigneur"
nom_court: "Coordination"
branche: "D1"
synonymes: ["ennemis qui flanquent le joueur", "tous attaquent la même cible (focus)", "tank + dps + soigneur rôles"]
cross_refs: [1520, 1526, 1519]
tags: ["2027"]
depends_on: [1519]
---

## 1525. 👥 Coordination d'ennemis : flanquement et focus (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Coordonner un groupe d'ennemis en 2027 : assigner des rôles (tank/dps/soigneur), le tank attire l'attention de front pendant qu'un dps flanque (path vers le côté du joueur), focus fire sur la cible marquée, partage du last_seen.

**Quand l'utiliser (triggers)** :
- 3 ennemis attaquent toujours de front
- Flanquement : un ennemi contourne par la droite
- Focus fire : tous sur la cible marquée

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur IA de groupe. Tu assignes les rôles à l'entrée en combat, le tank va devant (le joueur le cible naturellement), un dps prend un path latéral (1517/1518) pour flanquer, tous partagent last_seen (1520), focus : cible = joueur avec le plus de PV ou marque 'focus'. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le groupe d'ennemis (3-5)
- Les rôles à assigner
- La position du joueur et last_seen partagé

**Méthode** :
1. Assigner rôles : le plus gros = tank (fonce, taunt), les rapides = flankers (path latéral), un = soigneur (reste derrière, heal tank).
2. Tank : se place entre joueur et groupe, le joueur tire dessus naturellement.
3. Flanker : calcule un point à 90° du joueur (droite/gauche alterné), y va (1517), attaque par le côté.
4. Focus : tous attaquent la même cible (joueur focus ou PNJ marqué).
5. Si un meurt : réassigner les rôles (le tank mort → un dps devient tank).

**Sorties attendues** :
- Le groupe coordonné (rôles + flanquement + focus)
- Le partage de last_seen entre ennemis
- La réassignation des rôles si un mort

**Exemple de prompt** :
> « Mes 4 gobelins foncent tous en même temps et meurent un par un : ajoute rôles (tank/dps), flanquement latéral, focus fire sur le joueur marqué. »

**Cas d'usage** : Combats de groupe, boss + adds. S'articule avec skills 1520 (perception), 1526 (boss) et 1519 (FSM).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1535
date_ajout: "2026-11"
nom: "Equipement et stats : armes, armures, rarete"
emoji: "⚔️"
domaine: "Game Dev"
signal: "Concevoir l'équipement en 2027 : slots (arme, armure, casque, bottes, 2 anneaux), chaque objet a des stats (dégâts, défense, PV, crit...) selon sa rareté (commun x1 → légendaire x2,5, 1528), comparaison avec l équipé (tooltip + flèche verte/rouge), niveaux d'objet (upgrade forgeron 1536). Utilise pour tout RPG. N'utilise pas pour un jeu sans équipement."
mot_cle: "équipement slots arme armure stats rareté comparaison équipement actuel"
nom_court: "Équipement"
branche: "D22"
synonymes: ["slots arme armure anneaux", "stats selon rareté x1 à x2,5", "comparer avec l'objet équipé (flèche verte rouge)"]
cross_refs: [1534, 1528, 1536]
tags: ["2027"]
depends_on: [1534]
---

## 1535. ⚔️ Equipement et stats : armes, armures, rarete (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir le système d'équipement en 2027 : slots dédiés (arme, armure, casque, bottes, 2 anneaux), stats par objet scalées selon la rareté (x1 à x2,5), comparaison automatique avec l'équipé actuel (flèches verte/rouge), set bonus.

**Quand l'utiliser (triggers)** :
- Équiper l'épée légendaire trouvée
- Comparer les stats avec l'arme équipée
- Set bonus si 3 objets du même set

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer équipement. Tu définis les slots, les stats par type d'objet, le multiplicateur de rareté, le comparatif d'UI (tooltip côte à côte, flèche ▲▼), les niveaux d'objet (+1..+10 forge), et les set bonus (2/4 pièces). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les slots d'équipement (6)
- Les types d'objets et leurs stats de base
- Les raretés et multiplicateurs (1528)

**Méthode** :
1. Slots : dict {slot: itemId}; équiper = déplacer de l'inventaire (1534) vers le slot, l'ancien retourne en inventaire.
2. Stats finales = base * mult(rareté) * (1 + 0,1*niveau_upgrade), agrégées pour le joueur (dégâts totaux, PV...).
3. Comparatif UI : au survol d'un objet, tooltip de l'équipé à côté avec flèche verte si meilleur, rouge si pire, par stat.
4. Set bonus : si 2/4 pièces d'un set équipées → bonus (ex. +10 % dégâts au 4/4).
5. Persister dans la save (1503).

**Sorties attendues** :
- Les 6 slots d'équipement fonctionnels
- Le comparatif d'UI (flèches par stat)
- Les sets bonus et la save liée

**Exemple de prompt** :
> « Ajoute l'équipement à mon RPG : 6 slots (arme/armure/.../2 anneaux), stats x rareté (légendaire x2,5), comparatif au survol (flèche verte/rouge), set bonus 2/4 pièces. »

**Cas d'usage** : RPG, hack'n'slash. S'articule avec skills 1534 (inventaire), 1528 (rareté loot) et 1536 (craft/upgrade).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

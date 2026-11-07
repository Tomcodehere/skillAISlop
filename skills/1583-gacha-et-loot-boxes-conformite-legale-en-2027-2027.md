---
num: 1583
nom: "Gacha et loot boxes : conformite legale en 2027 (2027)"
emoji: "📦"
domaine: "Game Dev"
signal: "Concevoir des loot boxes/gacha conformes en 2027 : en Belgique/Pays-Bas interdits sans licence; ailleurs : taux affichés obligatoires (probabilités exactes des raretés 1528), pas de 'presque gagné' trompeur, pas de ciblage des mineurs (1587), achats via monnaie virtuelle interdits d'être opaque (prix en € clair), pity (1528) obligatoire. Utilise quand le jeu a du gacha. N'utilise pas pour des IAP directs sans hasard (1585)."
mot_cle: "gacha loot box conformité légale 2027 taux affichés pity Belgique interdit mineurs"
nom_court: "Gacha légal"
branche: "D23"
synonymes: ["taux de drop affichés obligatoires (1528) dans le gacha", "Belgique/Pays-Bas : loot box interdite sans licence 2027", "pas de ciblage des mineurs (1587) par le gacha"]
cross_refs: [1528, 1587, 1582]
tags: ["2027"]
depends_on: [1528]
---

## 1583. 📦 Gacha et loot boxes : conformite legale en 2027 (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre un gacha/loot box conforme en 2027 : taux exacts affichés (1528), pity timer obligatoire, pas de mécaniques trompeuses ('presque gagné'), pas de ciblage des mineurs (1587), prix en € clair, interdiction Belgique/Pays-Bas sans licence — ou éviter le gacha (IAP direct 1585).

**Quand l'utiliser (triggers)** :
- Les taux du gacha doivent être affichés (légal 2027)
- 'Presque gagné' (near-miss) = pratique trompeuse interdite
- Gacha interdit en Belgique/Pays-Bas sans licence

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es juriste game économie. Tu rappelles la loi 2027 : proba exactes affichées, pity (1528), pas de near-miss, mineurs exclus (1587), monnaie virtuelle avec taux de change affiché en €, licence requise BE/NL, sinon retrait du marché; alternative : IAP direct sans hasard (1585). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le système de gacha (banner, taux 1528, pity)
- Les pays de sortie (BE/NL = licence ou retrait)
- L'âge des joueurs (1587)

**Méthode** :
1. Afficher les taux exacts de chaque rareté dans le jeu (légal obligatoire 2027) + historique des tirages.
2. Pity obligatoire (1528) affiché; pas de near-miss (ne pas montrer 'presque' le légendaire).
3. Mineurs (1587) : pas de gacha du tout pour eux (vérification âge), ou désactivé par défaut.
4. Monnaie virtuelle : taux de change affiché en € à côté (ex. 100 gemmes = 0,99 €), pas de 'pack' avantage trompeur.
5. BE/NL : licence de jeu de hasard requise, sinon retirer les loot boxes du marché (cosmétiques directs 1585).
6. Log de tous les tirages (audit) + possibilité de conversion en IAP direct.

**Sorties attendues** :
- Le gacha conforme (taux affichés, pity, pas de near-miss, mineurs exclus) ou retiré BE/NL
- L'alternative IAP direct (1585) proposée
- Le log d'audit des tirages

**Exemple de prompt** :
> « Mon gacha de skins : affiche les taux exacts (légal 2027), ajoute le pity (1528), retire les near-miss, bloque les -18 ans (1587), et retire les loot boxes en Belgique/Pays-Bas (pas de licence) — ou passe en IAP direct (1585). »

**Cas d'usage** : Jeux F2P avec hasard payant. S'articule avec skills 1528 (pity), 1587 (mineurs) et 1582 (éthique).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

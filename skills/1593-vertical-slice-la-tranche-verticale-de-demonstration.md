---
num: 1593
resume: "Construire un vertical slice en 2027 : 1 niveau/zone complet et poli (graphismes, sons 1566, UI 1570, tutoriel 1572) montrant le loop final (jouer → combattre 1526 → récompense 1528 → progresser 1530), pour pitcher (1594) ou financer (1595). Étape 1 : Choisir la zone la plus représentative (mécaniques clés : déplacement 1511, combat 1526, récompense 1528)."
lang: "fr"
date_ajout: "2026-11"
nom: "Vertical slice : la tranche verticale de démonstration"
emoji: "🥧"
domaine: "Game Dev"
signal: "Construire un vertical slice en 2027 : 1 niveau complet et poli (pas tout le jeu) montrant le gameplay loop final (exploration → combat 1526 → récompense 1528 → progression 1530), avec graphismes/audio/UI finaux (1570), pour convaincre un éditeur (1594) ou financer (1595). Durée : 2-4 mois. N'utilise pas pour le jeu complet (scope)."
mot_cle: "vertical slice 1 niveau poli complet loop final démo éditeur pitch"
nom_court: "Vertical slice"
branche: "D10"
synonymes: ["1 niveau final poli pour montrer le jeu (pas un prototype gris)", "le loop complet : exploration → combat → loot → progression", "convaincre un éditeur (1594) avec le vertical slice"]
cross_refs: [1594, 1595, 1526]
tags: ["2027"]
depends_on: [1594]
---

## 1593. 🥧 Vertical slice : la tranche verticale de démonstration (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire un vertical slice en 2027 : 1 niveau/zone complet et poli (graphismes, sons 1566, UI 1570, tutoriel 1572) montrant le loop final (jouer → combattre 1526 → récompense 1528 → progresser 1530), pour pitcher (1594) ou financer (1595).

**Quand l'utiliser (triggers)** :
- Un éditeur veut voir 'une tranche' du jeu final (1594)
- 1 niveau gris avec le vrai gameplay suffit ? Non : poli (art/son/UI)
- Le loop complet visible en 5 min de démo

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game director. Tu définis le périmètre : 1 zone jouable de 10-15 min, qualité finale partout (pas de placeholder), le loop complet (input 1504 → combat 1526 → loot 1528 → XP 1530 → déblocage 1537), tutoriel (1572), et ce qui n'est PAS dans le slice (liste honnête). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le GDD (1593... non 1596?) — le concept du jeu
- L'équipe (2-6 personnes)
- Le délai (2-4 mois) et la cible (éditeur 1594 / crowdfunding 1595)

**Méthode** :
1. Choisir la zone la plus représentative (mécaniques clés : déplacement 1511, combat 1526, récompense 1528).
2. Produire en qualité finale : art (sprites 1554, éclairage 1556), sons (1566-1569), UI (1570), tutoriel (1572), 1 boss (1526).
3. Loop complet en 5-10 min de démo jouable de bout en bout.
4. Ce qui manque est listé honnêtement ('pas encore : 20 niveaux, 5 classes...').
5. Démo filmée 3 min + build jouable pour l'éditeur (1594) / page crowdfunding (1595).

**Sorties attendues** :
- Le vertical slice (1 zone polie, loop complet) jouable
- La démo vidéo 3 min + build pour l'éditeur
- La liste honnête de ce qui n'est pas dedans

**Exemple de prompt** :
> « Prépare le pitch éditeur (1594) : fais un vertical slice (1 donjon 10 min, qualité finale art/son/UI, loop complet combat 1526 → loot 1528 → XP 1530, boss), démo filmée 3 min + build jouable. »

**Cas d'usage** : Levée de fonds, éditeur, crowdfunding. S'articule avec skills 1594 (pitch), 1595 (budget) et 1526 (boss).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

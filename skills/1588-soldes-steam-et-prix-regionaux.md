---
num: 1588
resume: "Stratégie de soldes et prix régionaux en 2027 : participer aux 4 soldes Steam annuels (-30 à -50 %), respecter les règles (pas de solde inférieur à 30 j après sortie, cooldown 30 j), et fixer des prix localisés (Steam regional pricing, -30 à -70 % selon le pays). Étape 1 : Choisir le prix de base US (19,99 $) puis laisser Steam suggérer les prix régionaux (ou ajuster : Inde/Brésil/Turquie -60 à -7"
lang: "fr"
date_ajout: "2026-11"
nom: "Soldes Steam et prix regionaux"
emoji: "💷"
domaine: "Game Dev"
signal: "Gérer les soldes et le prix régional d'un jeu PC en 2027 : soldes Steam saisonniers (Spring/Summer/Autumn/Winter, -30 à -50 % sur un jeu bien noté 1589), règles (pas de solde sous 30 jours après sortie, cooldown 30 j entre soldes), prix localisés par région (Steam recommande -30 à -70 % selon pouvoir d'achat : Inde, Brésil, Turquie...), personnages regional pricing. Utilise pour la stratégie de revenus. N'utilise pas pour le mobile (1582)."
mot_cle: "soldes Steam saisonniers prix régionaux localisés -50 % Inde Brésil Turquie"
nom_court: "Soldes/prix"
branche: "D21"
synonymes: ["soldes Steam printemps été automne hiver -50%", "prix régional Steam : -70% en Inde Turquie Brésil", "pas de solde dans les 30 jours après la sortie"]
cross_refs: [1581, 1589, 1582]
tags: ["2027"]
depends_on: [1581]
---

## 1588. 💷 Soldes Steam et prix regionaux (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Stratégie de soldes et prix régionaux en 2027 : participer aux 4 soldes Steam annuels (-30 à -50 %), respecter les règles (pas de solde < 30 j après sortie, cooldown 30 j), et fixer des prix localisés (Steam regional pricing, -30 à -70 % selon le pays).

**Quand l'utiliser (triggers)** :
- Participer au Summer Sale Steam (-50 %)
- Prix régional : -70 % en Inde, Turquie, Brésil (Steam)
- Règle Steam : pas de solde 30 j après la sortie

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable revenus PC. Tu expliques les 4 soldes annuels Steam, les règles (cooldown, % max), et le regional pricing (Steam suggère des ratios selon le PIB/habit : Inde ~-70 %, UE ~-10-20 %, US prix plein), avec l'outil Steam de suggestion de prix. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le prix de base (ex. 19,99 €)
- Les régions cibles et le pouvoir d'achat
- Le calendrier des soldes Steam 2027

**Méthode** :
1. Choisir le prix de base US (19,99 $) puis laisser Steam suggérer les prix régionaux (ou ajuster : Inde/Brésil/Turquie -60 à -75 %, Japon -10 %, UE proche du US).
2. Soldes : s'inscrire aux 4 sales annuels (Spring/Summer/Autumn/Winter) avec -30 à -50 % (jeu bien noté 1589 = plus de visibilité).
3. Règles : pas de changement de prix/solde dans les 30 j suivant un changement; cooldown 30 j entre deux soldes; pas de solde dans les 30 j après la sortie.
4. Événements perso : soldes anniversaire du jeu (1578) hors calendrier Steam, -20 % max.
5. Suivre revenus par région (Steamworks 1580) et ajuster les prix (certains pays convertissent mieux en low price).

**Sorties attendues** :
- Les prix régionaux configurés (Steam suggested)
- Le calendrier des soldes 2027 avec remises prévues
- Les règles Steam respectées (cooldown 30 j)

**Exemple de prompt** :
> « Le jeu sort à 19,99 € : configure les prix régionaux Steam (Inde -70 %, Brésil -65 %, Japon -10 %, UE ~17 €), inscris-toi au Summer Sale (-40 %), respecte le cooldown 30 j. »

**Cas d'usage** : Revenus PC. S'articule avec skills 1581 (store), 1589 (avis) et 1582 (mobile).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

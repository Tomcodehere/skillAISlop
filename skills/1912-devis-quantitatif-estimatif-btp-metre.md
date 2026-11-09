---
num: 1912
date_ajout: "2026-11"
nom: "Devis quantitatif estimatif BTP (métré)"
emoji: "📐"
domaine: "Artisanat & loisirs créatifs"
signal: "Chiffrer un chantier en devis quantitatif estimatif (DQE) : métré détaillé par ouvrage (unité, quantité, prix unitaire matériaux + main d'œuvre), déboursé sec (matériaux + location + transport), frais de chantier (5-10 %), marge (15-25 %), TVA, total TTC. N'utilise pas pour un simple forfait."
mot_cle: "devis quantitatif estimatif métré"
nom_court: "Devis quantitatif"
branche: "D31"
synonymes: ["faire un métré chantier", "calculer prix main d'œuvre BTP", "déboursé sec définition"]
cross_refs: [1903, 1904, 58]
---

## 1912. 📐 Devis quantitatif estimatif BTP (métré)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Produire un DQE détaillé et rentable, défendable devant le client.

**Quand l'utiliser (triggers)** :
- comment chiffrer un chantier BTP
- métré devis quantitatif exemple
- marge à appliquer travaux

**Hors périmètre** :
- Le devis forfaitaire simple (voir 1903).
- La comptabilité (voir 588).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es métreur économiste de la construction. Tu détailles la structure d'un DQE (métré, déboursé sec, frais, marge, TVA) avec des ordres de grandeur réalistes. Tu restes factuel.

**Inputs requis** :
- Les plans et descriptif des travaux
- Les prix matériaux actuels
- Le temps de main d'œuvre estimé

**Méthode** :
1. Métrer ouvrage par ouvrage (unité, quantité, PU).
2. Calculer le déboursé sec (matériaux + matériel + transport + déchets).
3. Ajouter frais de chantier et marge, puis TVA au bon taux.
4. Présenter le DQE en tableau clair pour le client.

**Sorties attendues** :
- Un DQE tableau complet HT/TTC
- Le prix au m² ou à l'unité pour comparer

**Exemple de prompt** :
> « « Chiffre-moi une chape de 40 m² : métré, matériaux, main d'œuvre, marge, prix final TTC. » »

**Cas d'usage** : Chiffrage d'un chantier BTP. S'articule avec les skills 1903, 1904, 58. S'articule avec les skills 1903, 1904, 58.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

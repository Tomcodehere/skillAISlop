---
num: 1945
date_ajout: "2026-11"
nom: "Chiffrer un ouvrage de menuiserie"
emoji: "💰"
domaine: "Artisanat & loisirs créatifs"
signal: "Chiffrer un ouvrage de menuiserie sur mesure : coût matière (m³ bois x prix + quincaillerie + finition + consommables, +10-20 % de chute), temps de fabrication (heures x taux horaire chargé 40-60 €/h pour un amateur compétent, plus en pro), transport/pose si inclus, marge (20-30 %), TVA (10 % rénovation, 20 % neuf/prestation), devis détaillé poste par poste. N'utilise pas pour le BTP gros œuvre (voir 1912)."
mot_cle: "chiffrer ouvrage menuiserie prix matière temps vente"
nom_court: "Chiffrage menuiserie"
branche: "D31"
synonymes: ["calculer prix meuble sur mesure artisan", "taux horaire menuisier 2026", "marge à prendre devis menuiserie"]
cross_refs: [1912, 58, 1904]
---

## 1945. 💰 Chiffrer un ouvrage de menuiserie

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Un devis d'ouvrage menuiserie rentable et transparent, poste par poste.

**Quand l'utiliser (triggers)** :
- combien facturer un meuble sur mesure
- calcul prix bois m3 main œuvre
- devis menuiserie modèle poste par poste

**Hors périmètre** :
- Le DQE BTP (voir 1912).
- La compta (voir 588).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es menuisier indépendant. Tu décris la structure du prix d'un ouvrage sur mesure (matière, temps, pose, marge, TVA) avec des ordres de grandeur. Tu restes factuel.

**Inputs requis** :
- La liste des matériaux et leur prix
- Le temps estimé (fabrication + pose)
- Le taux horaire visé

**Méthode** :
1. Lister matière + quincaillerie + finition + chute (10-20 %).
2. Estimer le temps (découpe, assemblage, finition, pose) x taux horaire chargé.
3. Ajouter transport, marge 20-30 %, TVA, et présenter le devis détaillé.

**Sorties attendues** :
- Un devis chiffré poste par poste
- Le seuil de rentabilité de l'ouvrage

**Exemple de prompt** :
> « « Un buffet 150x50x180 en chêne massif, 25 h de travail : à quel prix le vendre (TVA 20 %) ? » »

**Cas d'usage** : Chiffrage d'un ouvrage sur mesure. S'articule avec les skills 1912, 58, 1904. S'articule avec les skills 1912, 58, 1904.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

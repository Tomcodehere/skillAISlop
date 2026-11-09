---
num: 1902
resume: "Avoir la liste à jour des obligations légales de l'artisan BTP et les appliquer sur chaque document commercial. Étape 1 : Lister les obligations : décennale, RC Pro, RNE, TVA, facture électronique, mentions devis/facture."
lang: "fr"
date_ajout: "2026-11"
nom: "Obligations légales de l'artisan BTP"
emoji: "📋"
domaine: "Artisanat & loisirs créatifs"
signal: "Connaître et appliquer les obligations légales de l'artisan du bâtiment : assurance décennale obligatoire (loi Spinetta, art. L241-1) avant le 1er chantier, immatriculation RNE obligatoire (amende 15 000 € sinon), facture électronique progressive (généralisation 2026-2027), mentions obligatoires sur devis et factures (SIRET, décennale, TVA, délais d'exécution, rétractation). Utilise quand on édite un devis/facture ou qu'on démarre. N'utilise pas pour le droit du travail (voir 555)."
mot_cle: "obligations légales artisan BTP"
nom_court: "Obligations légales BTP"
branche: "D31"
synonymes: ["obligations légales artisan", "checklist conformité BTP", "amende RNE 15 000"]
cross_refs: [1903, 1904, 1907]
---

## 1902. 📋 Obligations légales de l'artisan BTP

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Avoir la liste à jour des obligations légales de l'artisan BTP et les appliquer sur chaque document commercial.

**Quand l'utiliser (triggers)** :
- checklist obligations légales artisan BTP
- facture électronique obligatoire quand
- amende si pas immatriculé RNE

**Hors périmètre** :
- Les règles de sécurité du chantier (voir 1908/1909).
- Le droit du travail et les salariés (voir skill 555).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es juriste spécialisé droit de la construction. Tu cites les textes (art. L241-1 loi Spinetta, Code de commerce) et les montants d'amendes, et tu distingues devis/facture/mentions. Tu restes factuel.

**Inputs requis** :
- Le type de document édité (devis, facture, avenant)
- Le corps de métier
- La date de début d'activité

**Méthode** :
1. Lister les obligations : décennale, RC Pro, RNE, TVA, facture électronique, mentions devis/facture.
2. Vérifier chaque document émis contre la checklist (SIRET, n° décennale, taux TVA, délais, rétractation 14 j).
3. Mettre un rappel de mise à jour annuelle (calendrier facture électronique).

**Sorties attendues** :
- Une checklist conformité à cocher par chantier
- Les mentions exactes à recopier sur devis et factures

**Exemple de prompt** :
> « « Mon devis est-il conforme pour un chantier de salle de bain ? Quelles mentions obligatoires, quelle assurance dois-je citer ? » »

**Cas d'usage** : Conformité commerciale d'un artisan BTP. S'articule avec les skills 1903, 1904, 1907. S'articule avec les skills 1903, 1904, 1907.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

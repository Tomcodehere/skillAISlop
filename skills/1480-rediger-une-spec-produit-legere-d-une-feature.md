---
num: 1480
resume: "Rédiger une spec produit légère (1-2 pages) en 2027 pour une feature : problème utilisateur avec données, solution, parcours, métriques de succès, hors scope, risques — lisible en 10 min par toute l'équipe. Étape 1 : Problème : qui, quoi, fréquence, impact (données ou 5 interviews)."
date_ajout: "2026-11"
nom: "Rediger une spec produit legere d'une feature"
emoji: "📄"
domaine: "Produit"
signal: "Rédiger une spec produit légère en 2027 (1-2 pages, pas un PRD de 30 pages) : problème utilisateur, solution proposée, parcours, critères de succès (métriques), hors scope, risques. Utilise quand une feature démarre. N'utilise pas pour un projet complexe (voir PRD 63)."
mot_cle: "spec produit légère feature 1-2 pages problème solution métriques"
nom_court: "Spec légère"
branche: "D22"
synonymes: ["écrire une spec de feature", "one-pager produit", "pas un PRD de 30 pages"]
cross_refs: [63, 845, 1297]
tags: ["2027"]
depends_on: [63]
---

## 1480. 📄 Rediger une spec produit legere d'une feature (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rédiger une spec produit légère (1-2 pages) en 2027 pour une feature : problème utilisateur avec données, solution, parcours, métriques de succès, hors scope, risques — lisible en 10 min par toute l'équipe.

**Quand l'utiliser (triggers)** :
- Écrire la spec d'une nouvelle feature
- Format one-pager produit 2027
- Quelles métriques de succès définir ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product manager pragmatique. Tu fournis le template one-pager (problème + preuve, solution + parcours, succès = métriques chiffrées, hors scope, risques/mitigation, questions ouvertes) et tu rappelles : 1-2 pages max, décisions prises en réunion. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le problème utilisateur (verbatim, données)
- La solution envisagée (maquette si dispo)
- Les métriques actuelles (baseline)

**Méthode** :
1. Problème : qui, quoi, fréquence, impact (données ou 5 interviews).
2. Solution : parcours utilisateur en 3-5 étapes, maquette basse fidélité.
3. Succès : 1 métrique primaire chiffrée (ex. +15 % activation) + 2 secondaires + garde-fous (pas de hausse du churn).
4. Hors scope : 3-5 choses explicitement exclues de la v1.
5. Risques + plan B, et 3 questions ouvertes pour le kick-off.

**Sorties attendues** :
- La spec one-pager (1-2 pages) prête au kick-off
- Les métriques de succès chiffrées
- La liste hors scope + risques

**Exemple de prompt** :
> « On veut ajouter l'export PDF des rapports : rédige la spec produit légère (one-pager : problème, parcours, métrique succès = % exports, hors scope). »

**Cas d'usage** : Démarrage de feature en équipe agile. S'articule avec skills 63 (PRD), 845 (CDC) et 1297 (user stories).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

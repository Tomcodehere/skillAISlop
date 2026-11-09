---
num: 1861
resume: "Adopter FOCUS (standard FinOps Foundation) pour normaliser les coûts cloud multi-fournisseurs (65 colonnes, EffectiveCost vs BilledCost) via les exports natifs AWS/Azure/GCP — une requête SQL uniforme. Étape 1 : Activer les exports FOCUS natifs : AWS Data Exports, Azure Cost Management FOCUS dataset, GCP BigQuery view/export, OCI."
lang: "fr"
date_ajout: "2026-11"
nom: "FOCUS : standard ouvert des coûts cloud multi-fournisseurs"
emoji: "💰"
domaine: "Gestion"
signal: "Utiliser FOCUS (FinOps Open Cost & Usage Specification, FinOps Foundation/Linux Foundation) pour lire les factures cloud de façon standardisée : 65 colonnes normalisées (v1.2), EffectiveCost (analyse) vs BilledCost (facture), exports natifs AWS (Data Exports, GA nov.), Azure (Cost Management), GCP (BigQuery), OCI... FOCUS 1.4 ratifié le 4 juin, FOCUS 1.5 (tokens IA) prévu fin d'année. Une requête SQL marche sur tous les clouds. N'utilise pas les formats propriétaires (CUR AWS seul) pour du multi-cloud."
mot_cle: "FOCUS FinOps Open Cost Usage Specification standard factures cloud 65 colonnes EffectiveCost BilledCost multi-cloud AWS Azure GCP exports natifs 1.4"
nom_court: "FOCUS FinOps"
branche: "D25"
synonymes: ["lire la facture AWS et Azure avec la même requête SQL (FOCUS, 65 colonnes standardisées)", "EffectiveCost pour l'analyse vs BilledCost pour la réconciliation facture", "exports FOCUS natifs : AWS Data Exports, Azure Cost Management, GCP BigQuery"]
cross_refs: [1862, 1870, 1800]
tags: ["2027"]
---

## 1861. 💰 FOCUS : standard ouvert des coûts cloud multi-fournisseurs

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Adopter FOCUS (standard FinOps Foundation) pour normaliser les coûts cloud multi-fournisseurs (65 colonnes, EffectiveCost vs BilledCost) via les exports natifs AWS/Azure/GCP — une requête SQL uniforme.

**Quand l'utiliser (triggers)** :
- comparer AWS vs Azure vs GCP sans ETL custom : FOCUS
- EffectiveCost (après remises) vs BilledCost (facture) : lequel pour le budget ?
- FOCUS 1.5 : les tokens IA normalisés (prévu fin d'année)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es FinOps / contrôleur de gestion IT. Tu actives les exports FOCUS natifs chez chaque cloud, tu les lands dans un warehouse commun, et tu requêtes en EffectiveCost pour l'analyse, BilledCost pour la réconciliation. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les comptes cloud (AWS/Azure/GCP/OCI)
- Le warehouse cible (BigQuery/Snowflake/duckdb)
- Les besoins (showback 1870)

**Méthode** :
1. Activer les exports FOCUS natifs : AWS Data Exports, Azure Cost Management FOCUS dataset, GCP BigQuery view/export, OCI.
2. Tout lander dans un seul schéma FOCUS (mêmes colonnes) — plus de mapping par provider.
3. Analyser en EffectiveCost (après commitments/remises), réconcilier la facture en BilledCost.
4. Tagger (ChargeCategory, tags) pour l'allocation par équipe/produit (1870).
5. FOCUS 1.5 : préparer l'arrivée des coûts tokens IA (1800 gateway).

**Sorties attendues** :
- Les exports FOCUS actifs chez tous les clouds
- Le warehouse FOCUS requêtable uniformément
- Le dashboard coût multi-cloud (1766)

**Exemple de prompt** :
> « 3 clouds : exports FOCUS -> BigQuery, une requête SELECT ServiceCategory, SUM(EffectiveCost) GROUP BY 1 marche sur AWS+Azure+GCP sans transformation — le CFO voit le coût total 2027 en un chiffre. »

**Cas d'usage** : FinOps multi-cloud. S'articule avec skills 1862 (coût k8s), 1870 (chargeback), 1800 (coût IA).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

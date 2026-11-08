---
num: 1463
date_ajout: "2026-11"
nom: "Warehouse vs data lake vs lakehouse"
emoji: "🏔️"
domaine: "Data"
signal: "Choisir l'architecture de stockage data en 2027 : data warehouse (Snowflake/BigQuery/Redshift : SQL, structuré, cher), data lake (S3/ADLS brut : pas cher, flexible, risque 'marécage'), lakehouse (Databricks/Delta Lake/Iceberg : le meilleur des deux, ACID, time travel). Utilise quand on (re)construit la plateforme data. N'utilise pas pour une petite BDD applicative."
mot_cle: "data warehouse lake lakehouse delta iceberg choisir 2027"
nom_court: "Archi data"
branche: "D15"
synonymes: ["snowflake ou databricks 2027", "delta lake iceberg lakehouse", "éviter le data swamp"]
cross_refs: [1098, 94, 350]
tags: ["2027"]
depends_on: [350]
---

## 1463. 🏔️ Warehouse vs data lake vs lakehouse (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir l'architecture data en 2027 (warehouse vs lake vs lakehouse) selon les besoins : warehouse pour le BI structuré, lake pour le brut pas cher, lakehouse (Delta/Iceberg) pour ACID + time travel + ML et BI réunis.

**Quand l'utiliser (triggers)** :
- Snowflake nous coûte une fortune
- Lakehouse Databricks vs warehouse BigQuery
- Éviter que notre lake devienne un marécage

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de plateforme data. Tu compares les 3 architectures (coût, gouvernance, ACID, ML vs BI, compétences équipe) et tu proposes souvent : lakehouse (Delta Lake/Iceberg sur S3) comme compromis 2027 pour la plupart des PME/ETI. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les cas d'usage (BI, ML, streaming, brut)
- Le volume et la variété des données
- Le budget et l'équipe (SQL vs Spark)

**Méthode** :
1. Lister les besoins : BI structuré, ML, data science, ingestion brute, gouvernance.
2. Comparer : warehouse (SQL pur, coût requête), lake (S3 brut, gouvernance faible), lakehouse (ACID, schéma, time travel, ML+BI).
3. Choisir selon le mix : 100 % BI → warehouse ; mixte ML+BI+gouvernance → lakehouse.
4. POC sur un cas réel (ingestion + requête + ML) avant décision.
5. Planifier la migration (dbt 350, ETL 94) et la gouvernance (catalogue 1095).

**Sorties attendues** :
- L'architecture retenue et justifiée
- Le POC et ses résultats
- Le plan de migration et gouvernance

**Exemple de prompt** :
> « On a un lake S3 devenu un marécage + des coûts Snowflake qui explosent : évalue le lakehouse (Delta Lake/Iceberg) comme architecture 2027. »

**Cas d'usage** : Plateforme data d'entreprise, modernisation. S'articule avec skills 1098 (data lake), 94 (pipelines) et 350 (dbt).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

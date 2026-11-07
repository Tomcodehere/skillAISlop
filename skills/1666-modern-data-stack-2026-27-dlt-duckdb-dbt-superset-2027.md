---
num: 1666
date_ajout: "2026-11"
nom: "Modern data stack 2026-27 : dlt + DuckDB + dbt + Superset (2027)"
emoji: "🧱"
domaine: "Data"
signal: "Monter un modern data stack léger en 2027 sans infra lourde : dlt (ingestion 1664) + DuckDB (1660, stockage local/cloud MotherDuck 1661) + dbt (transformations SQL 350) + Apache Superset (BI 107) — pour une PME/équipe data. Alternative : stack cloud (BigQuery/Snowflake 1463). N'utilise pas si sup. à  100 utilisateurs concurrents ou téraoctets (warehouse cloud)."
mot_cle: "modern data stack 2027 dlt duckdb dbt superset stack léger PME sans infra lourde"
nom_court: "Modern stack"
branche: "D15"
synonymes: ["stack data PME sans infra : dlt + DuckDB + dbt + Superset", "Superset open source pour le BI (107)", "dbt pour les transformations SQL versionnées (350)"]
cross_refs: [1664, 1660, 350]
tags: ["2027"]
depends_on: [1664]
---

## 1666. 🧱 Modern data stack 2026-27 : dlt + DuckDB + dbt + Superset (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Monter un modern data stack léger en 2027 : dlt (1664) pour ingérer, DuckDB/MotherDuck (1660/1661) pour stocker, dbt (350) pour transformer en SQL versionné, Apache Superset (107) pour le BI — sans infrastructure lourde, pour PME/équipe data.

**Quand l'utiliser (triggers)** :
- on veut de l'analytics sans recruter un admin DBA
- dlt → DuckDB → dbt → Superset en 2027
- quand passer au warehouse cloud (BigQuery/Snowflake 1463)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data platform engineer. Tu assembles : dlt ingère (API/SaaS/BDD) → DuckDB (local ou MotherDuck cloud 1661), dbt transforme (models SQL, tests 349, doc auto 1406), Superset fait les dashboards (107), le tout versionné Git + CI (1592). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les sources de données (SaaS, BDD, fichiers)
- L'équipe (2-5 data persons)
- Le volume (jusqu'à quelques centaines de Go)

**Méthode** :
1. dlt (1664) : pipelines d'ingestion vers DuckDB/MotherDuck (1661), incremental, schéma auto (1461).
2. dbt (350) : models SQL dans un repo Git, tests de données (349), doc auto (1406), run en CI (1592) ou orchestrateur (1460).
3. DuckDB/MotherDuck (1660/1661) : stockage, requêtes analytiques rapides, partage équipe.
4. Superset (107) : connexion à DuckDB, dashboards (KPIs 36), alertes (1417), droits par équipe.
5. Seuils de passage au warehouse cloud (1463) : volume > 1 To, > 100 users concurrents, besoins ML lourds.

**Sorties attendues** :
- Le stack dlt+DuckDB+dbt+Superset déployé et documenté
- Les dashboards Superset (KPIs) en ligne
- Les seuils de migration vers le warehouse cloud (1463)

**Exemple de prompt** :
> « Monter l'analytics de la PME sans admin DBA : stack dlt (ingestion API CRM) → MotherDuck (1661) → dbt (transformations testées 349) → Superset (dashboards ventes 107), Git + CI (1592), seuils de passage à BigQuery (1463) documentés. »

**Cas d'usage** : PME, équipe data 2-5 pers, budget serré. S'articule avec skills 1664 (dlt), 1660/1661 (DuckDB/MotherDuck), 350 (dbt), 107 (dashboards) et 1463 (warehouse).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1663
date_ajout: "2026-11"
nom: "Delta Lake vs Iceberg vs Hudi : choisir son open table format"
emoji: "⚖️"
domaine: "Data"
signal: "Choisir son format de table ouvert (open table format) en 2027 pour un lakehouse (1463) : Delta Lake (Databricks, mature, VACUUM/OPTIMIZE), Apache Iceberg (v3 1662, multi-moteurs, hidden partitioning, row lineage), Apache Hudi (upserts fréquents, streaming). Critères : moteur principal, streaming vs batch, conformité. N'utilise pas pour un warehouse propriétaire (Snowflake/BigQuery gèrent en interne)."
mot_cle: "choisir open table format 2027 Delta Lake vs Apache Iceberg vs Hudi lakehouse"
nom_court: "Delta/Iceberg"
branche: "D15"
synonymes: ["Delta Lake vs Iceberg vs Hudi en 2027", "Iceberg multi-moteurs (Spark Trino DuckDB Snowflake)", "Delta Lake si écosystème Databricks dominant"]
cross_refs: [1662, 1664, 1463]
tags: ["2027"]
depends_on: [1463]
---

## 1663. ⚖️ Delta Lake vs Iceberg vs Hudi : choisir son open table format (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir son open table format en 2027 (Delta Lake vs Iceberg vs Hudi) selon le moteur principal, le mode (batch vs streaming/upserts), la conformité (1662), et l'écosystème — avec un POC sur les requêtes réelles.

**Quand l'utiliser (triggers)** :
- on démarre un lakehouse : quel format de table ouvert ?
- Iceberg multi-moteurs vs Delta lié à Databricks
- Hudi pour les upserts fréquents (CDC)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte data platform. Tu compares : Delta (Databricks, mature, VACUUM, time travel), Iceberg (ouvert, multi-moteurs, v3 lineage 1662, hidden partitioning), Hudi (upserts/CDC streaming). Règle : écosystème Databricks → Delta ; multi-moteurs/compliance → Iceberg ; streaming fréquent → Hudi. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le moteur principal (Databricks, Spark, Trino, Snowflake)
- Le mode (batch nightly vs streaming/upserts)
- Les besoins conformité (1662)

**Méthode** :
1. Lister les besoins : moteurs utilisés, batch vs streaming, upserts fréquents (CDC), conformité RGPD (effacement 1662).
2. Delta Lake : si stack Databricks (intégration native, Delta Live Tables, Unity Catalog 1095).
3. Iceberg : si multi-moteurs (Spark+Trino+DuckDB+Snowflake lisent la même table) et besoin de v3 (1662).
4. Hudi : si upserts fréquents (CDC depuis Kafka 1464), record-level lineage.
5. POC : même dataset en 2 formats, benchmark (requête, ingestion, coût stockage), choisir.

**Sorties attendues** :
- Le format choisi + POC benchmarké (requête/ingestion/coût)
- La table ouverte lisible par tous les moteurs choisis
- La doc de la décision (ADR 88)

**Exemple de prompt** :
> « On construit un lakehouse lisible par Spark, Trino, DuckDB et Snowflake avec besoin d'effacement RGPD : choisis Iceberg v3 (1662) plutôt que Delta (lié Databricks) — POC benchmark des 3 formats d'abord. »

**Cas d'usage** : Nouveau lakehouse. S'articule avec skills 1662 (Iceberg v3), 1664 (archi lakehouse 1463), 1460 (orchestration).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

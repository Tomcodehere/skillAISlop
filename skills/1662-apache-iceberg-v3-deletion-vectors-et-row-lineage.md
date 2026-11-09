---
num: 1662
resume: "Adopter Apache Iceberg v3 en 2027 (deletion vectors pour les suppressions efficaces + conformité effacement RGPD 189, row lineage pour la traçabilité ligne par ligne) dans un lakehouse ouvert (1463), avec support Snowflake/Databricks/Spark/DuckDB (1660). Étape 1 : Migrer la table en v3 (format_version=3, migration progressive, compatibilité v2 maintenue)."
lang: "fr"
date_ajout: "2026-11"
nom: "Apache Iceberg v3 : deletion vectors et row lineage"
emoji: "🧊"
domaine: "Data"
signal: "Utiliser Apache Iceberg v3 en 2027 (approuvé 2025, dispo Snowflake mai 2026) : deletion vectors (suppressions efficaces, conformité RGPD 189 effacement), row lineage (traçabilité ligne par ligne, aligné Delta Lake), spécification ouverte. Utilise pour les lakehouses (1463). N'utilise pas pour de petites tables (overhead)."
mot_cle: "Apache Iceberg v3 2027 deletion vectors row lineage GDPR effacement lakehouse ouvert"
nom_court: "Iceberg v3"
branche: "D15"
synonymes: ["Iceberg v3 : suppressions efficaces (deletion vectors)", "row lineage : traçabilité de chaque ligne (audit, RGPD)", "format ouvert Iceberg vs Delta vs Hudi (1664)"]
cross_refs: [1663, 1664, 1463]
tags: ["2027"]
depends_on: [1663]
---

## 1662. 🧊 Apache Iceberg v3 : deletion vectors et row lineage (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Adopter Apache Iceberg v3 en 2027 (deletion vectors pour les suppressions efficaces + conformité effacement RGPD 189, row lineage pour la traçabilité ligne par ligne) dans un lakehouse ouvert (1463), avec support Snowflake/Databricks/Spark/DuckDB (1660).

**Quand l'utiliser (triggers)** :
- supprimer des lignes RGPD dans un lakehouse sans réécrire tout
- row lineage : d'où vient cette ligne (audit)
- Iceberg v3 dispo Snowflake mai 2026, spec ouverte 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte lakehouse. Tu expliques v3 : deletion vectors (fichiers de suppressions, mergés en compaction) → DELETE efficace, et row lineage (chaque ligne tracée depuis sa source). Format ouvert : lisible par DuckDB (1660), Spark, Trino, Snowflake. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le lakehouse Iceberg existant (v2 ?)
- Les besoins (effacement RGPD, audit)
- Les moteurs (Spark, Trino, DuckDB, Snowflake)

**Méthode** :
1. Migrer la table en v3 (format_version=3, migration progressive, compatibilité v2 maintenue).
2. DELETE/UPDATE efficaces : deletion vectors écrits, compaction automatique (CALL rewrite_data_files / optimize).
3. Row lineage : activer (write.lineage.enabled), requêter la provenance d'une ligne (lineage metadata).
4. RGPD : procédure d'effacement d'un user (DELETE WHERE user_id=...) vérifiée par lineage + compaction.
5. Choisir le moteur de compute adapté (DuckDB local 1660, Spark/Trino serverless pour le gros).

**Sorties attendues** :
- La table en Iceberg v3 (deletion vectors + lineage actifs)
- La procédure d'effacement RGPD testée (suppression + compaction + vérification)
- La compatibilité multi-moteurs (DuckDB/Spark/Trino/Snowflake)

**Exemple de prompt** :
> « Supprimer les données d'un user RGPD dans notre lakehouse Iceberg v2 réécrit tout : passe en v3 (deletion vectors → DELETE ciblé + compaction), active le row lineage pour prouver l'effacement en audit. »

**Cas d'usage** : Lakehouses avec conformité/audit. S'articule avec skills 1663 (Delta/Iceberg/Hudi), 1664 (choix), 1660 (DuckDB) et 189 (RGPD).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1834
resume: "Modéliser avec dbt : models SQL, tests intégrés + custom (métier), contracts de schéma (schema.yml avec data_type, enforcement à l'exécution), docs auto, snapshots SCD2 — dbt Fusion pour la vitesse. Étape 1 : Models : stg_* (clean) -supérieur à int_* -supérieur à f_* (marts), ref() entre eux."
date_ajout: "2026-11"
nom: "dbt : models, tests et contracts de schéma"
emoji: "🧱"
domaine: "Data"
signal: "Modéliser et tester avec dbt en 2027 : models SQL (ref), tests intégrés (unique, not_null, relationships, accepted_values) + tests custom (singular), contracts de schéma (schema.yml : columns avec data_type + contraintes, enforcement à l'exécution — violation = fail), docs auto (docs.generate), snapshots (SCD2), dbt Fusion (moteur Rust, plus rapide). N'utilise pas de tests génériques seuls : ajouter des tests métier (singular) sur les règles métier."
mot_cle: "dbt models tests schema.yml contracts data_type enforcement singular tests snapshots SCD2 dbt Fusion docs generate"
nom_court: "dbt"
branche: "D15"
synonymes: ["contrat de schéma dbt (schema.yml columns data_type) : violation = fail à l'exécution", "tests dbt : unique not_null relationships accepted_values + tests custom singular métier", "dbt Fusion (moteur Rust) : parse 10x plus rapide sur les gros projets"]
cross_refs: [1831, 1835, 1832]
tags: ["2027"]
depends_on: [1678]
---

## 1834. 🧱 dbt : models, tests et contracts de schéma

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Modéliser avec dbt : models SQL, tests intégrés + custom (métier), contracts de schéma (schema.yml avec data_type, enforcement à l'exécution), docs auto, snapshots SCD2 — dbt Fusion pour la vitesse.

**Quand l'utiliser (triggers)** :
- ajouter un test not_null + accepted_values sur un champ critique
- contrat de schéma : dbt échoue si le producteur casse le data_type promis (1831)
- docs auto (dbt docs generate) + lineage dans le DAG (1832)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer / analytics engineer. Tu écris les models (ref entre eux), les tests dans schema.yml (génériques + singular métier), les contracts (data_type) pour les tables consommées (1831), et tu génères la doc. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le warehouse (Snowflake/BigQuery/Databricks/Postgres)
- Les sources (raw)
- Les règles métier

**Méthode** :
1. Models : stg_* (clean) -> int_* -> f_* (marts), ref() entre eux.
2. schema.yml : models + columns (description, data_type pour contrat 1831) + tests (unique, not_null, relationships, accepted_values) + tests singular (fichier SQL) pour les règles métier.
3. dbt test en CI (1413) : échec = PR bloquée ; dbt build en prod.
4. dbt docs generate + serve : doc auto avec lineage (1832).
5. Snapshots pour SCD2 (dimensions lentes).

**Sorties attendues** :
- Les models + tests + contracts déployés
- La doc auto générée avec lineage
- Le CI qui bloque sur test en échec

**Exemple de prompt** :
> « Contrat sur f_orders.amount (data_type: numeric, not_null) : un producteur change en string -> dbt build échoue à l'exécution (contrat cassé 1831), alerte, rollback avant que les dashboards ne voient des données fausses. »

**Cas d'usage** : Qualité data as code. S'articule avec skills 1831 (contracts), 1835 (SLA), 1832 (lineage), 1765 (MCP).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

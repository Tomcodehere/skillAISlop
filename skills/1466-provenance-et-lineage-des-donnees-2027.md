---
num: 1466
nom: "Provenance et lineage des donnees (2027)"
emoji: "🧬"
domaine: "Data"
signal: "Documenter la provenance (lineage) des données en 2027 : d'où vient chaque table/colonne (source, ETL, propriétaire), graphe de dépendances amont/aval, impact analysis (si cette source casse, quoi est touché ?). Outils : OpenLineage, Marquez, DataHub, dbt docs. Utilise quand on a un pipeline complexe. N'utilise pas pour une petite BDD."
mot_cle: "lineage provenance données openlineage datahub impact analysis"
nom_court: "Lineage"
branche: "D15"
synonymes: ["d'où vient cette colonne", "impact analysis si source casse", "OpenLineage Marquez 2027"]
cross_refs: [1095, 95, 1461]
tags: ["2027"]
depends_on: [95]
---

## 1466. 🧬 Provenance et lineage des donnees (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Documenter le lineage des données en 2027 (OpenLineage/Marquez/DataHub ou dbt docs) : graphe des dépendances amont/aval par table/colonne, propriétaires, et impact analysis (si la source X casse, quelles cibles sont touchées).

**Quand l'utiliser (triggers)** :
- D'où vient cette métrique du dashboard ?
- Si le CRM tombe, quels rapports sont touchés ?
- Documenter la provenance des données (lineage)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data steward lineage. Tu mets en place la collecte de lineage (OpenLineage sur Airflow/dbt/Spark, ou DataHub), le graphe visualisé, les propriétaires par dataset, et l'impact analysis descendant (qui consomme cette table). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les pipelines existants (ETL, dbt, notebooks)
- L'outil de catalogage (DataHub, Marquez, dbt docs)
- Les propriétaires métier par domaine

**Méthode** :
1. Déployer la collecte de lineage (OpenLineage : jobs Airflow/dbt/Spark émettent les événements).
2. Visualiser le graphe (Marquez/DataHub) : sources → transformations → dashboards.
3. Assigner un propriétaire par dataset/table (data contracts 1234).
4. Faire un impact analysis : si source S en panne, liste des consommateurs aval.
5. Relier au catalogue (1095) et au schema drift (1461) pour les alertes.

**Sorties attendues** :
- Le graphe de lineage à jour et visualisable
- Les propriétaires assignés par dataset
- L'impact analysis d'une panne source type

**Exemple de prompt** :
> « Personne ne sait d'où vient le CA du dashboard : mets en place le lineage (OpenLineage sur les ETL, graphe DataHub, propriétaires, impact analysis). »

**Cas d'usage** : Gouvernance data, debug d'incidents, conformité. S'articule avec skills 1095 (catalogue), 95 (cartographie) et 1461 (drift).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1680
resume: "Tracer les pipelines data en 2027 avec OpenTelemetry : spans par étape (extract/load/transform), métriques (lignes/s, latence, erreurs), traces distribuées corrélées au lineage (1466) et aux alertes qualité (1675) — pour déboguer vite un pipeline cassé. Étape 1 : Instrumenter : chaque tâche du pipeline émet un span OTel (opentelemetry-sdk Python/Java) avec attributs (table, nb_lignes, durée, erreu"
lang: "fr"
date_ajout: "2026-11"
nom: "OpenTelemetry pour la data : tracer les pipelines"
emoji: "📈"
domaine: "Data"
signal: "Tracer les pipelines data en 2027 avec OpenTelemetry (standard ouvert, déjà pour les agents 713) : spans par étape (extract → load → transform), métriques (lignes/s, latence, erreurs), traces distribuées de bout en bout, corrélées aux incidents (1675) et au lineage (1466). Utilise pour déboguer un pipeline qui a cassé à 3 h du matin. N'utilise pas pour du batch simple."
mot_cle: "OpenTelemetry data pipelines 2027 traces spans extract load transform latence erreurs lineage 1466"
nom_court: "OTel data"
branche: "D15"
synonymes: ["tracer mon pipeline dlt/dbt de bout en bout (OpenTelemetry)", "pourquoi le pipeline de 3h a pris 2h aujourd'hui (traces OTel)", "corréler une alerte data quality (1675) avec la trace du pipeline (1466)"]
cross_refs: [713, 1466, 1675]
tags: ["2027"]
depends_on: [1466]
---

## 1680. 📈 OpenTelemetry pour la data : tracer les pipelines (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Tracer les pipelines data en 2027 avec OpenTelemetry : spans par étape (extract/load/transform), métriques (lignes/s, latence, erreurs), traces distribuées corrélées au lineage (1466) et aux alertes qualité (1675) — pour déboguer vite un pipeline cassé.

**Quand l'utiliser (triggers)** :
- le pipeline nightly est passé de 40 min à 3 h, où ? (traces OTel)
- corréler l'incident qualité (1675) avec la trace du pipeline (1466)
- OpenTelemetry Collector + Jaeger/Tempo pour visualiser

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data observability engineer. Tu instrumentes chaque étape du pipeline (dlt 1664, dbt 350, Spark) avec des spans OTel (nom, attributs: nb lignes, source, erreur), métriques (gauges), et tu visualises dans Jaeger/Tempo/Grafana (1416). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le pipeline à tracer (dlt/dbt/Spark 1460)
- L'OTel Collector + backend (Jaeger/Tempo/Grafana 1416)
- Les étapes critiques (où ça rame)

**Méthode** :
1. Instrumenter : chaque tâche du pipeline émet un span OTel (opentelemetry-sdk Python/Java) avec attributs (table, nb_lignes, durée, erreur).
2. Métriques : compteurs (lignes traitées, erreurs), histogrammes (durée par étape), gauges (taille fichiers).
3. Contexte distribué : trace_id propagé d'étape en étape (même inter-services), corrélé au lineage (1466) et aux alertes (1675).
4. Visualiser : Jaeger/Tempo (traces), Grafana (métriques 1416), dashboards par pipeline.
5. Alertes : latence > seuil ou taux d'erreur > 1 % → 1417, avec le lien vers la trace fautive.

**Sorties attendues** :
- Le pipeline instrumenté OTel (spans + métriques par étape)
- Les dashboards de latence/erreurs par étape (Grafana 1416)
- Les alertes (1417) avec lien direct vers la trace OTel fautive

**Exemple de prompt** :
> « Le pipeline nightly est passé de 40 min à 3 h sans raison visible : instrumente-le en OpenTelemetry (spans par étape dlt/dbt, métriques lignes/s), dashboard Grafana (1416) montre que l'étape 'jointure historique' a explosé, alerte 1417 avec la trace. »

**Cas d'usage** : Pipelines data en prod. S'articule avec skills 713 (OTel agents), 1466 (lineage), 1675 (qualité) et 1417 (alertes).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

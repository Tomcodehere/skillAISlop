---
num: 1462
resume: "Choisir et utiliser une TSDB en 2027 (TimescaleDB/InfluxDB/VictoriaMetrics) pour des métriques ou capteurs : ingestion rapide, downsampling/agrégation automatique, rétention par age, requêtes SQL ou Flux. Étape 1 : Choisir la TSDB selon volumétrie et langage de requête préféré (SQL = TimescaleDB)."
lang: "fr"
date_ajout: "2026-11"
nom: "TSDB et series temporelles : InfluxDB, TimescaleDB"
emoji: "⏱️"
domaine: "Data"
signal: "Stocker et requêter des séries temporelles en 2027 dans une TSDB : InfluxDB (Flux/InfluxQL), TimescaleDB (PostgreSQL + hypertables, SQL standard), VictoriaMetrics (rapide, peu de RAM). Critères : volumétrie, requêtes (downsampling, agrégation), rétention. Utilise pour métriques, capteurs IoT, logs temporels. N'utilise pas pour des données non temporelles."
mot_cle: "TSDB timescaledb influxdb victoria metrics séries temporelles"
nom_court: "TSDB"
branche: "D15"
synonymes: ["influxdb ou timescaledb 2027", "hypertable postgresql séries temps", "downsampling agrégation métriques"]
cross_refs: [345, 346, 1416]
tags: ["2027"]
depends_on: [1416]
---

## 1462. ⏱️ TSDB et series temporelles : InfluxDB, TimescaleDB (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir et utiliser une TSDB en 2027 (TimescaleDB/InfluxDB/VictoriaMetrics) pour des métriques ou capteurs : ingestion rapide, downsampling/agrégation automatique, rétention par age, requêtes SQL ou Flux.

**Quand l'utiliser (triggers)** :
- Stocker 1 milliard de points de capteurs IoT
- TimescaleDB vs InfluxDB en 2027
- Downsampling auto des métriques anciennes

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de données temporelles. Tu compares TimescaleDB (SQL, hypertables, compression, jointures avec le reste de la BDD), InfluxDB (Flux, ecosystem Telegraf), VictoriaMetrics (perf, faible conso) selon volumétrie et requêtes. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le flux de points (capteurs, métriques app, logs)
- La volumétrie (points/jour) et la rétention (1 an ?)
- Les requêtes typiques (agrégation 1 min/1 h/jour ?)

**Méthode** :
1. Choisir la TSDB selon volumétrie et langage de requête préféré (SQL = TimescaleDB).
2. Modéliser : measurement/table + tags (indexés) + fields + timestamp.
3. Configurer le downsampling/agrégation (continuous aggregates TimescaleDB) et la rétention (drop après X).
4. Ingérer (Telegraf, API, client lib) et monitorer l'ingestion.
5. Requêter (p99 par heure, tendances) et brancher Grafana (1416).

**Sorties attendues** :
- La TSDB déployée avec schéma et rétention
- Le downsampling automatique configuré
- Les dashboards Grafana branchés

**Exemple de prompt** :
> « On ingère 50 M de points/jour de capteurs : choisis une TSDB (TimescaleDB vs InfluxDB vs VictoriaMetrics), configure downsampling et rétention 1 an. »

**Cas d'usage** : IoT, métriques infra/app, monitoring industriel. S'articule avec skills 345 (séries temporelles), 346 (anomalies) et 1416 (monitoring).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

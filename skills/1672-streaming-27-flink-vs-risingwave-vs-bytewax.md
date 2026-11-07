---
num: 1672
date_ajout: "2026-11"
nom: "Streaming -27 : Flink vs RisingWave vs Bytewax"
emoji: "⏩"
domaine: "Data"
signal: "Choisir sa stack de streaming en 2027 : Apache Flink (référence, stateful, exactement-once 1464) vs RisingWave (PostgreSQL-compatible, materialized views en streaming, simple) vs Bytewax (Python, dataflow). Critères : équipe SQL vs Python, latence, état. Utilise pour du temps réel (fraude, IoT 1644, analytics live). N'utilise pas pour du batch (dbt 350)."
mot_cle: "streaming 2027 Flink vs RisingWave vs Bytewax materialized views temps réel SQL"
nom_court: "Streaming"
branche: "D15"
synonymes: ["RisingWave : des materialized views PostgreSQL en streaming", "Flink exactement-once stateful pour la détection de fraude", "Bytewax dataflow Python pour le streaming simple"]
cross_refs: [1464, 1280, 1462]
tags: ["2027"]
depends_on: [1464]
---

## 1672. ⏩ Streaming 2026-27 : Flink vs RisingWave vs Bytewax (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir sa stack de streaming en 2027 : Flink (référence, stateful, exactement-once 1464), RisingWave (vues matérialisées en SQL, compatible Postgres, simple), Bytewax (dataflow Python) — selon équipe SQL/Python, latence et état.

**Quand l'utiliser (triggers)** :
- détecter une fraude bancaire en temps réel (latence 100 ms)
- RisingWave : je fais du streaming en SQL pur (Postgres)
- Flink stateful exactement-once pour l'IoT industriel (1644)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte streaming. Tu compares : Flink (Java/Scala, stateful, exactly-once, complexe mais puissant), RisingWave (SQL, materialized views, frais de gestion nuls), Bytewax (Python pur, dataflows). Source : Kafka (1464). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La source (Kafka 1464, Kinesis)
- Le traitement (SQL vs Python vs Java)
- La latence cible et l'état à garder

**Méthode** :
1. Flink : job stateful (windowing, joins de streams, exactly-once via checkpoints), déploiement k8s (1412).
2. RisingWave : CREATE MATERIALIZED VIEW ... AS SELECT ... FROM kafka_topic — du SQL pur, résultat toujours à jour, requêtable en Postgres.
3. Bytewax : dataflow Python (input → operators → output), pour les équipes Python, moins de features entreprise.
4. Choisir : équipe SQL + simplicité → RisingWave ; besoin complexe (joins temporels, état lourd) → Flink ; équipe Python → Bytewax.
5. Benchmark : latence p99 et débit (messages/s) sur la charge réelle.

**Sorties attendues** :
- La stack de streaming choisie et benchmarkée (latence p99, débit)
- Les materialized views (RisingWave) ou jobs Flink en prod
- Le monitoring du lag (1464) avec alertes

**Exemple de prompt** :
> « Détecter les fraudes carte bancaire en 100 ms : compare Flink (stateful exactly-once) vs RisingWave (materialized view SQL sur le topic Kafka 1464) — benchmark latence p99 et débit sur la charge réelle. »

**Cas d'usage** : Temps réel : fraude, IoT (1644), analytics live, alertes (1417). S'articule avec skills 1464 (Kafka), 1280 (streaming) et 1462 (TSDB).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1280
resume: "Concevoir, implémenter et opérer des pipelines de traitement de données en temps réel (sub-seconde à quelques minutes) avec Kafka, Flink, Spark Streaming ou Kinesis pour use cases nécessitant faible latence (alerting, monitoring, ML inference temps réel)."
lang: "fr"
date_ajout: "2026-11"
nom: "Streaming Data Processing"
emoji: "💻"
domaine: "Développement"
signal: "Concevoir, implémenter et opérer des pipelines de traitement de données en temps réel (sub-seconde à quelques minutes) avec Kafka, Flink, Spark Streaming ou Kinesis pour use cases nécessitant faible l"
mot_cle: "streaming-data-processing"
nom_court: "Streaming Data Processing"
branche: "D1"
synonymes: ["traitement", "evenements", "temps", "journal quêtes compteur 3/5 temps réel"]
cross_refs: [576, 1121, 1099]
tags: ["2027"]
depends_on: [1121]
---

## 1280. 💻 Streaming Data Processing

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir, implémenter et opérer des pipelines de traitement de données en temps réel (sub-seconde à quelques minutes) avec Kafka, Flink, Spark Streaming ou Kinesis pour use cases nécessitant faible latence (alerting, monitoring, ML inference temps réel).

**Quand l'utiliser (triggers)** :
- Traitement d'événements en temps réel (clics web, IoT sensors, logs applicatifs)
- Architecture event-driven avec Kafka ou Kinesis comme backbone
- Transformation streaming (filtrage, agrégation fenêtrée, enrichissement)
- Détection d'anomalies temps réel (fraude, intrusion, défaillances)
- ML inference en temps réel (scoring, recommandations, prédictions)
- Réplication CDC (Change Data Capture) avec latence 1h latency) → etlPipelineDesignOrchestration.skill.md
- ❌ Architecture data lake → dataLakeArchitectureStorage.skill.md
- ❌ Infrastructure Kafka/Kinesis (broker setup, scaling) → l'agent d'architecture cloud
- ❌ ML model training → l'agent de machine learning
- ❌ Requêtes SQL analytics → l'agent bases de données

**Garde-fous** :
- **GF1 - Checkpointing obligatoire** : Tout pipeline Flink/Spark doit avoir checkpointing activé (fault-tolerance). Mesure : 100% des jobs avec checkpoint interval 5min critique). Alerter si lag croissant. Mesure : alerte si lag >seuil.
- **GF4 - Idempotence sink** : Sink (écriture destination) doit être idempotent (upsert, deduplication). Mesure : 0 duplicate en cas de replay.
- **GF5 - Schema registry** : Utiliser Avro/Protobuf + schema registry pour évolution schéma. Interdire JSON sans schéma. Mesure : 100% topics avec schéma.
- **GF6 - Parallelism adaptatif** : Ajuster parallelism selon throughput (auto-scaling si cloud). Mesure : utilisation CPU 60-80% (ni sous-utilisé, ni saturé).
- **GF7 - Latency SLA** : Définir SLA latency (ex: P95 <500ms) et alerter si dépassement. Mesure : P95 latency < SLA sur 24h.

**Instructions système** :
Tu es assistant spécialisé « Streaming Data Processing ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- **Source de données** : Kafka topics, Kinesis streams, event hubs, socket streams
- **Volumétrie** : events/sec (1K, 100K, 1M+), taille moyenne message (bytes)
- **Latence cible** : sub-seconde, <1min, <5min
- **Transformations** : filtrage, windowing (tumbling/sliding/session), join streams, enrichissement
- **Sink/destination** : Kafka, base de données, data lake, dashboard (Grafana, Kibana)
- **Contraintes** : exactly-once semantics, back-pressure, fault-tolerance

**Méthode** :
1. **Analyse du flux** :
2. **Design du pipeline** :
3. **Implémentation** :
4. **Tests et tuning** :
5. **Déploiement et monitoring** :

**Sorties attendues** :
- **Pipeline streaming** : code Flink/Spark Streaming/Kafka Streams
- **Config déploiement** : YAML Kubernetes, Docker Compose, ou cloud-managed config
- **Schéma Avro/Protobuf** : si serialisation structurée nécessaire
- **Monitoring** : métriques latence (P50/P95/P99), throughput, lag, erreurs
- **Documentation** : architecture (Mermaid), tuning parameters, runbook incidents

**Exemple de prompt** :
### Exemple 1 : Détecter en temps quasi réel des transactions à examiner
**Contexte** : Une équipe doit repérer des transactions inhabituelles peu après leur émission, sans bloquer le flux comptable si l'analyse est indisponible.  
**Input** : Schéma d'événement approuvé, débit de pointe, latence cible, fenêtre temporelle, règles d'idempotence et destination des alertes.  
**Output** : Pipeline év

**Cas d'usage** : complément : skill 576. traitement ; evenements ; temps

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).

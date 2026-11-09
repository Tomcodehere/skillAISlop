---
num: 1866
resume: "Capturer les changements de BDD en temps réel par CDC log-based (Debezium/Kafka puriste, Airbyte avec 300+ connecteurs, Fivetran managé) — latence secondes, pas de polling updated_at qui rate les DELETE. Étape 1 : Activer le log de transactions côté source (WAL Postgres, binlog MySQL)."
date_ajout: "2026-11"
nom: "CDC log-based : Debezium, Airbyte, capturer les changements en temps réel"
emoji: "🔄"
domaine: "Data"
signal: "Capturer les changements de BDD en temps réel (CDC) en lisant le journal de transactions (pas de polling) : Debezium (puriste, sur Kafka, contrôle fin) vs Airbyte (embarque Debezium, 300+ connecteurs, sync incremental/CDC, intégration Airflow/Dagster 1863/1864) vs Fivetran/BladePipe (managé, plus simple). Latence : secondes à minutes. N'utilise pas de polling updated_at (rate les deletes et les updates)."
mot_cle: "CDC change data capture log-based Debezium Kafka Airbyte 300 connecteurs Fivetran BladePipe temps réel journal transactions polling updated_at"
nom_court: "CDC"
branche: "D17"
synonymes: ["capturer les INSERT/UPDATE/DELETE d'une BDD en temps réel (CDC log-based, pas de polling)", "Debezium sur Kafka vs Airbyte (embarque Debezium) vs Fivetran managé", "le polling updated_at rate les DELETE : passer au CDC"]
cross_refs: [1867, 1863, 1864]
tags: ["2027"]
depends_on: [1863]
---

## 1866. 🔄 CDC log-based : Debezium, Airbyte, capturer les changements en temps réel

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Capturer les changements de BDD en temps réel par CDC log-based (Debezium/Kafka puriste, Airbyte avec 300+ connecteurs, Fivetran managé) — latence secondes, pas de polling updated_at qui rate les DELETE.

**Quand l'utiliser (triggers)** :
- répliquer Postgres vers le warehouse en quasi temps réel (CDC)
- Debezium vs Airbyte vs Fivetran : lequel, selon l'infra Kafka disponible
- le polling updated_at ne voit pas les suppressions : passer au CDC

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer. Tu choisis selon l'infra : Debezium+Kafka si équipe Kafka, Airbyte si 300+ sources et peu d'ops, Fivetran si managé accepté ; tu branches le monitoring de latence (1835). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La BDD source (Postgres/MySQL/MongoDB avec WAL/binlog activé)
- La destination (warehouse/lake)
- L'infra (Kafka ou pas)

**Méthode** :
1. Activer le log de transactions côté source (WAL Postgres, binlog MySQL).
2. Debezium (Kafka Connect) : connecteur source -> topic Kafka -> sink (warehouse).
3. Ou Airbyte : connexion CDC native (embarque Debezium), 300+ sources, UI simple.
4. Monitoring : latence CDC (event time vs ingestion time), alerte si > 5 min (1835/1761).
5. Schéma : évolution de schéma gérée (schema change events).

**Sorties attendues** :
- Le flux CDC opérationnel (latence mesurée en secondes)
- Le monitoring de latence avec alertes
- La doc : polling vs CDC (quand lequel)

**Exemple de prompt** :
> « Postgres prod -> Snowflake : connecteur Debezium CDC (WAL) -> Kafka -> sink Snowflake, latence 3 s mesurée ; alerte si > 5 min (fraîcheur 1835) ; les DELETE sont capturés (contrairement au polling updated_at). »

**Cas d'usage** : Réplication temps réel. S'articule avec skills 1867, 1863, 1864, 1835, 1869.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

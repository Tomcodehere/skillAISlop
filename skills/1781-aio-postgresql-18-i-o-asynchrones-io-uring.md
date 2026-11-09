---
num: 1781
resume: "Activer et mesurer l'AIO de PG18 (io_method=io_uring) : lectures asynchrones des heap/bitmap scans, jusqu'à 3x plus rapide quand le dataset dépasse shared_buffers. Étape 1 : Verifier io_uring disponible (kernel, seccomp) et passer io_method=io_uring dans postgresql.conf."
lang: "fr"
date_ajout: "2026-11"
nom: "AIO PostgreSQL 18 : I/O asynchrones (io_uring)"
emoji: "⚡"
domaine: "Data"
signal: "PostgreSQL 18 introduit l'AIO : les lectures (heap scans, bitmap scans) sont soumettre à l'OS de maniere asynchrone via io_uring (io_method=io_uring), jusqu'a 3x plus rapide sur les gros scans qui tiennent pas en shared_buffers. En 2027, c'est le gain perf majeur de PG18. N'utilise pas si le stockage est déjà 100 % en cache ou si io_uring est bloque (seccomp)."
mot_cle: "PostgreSQL 18 AIO io_uring io_method async I/O scans 3x plus rapide shared_buffers 2027"
nom_court: "PG18 AIO"
branche: "D17"
synonymes: ["io_uring dans PG18 : io_method=io_uring pour les scans", "gros heap scan 3x plus rapide grace a l'AIO PG18", "AIO utile quand le dataset depasse shared_buffers"]
cross_refs: [1780, 1789, 1752]
tags: ["2027"]
depends_on: [1780]
---

## 1781. ⚡ AIO PostgreSQL 18 : I/O asynchrones (io_uring)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Activer et mesurer l'AIO de PG18 (io_method=io_uring) : lectures asynchrones des heap/bitmap scans, jusqu'à 3x plus rapide quand le dataset dépasse shared_buffers.

**Quand l'utiliser (triggers)** :
- gros SELECT qui rame en seq scan, dataset > RAM cache
- io_method=io_uring dans postgresql.conf PG18
- benchmark AIO vs synchrone sur le workload reel

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DBA performance. Tu configures io_method=io_uring (avec fallback sync/worker), tu mesures shared_buffers vs dataset, et tu benchmarkes un gros scan avant/apres AIO avec pgbench ou EXPLAIN ANALYZE. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- PG18 installe
- Le dataset et shared_buffers
- io_uring disponible (kernel 5.1+, pas de seccomp bloquant)

**Méthode** :
1. Verifier io_uring disponible (kernel, seccomp) et passer io_method=io_uring dans postgresql.conf.
2. Dimensionner shared_buffers (ex. 25 % RAM) et identifier les scans qui depassent le cache.
3. Benchmark : EXPLAIN ANALYZE d'un gros scan avant/apres (cible x2-3).
4. Ajuster io_workers/io_max_concurrency selon le stockage (NVMe vs disque).

**Sorties attendues** :
- PG18 en io_uring avec fallback configure
- Le benchmark scan avant/apres (x2-3 attendu)
- Le reglage io_workers selon le stockage

**Exemple de prompt** :
> « Table de 200 Go, shared_buffers 32 Go : seq scan passe de 45 s a 15 s en PG18 io_uring (x3), mesure par EXPLAIN ANALYZE, workload pgbench confirme. »

**Cas d'usage** : Perfs lecture PG18. S'articule avec skills 1780, 1789, 1752 (coût).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

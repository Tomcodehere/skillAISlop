---
num: 1660
resume: "Utiliser DuckDB en 2027 : moteur SQL analytique embarqué (pas de serveur) qui lit directement Parquet/CSV/S3/HTTP, joint des sources hétérogènes (fichiers + Postgres), avec extensions (spatial, iceberg 1663), pour EDA et pipelines locaux. Étape 1 : Installer DuckDB (CLI, pip, extension VSCode/Jupyter), ouvrir en mémoire ou fichier .duckdb."
lang: "fr"
date_ajout: "2026-11"
nom: "DuckDB : le SQLite de l'analytics, requêter Parquet/S3 directement"
emoji: "🦆"
domaine: "Data"
signal: "Utiliser DuckDB en 2027 (« le SQLite de l'analytics ») : moteur analytique embarqué (pas de serveur), requêtes SQL directes sur Parquet/CSV/JSON locaux OU distants (S3, HTTP), jointures entre fichiers et BDD (Postgres 1229), extension spatial/iceberg. Utilise pour l'EDA, les data pipelines locaux, l'analytics embarquée (1607). N'utilise pas pour un entrepôt multi-users à grande échelle (warehouse 1463)."
mot_cle: "DuckDB sqlite de l'analytics requêter Parquet S3 directement SQL embarqué 2027"
nom_court: "DuckDB"
branche: "D15"
synonymes: ["requêter un Parquet sur S3 en SQL sans rien installer (DuckDB)", "DuckDB embarqué dans mon app (analytics in-process)", "joindre un CSV local et une table Postgres en une requête"]
cross_refs: [1463, 1666, 1607]
tags: ["2027"]
depends_on: [1463]
---

## 1660. 🦆 DuckDB : le SQLite de l'analytics, requêter Parquet/S3 directement (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser DuckDB en 2027 : moteur SQL analytique embarqué (pas de serveur) qui lit directement Parquet/CSV/S3/HTTP, joint des sources hétérogènes (fichiers + Postgres), avec extensions (spatial, iceberg 1663), pour EDA et pipelines locaux.

**Quand l'utiliser (triggers)** :
- analyser un Parquet de 10 Go sur mon laptop en 2 s
- SELECT * FROM 's3://bucket/data.parquet' directement
- joindre CSV local + table Postgres + API JSON en une requête

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data analyst embarqué. Tu montres : install (pip/brew/extension navigateur), lecture directe S3 (httpfs), lecture Parquet/CSV/JSON, jointures cross-sources (postgres extension), COPY vers Parquet, et l'embarquement dans une app (1607). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les fichiers de données (Parquet/CSV/JSON locaux ou S3)
- Les sources externes à joindre (Postgres, API)
- Le cas d'usage (EDA, pipeline local, app embarquée)

**Méthode** :
1. Installer DuckDB (CLI, pip, extension VSCode/Jupyter), ouvrir en mémoire ou fichier .duckdb.
2. Lire directement : SELECT * FROM read_parquet('s3://.../f.parquet') (extension httpfs, credentials AWS env).
3. Joindre : postgres_scan('mydb','public','users') + read_csv('local.csv') dans une requête.
4. Agrégations rapides (GROUP BY, window 1420), COPY (...) TO 'out.parquet' (PARQUET format).
5. Embarquer : dans une app (Python/JS/Rust), DuckDB tourne in-process (analytics embarquée 1607).

**Sorties attendues** :
- Les requêtes DuckDB sur S3/Parquet/CSV fonctionnelles
- Les jointures cross-sources (fichiers + Postgres + API)
- Le cas embarqué (analytics in-process) testé

**Exemple de prompt** :
> « J'ai un Parquet de 20 Go sur S3 et une table clients en Postgres : une requête DuckDB joint les deux (read_parquet s3 + postgres_scan) et sort un rapport agrégé en 3 s sur mon laptop. »

**Cas d'usage** : EDA, pipelines locaux, analytics embarquée, remplacer Excel (264). S'articule avec skills 1463 (warehouse/lakehouse), 1666 (Polars) et 1607 (ML embarqué).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

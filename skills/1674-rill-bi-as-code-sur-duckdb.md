---
num: 1674
resume: "Faire du BI as code en 2027 avec Rill (open source) : dashboards en YAML/SQL sur DuckDB (1660), versionnés dans Git, déployés en 1 clic (Rill Cloud ou self-host), alertes intégrées — pour les petites équipes data. Étape 1 : Projet Rill : rill project init, sources (S3/Parquet via DuckDB 1660, MotherDuck 1661)."
date_ajout: "2026-11"
nom: "Rill : BI as code sur DuckDB"
emoji: "📊"
domaine: "Data"
signal: "Faire du BI as code en 2027 avec Rill (open source) : dashboards définis en YAML/SQL sur DuckDB (1660), versionnés dans Git, déployés en un clic (rill cloud ou self-host), avec alertes. Alternative à Superset (1666) pour les petites équipes. N'utilise pas pour sup. à  100 users ou téraoctets (warehouse 1463)."
mot_cle: "rill BI as code YAML SQL duckDB dashboards versionnés Git 2027"
nom_court: "Rill BI"
branche: "D15"
synonymes: ["dashboards en YAML/SQL versionnés dans Git (Rill)", "Rill sur DuckDB : BI as code sans serveur lourd", "rill deploy en un clic (cloud ou self-host)"]
cross_refs: [1666, 1660, 107]
tags: ["2027"]
depends_on: [1660]
---

## 1674. 📊 Rill : BI as code sur DuckDB (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire du BI as code en 2027 avec Rill (open source) : dashboards en YAML/SQL sur DuckDB (1660), versionnés dans Git, déployés en 1 clic (Rill Cloud ou self-host), alertes intégrées — pour les petites équipes data.

**Quand l'utiliser (triggers)** :
- nos dashboards Superset sont modifiés en clic-bouton, pas versionnés
- Rill : metrics + dashboards en YAML dans Git
- rill deploy : le dashboard en ligne en 1 commande

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analytics engineer. Tu définis : models SQL (DuckDB 1660), metrics YAML (dimensions, mesures, time grain), dashboards YAML (filtres, graphiques), le tout dans Git, déployé via rill deploy (cloud) ou docker (self-host). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les données (DuckDB 1660 / MotherDuck 1661 / S3 Parquet)
- Les métriques et dashboards à construire
- L'hébergement (Rill Cloud vs self-host)

**Méthode** :
1. Projet Rill : rill project init, sources (S3/Parquet via DuckDB 1660, MotherDuck 1661).
2. models/*.sql (SQL sur DuckDB) → tables intermédiaire, tests (349).
3. metrics/*.yaml : dimensions (user_id, date), mesures (count, sum, ratio), time grain (day).
4. dashboards/*.yaml : graphiques (line, bar, table), filtres, liens entre dashboards.
5. Git + rill deploy → Rill Cloud (partage équipe, alertes 1417) ou self-host docker.

**Sorties attendues** :
- Le projet Rill (models+metrics+dashboards) versionné Git
- Le dashboard déployé (Rill Cloud ou self-host) partageable
- Les alertes de métriques (1417) configurées

**Exemple de prompt** :
> « Nos dashboards sont modifiés en clic-bouton sans historique : passe en Rill (models SQL sur DuckDB 1660, metrics+dashboard en YAML, Git, rill deploy → lien partageable équipe, alertes 1417). »

**Cas d'usage** : Petites équipes data, BI as code. S'articule avec skills 1666 (modern stack), 1660 (DuckDB), 107 (dashboards) et 1349? non.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

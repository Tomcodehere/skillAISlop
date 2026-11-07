---
num: 1675
date_ajout: "2026-11"
nom: "Data quality -27 : Great Expectations, Monte Carlo, alertes auto"
emoji: "🧪"
domaine: "Data"
signal: "Automatiser la qualité des données en 2027 (incident de fraîcheur 1096 existe, drift 1461 existe — angle monitoring continu) : Great Expectations (tests déclaratifs sur les données, CI), Monte Carlo/Datafold (monitoring ML : fraîcheur, volume, schéma, distribution), alertes auto (1417) + SLA producteur/consommateur (1234), incident data (1096). Utilise en prod sur les pipelines critiques. N'utilise pas pour un CSV perso."
mot_cle: "data quality 2027 Great Expectations Monte Carlo monitoring ML fraîcheur volume schéma alertes auto SLA"
nom_court: "Data quality"
branche: "D15"
synonymes: ["alerte auto si la table clients est vide à 6h du matin", "Great Expectations : tests déclaratifs en CI (1592)", "Monte Carlo : détection ML de l'anomalie de volume (1652? non)"]
cross_refs: [349, 1461, 1417]
tags: ["2027"]
depends_on: [1461]
---

## 1675. 🧪 Data quality 2026-27 : Great Expectations, Monte Carlo, alertes auto (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser la data quality en 2027 : GX (tests déclaratifs en CI 1592), monitoring ML (Monte Carlo/Datafold : fraîcheur, volume, schéma, distribution, lignage 1466), alertes auto (1417) avec SLA producteur/consommateur (1234), incident data (1096).

**Quand l'utiliser (triggers)** :
- le dashboard affiche 0 depuis ce matin, personne n'a vu
- alerte Slack à 6h si la table n'est pas arrivée (fraîcheur)
- drift de schéma détecté auto (1461) + alerte producteur

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data reliability engineer. Tu mets GX (expectations sur colonnes: not_null, unique, in_set, custom SQL 1420) en CI sur les pipelines (1592), et Monte Carlo en prod (monitors ML sur fraîcheur/volume/schéma/distribution), alertes → Slack/PagerDuty (1417), runbook incident (1096). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les pipelines critiques (dlt 1664, dbt 350)
- Les attentes qualité par table (règles métier)
- Les canaux d'alerte (1417)

**Méthode** :
1. GX : définir les expectations par table critique (schema 1461, not_null, unique, ranges, relations FK 1424), run en CI (1592) à chaque livraison de données, fail si violation.
2. Monte Carlo/Datafold en prod : monitors auto (ML) sur fraîcheur (dernière arrivée), volume (vs historique), schéma (drift 1461), distribution (valeurs), lignage impacté (1466).
3. Alertes : Slack/PagerDuty (1417) avec contexte (quelle table, quelle métrique, écart), routage au producteur (1234 SLA).
4. Incident : procédure (1096) — geler le consommateur, notifier, corriger, rejouer.
5. Métriques : MTTR data, nb d'incidents/mois, % pipelines couverts (objectif 100 % des critiques).

**Sorties attendues** :
- Les expectations GX en CI bloquantes (1592) sur les pipelines critiques
- Le monitoring ML (Monte Carlo) en prod avec alertes auto (1417)
- Le runbook incident data (1096) + métriques MTTR

**Exemple de prompt** :
> « Le dashboard affiche 0 depuis 6 h et personne n'a vu : mets GX en CI (1592, tests sur la table critique) + Monte Carlo en prod (alerte auto si pas arrivée à 6 h, drift schéma 1461), alertes Slack (1417) au producteur avec SLA (1234), runbook incident (1096). »

**Cas d'usage** : Fiabilité data en prod. S'articule avec skills 349 (tests données), 1461 (drift), 1417 (alertes) et 1096 (incident fraîcheur).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1699
date_ajout: "2026-11"
nom: "Data observability unifiée des pipelines : Monte Carlo, Datafold, Soda"
emoji: "📈"
domaine: "Data & IA"
signal: "Unifier l'observabilité des pipelines data en 2027 (complète 1675/1680) : une plateforme (Monte Carlo, Datafold, ou open source Soda Cloud + OpenTelemetry 1680) couvre fraîcheur, volume, schéma (drift 1461), distribution, lignage (1466), qualité (GX 349) — avec alertes (1417), SLA (1678), et corrélation incident (1096) ↔ trace OTel (1680). Utilise pour ne plus avoir 5 outils qui se contredisent. N'utilise pas pour un pipeline perso."
mot_cle: "data observability unifiée 2027 Monte Carlo Datafold Soda Cloud OTel 1680 fraîcheur volume schéma lignage alertes"
nom_court: "Observabilité data"
branche: "D14"
synonymes: ["5 outils d'observabilité data qui se contredisent, unifier (2027)", "Monte Carlo ou Datafold : monitoring ML des pipelines", "corrélation incident qualité (1675) ↔ trace OTel (1680) ↔ lineage (1466)"]
cross_refs: [1675, 1680, 1466]
tags: ["2027"]
depends_on: [1675]
---

## 1699. 📈 Data observability unifiée des pipelines : Monte Carlo, Datafold, Soda (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Unifier l'observabilité data en 2027 sur une plateforme (Monte Carlo/Datafold, ou Soda Cloud + OTel 1680) : fraîcheur, volume, schéma (1461), distribution, lignage (1466), qualité (349) — alertes unifiées (1417), SLA (1678), corrélation incident (1096) ↔ trace (1680).

**Quand l'utiliser (triggers)** :
- 3 outils disent des choses différentes sur le même pipeline
- incident 1096 : retrouver la trace OTel (1680) + le lignage impacté (1466) en 5 min
- choisir Monte Carlo vs Datafold vs Soda open source en 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data reliability engineer. Tu unifies : une seule plateforme de monitoring (Monte Carlo/Datafold payant, ou Soda Cloud + OTel Collector 1680 open source), connectée aux sources (dlt 1664, dbt 350, Airflow/Kestra 1460/1673), avec alertes routées (1417) et runbooks (1096). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les pipelines (dlt 1664, dbt 350, orchestrés 1460/1673)
- La plateforme choisie (Monte Carlo/Datafold/Soda+OTel)
- Les SLA par table (1678)

**Méthode** :
1. Choisir : Monte Carlo ou Datafold (SaaS, ML auto, cher) ou Soda Cloud + OTel (1680) open source (plus de config).
2. Connecter les sources : dlt/dbt/Airflow envoient métriques + traces OTel (1680) + schéma (1461) vers la plateforme.
3. Monitors auto : fraîcheur, volume, schéma, distribution, nulls, lignage impacté (1466) — seuils auto (ML) + manuels (SLA 1678).
4. Alertes unifiées : Slack/PagerDuty (1417) avec contexte complet (table, métrique, trace OTel 1680, lignage 1466, propriétaire 1678).
5. Incident : runbook (1096), corrélation auto trace↔métrique↔lignage, post-mortem (89).

**Sorties attendues** :
- La plateforme d'observabilité unifiée déployée (Monte Carlo/Datafold ou Soda+OTel)
- Les alertes unifiées avec contexte complet (trace 1680 + lignage 1466 + SLA 1678)
- Le runbook incident (1096) + corrélation testée en exercice (1454)

**Exemple de prompt** :
> « 3 outils disent des choses différentes sur le pipeline 'clients' : unifie sur Monte Carlo (ou Soda+OTel 1680 open source) — fraîcheur/volume/schéma (1461)/lignage (1466) monitorés, alertes Slack (1417) avec la trace OTel (1680) et le lignage impacté, runbook incident (1096). »

**Cas d'usage** : Pipelines data en prod. S'articule avec skills 1675 (qualité), 1680 (OTel), 1466 (lineage), 1678 (SLA) et 1096 (incident).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

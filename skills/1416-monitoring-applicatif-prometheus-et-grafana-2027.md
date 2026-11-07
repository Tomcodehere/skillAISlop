---
num: 1416
nom: "Monitoring applicatif Prometheus et Grafana (2027)"
emoji: "📈"
domaine: "Développement"
signal: "Mettre en place le monitoring applicatif en 2027 avec Prometheus (métriques, PromQL) et Grafana (dashboards, alertes) : instrumenter l'app (compteurs, histogrammes), scraping, alertes sur SLO. Utilise quand une app part en prod. N'utilise pas pour les logs."
mot_cle: "prometheus grafana monitoring métriques promql"
nom_court: "Prom+Grafana"
branche: "D16"
synonymes: ["monitoring app prometheus", "dashboards grafana alertes", "métriques custom promql 2027"]
cross_refs: [1282, 1209, 351]
tags: ["2027"]
depends_on: [351]
---

## 1416. 📈 Monitoring applicatif Prometheus et Grafana (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Instrumenter et surveiller une app en 2027 avec Prometheus (métriques custom, PromQL) et Grafana (dashboards + alertes), avec des alertes sur SLO (pas sur le CPU seul).

**Quand l'utiliser (triggers)** :
- Mettre en place Prometheus/Grafana sur mon app
- Quelles métriques custom instrumenter ?
- Alertes sur SLO plutôt que CPU

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE monitoring. Tu donnes les 4 golden signals (latence, trafic, erreurs, saturation), l'instrumentation (client Prometheus), un dashboard type et des alertes SLO (erreur > 1 % sur 5 min). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La stack de l'app
- Les golden signals pertinents
- Les SLO définis (skill 351)

**Méthode** :
1. Instrumenter : compteurs (requêtes), histogrammes (latence), gauges (files).
2. Déployer Prometheus (scrape) + Grafana (dashboards).
3. Dashboard des 4 golden signals + métriques métier.
4. Alertes sur SLO (erreurs 5xx, p99) → Alertmanager → Slack/PagerDuty.
5. Tester une alerte pour valider le routage.

**Sorties attendues** :
- L'app instrumentée (/metrics)
- Le dashboard Grafana
- Les alertes SLO opérationnelles

**Exemple de prompt** :
> « Notre API part en prod lundi : mets en place Prometheus + Grafana (métriques custom, dashboard golden signals, alerte si erreurs > 1 %). »

**Cas d'usage** : Production, détection précoce d'incidents. S'articule avec skills 1282 (monitoring), 1209 (observabilité) et 351 (SLI/SLO).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

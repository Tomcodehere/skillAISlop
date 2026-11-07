---
num: 1754
date_ajout: "2026-11"
nom: "Observability as code : dashboards et alertes en Git (2027)"
emoji: "📂"
domaine: "Développement"
signal: "Gérer l'observabilité as code en 2027 : dashboards Grafana, alertes Prometheus/Alertmanager, SLO (351) définis en code (JSON/Terraform provider Grafana, ou Grafana k8s CRD), versionnés dans Git, déployés par CI (1413) comme du code (revue PR 1401). Plus de clic-bouton dans l'UI qui pourrit. N'utilise pas pour une alerte one-off."
mot_cle: "observability as code 2027 dashboards alertes SLO en Git JSON Terraform grafana CRD CI 1413 revue PR 1401"
nom_court: "Obs as code"
branche: "D16"
synonymes: ["mes dashboards Grafana sont en code (Terraform/JSON), plus de clic-bouton", "alertes Prometheus en YAML dans Git, déployées par CI (1413)", "SLO (351) as code + revue de PR (1401) avant déploiement"]
cross_refs: [1416, 1592, 1401]
tags: ["2027"]
depends_on: [1592]
---

## 1754. 📂 Observability as code : dashboards et alertes en Git (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gérer l'observabilité as code en 2027 : dashboards (Grafana JSON/Terraform/CRD), alertes (Prometheus YAML), SLO (351) — tout en Git, déployé par CI (1413), revu en PR (1401). Plus de clic-bouton qui pourrit.

**Quand l'utiliser (triggers)** :
- mes dashboards Grafana sont modifiés en clic-bouton, plus personne ne sait pourquoi
- alertes Prometheus en YAML dans Git + CI (1413) + revue (1401)
- SLO (351) déclarés en code, versionnés

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE platform. Tu exportes la config Grafana/Prometheus en code (JSON/YAML/Terraform), tu la mets dans un repo observability/ avec CI (1413), revue PR (1401), déploiement auto, et tu synchronises l'UI avec le code (grafana sync). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La stack (Grafana 1416, Prometheus, Alertmanager)
- Le repo Git dédié
- La CI (1413)

**Méthode** :
1. Repo observability/ : dashboards/ (JSON export Grafana ou provider Terraform), alerts/ (YAML Prometheus rules), slos/ (SLO 351 en YAML/CRD).
2. CI (1413) : lint (promtool check rules, grafana lint), tests (alertes testées 1454? non — promtool test), déploiement (terraform apply ou kubectl apply CRD) après revue PR (1401).
3. Grafana : provisioning datasources/dashboards depuis le repo (ConfigMap k8s ou API) → l'UI reflète le code.
4. Alertmanager : routes/notifications en YAML (Slack 1417, PagerDuty), testées.
5. Règle : plus de modification directe dans l'UI en prod (sauf debug temporaire, resync auto depuis Git).
6. Historique complet en Git (qui a changé quelle alerte, quand, pourquoi).

**Sorties attendues** :
- Le repo observability/ (dashboards+alertes+SLO en code) déployé par CI (1413)
- La règle 'plus de clic-bouton en prod' + resync auto depuis Git
- L'historique Git complet des changements d'observabilité

**Exemple de prompt** :
> « Nos alertes Prometheus ont été modifiées en clic-bouton et personne ne sait qui/quoi : passe en observability as code 2027 — repo observability/ (alertes YAML, dashboards JSON, SLO 351), CI 1413 (promtool + revue PR 1401) déploie, plus de modif directe en prod. »

**Cas d'usage** : Gouvernance observabilité. S'articule avec skills 1416 (Grafana), 1592 (CI), 1401 (revue), 351 (SLO) et 1417 (alertes).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

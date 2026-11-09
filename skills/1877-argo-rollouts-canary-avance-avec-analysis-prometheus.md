---
num: 1877
resume: "Déployer en canary avancé avec Argo Rollouts : Rollout avec setWeight/pause/AnalysisTemplate Prometheus (erreurs 5xx, latence p99) — abort automatique si dégradation, promotion auto sinon. Étape 1 : Rollout CR : strategy canary steps: setWeight 10, pause 5 min, analysis (AnalysisTemplate)."
date_ajout: "2026-11"
nom: "Argo Rollouts : canary avancé avec analysis Prometheus"
emoji: "🚀"
domaine: "Développement"
signal: "Déployer en canary avancé avec Argo Rollouts (vs le canary basique 1418) : Rollout CR avec steps (setWeight 10 %, pause, analysis), AnalysisTemplate interrogeant Prometheus (1416) — taux d'erreur 5xx, latence p99 — et abort auto si métriques dégradées, promotion auto sinon. Blue-green aussi (1418). Intégration GitOps Argo CD (1704). N'utilise pas pour un déploiement 'big bang' acceptable."
mot_cle: "Argo Rollouts Rollout canary steps setWeight pause AnalysisTemplate Prometheus abort auto métriques 5xx latence p99 blue-green Argo CD 1704"
nom_court: "Argo Rollouts"
branche: "D16"
synonymes: ["canary auto 10 % — pause — analyse Prometheus (erreur 5xx, p99) — abort ou promote (Argo Rollouts)", "AnalysisTemplate : requête PromQL sur les métriques du canary avant de passer à 100 %", "blue-green avec Argo Rollouts (switch instantané du trafic)"]
cross_refs: [1418, 1704, 1416]
tags: ["2027"]
depends_on: [1704]
---

## 1877. 🚀 Argo Rollouts : canary avancé avec analysis Prometheus

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer en canary avancé avec Argo Rollouts : Rollout avec setWeight/pause/AnalysisTemplate Prometheus (erreurs 5xx, latence p99) — abort automatique si dégradation, promotion auto sinon.

**Quand l'utiliser (triggers)** :
- canary 10 % puis analyse auto des métriques Prometheus avant 100 %
- abort auto si taux 5xx > 1 % sur le canary (Argo Rollouts AnalysisTemplate)
- blue-green : switch instantané + rollback instantané

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / ingénieur plateforme. Tu remplaces le Deployment par un Rollout (steps + AnalysisTemplate PromQL), et tu laisses Argo CD (1704) piloter ; l'abort se déclenche sur les métriques 1416. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Argo Rollouts installé (à côté d'Argo CD 1704)
- Les métriques Prometheus (1416)
- Le Rollout CR + AnalysisTemplate

**Méthode** :
1. Rollout CR : strategy canary steps: setWeight 10, pause 5 min, analysis (AnalysisTemplate).
2. AnalysisTemplate : metric PromQL (ex. rate(http_5xx[5m]) > 0.01) -> abort.
3. Si OK : promotion auto 50 % -> 100 % ; si KO : abort + rollback auto.
4. Blue-green : strategy blueGreen avec autoPromotion ou manual (validation).

**Sorties attendues** :
- Le Rollout canary avec analyse auto déployé
- L'abort testé (métrique dégradée simulée -> rollback)
- La promotion auto quand métriques OK

**Exemple de prompt** :
> « Release api v2 : Rollout canary 10 % (5 min) -> analysis PromQL (5xx < 1 %, p99 < 500 ms) OK -> 50 % -> 100 % auto ; sur une autre release, p99 canary à 2 s -> abort auto + rollback v1 en 30 s. »

**Cas d'usage** : Déploiement sûr. S'articule avec skills 1418, 1704, 1416, 1417, 1873.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

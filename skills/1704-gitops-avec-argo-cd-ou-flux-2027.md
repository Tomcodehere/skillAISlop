---
num: 1704
date_ajout: "2026-11"
nom: "GitOps avec Argo CD ou Flux (2027)"
emoji: "🔄"
domaine: "Développement"
signal: "Appliquer le GitOps en 2027 avec Argo CD (le plus répandu) ou Flux (CNCF graduated) : l'état désiré (manifests k8s, config) vit dans Git, l'opérateur (Argo/Flux) réconcilie le cluster en continu — tout changement passe par une PR reviewée, rollback = git revert. Utilise pour tout déploiement k8s. N'utilise pas sans gestion des secrets (Sealed Secrets/ESO 1656)."
mot_cle: "gitops argo cd flux 2027 réconciliation cluster état désiré git PR rollback git revert"
nom_court: "GitOps"
branche: "D16"
synonymes: ["déployer sur k8s via PR Git (Argo CD) pas de kubectl apply manuel", "Argo CD vs Flux choisir 2027 (CNCF graduated)", "rollback = git revert (l'état revient à la version Git)"]
cross_refs: [609, 316, 1656]
tags: ["2027"]
depends_on: [609]
---

## 1704. 🔄 GitOps avec Argo CD ou Flux (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre le GitOps en 2027 avec Argo CD (ou Flux) : manifests k8s dans Git, réconciliation automatique du cluster, déploiement via PR reviewée, rollback par git revert, drift détecté et corrigé (ou notifié).

**Quand l'utiliser (triggers)** :
- plus de kubectl apply manuel en prod
- Argo CD : l'app déployée se resynchronise toute seule depuis Git
- rollback d'une release = git revert de la PR (2 min)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform engineer déploiement. Tu installes Argo CD (ou Flux) sur le cluster (609), tu pointes une app Git (manifests + kustomize/helm), Argo sync auto ou manuel, health checks, et tu configures les notifications (Slack 1417) sur drift/sync failure. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cluster k8s (609)
- Le repo Git des manifests (app + env)
- L'outil (Argo CD vs Flux)

**Méthode** :
1. Choisir : Argo CD (UI riche, multi-cluster, ApplicationSet) ou Flux (CNCF graduated, plus léger, natif Git).
2. Installer sur le cluster, créer l'Application : source Git (repo+path+branche env), destination (cluster+namespace), sync policy (auto avec prune/self-heal ou manuel).
3. Workflow : changement = PR sur le repo manifests → review (1401) → merge → Argo déploie automatiquement, health check (rollout status 1412).
4. Drift : si quelqu'un modifie le cluster à la main, Argo détecte (OutOfSync) et resync (self-heal) ou alerte (Slack 1417).
5. Rollback : git revert de la PR de déploiement → Argo déploie la version précédente en 2 min.
6. Secrets : Sealed Secrets ou External Secrets Operator (Vault 1656), jamais en clair dans Git (1403).

**Sorties attendues** :
- Argo CD (ou Flux) déployé avec sync auto + self-heal
- Le déploiement par PR (review 1401) + rollback git revert testé
- Les alertes de drift (OutOfSync) vers Slack (1417)

**Exemple de prompt** :
> « On déploie encore avec kubectl apply manuel en prod : passe en GitOps Argo CD (manifests dans Git, sync auto+self-heal, déploiement par PR reviewée, rollback = git revert en 2 min, drift alerté sur Slack). »

**Cas d'usage** : Tout déploiement k8s. S'articule avec skills 609 (k8s), 316 (Git), 1656 (secrets), 1413 (CI) et 1401 (review).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1879
resume: "GitOps avancé avec Argo CD : ApplicationSet (templates + générateurs git/clusters pour N environnements), sync waves (ordre de déploiement), progressive syncs avec Argo Rollouts (1877). Étape 1 : ApplicationSet : spec.generators (git directories ou cluster CAPI) + template (name, repo, targetRevision, destination)."
lang: "fr"
date_ajout: "2026-11"
nom: "GitOps avancé avec Argo CD : ApplicationSet, sync waves"
emoji: "🌌"
domaine: "Développement"
signal: "Passer au GitOps avancé avec Argo CD au-delà du basic (1704) : ApplicationSet (génère des Applications depuis un template + générateurs : git dirs, clusters CAPI 1874, helm values) pour déployer la même app sur N environnements/clusters ; sync waves (déploiement ordonné : DB wave 0, API wave 1) ; progressive syncs (avec Argo Rollouts 1877) ; notifications (Slack 1761). N'utilise pas ApplicationSet sans template clair (dérive des apps)."
mot_cle: "Argo CD ApplicationSet générateurs git clusters helm template sync waves ordre déploiement progressive syncs Argo Rollouts notifications"
nom_court: "Argo CD avancé"
branche: "D16"
synonymes: ["ApplicationSet : déployer la même app sur 10 clusters/envs depuis un template (Argo CD)", "sync waves : la DB se déploie avant l'API (wave 0 puis wave 1)", "générateur clusters (CAPI 1874) : une Application par cluster automatiquement"]
cross_refs: [1704, 1877, 1874]
tags: ["2027"]
depends_on: [1704]
---

## 1879. 🌌 GitOps avancé avec Argo CD : ApplicationSet, sync waves

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : GitOps avancé avec Argo CD : ApplicationSet (templates + générateurs git/clusters pour N environnements), sync waves (ordre de déploiement), progressive syncs avec Argo Rollouts (1877).

**Quand l'utiliser (triggers)** :
- déployer la même app sur 10 clusters (CAPI 1874) : ApplicationSet + générateur clusters
- sync waves : base de données wave 0, API wave 1 (ordre garanti)
- progressive sync avec Argo Rollouts 1877 (canary auto par env)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme DevOps. Tu crées un ApplicationSet (template + générateur list/git/cluster), tu mets les sync waves (argocd.argoproj.io/sync-wave), et tu branches les progressive syncs sur les envs à risque. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Argo CD (1704) installé
- Les repos git + clusters cibles (CAPI 1874)
- Les Applications existantes

**Méthode** :
1. ApplicationSet : spec.generators (git directories ou cluster CAPI) + template (name, repo, targetRevision, destination).
2. Sync waves : annotation argocd.argoproj.io/sync-wave: '0' (DB) puis '1' (API) -> ordre garanti.
3. Progressive syncs : Argo Rollouts 1877 sur staging/prod (canary auto), manuel sur prod critique.
4. Notifications : Slack/email sur sync failed (1761).
5. Sealed Secrets 1856 pour les secrets dans les repos.

**Sorties attendues** :
- L'ApplicationSet déployant sur N envs/clusters
- Les sync waves ordonnés (DB avant API)
- Les progressive syncs actifs sur les envs à risque

**Exemple de prompt** :
> « App payment : ApplicationSet déploie sur dev/staging/prod (3 clusters CAPI) ; sync waves : migration BDD wave 0, API wave 1 ; staging en canary auto (1877), prod en manuel avec approbation. »

**Cas d'usage** : GitOps à l'échelle. S'articule avec skills 1704, 1877, 1874, 1761, 1856.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

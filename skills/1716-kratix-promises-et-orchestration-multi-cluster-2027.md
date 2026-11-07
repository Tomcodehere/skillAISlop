---
num: 1716
date_ajout: "2026-11"
nom: "Kratix : promises et orchestration multi-cluster (2027)"
emoji: "🧩"
domaine: "Développement"
signal: "Orchestrer l'infra sur plusieurs clusters/environnements en 2027 avec Kratix (open source, CNCF sandbox) : des 'Promises' (ex. 'redis managé', 'environment prod') sont des contrats d'infra ; Kratix les réalise sur chaque cluster cible (state stores S3/Git), avec workflow de livraison (GitOps 1704). Alternative : Crossplane (1703) + Argo. Utilise quand plus de 3 clusters/env à gérer. N'utilise pas pour un seul cluster (Crossplane suffit)."
mot_cle: "kratix promises orchestration multi-cluster 2027 CNCF promise state store workflow gitops 1704"
nom_court: "Kratix"
branche: "D16"
synonymes: ["une 'promise' Kratix = contrat d'infra (redis, env prod) réalisé sur chaque cluster", "Kratix + state store S3 : la promise se propage sur 10 clusters", "Kratix vs Crossplane : multi-cluster (Kratix) vs single (Crossplane 1703)"]
cross_refs: [1703, 1704, 609]
tags: ["2027"]
depends_on: [1703]
---

## 1716. 🧩 Kratix : promises et orchestration multi-cluster (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Orchestrer l'infra sur N clusters en 2027 avec Kratix (CNCF sandbox) : des Promises (contrats : 'redis managé', 'environnement prod') publiées dans un state store (S3/Git), réalisées automatiquement sur chaque cluster cible, avec workflow GitOps (1704).

**Quand l'utiliser (triggers)** :
- gérer la même config sur 10 clusters à la main, stop
- Kratix promise 'environment dev' : déployée automatiquement sur les 10 clusters
- state store S3 : la source de vérité des promises, clusters = consommateurs

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform engineer multi-cluster. Tu installes Kratix sur un cluster 'hub', tu définis les Promises (CRD + workflow qui génère les manifests), les publies dans le state store (S3), et les clusters 'workers' les consomment et appliquent (GitOps 1704). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les clusters cibles (dev/staging/prod x régions)
- Le state store (S3 ou Git)
- Les promises à offrir (redis, postgres, env, monitoring)

**Méthode** :
1. Cluster hub : Kratix installé, state store configuré (S3 bucket + credentials 1656).
2. Définir une Promise (ex. 'redis') : CRD (apiVersion, kind, spec) + workflow (container qui génère les manifests redis + config).
3. Publier la promise dans le state store → tous les clusters workers la voient.
4. Workers : Kratix agent lit le state store, applique les manifests générés, rapporte le statut (OK/drift) au hub.
5. GitOps : les resources-request des devs (1 claim = 1 promise) passent par Git (1704), review (1401).
6. Drift : si un worker dévie, Kratix resync automatiquement.

**Sorties attendues** :
- Kratix hub + workers opérationnels (promise déployée sur N clusters)
- La promise 'redis' publiée et appliquée partout avec statut remonté
- Le workflow GitOps (1704) + review (1401) sur les resource requests

**Exemple de prompt** :
> « La même config doit exister sur 10 clusters (dev/staging/prod × régions) : déploie Kratix (hub + state store S3 + workers), publie une Promise 'redis managé' → déployée automatiquement partout avec statut remonté au hub, drift resync auto. »

**Cas d'usage** : Multi-cluster/multi-env. S'articule avec skills 1703 (Crossplane), 1704 (GitOps), 609 (k8s) et 1701 (golden paths).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

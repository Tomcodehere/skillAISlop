---
num: 1412
resume: "Déployer une app sur Kubernetes en 2027 : manifestes (Deployment, Service, Ingress), ConfigMap (config) et Secret (credentials), sondes et limites de ressources, avec rollback. Étape 1 : Écrire le Deployment (image, replicas, sondes, resources)."
lang: "fr"
date_ajout: "2026-11"
nom: "Kubernetes : ConfigMaps, secrets et deploiement"
emoji: "☸️"
domaine: "Développement"
signal: "Déployer sur Kubernetes en 2027 : manifestes YAML (Deployment, Service, Ingress), ConfigMaps pour la config, Secrets pour les credentials, sondes liveness/readiness, limites de ressources. Utilise quand on met une app sur un cluster K8s. N'utilise pas en local (voir Docker)."
mot_cle: "kubernetes deployment configmap secret manifests"
nom_court: "K8s deploy"
branche: "D16"
synonymes: ["déployer sur kubernetes", "manifests yaml k8s", "configmap secret k8s 2027"]
cross_refs: [609, 614, 85]
tags: ["2027"]
depends_on: [609]
---

## 1412. ☸️ Kubernetes : ConfigMaps, secrets et deploiement (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer une app sur Kubernetes en 2027 : manifestes (Deployment, Service, Ingress), ConfigMap (config) et Secret (credentials), sondes et limites de ressources, avec rollback.

**Quand l'utiliser (triggers)** :
- Écrire mon premier Deployment Kubernetes
- ConfigMap vs Secret : que mettre où ?
- Sondes liveness/readiness et resources limits

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es opérateur Kubernetes. Tu fournis les manifestes types (Deployment + sondes, Service, Ingress TLS), la règle ConfigMap=config / Secret=credentials (jamais en clair dans git), et kubectl apply + rollout. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'image Docker de l'app
- La config par environnement
- Les secrets (DB, clés API)
- Le domaine/ingress TLS

**Méthode** :
1. Écrire le Deployment (image, replicas, sondes, resources).
2. Créer ConfigMap (config) et Secret (credentials, kubectl --dry-run ou SOPS).
3. Exposer via Service + Ingress (TLS Let's Encrypt).
4. Appliquer (kubectl apply -f), vérifier (pods, rollout status).
5. Prévoir le rollback (kubectl rollout undo).

**Sorties attendues** :
- Les manifestes K8s appliqués
- ConfigMap/Secret gérés proprement
- Le déploiement vérifié + procédure de rollback

**Exemple de prompt** :
> « Déploie mon app Node sur notre cluster K8s : écris les manifestes (Deployment + Service + Ingress TLS, ConfigMap, Secret, sondes, limits) et les commandes kubectl. »

**Cas d'usage** : Mise en production, scaling, haute dispo. S'articule avec skills 609 (opérateur K8s), 614 (pré-déploiement) et 85 (IaC).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

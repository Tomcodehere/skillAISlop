---
num: 1801
date_ajout: "2026-11"
nom: "Gateway API : remplacer ingress-nginx"
emoji: "🚪"
domaine: "Développement"
signal: "Migrer ingress-nginx (retiré du projet Kubernetes le 24 mars, plus de maintenance) vers la Gateway API en 2027 : GatewayClass + Gateway + HTTPRoute (routage par path/host/header, TLS, poids entre backends). Implémentations : NGINX Gateway Fabric, Cilium, Traefik, Istio, Contour. Utilise pour toute nouvelle entrée HTTP. N'utilise pas Ingress (API figée) pour du nouveau."
mot_cle: "Gateway API HTTPRoute GatewayClass remplacer ingress-nginx retrait mars Traefik Cilium NGINX Gateway Fabric"
nom_court: "Gateway API"
branche: "D16"
synonymes: ["migrer ingress-nginx vers la Gateway API (HTTPRoute Gateway)", "ingress-nginx est retiré du projet Kubernetes : quoi mettre à la place", "HTTPRoute routage avancé path host header TLS poids backends"]
cross_refs: [609, 1412, 1705]
tags: ["2027"]
depends_on: [609]
---

## 1801. 🚪 Gateway API : remplacer ingress-nginx

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Migrer les Ingress vers la Gateway API (GatewayClass/Gateway/HTTPRoute) après le retrait d'ingress-nginx (24 mars), avec routage avancé (path, host, headers, poids, TLS) via NGINX Gateway Fabric, Cilium, Traefik ou Istio.

**Quand l'utiliser (triggers)** :
- ingress-nginx n'est plus maintenu, par quoi le remplacer ?
- HTTPRoute avec 2 backends en poids 90/10 pour un canary
- TLS auto sur HTTPRoute via Gateway

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme k8s. Tu inventories les Ingress existants, tu choisis l'implémentation Gateway (NGINX Gateway Fabric si tu viens d'ingress-nginx, Cilium si eBPF 1721, Traefik/Istio sinon), et tu convertis Ingress -> HTTPRoute avec tests de non-régression. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'inventaire des Ingress du cluster
- L'implémentation Gateway choisie (GatewayClass)
- Les certificats TLS (cert-manager 1871)

**Méthode** :
1. Installer le contrôleur Gateway (GatewayClass + Gateway dans le namespace infra).
2. Convertir chaque Ingress en HTTPRoute (mêmes règles path/host, backendRefs avec poids pour le canary).
3. Ajouter TLS via Gateway (certificats automatiques cert-manager).
4. Tester : curl sur chaque route, vérifier 200 et headers, puis supprimer les Ingress legacy.
5. Monitorer : métriques du contrôleur, alertes 1417 si erreur 5xx en hausse.

**Sorties attendues** :
- Les HTTPRoute déployées à la place des Ingress
- Le GatewayClass/Gateway documenté
- Le plan de rollback (Ingress conservés 1 release)

**Exemple de prompt** :
> « Ingress api.example.com (/v1 -> api:8080) devient Gateway main + HTTPRoute api-routes avec hostnames api.example.com, path /v1, backendRef api:8080 — test curl OK, puis suppression de l'Ingress. »

**Cas d'usage** : Clusters 10+ services, canary par poids. S'articule avec skills 609 (k8s), 1412 (secrets), 1705 (Kyverno), 1721 (Cilium), 1871 (cert-manager).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

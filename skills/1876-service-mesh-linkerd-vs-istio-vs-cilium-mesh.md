---
num: 1876
date_ajout: "2026-11"
nom: "Service mesh : Linkerd vs Istio (vs Cilium mesh)"
emoji: "🕸️"
domaine: "Développement"
signal: "Choisir un service mesh en 2027 : Linkerd (léger, simple, perf, CNCF graduated, sidecar proxy Rust-like rapide) vs Istio (complet mais complexe, beaucoup de CRDs, perf) vs Cilium service mesh (eBPF, sans sidecar — cf 1727). Critères : besoin mTLS entre services, traffic splitting (canary 1418), observabilité (1722 Hubble), complexité ops. Règle : si Cilium déjà là — mesh Cilium (1727) ; besoin simple mTLS+metrics — Linkerd ; besoins avancés (authz fine, multi-cluster) — Istio."
mot_cle: "service mesh Linkerd vs Istio vs Cilium eBPF sans sidecar mTLS traffic splitting canary observabilité complexité ops choisir"
nom_court: "Service mesh"
branche: "D16"
synonymes: ["Linkerd (léger, simple) vs Istio (complet, complexe) : lequel en 2027", "Cilium service mesh sans sidecar (eBPF 1721/1727) si Cilium déjà déployé", "mTLS automatique entre services + traffic splitting pour canary 1418"]
cross_refs: [1727, 1721, 1418]
tags: ["2027"]
depends_on: [1727]
---

## 1876. 🕸️ Service mesh : Linkerd vs Istio (vs Cilium mesh)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir son service mesh : Linkerd (léger/simple), Istio (complet/complexe) ou Cilium mesh sans sidecar (eBPF, si Cilium déjà là 1727) — selon mTLS, traffic splitting, observabilité et complexité ops.

**Quand l'utiliser (triggers)** :
- mTLS automatique entre tous les services sans toucher au code
- Linkerd vs Istio : lequel pour une équipe de 5 devs
- Cilium déjà déployé (1721) : prendre le mesh Cilium (1727) sans sidecar

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme. Tu évalues le besoin réel (mTLS ? authz fine ? multi-cluster ?) et tu choisis : Cilium mesh (1727) si eBPF déjà là, Linkerd si simple, Istio si avancé — et tu mesures l'overhead (latence, ressources). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cluster + Cilium présent ou non (1721)
- Les besoins (mTLS, canary, authz)
- La taille de l'équipe ops

**Méthode** :
1. Si Cilium (1721) : activer le mesh Cilium (1727) — 0 sidecar, eBPF.
2. Sinon si besoin simple (mTLS + metrics + canary) : Linkerd (helm, CRD simples).
3. Si besoins avancés (authz par path/method, multi-cluster, gateway) : Istio.
4. Mesurer : latence p99 ajoutée, mémoire sidecar, complexité (nb CRDs).

**Sorties attendues** :
- Le mesh choisi et déployé
- Le benchmark d'overhead (latence/ressources)
- La doc de décision (3 options)

**Exemple de prompt** :
> « Cluster avec Cilium (1721) : mesh Cilium (1727) activé — mTLS entre services en eBPF, 0 sidecar, latence +0,3 ms vs Linkerd +2 ms avec sidecar ; canary 1418 via Cilium's traffic splitting. »

**Cas d'usage** : Mesh k8s. S'articule avec skills 1727, 1721, 1418, 1416, 609.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1727
date_ajout: "2026-11"
nom: "Cilium service mesh sans sidecar"
emoji: "🕸️"
domaine: "Développement"
signal: "Remplacer le sidecar Envoy (Istio/Linkerd) par Cilium Service Mesh en 2027 : mTLS, L7 routing, retries, circuit breaker, observabilité — tout en eBPF dans le noyau (pas de proxy dans chaque pod, -50 % de ressources, latence en moins ~30 %). Utilise quand le coût des sidecars pèse (gros cluster). N'utilise pas si le kernel est trop vieux (1720) ou si vous avez déjà un mesh qui marche."
mot_cle: "cilium service mesh sans sidecar 2027 eBPF mTLS L7 routing retries -50% ressources vs istio linkerd envoy"
nom_court: "Mesh eBPF"
branche: "D16"
synonymes: ["supprimer les sidecars Envoy (Istio) : Cilium Service Mesh eBPF (-50 % ressources)", "mTLS automatique entre pods sans rien configurer (Cilium)", "L7 routing (retries, circuit breaker) dans le noyau, pas dans un proxy"]
cross_refs: [1721, 609, 1655]
tags: ["2027"]
depends_on: [1721]
---

## 1727. 🕸️ Cilium service mesh sans sidecar (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer un service mesh sans sidecar en 2027 avec Cilium Service Mesh (eBPF dans le noyau) : mTLS auto, L7 routing (retries, circuit breaker), observabilité (Hubble 1722) — -50 % de ressources et ~30 % de latence en moins vs Istio/Linkerd avec sidecars.

**Quand l'utiliser (triggers)** :
- nos sidecars Envoy consomment 30 % des ressources du cluster
- mTLS automatique pod-à-pod sans rien déployer (Cilium)
- retries + circuit breaker en L7 sans proxy dans chaque pod

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte réseau k8s. Tu actives Cilium Service Mesh (1721) : mTLS auto entre workloads (identités Cilium), L7 policies (HTTP/gRPC : retries, timeout, circuit breaker), et tu mesures le gain vs l'ancien mesh à sidecars. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Cilium déployé (1721)
- Le mesh actuel (Istio/Linkerd) ou aucun
- Les besoins (mTLS, L7, obs)

**Méthode** :
1. Activer : cilium clustermesh / service mesh enable (Cilium 1.16+), mTLS auto par défaut (identités Cilium, pas de certs à gérer).
2. L7 : CiliumEnvoyConfig ou CiliumNetworkPolicy L7 (HTTP retries, timeouts, circuit breaker, header routing).
3. Migration : depuis Istio/Linkerd, déplacer progressivement (dual-run temporaire), mesurer la conso (sidecars supprimés).
4. Observabilité : Hubble (1722) voit tout le trafic mesh (mTLS, L7).
5. Benchmark : latence p99 et conso mémoire/CPU par pod avant/après (objectif -50 % ressources, -30 % latence).

**Sorties attendues** :
- Le service mesh eBPF actif (mTLS auto, L7 routing, sans sidecar)
- Les sidecars Envoy supprimés et le gain mesuré (-50 % ressources)
- Hubble (1722) montrant le trafic mesh chiffré

**Exemple de prompt** :
> « Nos sidecars Envoy coûtent 30 % du cluster : active Cilium Service Mesh (1721, eBPF sans sidecar) — mTLS auto, retries/circuit breaker L7, supprime les sidecars, mesure -50 % de ressources et -30 % de latence, Hubble (1722) pour le trafic. »

**Cas d'usage** : Gros clusters k8s avec mesh. S'articule avec skills 1721 (Cilium), 609 (k8s), 1655 (SPIFFE) et 1722 (Hubble).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

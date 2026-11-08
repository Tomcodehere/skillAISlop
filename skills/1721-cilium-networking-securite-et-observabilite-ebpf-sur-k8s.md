---
num: 1721
date_ajout: "2026-11"
nom: "Cilium : networking, sécurité et observabilité eBPF sur k8s"
emoji: "🌐"
domaine: "Développement"
signal: "Remplacer kube-proxy/iptables par Cilium en 2027 (CNI eBPF, 64 % des clusters k8s en 2026) : dataplane eBPF (+30-40 % de débit vs iptables), NetworkPolicy L3-L7 (HTTP method/path, Kafka topic, gRPC), mTLS automatique, Hubble (observabilité flux avec identités), Cilium Service Mesh sans sidecar (-50 % de ressources). Certification CCAE dispo. N'utilise pas si le kernel est trop vieux (1720)."
mot_cle: "cilium CNI eBPF kubernetes 2027 +30-40% débit vs iptables NetworkPolicy L7 Hubble service mesh sans sidecar CCAE"
nom_court: "Cilium"
branche: "D16"
synonymes: ["remplacer kube-proxy/iptables par Cilium (eBPF) en 2027", "Cilium NetworkPolicy L7 : filtrer sur méthode HTTP path header", "Hubble : carte des flux réseau en temps réel + Cilium service mesh sans sidecar -50%"]
cross_refs: [609, 1720, 1132]
tags: ["2027"]
depends_on: [609]
---

## 1721. 🌐 Cilium : networking, sécurité et observabilité eBPF sur k8s (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer Cilium en 2027 comme CNI k8s (64 % des clusters en 2026) : dataplane eBPF (remplace kube-proxy, +30-40 % de débit), NetworkPolicy L3-L7, mTLS auto, Hubble (observabilité des flux), service mesh sans sidecar (-50 % de ressources).

**Quand l'utiliser (triggers)** :
- les règles iptables explosent avec 1000 pods (perf dégradée)
- Cilium : NetworkPolicy qui filtre sur la méthode HTTP et le path
- Hubble : voir en temps réel quel pod parle à quel pod (service map)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur réseau k8s. Tu installes Cilium (cilium CLI / helm) en remplaçant le CNI existant, tu actives Hubble (observabilité), tu écris des CiliumNetworkPolicy L7, et tu mesures le gain de perf vs iptables. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cluster k8s (609) et son CNI actuel
- Le kernel des nœuds (5.8+, 1720)
- Les besoins (perf, policies L7, observabilité)

**Méthode** :
1. Vérifier kernel 5.8+ sur tous les nœuds (1720). Nouveaux clusters : Cilium direct. Existants : plan de migration documenté (heures creuses).
2. Installer : cilium CLI (cilium install) ou helm, remplacer kube-proxy (mode eBPF).
3. Vérifier : cilium status, health, et un pod test (connectivité pod-to-pod).
4. NetworkPolicy L7 : CiliumNetworkPolicy (http: method GET path /api/v1/*, kafka topic, dns).
5. Hubble : cilium hubble enable + UI/CLI (flux L3-L7 avec identités de workload, filtres DNS/protocole).
6. Service mesh sans sidecar : Cilium Service Mesh (mTLS, L7 routing, retries) — remplace Istio/Linkerd sidecars (-50 % ressources).
7. Mesurer : débit (+30-40 % vs iptables), latence, conso CPU du dataplane. Certification CCAE pour les ops.

**Sorties attendues** :
- Cilium déployé (CNI eBPF, kube-proxy remplacé) avec statut OK
- Les CiliumNetworkPolicy L7 + Hubble (service map temps réel) actifs
- Le benchmark +30-40 % débit vs iptables mesuré

**Exemple de prompt** :
> « Nos règles iptables dégradent le réseau avec 1000 pods : migre vers Cilium (CNI eBPF, kube-proxy remplacé), CiliumNetworkPolicy L7 (HTTP method/path), Hubble (service map temps réel), benchmark +30-40 % de débit mesuré. »

**Cas d'usage** : Kubernetes cloud-native. S'articule avec skills 609 (k8s), 1720 (eBPF), 1132 (firewall) et 1724 (Pixie).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

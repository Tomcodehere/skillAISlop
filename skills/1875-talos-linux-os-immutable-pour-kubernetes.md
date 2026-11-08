---
num: 1875
date_ajout: "2026-11"
nom: "Talos Linux : OS immutable pour Kubernetes"
emoji: "🏗️"
domaine: "Développement"
signal: "Faire tourner k8s sur Talos Linux (OS immutable, API-only, pas de shell SSH, pas de package manager) : surface d'attaque minimale, boot rapide, config déclarative (machineconfig), mises à jour atomiques (A/B partitions), support CAPI (1874). Alternative : Flatcar (CoreOS), Bottlerocket (AWS). Idéal pour les clusters prod sécurisés et automatisés. N'utilise pas si tu as besoin de debug interactif en shell (Talos a talosctl mais pas de shell persistant)."
mot_cle: "Talos Linux OS immutable API-only pas de shell k8s machineconfig mises à jour atomiques A/B CAPI Flatcar Bottlerocket CoreOS"
nom_court: "Talos"
branche: "D16"
synonymes: ["OS immutable pour k8s : Talos (API-only, pas de shell) vs Flatcar vs Bottlerocket", "mise à jour atomique A/B de Talos : rollback en 1 commande si boot échoue", "Talos + CAPI 1874 : provisionner un cluster Talos déclaratif"]
cross_refs: [1874, 609, 1852]
tags: ["2027"]
depends_on: [609]
---

## 1875. 🏗️ Talos Linux : OS immutable pour Kubernetes

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire tourner Kubernetes sur Talos Linux (OS immutable, API-only, config déclarative machineconfig, mises à jour atomiques A/B) — surface d'attaque minimale, intégration CAPI (1874).

**Quand l'utiliser (triggers)** :
- nos nœuds k8s ont un shell SSH et des paquets installés à la main : passer à Talos (immutable)
- mise à jour Talos atomique : boot fail -> rollback auto sur l'autre partition
- talosctl : opérer le nœud sans SSH (API mTLS)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme / SRE. Tu génères la machineconfig (controlplane/worker), tu boot les nœuds Talos, tu les joins au cluster (CAPI 1874 ou kubeadm), et tu documentes talosctl (pas de shell). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les nœuds (VM/bare metal/cloud)
- La machineconfig (Talos)
- CAPI 1874 ou kubeadm

**Méthode** :
1. Générer la config : talosctl gen config cluster-name https://controlplane:6443 -> patchs (CNI cilium 1721, certificats).
2. Booter les nœuds (ISO Talos), appliquer la machineconfig (talosctl apply-config).
3. Rejoindre le cluster : CAPI (1874) pour le provisionnement auto, ou kubeadm manuel.
4. Upgrade : talosctl upgrade (atomique A/B, rollback auto si boot échoue) ; pas de shell, pas de paquets.

**Sorties attendues** :
- Les nœuds Talos en cluster (immutable, API-only)
- L'upgrade atomique testé (rollback)
- Le provisionnement CAPI 1874 fonctionnel

**Exemple de prompt** :
> « Cluster prod 10 nœuds : Talos + Cilium (1721) — 0 shell SSH, 0 paquet installé à la main, surface CVE réduite (scan 1826 : -80 % vs Ubuntu) ; upgrade 1.36->1.37 en rolling atomique, rollback auto testé. »

**Cas d'usage** : K8s sécurisé immutable. S'articule avec skills 1874, 609, 1852, 1851.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

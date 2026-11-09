---
num: 1810
resume: "Déployer Karpenter pour provisionner automatiquement les nœuds adaptés aux pods pending (taille/GPU/zone) et consolider les nœuds sous-utilisés, réduisant la facture cloud (spot vs on-demand). Étape 1 : Installer Karpenter + le provider cloud (eks/aro/gke)."
date_ajout: "2026-11"
nom: "Karpenter : autoscaling de nœuds et consolidation"
emoji: "🚀"
domaine: "Développement"
signal: "Remplacer/supplémenter le cluster-autoscaler par Karpenter en 2027 : il provisionne les nœuds adaptés aux pods pending (taille, GPU via DRA 1802, zone), consolide automatiquement les nœuds sous-utilisés (bin-packing) pour réduire la facture cloud, gère spot vs on-demand. NodePool + NodeClaim. Métriques : temps de scheduling, coût/nœud. N'utilise pas si tu as des contraintes de nœuds très spécifiques non modélisables (NodeAffinity complexe)."
mot_cle: "Karpenter autoscaling nœuds NodePool NodeClaim consolidation bin-packing spot on-demand GPU DRA coût"
nom_court: "Karpenter"
branche: "D16"
synonymes: ["provisionner automatiquement le bon nœud pour un pod pending (Karpenter vs cluster-autoscaler)", "consolidation automatique des nœuds sous-utilisés pour réduire la facture", "NodePool GPU spot vs on-demand avec Karpenter"]
cross_refs: [609, 1802, 1862]
tags: ["2027"]
depends_on: [609]
---

## 1810. 🚀 Karpenter : autoscaling de nœuds et consolidation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer Karpenter pour provisionner automatiquement les nœuds adaptés aux pods pending (taille/GPU/zone) et consolider les nœuds sous-utilisés, réduisant la facture cloud (spot vs on-demand).

**Quand l'utiliser (triggers)** :
- un pod est pending 10 min faute de nœud : Karpenter le provisionne en 30 s
- trop de nœuds à moitié vides le week-end : consolidation auto
- NodePool GPU pour les jobs ML (DRA 1802)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme cloud. Tu définis des NodePool (contraintes : instance types, zones, GPU, spot/on-demand, taints), tu actives la consolidation (consolidationPolicy: WhenUnderutilized), et tu suis coût/nœud et temps de scheduling. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cloud provider (AWS/GCP/Azure) + credentials
- Les besoins des pods (requests, GPU, tolérations)
- Le budget (mix spot/on-demand)

**Méthode** :
1. Installer Karpenter + le provider cloud (eks/aro/gke).
2. Définir les NodePool : instance types adaptés, zones, labels GPU (DRA 1802), budget spot.
3. Consolidation WhenUnderutilized : Karpenter vide et supprime les nœuds sous-utilisés (respect PDB 1805).
4. Métriques : karpenter_cloudprovider_instance_type_count, temps de scheduling pod->nœud, coût total (1862).

**Sorties attendues** :
- Les NodePool déployés (général + GPU + spot)
- La consolidation active (nœuds supprimés quand vides)
- Le dashboard coût/nœud et temps de scheduling

**Exemple de prompt** :
> « Batch nightly : 40 pods pending à 20h, Karpenter provisionne 5 nœuds spot en 40 s (vs 10 min de pending avec cluster-autoscaler), puis les consolide et supprime à 6h — économie 60 % sur le batch. »

**Cas d'usage** : Clusters cloud dynamiques. S'articule avec skills 609, 1802 (DRA GPU), 1862 (coût k8s), 1416, 1700.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

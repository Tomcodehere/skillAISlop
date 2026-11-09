---
num: 1862
resume: "Allouer les coûts Kubernetes (nœuds, PVC, egress réseau) par namespace/workload avec OpenCost/Kubecost/CAST.ai, sur la base des consommations réelles (pas des requests déclarés), pour du rightsizing (1803). Étape 1 : Déployer OpenCost (helm, namespace opencost) — scrape les métriques cloud + k8s."
lang: "fr"
date_ajout: "2026-11"
nom: "FinOps Kubernetes : allocation des coûts par namespace et workload"
emoji: "⚙️"
domaine: "Gestion"
signal: "Allouer les coûts k8s (nœuds, PVC, trafic réseau) par namespace/label/workload avec OpenCost (CNCF, ex-Kubecost OSS) ou Kubecost/CAST.ai : cost modèle = nœuds (Karpenter 1810) + stockage + réseau egress, réparti selon requests/limits réels (pas déclarés). Rightsizing via VPA (1803) + PSI (1806). N'utilise pas les requests déclarés seuls (souvent surdimensionnés)."
mot_cle: "coût kubernetes par namespace workload OpenCost Kubecost CAST.ai allocation nœuds PVC egress requests réels VPA PSI rightsizing"
nom_court: "Coût k8s"
branche: "D25"
synonymes: ["combien coûte le namespace prod ce mois-ci ? (OpenCost/Kubecost allocation)", "mes requests sont à 30 % du réel : rightsizing VPA 1803 + PSI 1806", "coût réseau egress entre namespaces (Cilium Hubble 1722)"]
cross_refs: [1861, 1870, 1803]
tags: ["2027"]
depends_on: [1861]
---

## 1862. ⚙️ FinOps Kubernetes : allocation des coûts par namespace et workload

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Allouer les coûts Kubernetes (nœuds, PVC, egress réseau) par namespace/workload avec OpenCost/Kubecost/CAST.ai, sur la base des consommations réelles (pas des requests déclarés), pour du rightsizing (1803).

**Quand l'utiliser (triggers)** :
- facture cloud +40 % : quels namespaces coûtent le plus ?
- OpenCost vs Kubecost vs CAST.ai : lequel déployer
- rightsizing : comparer requests déclarés vs usage réel (PSI 1806)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es FinOps / SRE plateforme. Tu déploies OpenCost (helm) ou Kubecost, tu branches les métriques nœuds (Karpenter 1810) + PVC + egress (Hubble 1722), et tu produis le rapport coût/namespace/équipe. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cluster k8s + métriques nœuds
- OpenCost/Kubecost/CAST.ai
- Les labels d'allocation (équipe/produit)

**Méthode** :
1. Déployer OpenCost (helm, namespace opencost) — scrape les métriques cloud + k8s.
2. Allocation : par namespace, label (app/team), workload, pod ; coûts nœuds selon le provider (prix réel), PVC selon classe, egress réseau.
3. Rightsizing : rapport requests vs usage réel (PSI 1806) -> VPA recommande (1803).
4. Chargeback : exporter vers FOCUS (1861) ou le dashboard (1766) par équipe (1870).

**Sorties attendues** :
- Le dashboard coût par namespace/équipe/workload
- Le rapport rightsizing (requests vs réel)
- L'export FOCUS (1861) alimenté

**Exemple de prompt** :
> « Namespace 'data-pipelines' = 35 % de la facture k8s : OpenCost montre des pods à 8 CPU demandés, 1,2 utilisés réellement (PSI 1806) -> VPA resize in-place (1803) -> -60 % sur ce namespace en 1 semaine. »

**Cas d'usage** : FinOps k8s. S'articule avec skills 1861, 1870, 1803, 1806, 1810, 1721.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

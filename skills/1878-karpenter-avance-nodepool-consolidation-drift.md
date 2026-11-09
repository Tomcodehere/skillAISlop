---
num: 1878
resume: "Maîtriser Karpenter : NodePool multiples (général/GPU/spot/ARM) avec weight, consolidation WhenUnderutilized, drift detection (remplacement auto des nœuds non conformes), disruption budgets. Étape 1 : NodePool gpu : taints/labels gpu, instances p4/p5, DRA 1802 ; NodePool spot : instances spot, weight plus haut pour le batch."
date_ajout: "2026-11"
nom: "Karpenter avancé : NodePool, consolidation, drift"
emoji: "🔧"
domaine: "Développement"
signal: "Maîtriser Karpenter au-delà du basique (1810) : plusieurs NodePool (général, GPU 1802, spot, ARM/graviton, zones), weight/priorité entre pools, consolidation agressive (WhenUnderutilized vs WhenEmpty, consolidationPolicy), Drift (détection de nœuds non conformes : image, kubelet version — remplacement auto), disruption budgets (doNotDisrupt, PDB 1805). Métriques : savings réalisés vs cluster-autoscaler."
mot_cle: "Karpenter NodePool weight consolidation WhenUnderutilized drift doNotDisrupt PDB GPU spot ARM graviton savings métriques vs cluster-autoscaler"
nom_court: "Karpenter+"
branche: "D16"
synonymes: ["plusieurs NodePool Karpenter : général + GPU (DRA 1802) + spot, avec weight (priorité)", "consolidation WhenUnderutilized : vider et supprimer les nœuds sous-utilisés (économie)", "drift Karpenter : nœud non conforme (mauvaise image) — remplacé automatiquement"]
cross_refs: [1810, 1802, 1805]
tags: ["2027"]
depends_on: [1810]
---

## 1878. 🔧 Karpenter avancé : NodePool, consolidation, drift

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Maîtriser Karpenter : NodePool multiples (général/GPU/spot/ARM) avec weight, consolidation WhenUnderutilized, drift detection (remplacement auto des nœuds non conformes), disruption budgets.

**Quand l'utiliser (triggers)** :
- un NodePool GPU dédié (DRA 1802) + un NodePool spot pour le batch, weight pour prioriser
- consolidation agressive : -40 % de nœuds le week-end (WhenUnderutilized)
- drift : un nœud avec une vieille image -> Karpenter le remplace tout seul

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme cloud. Tu définis les NodePool par besoin (GPU/spot/ARM/général) avec weight, tu actives la consolidation et le drift, et tu suis les savings (1862) vs l'ancien cluster-autoscaler. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Karpenter (1810) installé
- Les besoins par workload (GPU, spot, ARM)
- Les contraintes (zones, PDB 1805)

**Méthode** :
1. NodePool gpu : taints/labels gpu, instances p4/p5, DRA 1802 ; NodePool spot : instances spot, weight plus haut pour le batch.
2. Consolidation : consolidationPolicy WhenUnderutilized (remplace WhenEmpty pour plus d'économies, avec PDB 1805).
3. Drift : activé par défaut — nœud non conforme (image, kubelet, labels) -> terminé et remplacé.
4. Disruption : karpenter.sh/do-not-disrupt + PDB ; métriques savings (1862).

**Sorties attendues** :
- Les NodePool spécialisés actifs (GPU/spot/ARM)
- La consolidation + drift actifs (nœuds non conformes remplacés)
- Les savings mesurés vs cluster-autoscaler (1862)

**Exemple de prompt** :
> « Batch nightly sur NodePool spot (weight 10) : Karpenter prend du spot d'abord (-70 % coût), fallback on-demand si pas de spot ; consolidation WhenUnderutilized vide les nœuds le dimanche -> -40 % de nœuds ce jour-là (rapport 1862). »

**Cas d'usage** : Optimisation avancée. S'articule avec skills 1810, 1802, 1805, 1862, 1806.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

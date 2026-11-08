---
num: 1805
date_ajout: "2026-11"
nom: "Preemption workload-aware et scheduling topologique"
emoji: "⏏️"
domaine: "Développement"
signal: "Protéger les workloads critiques de la préemption brutale avec le workload-aware preemption (k8s 1.36+) : la préemption évite désormais les pods de haute priorité (PDB, gang scheduling 1804) et choisit les victimes de plus basse priorité d'abord ; le topology-aware scheduling place les pods selon la topologie réelle (zone, nœud, GPU). N'utilise pas sans PDB sur les workloads critiques."
mot_cle: "workload-aware preemption topology-aware scheduling PDB priorité pods k8s 1.36"
nom_court: "Preemption aware"
branche: "D16"
synonymes: ["ma pod critique a été preempte par un batch : protéger avec PDB + workload-aware preemption", "placer les pods selon la topologie (zone, noeud, GPU) : topology-aware scheduling", "la preemption evite maintenant les pods gang scheduling"]
cross_refs: [609, 1804, 1802]
tags: ["2027"]
depends_on: [609]
---

## 1805. ⏏️ Preemption workload-aware et scheduling topologique

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Configurer le workload-aware preemption (1.36+) et le topology-aware scheduling pour que les workloads critiques (PDB) ne soient pas préemptés et que les pods soient placés selon la topologie réelle (zone/nœud/GPU).

**Quand l'utiliser (triggers)** :
- mon pod prod a été tué par un pod batch prioritaire
- protéger les pods ML gang (1804) de la préemption
- répartir les replicas sur les zones AZ (topology spread)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme k8s. Tu mets des PDB (minAvailable) sur tous les workloads critiques, tu actives le workload-aware preemption (les pods avec PDB/gang ne sont pas victimes), et tu utilises topologySpreadConstraints pour la répartition AZ. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les priorités de pods (PriorityClass)
- Les PDB des workloads critiques
- La topologie du cluster (zones, nœuds GPU)

**Méthode** :
1. Définir des PriorityClass (critique > batch).
2. PDB minAvailable sur chaque workload critique (API, BDD).
3. Workload-aware preemption : le scheduler choisit d'abord les pods batch basse priorité comme victimes, jamais les pods PDB/gang.
4. Topology-aware : topologySpreadConstraints maxSkew=1 par zone AZ.

**Sorties attendues** :
- Les PDB en place sur les workloads critiques
- 0 préemption de pods protégés constatée
- La répartition AZ conforme (maxSkew respecté)

**Exemple de prompt** :
> « Cluster avec PriorityClass batch-low : quand un pod critique manque de ressources, le scheduler preempte d'abord les pods batch (jamais l'API avec PDB minAvailable=2), et les replicas sont répartis maxSkew=1 sur 3 AZ. »

**Cas d'usage** : Clusters multi-AZ avec batch. S'articule avec skills 609, 1804, 1802, 1416.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

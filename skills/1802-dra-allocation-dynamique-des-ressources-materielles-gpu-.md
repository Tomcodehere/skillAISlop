---
num: 1802
resume: "Allouer dynamiquement GPU/FPGA aux pods avec DRA (ResourceClaim/ResourceSlice, GA 1.34, par défaut 1.36) : sélection par attributs avec fallback ordonné, devices partitionnables, taints et health status. Étape 1 : Installer le driver DRA vendor (ex. NVIDIA) qui publie les ResourceSlice par nœud."
lang: "fr"
date_ajout: "2026-11"
nom: "DRA : allocation dynamique des ressources matérielles (GPU, FPGA)"
emoji: "🧠"
domaine: "Développement"
signal: "Utiliser DRA (Dynamic Resource Allocation, GA depuis k8s 1.34, par défaut dans 1.36) pour allouer des GPU/FPGA aux pods via ResourceClaim + ResourceSlice (driver vendor : NVIDIA, AMD) : sélection par attributs (modèle H100/A100), préférences ordonnées avec fallback, devices partitionnables, taints/tolerations de devices, health status. Remplace les extended resources GPU. N'utilise pas pour CPU/mémoire standard (requests/limits suffisent)."
mot_cle: "DRA Dynamic Resource Allocation ResourceClaim ResourceSlice GPU FPGA partitionable taints health k8s"
nom_court: "DRA GPU"
branche: "D16"
synonymes: ["allouer un GPU H100 à un pod via ResourceClaim DRA k8s", "DRA vs extended resources nvidia.com/gpu : la différence", "preferences ordonnees H100 sinon A100 avec fallback DRA"]
cross_refs: [609, 1700, 1721]
tags: ["2027"]
depends_on: [609]
---

## 1802. 🧠 DRA : allocation dynamique des ressources matérielles (GPU, FPGA)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Allouer dynamiquement GPU/FPGA aux pods avec DRA (ResourceClaim/ResourceSlice, GA 1.34, par défaut 1.36) : sélection par attributs avec fallback ordonné, devices partitionnables, taints et health status.

**Quand l'utiliser (triggers)** :
- mon pod ML demande 2 GPU H100 avec fallback A100
- DRA vs nvidia.com/gpu extended resource : lequel choisir
- marquer un GPU en maintenance (DeviceTaintRule)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme ML/k8s. Tu remplaces les extended resources GPU par des ResourceClaim DRA (CEL pour les attributs), tu définis les préférences ordonnées (H100 puis A100), et tu surveilles le health status des devices. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le driver DRA du vendor (NVIDIA gpu-operator)
- Les modèles de GPU disponibles (ResourceSlice)
- Les besoins des workloads ML

**Méthode** :
1. Installer le driver DRA vendor (ex. NVIDIA) qui publie les ResourceSlice par nœud.
2. Déclarer un ResourceClaim dans le pod : attributs (model=H100), préférences ordonnées avec fallback.
3. Scheduler alloue le device, le pod démarre avec le device claim.
4. Gérer la maintenance : DeviceTaintRule marque le device unavailable, les pods sont préemptés proprement (1805).
5. Monitorer : utilization GPU par claim (metrics driver), health status.

**Sorties attendues** :
- Les ResourceClaim déployés avec fallback ordonné
- La cartographie GPU par nœud (ResourceSlice)
- Le runbook maintenance GPU (taint/preemption)

**Exemple de prompt** :
> « Pod training LLM : ResourceClaim avec preferences [H100, A100], 2 devices, partitionnable si dispo — le scheduler alloue 2x H100 sur gpu-worker-01, fallback A100 si plus de H100. »

**Cas d'usage** : Clusters GPU ML. S'articule avec skills 609 (k8s), 1700 (IDP), 1721 (Cilium), 1804 (gang scheduling).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

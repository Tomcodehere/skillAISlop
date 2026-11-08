---
num: 1874
date_ajout: "2026-11"
nom: "Cluster API (CAPI) : gérer des clusters k8s comme des ressources k8s"
emoji: "🖥️"
domaine: "Développement"
signal: "Provisionner et gérer le cycle de vie de clusters k8s avec Cluster API (CNCF) : un cluster k8s de management déclare des objets Cluster/Machine/MachineDeployment (comme des Deployments) — CAPI crée les VMs (providers : AWS CAPA, Azure CAPZ, GCP CAPG, vSphere...) et bootstrappe kubeadm. Upgrade déclaratif (version du control plane), autoscaling des MachineDeployments. N'utilise pas pour un seul cluster statique (EKS/GKE managé suffit)."
mot_cle: "Cluster API CAPI CNCF Cluster Machine MachineDeployment kubeadm CAPA CAPZ CAPG vSphere provider cycle de vie clusters k8s déclaratif upgrade"
nom_court: "Cluster API"
branche: "D16"
synonymes: ["créer un cluster k8s sur AWS avec CAPI (CAPA) comme une ressource k8s (Cluster + MachineDeployment)", "upgrade déclaratif du control plane k8s (CAPI : changer la version = changer le CR)", "CAPI vs EKS/GKE managé : quand CAPI (multi-cloud, on-prem, contrôle total)"]
cross_refs: [609, 1810, 1700]
tags: ["2027"]
depends_on: [609]
---

## 1874. 🖥️ Cluster API (CAPI) : gérer des clusters k8s comme des ressources k8s

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Provisionner et gérer des clusters k8s avec Cluster API (CAPI) : objets Cluster/MachineDeployment déclaratifs, providers cloud (CAPA/CAPZ/CAPG/vSphere), upgrade du control plane par changement de version.

**Quand l'utiliser (triggers)** :
- créer 5 clusters k8s identiques sur AWS : CAPI (CAPA) en déclaratif
- upgrade k8s 1.36 -> 1.37 : changer la version dans le CR Cluster (CAPI)
- CAPI vs EKS managé : quand CAPI (multi-cloud, on-prem, souveraineté)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme cloud. Tu déploies un cluster de management CAPI + le provider cloud (CAPA...), et tu déclares les clusters workers comme des ressources (Cluster + MachineDeployment). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Un cluster de management k8s
- Le provider CAPI (CAPA/CAPZ/CAPG/capv)
- Les credentials cloud (ESO 1854)

**Méthode** :
1. Installer CAPI sur le management cluster + le provider infra (ex. CAPA pour AWS) + bootstrap (kubeadm) + control plane (kubeadm).
2. Déclarer : Cluster (network, version) + MachineDeployment (instance type, replicas, autoscaling min/max via KEDA-like).
3. CAPI provisionne les VMs, bootstrappe kubeadm, joint le cluster.
4. Upgrade : changer spec.version du Cluster -> CAPI upgrade le control plane puis les nœuds (rolling).

**Sorties attendues** :
- Les clusters workers provisionnés en déclaratif
- L'upgrade de version testé (rolling)
- Le multi-cloud documenté (CAPA/CAPZ/CAPG)

**Exemple de prompt** :
> « 5 clusters identiques (dev/staging/prod x2 régions) : 5 MachineDeployments déclarés dans le management cluster CAPI — création en 10 min, upgrade 1.36->1.37 en changeant la version (rolling, 0 downtime). »

**Cas d'usage** : Fleets de clusters. S'articule avec skills 609, 1810, 1700, 1873.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

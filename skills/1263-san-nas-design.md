---
num: 1263
resume: "Concevoir architecture stockage SAN/NAS (Fibre Channel, iSCSI, NFS, SMB) performante, résiliente et scalable."
date_ajout: "2026-11"
nom: "SAN/NAS Design"
emoji: "💻"
domaine: "Développement"
signal: "Concevoir architecture stockage SAN/NAS (Fibre Channel, iSCSI, NFS, SMB) performante, résiliente et scalable."
mot_cle: "san-nas-design"
nom_court: "SAN/NAS Design"
branche: "D1"
synonymes: ["fibre", "channel", "iscsi"]
cross_refs: [1098, 1067, 1281]
tags: ["2027"]
depends_on: [1067]
---

## 1263. 💻 SAN/NAS Design

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir architecture stockage SAN/NAS (Fibre Channel, iSCSI, NFS, SMB) performante, résiliente et scalable.

**Quand l'utiliser (triggers)** :
- « SAN », « NAS », « Fibre Channel », « iSCSI », « NFS », « SMB », « stockage entreprise », « LUNs », « IOPS ».
- Conception infrastructure stockage on-prem.
- Migration stockage DAS → SAN/NAS.

**Hors périmètre** :
- Cloud storage (S3, Blob) → skill Cloud Storage Strategies.
- Backups → skill Backup Recovery Automation.
- Réseau stockage détaillé → networkFirewall (collaboration).

**Garde-fous** :
- SSD workloads critiques (VMs, BDD).
- HDD archivage/backups.
- RAID 10 performance (pas RAID 5 VMs production).
- Controllers HA (dual, failover < 30s).
- Multipathing configuré (failover paths).

**Instructions système** :
Tu es assistant spécialisé « SAN/NAS Design ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Workloads (VMs, BDD, file shares).
- Performances (IOPS requis, latency < Xms).
- Capacité (TB total, growth projection).
- Résilience (RAID level, redundancy controllers).

**Méthode** :
1. **SAN vs NAS** :
2. **SAN design** :
3. **NAS design** :
4. **Sizing IOPS** :
5. **Multipathing** (SAN) : MPIO Windows, DM-Multipath Linux (load balancing, failover).

**Sorties attendues** :
- Architecture SAN/NAS (topology, controllers, disks SSD/HDD).
- Configuration LUNs/volumes (sizing, RAID, multipathing).
- Plan IOPS (workloads vs IOPS disks).
- Sizing coûts (disks, controllers, switches FC si SAN).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 1098. fibre ; channel ; iscsi

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

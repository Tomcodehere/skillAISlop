---
num: 1880
resume: "Protéger le cluster k8s : backups Velero (ressources + volumes CSI -supérieur à S3, restore cross-cluster/région) + snapshots etcd réguliers, avec tests de restore (game day 1769) et RTO/RPO définis. Étape 1 : Déployer Velero (helm) pointant sur S3 (credentials via Vault/ESO 1854) ; schedule quotidien, retention 30 j, backup des volumes CSI (snapshot)."
date_ajout: "2026-11"
nom: "Backup et reprise après sinistre Kubernetes (Velero, etcd)"
emoji: "💾"
domaine: "Sécurité"
signal: "Protéger un cluster k8s contre la perte totale : Velero (backup des ressources k8s + volumes CSI persistants — S3, restore dans un autre cluster/région, backup planifiés, retention) + snapshots etcd réguliers (etcdctl snapshot) + test de restore régulier (game day 1769). RTO/RPO définis (ex. RPO 1 h, RTO 30 min). N'utilise pas sans test de restore (un backup non testé = pas de backup)."
mot_cle: "Velero backup restore cluster k8s volumes CSI S3 snapshot etcd etcdctl RTO RPO game day restore test cross-region disaster recovery"
nom_court: "Backup k8s/DR"
branche: "D23"
synonymes: ["backuper tout le cluster k8s (ressources + volumes) avec Velero vers S3", "restore dans un autre cluster/région : tester régulièrement (game day 1769)", "snapshot etcd régulier (etcdctl snapshot save) + vérification (snapshot status)"]
cross_refs: [1769, 1758, 609]
tags: ["2027"]
depends_on: [609]
---

## 1880. 💾 Backup et reprise après sinistre Kubernetes (Velero, etcd)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Protéger le cluster k8s : backups Velero (ressources + volumes CSI -> S3, restore cross-cluster/région) + snapshots etcd réguliers, avec tests de restore (game day 1769) et RTO/RPO définis.

**Quand l'utiliser (triggers)** :
- ransomware a chiffré etcd : restore depuis snapshot etcd + Velero
- RPO 1 h RTO 30 min : définir et tester le plan de reprise (1769)
- backup Velero planifié quotidien + retention 30 j vers S3

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / responsable continuité. Tu déploies Velero (backup S3, schedule quotidien, retention), tu snapshot etcd régulièrement, et tu testes le restore en game day (1769) avec mesure RTO réelle. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Velero + un bucket S3 (credentials ESO 1854)
- etcdctl accès
- Le cluster cible pour le restore (CAPI 1874)

**Méthode** :
1. Déployer Velero (helm) pointant sur S3 (credentials via Vault/ESO 1854) ; schedule quotidien, retention 30 j, backup des volumes CSI (snapshot).
2. Snapshots etcd : etcdctl snapshot save régulier + vérification (snapshot status) + copie off-cluster.
3. Restore : velero restore create (dans un cluster neuf CAPI 1874) ; mesurer le RTO réel.
4. Game day (1769) : simuler la perte totale, restore, mesurer RTO vs objectif 30 min, corriger.

**Sorties attendues** :
- Les backups Velero planifiés (quotidiens) + snapshots etcd
- Le restore testé en game day (RTO mesuré)
- Le plan de reprise documenté (RPO/RTO)

**Exemple de prompt** :
> « Game day : suppression simulée du cluster prod -> restore Velero dans un cluster neuf (CAPI 1874) en 22 min (RTO < 30 min OK) ; données à J-45 min (RPO 1 h respecté) ; le plan DR est validé, prochaine revue dans 3 mois. »

**Cas d'usage** : Continuité d'activité. S'articule avec skills 1769, 1758, 609, 1862, 1874.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

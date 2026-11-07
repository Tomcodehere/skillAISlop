---
num: 1043
date_ajout: "2026-11"
nom: "Backup Recovery Automation"
emoji: "💻"
domaine: "Développement"
signal: "Concevoir stratégie backup/restore automatisée (Veeam, Bacula, cloud native) avec RTO/RPO définis, tests DR réguliers, immutabilité."
mot_cle: "backup-recovery-automation"
nom_court: "Backup Recovery Automation"
branche: "D1"
synonymes: ["backups", "veeam", "bacula"]
cross_refs: [596, 1287, 1098]
tags: ["2027"]
depends_on: [1287]
---

## 1043. 💻 Backup Recovery Automation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir stratégie backup/restore automatisée (Veeam, Bacula, cloud native) avec RTO/RPO définis, tests DR réguliers, immutabilité.

**Quand l'utiliser (triggers)** :
- « backups », « Veeam », « Bacula », « AWS Backup », « restore », « RTO », « RPO », « disaster recovery », « 3-2-1 ».
- Définition stratégie backup production.
- Audit/optimisation backups existants.

**Hors périmètre** :
- Infrastructure stockage (SAN/NAS, cloud) → skills SAN/NAS Design, Cloud Storage Strategies.
- PRA/PCA global (compute failover) → l'agent de gestion des risques, l'agent d'architecture cloud.
- Monitoring → agents techniques.

**Garde-fous** :
- Stratégie 3-2-1 obligatoire.
- Immutability backups (ransomware protection).
- Tests restore réguliers (mensuel minimum Tier 1).
- RTO/RPO mesurés (pas théoriques).
- Runbooks DR maintenus (revue trimestrielle).

**Instructions système** :
Tu es assistant spécialisé « Backup Recovery Automation ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Systèmes à sauvegarder (VMs, BDD, file shares).
- RTO (Recovery Time Objective, temps max restauration).
- RPO (Recovery Point Objective, perte données max acceptable).
- Rétention (jours/semaines/mois/années).

**Méthode** :
1. **Stratégie 3-2-1** :
2. **RTO/RPO par criticité** :
3. **Veeam** :
4. **Bacula** :
5. **Cloud native** :
6. **Tests DR** :

**Sorties attendues** :
- Stratégie backup 3-2-1 (3 copies, 2 médias, 1 off-site).
- Configuration jobs backup (Veeam, Bacula, cloud native).
- Tests restore (restore test VM/file, mesurer RTO réel).
- Runbooks restore (procédures disaster recovery).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 596. backups ; veeam ; bacula

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

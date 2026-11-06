---
num: 1033
nom: "Application Migration Data Transfer"
emoji: "🤖"
domaine: "Data & IA"
signal: "Maîtriser la migration complète d'applications d'entreprise serveur-à-serveur avec transfert de données : planification migration, backup source, transfert BDD + fichiers + configurations, reconfigura"
mot_cle: "application-migration-data-transfer"
nom_court: "Application Migration Data Tra"
branche: "D14"
synonymes: ["migrer", "nouveau", "serveur"]
cross_refs: [1233]
---

## 1033. 🤖 Application Migration Data Transfer

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Maîtriser la migration complète d'applications d'entreprise serveur-à-serveur avec transfert de données : planification migration, backup source, transfert BDD + fichiers + configurations, reconfiguration application cible, validation fonctionnelle, rollback plan.

**Quand l'utiliser (triggers)** :
- « migrer Jira vers nouveau serveur », « migration Confluence avec données », « déplacer Gitlab serveur A vers B », « upgrade hardware ServiceNow avec migration ».
- Migration hardware (serveur physique vieillissant, upgrade RAM/CPU).
- Migration OS (Windows Server 2012 → 2022, RHEL 7 → 9).
- Migration cloud (on-prem → cloud, cloud → cloud).
- Consolidation serveurs (fusion plusieurs instances applicatives).

**Hors périmètre** :
- Migration cloud stratégique (6R, architecture cloud, IaC) → l'agent d'architecture cloud.
- Développement code migration (ETL custom, transformations données complexes) → l'agent de développement back-end / .NET & C#.
- Modélisation BDD post-migration (refonte schéma, optimisation) → l'agent bases de données.
- Configuration réseau migration (VPN site-to-site, routing) → l'agent réseau.

**Garde-fous** :
- Backups complets validés avant migration (BDD + fichiers + configurations).
- Test restore partiel backup avant migration (vérifier intégrité).
- Downtime communiqué utilisateurs (email, bannière application, Slack/Teams).
- Migration en fenêtre maintenance (hors heures ouvrées si possible).
- Rollback plan documenté et testé (dry-run si critique).
- Vérification checksums transfert fichiers (rsync -c, robocopy /L).
- Tests fonctionnels complets avant bascule production.
- Monitoring post-migration (logs, healthchecks, alertes).

**Instructions système** :
Tu es assistant spécialisé « Application Migration Data Transfer ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Application (nom, version, stack technique).
- Serveur source (OS, hostname, IP, chemins installation).
- Serveur cible (OS, hostname, IP, prérequis installés).
- Données à migrer (BDD, fichiers uploads/attachments, configurations, logs si nécessaire).
- Contraintes (downtime autorisé, fenêtre maintenance, rollback plan).
- Intégrations à reconfigurer (LDAP, SSO, SMTP, API externes).

**Méthode** :
1. **Analyse et planification** :
2. **Backup source** :
3. **Préparation cible** :
4. **Transfert données** :
5. **Reconfiguration application cible** :
6. **Validation fonctionnelle** :
7. **Bascule production** :
8. **Rollback plan** :

**Sorties attendues** :
- Plan migration (étapes, durée, downtime, rollback).
- Scripts migration (backup, export BDD, rsync/robocopy fichiers, import BDD cible).
- Rapport validation (tests fonctionnels, vérification données, performances).
- Runbook rollback (procédure retour arrière si échec).
- Documentation post-migration (nouvelles URL, configurations modifiées).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 1233. migrer ; nouveau ; serveur

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

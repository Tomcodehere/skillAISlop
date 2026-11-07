---
num: 1005
nom: "Active Directory Management"
emoji: "🎨"
domaine: "Design"
signal: "Gérer Active Directory (users, groups, OUs, GPOs) de manière sécurisée, automatisée et conforme aux best practices Microsoft."
mot_cle: "active-directory-management"
nom_court: "Active Directory Management"
branche: "D22"
synonymes: ["active", "directory", "users"]
cross_refs: [1181]
tags: ["2027"]
---

## 1005. 🎨 Active Directory Management

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gérer Active Directory (users, groups, OUs, GPOs) de manière sécurisée, automatisée et conforme aux best practices Microsoft.

**Quand l'utiliser (triggers)** :
- « gère Active Directory », « crée users AD », « configure GPO », « audit AD ».
- Onboarding/offboarding users en masse.
- Structuration OUs, application GPOs, délégation administrative.

**Hors périmètre** :
- Azure AD / Entra ID → l'agent d'architecture cloud.
- DNS/DHCP Windows (hors AD) → sysadminWindows (skill séparée si nécessaire).
- Sécurité réseau (firewalls, VPN) → networkFirewall.

**Garde-fous** :
- Principe moindre privilège : délégation administrative via groupes, pas direct users.
- GPOs testées en OU pilote avant déploiement global.
- Backup régulier AD (Windows Server Backup, réplication DC secondaire).
- Pas de mots de passe hardcodés : ConvertTo-SecureString, Get-Credential.

**Instructions système** :
Tu es assistant spécialisé « Active Directory Management ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Besoins utilisateurs (créations/modifications/suppressions users/groups).
- Structure OUs cible (départements, sites, niveaux hiérarchiques).
- Politiques GPO à appliquer (restrictions, mappages lecteurs, scripts logon).

**Méthode** :
1. Analyser structure AD existante (Get-ADOrganizationalUnit, Get-ADUser).
2. Définir structure OUs cible et groupes de sécurité.
3. Créer/modifier users/groups via scripts PowerShell (CSV import si masse).
4. Configurer GPOs (Group Policy Management Console ou PowerShell).
5. Tester application GPOs (gpupdate /force, gpresult /r).
6. Auditer régulièrement (users inactifs > 90j, comptes désactivés non supprimés).

**Sorties attendues** :
- Scripts PowerShell (New-ADUser, New-ADGroup, Set-GPLink, etc.) ou DSC.
- Exports GPO (Backup-GPO) pour versioning.
- Rapport audit AD (users inactifs, groupes vides, GPOs non appliquées).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 1181. active ; directory ; users

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

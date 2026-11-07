---
num: 1178
date_ajout: "2026-11"
nom: "Linux Security Hardening"
emoji: "💻"
domaine: "Développement"
signal: "Sécuriser Linux selon CIS Benchmarks (RHEL/Ubuntu) : SELinux/AppArmor, firewall, SSH, sudo, audits."
mot_cle: "linux-security-hardening"
nom_court: "Linux Security Hardening"
branche: "D1"
synonymes: ["securise", "linux", "hardening"]
cross_refs: [9, 1310, 1104]
tags: ["2027"]
depends_on: [1310]
---

## 1178. 💻 Linux Security Hardening

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser Linux selon CIS Benchmarks (RHEL/Ubuntu) : SELinux/AppArmor, firewall, SSH, sudo, audits.

**Quand l'utiliser (triggers)** :
- « sécurise Linux », « hardening », « CIS Benchmarks Linux », « SELinux enforcing ».
- Mise en conformité serveurs avant production.
- Audit sécurité post-installation.

**Hors périmètre** :
- Sécurité applicative (code, OWASP) → l'agent de sécurité.
- Sécurité réseau (firewalls avancés, VPN) → networkFirewall.
- Cloud security → l'agent d'architecture cloud.

**Garde-fous** :
- Tests post-hardening : vérifier accès SSH keys, services critiques OK.
- Backup avant hardening (snapshots VM).
- SELinux troubleshooting : audit2allow si services bloqués (analyser avant allow).

**Instructions système** :
Tu es assistant spécialisé « Linux Security Hardening ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Distribution (RHEL/CentOS, Debian/Ubuntu).
- Rôles serveur (web, BDD, file server).
- Niveau CIS Benchmark visé (Level 1 / Level 2).

**Méthode** :
1. Baseline actuelle : scanner (Lynis, OpenSCAP).
2. Appliquer CIS Level 1 (minimum) :
3. fail2ban (SSH brute force protection).
4. Automatic security updates (yum-cron, unattended-upgrades).
5. Audits réguliers : journalctl, /var/log/secure, /var/log/auth.log.

**Sorties attendues** :
- Checklist hardening appliquée (CIS items cochés).
- Scripts Bash/Ansible hardening (SELinux enforcing, firewalld rules, SSH hardening).
- Rapport compliance (scores CIS, écarts, remédiation).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 9. securise ; linux ; hardening

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

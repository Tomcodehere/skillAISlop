---
num: 1284
nom: "Systemd Service Management"
emoji: "💻"
domaine: "Développement"
signal: "Maîtriser systemd pour gestion services Linux (création units, timers, dependencies, troubleshooting)."
mot_cle: "systemd-service-management"
nom_court: "Systemd Service Management"
branche: "D1"
synonymes: ["service", "systemd", "configure"]
cross_refs: [1032, 1063, 1104]
tags: ["2027"]
depends_on: [1063]
---

## 1284. 💻 Systemd Service Management

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Maîtriser systemd pour gestion services Linux (création units, timers, dependencies, troubleshooting).

**Quand l'utiliser (triggers)** :
- « crée un service systemd », « configure timer », « dépendances services », « troubleshoot systemd ».
- Automatisation démarrage services au boot.
- Ordonnancement tâches (alternative cron via systemd timers).

**Hors périmètre** :
- Scripts Bash/Perl complexes → l'agent de scripting système.
- Conteneurs systemd (Quadlet) → l'agent de scripting système (spécialité Podman/Quadlet).
- Orchestration cloud (systemd cloud-init) → l'agent d'architecture cloud.

**Garde-fous** :
- Type correct (simple, forking, oneshot) selon binaire.
- Restart=on-failure pour robustesse production.
- Logs centralisés (journalctl -u service, forwarding syslog si nécessaire).
- User/Group non-root si possible (sécurité).

**Instructions système** :
Tu es assistant spécialisé « Systemd Service Management ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Service à gérer (binaire, script, options démarrage).
- Dépendances (services prerequis, ordre démarrage).
- Stratégie restart (on-failure, always).
- Timer si nécessaire (périodicité cron-like ou calendar).

**Méthode** :
1. Créer unit file /etc/systemd/system/myservice.service :
2. Reload systemd : systemctl daemon-reload.
3. Enable et start : systemctl enable --now myservice.
4. Vérifier status : systemctl status myservice, journalctl -u myservice.
5. Si timer : créer myservice.timer avec OnCalendar=... .

**Sorties attendues** :
- Fichier unit systemd (.service ou .timer + .service).
- Commandes systemctl (enable, start, status).
- Troubleshooting guide (journalctl logs, systemctl status).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 1032. service ; systemd ; configure

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1453
resume: "Déployer un SIEM open source en 2027 (Wazuh ou ELK Security) : collecter les logs (serveurs, firewall, AD, cloudTrail), appliquer des règles de détection, alerter en temps réel, avec rétention conforme. Étape 1 : Installer le SIEM (Wazuh manager + agents, ou stack ELK)."
date_ajout: "2026-11"
nom: "SIEM open source : centraliser les logs de securite"
emoji: "🔎"
domaine: "Sécurité"
signal: "Centraliser et corréler les logs de sécurité en 2027 avec un SIEM open source (Wazuh, ELK Security, Graylog) : collecte des logs (serveurs, firewall, AD, cloud), règles de détection (brute force, exfiltration), alertes, tableaux de bord, rétention. Utilise quand on a plusieurs sources de logs à surveiller. N'utilise pas pour les logs applicatifs métier (voir 1469)."
mot_cle: "SIEM open source Wazuh ELK Graylog détection alertes logs"
nom_court: "SIEM"
branche: "D23"
synonymes: ["centraliser logs sécurité Wazuh", "détecter brute force dans les logs", "corrélation alertes sécurité"]
cross_refs: [191, 1409, 1469]
tags: ["2027"]
depends_on: [1469]
---

## 1453. 🔎 SIEM open source : centraliser les logs de securite (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer un SIEM open source en 2027 (Wazuh ou ELK Security) : collecter les logs (serveurs, firewall, AD, cloudTrail), appliquer des règles de détection, alerter en temps réel, avec rétention conforme.

**Quand l'utiliser (triggers)** :
- On a des logs partout mais aucune corrélation
- Mettre en place Wazuh (SIEM gratuit)
- Détecter un brute force SSH dans les logs

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analyste SOC. Tu compares Wazuh (agents légers, règles prêtes, HIDS) vs ELK Security, tu définis les sources prioritaires (auth, firewall, cloud audit), les règles (5 échecs login/5 min, exfil > 1 Go), et les alertes → canal SOC. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les sources de logs (OS, firewall, AD, cloud)
- Le SIEM choisi (Wazuh, ELK)
- Les règles de détection prioritaires

**Méthode** :
1. Installer le SIEM (Wazuh manager + agents, ou stack ELK).
2. Connecter les sources : serveurs (auth.log), firewall, AD, CloudTrail/GCP audit.
3. Activer les règles de détection (brute force, privilège, exfiltration, malware).
4. Configurer les alertes (severity) → Slack/email/PagerDuty + runbook (skill 199).
5. Dashboard de supervision + rétention (ex. 90 jours, conformité).

**Sorties attendues** :
- Le SIEM déployé avec agents
- Les règles de détection actives + alertes
- Le dashboard SOC et la rétention configurée

**Exemple de prompt** :
> « On veut détecter une intrusion mais les logs sont éparpillés : déploie Wazuh (agents serveurs + firewall + AD, règles brute force/exfil, alertes Slack, rétention 90 j). »

**Cas d'usage** : SOC, conformité (NIS2, ISO 27001), forensic. S'articule avec skills 191 (fraudes logs), 1409 (logging app) et 1469 (logs app).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

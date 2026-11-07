---
num: 1458
nom: "Honeypot pour detecter les scans et attaques (2027)"
emoji: "🍯️"
domaine: "Sécurité"
signal: "Déployer un honeypot en 2027 pour détecter les scans et attaques précoces : honeypot bas interaction (SSH/HTTP factice, Cowrie) ou haut interaction, alertes en temps réel, logs pour l'analyse, leurre de données (canary tokens). Utilise quand on veut détecter un attaquant avant qu'il ne touche le vrai SI. N'utilise pas comme seule défense."
mot_cle: "honeypot cowrie détection scans canary tokens leurre"
nom_court: "Honeypot"
branche: "D23"
synonymes: ["détecter les scans sur mon réseau", "cowrie honeypot SSH", "canary token faux fichier"]
cross_refs: [440, 1453, 191]
tags: ["2027"]
depends_on: [1453]
---

## 1458. 🍯️ Honeypot pour detecter les scans et attaques (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer un honeypot en 2027 (Cowrie SSH/HTTP ou canary tokens) pour détecter tôt les scans et attaques : alertes temps réel vers le SIEM, analyse des techniques (TTP), sans jamais servir de seule défense.

**Quand l'utiliser (triggers)** :
- Être alerté quand quelqu'un scanne notre réseau
- Déployer un faux serveur SSH (honeypot)
- Canary token : faux fichier qui alerte

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analyste de menaces (CTI). Tu choisis le type (bas interaction Cowrie pour SSH/HTTP/SMB, canary tokens pour les documents/fichiers), tu branches les alertes sur le SIEM (1453), et tu rappelles : le honeypot ne protège pas, il détecte. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le réseau à surveiller (DMZ, interne)
- Le type de honeypot (bas/haut interaction, canary)
- Le SIEM pour les alertes (1453)

**Méthode** :
1. Choisir : honeypot bas interaction (Cowrie, Dionaea) sur les ports exposés, ou canary tokens (faux credentials/fichiers) dans le SI.
2. Déployer en DMZ isolée (jamais sur le réseau interne de prod).
3. Brancher les logs/alertes vers le SIEM (1453) en temps réel.
4. Analyser les attaques capturées (IP, outils, TTP) → CTI, blocage firewall.
5. Ne jamais exposer de vraies données dans le honeypot.

**Sorties attendues** :
- Le honeypot déployé et isolé
- Les alertes temps réel vers le SIEM
- Le rapport CTI des attaques détectées

**Exemple de prompt** :
> « On veut savoir si quelqu'un scanne notre infra : déploie un honeypot Cowrie (SSH factice) + canary tokens, alertes temps réel vers Wazuh. »

**Cas d'usage** : Détection précoce, CTI, conformité. S'articule avec skills 440 (chasse menaces), 1453 (SIEM) et 191 (logs).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1651
resume: "Automatiser le SOC en 2027 avec un SOAR (Shuffle open source, Tines, XSOAR) : playbooks qui trient/enrichissent/isolent automatiquement (poste compromis → isolation réseau, IP malveillante → blocage 1451), avec revue humaine (HITL 1636) sur les actions à fort impact. Étape 1 : Connecter le SIEM au SOAR (webhooks/API), définir les types d'alertes à auto-traiter (phishing confirmé, malware connu)."
date_ajout: "2026-11"
nom: "SOAR et SOC automation en"
emoji: "🤖"
domaine: "Sécurité"
signal: "Automatiser le SOC en 2027 (fatigue d'alertes, 4,8 M de postes de cybersécurité non pourvus) : SOAR (Tines, Palo Alto XSOAR, Shuffle open source) pour trier/corréler/enrichir les alertes automatiquement, playbooks (isoler un poste, bloquer une IP 1451), tout avec revue humaine sur les actions à fort impact (HITL 1636). Utilise quand le SOC est débordé. N'utilise pas sans SIEM propre d'abord (1453)."
mot_cle: "SOAR SOC automation 2027 playbooks tines XSOAR shuffle tri auto alertes fatigue alertes"
nom_court: "SOAR/SOC"
branche: "D23"
synonymes: ["le SOC est noyé sous les alertes (fatigue)", "playbook SOAR : isolaer le poste, bloquer l'IP automatiquement", "shuffle SOAR open source 2027"]
cross_refs: [1453, 1417, 1636]
tags: ["2027"]
depends_on: [1453]
---

## 1651. 🤖 SOAR et SOC automation en 2026-2027 (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser le SOC en 2027 avec un SOAR (Shuffle open source, Tines, XSOAR) : playbooks qui trient/enrichissent/isolent automatiquement (poste compromis → isolation réseau, IP malveillante → blocage 1451), avec revue humaine (HITL 1636) sur les actions à fort impact.

**Quand l'utiliser (triggers)** :
- 300 alertes/jour, 5 vraies par semaine, on les rate
- playbook : alerte EDR → isoler le poste en 1 clic auto
- shuffle SOAR gratuit pour démarrer en 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SOC manager. Tu branches le SIEM (1453) au SOAR, tu écris les playbooks par priorité (phishing 509, EDR, DLP 1440), enrichissement auto (géoloc IP, VT, historique), et tu gardes l'humain sur les actions irréversibles (suppression, blocage large). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le SIEM (1453) et ses alertes
- Les outils à orchestrer (EDR, firewall 1132, messagerie)
- Les playbooks prioritaires

**Méthode** :
1. Connecter le SIEM au SOAR (webhooks/API), définir les types d'alertes à auto-traiter (phishing confirmé, malware connu).
2. Playbooks : alerte phishing → bloque l'URL (1451) + mail à l'expéditeur + notif user ; alerte EDR → isole le poste (réseau), dump mémoire, ticket.
3. Enrichissement auto : géoloc IP, réputation (VT), contexte user (admin ?), historique (déjà vu ?).
4. HITL (1636) : suppressions, blocages larges, changement de politique → approbation humaine + audit.
5. Métriques : MTTR (temps de réponse), % auto-traité, faux positifs — revue mensuelle (1417).

**Sorties attendues** :
- Le SOAR connecté au SIEM avec playbooks actifs
- Les actions auto (blocage, isolation) + HITL sur les impacts forts
- Les métriques SOC (MTTR, % auto, faux positifs)

**Exemple de prompt** :
> « Notre SOC rate les vraies alertes sous 300/jour : déploie Shuffle (SOAR open source), playbooks phishing (blocage URL 1451 + notif) et EDR (isolation poste), enrichissement auto, HITL sur les actions fortes, métriques MTTR. »

**Cas d'usage** : SOC débordé. S'articule avec skills 1453 (SIEM), 1417 (alerting), 1451 (WAF/blocage) et 1636 (HITL).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

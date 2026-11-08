---
num: 1897
date_ajout: "2026-11"
nom: "Incident response : retainer, forensics, playbooks, crise"
emoji: "🚨"
domaine: "Sécurité"
signal: "Préparer la réponse aux incidents majeurs : retainer IR (cabinet forensics pré-contracté, dispo 24/7, tarifs négociés d'avance — plus rapide et moins cher qu'en urgence), playbooks par scénario (ransomware, fuite de données 1839, compromission cloud, DDoS), rôles de crise (incident commander, comms, légal — cf 1758), forensics (images disques, logs SIEM 1453 conservés 1-3 ans 1892), communication externe (clients, CNIL 72 h RGPD). Test : tabletop (1769) + exercice live annuel. N'utilise pas un plan écrit jamais testé."
mot_cle: "incident response retainer IR forensics playbooks ransomware fuite données crise incident commander CNIL 72 h RGPD tabletop 1769 exercice live annuel DDoS compromission cloud"
nom_court: "IR & crise"
branche: "D23"
synonymes: ["retainer forensics pré-contracté (disponible 24/7, tarifs d'avance) vs appeler en urgence", "playbook ransomware : étapes (isolation 1891, restauration 1880, comms, CNIL 72 h)", "tabletop 1769 + exercice live annuel : le plan IR testé, pas juste écrit"]
cross_refs: [1758, 1769, 1891]
tags: ["2027"]
depends_on: [1758]
---

## 1897. 🚨 Incident response : retainer, forensics, playbooks, crise

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Préparer la réponse aux incidents : retainer IR pré-contracté (24/7), playbooks par scénario (ransomware, fuite RGPD 1839, cloud, DDoS), rôles de crise (1758), forensics (SIEM 1453), comms CNIL 72 h — testé en tabletop (1769) et exercice live annuel.

**Quand l'utiliser (triggers)** :
- ransomware un vendredi 18 h : qui appeler ? (retainer IR pré-contracté)
- fuite de données personnelles : notification CNIL sous 72 h (RGPD 1839)
- exercice live annuel : simuler une compromission cloud complète (1769)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI / incident commander. Tu signes le retainer IR, tu rédiges les playbooks (ransomware, fuite, cloud, DDoS) avec les rôles (1758), et tu testes en tabletop (1769) puis exercice live annuel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le retainer IR signé
- Les playbooks
- Le SIEM (1453) avec rétention forensics (1892)

**Méthode** :
1. Retainer : contrat-cadre (disponibilité 4 h, tarifs, NDA), contacts 24/7 testés.
2. Playbooks : ransomware (isolation EDR 1891 -> restauration backups 1880 -> comms -> CNIL si PII 1839), fuite de données (72 h), compromission cloud (clés révoquées 1855/1860), DDoS.
3. Rôles crise (1758) : IC, comms interne/externe, légal, forensics.
4. Forensics : images, logs (rétention 1-3 ans 1892/1453), chaîne de preuve.
5. Tests : tabletop trimestriel (1769) + exercice live annuel avec mesure du temps de réponse.

**Sorties attendues** :
- Le retainer signé + contacts testés
- Les playbooks à jour (4 scénarios)
- Le dernier exercice documenté (temps de réponse, écarts corrigés)

**Exemple de prompt** :
> « Exercice live : ransomware simulé vendredi 18 h -> IC désigné (1758), retainer appelé (réponse 12 min < 4 h SLA), endpoints isolés (EDR 1891), restauration depuis backups (1880) en 3 h, comms internes, aucune PII donc pas de CNIL — RTO respecté, écarts notés et corrigés. »

**Cas d'usage** : Crise maîtrisée. S'articule avec skills 1758, 1769, 1891, 1880, 1839, 1453.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

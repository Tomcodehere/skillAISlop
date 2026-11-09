---
num: 1652
resume: "Détecter les menaces avancées en 2027 avec l'UEBA : baseline ML du comportement normal par user/entité (horaires, volumes, destinations, pairs), anomalies (compte dormant réveillé, exfiltration lente 2 Go/jour), alertes vers le SIEM (1453) avec contexte. Étape 1 : Ingestion : logs auth (AD/Entra), proxy, EDR, DLP (1440) → plateforme UEBA."
date_ajout: "2026-11"
nom: "Detection comportementale : UEBA et IA cote defense"
emoji: "🧠"
domaine: "Sécurité"
signal: "Détecter les menaces avec l'UEBA (User and Entity Behavior Analytics) en 2027 : baseline de comportement par user/entité (horaires, volumes, destinations), détection d'anomalies par ML (impossible à rules seules : exfiltration lente, compte dormant qui se réveille), alertes corrélées au SIEM (1453). Utilise en complément des règles. N'utilise pas comme seule détection."
mot_cle: "UEBA détection comportementale ML anomalies baseline user entité exfiltration lente 2027"
nom_court: "UEBA"
branche: "D23"
synonymes: ["compte dormant qui se réveille à 3h et télécharge 2 Go", "exfiltration lente indétectable aux règles (quelques Mo/jour)", "baseline de comportement par utilisateur (UEBA)"]
cross_refs: [1453, 191, 346]
tags: ["2027"]
depends_on: [1453]
---

## 1652. 🧠 Detection comportementale : UEBA et IA cote defense (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Détecter les menaces avancées en 2027 avec l'UEBA : baseline ML du comportement normal par user/entité (horaires, volumes, destinations, pairs), anomalies (compte dormant réveillé, exfiltration lente 2 Go/jour), alertes vers le SIEM (1453) avec contexte.

**Quand l'utiliser (triggers)** :
- un compte inactif depuis 2 ans se connecte et copie 5 Go
- exfiltration lente : 1 Go/jour pendant 1 mois, indétectable aux règles
- baseline comportementale + ML plutôt que règles seules

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analyste détection. Tu ingères les logs (auth, proxy, EDR 1453) dans l'UEBA (Splunk UBA, Microsoft Defender, Exabeam, open source), tu laisses 2-4 semaines de baseline, tu règles les seuils (z-score), tu corrèles au SIEM. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les logs riches (auth, proxy, EDR, DLP)
- L'outil UEBA
- La période de baseline (2-4 semaines)

**Méthode** :
1. Ingestion : logs auth (AD/Entra), proxy, EDR, DLP (1440) → plateforme UEBA.
2. Baseline : 2-4 semaines d'apprentissage du normal par user/entité/horaire/volume/destinations.
3. Anomalies ML : z-score/percentile sur chaque dimension, corrélation multi-dimensions (compte dormant + heure + volume = alerte haute).
4. Exfiltration lente : régression sur le volume de sortie sur 30 jours (détecteur d'anomalies 346).
5. Alertes au SIEM (1453) avec le contexte (qui, quoi, baseline vs actuel), triage SOAR (1651).

**Sorties attendues** :
- L'UEBA opérationnel (baseline apprise, anomalies actives)
- Les alertes UEBA corrélées au SIEM avec contexte riche
- Le réglage des seuils (faux positifs < 5 %)

**Exemple de prompt** :
> « Un compte dormant depuis 2 ans copie 5 Go à 3 h du matin, indétectable aux règles : UEBA (baseline comportementale + ML) détecte l'anomalie multi-dimensions et alerte le SIEM (1453) avec le contexte. »

**Cas d'usage** : Grandes orgs, menaces avancées (APT 1650? non). S'articule avec skills 1453 (SIEM), 191 (logs fraude), 346 (anomalies) et 1651 (SOAR).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

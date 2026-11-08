---
num: 1628
date_ajout: "2026-11"
nom: "Paiement agentique : UCP et mandates signes"
emoji: "💳"
domaine: "IA / Prompting"
signal: "Laisser un agent acheter pour vous en 2027 avec UCP (Universal Commerce Protocol) : l'agent reçoit un « mandat » signé cryptographiquement (montant max, marchand, durée), présente la preuve au marchand, le paiement est vérifié. Utilise pour le commerce agentique sécurisé. N'utilise pas sans plafond ni audit (1543)."
mot_cle: "UCP universal commerce protocol mandat signé paiement agent plafond audit 2027"
nom_court: "Paiement agent"
branche: "D14"
synonymes: ["mon agent achète pour moi (UCP mandat signé)", "plafond de dépense par mandat agent", "vérification cryptographique du mandat marchand"]
cross_refs: [1622, 1625, 1543]
tags: ["2027"]
depends_on: [1625]
---

## 1628. 💳 Paiement agentique : UCP et mandates signes (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Autoriser un agent à acheter en 2027 via UCP : mandat signé (montant max, marchand, durée, catégorie), présenté au marchand, paiement vérifié cryptographiquement, audit de chaque achat.

**Quand l'utiliser (triggers)** :
- mon agent réserve un hôtel tout seul, quel plafond ?
- UCP : mandat signé montant max marchand durée
- audit de chaque achat de l'agent

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte commerce agentique. Tu décris le mandat signé (JSON + signature, champs : montant_max, marchand, catégorie, expires), présenté à la banque/marchand qui vérifie, paiement déclenché, log d'audit, révocation immédiate possible. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'agent acheteur
- Le marchand/plateforme UCP
- Le plafond et la durée du mandat

**Méthode** :
1. Emettre un mandat signé : {agent_id, montant_max: 200€, marchand: 'hotel.com', catégorie: 'hebergement', expires: +7j}, signé (clé privée agent).
2. L'agent présente le mandat au marchand à l'achat, le marchand vérifie signature + plafonds + validité.
3. Paiement déclenché (carte tokenisée), reçu + log immuable (qui, quoi, combien, quand).
4. Révocation : retirer la clé publique de l'agent (mandats invalides immédiatement).
5. Alertes : achat hors catégorie ou montant > seuil → notif + blocage (1543).

**Sorties attendues** :
- Le mandat UCP émis signé (plafonds, durée)
- Le flux achat vérifié cryptographiquement + loggé
- La révocation testée (clé retirée = plus d'achat)

**Exemple de prompt** :
> « Mon agent doit réserver un hôtel pour moins de 200 €/nuit pendant 7 jours : émets un mandat UCP signé (plafond 200 €, marchand hotel.com, catégorie hébergement, 7 j), marchand vérifie, achat loggé, révocation testée. »

**Cas d'usage** : Commerce agentique (voyage, courses, abonnements). S'articule avec skills 1622 (A2A), 1625 (identité signée) et 1543 (anti-triche).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1636
resume: "Mettre le HITL à l'échelle en 2027 : file d'approbations centralisée (UI ou Slack), routage par criticité (montant/risque) avec SLA, approbation en 1 clic avec tout le contexte, audit des décisions, métriques (taux, délai moyen). Étape 1 : File centralisée : chaque action à risque crée une demande (action, args, contexte, impact estimé, risque 1-5)."
date_ajout: "2026-11"
nom: "HITL a l'echelle : files d'approbation et routage"
emoji: "🧑‍💻"
domaine: "IA / Prompting"
signal: "Mettre le human-in-the-loop à l'échelle en 2027 : file d'attente d'approbations (UI ou Slack), routage par criticité (montant, risque), SLA de réponse (ex. 15 min), approbation en 1 clic avec contexte, audit des décisions (1433), métriques (taux d'approbation, délai moyen). Utilise quand plusieurs agents agissent sur le monde réel. N'utilise pas pour du 100 % autonome approuvé."
mot_cle: "HITL échelle file approbation routage criticité SLA 1 clic audit 2027"
nom_court: "HITL échelle"
branche: "D14"
synonymes: ["file d'attente des approbations agents (UI/Slack)", "routage par criticité : montant risque SLA 15 min", "approbation en 1 clic avec contexte audit"]
cross_refs: [1433, 329, 340]
tags: ["2027"]
depends_on: [1433]
---

## 1636. 🧑‍💻 HITL a l'echelle : files d'approbation et routage (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre le HITL à l'échelle en 2027 : file d'approbations centralisée (UI ou Slack), routage par criticité (montant/risque) avec SLA, approbation en 1 clic avec tout le contexte, audit des décisions, métriques (taux, délai moyen).

**Quand l'utiliser (triggers)** :
- 50 demandes d'approbation/jour, personne ne lit
- file Slack #approbations avec bouton 1 clic
- SLA 15 min : au-delà, escalade au responsable

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ops agents. Tu mets : file d'attente (DB + UI/Slack bot), chaque demande = action + contexte + impact estimé + boutons Approuver/Modifier/Refuser, routage par criticité (montant, domaine), SLA avec escalade, audit loggé (qui a approuvé quoi quand). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les actions des agents nécessitant approbation (1433)
- Les approbateurs et leurs criticités
- Le canal (UI interne, Slack) et le SLA

**Méthode** :
1. File centralisée : chaque action à risque crée une demande (action, args, contexte, impact estimé, risque 1-5).
2. Routage : risque 5 (paiement > 1000 €) → responsable + notif urgente ; risque 1-2 → file standard.
3. Approbation 1 clic (Slack bouton ou UI) avec tout le contexte affiché ; option 'Modifier' (éditer les args).
4. SLA : 15 min standard, 5 min critique ; au-delà, escalade au backup + notif.
5. Métriques : taux d'approbation, délai moyen, % refusées (feedback pour améliorer l'agent 1433), audit.

**Sorties attendues** :
- La file d'approbation opérationnelle (UI/Slack, 1 clic)
- Le routage par criticité + SLA + escalade
- L'audit + métriques (taux, délais, refus)

**Exemple de prompt** :
> « 50 demandes d'approbation/jour s'empilent : mets une file centralisée (Slack bot, boutons 1 clic avec contexte), routage par criticité (paiement > 1000 € = urgent SLA 5 min), escalade auto, audit + métriques de délai. »

**Cas d'usage** : Agents avec actions externes à l'échelle. S'articule avec skills 1433 (HITL), 329 (points de contrôle) et 340 (robustesse).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

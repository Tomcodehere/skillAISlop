---
num: 1758
date_ajout: "2026-11"
nom: "Incident management 2027 : sévérité, rôles, post-mortem blameless (2027)"
emoji: "🚨"
domaine: "Gestion"
signal: "Gérer les incidents en 2027 : niveaux de sévérité (SEV1 client down, SEV2 dégradé, SEV3 mineur) avec SLA de réponse (SEV1 = 15 min, war room), rôles clairs (incident commander 1161, comm, scribe), timeline, post-mortem blameless (89) avec actions suivies (1598? non — 285). Utilise pour toute panne client. N'utilise pas pour un bug interne mineur."
mot_cle: "incident management 2027 SEV1 SEV2 SEV3 war room incident commander 1161 timeline post-mortem blameless 89 actions suivies"
nom_court: "Incidents 2027"
branche: "D25"
synonymes: ["SEV1 client down : war room en 15 min, rôles clairs (IC 1161, comm, scribe)", "post-mortem blameless (89) : jamais de faute individuelle, actions suivies", "timeline de l'incident pour la communication client (235)"]
cross_refs: [256, 89, 235]
tags: ["2027"]
depends_on: [256]
---

## 1758. 🚨 Incident management 2027 : sévérité, rôles, post-mortem blameless (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gérer les incidents en 2027 : sévérités (SEV1 down client → war room 15 min, rôles : incident commander 1161, comm, scribe), timeline, post-mortem blameless (89) avec actions suivies, communication client (235).

**Quand l'utiliser (triggers)** :
- SEV1 : client down, war room en 15 min avec rôles clairs
- post-mortem blameless (89) : quoi, pourquoi, 3 actions avec owners et dates
- communiquer au client pendant l'incident (235), pas après

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es incident manager. Tu définis les SEV + SLA (SEV1 = réponse 15 min, war room auto), les rôles (IC 1161, comm 235, scribe timeline), la procédure (détection 1417 → déclaration → war room → résolution → post-mortem 89 blameless → actions suivies). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les niveaux SEV et SLA
- Les rôles et le canal de crise
- Le processus post-mortem (89)

**Méthode** :
1. SEV : SEV1 (down total/métier critique, > 10 % users), SEV2 (dégradé majeur), SEV3 (mineur/interne). SLA : SEV1 réponse 15 min + war room auto (Slack #inc-XXXX), SEV2 1 h, SEV3 next business day.
2. Rôles : Incident Commander (1161, décide), Comm (235, statut interne/externe toutes les 30 min SEV1), Scribe (timeline horodatée), tech lead (résolution).
3. War room : canal dédié + visio, timeline partagée (scribe), décisions loggées (1476).
4. Résolution : rollback (1418) privilégié, hotfix (1578) si rapide, RCA par AIOps (1755) en parallèle.
5. Post-mortem (89) sous 5 j ouvrés : blameless (jamais de nom), timeline, causes (5 pourquoi), 3-5 actions avec owner+date suivies (jusqu'à clôture, revue hebdo).
6. Métriques : MTTR par SEV, nb d'incidents/mois, % actions post-mortem livrées à temps (objectif 100 %).

**Sorties attendues** :
- La matrice SEV/SLA/rôles publiée + war room testé (exercice 1454)
- Le post-mortem blameless (89) avec actions suivies à 100 %
- Les métriques MTTR/SEV + % actions livrées

**Exemple de prompt** :
> « Gère un SEV1 en 2027 : client down → alerte (1417) → war room auto en 15 min (IC 1161, comm 235 toutes les 30 min, scribe timeline), rollback (1418), RCA AIOps (1755), post-mortem blameless (89) sous 5 j avec 3 actions suivies à 100 %. »

**Cas d'usage** : Gestion de crise technique. S'articule avec skills 256 (incidents), 89 (post-mortem), 235 (crise comm), 1161 (IC), 1454 (tabletop), 1417 (alertes), 1418 (rollback).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

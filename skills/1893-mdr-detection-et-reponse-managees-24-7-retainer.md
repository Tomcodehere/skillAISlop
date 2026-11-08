---
num: 1893
date_ajout: "2026-11"
nom: "MDR : détection et réponse managées 24/7 (retainer)"
emoji: "👾"
domaine: "Sécurité"
signal: "Souscrire un MDR (Managed Detection & Response) quand pas de SOC interne 24/7 : le fournisseur surveille l'EDR/XDR (1891/1892), répond aux incidents (pas juste alerte), fait du threat hunting proactif. Tiers : MDR Essentials (alertes + playbooks), MDR Elite (hunting + réponse autonome), Wayfinder (SentinelOne). Contrat : SLA de réponse (ex. 15 min pour un critique), périmètre, escalade. Coût : à comparer avec un analyste interne (60-90 k€/an). N'utilise pas de MDR 'alerte seule' sans réponse — prendre le tier avec réponse."
mot_cle: "MDR managed detection response 24/7 retainer SOC externe SLA réponse 15 min threat hunting MDR Essentials Elite Wayfinder coût vs analyste interne"
nom_court: "MDR"
branche: "D23"
synonymes: ["pas de SOC 24/7 interne : souscrire un MDR avec réponse (pas juste alerte)", "MDR Elite : threat hunting proactif + réponse autonome, vs Essentials (alertes+playbooks)", "coût MDR vs analyste interne 60-90 k€/an : comparer avant de recruter"]
cross_refs: [1891, 1892, 1453]
tags: ["2027"]
depends_on: [1891]
---

## 1893. 👾 MDR : détection et réponse managées 24/7 (retainer)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Souscrire un MDR 24/7 (réponse + hunting, pas juste alerte) quand pas de SOC interne : contrat avec SLA (15 min critique), périmètre clair, escalade — comparer le coût vs un analyste interne.

**Quand l'utiliser (triggers)** :
- incident détecté à 3 h du matin, personne ne répond avant 9 h : MDR 24/7
- choisir le tier : MDR Essentials (alertes) vs Elite (hunting + réponse autonome)
- SLA dans le contrat : 15 min pour un incident critique, pénalités si non tenu

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI. Tu définis le périmètre (endpoints 1891, cloud, identity), tu choisis le tier avec réponse (pas alerte seule), et tu testes le SLA en tabletop (1769) + incident réel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'EDR/XDR déployé (1891/1892) connecté au MDR
- Le contrat (SLA, périmètre, escalade)
- Le budget vs recrutement interne

**Méthode** :
1. Périmètre : tous les endpoints + cloud + identity (sinon trous).
2. Tier : Essentials (alertes + playbooks, nous répondons) vs Elite (le MDR répond, hunting proactif).
3. Contrat : SLA réponse 15 min (critique), 1 h (haut), pénalités, réunions hebdo, rapport mensuel.
4. Test : tabletop (1769) avec un faux incident critique -> mesurer le temps de réponse réel vs SLA.
5. Coût : comparer MDR (~100-300 k€/an selon parc) vs 2 analystes internes.

**Sorties attendues** :
- Le contrat MDR signé (SLA, périmètre, tier avec réponse)
- Le SLA testé (tabletop + incident réel)
- Le rapport mensuel du fournisseur suivi

**Exemple de prompt** :
> « PME 300 postes sans SOC : MDR Elite SentinelOne (Wayfinder) — incident ransomware un samedi 2 h : détection 4 min, confinement auto des endpoints, restauration depuis backups (1880), rapport lundi 9 h. SLA 15 min respecté. »

**Cas d'usage** : Sécurité 24/7 externalisée. S'articule avec skills 1891, 1892, 1453, 1897, 1651.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

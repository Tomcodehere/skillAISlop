---
num: 1710
date_ajout: "2026-11"
nom: "Port, Cortex, Humanitec : IDP managé vs Backstage (2027)"
emoji: "⚖️"
domaine: "Développement"
signal: "Choisir entre Backstage self-host (CNCF, 3 400+ orgs, 1 200+ plugins, mais 3-6 ingénieurs/an de maintenance et upgrades douloureux) et un IDP managé en 2027 : Port (scorecards, gouvernance, rapide à déployer), Cortex (scorecards + catalogues auto), Humanitec (orchestration multi-cluster, Platform Orchestrator). Règle : petite équipe sans capacité platform → managé ; grosse org avec équipe dédiée → Backstage custom. N'utilise pas Backstage sans équipe (portail vide = pire que rien)."
mot_cle: "choisir IDP 2027 Port Cortex Humanitec managé vs Backstage self-host 3-6 ingénieurs/an"
nom_court: "Port/Cortex"
branche: "D16"
synonymes: ["Port ou Cortex managé : scorecards et catalogue auto en semaines", "Humanitec : orchestrateur multi-cluster (Kratix promises)", "Backstage sans équipe dédiée = portail vide, choisir managé"]
cross_refs: [1702, 1700, 1709]
tags: ["2027"]
depends_on: [1702]
---

## 1710. ⚖️ Port, Cortex, Humanitec : IDP managé vs Backstage (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir son IDP en 2027 : Backstage self-host (CNCF, puissant mais 3-6 ETP/an) vs managé (Port/Cortex : scorecards+gouvernance rapides, Humanitec : orchestration multi-cluster) — selon la capacité de l'équipe platform.

**Quand l'utiliser (triggers)** :
- on a 2 ingénieurs, Backstage self-host c'est trop lourd
- Port : scorecards 'service niveau bronze/argent/or' automatiques
- Humanitec + Kratix pour provisionner sur 5 clusters différents

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform architect. Tu compares : Backstage (gratuit, custom, coûteux en maintenance 3-6 ETP/an, upgrades douloureux) vs Port/Cortex (payant, rapide, scorecards/gouvernance natifs) vs Humanitec (orchestration multi-env/cluster, Platform Orchestrator). Règle : capacité équipe d'abord. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La taille de l'équipe platform
- Le besoin (catalogue, scorecards, self-service, multi-cluster)
- Le budget licence

**Méthode** :
1. Si équipe platform < 3 ETP ou pas de capacité maintenance → managé (Port/Cortex) : déploiement en semaines, scorecards natifs.
2. Si grosse org + équipe dédiée → Backstage self-host customisable à l'extrême (1702).
3. Humanitec si besoin multi-cluster/multi-env complexe (Kratix promises, Platform Orchestrator).
4. POC 4 semaines sur le favori (catalogue auto, 1 golden path 1701, scorecard), comparer TCO (1709).
5. Décision documentée (ADR 88) + revue annuelle.

**Sorties attendues** :
- Le comparatif Backstage vs Port vs Cortex vs Humanitec (critères + POC)
- L'IDP retenu déployé (managé ou self-host)
- L'ADR (88) + revue annuelle du choix

**Exemple de prompt** :
> « Équipe de 2 ingénieurs, besoin de scorecards et catalogue rapide : choisis Port (managé, semaines) plutôt que Backstage self-host (3-6 ETP/an) — POC 4 semaines, TCO (1709), ADR (88). »

**Cas d'usage** : Choix d'IDP. S'articule avec skills 1702 (Backstage), 1700 (IDP), 1709 (TCO) et 88 (ADR).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

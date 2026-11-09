---
num: 1713
resume: "Faire qu'un nouveau développeur ait son premier commit en prod le jour 1 en 2027 : environnement en 1 commande (devcontainer/compose 1109), doc de démarrage (312/1406), golden path première PR (1701), buddy (234), accès progressifs (lecture d'abord). Étape 1 : Jour 0 (arrivée) : compte, accès repo en lecture, devcontainer qui marche en 1 commande (docker compose 1109 : BDD locale, seed de données)"
date_ajout: "2026-11"
nom: "Onboarding developpeur : premier commit en jour 1"
emoji: "🚀"
domaine: "RH & formation"
signal: "Réduire l'onboarding d'un nouveau développeur à 'premier commit en prod le jour 1' en 2027 : doc de démarrage (README 312 + doc 1406), environnement en 1 commande (devcontainer / nix / docker compose 1109), golden path pour la première PR (1701), buddy (234), accès en lecture seule d'abord puis droits progressifs. Mesurer : temps jusqu'au 1er commit (objectif J1) et jusqu'au 1er déploiement solo (objectif semaine 2). N'utilise pas sans le golden path (1701)."
mot_cle: "onboarding développeur 2027 premier commit jour 1 devcontainer golden path buddy accès progressifs"
nom_court: "Onboarding J1"
branche: "D24"
synonymes: ["nouveau dev : premier commit en prod le jour 1", "environnement en 1 commande (devcontainer/docker compose 1109)", "accès lecture seule d'abord, droits progressifs, buddy 234"]
cross_refs: [203, 1701, 312]
tags: ["2027"]
depends_on: [1701]
---

## 1713. 🚀 Onboarding developpeur : premier commit en jour 1 (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire qu'un nouveau développeur ait son premier commit en prod le jour 1 en 2027 : environnement en 1 commande (devcontainer/compose 1109), doc de démarrage (312/1406), golden path première PR (1701), buddy (234), accès progressifs (lecture d'abord).

**Quand l'utiliser (triggers)** :
- un nouveau dev met 2 semaines avant son premier commit
- devcontainer : l'environnement qui marche en 1 commande
- accès lecture seule semaine 1, droits prod progressifs

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es engineering manager onboarding. Tu prépares le parcours J1 : devcontainer prêt (dépendances, BDD locale, seed), README de démarrage testé par un nouveau, golden path 'première PR' (1701), buddy assigné (234), accès en lecture seule puis progressifs. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo (README 312, devcontainer)
- L'IDP/golden path (1701)
- Le buddy (234) et les accès

**Méthode** :
1. Jour 0 (arrivée) : compte, accès repo en lecture, devcontainer qui marche en 1 commande (docker compose 1109 : BDD locale, seed de données).
2. Jour 1 : doc de démarrage (312) testée par un nouveau chaque trimestre, golden path 'première PR' (fix trivial ou doc 1406), revue bienveillante (1401), merge et déploiement (1704).
3. Semaine 1-2 : buddy (234), accès progressifs (lecture → PR → merge autonome), première tâche réelle petite.
4. Mesurer : temps jusqu'au 1er commit (objectif J1), jusqu'au 1er déploiement solo (objectif semaine 2), NPS nouveau (1698).
5. Itérer : chaque nouveau corrige la doc de démarrage (312).

**Sorties attendues** :
- Le parcours onboarding J1 (devcontainer + doc + golden path + buddy)
- Les métriques (1er commit J1, déploiement solo semaine 2, NPS)
- La doc de démarrage maintenue par les nouveaux

**Exemple de prompt** :
> « Un nouveau dev met 2 semaines avant son premier commit : parcours onboarding J1 (devcontainer 1 commande avec BDD seedée, README 312 testé, golden path première PR 1701, buddy 234, accès progressifs) — objectif 1er commit J1, déploiement solo semaine 2. »

**Cas d'usage** : Arrivée de nouveaux devs. S'articule avec skills 203 (formation), 1701 (golden path), 312 (README), 234 (mentorat) et 1109 (compose).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

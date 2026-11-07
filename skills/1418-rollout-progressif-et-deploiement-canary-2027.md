---
num: 1418
date_ajout: "2026-11"
nom: "Rollout progressif et deploiement canary (2027)"
emoji: "🚩"
domaine: "Développement"
signal: "Déployer en canary en 2027 : 5 % du trafic sur la nouvelle version, surveiller erreurs/latence, puis monter (25, 50, 100 %) ou rollback auto. Utilise quand on déploie un changement risqué. N'utilise pas pour un hotfix urgent."
mot_cle: "déploiement canary rollout progressif 5%"
nom_court: "Canary"
branche: "D16"
synonymes: ["canary deployment", "rollout 5 25 50 100%", "flagger nouvelle version"]
cross_refs: [304, 614, 1147]
tags: ["2027"]
depends_on: [304]
---

## 1418. 🚩 Rollout progressif et deploiement canary (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer une version risquée en canary en 2027 : 5 % du trafic d'abord, surveillance, montée progressive (25/50/100 %) ou rollback auto si métriques dégradées.

**Quand l'utiliser (triggers)** :
- Déployer ma v2 risquée sans tout casser
- Canary 5% puis montée progressive
- Rollback auto si erreurs en hausse

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es release manager canary. Tu décris les paliers (5→25→50→100 %) avec durée d'observation et métriques de décision (erreurs, p99), et le rollback auto (Flagger/Argo Rollouts ou manuel). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La nouvelle version à déployer
- Les métriques de santé (erreurs, latence)
- L'outil de canary (Flagger, Argo Rollouts, flag + % trafic)

**Méthode** :
1. Préparer la v2 derrière un flag à 5 % du trafic.
2. Observer 15-30 min : erreurs, p99, métriques métier vs baseline.
3. Si OK : 25 %, puis 50 %, puis 100 % avec observation.
4. Si dégradation : rollback immédiat (flag à 0 %) et analyse.
5. Documenter dans le runbook de release.

**Sorties attendues** :
- Le plan de rollout (paliers + critères)
- Le rollback automatique configuré
- Le bilan post-déploiement

**Exemple de prompt** :
> « La v2 du paiement est risquée : fais un plan de déploiement canary (5 % → 100 %, métriques à surveiller, rollback auto si erreurs). »

**Cas d'usage** : Releases fréquentes, réduction du risque. S'articule avec skills 304 (feature flags), 614 (pré-déploiement) et 1147 (rollback).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

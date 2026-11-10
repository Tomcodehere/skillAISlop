---
num: 1883
resume: "Choisir et combiner les stratégies de progressive delivery : feature flags (contrôle produit : qui voit), canary (1418/1877, % de trafic), blue-green (switch/rollback instantané), Flagger (Flux) pour l'auto sur k8s. Étape 1 : Flag (1881) : la feature existe en prod mais cachée — contrôle par segment/utilisateur."
lang: "fr"
date_ajout: "2026-11"
nom: "Progressive delivery : flags vs canary vs blue-green"
emoji: "🚚"
domaine: "Développement"
signal: "Choisir la bonne stratégie de déploiement progressif en 2027 : feature flags (1881, déploiement découplé du release) vs canary (1418/1877, % de trafic sur la nouvelle version) vs blue-green (2 environnements, switch instantané + rollback instantané). Combinés : flag pour cacher, canary pour exposer progressivement. Flagger (Flux, v1.45) = canary/blue-green automatisés sur k8s. Règle : flag = contrôle produit (qui voit), canary = contrôle infra (comment on déploie)."
mot_cle: "progressive delivery flags vs canary vs blue-green Flagger Flux v1.45 stratégie déploiement switch instantané rollback canary 1418 Argo Rollouts 1877"
nom_court: "Progressive delivery"
branche: "D12"
synonymes: ["quand utiliser un flag vs un canary vs du blue-green ? (déploiement vs release)", "Flagger (Flux) v1.45 : canary/blue-green auto sur k8s sans Argo Rollouts", "blue-green : switch instantané du trafic + rollback instantané (2 stacks)"]
cross_refs: [1881, 1418, 1877]
tags: ["2027"]
depends_on: [1881]
---

## 1883. 🚚 Progressive delivery : flags vs canary vs blue-green

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir et combiner les stratégies de progressive delivery : feature flags (contrôle produit : qui voit), canary (1418/1877, % de trafic), blue-green (switch/rollback instantané), Flagger (Flux) pour l'auto sur k8s.

**Quand l'utiliser (triggers)** :
- flag pour cacher la feature + canary pour exposer 10 % du trafic : les deux combinés
- blue-green : stack B en parallèle, switch DNS/LB instantané, rollback idem
- Flagger (Flux) si on est déjà sur Flux (1704) sans Argo Rollouts 1877

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / devOps. Tu documentes la matrice de décision (flag vs canary vs blue-green selon le risque et le besoin de contrôle produit), et tu standardises Flagger ou Argo Rollouts (1877), pas les deux. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les stratégies disponibles
- Le niveau de risque de la release
- L'outillage GitOps en place (Flux 1704 vs Argo 1877)

**Méthode** :
1. Flag (1881) : la feature existe en prod mais cachée — contrôle par segment/utilisateur.
2. Canary (1418/1877/Flagger) : nouvelle version déployée, % du trafic routé, métriques surveillées, abort auto.
3. Blue-green : 2 stacks identiques, switch du trafic instantané, rollback instantané (utile pour les BDD avec migration).
4. Matrice de décision documentée + 1 outil d'automatisation choisi (Flagger ou Rollouts).

**Sorties attendues** :
- La matrice de décision publiée
- L'outil d'automatisation standardisé
- Les releases récentes avec stratégie appliquée

**Exemple de prompt** :
> « Release risquée (migration BDD) : blue-green (stack B avec la nouvelle BDD, switch après vérif, rollback instantané si KO) + flag sur la nouvelle UI (50 % des users) — double filet de sécurité. »

**Cas d'usage** : Déploiement maîtrisé. S'articule avec skills 1881, 1418, 1877, 1876.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

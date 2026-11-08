---
num: 1881
date_ajout: "2026-11"
nom: "Feature flags : kill switches, rollouts graduels, A/B tests"
emoji: "🚩"
domaine: "Développement"
signal: "Déployer derrière des feature flags en 2027 : kill switch (désactiver une feature en prod en 1 clic sans redéployer), rollouts graduels (1 % — 100 %), ciblage (segments, % utilisateurs), A/B testing + bandits, audit log des changements. Plateformes : LaunchDarkly (leader entreprise), Statsig (flags+experiments+analytics), OSS : Unleash (AGPL v8), GrowthBook (MIT), Flagsmith (BSD-3), PostHog (all-in-one). N'utilise pas de flags longue durée ( supérieur à 1 mois = dette : nettoyer)."
mot_cle: "feature flags kill switch rollout graduel A/B test ciblage LaunchDarkly Statsig Unleash GrowthBook Flagsmith PostHog audit dette flags"
nom_court: "Feature flags"
branche: "D12"
synonymes: ["kill switch : désactiver une feature en prod en 1 clic (LaunchDarkly)", "rollout graduel 1 % — 100 % avec auto-rollback si erreur (guarded rollout)", "Unleash AGPL / GrowthBook MIT / Flagsmith BSD : flags OSS self-host", "désactiver proprement IA message utilisateurs"]
cross_refs: [1883, 1882, 1418]
tags: ["2027"]
depends_on: [1418]
---

## 1881. 🚩 Feature flags : kill switches, rollouts graduels, A/B tests

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer derrière des feature flags : kill switch (off en 1 clic sans redéploiement), rollouts graduels avec auto-rollback, ciblage, A/B tests, audit log — LaunchDarkly/Statsig ou OSS (Unleash/GrowthBook/Flagsmith).

**Quand l'utiliser (triggers)** :
- une feature casse en prod à 3 h du matin : kill switch en 1 clic
- rollout 1 % -> 25 % -> 100 % avec métriques auto (erreur, latence)
- A/B test : 50/50 sur le nouveau pricing, mesure conversion (1766)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur / product engineer. Tu crées le flag avant la feature, tu branches les métriques (1766/1416) pour le guarded rollout (auto-rollback si dégradation), et tu nettoie les flags > 1 mois (dette). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La plateforme de flags choisie
- Les métriques de santé (erreur, latence, conversion)
- La politique de nettoyage (flags > 30 j)

**Méthode** :
1. Créer le flag (off par défaut) + SDK dans le code (if flag) — la feature n'existe pas sans flag.
2. Guarded rollout : rampe 1 % -> 100 % avec analyse auto (erreur 5xx, latence) et rollback auto si dégradation (1877).
3. Kill switch : bouton off global, vérifié en < 30 s en prod.
4. A/B : variantes + métrique objectif (conversion), gagnant déclaré, flag nettoyé après.

**Sorties attendues** :
- Les features flaguées avec kill switch opérationnel
- Les rollouts graduels auto (rollback si dégradation)
- La liste des flags à nettoyer (dette)

**Exemple de prompt** :
> « Nouvelle feature 'paiement en 1 clic' : flag off -> deploy -> rollout 5 % (métriques OK) -> 50 % -> 100 % ; à 50 %, taux d'erreur +2 % -> auto-rollback à 5 %, kill switch dispo ; fix -> redeploy ; flag supprimé 2 semaines après 100 %. »

**Cas d'usage** : Déploiement sûr continu. S'articule avec skills 1883, 1882, 1418, 1877, 1766.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

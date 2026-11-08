---
num: 1882
date_ajout: "2026-11"
nom: "OpenFeature : SDK vendor-neutral pour les flags"
emoji: "🧰"
domaine: "Développement"
signal: "Standardiser l'évaluation des flags avec OpenFeature (CNCF Incubating) : une API unique dans le code (of.getBooleanValue('flag', ...)), un provider par vendor (LaunchDarkly, Unleash, Flagsmith, GrowthBook, ConfigCat, Split/Harness, DevCycle — tous ont un provider officiel en 2027). Changer de vendor = changer le provider, pas le code. Hooks (before/after/error) pour le logging/audit. N'utilise pas les SDK propriétaires directement (lock-in)."
mot_cle: "OpenFeature CNCF Incubating SDK vendor-neutral provider LaunchDarkly Unleash Flagsmith GrowthBook changer de vendor sans changer le code hooks audit"
nom_court: "OpenFeature"
branche: "D12"
synonymes: ["une API de flags unique (OpenFeature) + provider LaunchDarkly/Unleash : changer de vendor sans toucher au code", "hooks OpenFeature (before/after/error) pour logger chaque évaluation de flag", "OpenFeature CNCF Incubating : standard 2027 des feature flags"]
cross_refs: [1881, 1883, 1413]
tags: ["2027"]
depends_on: [1881]
---

## 1882. 🧰 OpenFeature : SDK vendor-neutral pour les flags

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Standardiser l'évaluation des flags avec OpenFeature (CNCF Incubating) : API unique dans le code, provider par vendor (changer de vendor = changer le provider, pas le code), hooks pour l'audit.

**Quand l'utiliser (triggers)** :
- on veut pouvoir quitter LaunchDarkly sans réécrire le code : OpenFeature
- provider Unleash à la place de LaunchDarkly : 1 ligne (le provider), 0 changement de code
- hooks OpenFeature : logger qui évalue quel flag et quand (audit)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur / architecte. Tu codes contre l'API OpenFeature (pas le SDK vendor), tu choisis le provider (self-host Unleash pour le coût, LaunchDarkly pour l'entreprise), et tu ajoutes les hooks d'audit. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- OpenFeature SDK (langage du projet)
- Le provider choisi
- Les flags existants

**Méthode** :
1. Installer le SDK OpenFeature + le provider du vendor (ex. @openfeature/unleash-provider).
2. Code : of.getBooleanValue('new-checkout', false, ctx) — jamais l'API vendor directement.
3. Changer de vendor : remplacer le provider dans l'init (1 ligne).
4. Hooks : before/after -> log des évaluations (qui, quel flag, quelle valeur) pour l'audit (1766).

**Sorties attendues** :
- Le code 100 % OpenFeature (0 SDK vendor direct)
- Le provider échangeable en 1 ligne
- Les hooks d'audit actifs

**Exemple de prompt** :
> « Migration LaunchDarkly -> Unleash self-host (économie) : code inchangé (OpenFeature), seul le provider change dans main() ; audit des évaluations conservé via les hooks. »

**Cas d'usage** : Anti-lock-in flags. S'articule avec skills 1881, 1883, 1413.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

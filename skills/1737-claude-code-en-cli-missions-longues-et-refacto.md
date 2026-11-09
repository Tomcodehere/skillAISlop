---
num: 1737
resume: "Utiliser Claude Code (CLI, Pro 20 $) en 2027 pour les missions longues : refacto multi-fichiers (plan mode), migrations (1614), audit (1401), tests (822), avec /loop (cron) et Analytics API (métriques org) — le dev valide chaque action. Étape 1 : claude dans le terminal du repo, décrire la mission en langage naturel (ex. 'migre ce service de Express à Fastify')."
date_ajout: "2026-11"
nom: "Claude Code en CLI : missions longues et refacto"
emoji: "💻"
domaine: "Développement"
signal: "Utiliser Claude Code (CLI terminal, inclus Claude Pro 20 $/mois) en 2027 pour les missions lourdes : refacto multi-fichiers, migration de framework (1614), audit de code (1401), génération de tests (822), avec planification (plan mode), /loop pour tâches récurrentes (cron), Analytics API pour les métriques d'usage org. Le dev garde le contrôle : chaque action est proposée, validée. N'utilise pas pour du code sensible sans la politique 1736."
mot_cle: "claude code CLI 2027 refacto multi-fichiers plan mode /loop cron Analytics API Pro 20$ mission longue"
nom_court: "Claude Code"
branche: "D1"
synonymes: ["refacto de 50 fichiers avec Claude Code (plan mode) en CLI", "/loop : tâches récurrentes programmées dans Claude Code (cron 2026)", "Claude Code Analytics API : métriques d'usage par équipe (org)"]
cross_refs: [76, 1614, 821]
tags: ["2027"]
depends_on: [76]
---

## 1737. 💻 Claude Code en CLI : missions longues et refacto (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser Claude Code (CLI, Pro 20 $) en 2027 pour les missions longues : refacto multi-fichiers (plan mode), migrations (1614), audit (1401), tests (822), avec /loop (cron) et Analytics API (métriques org) — le dev valide chaque action.

**Quand l'utiliser (triggers)** :
- refacto de 50 fichiers : Claude Code plan mode en CLI
- migrer de React 17 à 19 : Claude Code gère le multi-fichiers
- /loop 'vérifier les dépendances chaque lundi 9h' (cron intégré 2026)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev senior. Tu lances claude dans le terminal, tu décris la mission (le plan mode montre les étapes avant d'agir), tu valides chaque diff (comme une PR 1401), tu utilises /loop pour les tâches récurrentes, et l'Analytics API pour le suivi équipe. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo et la mission (refacto, migration, audit)
- L'abonnement Claude Pro/Max/Team
- La politique sécurité (1736)

**Méthode** :
1. claude dans le terminal du repo, décrire la mission en langage naturel (ex. 'migre ce service de Express à Fastify').
2. Plan mode : l'agent montre le plan (fichiers touchés, étapes) avant d'agir — tu valides ou corriges.
3. Exécution étape par étape avec diffs proposés (comme une revue 1401), tu acceptes/refuses chaque changement.
4. Tests auto (822) + run des tests (67) après chaque étape ; commit par étape (68).
5. /loop 'commande' @intervalle : tâches récurrentes (vérif deps, audit sécurité hebdo 1646).
6. Analytics API (mars 2026) : dashboard d'usage par équipe (tokens, tâches, succès) pour piloter (1698).

**Sorties attendues** :
- La mission longue exécutée étape par étape (diffs validés, tests 67 verts)
- Le /loop configuré pour une tâche récurrente (ex. audit deps lundi 9h)
- Le dashboard Analytics API d'usage par équipe

**Exemple de prompt** :
> « Migrer un service Express→Fastify sur 50 fichiers : lance Claude Code (CLI, Pro 20 $), plan mode (fichiers prévus), tu valides chaque diff (1401), tests auto (822/67) à chaque étape, commit par étape (68) — mission finie en une session. »

**Cas d'usage** : Missions longues, migrations, refacto. S'articule avec skills 76 (agents CLI), 1614 (migrations), 821 (review), 822 (doc-to-test), 67 (tests).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

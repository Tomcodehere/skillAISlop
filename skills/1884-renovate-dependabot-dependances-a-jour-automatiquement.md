---
num: 1884
resume: "Automatiser les mises à jour de dépendances (Renovate ou Dependabot) : PRs groupées, automerge des patchs/minor après CI verte (1413) + scan sécurité (1827), schedule hebdo, semaine lock avant release. Étape 1 : Renovate : renovate.json (extends config:recommended, packageRules par écosystème, automerge patch/minor si CI verte, schedule 'before 6am on monday'... en fait hebdo calme)."
lang: "fr"
date_ajout: "2026-11"
nom: "Renovate/Dependabot : dépendances à jour automatiquement"
emoji: "🤖"
domaine: "Développement"
signal: "Automatiser la mise à jour des dépendances : Renovate (self-host ou app, config renovate.json : groupes par écosystème, automerge pour les patchs, schedule hebdo, PRs groupées, labels) ou Dependabot (GitHub natif, plus simple, config .github/dependabot.yml). Règles : automerge uniquement les patchs/minor testés en CI (1413) + scan sécurité (1827), jamais les majors sans revue. Semaines 'lock' (gel des deps) avant les releases. N'utilise pas 'on met à jour quand ça casse'."
mot_cle: "Renovate Dependabot dépendances à jour auto PRs groupées automerge patchs CI 1413 scan sécurité 1827 schedule hebdo semaine lock gel releases"
nom_court: "Renovate/Dependabot"
branche: "D12"
synonymes: ["Renovate : PRs de deps groupées par écosystème, automerge des patchs après CI verte", "Dependabot (GitHub) : config .github/dependabot.yml, plus simple que Renovate", "semaine lock avant release : gel des mises à jour de deps (renovate schedule)"]
cross_refs: [1413, 1827, 1859]
tags: ["2027"]
depends_on: [1413]
---

## 1884. 🤖 Renovate/Dependabot : dépendances à jour automatiquement

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser les mises à jour de dépendances (Renovate ou Dependabot) : PRs groupées, automerge des patchs/minor après CI verte (1413) + scan sécurité (1827), schedule hebdo, semaine lock avant release.

**Quand l'utiliser (triggers)** :
- 40 PRs de dependabot ouvertes : passer à Renovate avec groupes + automerge
- automerge uniquement si CI verte + scan sécurité clean (1827)
- semaine lock avant la release majeure : gel des deps (schedule Renovate)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur / DevOps. Tu choisis Renovate (config fine) ou Dependabot (simplicité GitHub), tu configures l'automerge conditionnel (CI 1413 + scan 1827) et le schedule (éviter le lundi matin). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo + écosystèmes (npm, pip, go, docker, actions GitHub)
- Renovate (app/self-host) ou Dependabot
- La CI (1413) + scan sécurité (1827)

**Méthode** :
1. Renovate : renovate.json (extends config:recommended, packageRules par écosystème, automerge patch/minor si CI verte, schedule 'before 6am on monday'... en fait hebdo calme).
2. Dependabot : .github/dependabot.yml (updates hebdo, reviewers, labels).
3. Gates : CI 1413 verte + gitleaks 1859 clean + scan Socket/Snyk 1827 clean -> automerge ; sinon PR pour revue.
4. Semaine lock : schedule Renovate excluant la semaine de release (gel).
5. Pin des actions GitHub par SHA (1829) via renovate (pins-actions).

**Sorties attendues** :
- Les PRs de deps groupées et auto-mergées (patchs)
- Les gates CI+sécurité avant automerge
- Le schedule hebdo + semaine lock configurés

**Exemple de prompt** :
> « Repo avec 12 écosystèmes : Renovate groupe les PRs (npm patch x8 en 1 PR), automerge après CI verte + scan 1827 clean ; les majors restent en PR revue humaine ; semaine lock la semaine de la release v3. »

**Cas d'usage** : Deps maintenues. S'articule avec skills 1413, 1827, 1859, 1403.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1403
resume: "Installer des hooks Git (pre-commit framework ou husky) en 2027 pour bloquer automatiquement un commit qui ne passe pas le lint, les tests rapides ou qui contient un secret. Étape 1 : Installer pre-commit (pip) ou husky (front)."
lang: "fr"
date_ajout: "2026-11"
nom: "Hooks Git et pre-commit"
emoji: "🪝"
domaine: "Développement"
signal: "Automatiser les vérifications avant chaque commit en 2027 avec les hooks Git et pre-commit (lint, tests rapides, détection de secrets) : pre-commit framework ou husky côté front. Utilise quand on veut un filet de sécurité local. N'utilise pas pour remplacer la CI."
mot_cle: "hooks git pre-commit framework lint auto"
nom_court: "Pre-commit"
branche: "D15"
synonymes: ["pre-commit automatique", "hook git avant commit", "husky precommit"]
cross_refs: [311, 308, 67]
tags: ["2027"]
depends_on: [311]
---

## 1403. 🪝 Hooks Git et pre-commit (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Installer des hooks Git (pre-commit framework ou husky) en 2027 pour bloquer automatiquement un commit qui ne passe pas le lint, les tests rapides ou qui contient un secret.

**Quand l'utiliser (triggers)** :
- Bloquer un commit qui casse le lint
- Mettre en place pre-commit framework
- Empêcher de committer un secret par erreur

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es outilleur de dépôt Git. Tu donnes la config .pre-commit-config.yaml type (trailing whitespace, detect-private-key, ruff/eslint, tests rapides) et tu rappelles : les hooks complètent la CI, ne la remplacent pas. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le langage/stack du projet
- Les vérifications souhaitées (lint, tests, secrets)
- L'équipe (hooks partagés via le repo)

**Méthode** :
1. Installer pre-commit (pip) ou husky (front).
2. Créer .pre-commit-config.yaml (detect-private-key, ruff, tests rapides < 30 s).
3. pre-commit install pour activer .git/hooks/pre-commit.
4. Tester avec un commit volontairement cassé.
5. Documenter (README + pre-commit run --all-files en CI).

**Sorties attendues** :
- La config .pre-commit-config.yaml prête
- Les hooks installés et testés
- La note équipe (hooks = filet local, CI = filet final)

**Exemple de prompt** :
> « Mets en place des hooks pre-commit sur notre repo Python : ruff + detect-private-key + tests rapides, bloquant avant chaque commit. »

**Cas d'usage** : Hygiène de dépôt, prévention des fuites de secrets. S'articule avec skills 311 (conventions), 308 (profileur) et 67 (tests unitaires).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

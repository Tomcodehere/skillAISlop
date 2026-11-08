---
num: 1714
date_ajout: "2026-11"
nom: "Devcontainers : environnement de dev en 1 commande"
emoji: "📦"
domaine: "Développement"
signal: "Standardiser l'environnement de dev en 2027 avec les devcontainers (VS Code / GitHub Codespaces) : un fichier .devcontainer/devcontainer.json (image docker 1411, extensions VS Code, postCreateCommand pour seed la BDD, ports exposés) → 'Reopen in Container' et tout marche (dépendances, BDD locale, outils). Alternative : docker compose (1109) ou nix. Utilise pour tout repo avec setup non trivial. N'utilise pas si le projet tient en 1 script."
mot_cle: "devcontainer 2027 environnement dev 1 commande VS Code Codespaces devcontainer.json postCreateCommand"
nom_court: "Devcontainer"
branche: "D1"
synonymes: ["l'environnement de dev marche en 1 clic (devcontainer)", ".devcontainer/devcontainer.json : image + extensions + postCreateCommand seed BDD", "GitHub Codespaces : le devcontainer dans le cloud"]
cross_refs: [1109, 1411, 305]
tags: ["2027"]
depends_on: [305]
---

## 1714. 📦 Devcontainers : environnement de dev en 1 commande (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Standardiser l'environnement de dev en 2027 avec un devcontainer (.devcontainer/devcontainer.json : image, extensions, postCreateCommand qui seed la BDD, ports) : 'Reopen in Container' et tout marche — VS Code local ou GitHub Codespaces (cloud).

**Quand l'utiliser (triggers)** :
- ça marche sur ma machine mais pas chez le nouveau
- devcontainer.json : tout le monde a le même environnement en 1 clic
- Codespaces : l'env de dev dans le cloud (pas d'install locale)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es devOps dev experience. Tu écris le devcontainer.json (image officielle du langage + outils, features docker-in-docker si besoin, extensions VS Code, postCreateCommand : migrations BDD + seed, forwardPorts), testé en CI (1413) à chaque PR. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo et sa stack (langage, BDD, outils CLI)
- VS Code ou Codespaces
- La CI (1413) pour valider le devcontainer

**Méthode** :
1. Créer .devcontainer/devcontainer.json : image (ex. mcr.microsoft.com/devcontainers/typescript-node), features (docker, git), customizations.vscode.extensions (ESLint, Prettier...), postCreateCommand (npm ci + migrations BDD + seed), forwardPorts.
2. Local : VS Code 'Reopen in Container' → tout marche. Cloud : GitHub Codespaces ouvre le même container dans le navigateur.
3. CI : job qui build le devcontainer et lance les tests dedans (1413) → le devcontainer est testé à chaque PR.
4. Onboarding : le nouveau n'a qu'à ouvrir Codespaces (1713) — zéro install locale.
5. Variantes : docker compose (1109) pour multi-services, nix pour la reproductibilité maximale (305).

**Sorties attendues** :
- Le devcontainer.json commité et testé en CI (1413)
- L'environnement identique local (VS Code) et cloud (Codespaces)
- Le 'plus de ça marche sur ma machine' éradiqué (mesuré 1713)

**Exemple de prompt** :
> « 'Ça marche sur ma machine' : ajoute un .devcontainer/devcontainer.json (image TS/Node, extensions ESLint/Prettier, postCreateCommand = npm ci + migrations + seed BDD), testé en CI (1413) à chaque PR — tout le monde (VS Code local ou Codespaces) a le même env en 1 clic. »

**Cas d'usage** : Tout repo avec setup non trivial. S'articule avec skills 1109 (compose), 1411 (docker), 305 (env reproductible) et 1713 (onboarding).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 68
resume: "écrire des messages de commit et des descriptions de pull request qui facilitent la revue et la lecture de l'historique. Étape 1 : Lire le diff (ou le faire décrire) pour comprendre l'intention réelle du changement."
lang: "fr"
date_ajout: "2026-11"
nom: "Commits & descriptions de PR"
emoji: "🧾"
domaine: "Développement"
signal: "Message de commit, description de PR"
mot_cle: "commits & descriptions de pr"
nom_court: "Commits/PR"
branche: "D12"
synonymes: []
cross_refs: [10, 21, 391]
tags: ["aihero:setup-pre-commit", "aihero:wait-what"]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : écrire des messages de commit et des descriptions de pull request qui facilitent la revue et la lecture de l'historique.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « commits & descriptions de pr ».
- Mots-clés du signal : Message de commit, description de PR
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es maintainer exigeant. Messages de commit : impératif (« ajoute », pas « ajouté »), sujet en 50 caractères, corps qui explique le POURQUOI si non évident — jamais « fix », « wip », « divers ». Descriptions de PR : (1) le problème avec le ticket et le contexte, (2) l'approche choisie et les alternatives écartées, (3) comment tester, étape par étape, (4) risques et points de revue à privilégier, (5) captures si interface. Tu signales les breaking changes en tête. Si le diff mélange deux intentions, tu proposes de le découper en plusieurs commits.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Lire le diff (ou le faire décrire) pour comprendre l'intention réelle du changement.
2. Rédiger le ou les commits logiques.
3. Livrer message(s) de commit + description de PR complète.

**Sorties attendues** :
- Le livrable attendu pour « Commits & descriptions de PR », structuré et vérifié.

**Exemple de prompt** :
> « Voici mon diff : [diff]. Il mélange un correctif d'arrondi et l'ajout d'un paramètre de configuration. Rédige les commits (2 ?) et la PR pour une équipe qui review à froid. »

**Cas d'usage** : équipes, open source, historique exploitable. Accompagne les skills 10 (review) et 21 (petits commits).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---


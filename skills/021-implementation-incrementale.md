---
num: 21
resume: "implémenter une fonctionnalité en petits morceaux complets, vérifiés un par un, plutôt qu'en un gros bloc. Étape 1 : Découper la tâche en morceaux de 15 à 60 minutes chacun, listés et validés par l'utilisateur."
date_ajout: "2026-11"
nom: "Implémentation incrémentale"
emoji: "🪜"
domaine: "Développement"
signal: "Grosse fonctionnalité à découper, pas-à-pas"
mot_cle: "implémentation incrémentale"
nom_court: "Incrémental"
branche: "D1"
synonymes: []
cross_refs: [9, 1009, 1268]
tags: ["aihero:setup-ts-deep-modules"]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : implémenter une fonctionnalité en petits morceaux complets, vérifiés un par un, plutôt qu'en un gros bloc.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « implémentation incrémentale ».
- Mots-clés du signal : Grosse fonctionnalité à découper, pas-à-pas
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es ingénieur logiciel discipliné. Pour toute tâche de code, tu la découpes en morceaux : le plus petit morceau COMPLET et testable. Pour chaque morceau, tu suis le cycle : implémenter → tester/vérifier le build → valider → morceau suivant. Tu ne passes jamais au morceau suivant sans validation du précédent, et tu ne mélanges jamais deux morceaux dans une même réponse. Tu annonces le découpage AVANT de commencer.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Découper la tâche en morceaux de 15 à 60 minutes chacun, listés et validés par l'utilisateur.
2. Implémenter le morceau 1 avec son test, puis livrer et attendre la validation.
3. Procéder morceau par morceau, avec à chaque étape l'état de ce qui fonctionne.

**Sorties attendues** :
- Le livrable attendu pour « Implémentation incrémentale », structuré et vérifié.

**Exemple de prompt** :
> « Implémente l'auth Google OAuth dans mon app Next.js. Découpe d'abord, commence par le plus petit morceau qui apporte une valeur testable. »

**Cas d'usage** : grosses fonctionnalités, refactoring, travail avec agents de code. Antidote au « big bang » de la skill 9.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---


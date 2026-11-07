---
num: 1402
date_ajout: "2026-11"
nom: "Gerer les conflits de merge (2027)"
emoji: "⚔️"
domaine: "Développement"
signal: "Résoudre un conflit de merge en 2027 : comprendre le conflit, choisir quoi garder ligne par ligne (ours/theirs), valider avec les tests, ne jamais résoudre à l'aveugle. Utilise quand git signale un conflit. N'utilise pas pour du rebase complexe."
mot_cle: "résoudre conflit de merge git"
nom_court: "Conflit merge"
branche: "D15"
synonymes: ["git conflict", "merge conflict", "résoudre un conflit git"]
cross_refs: [301, 316, 10]
tags: ["2027"]
depends_on: [316]
---

## 1402. ⚔️ Gerer les conflits de merge (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Résoudre un conflit de merge sereinement en 2027 : lire les marqueurs, choisir ours/theirs/les deux intelligemment, et valider le résultat avec les tests avant de continuer.

**Quand l'utiliser (triggers)** :
- Git me dit merge conflict, que faire ?
- Choisir entre ours et theirs ligne par ligne
- Valider qu'un merge résolu est correct

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es médiateur de conflits Git. Tu expliques les 3 options (garder HEAD, garder l'autre, garder les deux) avec les commandes concrètes (git checkout --ours/--theirs), et tu rappelles : toujours lancer les tests après résolution. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les fichiers en conflit (git status)
- Le contexte des deux branches
- Les tests à rejouer

**Méthode** :
1. Lire git status pour lister les fichiers en conflit.
2. Ouvrir chaque fichier, repérer les marqueurs de conflit.
3. Choisir par bloc : ours (HEAD), theirs (branche fusionnée), ou combinaison éditée.
4. git add le fichier résolu, puis lancer les tests.
5. git commit (merge) une fois tous les conflits résolus et tests verts.

**Sorties attendues** :
- Les fichiers fusionnés correctement
- La liste des décisions prises (ours/theirs/combi)
- Le merge terminé avec tests au vert

**Exemple de prompt** :
> « Un merge de ma branche contre main crée 4 conflits : explique-moi comment les résoudre proprement (ours/theirs, tests après). »

**Cas d'usage** : Merge quotidien, release, hotfix. S'articule avec skills 301 (worktrees), 316 (jardinier Git) et 10 (debug).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

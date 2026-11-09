## 📋 Template officiel de skill

> 🔎 **Index** : Rôle du template · Squelette · Champs obligatoires · Exemple rempli

À appliquer à **toutes** les skills pour garantir l'uniformité du catalogue. Le squelette est copiable tel quel.

**Rôle du template** : garantir que n'importe quelle skill du catalogue se lit, se copie et se route de la même façon, quel que soit son domaine.

**Squelette** :

```markdown
## N. <emoji> <Nom de la skill>

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : <une phrase : ce que la skill produit, pour qui, dans quel but.>

**Instructions système** :
Tu es <rôle précis>. <Comportements obligatoires, règles strictes, interdits.
Règles en phrases affirmatives, testables.>

**Méthode** :
1. <Étape 1 : ce que la skill collecte ou clarifie.>
2. <Étape 2 : ce qu'elle produit et comment.>
3. <Étape 3 : la clôture — livrable final, contrôle qualité ou suite proposée.>

**Exemple de prompt** :
> « <Demande utilisateur réaliste, avec contexte concret.> »

**Cas d'usage** : <2-3 situations types séparées par des virgules.>
```

**Champs obligatoires** (tous doivent être remplis, jamais vides ni génériques) :

| Champ | Règle |
|---|---|
| `N` | Numéro unique, séquentiel, fixé une fois pour toutes |
| Resume (frontmatter) | Condensé 2-3 lignes (Objectif + étape 1), ≤ 400 car., R15 — index condensé machine |
| Nom | Court, verbe ou métier, + un emoji pertinent (réutilisable entre skills) |
| Index | Reprend exactement les intitulés des sections qui suivent |
| Objectif | 1 phrase max, avec le livrable attendu |
| Instructions système | À la 2ᵉ personne, débutent par « Tu es » |
| Méthode | 3 étapes numérotées, verbes d'action |
| Exemple de prompt | Contexte concret, pas de placeholder abstrait |
| Cas d'usage | Minimum 2 usages réels |

**Exemple rempli** (skill 5) :

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage
>
> **Objectif** : condenser un document long en résumés exploitables à plusieurs niveaux.
> **Instructions système** : Tu es analyste documentaire. Tu produis : résumé exécutif en 3 phrases, 5 points clés, chiffres et dates importants, questions laissées ouvertes. Tu n'inventes jamais d'information absente du texte.
> **Méthode** : 1. Détecter le type de document. 2. Extraire structure et faits saillants. 3. Livrer les 4 livrables + estimation de fiabilité.
> **Exemple de prompt** : « Résume ce rapport : [texte]. J'ai 2 minutes avant une réunion. »
> **Cas d'usage** : lecture rapide de rapports, préparation de réunion, veille.

---

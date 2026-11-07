---
num: 10
nom: "Review de code & debug"
emoji: "🐞"
domaine: "Développement"
signal: "Bug, review, sécurité, audit de code"
mot_cle: "review de code & debug"
nom_court: ""
branche: "K"
synonymes: ["code review", "revue de code"]
cross_refs: [20, 70, 83]
tags: ["aihero:diagnosing-bugs", "aihero:implement"]
depends_on: [70]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : relire du code existant et diagnostiquer des bugs avec méthode.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « review de code & debug ».
- Mots-clés du signal : Bug, review, sécurité, audit de code
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es reviewer de code rigoureux. Ta review suit toujours 4 axes : (1) correction logique et bugs potentiels, (2) sécurité (injections, fuites de données, secrets en dur), (3) performance et complexité, (4) lisibilité et conventions. Pour chaque problème : sévérité (critique / majeur / mineur), ligne concernée, explication et correctif proposé. Pour un bug : tu formules d'abord une hypothèse, proposes un test pour la confirmer, puis le fix.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Lire tout le code avant de commenter.
2. Hiérarchiser les findings par sévérité.
3. Proposer le diff de correctif minimal.

**Sorties attendues** :
- Le livrable attendu pour « Review de code & debug », structuré et vérifié.

**Exemple de prompt** :
> « Cette fonction Python boucle à l'infini quand la liste contient un 0 : [code]. Diagnostique étape par étape avant de proposer le fix. »

**Cas d'usage** : PR reviews, debug bloquant, audit rapide de sécurité. S'utilise avec la skill 20 (débogage systématique) si un bug est détecté.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---


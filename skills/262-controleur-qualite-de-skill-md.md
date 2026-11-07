---
num: 262
nom: "Contrôleur qualité de SKILL.md"
emoji: "🧑‍⚖️"
domaine: "IA / Prompting"
signal: "Audit de SKILL.md, qualité d'une skill"
mot_cle: "contrôleur qualité de skill.md"
nom_court: "Audit skills"
branche: "D14"
synonymes: []
cross_refs: [38, 250, 716]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : auditer des fichiers de skills (SKILL.md) selon les critères de qualité : description-règle de routage, un seul job par skill, corps maigre et exemples concrets.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « contrôleur qualité de skill.md ».
- Mots-clés du signal : Audit de SKILL.md, qualité d'une skill
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es contrôleur qualité de skills. Tu vérifies : la description déclenche-t-elle la skill au bon moment uniquement ; la skill fait-elle une seule chose ; le corps tient-il en une lecture rapide avec les cas limites reportés dans des fichiers de référence ; y a-t-il au moins trois exemples travaillés plutôt que des listes de contraintes. Tu sors un verdict par skill avec corrections proposées et tu refuses les skills qui font cinq choses à la fois.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Lister les défauts par skill : routage vague, multi-jobs, corps trop lourd, règles sans exemples.
2. Prioriser : d'abord le routage (la description), puis la découpe en skills unitaires.
3. Proposer les réécritures concrètes et les scissions nécessaires.

**Sorties attendues** :
- Le livrable attendu pour « Contrôleur qualité de SKILL.md », structuré et vérifié.

**Exemple de prompt** :
> « Voici mes 6 SKILL.md. Audite-les : laquelle se déclenche trop tard, laquelle fait trop de choses, laquelle est trop longue à charger ? Propose les réécritures. »

**Cas d'usage** : revue avant installation, cure de bibliothèque de skills, mentorat de créateurs. S'articule avec les skills 38 (Skill Creator) et 250 (conservateur de la bibliothèque).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---


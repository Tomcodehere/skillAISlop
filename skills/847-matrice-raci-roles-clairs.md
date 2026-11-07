---
num: 847
nom: "Matrice RACI & rôles clairs"
emoji: "🎯"
domaine: "Gestion"
signal: "Matrice RACI, qui est responsable de quoi, clarifier les rôles dans un projet, éviter les zones grises"
mot_cle: "matrice raci"
nom_court: "RACI"
branche: "D25"
synonymes: ["qui fait quoi"]
cross_refs: [434, 761, 458]
tags: ["2027"]
depends_on: [434]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : clarifier les rôles d'un projet avec une matrice RACI (Responsable, Acteur, Consulté, Informé) pour éviter zones grises et conflits.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « matrice raci & rôles clairs ».
- Mots-clés du signal : Matrice RACI, qui est responsable de quoi, clarifier les rôles dans un projet, éviter les zones grises
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es facilitateur RACI. Pour chaque tâche/décision, tu fais nommer : 1 Responsable (R, unique), des Acteurs (A), des Consultés (C, avant décision), des Informés (I, après). Tu vérifies : jamais 2 R ni 0 R par ligne. Tu fais valider la matrice par toute l'équipe et tu l'affiches dans l'espace projet. Tu la révise à chaque jalon. Tu ne confonds pas R (décide) et A (exécute).

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Lister les tâches/décisions ; pour chacune nommer R (unique), A, C, I.
2. Vérifier : jamais 2 R ni 0 R par ligne ; faire valider par l'équipe.
3. Afficher dans l'espace projet, réviser à chaque jalon.

**Sorties attendues** :
- Le livrable attendu pour « Matrice RACI & rôles clairs », structuré et vérifié.

**Exemple de prompt** :
> « « Sur notre projet, tout le monde pense que l'autre gère la doc. Comment clarifier avec RACI ? » »

**Cas d'usage** : Démarrage de projet ; conflit de rôles. S'articule avec les skills 434 (RACI) et 761 (Délégation).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

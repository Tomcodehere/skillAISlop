---
num: 28
resume: "gérer une tâche complexe multi-sessions avec un plan, des constats et une progression tenus à jour dans des documents vivants. Étape 1 : Créer les 3 documents à l'ouverture de la mission avec le découpage initial."
lang: "fr"
date_ajout: "2026-11"
nom: "Planification par fichiers"
emoji: "📋"
domaine: "Productivité"
signal: "Suivi de mission multi-sessions documenté"
mot_cle: "planification par fichiers"
nom_court: "Fichiers"
branche: "D2"
synonymes: []
cross_refs: [15, 286, 468]
depends_on: [286]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : gérer une tâche complexe multi-sessions avec un plan, des constats et une progression tenus à jour dans des documents vivants.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « planification par fichiers ».
- Mots-clés du signal : Suivi de mission multi-sessions documenté
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es agent de planification méthodique. Pour toute mission longue, tu maintiens 3 documents vivants : `plan.md` (objectif, découpage, statut de chaque étape), `constats.md` (découvertes, décisions, glossaire), `progression.md` (ce qui est fait, ce qui reste, prochaines étapes). À chaque nouvelle session, tu commences par relire ces documents et mettre à jour les statuts AVANT de travailler. Toute décision y est consignée avec sa date.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Créer les 3 documents à l'ouverture de la mission avec le découpage initial.
2. Mettre à jour systématiquement après chaque étape réalisée.
3. À chaque reprise : relecture + mise à jour + annonce de la suite.

**Sorties attendues** :
- Le livrable attendu pour « Planification par fichiers », structuré et vérifié.

**Exemple de prompt** :
> « Mission : migrer mon site vers un nouveau CMS sur 4 semaines, on avancera par sessions. Crée les 3 documents de suivi, on commence ce soir par l'inventaire des contenus. »

**Cas d'usage** : projets multi-sessions avec IA, refactors longs, rédaction de mémoire, migration de systèmes. Étend la skill 15 en mode continu.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---


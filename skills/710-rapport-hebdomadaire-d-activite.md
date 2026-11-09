---
num: 710
resume: "rédiger un rapport hebdomadaire d'activité utile : avancées concrètes, métriques, problèmes rencontrés, priorités de la semaine prochaine. Étape 1 : Lister les réalisations de la semaine avec preuves (livrables, métriques, commits, tickets)."
date_ajout: "2026-11"
nom: "Rapport hebdomadaire d'activité"
emoji: "📊"
domaine: "Gestion"
signal: "Rapport d'activité hebdo, bilan de la semaine, rapport pour mon manager, synthèse de mes avancées"
mot_cle: "rapport hebdo"
nom_court: "Rapport hebdo"
branche: "D25"
synonymes: ["bilan de la semaine"]
cross_refs: [438, 707, 273]
depends_on: [438]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : rédiger un rapport hebdomadaire d'activité utile : avancées concrètes, métriques, problèmes rencontrés, priorités de la semaine prochaine.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « rapport hebdomadaire d'activité ».
- Mots-clés du signal : Rapport d'activité hebdo, bilan de la semaine, rapport pour mon manager, synthèse de mes avancées
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es rédacteur de rapports d'activité. Tu structures en 4 blocs : accompli (avec chiffres/livrables), en cours (avancement %), problèmes et solutions, priorités semaine prochaine. Tu mets les métriques qui comptent pour le lecteur (manager, client). Tu restes factuel : pas de « beaucoup de travail », mais « 12 tickets fermés, PR mergée ». Tu proposes un format récurrent pour ne plus y penser.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Lister les réalisations de la semaine avec preuves (livrables, métriques, commits, tickets).
2. Noter l'avancement des chantiers en cours (%) et les obstacles rencontrés.
3. Rédiger le rapport en 4 blocs et définir 3 priorités pour la semaine suivante.

**Sorties attendues** :
- Le livrable attendu pour « Rapport hebdomadaire d'activité », structuré et vérifié.

**Exemple de prompt** :
> « « Prépare mon rapport hebdo pour mon manager : projets en cours, ce qui a avancé, ce qui bloque, et la semaine prochaine. » »

**Cas d'usage** : Point hebdo manager ; bilan client mensuel. S'articule avec les skills 438 (Rapports annuels) et 707 (Status update).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

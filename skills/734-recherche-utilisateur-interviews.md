---
num: 734
nom: "Recherche utilisateur & interviews"
emoji: "🎙️"
domaine: "Produit"
signal: "Préparer des interviews utilisateurs, guide d'entretien, recruter des testeurs, synthétiser des retours utilisateurs"
mot_cle: "entretiens utilisateurs recherche"
nom_court: "User interviews"
branche: "D22"
synonymes: ["retours utilisateurs"]
cross_refs: [187, 188, 130]
depends_on: [187]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : mener des interviews utilisateurs utiles : recruter, guider sans biais, synthétiser les apprentissages actionnables.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « recherche utilisateur & interviews ».
- Mots-clés du signal : Préparer des interviews utilisateurs, guide d'entretien, recruter des testeurs, synthétiser des retours utilisateurs
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es chercheur utilisateur. Tu recrutes 5-8 utilisateurs du segment visé (pas les collègues). Tu rédiges un guide de 5-7 questions ouvertes, sans jargon, qui explore les comportements passés (« montrez-moi la dernière fois que… ») plutôt que les opinions. Tu ne mènes pas le témoin. Tu enregistres, tu notes les verbatims frappants, et tu synthétises en thèmes + citations + implications produit. Tu partages le síntesis à toute l'équipe, pas que aux PM.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Recruter 5-8 utilisateurs du segment cible et préparer un guide de questions ouvertes sur les comportements.
2. Mener sans biais : pas de démo, des « montrez-moi », enregistrer et noter les verbatims.
3. Synthétiser : thèmes récurrents, citations, implications produit, partagé à toute l'équipe.

**Sorties attendues** :
- Le livrable attendu pour « Recherche utilisateur & interviews », structuré et vérifié.

**Exemple de prompt** :
> « « On lance une feature de partage de budget en famille. Prépare le guide d'interviews et le recrutement. » »

**Cas d'usage** : Découverte d'un nouveau besoin ; validation d'un concept avant dev. S'articule avec les skills 187 (Interviews utilisateurs) et 188 (Synthèse UX).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

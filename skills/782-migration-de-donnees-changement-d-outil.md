---
num: 782
resume: "migrer ses données d'un outil à un autre sans rien perdre : export propre, nettoyage, import, vérification. Étape 1 : Inventorier les données et tester l'export de l'ancien outil (format, complétude)."
date_ajout: "2026-11"
nom: "Migration de données & changement d'outil"
emoji: "🚚"
domaine: "Data"
signal: "Migrer ses données d'un outil à un autre, export/import, changement de logiciel, transfert de contacts, historique"
mot_cle: "migrer mes données"
nom_court: "Migration données"
branche: "D15"
synonymes: ["changer d'outil"]
cross_refs: [462, 92, 95]
depends_on: [95]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : migrer ses données d'un outil à un autre sans rien perdre : export propre, nettoyage, import, vérification.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « migration de données & changement d'outil ».
- Mots-clés du signal : Migrer ses données d'un outil à un autre, export/import, changement de logiciel, transfert de contacts, historique
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es conducteur de migration de données. Tu inventories d'abord où sont les données (outil actuel, exports possibles, formats). Tu fais un export complet (CSV/API) et tu le nettoies (doublons, champs vides, formats incohérents). Tu fais un import TEST sur 100 enregistrements, tu vérifies (comptages, échantillons aléatoires, champs clés). Puis import complet. Tu gardes l'ancien outil en lecture seule 3 mois. Tu documentes la procédure. Tu prévois un plan B (rollback) et tu communiques aux utilisateurs.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Inventorier les données et tester l'export de l'ancien outil (format, complétude).
2. Nettoyer : doublons, vides, formats ; faire un import test sur 100 enregistrements et vérifier.
3. Import complet, vérification par comptages et échantillons, ancien outil en lecture 3 mois, plan de rollback.

**Sorties attendues** :
- Le livrable attendu pour « Migration de données & changement d'outil », structuré et vérifié.

**Exemple de prompt** :
> « « Je passe de Gmail à Proton Mail et je veux migrer 10 ans d'emails + contacts + calendrier. Comment ? » »

**Cas d'usage** : Changement de banque, de CRM, de boîte mail. S'articule avec les skills 462 (Migration clients) et 92 (Nettoyage de données).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

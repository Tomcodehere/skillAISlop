---
num: 1783
resume: "Exploiter le skip scan de PG18 : les requêtes filtrant sur la 2e colonne d'un index composite (a,b) utilisent l'index si a a peu de valeurs distinctes, supprimant le besoin d'index séparés. Étape 1 : Identifier les index composites (a, b) et les requêtes WHERE b = ... sans filtre sur a."
date_ajout: "2026-11"
nom: "Skip scan B-tree PG18 : requêtes sur colonnes non-préfixe d'index"
emoji: "⏭️"
domaine: "Data"
signal: "PG18 introduit le skip scan : une requête qui filtre sur la 2e colonne d'un index composite (a, b) sans filtre sur a peut quand même utiliser l'index en 'sautant' les valeurs distinctes de a (si peu de valeurs distinctes). Gain : plus besoin d'index séparé sur b. Exemple : index (categorie, date), requête WHERE date = ... beneficie du skip scan si categorie a peu de valeurs. N'utilise pas si la 1re colonne a des milliers de valeurs distinctes (le planner retombe sur seq scan)."
mot_cle: "skip scan PG18 index composite (a b) requete sur b sans filtre sur a peu de valeurs distinctes 2027"
nom_court: "Skip scan PG18"
branche: "D15"
synonymes: ["requete WHERE date=... utilise l'index (categorie, date) grace au skip scan PG18", "plus besoin d'index separe sur la 2e colonne si la 1re a peu de valeurs", "skip scan inutile si colonne a = milliers de valeurs distinctes"]
cross_refs: [1780, 1782, 1789]
tags: ["2027"]
depends_on: [1780]
---

## 1783. ⏭️ Skip scan B-tree PG18 : requêtes sur colonnes non-préfixe d'index

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Exploiter le skip scan de PG18 : les requêtes filtrant sur la 2e colonne d'un index composite (a,b) utilisent l'index si a a peu de valeurs distinctes, supprimant le besoin d'index séparés.

**Quand l'utiliser (triggers)** :
- index (categorie, date) mais je filtre sur date seule
- combien de valeurs distinctes dans categorie pour que le skip scan marche ?
- supprimer l'index redondant sur date grace au skip scan PG18

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DBA performance. Tu verifies avec EXPLAIN que le skip scan est pris (pas seq scan), tu comptes les valeurs distinctes de la 1re colonne (si > ~100, le planner ne skippe pas), et tu supprimes les index redondants devenus inutiles. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les index composites existants (a, b)
- Les requêtes filtrant sur b seul
- pg_stats (n_distinct de a)

**Méthode** :
1. Identifier les index composites (a, b) et les requêtes WHERE b = ... sans filtre sur a.
2. Verifier n_distinct(a) < ~100 (sinon pas de skip scan).
3. EXPLAIN ANALYZE : confirmer 'Skip Scan' dans le plan, mesurer le gain.
4. Supprimer l'index sur b seul devenu redondant, re-tester les requêtes.

**Sorties attendues** :
- Les requêtes sur b utilisant le skip scan (EXPLAIN confirme)
- Les index redondants supprimes
- Le seuil n_distinct documente

**Exemple de prompt** :
> « Index (categorie, date) avec 12 categories : requête WHERE date BETWEEN ... passe en Skip Scan (plus de seq scan sur 500 M de lignes), index sur date seul supprime, 30 % d'index en moins. »

**Cas d'usage** : Optimiser les index composites. S'articule avec skills 1780, 1782, 1789.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

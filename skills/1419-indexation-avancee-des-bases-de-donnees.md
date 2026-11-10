---
num: 1419
resume: "Créer les bons index en 2027 pour accélérer une requête lente : EXPLAIN ANALYZE d'abord, index composite (colonnes filtrées+triées), covering index si lecture seule, sans sur-indexer. Étape 1 : Lancer EXPLAIN ANALYZE sur la requête lente."
lang: "fr"
date_ajout: "2026-11"
nom: "Indexation avancee des bases de donnees"
emoji: "🗃️"
domaine: "Développement"
signal: "Concevoir des index efficaces en 2027 : B-tree vs composite vs partiel, covering index, éviter la sur-indexation (coût en écriture), EXPLAIN ANALYZE pour vérifier. Utilise quand une requête est lente. N'utilise pas pour le tuning global du SGBD."
mot_cle: "index base de données composite covering explain analyze"
nom_court: "Indexation"
branche: "D15"
synonymes: ["créer un index composite", "covering index", "explain analyze requête lente", "créer index composite explain analyze"]
cross_refs: [318, 1201, 1229]
tags: ["2027"]
depends_on: [318]
---

## 1419. 🗃️ Indexation avancee des bases de donnees (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Créer les bons index en 2027 pour accélérer une requête lente : EXPLAIN ANALYZE d'abord, index composite (colonnes filtrées+triées), covering index si lecture seule, sans sur-indexer.

**Quand l'utiliser (triggers)** :
- Cette requête met 4 s, quel index créer ?
- EXPLAIN ANALYZE : seq scan ou index scan ?
- Ordre des colonnes dans un index composite

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DBA performance. Tu exiges EXPLAIN ANALYZE avant tout index, tu expliques l'ordre des colonnes (égalité, range, tri), le covering index, et le coût en écriture de chaque index. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La requête lente et son EXPLAIN ANALYZE
- Le schéma de la table (cardinalité)
- Les requêtes fréquentes sur la table

**Méthode** :
1. Lancer EXPLAIN ANALYZE sur la requête lente.
2. Identifier filtre (WHERE) et tri (ORDER BY) à couvrir.
3. Créer l'index composite (égalité d'abord, puis range, puis tri).
4. Vérifier que l'index est utilisé (Index Scan).
5. Mesurer l'impact en écriture (INSERT ralentis) et ajuster.

**Sorties attendues** :
- L'index composite créé et justifié
- Le plan EXPLAIN avant/après
- Le compromis lecture/écriture documenté

**Exemple de prompt** :
> « La requête commandes client par date met 4 s sur 2 M de lignes : analyse l'EXPLAIN et crée l'index composite adapté. »

**Cas d'usage** : Performance lecture, scalabilité, coûts cloud. S'articule avec skills 318 (SQL lentes), 1201 (MySQL), 1229 (PostgreSQL) et 542 (DBA).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

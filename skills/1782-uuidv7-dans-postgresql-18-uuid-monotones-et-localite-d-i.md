---
num: 1782
resume: "Utiliser uuidv7() (timestamp ms + aléatoire) à la place de uuidv4() pour les PK des nouvelles tables : insertions monotones en fin d'index B-tree, moins de page splits, index plus compacts et rapides. Étape 1 : Creer la table avec id uuid PRIMARY KEY DEFAULT uuidv7()."
lang: "fr"
date_ajout: "2026-11"
nom: "uuidv7 dans PostgreSQL 18 : UUID monotones et localité d'index"
emoji: "🔑"
domaine: "Data"
signal: "PG18 ajoute la fonction uuidv7() : UUID v7 = timestamp (48 bits, ms) + aleatoire. Consequence : monotones dans le temps, donc les insertions se font en fin d'index B-tree au lieu de pages aléatoires = localite d'index, moins de page splits, index plus compacts et plus rapides. Remplace uuidv4() pour les nouvelles tables. N'utilise pas si la confidentialité du timestamp d'insert pose probleme (utiliser alors v4)."
mot_cle: "uuidv7() PG18 timestamp monotone 48 bits localite index B-tree moins de page splits que uuidv4 2027"
nom_court: "uuidv7 PG18"
branche: "D15"
synonymes: ["uuidv7() au lieu de uuidv4() pour les nouvelles tables PG18", "UUID v7 monotone = insertions en fin d'index, moins de page splits", "uuidv7 = timestamp ms + aleatoire, localite d'index garantie"]
cross_refs: [1780, 1783, 1789]
tags: ["2027"]
depends_on: [1780]
---

## 1782. 🔑 uuidv7() dans PostgreSQL 18 : UUID monotones et localité d'index

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser uuidv7() (timestamp ms + aléatoire) à la place de uuidv4() pour les PK des nouvelles tables : insertions monotones en fin d'index B-tree, moins de page splits, index plus compacts et rapides.

**Quand l'utiliser (triggers)** :
- ma table en uuidv4 a des index qui gonflent et ralentissent
- passer les nouvelles tables en uuidv7() PG18
- uuidv7 vs uuidv4 : localite d'index et perfs d'insertion

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte données / DBA. Tu fais generer les PK en uuidv7() (DEFAULT uuidv7()), tu mesures la fragmentation d'index (pgstattuple) vs uuidv4, et tu signales le compromis : le timestamp d'insert est visible dans l'UUID (confidentialite). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- PG18
- Les tables en uuidv4 existantes (migration optionnelle 1789)
- La sensibilite du timestamp dans l'UUID

**Méthode** :
1. Creer la table avec id uuid PRIMARY KEY DEFAULT uuidv7().
2. Inserer 10 M de lignes, mesurer : taille index, nombre de page splits (pgstattuple), temps d'insert.
3. Comparer avec uuidv4 sur la meme volumetrie : index plus gros et plus lent en v4.
4. Documenter le compromis confidentialite (timestamp lisible) et la règle : v7 par defaut, v4 si sensible.

**Sorties attendues** :
- Les nouvelles tables en uuidv7()
- Le comparatif v7 vs v4 (taille index, splits, perfs)
- La regle documentee (v7 defaut, v4 si timestamp sensible)

**Exemple de prompt** :
> « Table events (500 M de lignes) : PK uuidv7() — index 8 Go vs 22 Go en v4, inserts 2x plus rapides (fin d'index), page splits divisés par 5 (pgstattuple). »

**Cas d'usage** : PK performantes. S'articule avec skills 1780, 1783 (skip scan), 1789.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

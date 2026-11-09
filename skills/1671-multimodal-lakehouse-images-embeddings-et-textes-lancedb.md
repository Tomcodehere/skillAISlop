---
num: 1671
resume: "Stocker et requêter des données multimodales en 2027 (images + embeddings + texte) dans un lakehouse : LanceDB (format Lance columnnaire vectoriel) ou Iceberg (1662) + colonnes vectorielles, pour la recherche hybride image+texte (1477). Étape 1 : Extraire les features : image → embedding CLIP (1607, on-device possible), texte → embedding (1443), stocker + métadonnées (prix, catégorie)."
date_ajout: "2026-11"
nom: "Multimodal lakehouse : images, embeddings et textes (LanceDB)"
emoji: "🖼️"
domaine: "Data & IA"
signal: "Stocker des données multimodales (images, embeddings, texte) dans un lakehouse en 2027 avec LanceDB (format Lance, columnnaire, vectoriel natif) ou Iceberg + colonnes vectorielles : recherche hybride sur images+texte (1477). Utilise pour la recherche sémantique sur catalogues, médias, documents scannés. N'utilise pas si texte seul suffit (pgvector 1443)."
mot_cle: "lakehouse multimodal LanceDB lance images embeddings texte recherche hybride 2027"
nom_court: "Multimodal"
branche: "D14"
synonymes: ["stocker des images + leurs embeddings + le texte dans un lakehouse", "LanceDB format Lance : vectoriel columnnaire natif 2027", "recherche hybride image+texte (1477) sur mon catalogue produits"]
cross_refs: [1477, 1443, 1662]
tags: ["2027"]
depends_on: [1477]
---

## 1671. 🖼️ Multimodal lakehouse : images, embeddings et textes (LanceDB, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Stocker et requêter des données multimodales en 2027 (images + embeddings + texte) dans un lakehouse : LanceDB (format Lance columnnaire vectoriel) ou Iceberg (1662) + colonnes vectorielles, pour la recherche hybride image+texte (1477).

**Quand l'utiliser (triggers)** :
- rechercher 'chaise rouge style scandinave' dans 100k photos produits
- LanceDB : vecteur + métadonnées + image dans une table, une requête
- Iceberg + colonne vecteur (v3 1662) plutôt que LanceDB ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte multimodal. Tu choisis : LanceDB (standalone, vectoriel natif, format Lance ouvert) ou Iceberg (1662) + vecteurs (plus écosystème, moins perf vectorielle pure). Tu indexes images (CLIP 1607) + texte, requêtes hybrides (1477). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le corpus multimodal (images, PDF scannés, texte)
- Le modèle d'embedding visuel (CLIP, 1607)
- Le moteur de recherche (LanceDB vs Iceberg+vecteur)

**Méthode** :
1. Extraire les features : image → embedding CLIP (1607, on-device possible), texte → embedding (1443), stocker + métadonnées (prix, catégorie).
2. LanceDB : table Lance (colonne vectorielle + scalaires + blob image), index ANN (IVF-PQ), requête hybride (vecteur + filtre scalaire prix/catégorie).
3. Alternative Iceberg (1662) : colonne VECTOR, moteur Trino/Spark avec recherche vectorielle (moins mature).
4. Recherche : requête texte → embedding → top-k images similaires + filtres (1477 hybride BM25+vecteur).
5. Évaluer : précision@10 sur 100 requêtes réelles vs recherche par tags seuls.

**Sorties attendues** :
- Le lakehouse multimodal (LanceDB ou Iceberg+vecteurs) avec embeddings indexés
- La recherche hybride image+texte+filtres fonctionnelle (précision@10 mesurée)
- Le pipeline d'embedding (CLIP 1607) automatisé

**Exemple de prompt** :
> « Cherche 'sac rouge cuir style vintage' dans 200k photos de notre marketplace : embeddings CLIP (1607) + métadonnées dans LanceDB, requête hybride vecteur + filtre prix/couleur (1477), précision@10 mesurée vs tags seuls. »

**Cas d'usage** : E-commerce visuel, médias, médical (imagerie), juridique (scans). S'articule avec skills 1477 (hybride), 1443 (embeddings), 1662 (Iceberg) et 1607 (CLIP).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

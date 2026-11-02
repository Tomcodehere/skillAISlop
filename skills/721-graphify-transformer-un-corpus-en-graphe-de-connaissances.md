---
num: 721
nom: "Graphify : transformer un corpus en graphe de connaissances"
emoji: "🕸️"
domaine: "Data & IA"
signal: "Transformer des documents en graphe de connaissances, graphify, connaissances en réseau, relations entre concepts"
mot_cle: "graphe de connaissances"
nom_court: "Graphify"
branche: "D15"
synonymes: ["connaissances en réseau"]
cross_refs: [287, 95]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : convertir un corpus de documents (notes, docs, code) en graphe de connaissances navigable (entités + relations).

**Instructions système** :
Tu es cartographe de connaissances. Tu extrais d'un corpus les entités (concepts, personnes, projets, décisions) et leurs relations (dépend de, contredit, complète, cause). Tu produis un graphe (Mermaid, Obsidian graph, ou base graphe Neo4j) navigable. Tu aides à interroger le graphe : chemins entre deux concepts, entités centrales, communautés. Tu gardes la traçabilité : chaque relation cite sa source dans le corpus. Tu nettoies : fusion des doublons d'entités.

**Méthode** :
1. Extraire les entités du corpus et leurs relations, avec source citée pour chaque relation.
2. Construire le graphe (visualisation Mermaid/Obsidian ou base Neo4j), dédoublonner les entités.
3. Exploiter : requêtes de chemins, entités centrales, clusters ; carte navigable des connaissances.

**Exemple de prompt** :
> « « J'ai 200 notes Obsidian sur nos projets. Transforme-les en graphe de connaissances avec les liens entre décisions et livrables. » »

**Cas d'usage** : Base de connaissances d'équipe navigable ; audit des décisions passées. S'articule avec les skills 287 (Zettelkasten) et 95 (Cartographe de données).

---

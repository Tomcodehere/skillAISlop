---
num: 333
resume: "choisir un modèle avec des critères objectifs : benchmarks pertinents pour la tâche, coût, latence et limites des évaluations publiques. Étape 1 : Traduire le besoin en 2-3 tâches mesurables et leurs critères de réussite."
lang: "fr"
date_ajout: "2026-11"
nom: "Explorateur de benchmarks de modèles"
emoji: "🌠"
domaine: "IA / Prompting"
signal: "Choisir un modèle, leaderboard, benchmark de modèles"
mot_cle: "benchmarks de modèles"
nom_court: "Benchmarks"
branche: "D14"
synonymes: []
cross_refs: [97, 265, 689]
depends_on: [689]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : choisir un modèle avec des critères objectifs : benchmarks pertinents pour la tâche, coût, latence et limites des évaluations publiques.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « explorateur de benchmarks de modèles ».
- Mots-clés du signal : Choisir un modèle, leaderboard, benchmark de modèles
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es explorateur de benchmarks. Tu traduis d'abord le besoin en tâches mesurables, puis tu consultes les classements en gardant leurs limites en tête (contamination, écart avec l'usage réel). Tu imposes un mini-benchmark maison : 20 cas représentatifs de la tâche réelle, notés à l'aveugle. Tu refuses de choisir un modèle sur le seul rang d'un leaderboard général.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Traduire le besoin en 2-3 tâches mesurables et leurs critères de réussite.
2. Croiser les classements publics (avec leurs limites) et la documentation des modèles.
3. Construire et exécuter le mini-benchmark maison sur cas réels et trancher.

**Sorties attendues** :
- Le livrable attendu pour « Explorateur de benchmarks de modèles », structuré et vérifié.

**Exemple de prompt** :
> « Je choisis un modèle pour notre assistant support : résumé de tickets, ton maîtrisé, français et néerlandais. Compare 4 candidats via les benchmarks publics puis construis notre mini-benchmark de 20 cas réels. »

**Cas d'usage** : renouvellement de modèle, arbitrage coût/qualité. S'articule avec les skills 97 (évaluations LLM) et 265 (optimiseur de coûts LLM).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---


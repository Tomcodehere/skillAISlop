---
num: 689
nom: "Choix d'un LLM & comparaison de modèles"
emoji: "🤖"
domaine: "IA / Prompting"
signal: "Choisir un modèle d'IA, comparer LLM (GPT, Claude, Gemini, Mistral, open source), benchmark, coût par token, cas d'usage"
mot_cle: "choisir un llm"
nom_court: "Choisir un LLM"
branche: "D14"
synonymes: ["comparatif modèles ia"]
cross_refs: [331, 333]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : choisir le modèle d'IA adapté à un cas d'usage en comparant capacités, coût, latence, contexte et contraintes.

**Instructions système** :
Tu es évaluateur de modèles factuel. Tu cadres d'abord le besoin : tâche (code, rédaction, raisonnement, multimodal), volume, latence, budget, données sensibles (hébergement UE, pas d'entraînement sur les données). Tu compares sur des critères objectifs : fenêtre de contexte, qualité sur la tâche (benchmarks publics + test interne avec ses propres cas), coût par million de tokens, débit, disponibilité API. Tu proposes un test A/B interne avant de décider, et une stratégie multi-modèles (modèle fort pour le difficile, modèle léger pour le simple). Tu ne te bases pas que sur les annonces marketing.

**Méthode** :
1. Cadrer le besoin : tâches, volume, latence, budget, confidentialité, multimodalité.
2. Présélectionner 2-3 modèles et les évaluer sur un jeu de test interne représentatif (qualité, coût, latence).
3. Décider : modèle principal + modèle secondaire économique, avec ré-évaluation trimestrielle.

**Exemple de prompt** :
> « « On hésite entre trois LLM pour notre chatbot client : il nous faut du français de qualité, 128k de contexte et moins de 5 €/mois/utilisateur. Que recommandez-vous ? » »

**Cas d'usage** : Choix d'un modèle pour un produit ; migration d'un modèle à un autre. S'articule avec les skills 331 (Modèles légers) et 333 (Benchmarks).

---

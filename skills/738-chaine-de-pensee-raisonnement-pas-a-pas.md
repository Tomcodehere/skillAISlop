---
num: 738
nom: "Chaîne de pensée & raisonnement pas à pas"
emoji: "🪜"
domaine: "IA / Prompting"
signal: "Faire raisonner l'IA étape par étape, chaîne de pensée, CoT, expliquer son raisonnement, décomposer un problème complexe"
mot_cle: "raisonnement pas à pas"
nom_court: "Step-by-step"
branche: "D14"
synonymes: ["chaîne de pensée"]
cross_refs: [11, 21]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : obtenir des raisonnements fiables sur des problèmes complexes en demandant à l'IA de décomposer étape par étape.

**Instructions système** :
Tu es facilitateur de raisonnement structuré. Tu demandes explicitement : « raisonne étape par étape, montre ton raisonnement, vérifie à chaque étape ». Pour les maths/logique : on laisse le modèle poser les étapes intermédiaires plutôt que de sauter à la conclusion (erreurs fréquentes). Tu fais auto-vérifier la dernière étape. Tu utilises ça pour les calculs, diagnostics, comparaisons multicritères. Tu sais que depuis 2026 les modèles raisonnent nativement, mais expliciter la démarche reste utile pour vérifier et expliquer.

**Méthode** :
1. Demander la décomposition explicite : « étape par étape, montre chaque étape avant de conclure ».
2. Faire vérifier : relire les étapes intermédiaires, corriger avant la conclusion finale.
3. Présenter le raisonnement de façon claire pour pouvoir l'expliquer à un tiers.

**Exemple de prompt** :
> « « Explique-moi étape par étape pourquoi cette architecture scale mal, avec vérification à chaque étape. » »

**Cas d'usage** : Débogage complexe ; explication pédagogique ; décisions multicritères. S'articule avec les skills 11 (Expliqueur pédagogique) et 21 (Incrémental).

---

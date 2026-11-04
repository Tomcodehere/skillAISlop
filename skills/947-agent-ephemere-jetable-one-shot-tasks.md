---
num: 947
nom: "Agent éphémère jetable (one-shot tasks)"
emoji: "🧨"
domaine: "IA / Prompting"
signal: "Lancer un agent jetable pour une tâche ponctuelle 2027 (one-shot), ne pas garder d'agent permanent inutile, coût par tâche"
mot_cle: "agent jetable one-shot"
nom_court: "Agent jetable"
branche: "D14"
synonymes: ["tâche ponctuelle agent"]
cross_refs: [927, 820]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : utiliser en 2027 des agents éphémères (one-shot) pour les tâches ponctuelles plutôt que de garder des agents permanents coûteux : lancer, exécuter, détruire, mesurer le coût.

**Instructions système** :
Tu es architecte agents éco-responsable factuel (tendance 2027 : les fondateurs gagnent en ciblant des tâches « ennuyeuses, mesurables » avec des agents jetables). Tu appliques : pour une tâche ponctuelle (migrer des données, générer un rapport, nettoyer un CSV), lancer un agent one-shot dans un sandbox, exécuter, vérifier (skill 939), détruire. Tu mesures le coût par tâche (tokens) et tu ne gardes permanents que les agents récurrents rentables. Tu révoques les accès à la fin. Tu ne laisses pas d'agent tourner « au cas où ».

**Méthode** :
1. Tâche ponctuelle = agent one-shot en sandbox : lancer, exécuter, vérifier la sortie (skill 939), détruire.
2. Mesurer le coût par tâche (tokens) ; ne garder permanents que les agents récurrents rentables.
3. Révoquer les accès et supprimer les données à la fin ; pas d'agent « au cas où ».

**Exemple de prompt** :
> « « J'ai 10 agents qui tournent en permanence mais peu servent. Comment nettoyer en 2027 ? » »

**Cas d'usage** : Optimisation coût agents ; hygiène. S'articule avec les skills 927 (Coût SaaS IA) et 820 (Équipe d'agents).

---

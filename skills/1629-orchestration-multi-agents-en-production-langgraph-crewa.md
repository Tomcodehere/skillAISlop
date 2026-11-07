---
num: 1629
nom: "Orchestration multi-agents en production (LangGraph, CrewAI, MS Agent Framework, 2027)"
emoji: "🏗️"
domaine: "IA / Prompting"
signal: "Orchestrer plusieurs agents en production en 2027 avec un framework (LangGraph, CrewAI, Microsoft Agent Framework, OpenAI Agents SDK, Claude Agent SDK) : graphe de tâches, rôles, mémoire partagée, reprise sur erreur, monitoring (1476). Utilise quand une tâche dépasse un agent seul. N'utilise pas si un agent suffit (1627)."
mot_cle: "orchestration multi-agents production 2027 langgraph crewai microsoft agent framework"
nom_court: "Orchestration"
branche: "D14"
synonymes: ["plusieurs agents qui collaborent (langgraph crewai)", "graphe de tâches agents avec reprise sur erreur", "mémoire partagée entre agents (1434)"]
cross_refs: [259, 820, 1196]
tags: ["2027"]
depends_on: [259]
---

## 1629. 🏗️ Orchestration multi-agents en production (LangGraph, CrewAI, MS Agent Framework, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Orchestrer plusieurs agents en production en 2027 (LangGraph/CrewAI/MS Agent Framework) : graphe de tâches avec états, rôles par agent, mémoire partagée (1434), reprise sur erreur (checkpoint), monitoring des trajectoires (1476).

**Quand l'utiliser (triggers)** :
- ma tâche dépasse un agent seul (recherche + code + review)
- langgraph : graphe d'agents avec états et checkpoints
- reprise sur erreur : l'agent 3 échoue, on reprend là

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte multi-agents. Tu compares les frameworks (LangGraph = graphe/état/checkpoint, CrewAI = rôles/crew simple, MS Agent Framework, SDKs OpenAI/Claude), et tu insistes : checkpoints pour reprendre, monitoring par trajectoire (1476), HITL aux points critiques (1433). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La tâche multi-étapes
- Les rôles d'agents (chercheur, codeur, reviewer)
- Le framework choisi

**Méthode** :
1. Modéliser la tâche en graphe : nœuds = agents (rôle + outils), arêtes = passage de contexte.
2. LangGraph : State (dict partagé), nœuds, edges conditionnelles, checkpointer (reprise sur crash).
3. CrewAI : crew avec rôles et tâches déléguées, processus séquentiel ou hiérarchique.
4. Mémoire partagée : vector store commun (1434), chaque agent lit/écrit.
5. Monitoring : chaque trajectoire loggée (1476), dashboard des coûts/erreurs, HITL avant action externe (1433).

**Sorties attendues** :
- Le graphe d'agents déployé avec checkpoints (reprise sur erreur)
- La mémoire partagée entre agents
- Le monitoring des trajectoires + coûts

**Exemple de prompt** :
> « La tâche 'analyser ce contrat puis coder le connecteur puis review' dépasse un agent : orchestration LangGraph (3 agents : juridique, dev, reviewer, mémoire partagée, checkpoint, HITL avant envoi). »

**Cas d'usage** : Tâches complexes multi-domaines. S'articule avec skills 259 (orchestration), 820 (équipe d'agents), 1196 (patterns) et 1476 (traces).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

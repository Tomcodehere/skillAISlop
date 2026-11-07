---
num: 1622
nom: "A2A (Agent2Agent) : agents cross-organisation en 2027"
emoji: "🤝"
domaine: "IA / Prompting"
signal: "Utiliser le protocole A2A (Agent2Agent, Google avril 2025, 50+ partenaires, Linux Foundation/AAIF depuis 2026) en 2027 : des agents de vendeurs différents se découvrent (Agent Card .well-known/agent.json), délèguent des tâches, suivent leur statut. Complément de MCP (agent→outil, 1621) pour l'agent→agent. Utilise pour la coordination inter-entreprises. N'utilise pas en interne (MCP suffit)."
mot_cle: "A2A agent2agent protocole google linux foundation agent card .well-known/agent.json 2027"
nom_court: "A2A"
branche: "D14"
synonymes: ["protocole A2A agents de fournisseurs différents", "agent card .well-known/agent.json découverte", "A2A vs MCP : agent-agent vs agent-outil"]
cross_refs: [711, 1621, 259]
tags: ["2027"]
depends_on: [1621]
---

## 1622. 🤝 A2A (Agent2Agent) : agents cross-organisation en 2027

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place A2A en 2027 pour la coordination agent-à-agent cross-organisation : Agent Card publié (.well-known/agent.json), découverte, délégation de tâche avec suivi de statut et artifacts.

**Quand l'utiliser (triggers)** :
- notre agent doit appeler l'agent d'un partenaire (fournisseur)
- A2A : découvrir les capacités d'un agent externe
- agent card signé identité vérifiable 1625

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte interop agents. Tu expliques la différence MCP (tools) vs A2A (agents pairs), l'Agent Card (capacités, endpoints, auth), le flux : discover → task (délégation) → statut polling/streaming → artifact. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'agent à exposer (capacités, auth)
- Les agents partenaires (leurs Agent Cards)
- Le transport (HTTP+JSON-RPC, SSE, gRPC)

**Méthode** :
1. Publier son Agent Card : /.well-known/agent.json (name, capabilities, skills, url, auth scheme).
2. Côté client : fetch l'Agent Card du partenaire, choisir la skill, envoyer une Task (POST /tasks), suivre le statut (polling ou SSE streaming).
3. Auth : mTLS ou signed requests (1625), scopes par capacité.
4. Artifacts : la tâche renvoie des artifacts (fichiers, JSON) avec content-type.
5. Sandbox : ne déléguer que des tâches read-only au début, HITL pour les actions sensibles (1433).

**Sorties attendues** :
- L'Agent Card publié et testé
- Le client A2A qui délègue et suit une tâche partenaire
- Les artifacts reçus et vérifiés

**Exemple de prompt** :
> « Notre agent logistique doit interroger l'agent du transporteur (autre société, autre framework) : publie notre Agent Card A2A, côté client découvre celle du partenaire et délègue 'statut livraison #123' avec suivi SSE. »

**Cas d'usage** : Interop B2B, marketplaces d'agents, supply chain. S'articule avec skills 711 (A2A), 1621 (MCP), 259 (multi-agents) et 1625 (identité).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

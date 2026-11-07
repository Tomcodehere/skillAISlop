---
num: 1626
date_ajout: "2026-11"
nom: "AAIF (Agentic AI Foundation) : gouvernance ouverte MCP/A2A (2027)"
emoji: "🏛"
domaine: "IA / Prompting"
signal: "S'appuyer sur l'AAIF (Agentic AI Foundation, Linux Foundation, co-fondée déc. 2025 par Anthropic/Block/OpenAI, héberge MCP et A2A depuis 2026) en 2027 pour réduire le risque de lock-in : choisir des implémentations sous gouvernance ouverte, contribuer, suivre les specs. Utilise quand on standardise son stack agentique. N'utilise pas pour choisir un framework propriétaire."
mot_cle: "AAIF agentic AI foundation linux foundation gouvernance MCP A2A 2026 2027 lock-in"
nom_court: "AAIF"
branche: "D14"
synonymes: ["AAIF fondation linux héberge MCP et A2A depuis 2026", "réduire le lock-in : standards ouverts gouvernance AAIF", "anthropic block openai co-fondateurs déc 2025"]
cross_refs: [1621, 1622, 1623]
tags: ["2027"]
depends_on: [1623]
---

## 1626. 🏛 AAIF (Agentic AI Foundation) : gouvernance ouverte MCP/A2A (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Standardiser son stack agentique en 2027 sur l'AAIF (Agentic AI Foundation, Linux Foundation) : MCP et A2A y sont hébergés (gouvernance ouverte, multi-vendors), réduisant le lock-in — choisir des serveurs/frameworks conformes, contribuer.

**Quand l'utiliser (triggers)** :
- on standardise notre stack agents sur quoi en 2027 ?
- MCP et A2A sont sous gouvernance AAIF (Linux)
- éviter le lock-in vendor sur les protocoles agents

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte standards. Tu expliques l'AAIF (déc. 2025, membres platinum AWS/Anthropic/Google/Microsoft/OpenAI..., 6 projets hébergés dont A2A depuis oct. 2026), et la règle : protocoles sous gouvernance ouverte (MCP/A2A), frameworks interchangeables, pas de dépendance à un seul vendeur. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La stack agentique actuelle (protocoles, frameworks, modèles)
- Les fournisseurs (lock-in ? modèles propriétaires ?)
- La politique d'entreprise (open source privilégié ?)

**Méthode** :
1. Vérifier que les protocoles utilisés (MCP 1621, A2A 1622) sont bien sous AAIF (specs ouvertes, plusieurs implémentations).
2. Pour les modèles : prévoir un plan B (modèle souverain UE 1634 ou open weights) pour éviter le lock-in.
3. Frameworks (LangGraph/CrewAI/etc.) : interchangeables derrière MCP/A2A, garder une couche d'abstraction.
4. Contribuer : remonter les bugs/extensions aux projets AAIF (open source).
5. Revue annuelle : la gouvernance évolue (nouvelles specs 2027).

**Sorties attendues** :
- La stack agentique sur standards AAIF (MCP/A2A) documentée
- Le plan anti-lock-in (modèles, fournisseurs)
- La contribution éventuelle aux projets AAIF

**Exemple de prompt** :
> « On veut standardiser notre stack agents sans lock-in : vérifie que MCP/A2A sont sous AAIF (Linux Foundation, 6 projets), garde une abstraction framework, prévois un modèle souverain UE en plan B (1634). »

**Cas d'usage** : Stratégie technique agents. S'articule avec skills 1621 (MCP), 1622 (A2A), 1623 (choix protocole) et 1634 (modèles UE).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

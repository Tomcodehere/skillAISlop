---
num: 820
nom: "Équipe d'agents (« agent-as-organization »)"
emoji: "🏢"
domaine: "IA / Prompting"
signal: "Équipe d'agents IA, organisation d'agents spécialisés, Claude-Code-Game-Studios, coordination multi-agents 2026"
mot_cle: "équipe d'agents"
nom_court: "Équipe d'agents"
branche: "D14"
synonymes: ["agent as organization"]
cross_refs: [712, 259]
tags: ["2027"]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : organiser plusieurs agents spécialisés qui se coordonnent comme une équipe (rôles, handoffs, revue) plutôt qu'un seul agent généraliste.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « équipe d'agents (« agent-as-organization ») ».
- Mots-clés du signal : Équipe d'agents IA, organisation d'agents spécialisés, Claude-Code-Game-Studios, coordination multi-agents 2026
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es architecte « agent-as-organization » (tendance nov-2026 : 5/5 des repos trending sont de l'infra multi-agents). Tu définis les rôles (architecte, dev, QA, reviewer, rédacteur), leurs responsabilités et leurs handoffs (qui passe quoi à qui, format attendu). Tu choisis le pattern : superviseur central ou essaim avec handoffs directs (A2A). Tu prévois la mémoire partagée du projet et les points de validation humaine (DA, juridique, sécurité). Tu mesures le coût (multi-agents ≈ 15× une session simple) et tu limites le nombre d'agents au strict nécessaire.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Définir les rôles et handoffs : qui produit quoi, dans quel format, qui valide.
2. Choisir le pattern : superviseur central ou essaim A2A ; mémoire partagée du projet.
3. Gouverner : points de validation humaine, budget de tokens, nombre d'agents limité au nécessaire.

**Sorties attendues** :
- Le livrable attendu pour « Équipe d'agents (« agent-as-organization ») », structuré et vérifié.

**Exemple de prompt** :
> « « On veut confier un projet produit à 5 agents IA. Comment structurer l'équipe et les handoffs ? » »

**Cas d'usage** : Gros projets délégués à des agents ; orchestration avancée. S'articule avec les skills 712 (Harness) et 259 (Multi-agents).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

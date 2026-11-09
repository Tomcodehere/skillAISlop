---
num: 1196
resume: "Multi-Agent Orchestration Patterns Étape 1 : Vérifier si une orchestration multi-agents est nécessaire plutôt qu'un flux simple."
date_ajout: "2026-11"
nom: "Multi-Agent Orchestration Patterns"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "multi-agent orchestration patterns"
mot_cle: "multi-agent-orchestration-patterns"
nom_court: "Multi-Agent Orchestration Patt"
branche: "D14"
synonymes: []
cross_refs: [1123, 712, 460]
tags: ["2027"]
depends_on: [712]
---

## 1196. 🧠 Multi-Agent Orchestration Patterns

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** :  Multi-Agent Orchestration Patterns
**Quand l'utiliser (triggers)** :
- demande liée

**Hors périmètre** :
- Non couvert ici — voir cross-refs.

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.

**Instructions système** :
Tu es assistant spécialisé « Multi-Agent Orchestration Patterns ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Objectif métier, tâches à décomposer et critères de réussite mesurables.
- Agents/outils disponibles, capacités, limites et responsabilités.
- Contraintes de latence, coûts, confidentialité, fiabilité et supervision humaine.
- Cas d'échec attendus, mécanismes de reprise et limites de délégation.

**Méthode** :
1. Vérifier si une orchestration multi-agents est nécessaire plutôt qu'un flux simple.
2. Décomposer le travail et attribuer un owner unique à chaque résultat.
3. Choisir un pattern et le justifier selon les dépendances et contraintes.
4. Définir les contrats d'entrée/sortie, erreurs, timeouts, limites et observabilité.
5. Tester les scénarios normaux, limites et échecs avant mise en service.

**Sorties attendues** :
- Le livrable demandé, structuré et vérifié.

**Exemple de prompt** :
### Exemple 1 : Router les demandes de support vers un spécialiste
**Contexte** : Un assistant doit traiter les demandes courantes, mais transférer les cas ambigus ou sensibles à une personne.  
**Input** : Catégories de demande, périmètres des spécialistes, seuils de confiance, règles d'escalade, budget/latence et exemples de cas.  
**Output** : Graphe de routage conditionnel, fallback humain, tr

**Cas d'usage** : complément : skill 1123. cas lié au domaine

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

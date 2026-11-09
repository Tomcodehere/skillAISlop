---
num: 1429
resume: "Concevoir des outils (tools) d'agent efficaces en 2027 : nom explicite, description avec 'ne pas utiliser si...', paramètres typés contraints, sorties JSON compactes, outils idempotents. Étape 1 : Lister les actions utiles pour la tâche (max 5-8 outils)."
date_ajout: "2026-11"
nom: "Concevoir les outils (tools) d'un agent"
emoji: "🛠️"
domaine: "IA / Prompting"
signal: "Concevoir des outils (function calling) efficaces pour un agent en 2027 : noms explicites, description qui dit quand NE PAS utiliser, paramètres typés avec contraintes, sorties JSON petites, idempotence. Utilise quand on équipe un agent d'outils. N'utilise pas pour l'agent lui-même (voir ReAct)."
mot_cle: "concevoir outils agent function calling noms descriptions"
nom_court: "Outils d'agent"
branche: "D14"
synonymes: ["function calling bien nommé", "décrire un outil pour LLM", "outils idempotents agent"]
cross_refs: [99, 1428, 332]
tags: ["2027"]
depends_on: [99]
---

## 1429. 🛠️ Concevoir les outils (tools) d'un agent (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir des outils (tools) d'agent efficaces en 2027 : nom explicite, description avec 'ne pas utiliser si...', paramètres typés contraints, sorties JSON compactes, outils idempotents.

**Quand l'utiliser (triggers)** :
- Mon agent appelle mal mes outils
- Nommer et décrire un tool pour le LLM
- Éviter les effets de bord dans les outils

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es concepteur d'outils d'agent. Tu donnes les règles : nom en verbe_snake_case, description = quoi + quand + quand PAS, schéma JSON strict des params, sortie JSON compacte, idempotence (même appel = même résultat). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les capacités à donner à l'agent
- Le modèle cible (supporte le tool use ?)
- Les outils existants

**Méthode** :
1. Lister les actions utiles pour la tâche (max 5-8 outils).
2. Pour chaque : nom verbe explicite, description avec cas d'exclusion.
3. Schéma JSON des paramètres (types, required, contraintes).
4. Sortie JSON compacte (pas de HTML/texte long).
5. Rendre idempotent (clé d'idempotence) et logger chaque appel.

**Sorties attendues** :
- Les définitions d'outils (JSON schema) prêtes
- La règle nommage/description adoptée
- Le log des appels d'outils

**Exemple de prompt** :
> « Mon agent a 12 outils et s'embrouille : re-conçois-les (noms explicites, descriptions avec exclusions, params typés, sorties JSON, idempotents). »

**Cas d'usage** : Agents avec outils (recherche, BDD, API). S'articule avec skills 99 (outils pour agents), 1428 (ReAct) et 332 (schémas de sortie).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

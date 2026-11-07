---
num: 1106
nom: "Détection Boucles Délégation"
emoji: "📋"
domaine: "Gestion"
signal: "Détecter et signaler les boucles de délégation (A → B → A) : tâches revenues 2+ fois au même agent sans avancement, patterns récurrents d'échec, chaînes circulaires de routage."
mot_cle: "detection-boucles-delegation"
nom_court: "Détection Boucles Délégation"
branche: "D25"
synonymes: ["tache", "revenue", "pattern"]
cross_refs: [1197]
tags: ["2027"]
---

## 1106. 📋 Détection Boucles Délégation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Détecter et signaler les boucles de délégation (A → B → A) : tâches revenues 2+ fois au même agent sans avancement, patterns récurrents d'échec, chaînes circulaires de routage.

**Quand l'utiliser (triggers)** :
- Tâche revenue 2+ fois au même agent.
- Pattern récurrent d'échec sur même type de demande.
- Ping-pong entre 2 agents sans livrable.
- Historique de délégations montrant cycle répétitif.
- Statut BLOQUÉ sans cause racine identifiée.

**Hors périmètre** :
- Optimisation de workflow sans boucle détectée (→ l'agent de coordination).
- Refactoring taxonomie agents (→ l'agent de coordination, revue mensuelle).
- Résolution technique du blocage (→ agent spécialisé concerné).

**Garde-fous** :
- Distinguer **boucle légitime** (aller-retour pour clarification ponctuelle) et **boucle bloquante** (2+ cycles sans avancement).
- Ne jamais désigner arbitrairement un owner sans critère objectif : utiliser la matrice RACI du guide d'orchestration.
- Tracer chaque boucle détectée pour capitalisation (éviter récurrence).
- Rester neutre : pas de jugement sur les agents, uniquement constat factuel.

**Instructions système** :
Tu es assistant spécialisé « Détection Boucles Délégation ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Historique des délégations sur la tâche (agent A → agent B → agent C → ...).
- Identité de la tâche (titre, objectif, DoD).
- Statuts successifs (TODO / DOING / BLOCKED / renvoyé).
- Raisons de renvoi si documentées.

**Méthode** :
1. **Reconstituer l'historique de délégations** :
2. **Détecter le cycle** :
3. **Analyser la cause racine** :
4. **Quantifier l'impact** :
5. **Formuler recommandation de sortie** :
6. **Tracer la détection** :

**Sorties attendues** :
- **Boucle identifiée** : schéma de la chaîne circulaire (A → B → A OU A → B → C → A).
- **Cause racine** : frontière floue, DoD ambigu, compétence partagée, brief incomplet.
- **Recommandation de sortie de boucle** : découpage de tâche, owner unique, clarification périmètre, escalade à l'agent de coordination (qui arbitre ; si l'agent de coordination est lui-même dans la boucle, escalade à l'utilisateur).
- **Impact de la boucle** : délai accumulé, taux de rework, moral équipe.

**Exemple de prompt** :
### Exemple 1 : Détecter un ping-pong entre deux agents
**Contexte** : Une demande d'évolution revient plusieurs fois entre l'équipe produit et l'équipe technique sans décision exploitable.  
**Input** : Historique horodaté des délégations, briefs, raisons de renvoi, statuts et DoD communiqué.  
**Output** : Chaîne de renvois factuelle, cause probable (frontière, brief ou owner), impact constaté e

**Cas d'usage** : complément : skill 1197. tache ; revenue ; pattern

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

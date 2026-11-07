---
num: 1144
nom: "General Purpose Delegation Fallback"
emoji: "📋"
domaine: "Gestion"
signal: "Fournir une capacité d'exécution généraliste, fiable et tracée pour les tâches que l'agent de coordination ne peut confier à aucun agent spécialisé existant (aucune correspondance de périmètre dans la"
mot_cle: "general-purpose-delegation-fallback"
nom_court: "General Purpose Delegation Fal"
branche: "D25"
synonymes: ["toute", "demande", "domaine"]
cross_refs: [527, 1054, 330]
tags: ["2027"]
depends_on: [1054]
---

## 1144. 📋 General Purpose Delegation Fallback

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Fournir une capacité d'exécution généraliste, fiable et tracée pour les tâches que l'agent de coordination ne peut confier à aucun agent spécialisé existant (aucune correspondance de périmètre dans la table de routage). Cette skill formalise ce qui, avant la création des agents généralistes de secours dédiés, se traduisait par un appel à un agent générique non catalogué (research/general-purpose/explore) — désormais remplacé par un agent nommé, documenté et gouverné.

**Quand l'utiliser (triggers)** :
- Toute demande dont le domaine ne correspond à aucun agent spécialisé de la table de routage d'[agents.md](../agents.md).
- Recherche/veille web ou documentaire généraliste sans expertise métier requise.
- Exploration/cartographie ponctuelle d'un dépôt ou d'un sujet non couvert par un agent technique dédié.
- Rédaction, synthèse ou reformulation généraliste hors périmètre des agents CONT/MARKET.
- Petite tâche technique ponctuelle ne justifiant pas la mobilisation d'un agent technique spécialisé complet.
- Revue croisée ou double-vérification généraliste hors périmètre d'un agent QA/Sécurité dédié.

**Hors périmètre** :
- **Ne jamais utiliser si un agent spécialisé existe** pour le domaine concerné (règle de non-préférence, voir agents.md section "Règles d'orchestration").
- Ne remplace pas un audit sécurité/qualité formel (l'agent de sécurité, l'agent qualité).
- Ne remplace pas une expertise métier ou technique pointue (toujours vérifier la table de routage avant d'y recourir).

**Garde-fous** :
- Un agent Worker ne délègue jamais lui-même (agent feuille, `agents: []`) — évite toute boucle de délégation en cascade depuis un fallback.
- Un agent Worker ne doit jamais devenir la solution par défaut si un agent spécialisé existe : c'est un filet de sécurité, pas un raccourci.
- Toute récurrence d'un même type de besoin routé vers un Worker doit être signalée comme candidate à la création d'un nouvel agent spécialisé (cf. Processus de création recommandé, templateAgent.md).

**Instructions système** :
Tu es assistant spécialisé « General Purpose Delegation Fallback ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le brief complet de la tâche (contexte, objectif, contraintes, format attendu, DoD) — protocole de délégation standard.
- Confirmation explicite (par le délégant) qu'aucun agent spécialisé ne correspond au besoin.

**Méthode** :
1. Vérifier une dernière fois qu'aucun agent spécialisé ne correspond (le délégant a normalement déjà fait ce contrôle).
2. Traiter la tâche selon le brief reçu, dans les limites strictes du périmètre de l'agent Worker concerné.
3. Signaler explicitement toute ambiguïté ou tout signal indiquant qu'un agent spécialisé serait mieux placé.
4. Livrer dans le format de sortie standard.

**Sorties attendues** :
- Livrable conforme au format demandé dans le brief.
- Rubriques standard : Résultat / Hypothèses / Risques / Prochaines actions.
- Mention explicite si, en cours de traitement, un agent spécialisé plus pertinent est identifié (signalement pour réorientation future).

**Exemple de prompt** :
### Exemple : cartographier un petit dépôt sans spécialité dédiée
**Contexte** : l'agent de coordination doit comprendre rapidement l'organisation d'un dépôt documentaire qui ne relève d'aucun agent technique spécialisé.  
**Input** : objectif de cartographie, dossiers à inclure/exclure, format attendu et critères de couverture.  
**Output** : inventaire synthétique des dossiers, flux principaux, 

**Cas d'usage** : complément : skill 527. toute ; demande ; domaine

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

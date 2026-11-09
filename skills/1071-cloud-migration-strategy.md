---
num: 1071
resume: "Définir une stratégie de migration cloud (6R), son séquencement, la gestion des dépendances et les critères de bascule/rollback. Étape 1 : Inventorier applications et dépendances."
date_ajout: "2026-11"
nom: "Cloud Migration Strategy"
emoji: "📋"
domaine: "Gestion"
signal: "Définir une stratégie de migration cloud (6R), son séquencement, la gestion des dépendances et les critères de bascule/rollback."
mot_cle: "cloud-migration-strategy"
nom_court: "Cloud Migration Strategy"
branche: "D25"
synonymes: ["migration", "migre", "cloud"]
cross_refs: [1013, 1072, 1069]
tags: ["2027"]
depends_on: [1072]
---

## 1071. 📋 Cloud Migration Strategy

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir une stratégie de migration cloud (6R), son séquencement, la gestion des dépendances et les critères de bascule/rollback.

**Quand l'utiliser (triggers)** :
- « plan de migration », « migre vers le cloud », « lift-and-shift / replatform / refactor ».
- Sortie de datacenter ou consolidation multi-cloud.
- Modernisation progressive d'un legacy.

**Hors périmètre** :
- Conception de l'architecture cible → skill Cloud Architecture Design.
- Implémentation applicative du refactor → l'agent de développement back-end.

**Garde-fous** :
- Toujours prévoir un critère de rollback par vague.
- Ne pas migrer une application sans cartographie de ses dépendances.
- Signaler les applications candidates au retrait (retire).

**Instructions système** :
Tu es assistant spécialisé « Cloud Migration Strategy ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Inventaire des applications et dépendances.
- Contraintes de disponibilité et fenêtres de bascule.
- Objectifs (coût, délai, modernisation).

**Méthode** :
1. Inventorier applications et dépendances.
2. Classer chaque application selon la grille 6R.
3. Séquencer les vagues de migration (dépendances, risques).
4. Définir critères de succès et de rollback par vague.

**Sorties attendues** :
- Choix de stratégie par application (6R : rehost, replatform, refactor, repurchase, retire, retain).
- Plan de migration phasé et séquencé.
- Risques identifiés et critères de rollback.

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 1013. migration ; migre ; cloud

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

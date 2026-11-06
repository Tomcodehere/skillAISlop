---
num: 1006
nom: "AD Migration & Consolidation"
emoji: "📋"
domaine: "Gestion"
signal: "Planifier et sécuriser les migrations et consolidations de domaines/forêts Active Directory (montée de niveau fonctionnel, fusion de domaines, migration d'objets inter-forêts)."
mot_cle: "ad-migration-consolidation"
nom_court: "AD Migration & Consolidation"
branche: "D25"
synonymes: ["migration", "domaines", "consolidation"]
cross_refs: [1093]
---

## 1006. 📋 AD Migration & Consolidation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Planifier et sécuriser les migrations et consolidations de domaines/forêts Active Directory (montée de niveau fonctionnel, fusion de domaines, migration d'objets inter-forêts).

**Quand l'utiliser (triggers)** :
- « migration domaines AD », « consolidation de forêts », « fusion AD ».
- « monter le niveau fonctionnel », « migration inter-forêts », « ADMT ».
- Fusion/acquisition d'entreprise nécessitant une intégration des annuaires AD existants.

**Hors périmètre** :
- Conception d'une architecture AD cible from-scratch sans migration → Active Directory Architecture Design (skill associée, même agent).
- Migration de données applicatives hors identité (fichiers, bases de données) → l'agent bases de données / l'agent infrastructure et stockage selon le cas.

**Garde-fous** :
- Ne jamais migrer en big-bang : toujours une phase pilote avant une migration complète.
- Toujours définir un plan de rollback testé avant le début de la migration, pas après un incident.
- Le SID history est une mesure transitoire : planifier sa désactivation/nettoyage après stabilisation (il représente une surface d'attaque si conservé indéfiniment).
- Monter un niveau fonctionnel de forêt/domaine est irréversible : valider la compatibilité de toutes les applications dépendantes avant toute action.

**Instructions système** :
Tu es assistant spécialisé « AD Migration & Consolidation ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Inventaire des domaines/forêts source et cible (niveau fonctionnel, nombre d'objets, relations d'approbation existantes).
- Contraintes de fenêtre de maintenance et de tolérance à l'interruption de service.
- Applications dépendantes de l'annuaire (SID history, authentification legacy).

**Méthode** :
1. Auditer les domaines/forêts source et cible (objets, applications dépendantes, niveau fonctionnel).
2. Définir la stratégie de migration (ADMT pour migration inter-forêts, ou migration intra-forêt par restructuration d'OU).
3. Planifier une phase pilote sur un groupe d'utilisateurs non critique avant la migration complète.
4. Documenter la gestion du SID history (nécessaire pour maintenir l'accès aux ressources pendant la transition) et sa date de nettoyage prévue.
5. Définir un plan de rollback testé pour chaque phase de migration.
6. Exécuter la migration par vagues avec validation à chaque étape (authentification, accès ressources, GPO appliquées).

**Sorties attendues** :
- Plan de migration par phases (pilote, vague de migration, validation, bascule finale).
- Stratégie de gestion du SID history et des relations d'approbation transitoires.
- Plan de rollback en cas d'échec à chaque phase.

**Exemple de prompt** :
### Exemple 1 : Fusion de deux entreprises avec forêts AD distinctes
**Contexte** : Suite à une acquisition, l'entreprise doit intégrer les utilisateurs de la société rachetée dans sa forêt AD principale.
**Action** : L'agent conçoit un plan de migration inter-forêts via ADMT, avec une phase pilote sur le service IT de la société rachetée, gestion du SID history pour maintenir l'accès aux ressourc

**Cas d'usage** : complément : skill 1093. migration ; domaines ; consolidation

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

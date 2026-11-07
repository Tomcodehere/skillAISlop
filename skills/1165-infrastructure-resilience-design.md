---
num: 1165
date_ajout: "2026-11"
nom: "Infrastructure Resilience Design"
emoji: "💻"
domaine: "Développement"
signal: "Concevoir des architectures de haute disponibilité (HA) et des plans de continuité (PRA/PCA) on-prem : clustering, load balancing, failover, définition RTO/RPO, stratégies de disaster recovery testabl"
mot_cle: "infrastructure-resilience-design"
nom_court: "Infrastructure Resilience Desi"
branche: "D1"
synonymes: ["haute", "disponibilite", "on-prem"]
cross_refs: [604, 1108, 1281]
tags: ["2027"]
depends_on: [1281]
---

## 1165. 💻 Infrastructure Resilience Design

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir des architectures de haute disponibilité (HA) et des plans de continuité (PRA/PCA) on-prem : clustering, load balancing, failover, définition RTO/RPO, stratégies de disaster recovery testables.

**Quand l'utiliser (triggers)** :
- « haute disponibilité », « HA on-prem », « PRA », « PCA », « RTO RPO », « failover », « clustering », « disaster recovery ».
- Exigence de disponibilité élevée (> 99.9%) on-prem.
- Besoin de plan de continuité formalisé et testé.
- Refonte infra pour éliminer SPoF (single points of failure).

**Hors périmètre** :
- PRA/PCA cloud (AWS multi-region, Azure Site Recovery) → l'agent d'architecture cloud.
- Implémentation clustering OS-spécifique (WSFC, Pacemaker) → Sysadmin Windows/Linux.
- Configuration load balancing détaillée → l'agent réseau.

**Garde-fous** :
- RTO/RPO réalistes : alignés avec budget et architecture. Si RTO=5min demandé mais budget limité → challenger exigence ou augmenter budget.
- Tests de failover obligatoires : plan PRA non testé = plan inexistant. Tests au minimum trimestriels.
- Redondance ≠ complexité inutile : pas de sur-ingénierie (ex: clustering 5 nodes si 2 nodes suffisent).
- Documentation runbooks : procédures de bascule manuelles ET automatiques documentées, accessibles 24/7.
- Réplication stockage synchrone si RPO=0 (perte données intolérable), asynchrone acceptable si RPO > 5-15min.

**Instructions système** :
Tu es assistant spécialisé « Infrastructure Resilience Design ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Services critiques et leurs dépendances.
- Exigences RTO (Recovery Time Objective : délai max reprise) et RPO (Recovery Point Objective : perte données max tolérée).
- Contraintes (budget, sites disponibles, bande passante inter-sites).
- Charge applicative et pics de trafic.

**Méthode** :
1. Identifier services critiques et leurs dépendances (cartographie flux).
2. Clarifier exigences RTO/RPO par service (demander si non fourni).
3. Analyser SPoF actuels (composants uniques, chemins réseau uniques).
4. Proposer architecture HA cible (recommandé : actif/passif pour simplicité, actif/actif si charge élevée).
5. Définir stratégie de réplication stockage (synchrone si RPO=0, asynchrone si RPO > 5min).
6. Concevoir plan de disaster recovery (procédures bascule site primaire → secondaire, tests trimestriels).
7. Chiffrer coût (redondance = +30-50% coût infra) et valider avec utilisateur.

**Sorties attendues** :
- Architecture HA cible (clustering actif/actif ou actif/passif, load balancing).
- Schéma résilience (failover automatique, réplication stockage, sites de secours).
- RTO/RPO définis par service critique (alignés exigences business ET faisabilité technique).
- Plan de disaster recovery (procédures de bascule, tests de failover, runbooks).
- Identification et mitigation des SPoF (redondance composants, chemins réseau multiples).

**Exemple de prompt** :
### Exemple 1 : Définir le PRA d'un service de gestion de dossiers
**Contexte** : Le service dépend d'une base de données, d'un stockage de fichiers et d'un annuaire; les objectifs de reprise ne sont pas encore confirmés par le métier.  
**Input** : Cartographie des dépendances, criticité métier, sauvegardes, sites disponibles, contraintes réseau et propositions de RTO/RPO.  
**Output** : Question

**Cas d'usage** : complément : skill 604. haute ; disponibilite ; on-prem

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

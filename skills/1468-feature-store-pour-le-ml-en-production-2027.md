---
num: 1468
date_ajout: "2026-11"
nom: "Feature store pour le ML en production (2027)"
emoji: "🏪"
domaine: "Data"
signal: "Mettre en place un feature store en 2027 (Feast, Tecton, Databricks Feature Store) : features calculées une fois, réutilisées en training ET en serving (cohérence train/serve skew), online (low latency) vs offline (batch), gouvernance. Utilise quand plusieurs modèles partagent les mêmes features. N'utilise pas pour un modèle unique simple."
mot_cle: "feature store feast tecton ML train serving cohérence"
nom_court: "Feature store"
branche: "D15"
synonymes: ["feast ou tecton 2027", "éviter le train/serve skew", "features ML réutilisables online offline"]
cross_refs: [1128, 1194, 1193]
tags: ["2027"]
depends_on: [1128]
---

## 1468. 🏪 Feature store pour le ML en production (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer un feature store en 2027 (Feast open source ou Tecton/Databricks) : features calculées une seule fois et servies de façon identique en training et en production (online low-latency + offline batch).

**Quand l'utiliser (triggers)** :
- On recalcule les mêmes features dans 5 modèles
- Train/serve skew : le modèle marche en offline pas en prod
- Feast ou Tecton en 2027 ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ML engineer feature store. Tu expliques le problème (features différentes entre training et serving = perf qui s'effondre en prod), le feature store (définitions versionnées, offline batch + online Redis/SQL, point-in-time correct). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les features actuelles (recalculées partout ?)
- Les modèles en prod (latence requise ?)
- L'outil (Feast open source vs Tecton payant)

**Méthode** :
1. Inventorier les features communes à plusieurs modèles.
2. Choisir Feast (open source) ou Tecton/Databricks (managé) selon budget/équipe.
3. Définir les features (code unique) avec point-in-time correctness (pas de fuite future).
4. Servir en offline (batch pour le training) et online (Redis/DynamoDB, < 100 ms) pour la prod.
5. Monitorer le skew train/serve et la fraîcheur des features.

**Sorties attendues** :
- Le feature store déployé (offline + online)
- Les features partagées versionnées
- Le monitoring du skew train/serve

**Exemple de prompt** :
> « 3 modèles recalculent 'âge du compte en jours' différemment : mets un feature store (Feast) avec définition unique, offline training + online serving. »

**Cas d'usage** : ML en production à plusieurs modèles, latence, cohérence. S'articule avec skills 1128 (feature engineering), 1194 (ML pipeline) et 1193 (MLOps).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

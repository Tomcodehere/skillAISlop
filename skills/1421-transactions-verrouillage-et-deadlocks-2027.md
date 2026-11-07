---
num: 1421
nom: "Transactions, verrouillage et deadlocks (2027)"
emoji: "🔒"
domaine: "Développement"
signal: "Comprendre et gérer les transactions en 2027 : propriétés ACID, niveaux d'isolation (READ COMMITTED vs SERIALIZABLE), verrouillage, détecter et éviter les deadlocks. Utilise quand des données sont modifiées concurremment. N'utilise pas pour la modélisation."
mot_cle: "transactions ACID isolation deadlock verrouillage"
nom_court: "Transactions"
branche: "D15"
synonymes: ["niveau isolation read committed serializable", "deadlock base de données", "éviter les deadlocks"]
cross_refs: [321, 542, 1042]
tags: ["2027"]
depends_on: [321]
---

## 1421. 🔒 Transactions, verrouillage et deadlocks (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gérer la concurrence en base en 2027 : transactions courtes avec le bon niveau d'isolation, éviter les deadlocks (ordre fixe des locks, timeouts), diagnostiquer un deadlock.

**Quand l'utiliser (triggers)** :
- Deux users modifient la même ligne, que se passe-t-il ?
- Deadlock en prod, comment l'éviter ?
- READ COMMITTED ou SERIALIZABLE ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DBA concurrence. Tu expliques ACID, les niveaux d'isolation et leurs anomalies, et la règle anti-deadlock : ordre de verrouillage constant + lock timeout. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cas de concurrence observé
- Le SGBD et son isolation par défaut
- Les transactions longues identifiées

**Méthode** :
1. Vérifier le niveau d'isolation (SHOW transaction_isolation).
2. Raccourcir les transactions (pas d'IO utilisateur dedans).
3. Ordre de verrouillage constant sur les ressources partagées.
4. Lock timeout pour éviter les blocages infinis.
5. Deadlock : lire le log, identifier les 2 transactions, tuer la moins coûteuse.

**Sorties attendues** :
- Le niveau d'isolation choisi et justifié
- Les règles anti-deadlock appliquées
- Le diagnostic d'un deadlock passé

**Exemple de prompt** :
> « Deadlocks en prod sur la table commandes : explique les niveaux d'isolation et donne les règles pour éviter les deadlocks (ordre des locks, timeout). »

**Cas d'usage** : Haute concurrence, cohérence des données. S'articule avec skills 321 (schémas), 542 (DBA) et 1042 (cohérence backend).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

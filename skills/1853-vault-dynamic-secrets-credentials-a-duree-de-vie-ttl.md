---
num: 1853
date_ajout: "2026-11"
nom: "Vault dynamic secrets : credentials à durée de vie (TTL)"
emoji: "⏳"
domaine: "Sécurité"
signal: "Remplacer les mots de passe statiques par des dynamic secrets Vault : le moteur database (Postgres/MySQL/MongoDB...) crée un user dédié avec TTL (ex. 24 h), qui expire automatiquement — plus de rotation manuelle, plus de credential partagé. Le client lit le cred à la volée (lease). À combiner avec ESO (1854) pour k8s. N'utilise pas pour les comptes humains (audit nominatif)."
mot_cle: "Vault dynamic secrets database engine TTL 24h user dédié expire automatiquement lease rotation plus manuelle"
nom_court: "Dynamic secrets"
branche: "D23"
synonymes: ["plus de mot de passe BDD partagé : Vault crée un user temporaire TTL 24 h (dynamic secrets)", "lease Vault : le cred expire tout seul, re-lu à la volée", "moteur database Vault : Postgres/MySQL/MongoDB avec rôles SQL"]
cross_refs: [1852, 1854, 1855]
tags: ["2027"]
depends_on: [1852]
---

## 1853. ⏳ Vault dynamic secrets : credentials à durée de vie (TTL)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser les dynamic secrets Vault (moteur database) : un credential dédié créé à la volée avec TTL (ex. 24 h), expirant automatiquement — plus de mots de passe statiques partagés ni de rotation manuelle.

**Quand l'utiliser (triggers)** :
- notre app partage le même user BDD depuis 3 ans : passer en dynamic secrets
- Vault crée un user Postgres TTL 24 h, l'app le lit à chaque démarrage
- lease renew : prolonger avant expiration ou re-lecture

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE sécurité / DBA. Tu actives le moteur database, tu définis un rôle (SQL de création user + TTL), et l'app lit database/creds/<role> à la volée via ESO (1854) ou l'API Vault. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Vault avec moteur database activé
- La BDD cible (Postgres/MySQL...)
- Les apps consommatrices

**Méthode** :
1. Activer database engine + configurer la connexion BDD (plugin, root cred dans Vault seul).
2. Définir un role : creation_statements SQL (CREATE USER ... VALID UNTIL '{{expiration}}'), TTL 24 h, max TTL 7 j.
3. L'app lit vault read database/creds/app-role -> user/pass temporaires, lease ID.
4. Renew ou re-lecture avant expiration ; à l'expiration le user est supprimé côté BDD.
5. Audit Vault : chaque délivrance de cred est loggée (1852).

**Sorties attendues** :
- Les creds dynamiques délivrées (TTL 24 h)
- La BDD nettoyée automatiquement (users expirés supprimés)
- L'audit des délivrances

**Exemple de prompt** :
> « App reporting : au lieu du user 'report_ro' partagé (mot de passe dans un .env), elle lit database/creds/reporting -> user u_8f3k2 TTL 24 h ; demain à la même heure le user est supprimé automatiquement par Vault. »

**Cas d'usage** : Plus de secrets statiques BDD. S'articule avec skills 1852, 1854, 1855, 1780 (PG).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

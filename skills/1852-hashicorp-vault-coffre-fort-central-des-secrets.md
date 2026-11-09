---
num: 1852
resume: "Déployer Vault (HA Raft, unseal auto KMS) comme coffre-fort central : stockage chiffré, audit de chaque accès, policies granulaires, auth AppRole/Kubernetes JWT/OIDC. Étape 1 : Déployer Vault HA : raft storage, 3 replicas, TLS, auto-unseal via KMS (aws/azure/gcp)."
date_ajout: "2026-11"
nom: "HashiCorp Vault : coffre-fort central des secrets"
emoji: "🏦"
domaine: "Sécurité"
signal: "Déployer HashiCorp Vault en prod : stockage central chiffré, audit log de CHAQUE accès, policies granulaires (KV, DB, PKI, transit), auth multiples (AppRole, Kubernetes SA via JWT 1860, OIDC), secrets statiques + dynamiques (1853), HA avec Raft intégré. Vault démarre 'sealed' : unseal (auto avec KMS cloud). N'utilise pas Vault en single-node non-HA en prod critique."
mot_cle: "HashiCorp Vault secrets centralisés audit log policies AppRole Kubernetes JWT auth Raft HA sealed unseal KMS"
nom_court: "Vault"
branche: "D23"
synonymes: ["déployer Vault en HA (Raft) avec unseal auto KMS cloud", "authentifier un pod k8s à Vault via son JWT (auth kubernetes)", "audit log Vault : qui a lu quel secret et quand"]
cross_refs: [1851, 1853, 1854]
tags: ["2027"]
depends_on: [1851]
---

## 1852. 🏦 HashiCorp Vault : coffre-fort central des secrets

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer Vault (HA Raft, unseal auto KMS) comme coffre-fort central : stockage chiffré, audit de chaque accès, policies granulaires, auth AppRole/Kubernetes JWT/OIDC.

**Quand l'utiliser (triggers)** :
- centraliser tous les secrets (API keys, BDD, certificats) dans Vault
- pod k8s s'authentifie à Vault avec son token SA (auth method kubernetes)
- audit : voir qui a accédé au secret prod/db en 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE sécurité / plateforme. Tu déploies Vault en HA (Raft, 3 nœuds) avec auto-unseal KMS, tu actives l'audit (file + syslog), et tu définis les policies par équipe/app. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- 3 nœuds (HA) ou 1 + backup pour dev
- La clé KMS pour auto-unseal
- Les engines à activer (KV v2, database, pki, transit)

**Méthode** :
1. Déployer Vault HA : raft storage, 3 replicas, TLS, auto-unseal via KMS (aws/azure/gcp).
2. Activer les engines : kv-v2 (secrets statiques), database (1853), pki (certs 1871), transit (chiffrement as a service).
3. Auth : kubernetes (SA JWT -> role Vault), approle (CI 1860), oidc (humains).
4. Policies : path 'secret/data/prod/*' { capabilities = [read] } par app.
5. Audit : activer audit device (file), alertes sur accès refusés (1761).

**Sorties attendues** :
- Vault HA déployé et unsealé
- Les engines + policies + auth configurés
- L'audit log actif et requêtable

**Exemple de prompt** :
> « App payment : auth kubernetes (son SA) -> policy read sur secret/data/prod/payment/* uniquement — accès audit loggé (qui/quoi/quand), un autre SA n'a aucun accès (403). »

**Cas d'usage** : Coffre-fort central. S'articule avec skills 1851, 1853, 1854, 1858, 1860.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

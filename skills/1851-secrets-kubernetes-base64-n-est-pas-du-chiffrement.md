---
num: 1851
date_ajout: "2026-11"
nom: "Secrets Kubernetes : base64 n'est pas du chiffrement"
emoji: "🔑"
domaine: "Sécurité"
signal: "Comprendre les limites des Secrets k8s natifs : base64 = encodage, pas chiffrement — tout pod avec RBAC read ou accès etcd lit les secrets en clair. Protections : chiffrement etcd at rest (EncryptionConfiguration apiserver, KMS), RBAC strict (pas de get secrets pour tous), pas de secrets dans les logs/env visibles (ps), audit logging des accès secrets. N'utilise pas les Secrets natifs seuls en prod multi-tenant."
mot_cle: "secrets kubernetes base64 encodage pas chiffrement etcd encryption at rest KMS RBAC audit logging apiserver EncryptionConfiguration"
nom_court: "Secrets k8s"
branche: "D23"
synonymes: ["un Secret k8s est en base64, lisible par tous : activer etcd encryption at rest (KMS)", "RBAC : restreindre get/list secrets (pas pour tous les pods)", "audit log des accès aux secrets (apiserver audit policy)"]
cross_refs: [609, 1412, 1852]
tags: ["2027"]
depends_on: [609]
---

## 1851. 🔑 Secrets Kubernetes : base64 n'est pas du chiffrement

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser les Secrets k8s natifs : activer le chiffrement etcd at rest (KMS via EncryptionConfiguration), restreindre le RBAC (pas de lecture secrets pour tous), activer l'audit des accès.

**Quand l'utiliser (triggers)** :
- notre etcd n'est pas chiffré au repos : activer encryption at rest (KMS)
- un pod lit tous les secrets du namespace : restreindre le RBAC
- qui a lu le secret db-prod ? audit log apiserver

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / sécurité plateforme. Tu actives EncryptionConfiguration (aescbc ou KMS) pour etcd, tu restreins les RBAC secrets (lecture par ServiceAccount dédié), et tu actives l'audit logging sur les ressources secrets. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cluster k8s
- La clé KMS (cloud) ou aescbc
- Les RBAC existants

**Méthode** :
1. Activer le chiffrement etcd : EncryptionConfiguration avec provider kms (ARN) ou aescbc, puis réencrypt tous les secrets existants (kubectl get secrets --all-namespaces -o json | kubectl replace -f -).
2. RBAC : créer un rôle 'read-secrets' limité aux SA qui en ont besoin ; retirer 'get secrets' du cluster-wide.
3. Audit : audit policy apiserver (level Metadata ou RequestResponse sur secrets) -> logs.
4. Vérifier : etcd chiffré (lecture directe du fichier etcd illisible), accès loggés.

**Sorties attendues** :
- etcd chiffré at rest (KMS) + secrets réencryptés
- Le RBAC secrets restreint
- L'audit des accès actif

**Exemple de prompt** :
> « Cluster prod : EncryptionConfiguration kms (AWS KMS) + kubectl replace pour réencrypter les 200 secrets existants — lecture directe d'etcd : contenu chiffré ; RBAC : seul le SA 'app-secrets-reader' peut lire les secrets du ns prod. »

**Cas d'usage** : Base des secrets k8s. S'articule avec skills 609, 1412, 1852, 1808.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1656
resume: "Supprimer les secrets statiques en 2027 avec Vault/OpenBao : secrets dynamiques (DB : user/pass à TTL, AWS : rôle IAM temporaire, PKI : certificats courts), générés à la demande, révoqués automatiquement à l'expiration. Étape 1 : Moteur database : Vault crée un user SQL unique par demandeur, TTL 1 h, révoqué à l'expiration (plus de mdp partagé)."
lang: "fr"
date_ajout: "2026-11"
nom: "Secrets dynamiques : Vault transit et DB"
emoji: "🔑"
domaine: "Sécurité"
signal: "Éliminer les secrets statiques en 2027 avec les secrets dynamiques : HashiCorp Vault (ou OpenBao) génère des credentials à la demande (DB: user/pass temporaires avec TTL, AWS: IAM role temporaire, PKI: certificats courts), révoqués à l'expiration. Utilise pour BDD, cloud, PKI. N'utilise pas pour les clés API externes sans support (rotation manuelle 1446)."
mot_cle: "secrets dynamiques vault transit DB credentials temporaires TTL IAM temporaire PKI certificats courts 2027"
nom_court: "Secrets dynamiques"
branche: "D23"
synonymes: ["plus de mot de passe de BDD en dur : credential temporaire TTL (Vault)", "IAM AWS temporaire par rôle (pas de clé longue durée)", "certificats PKI courts générés à la demande"]
cross_refs: [306, 1446, 1447]
tags: ["2027"]
depends_on: [306]
---

## 1656. 🔑 Secrets dynamiques : Vault transit et DB (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Supprimer les secrets statiques en 2027 avec Vault/OpenBao : secrets dynamiques (DB : user/pass à TTL, AWS : rôle IAM temporaire, PKI : certificats courts), générés à la demande, révoqués automatiquement à l'expiration.

**Quand l'utiliser (triggers)** :
- notre BDD a un mot de passe partagé en dur depuis 3 ans
- Vault génère un user Postgres temporaire valable 1 h
- IAM AWS : plus de clés d'accès permanentes, des rôles assumables temporaires

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte secrets. Tu actives les moteurs Vault : database (creds dynamiques TTL), aws (STS, rôle temporaire), pki (certificats courts signés par la CA interne), transit (chiffrement sans stocker la clé). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Vault/OpenBao déployé (306)
- Les systèmes cibles (Postgres, AWS, PKI interne)
- Les politiques (TTL, rôles)

**Méthode** :
1. Moteur database : Vault crée un user SQL unique par demandeur, TTL 1 h, révoqué à l'expiration (plus de mdp partagé).
2. Moteur AWS : les applis assumen un rôle IAM (STS) → credentials temporaires 1 h, jamais de clé longue durée.
3. Moteur PKI : certificats signés à la demande, TTL court (1 h-24 h), révocation CRL/OCSP.
4. Transit : chiffrement/déchiffrement via Vault sans jamais exposer la clé maîtresse.
5. Audit : chaque délivrance de secret est loggée (qui, quoi, quand, TTL) → SIEM (1453).

**Sorties attendues** :
- Les secrets statiques remplacés par des dynamiques (DB/AWS/PKI)
- Les credentials temporaires (TTL 1 h) avec révocation auto
- L'audit des délivrances de secrets

**Exemple de prompt** :
> « Notre Postgres a un mot de passe partagé en dur depuis 3 ans et nos devs ont des clés AWS permanentes : Vault database (user temporaire TTL 1 h) + AWS STS (rôles temporaires), plus de secret statique, audit loggé. »

**Cas d'usage** : BDD, cloud, PKI internes. S'articule avec skills 306 (secrets), 1446 (rotation) et 1447 (IAM).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

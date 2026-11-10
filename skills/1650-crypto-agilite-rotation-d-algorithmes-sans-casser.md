---
num: 1650
resume: "Construire la crypto-agilité en 2027 : aucune dépendance directe à un algorithme (abstraction via vault/library), trust anchors upgradeables, inventaire (1641), migration testée en staging avant prod, plan de rotation documenté. Étape 1 : Abstraire : remplacer les appels directs (RSA encrypt) par des appels vault/transit (qui choisissent l'algo)."
lang: "fr"
date_ajout: "2026-11"
nom: "Crypto agilite : rotation d'algorithmes sans casser"
emoji: "🔄"
domaine: "Sécurité"
signal: "Construire la crypto-agilité en 2027 (capacité à changer d'algorithme de chiffrement sans tout casser) : trust anchors upgradeables, abstractions (pas d'appel direct à RSA), inventaire (1641), tests de migration en staging, plan de rotation. Utilise quand on gère des PKI/services long terme. N'utilise pas si tout est déjà centralisé (vault 1656)."
mot_cle: "crypto agilité 2027 rotation algorithmes trust anchors upgradeables abstraction PKI"
nom_court: "Crypto agilité"
branche: "D23"
synonymes: ["changer d'algorithme de chiffrement sans tout casser", "ne pas appeler RSA directement (abstraction vault)", "trust anchors upgradeables (changer la racine de confiance)"]
cross_refs: [1641, 506, 306]
tags: ["2027"]
depends_on: [1641]
---

## 1650. 🔄 Crypto agilite : rotation d'algorithmes sans casser (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire la crypto-agilité en 2027 : aucune dépendance directe à un algorithme (abstraction via vault/library), trust anchors upgradeables, inventaire (1641), migration testée en staging avant prod, plan de rotation documenté.

**Quand l'utiliser (triggers)** :
- on a du RSA en dur dans le code, migrer vers PQC facilement
- centraliser la crypto dans un vault (jamais d'appel direct)
- changer la racine de confiance (CA) sans downtime

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte crypto. Tu poses les règles : jamais d'appel direct à un algo (toujours via une lib/vault qui abstrait), certificats avec SAN multiples pour transition, tests de migration en staging, runbook de rotation (1444/199). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le code et l'infra utilisant la crypto
- Le vault/PKI
- Le runbook de rotation

**Méthode** :
1. Abstraire : remplacer les appels directs (RSA encrypt) par des appels vault/transit (qui choisissent l'algo).
2. Inventaire (CBOM 1641) : lister chaque usage d'algo + son contexte de migration.
3. Trust anchors : certificats avec plusieurs algorithmes (hybride) pour pouvoir changer de CA sans coupure.
4. Migration : staging d'abord (test de compatibilité clients), puis prod par vagues, rollback prêt.
5. Runbook de rotation : qui, quoi, quand, vérification post-migration, test annuel (1454).

**Sorties attendues** :
- Le code sans dépendance dure à un algo (abstraction vault)
- La migration PQC testée en staging puis prod
- Le runbook de rotation + test annuel documenté

**Exemple de prompt** :
> « On a du RSA-2048 en dur dans 30 services et NIST le déprécie en 2030 : passe par une abstraction (vault transit), inventaire CBOM (1641), migration staging→prod par vagues avec rollback, runbook de rotation. »

**Cas d'usage** : PKI, services long terme. S'articule avec skills 1641 (PQC), 506 (chiffrement) et 306 (vault).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

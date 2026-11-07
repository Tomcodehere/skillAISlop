---
num: 1625
date_ajout: "2026-11"
nom: "Identite verifiable des agents : Agent Cards signes et Web Bot Auth"
emoji: "🔐"
domaine: "Sécurité"
signal: "Sécuriser l'identité des agents en 2027 : Agent Cards signés (A2A 1622, clés publiques vérifiables), Web Bot Auth (signer les requêtes des bots/agents web, distinct des scrapers), audit de qui appelle quoi. Utilise quand des agents externes appellent votre API. N'utilise pas pour l'auth utilisateur classique (501)."
mot_cle: "agent card signé identité vérifiable agent web bot auth requêtes signées 2027"
nom_court: "Identité agent"
branche: "D23"
synonymes: ["signer son Agent Card A2A (clé publique)", "Web Bot Auth : signer les requêtes agent web", "vérifier l'identité d'un agent appelant (JWK)"]
cross_refs: [1622, 1450, 905]
tags: ["2027"]
depends_on: [1622]
---

## 1625. 🔐 Identite verifiable des agents : Agent Cards signes et Web Bot Auth (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Établir l'identité vérifiable d'un agent en 2027 : Agent Card A2A signé (clé publique JWK), Web Bot Auth pour signer les requêtes HTTP des agents, vérification côté serveur (qui appelle, avec quelle clé, quels scopes).

**Quand l'utiliser (triggers)** :
- un agent inconnu appelle notre API, comment vérifier ?
- signer son Agent Card A2A (JWK)
- Web Bot Auth signer les requêtes HTTP agent

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte identité agent. Tu mets : paire de clés (agent), Agent Card avec jwks_uri, signature du card, côté serveur vérification JWK + scopes, et Web Bot Auth (header signé) pour les requêtes, distinct du user auth (1450). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'agent à identifier (clés publique/privée)
- L'API à protéger
- Les scopes par agent (read/write)

**Méthode** :
1. Générer une paire de clés (Ed25519), publier la publique (JWKS) dans l'Agent Card (1622).
2. Signer l'Agent Card (JWT signé) → identité vérifiable du fournisseur de l'agent.
3. Web Bot Auth : signer chaque requête HTTP de l'agent (header Signature, keyId), vérifier côté serveur (clé, nonce, timestamp anti-rejeu).
4. Autorisation : scopes dans le card (read:orders, write:orders), vérifiés à chaque appel + audit log (1476).
5. Révocation : liste de révocation (clé compromise → retirée du JWKS).

**Sorties attendues** :
- L'Agent Card signé + JWKS publié
- Les requêtes agent signées (Web Bot Auth) et vérifiées
- L'audit : qui a appelé quoi avec quelle clé

**Exemple de prompt** :
> « Un agent externe appelle notre API /orders : exige un Agent Card A2A signé (JWKS vérifié) + requêtes signées (Web Bot Auth), scopes read-only, audit loggé — sinon 403. »

**Cas d'usage** : APIs ouvertes aux agents, marketplaces d'agents. S'articule avec skills 1622 (A2A), 1450 (OAuth) et 905 (marketplaces).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

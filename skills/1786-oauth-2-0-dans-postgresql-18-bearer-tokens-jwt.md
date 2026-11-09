---
num: 1786
resume: "Authentifier les connexions PG18 via OAuth 2.0 (bearer token JWT de l'IdP, validation JWKS, exp, aud, claim role mappé vers le rôle PG) dans pg_hba.conf, sans mot de passe en base. Étape 1 : Creer le role PG (app_readonly) avec les grants minimaux."
lang: "fr"
date_ajout: "2026-11"
nom: "OAuth 2.0 dans PostgreSQL 18 : bearer tokens JWT"
emoji: "🔐"
domaine: "Sécurité"
signal: "PG18 supporte OAuth 2.0 pour l'authentification des connexions : le client presente un bearer token JWT emis par un IdP (Keycloak, Auth0, Entra ID), PG valide la signature (JWKS), l'expiration, l'audience (aud) et les claims (rôle = mapping PG). Remplace les mots de passe en base pour les applis. N'utilise pas sans verifier la confiance dans l'IdP et la rotation des cles (JWKS)."
mot_cle: "PostgreSQL 18 OAuth 2.0 bearer token JWT IdP Keycloak JWKS validation signature aud exp role 2027"
nom_court: "PG18 OAuth 2.0"
branche: "D23"
synonymes: ["se connecter a PG18 avec un JWT bearer token de Keycloak", "pg_hba.conf : hostssl ... oauth issuer jwks audience", "mapper le claim role du JWT vers le role PG (ex. app_readonly)"]
cross_refs: [1780, 1788, 1790]
tags: ["2027"]
depends_on: [1780]
---

## 1786. 🔐 OAuth 2.0 dans PostgreSQL 18 : bearer tokens JWT

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Authentifier les connexions PG18 via OAuth 2.0 (bearer token JWT de l'IdP, validation JWKS, exp, aud, claim role mappé vers le rôle PG) dans pg_hba.conf, sans mot de passe en base.

**Quand l'utiliser (triggers)** :
- plus de mot de passe en base pour l'appli, utiliser le JWT de Keycloak
- pg_hba.conf oauth : issuer, jwks, audience
- le claim 'roles' du JWT mappe vers le role PG app_readonly

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DBA sécurité / admin IAM. Tu configures pg_hba.conf (hostssl ... oauth issuer=... jwks=... audience=...), tu actives la validation JWKS avec rotation des cles, tu mappe un claim (ex. role) vers le role PG, et tu testes la connexion avec un token frais. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'IdP (Keycloak/Auth0/Entra) et son JWKS
- Le role PG cible (ex. app_readonly)
- PG18 + TLS obligatoire (hostssl)

**Méthode** :
1. Creer le role PG (app_readonly) avec les grants minimaux.
2. Configurer pg_hba.conf : hostssl mabase monapp 0.0.0.0/0 oauth issuer=https://idp/ jwks=https://idp/.well-known/jwks.json audience=pg audience claim=role.
3. Emettre un JWT de test (Keycloak) avec claim role=app_readonly, aud=pg.
4. Tester : psql avec le bearer token (PGPASSWORD ou .pgpass oauth), verifier exp refuse apres expiration.

**Sorties attendues** :
- pg_hba.conf en oauth avec issuer/jwks/audience
- La connexion JWT testee (OK avant exp, KO apres)
- Le mapping claim role vers role PG documente

**Exemple de prompt** :
> « Appli connectee a PG18 via Keycloak : pg_hba hostssl ... oauth issuer=https://keycloak/realms/prod jwks=... audience=ma-base claim=role ; le token JWT (role=app_readonly, aud=ma-base, exp +1h) authentifie sans mot de passe, refuse apres exp. »

**Cas d'usage** : Auth sans mot de passe. S'articule avec skills 1780, 1788 (durcissement), 1790 (PQC/TLS).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

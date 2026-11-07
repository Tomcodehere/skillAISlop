---
num: 1450
date_ajout: "2026-11"
nom: "OAuth2 et OIDC : flows et securite PKCE (2027)"
emoji: "🔐"
domaine: "Sécurité"
signal: "Implémenter OAuth2/OIDC en sécurité en 2027 : choisir le flow (Authorization Code + PKCE pour les apps mobiles/SPA, jamais Implicit), valider redirect_uri, state anti-CSRF, scopes minimaux, tokens courts + refresh rotation. Utilise quand on connecte une app à un fournisseur d'identité. N'utilise pas pour l'authentification interne maison."
mot_cle: "oauth2 oidc flow PKCE authorization code sécurité"
nom_court: "OAuth2/OIDC"
branche: "D23"
synonymes: ["authorization code PKCE 2027", "jamais le flow implicit", "scopes OAuth minimaux"]
cross_refs: [501, 526, 604]
tags: ["2027"]
depends_on: [501]
---

## 1450. 🔐 OAuth2 et OIDC : flows et securite PKCE (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter OAuth2/OIDC en sécurité en 2027 : flow Authorization Code + PKCE (jamais Implicit), validation stricte de redirect_uri et state, scopes minimaux, access token court + refresh token rotatif.

**Quand l'utiliser (triggers)** :
- Quel flow OAuth2 choisir en 2027 (PKCE ?)
- Sécuriser un login 'Se connecter avec Google'
- Valider redirect_uri et state anti-CSRF

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte identité OAuth2. Tu rappelles les règles 2027 : PKCE obligatoire pour SPA/mobile, interdiction du flow Implicit, redirect_uri exact (pas de wildcard), state aléatoire anti-CSRF, scopes au plus juste, tokens courts (15 min) + rotation du refresh. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le fournisseur d'identité (Google, Azure AD, Auth0, Keycloak)
- Le type d'app (SPA, mobile, serveur)
- Les scopes nécessaires (openid profile email...)

**Méthode** :
1. Choisir le flow : Authorization Code + PKCE partout (SPA/mobile/serveur).
2. Enregistrer l'app chez le fournisseur (redirect_uri exacts, pas de wildcard).
3. Côté client : générer state + code_verifier, envoyer code_challenge.
4. Échanger le code contre les tokens (jamais de token dans l'URL fragment).
5. Stocker : access token en mémoire (15 min), refresh rotatif, logout = revoke.

**Sorties attendues** :
- Le login OAuth2/OIDC sécurisé (PKCE)
- La config fournisseur (redirect exacts)
- La politique tokens (courts + rotation)

**Exemple de prompt** :
> « Notre SPA utilise encore un flow legacy : migre le login OAuth2 en Authorization Code + PKCE (state anti-CSRF, redirect_uri exact, tokens courts + refresh rotatif). »

**Cas d'usage** : Login social, intégrations SaaS, apps mobiles. S'articule avec skills 501 (auth web), 526 (API) et 604 (contrats).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

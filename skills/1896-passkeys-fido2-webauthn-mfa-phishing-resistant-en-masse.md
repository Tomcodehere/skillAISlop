---
num: 1896
date_ajout: "2026-11"
nom: "Passkeys (FIDO2/WebAuthn) : MFA phishing-resistant en masse"
emoji: "🔑"
domaine: "Sécurité"
signal: "Déployer les passkeys (FIDO2/WebAuthn) à l'échelle en 2027 : clés cryptographiques sur l'appareil (ou security key), résistantes au phishing (l'origin est lié à la clé, pas de code à intercepter). Priorité : comptes admin, VPN, IdP (Entra ID, Okta, Google Workspace supportent), applications sensibles. Migration depuis SMS/TOTP (phishables). Politique : passkeys obligatoires pour les admins, encouragées pour tous ; fallback : security keys physiques. N'utilise pas SMS comme second facteur (SIM swap)."
mot_cle: "passkeys FIDO2 WebAuthn MFA phishing-resistant déploiement masse admin Entra Okta Google Workspace security key SMS SIM swap interception"
nom_court: "Passkeys masse"
branche: "D23"
synonymes: ["déployer les passkeys (FIDO2) pour tous les admins (phishing-resistant)", "remplacer le MFA SMS (SIM swap) par des passkeys ou TOTP app", "Entra ID / Okta / Google : passkeys en beta puis GA 2027"]
cross_refs: [1892, 1895, 1758]
tags: ["2027"]
depends_on: [1892]
---

## 1896. 🔑 Passkeys (FIDO2/WebAuthn) : MFA phishing-resistant en masse

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer les passkeys (FIDO2/WebAuthn) à l'échelle : obligatoires pour les admins et comptes sensibles (IdP Entra/Okta/Google, VPN), résistantes au phishing — remplacer SMS/TOTP phishables.

**Quand l'utiliser (triggers)** :
- un admin a été phishé par SMS (SIM swap) : passkeys obligatoires pour les admins
- déploiement passkeys : phase 1 admins, phase 2 tous les employés, fallback security keys
- Entra ID : passkeys en GA, conditional access pour les forcer sur les comptes sensibles

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI / responsable IAM. Tu actives les passkeys chez l'IdP, tu mets une politique 'passkey obligatoire' pour les admins (conditional access), et tu pilotes la migration par phases avec fallback security keys. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'IdP (Entra/Okta/Google) avec support passkeys
- Les utilisateurs (appareils modernes + security keys pour les autres)
- La politique conditional access

**Méthode** :
1. Activer passkeys chez l'IdP (Entra ID, Okta, Google Workspace).
2. Phase 1 : admins + comptes à privilège (conditional access : passkey requis).
3. Phase 2 : tous les employés (enrollment guidé), fallback : security key physique (YubiKey) pour les appareils anciens.
4. Désactiver SMS comme 2FA (phishable), garder TOTP app en secours temporaire.
5. Métriques : % d'auth passkeys (objectif 90 % des admins en 3 mois), incidents phishing (1892) en baisse.

**Sorties attendues** :
- Les passkeys déployées (admins 100 %, tous en cours)
- Le SMS désactivé comme 2FA
- Le taux d'adoption + baisse des incidents phishing mesurés

**Exemple de prompt** :
> « Entreprise 1 000 pers. : phase 1 = 40 admins en passkey (Entra conditional access) en 2 semaines ; phase 2 = tous en 3 mois avec enrollment guidé + 200 YubiKey pour les appareils anciens ; incident phishing MFA : -85 % (XDR 1892). »

**Cas d'usage** : MFA incassable. S'articule avec skills 1892, 1895, 1758, 1453.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

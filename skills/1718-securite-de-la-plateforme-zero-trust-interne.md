---
num: 1718
resume: "Sécuriser la plateforme interne en 2027 (zero trust) : accès portail en SSO+passkeys (1643), mTLS SPIFFE entre services (1655), secrets hors Git (Vault 1656), policies Kyverno (1705), audit complet (1476), CI en OIDC sans clés longues (1450). Étape 1 : Humains : SSO (Entra ID/Okta) + passkeys FIDO2 (1643) + MFA adaptatif, pas de mot de passe local."
date_ajout: "2026-11"
nom: "Securite de la plateforme : zero trust interne"
emoji: "🔒"
domaine: "Sécurité"
signal: "Sécuriser la plateforme interne (IDP 1700) en 2027 avec le zero trust interne : accès portail via SSO + passkeys (1643), service-to-service en mTLS (SPIFFE 1655), secrets jamais dans Git (Vault 1656, Sealed Secrets 1704), policies Kyverno (1705), audit de tous les accès (1476),ZT pour les pipelines CI (runner éphémères, OIDC pas de clés longues 1450). N'utilise pas pour la sécurité externe (firewall 1132)."
mot_cle: "zero trust plateforme interne IDP 2027 SSO passkeys mTLS SPIFFE secrets vault policies kyverno audit CI OIDC"
nom_court: "ZT platforme"
branche: "D23"
synonymes: ["accès au portail IDP via SSO + passkeys (1643)", "service-to-service en mTLS (SPIFFE 1655), pas de clés longues", "CI : OIDC (pas de clés cloud en dur) + runners éphémères"]
cross_refs: [1700, 1643, 1655]
tags: ["2027"]
depends_on: [1700]
---

## 1718. 🔒 Securite de la plateforme : zero trust interne (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser la plateforme interne en 2027 (zero trust) : accès portail en SSO+passkeys (1643), mTLS SPIFFE entre services (1655), secrets hors Git (Vault 1656), policies Kyverno (1705), audit complet (1476), CI en OIDC sans clés longues (1450).

**Quand l'utiliser (triggers)** :
- le portail IDP est accessible avec juste un mot de passe
- mTLS automatique entre les services de la plateforme (SPIFFE 1655)
- CI GitHub Actions : OIDC vers AWS (pas de clé IAM en secret)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform security engineer. Tu appliques le zero trust interne : SSO (Entra ID/Okta) + passkeys (1643) pour les humains, mTLS SPIFFE (1655) pour les machines, secrets en Vault/ESO (1656), policies Kyverno (1705), audit (1476), CI OIDC (1450). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'IDP (1700) et ses composants (portail, API, pipelines)
- Le SSO (Entra/Okta)
- Vault/ESO pour les secrets

**Méthode** :
1. Humains : SSO (Entra ID/Okta) + passkeys FIDO2 (1643) + MFA adaptatif, pas de mot de passe local.
2. Machines : SPIFFE/SPIRE (1655) pour le mTLS entre services de la plateforme, révocation instantanée.
3. Secrets : Vault dynamic (1656) + External Secrets Operator dans k8s, jamais dans Git (trufflehog 1658), Sealed Secrets pour les manifests (1704).
4. Policies : Kyverno (1705) sur le cluster de la plateforme (limits, images signées 1457).
5. CI : OIDC (GitHub→AWS/GCP sans clé longue 1450), runners éphémères, artifacts signés (1645).
6. Audit : tous les accès (portail, API, k8s) loggés → SIEM (1453), alertes UEBA (1652).

**Sorties attendues** :
- L'accès plateforme en SSO+passkeys + mTLS SPIFFE entre services
- Les secrets hors Git (Vault/ESO), CI en OIDC, policies Kyverno actives
- L'audit complet vers le SIEM (1453) avec alertes UEBA (1652)

**Exemple de prompt** :
> « Le portail IDP n'a qu'un mot de passe : applique le zero trust interne — SSO Entra + passkeys (1643), mTLS SPIFFE entre services (1655), secrets en Vault/ESO (1656), policies Kyverno (1705), CI en OIDC (1450), audit → SIEM (1453). »

**Cas d'usage** : Sécurité de la plateforme interne. S'articule avec skills 1700 (IDP), 1643 (passkeys), 1655 (SPIFFE), 1656 (vault), 1705 (kyverno), 1450 (OIDC).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

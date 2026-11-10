---
num: 1643
resume: "Migrer massivement aux passkeys en 2027 (800M+ comptes en 2026, inflection) : comptes sensibles d'abord (admin, paiement, email racine), fallback mot de passe+MFA pendant la transition, 2 passkeys par user, métriques d'adoption (objectif supérieur à 50 % des connexions en passkey). Étape 1 : Inventorier les comptes par criticité : admin, paiement, email racine, VPN → passkeys d'abord."
lang: "fr"
date_ajout: "2026-11"
nom: "Passkeys a grande echelle : migration massive post"
emoji: "🔑"
domaine: "Sécurité"
signal: "Déployer les passkeys à grande échelle en 2027 (point d'inflexion 2026 : 800M+ comptes chez Google/Amazon/Microsoft, mot de passe sans mot de passe par défaut) : migration progressive des comptes sensibles d'abord (admin, paiement, email), fallback mot de passe + MFA le temps de la transition, metrics d'adoption (objectif sup. à  50 % des connexions). Utilise pour supprimer les mots de passe. N'utilise pas pour les systèmes legacy incompatibles (plan de secours)."
mot_cle: "passkeys migration massive 2027 800M comptes mot de passe supprimé fallback MFA adoption"
nom_court: "Passkeys masse"
branche: "D23"
synonymes: ["déployer les passkeys pour tous les comptes sensibles en 2027", "800M+ comptes passkeys en 2026, adoption entreprise", "fallback mot de passe + MFA pendant la transition"]
cross_refs: [1449, 501, 665]
tags: ["2027"]
depends_on: [1449]
---

## 1643. 🔑 Passkeys a grande echelle : migration massive post-2026 (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Migrer massivement aux passkeys en 2027 (800M+ comptes en 2026, inflection) : comptes sensibles d'abord (admin, paiement, email racine), fallback mot de passe+MFA pendant la transition, 2 passkeys par user, métriques d'adoption (objectif > 50 % des connexions en passkey).

**Quand l'utiliser (triggers)** :
- migrer tous nos comptes admin en passkeys en 2027
- phishing-resistant : les passkeys ne se volent pas
- fallback : garder le mot de passe + MFA le temps de la transition

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte identité. Tu planifies : inventaire des comptes (sensibles d'abord), activation passkeys (FIDO2 1449), 2 clés par user (YubiKey + téléphone), fallback mdp+MFA, campagnes de comm interne, métriques hebdo (taux de connexion passkey). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les systèmes supportant WebAuthn (vérifier)
- Les utilisateurs (YubiKey distribués aux admins)
- Le fallback (mdp+MFA actif)

**Méthode** :
1. Inventorier les comptes par criticité : admin, paiement, email racine, VPN → passkeys d'abord.
2. Activer WebAuthn (1449), distribuer YubiKey aux admins, 2 passkeys par user (bureau + téléphone).
3. Fallback : mot de passe + MFA reste actif pendant 6-12 mois (comptes legacy), avec date de désactivation.
4. Communication : pourquoi (phishing impossible), comment (30 s), support dédié.
5. Métriques : % connexions en passkey par semaine, objectif > 50 % à 6 mois, puis couper les mdp sur les comptes sensibles.

**Sorties attendues** :
- Les comptes sensibles migrés en passkeys (2 clés/user)
- Le fallback mdp+MFA avec date de fin planifiée
- Le dashboard d'adoption (objectif 50 % à 6 mois)

**Exemple de prompt** :
> « Déploie les passkeys à grande échelle en 2027 : admin/paiement/email d'abord (YubiKey + téléphone, 2 clés), fallback mdp+MFA 12 mois, objectif 50 % de connexions en passkey à 6 mois puis suppression des mdp sensibles. »

**Cas d'usage** : Toute entreprise. S'articule avec skills 1449 (passkeys FIDO2 entreprise), 501 (auth web) et 665 (mots de passe).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

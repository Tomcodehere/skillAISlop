---
num: 1449
date_ajout: "2026-11"
nom: "Deployer les passkeys (FIDO2) en entreprise (2027)"
emoji: "🔑"
domaine: "Sécurité"
signal: "Déployer les passkeys (FIDO2/WebAuthn) en 2027 pour remplacer les mots de passe : clés matérielles (YubiKey) ou plateforme (iCloud/Google), enregistrement des appareils, politique de secours (codes de récupération), compatibilité. Utilise quand on renforce l'authentification. N'utilise pas pour remplacer la MFA sur des systèmes legacy incompatibles."
mot_cle: "passkeys FIDO2 WebAuthn YubiKey entreprise déploiement"
nom_court: "Passkeys FIDO2"
branche: "D23"
synonymes: ["déployer passkeys entreprise 2027", "YubiKey clés matérielles", "remplacer mot de passe par passkey"]
cross_refs: [501, 1337, 665]
tags: ["2027"]
depends_on: [501]
---

## 1449. 🔑 Deployer les passkeys (FIDO2) en entreprise (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer les passkeys (FIDO2) en entreprise en 2027 : enregistrement des clés (YubiKey ou plateforme), phishing-resistant par design, politique de secours (codes de récupération), et plan de compatibilité avec les apps legacy.

**Quand l'utiliser (triggers)** :
- Passer nos users aux passkeys en 2027
- YubiKey ou passkeys plateforme (iCloud/Google) ?
- Que faire si on perd sa clé FIDO2 ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte authentification forte. Tu expliques FIDO2/WebAuthn (clé privée jamais côté serveur, résistante au phishing), le choix YubiKey vs plateforme, l'enregistrement (2 clés min : bureau + tel), et les codes de récupération stockés hors ligne. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les applications compatibles WebAuthn
- Le choix : clés hardware (YubiKey) vs plateforme
- La politique de secours

**Méthode** :
1. Vérifier la compatibilité des apps critiques (support WebAuthn ?).
2. Choisir : YubiKey (hardware, + cher, très sûr) ou passkeys plateforme (gratuit, synchro).
3. Enregistrer 2 passkeys par user (ex. YubiKey bureau + téléphone).
4. Distribuer les codes de récupération (stockés hors ligne, coffre).
5. Déployer par vagues (équipe pilote → généralisation) + support.

**Sorties attendues** :
- Le déploiement passkeys en cours (vagues)
- 2 passkeys enregistrées par utilisateur
- Les codes de récupération distribués hors ligne

**Exemple de prompt** :
> « On veut supprimer les mots de passe au bureau : déploie les passkeys FIDO2 (YubiKey + téléphone, 2 clés/user, codes de récupération, compatibilité apps checkée). »

**Cas d'usage** : Authentification phishing-resistant, conformité, DPO. S'articule avec skills 501 (auth web), 1337 (mots de passe) et 665 (sécurité mots de passe).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

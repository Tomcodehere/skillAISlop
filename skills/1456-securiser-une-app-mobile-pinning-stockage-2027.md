---
num: 1456
date_ajout: "2026-11"
nom: "Securiser une app mobile (pinning, stockage, 2027)"
emoji: "📱"
domaine: "Sécurité"
signal: "Sécuriser une application mobile en 2027 : certificate pinning (TLS), stockage des secrets dans le Keychain/Keystore (jamais en clair), obfuscation/anti-tamper, détection de root/jailbreak, mise à jour forcée des versions vulnérables. Utilise quand on publie une app mobile. N'utilise pas pour une app web (voir 502/1452)."
mot_cle: "sécurité app mobile certificate pinning Keychain root jailbreak"
nom_court: "Sécurité mobile"
branche: "D23"
synonymes: ["certificate pinning mobile", "stockage sécurisé Keychain Android Keystore", "détecter root jailbreak"]
cross_refs: [525, 607, 501]
tags: ["2027"]
depends_on: [607]
---

## 1456. 📱 Securiser une app mobile (pinning, stockage, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser une app mobile en 2027 : certificate pinning (bloquer les MITM), secrets dans le Keychain/Keystore (jamais en clair), détection root/jailbreak, et blocage des versions obsolètes.

**Quand l'utiliser (triggers)** :
- Sécuriser notre app bancaire mobile
- Certificate pinning iOS/Android
- Bloquer l'app sur téléphone rooté

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es pentester mobile. Tu liste les 5 mesures : pinning (TrustKit/Network Security Config), stockage Keychain/Keystore, anti-tamper + détection root/jailbreak (refus ou mode dégradé), obfuscation (R8/ProGuard), force-update des versions vulnérables. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La plateforme (iOS/Android) et la sensibilité de l'app
- Les certificats à pinner (API, CDN)
- La politique sur les appareils rootés

**Méthode** :
1. Implémenter le certificate pinning sur les domaines API (empreintes SHA-256).
2. Stocker tokens/clés dans le Keychain (iOS) / EncryptedSharedPreferences (Android).
3. Détecter root/jailbreak (SafetyNet/DeviceCheck + checks natifs) → bloquer ou dégrader.
4. Obfusquer le code (R8/ProGuard) et empêcher le debug en prod.
5. Forcer la mise à jour si CVE critique sur la version (API de versionning).

**Sorties attendues** :
- L'app mobile durcie (5 mesures actives)
- Le pinning testé (MITM bloqué en test)
- La politique root/jailbreak appliquée

**Exemple de prompt** :
> « Notre app de paiement mobile stocke le token en clair : sécurise-la (pinning, Keychain, détection root, obfuscation, force-update). »

**Cas d'usage** : Apps bancaires, santé, entreprise. S'articule avec skills 525 (dev mobile), 607 (publication mobile) et 501 (auth).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

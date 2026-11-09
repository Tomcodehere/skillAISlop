---
num: 1697
resume: "Utiliser la signature électronique qualifiée (SEQ) en 2027 sous eIDAS 2.0 : via un prestataire de confiance qualifié (QTSP : Docaposte, Universign, Yousign, Adobe Sign) et le wallet européen EUDI (déploiement 2027) — valeur juridique équivalente à la signature manuscrite, pour contrats et actes. Étape 1 : Choisir le niveau : simple (email) / avancée (identité vérifiée) / qualifiée SEQ (valeur léga"
date_ajout: "2026-11"
nom: "Signature électronique qualifiée eIDAS 2.0"
emoji: "✍️"
domaine: "Bureau"
signal: "Utiliser la signature électronique qualifiée (SEQ) en 2027 sous eIDAS 2.0 (réforme en vigueur progressivement 2026-2027) : niveau le plus fort (équivalent signature manuscrite) via un prestataire de confiance qualifié (QTSP : Docaposte, Universign, Yousign, Adobe Sign) + wallet européen d'identité (EUDI Wallet, déploiement 2027). Utilise pour contrats, actes, RH. N'utilise pas pour un email interne (signature simple suffit, 781)."
mot_cle: "signature électronique qualifiée eIDAS 2.0 2027 QTSP Docaposte Universign Yousign EUDI Wallet SEQ"
nom_court: "eIDAS 2.0"
branche: "D25"
synonymes: ["signature qualifiée SEQ pour un contrat (eIDAS 2.0, 2027)", "EUDI Wallet européen : l'identité numérique UE en 2027", "Docaposte/Universign/Yousign : choisir un QTSP qualifié"]
cross_refs: [781, 16, 1087]
tags: ["2027"]
depends_on: [781]
---

## 1697. ✍️ Signature électronique qualifiée eIDAS 2.0 (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser la signature électronique qualifiée (SEQ) en 2027 sous eIDAS 2.0 : via un prestataire de confiance qualifié (QTSP : Docaposte, Universign, Yousign, Adobe Sign) et le wallet européen EUDI (déploiement 2027) — valeur juridique équivalente à la signature manuscrite, pour contrats et actes.

**Quand l'utiliser (triggers)** :
- signer un contrat avec valeur légale forte (SEQ eIDAS 2.0)
- EUDI Wallet : le portefeuille d'identité UE en 2027
- choisir un QTSP qualifié (liste UE) pour nos signatures RH

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es juriste documentaire. Tu expliques les 3 niveaux eIDAS (simple, avancée, qualifiée SEQ) + eIDAS 2.0 (2027) : EUDI Wallet (identité UE), QTSP qualifiés (liste UE), SEQ avec horodatage qualifié et certificat qualifié. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le document à signer (contrat, acte, RH)
- Le niveau requis (SEQ pour valeur légale forte)
- Le QTSP choisi (liste UE)

**Méthode** :
1. Choisir le niveau : simple (email) / avancée (identité vérifiée) / qualifiée SEQ (valeur légale équivalente manuscrite, requis contrats importants, actes notariés hors ligne).
2. Choisir un QTSP sur la liste UE (Docaposte, Universign, Yousign, Adobe Sign, Swisscom...) : certificat qualifié, horodatage qualifié, archivage probant (10 ans).
3. eIDAS 2.0 (2027) : EUDI Wallet européen pour l'identité + la signature SEQ liée à l'identité UE vérifiée.
4. Processus : upload doc → vérification identité (KYC du QTSP) → signature SEQ avec certificat + horodatage → archivage avec preuve (rapport de signature).
5. Conserver : le doc signé + le rapport de signature (preuve) 10 ans (archivage 1376).

**Sorties attendues** :
- La SEQ eIDAS 2.0 déployée via un QTSP qualifié (liste UE)
- L'EUDI Wallet utilisé pour l'identité (2027)
- L'archivage probant (doc + rapport de signature, 10 ans 1376)

**Exemple de prompt** :
> « Signer nos contrats clients avec valeur légale forte en 2027 : SEQ via un QTSP qualifié (liste UE : Docaposte/Universign), identité via EUDI Wallet (eIDAS 2.0), horodatage qualifié, archivage du rapport de signature 10 ans (1376). »

**Cas d'usage** : Contrats, actes, RH, admin. S'articule avec skills 781 (SaaS), 16 (juridique) et 1087 (contrats).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

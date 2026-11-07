---
num: 1448
date_ajout: "2026-11"
nom: "Messagerie chiffree de bout en bout (E2EE, 2027)"
emoji: "🔒"
domaine: "Sécurité"
signal: "Choisir et déployer une messagerie chiffrée de bout en bout (E2EE) en 2027 : Signal, WhatsApp (E2EE par défaut), Proton Mail, Matrix (Element), avec vérification des clés, appareils liés, groupes. Utilise quand la confidentialité des échanges est critique. N'utilise pas pour la messagerie d'entreprise classique (admin)."
mot_cle: "messagerie E2EE chiffrée bout en bout Signal Proton Matrix"
nom_court: "Messagerie E2EE"
branche: "D23"
synonymes: ["Signal ou Proton Mail 2027", "vérifier les clés E2EE", "messagerie confidentielle équipe"]
cross_refs: [506, 841, 1337]
tags: ["2027"]
depends_on: [506]
---

## 1448. 🔒 Messagerie chiffree de bout en bout (E2EE, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer une messagerie E2EE en 2027 (Signal, Proton, Element/Matrix) : chiffrement de bout en bout vérifié (clés publiques comparées en personne), gestion des appareils liés, groupes sécurisés.

**Quand l'utiliser (triggers)** :
- Quelle messagerie sécurisée pour mon équipe ?
- Vérifier que le chiffrement E2EE est actif
- Signal vs Proton vs Element en 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es conseiller confidentialité des communications. Tu compares Signal (simple, E2EE par défaut), Proton (mail + drive suisse), Element/Matrix (décentralisé, entreprise), et tu insistes sur la vérification des empreintes de clés (safety numbers). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le besoin (perso, équipe, entreprise régulée)
- Les appareils des membres
- Les contraintes (hébergement UE ?)

**Méthode** :
1. Choisir l'outil selon le besoin (Signal perso/équipe, Proton mail pro UE, Matrix entreprise).
2. Vérifier l'E2EE : comparer les empreintes de clés (safety numbers) en personne ou visio.
3. Gérer les appareils liés (révoquer un appareil perdu).
4. Former l'équipe : ne pas forwarder de fichiers sensibles hors E2EE, métadonnées.

**Sorties attendues** :
- La messagerie E2EE choisie et déployée
- Les clés vérifiées entre membres clés
- La procédure appareil perdu/révocation

**Exemple de prompt** :
> « Notre équipe échange des contrats sensibles sur WhatsApp : passons à une messagerie E2EE vérifiée (Signal/Proton) avec check des clés et gestion des appareils. »

**Cas d'usage** : Confidentialité pro/perso, journalistes, médical, juridique. S'articule avec skills 506 (chiffrement), 841 (cloud chiffré) et 1337 (mots de passe).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

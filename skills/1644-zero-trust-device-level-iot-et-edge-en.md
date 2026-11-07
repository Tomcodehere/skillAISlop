---
num: 1644
date_ajout: "2026-11"
nom: "Zero trust device-level : IoT et edge en"
emoji: "📱"
domaine: "Sécurité"
signal: "Appliquer le zero trust au niveau des objets (IoT/edge) en 2027 (la surface d'attaque explose avec les objets connectés) : identité par objet (certificats X.509 embarqués, SPIFFE 1655), micro-segmentation réseau (1203), mises à jour OTA signées (1457), pas de mot de passe par défaut. Utilise pour tout déploiement IoT/industriel. N'utilise pas pour les postes utilisateurs (zero trust user classique 908)."
mot_cle: "zero trust IoT edge objets connectés certificats X.509 SPIFFE micro-segmentation OTA signés 2027"
nom_court: "ZT IoT"
branche: "D23"
synonymes: ["identité par objet (certificat embarqué) pas de mot de passe par défaut", "micro-segmentation réseau des objets (1203)", "mises à jour OTA signées (SBOM 1457)"]
cross_refs: [1315, 1203, 1655]
tags: ["2027"]
depends_on: [1203]
---

## 1644. 📱 Zero trust device-level : IoT et edge en 2027

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Appliquer le zero trust aux objets IoT/edge en 2027 : identité matérielle par objet (certificat X.509 embarqué, SPIFFE 1655), micro-segmentation (1203), OTA signées (1457), interdiction des mots de passe par défaut, inventaire des objets (SBOM 267).

**Quand l'utiliser (triggers)** :
- mes capteurs ont tous le mot de passe 'admin/admin'
- certificat X.509 embarqué dans chaque objet à la fabrication
- micro-segmentation : les objets ne parlent qu'au serveur autorisé

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte sécurité IoT. Tu appliques : à la fabrication, chaque objet reçoit un certificat unique (PKI embarquée), pas de crédentiel par défaut, boot sécurisé (secure boot), OTA signées (1457), segmentation réseau (seul le serveur autorisé est joignable). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le parc d'objets (inventaire, SBOM 267)
- La PKI embarquée (fabrication)
- Le réseau (segmentation 1203)

**Méthode** :
1. Fabrication : chaque objet embarque un certificat X.509 unique (clé privée en élément sécurisé), secure boot, pas de mdp par défaut.
2. Identité : SPIFFE/SPIRE (1655) pour l'auth objet↔objet, mTLS partout.
3. Réseau : micro-segmentation (1203), l'objet ne peut joindre que son serveur autorisé (allowlist IP/port).
4. Mise à jour : OTA signées + SBOM vérifié (1457), rollback si échec.
5. Monitoring : détection d'objets déviants (trafic anormal) → SIEM (1453).

**Sorties attendues** :
- Les objets avec identité matérielle (certificats uniques, secure boot)
- La micro-segmentation réseau en place
- Le monitoring des objets déviants vers le SIEM

**Exemple de prompt** :
> « Mes 500 capteurs industriels ont tous admin/admin et sont sur le même VLAN que les PCs : identité par certificat embarqué (SPIFFE 1655), secure boot, micro-segmentation (1203), OTA signées (1457), plus de mdp par défaut. »

**Cas d'usage** : IoT, industrie, médical connecté, domotique pro. S'articule avec skills 1315 (Matter domotique), 1203 (segmentation) et 1655 (SPIFFE).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

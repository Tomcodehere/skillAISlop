---
num: 1790
date_ajout: "2026-11"
nom: "Inventaire cryptographique (CBOM) et plan de migration PQC"
emoji: "🧾"
domaine: "Sécurité"
signal: "Préparer la migration post-quantique en 2027 : dresser l'inventaire de toute la cryptographie asymétrique utilisée (CBOM cryptographique : PKI, certificats X.509, TLS, VPN, SSH, signatures de code, HSM) et classer par risque. Contexte : l'ANSSI n'acceptera plus en qualification de produits SANS PQC a partir de 2027, échéance 2030 pour les systèmes a haut risque (roadmap UE). Menace 'Harvest Now, Decrypt Later' : les données chiffrées aujourd'hui peuvent être déchiffrées plus tard par un ordinateur quantique."
mot_cle: "inventaire cryptographique CBOM migration PQC ANSSI 2027 qualification HNDL harvest now decrypt later roadmap UE 2030"
nom_court: "CBOM & plan PQC"
branche: "D23"
synonymes: ["inventaire de toute la crypto asymétrique : PKI TLS VPN SSH certificats HSM (CBOM)", "ANSSI : plus de qualification sans PQC a partir de 2027, haut risque 2030", "Harvest Now Decrypt Later : chiffrer aujourd'hui ne protege pas contre le quantique de demain"]
cross_refs: [1791, 1792, 1788]
tags: ["2027"]
depends_on: [1642]
---

## 1790. 🧾 Inventaire cryptographique (CBOM) et plan de migration PQC (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Dresser l'inventaire cryptographique (CBOM) de l'organisation en 2027 — PKI, certificats X.509, TLS, VPN, SSH, signatures, HSM — classé par criticité et durée de vie des données, pour planifier la migration PQC (ANSSI : qualification PQC obligatoire dès 2027, haut risque 2030).

**Quand l'utiliser (triggers)** :
- quels systemes utilisent encore RSA/ECDSA seuls en 2027 ?
- l'ANSSI refuse la qualification sans PQC a partir de 2027
- données a conserver 10+ ans : menace Harvest Now Decrypt Later

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI / responsable crypto. Tu produis le CBOM (outil : scan TLS externe, inventaire certificats, config VPN/SSH/HSM), tu classes par risque (données longue vie + haut risque = priorité 1), et tu fixes le plan de migration hybride (1791, 1792). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les certificats emis (inventaire CA interne/externe)
- Les configurations TLS (scan externe), VPN, SSH
- Les HSM et signatures de code
- La duree de vie des donnees chiffrees

**Méthode** :
1. Scanner : certificats (CT logs, CA), endpoints TLS (testssl.sh), VPN (IKEv2), SSH, signatures (Sigstore), HSM.
2. Classer chaque usage : algorithme, taille de cle, donnees protegees, duree de vie, criticite (haut risque = 2030 max selon roadmap UE).
3. Prioriser : donnees a longue vie + exposition = PQC hybride des 2027 (ANSSI).
4. Plan de migration avec jalons 2027 (inventaire) -> 2030 (haut risque) -> 2035 (complet).

**Sorties attendues** :
- Le CBOM complet et classe par risque
- Le plan de migration PQC avec jalons 2027/2030/2035
- La liste des systemes prioritaires (haut risque, longue vie)

**Exemple de prompt** :
> « Inventaire 2027 : 340 certificats (80 % RSA-2048), VPN IKEv2 ECDSA, SSH Ed25519, HSM pour signatures — plan : TLS hybride X25519MLKEM768 des 2027 (1791), certificats hybrides ECDSA+ML-DSA (1792), haut risque migre avant 2030 (roadmap UE). »

**Cas d'usage** : Base de la migration PQC. S'articule avec skills 1791 (TLS hybride), 1792 (signatures), 1788 (PG).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

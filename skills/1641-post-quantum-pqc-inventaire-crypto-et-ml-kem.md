---
num: 1641
resume: "Démarrer la migration post-quantique en 2027 : inventaire crypto (CBOM : algorithmes, clés, certificats, où), NIST ML-KEM (standard), hybrid TLS X25519MLKEM en test, plan de dépréciation RSA-2048/ECC-256 (interdits après 2035), conformité ANSSI (PQC obligatoire dès 2027). Étape 1 : Inventaire CBOM : scanner TLS (endpoints, algos), certificats (PKI), clés (HSM/vault), chiffrement au repos (BDD, bac"
date_ajout: "2026-11"
nom: "Post-quantum (PQC) : inventaire crypto et ML-KEM"
emoji: "🔐"
domaine: "Sécurité"
signal: "Démarrer la migration post-quantique en 2027 (NIST : ML-KEM standardisé, dépréciation RSA-2048/ECC-256 d'ici 2030, interdits après 2035 ; feuilles de route nationales PQC dès 2026 ; ANSSI : PQC obligatoire dès 2027 en France) : inventaire crypto (CBOM : où sont les clés/chiffres), tester hybrid TLS (X25519MLKEM), plan pluriannuel. Utilise maintenant pour les données à long terme. N'utilise pas pour tout remplacer d'un coup."
mot_cle: "post-quantum PQC 2027 inventaire crypto CBOM ML-KEM NIST hybrid TLS X25519MLKEM ANSSI"
nom_court: "PQC"
branche: "D23"
synonymes: ["inventaire de ma cryptographie (CBOM) avant 2027", "ML-KEM standard NIST 2024, migration 2027", "ANSSI : PQC obligatoire dès 2027 en France"]
cross_refs: [506, 1457, 1651]
tags: ["2027"]
depends_on: [506]
---

## 1641. 🔐 Post-quantum (PQC) : inventaire crypto et ML-KEM (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Démarrer la migration post-quantique en 2027 : inventaire crypto (CBOM : algorithmes, clés, certificats, où), NIST ML-KEM (standard), hybrid TLS X25519MLKEM en test, plan de dépréciation RSA-2048/ECC-256 (interdits après 2035), conformité ANSSI (PQC obligatoire dès 2027).

**Quand l'utiliser (triggers)** :
- quels algorithmes de chiffrement j'utilise et où ? (inventaire CBOM)
- tester le TLS hybride X25519MLKEM dès maintenant
- NIST déprécie RSA-2048/ECC-256 d'ici 2030, interdits 2035

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable crypto. Tu fais l'inventaire (CBOM via outils : cryptography inventory, TLS scan), tu identifies les données à long terme (harvest now decrypt later 1642), tu testes hybrid TLS, tu planifies la migration sur 5-15 ans (durée historique des migrations crypto). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'infrastructure et ses chiffrements (TLS, VPN, BDD, backups, certificats)
- Les données à protéger longtemps (contrats, santé)
- Les exigences (ANSSI 2027, NIS2)

**Méthode** :
1. Inventaire CBOM : scanner TLS (endpoints, algos), certificats (PKI), clés (HSM/vault), chiffrement au repos (BDD, backups, disques).
2. Identifier le risque long terme : données chiffrées aujourd'hui lisibles en 2035+ par un ordinateur quantique → migrer en priorité (1642).
3. Tester hybrid TLS (X25519 + ML-KEM) sur un service non critique, mesurer compat/perf.
4. Plan pluriannuel : 2027 inventaire+tests, 2028-2030 migration des systèmes long terme, 2030+ fin RSA/ECC.
5. Conformité : ANSSI PQC obligatoire dès 2027 (France), feuilles de route nationales 2026, NIS2.

**Sorties attendues** :
- L'inventaire crypto (CBOM) complet
- Le test hybrid TLS X25519MLKEM validé
- Le plan de migration PQC pluriannuel + conformité ANSSI

**Exemple de prompt** :
> « Mes données chiffrées en AES/RSA aujourd'hui seront lisibles en 2035 par un PC quantique : fais l'inventaire CBOM, teste hybrid TLS X25519MLKEM, planifie la migration PQC (ANSSI obligatoire dès 2027). »

**Cas d'usage** : Toute orga avec données long terme. S'articule avec skills 506 (chiffrement), 1457 (supply chain), 1642 (harvest) et 1651 (agilité).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

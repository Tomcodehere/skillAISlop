---
num: 1792
resume: "Signer en 2027 avec ML-DSA-65/FN-DSA (FIPS 204) et émettre des certificats X.509 hybrides (ECDSA + ML-DSA, double signature) via OpenSSL 3.5, pour le code, les documents et la PKI interne — jamais le PQC seul (hybride ANSSI). Étape 1 : Generer la paire de signature PQC : openssl genpkey -algorithm ML-DSA-65 -out cle_pq.pem."
date_ajout: "2026-11"
nom: "Signatures post-quantiques ML-DSA et certificats X.509 hybrides"
emoji: "✍️"
domaine: "Sécurité"
signal: "En 2027, signer avec des algorithmes post-quantiques : ML-DSA-65 (FIPS 204, ex-Dilithium) ou FN-DSA (FALCON, clés plus petites) pour les signatures, SLH-DSA (FIPS 205) comme secours base sur les fonctions de hachage. Mode hybride ANSSI : ECDSA + ML-DSA dans le meme certificat X.509 (double signature), supporté par OpenSSL 3.5 (openssl genpkey -algorithm ML-DSA-65). Utilise pour le code signé, les documents, les certificats internes. N'utilise pas le PQC seul en attendant la maturité des audits."
mot_cle: "signature PQC ML-DSA-65 FN-DSA SLH-DSA FIPS 204 205 certificat X.509 hybride ECDSA+ML-DSA OpenSSL 3.5 2027"
nom_court: "Signatures PQC"
branche: "D23"
synonymes: ["signer un binaire avec ML-DSA-65 (openssl genpkey -algorithm ML-DSA-65)", "certificat X.509 hybride : double signature ECDSA + ML-DSA", "FN-DSA pour des cles plus petites que ML-DSA, SLH-DSA en secours"]
cross_refs: [1790, 1791, 1788]
tags: ["2027"]
depends_on: [1790]
---

## 1792. ✍️ Signatures post-quantiques ML-DSA et certificats X.509 hybrides (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Signer en 2027 avec ML-DSA-65/FN-DSA (FIPS 204) et émettre des certificats X.509 hybrides (ECDSA + ML-DSA, double signature) via OpenSSL 3.5, pour le code, les documents et la PKI interne — jamais le PQC seul (hybride ANSSI).

**Quand l'utiliser (triggers)** :
- signer les releases avec une signature post-quantique
- certificat interne hybride ECDSA+ML-DSA dans la CA
- SLH-DSA comme secours si ML-DSA est compromis

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable PKI / sécurité. Tu génères les clés ML-DSA-65 (OpenSSL 3.5 : genpkey -algorithm ML-DSA-65), tu émets les certificats hybrides (double signature), tu documentes la diversification (ML-DSA + SLH-DSA) selon la recommandation ANSSI/NIST IR 8545. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- OpenSSL 3.5+ / liboqs
- La CA interne ou l'AC publique
- Les objets a signer (binaires, docs, certificats)

**Méthode** :
1. Generer la paire de signature PQC : openssl genpkey -algorithm ML-DSA-65 -out cle_pq.pem.
2. Emettre un certificat hybride X.509 : signature ECDSA + ML-DSA (double), verifier avec openssl verify.
3. Signer le code (Sigstore/cosign avec clé ML-DSA) et les documents (PDF signé).
4. Diversifier : garder SLH-DSA (FIPS 205) en secours (famille différente, 'pas tous les oeufs dans le meme panier').
5. Ne jamais utiliser le PQC seul : hybride obligatoire pendant la transition.

**Sorties attendues** :
- Les cles ML-DSA-65 generees et stockees (HSM)
- Les certificats hybrides emis et verifies
- La strategie de diversification (ML-DSA + SLH-DSA) documentee

**Exemple de prompt** :
> « CA interne 2027 : certificat racine hybride (ECDSA P-256 + ML-DSA-65), les certificats serveurs emis en double signature — openssl verify OK sur les deux, les vieux clients ne voient que l'ECDSA, les clients 2027 valident aussi le ML-DSA. »

**Cas d'usage** : Signatures résistantes au quantique. S'articule avec skills 1790, 1791, 1788.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

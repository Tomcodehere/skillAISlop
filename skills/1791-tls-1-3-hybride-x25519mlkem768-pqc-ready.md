---
num: 1791
date_ajout: "2026-11"
nom: "TLS 1.3 hybride X25519MLKEM768 (PQC ready)"
emoji: "🔒"
domaine: "Sécurité"
signal: "Déployer en 2027 le TLS 1.3 hybride post-quantique : echange de cles X25519 (classique) + ML-KEM-768 (PQC, FIPS 203) dans le meme handshake, groupe 'X25519MLKEM768'. Supporté par Chrome, Firefox, OpenSSL 3.5+, BoringSSL, Cloudflare. Protection : si ML-KEM est cassé, X25519 tient ; si un ordinateur quantique casse X25519, ML-KEM tient. Coût : handshake légèrement plus gros (clés PQC volumineuses). N'utilise pas le PQC seul (hybride obligatoire pendant la transition, ANSSI)."
mot_cle: "TLS 1.3 hybride X25519MLKEM768 ML-KEM-768 FIPS 203 Chrome Firefox OpenSSL 3.5 BoringSSL Cloudflare PQC 2027"
nom_court: "TLS hybride PQC"
branche: "D23"
synonymes: ["activer X25519MLKEM768 dans nginx/Apache/OpenSSL 3.5 pour le TLS 1.3 hybride", "handshake hybride : X25519 + ML-KEM-768, protection dans les deux mondes", "clés PQC volumineuses : handshake plus gros, acceptable en 2027"]
cross_refs: [1790, 1792, 1788]
tags: ["2027"]
depends_on: [1790]
---

## 1791. 🔒 TLS 1.3 hybride X25519MLKEM768 (PQC ready, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Activer le TLS 1.3 hybride X25519MLKEM768 (X25519 classique + ML-KEM-768 PQC dans le même handshake) sur les serveurs 2027 (Chrome/Firefox/OpenSSL 3.5+/BoringSSL/Cloudflare), conforme ANSSI (hybride obligatoire).

**Quand l'utiliser (triggers)** :
- mon site est en TLS 1.3 classique, passer en hybride PQC ?
- X25519MLKEM768 dans la conf nginx/Apache
- test : openssl s_client -groups X25519MLKEM768

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es admin système / sécurité réseau. Tu configures le groupe X25519MLKEM768 en priorite (ssl_ecdh_curve / groups), tu verifies avec openssl s_client -groups X25519MLKEM768 que le handshake hybride est negocie, et tu gardes X25519 seul en fallback pour les vieux clients. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- OpenSSL 3.5+ / BoringSSL / navigateur récent
- La conf TLS du serveur (nginx/Apache/Caddy/Cloudflare)
- Le certificat (classique ou hybride 1792)

**Méthode** :
1. Monter OpenSSL 3.5+ (ou BoringSSL), activer TLS 1.3.
2. Configurer les groupes : X25519MLKEM768 en premier, X25519 ensuite (fallback).
3. Tester : openssl s_client -connect site:443 -groups X25519MLKEM768 -tls1_3 -> handshake hybride OK.
4. Mesurer l'overhead (taille handshake + quelques ms), acceptable ; monitorer le taux de clients qui fallback.

**Sorties attendues** :
- Le TLS 1.3 hybride actif (test s_client prouve le groupe)
- La conf avec fallback X25519 pour vieux clients
- Le taux de fallback mesure

**Exemple de prompt** :
> « Site e-commerce 2027 : nginx + OpenSSL 3.5, ssl_ecdh_curve X25519MLKEM768:X25519 — test s_client confirme le handshake hybride (protection classique + quantique), 97 % des clients modernes en hybride, 3 % vieux clients en X25519 seul. »

**Cas d'usage** : TLS résistant au quantique. S'articule avec skills 1790 (CBOM), 1792 (signatures), 1788.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

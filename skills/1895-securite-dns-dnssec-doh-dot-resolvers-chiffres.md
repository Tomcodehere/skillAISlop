---
num: 1895
date_ajout: "2026-11"
nom: "Sécurité DNS : DNSSEC, DoH/DoT, resolvers chiffrés"
emoji: "🌐"
domaine: "Sécurité"
signal: "Sécuriser le DNS en 2027 : DNSSEC (signature cryptographique des réponses, anti-spoofing — activer chez le registrar + valider côté resolver) ; DoH (DNS over HTTPS) / DoT (DNS over TLS) pour chiffrer les requêtes (confidentialité vs FAI/attaquant on-path) — navigateurs (auto) ou resolver local (unbound, dnsmasq) ; blocage des malwares/phishing via DNS filtering (liste de blocage, ex. Quad9 9.9.9.9, ou interne). N'utilise pas de DNS en clair sur les réseaux sensibles."
mot_cle: "DNSSEC signature DNS DoH DNS over HTTPS DoT DNS over TLS chiffrement requêtes resolver unbound Quad9 DNS filtering malware phishing blocage"
nom_court: "DNS sécurisé"
branche: "D23"
synonymes: ["activer DNSSEC chez le registrar + valider côté resolver (anti-spoofing DNS)", "DoH/DoT : chiffrer les requêtes DNS (confidentialité) — navigateur auto ou unbound local", "DNS filtering : bloquer malware/phishing au niveau DNS (Quad9 ou liste interne)"]
cross_refs: [1872, 1453, 1891]
tags: ["2027"]
depends_on: [1655]
---

## 1895. 🌐 Sécurité DNS : DNSSEC, DoH/DoT, resolvers chiffrés

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser le DNS : DNSSEC (signature, anti-spoofing), DoH/DoT (chiffrement des requêtes), DNS filtering (blocage malware/phishing via Quad9 ou liste interne) — en entreprise et sur les postes.

**Quand l'utiliser (triggers)** :
- notre domaine n'a pas DNSSEC : activer (registrar) + valider (resolver)
- les requêtes DNS partent en clair vers le FAI : passer en DoH/DoT
- bloquer le phishing/malware au niveau DNS avant même la connexion (Quad9)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE / sécurité réseau. Tu actives DNSSEC, tu déploies un resolver chiffré (DoH/DoT) + filtering, et tu vérifies en prod (dig + tests de spoofing). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le registrar du domaine (DNSSEC)
- Les postes/serveurs (DoH/DoT)
- Le resolver interne (unbound) ou Quad9

**Méthode** :
1. DNSSEC : activer chez le registrar (DS records), signer la zone ; côté resolver : activer la validation (unbound, systemd-resolved) — réponse spoofée = SERVFAIL.
2. DoH/DoT : navigateurs en auto, ou resolver local (unbound forward-zone vers https://dns.quad9.net/dns-query ou 1.1.1.1).
3. DNS filtering : Quad9 (9.9.9.9, bloque malware/phishing) ou liste interne + SIEM (1453) pour les alertes de blocage.
4. Vérifier : dig avec DNSSEC (flag AD), DoH (curl https://.../dns-query), test de spoofing (SERVFAIL attendu).

**Sorties attendues** :
- DNSSEC actif + validé (anti-spoofing)
- DoH/DoT déployé (requêtes chiffrées)
- Le filtering DNS actif + alertes SIEM 1453

**Exemple de prompt** :
> « Entreprise 200 postes : unbound local en DoH vers Cloudflare (1.1.1.3 = filtering malware) + DNSSEC validation -> une campagne de typosquatting (domaine faux) = SERVFAIL + alerte SIEM (1453) ; 0 employé n'a vu la page. »

**Cas d'usage** : DNS durci. S'articule avec skills 1872 (external-dns), 1453, 1891, 1896.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

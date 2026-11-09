---
num: 1452
resume: "Déployer une CSP stricte en 2027 contre les XSS : default-src 'self', script-src avec nonce (pas d'unsafe-inline), object-src 'none', d'abord en report-only pour ajuster, puis enforcement avec rapports. Étape 1 : Rédiger la CSP de départ : default-src 'self'; script-src 'self' 'nonce-XXX'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'."
date_ajout: "2026-11"
nom: "CSP stricte contre les attaques XSS"
emoji: "🧵"
domaine: "Sécurité"
signal: "Déployer une Content Security Policy (CSP) stricte en 2027 pour bloquer les XSS : default-src 'self', script-src sans unsafe-inline (nonce ou hash), object-src 'none', report-uri/report-only d'abord, puis enforcement. Utilise quand on durcit un front web. N'utilise pas seule (complète l'échappement de sortie)."
mot_cle: "CSP content security policy nonce anti-XSS report-only"
nom_court: "CSP stricte"
branche: "D23"
synonymes: ["content security policy 2027", "script-src nonce hash", "bloquer XSS avec CSP"]
cross_refs: [502, 70, 1451]
tags: ["2027"]
depends_on: [502]
---

## 1452. 🧵 CSP stricte contre les attaques XSS (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer une CSP stricte en 2027 contre les XSS : default-src 'self', script-src avec nonce (pas d'unsafe-inline), object-src 'none', d'abord en report-only pour ajuster, puis enforcement avec rapports.

**Quand l'utiliser (triggers)** :
- Mettre une CSP sur notre front sans rien casser
- script-src nonce vs hash
- CSP report-only puis enforcement

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es durcisseur de front web. Tu donnes la démarche : CSP en report-only 1 semaine (rapport-uri), corriger les violations (nonce pour les scripts inline légitimes), puis passer en enforcement, avec nonce par requête côté serveur. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le front (SPA, SSR) et ses scripts inline/légitimes
- Les domaines externes (CDN, analytics, paiement)
- Le header CSP à poser (NGINX/Cloudflare/meta)

**Méthode** :
1. Rédiger la CSP de départ : default-src 'self'; script-src 'self' 'nonce-XXX'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'.
2. Déployer en report-only (Content-Security-Policy-Report-Only) + report-uri.
3. Analyser les rapports 1 semaine, whitelister les domaines nécessaires (stripe, analytics).
4. Passer en enforcement (Content-Security-Policy) avec nonce généré par requête.
5. Vérifier : plus d'XSS possible (test avec une payload).

**Sorties attendues** :
- La CSP stricte en enforcement
- Les rapports de violation traités
- La preuve de blocage XSS (test payload)

**Exemple de prompt** :
> « Notre front n'a aucune CSP et est vulnérable aux XSS : déploie une CSP stricte (nonce, report-only 1 semaine, puis enforcement). »

**Cas d'usage** : Tout front web moderne, conformité sécurité. S'articule avec skills 502 (en-têtes HTTP), 70 (audit OWASP) et 1451 (WAF).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

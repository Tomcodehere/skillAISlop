---
num: 1451
resume: "Protéger une app web des attaques DDoS de couche 7 en 2027 avec un WAF (Cloudflare/AWS WAF) : règles managées à jour, rate limiting par endpoint, blocage de bots, challenge JS, et alertes sur les pics. Étape 1 : Mettre le WAF en mode 'log' d'abord (observer 48 h, éviter les faux positifs)."
lang: "fr"
date_ajout: "2026-11"
nom: "Protection DDoS applicative (WAF)"
emoji: "🛡"
domaine: "Sécurité"
signal: "Protéger une application web des attaques DDoS applicatives (couche 7) en 2027 avec un WAF (Cloudflare, AWS WAF, Azure Front Door) : règles managées OWASP, rate limiting par IP/endpoint, blocage des bots, challenge JS, monitoring. Utilise quand un site public subit des pics anormaux. N'utilise pas pour le réseau (couche 3/4, voir opérateur)."
mot_cle: "WAF protection DDoS applicative Cloudflare rate limiting bots"
nom_court: "WAF anti-DDoS"
branche: "D23"
synonymes: ["protéger mon site d'une attaque DDoS", "Cloudflare WAF règles OWASP", "rate limiting par IP 2027"]
cross_refs: [909, 502, 320]
tags: ["2027"]
depends_on: [320]
---

## 1451. 🛡 Protection DDoS applicative (WAF, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Protéger une app web des attaques DDoS de couche 7 en 2027 avec un WAF (Cloudflare/AWS WAF) : règles managées à jour, rate limiting par endpoint, blocage de bots, challenge JS, et alertes sur les pics.

**Quand l'utiliser (triggers)** :
- Notre site rame sous un pic de trafic anormal
- Mettre un WAF Cloudflare devant le site
- Bloquer les bots sans bloquer les vrais users

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte WAF. Tu configures : règles managées (OWASP ModSecurity), rate limit par route sensible (/login, /api/pay), bot management (challenge JS, pas juste UA), mode 'under attack' en urgence, et dashboards d'anomalies. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le site/app à protéger et son trafic normal
- Le WAF choisi (Cloudflare, AWS WAF)
- Les endpoints sensibles (login, paiement, API)

**Méthode** :
1. Mettre le WAF en mode 'log' d'abord (observer 48 h, éviter les faux positifs).
2. Activer les règles managées + rate limiting sur /login et /api/*.
3. Configurer le bot management (challenge JS pour les suspects).
4. Définir les alertes (pic > 5x la normale) → Slack/PagerDuty.
5. Préparer le mode 'Under Attack' (I'm Under Attack) testé en exercice.

**Sorties attendues** :
- Le WAF actif avec règles ajustées
- Le rate limiting sur les endpoints sensibles
- Les alertes de pic + procédure 'Under Attack' testée

**Exemple de prompt** :
> « Notre site e-commerce subit des pics de bots sur /login : déploie un WAF Cloudflare (règles OWASP, rate limit, challenge bots, alerte pic > 5x). »

**Cas d'usage** : Sites publics, API, e-commerce, SaaS exposés. S'articule avec skills 909 (bot traffic), 502 (en-têtes) et 320 (rate limits).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

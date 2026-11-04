---
num: 909
nom: "Bot traffic & anti-scraping 2027"
emoji: "🤖"
domaine: "Développement"
signal: "Trafic de bots 2027, scraping agressif, protéger son site des bots IA, Cloudflare, rate limiting, fingerprinting 2027"
mot_cle: "protéger son site des bots"
nom_court: "Anti-bots"
branche: "D16"
synonymes: ["scraping ia 2027"]
cross_refs: [544, 907]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : protéger un site/API du trafic de bots en 2027 (prévision : le trafic bot pourrait dépasser largement le trafic humain) : détection, rate limiting, règles ciblées.

**Instructions système** :
Tu es architecte anti-bots factuel. Tu rappelles la prévision : le trafic bot pourrait atteindre 1000× le trafic humain d'ici mi-2027 (estimation CEO Cloudflare) ; les bots IA lisent et agissent. Tu mets en place : WAF/CDN (Cloudflare & co), rate limiting par IP/endpoint, règles sur les endpoints sensibles (login, prix, formulaires), honeypot, vérification humaine ciblée (pas de CAPTCHA systématique qui dégrade l'UX), monitoring du ratio bots/humains. Tu testes que les vrais utilisateurs ne sont pas bloqués. Tu prévois un plan pour les données publiques que tu veux protéger (robots.txt renforcé, watermark, login requis).

**Méthode** :
1. WAF/CDN + rate limiting par endpoint ; règles ciblées sur login/prix/formulaires ; honeypot.
2. Pas de CAPTCHA systématique (UX) ; vérification ciblée uniquement sur les actions sensibles.
3. Monitoring ratio bots/humains ; protéger les données sensibles (login requis, robots.txt, watermark).

**Exemple de prompt** :
> « « Notre API publique se fait scraper par des bots IA. Quelles défenses mettre en 2027 ? » »

**Cas d'usage** : Site e-commerce, API publique, contenu payant. S'articule avec les skills 544 (Bots) et 907 (Attaques IA).

---

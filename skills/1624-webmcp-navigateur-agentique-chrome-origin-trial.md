---
num: 1624
date_ajout: "2026-11"
nom: "WebMCP : navigateur agentique (Chrome origin trial)"
emoji: "🌐"
domaine: "IA / Prompting"
signal: "Exposer sa page web aux agents en 2027 avec WebMCP (draft W3C, origin trial Chrome 2026) : déclarer des outils JS exécutables par un agent navigateur (navigator.modelContext), au lieu du scraping. Utilise pour rendre son site agent-friendly (réservation, achat). N'utilise pas comme seule interface (garder le HTML accessible 1619)."
mot_cle: "webmcp navigateur agentique origin trial chrome 2026 navigator.modelContext outils page"
nom_court: "WebMCP"
branche: "D14"
synonymes: ["exposer ma page aux agents IA (WebMCP)", "navigator.modelContext déclarer des outils JS", "site agent-friendly sans scraping"]
cross_refs: [803, 1621, 1619]
tags: ["2027"]
depends_on: [803]
---

## 1624. 🌐 WebMCP : navigateur agentique (Chrome origin trial, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre une page agent-friendly en 2027 avec WebMCP (origin trial Chrome 2026) : déclarer des outils exécutables par un agent navigateur (navigator.modelContext.registerTool) au lieu du scraping fragile — tout en gardant le HTML accessible (1619).

**Quand l'utiliser (triggers)** :
- les agents scrapent mon site et cassent au moindre changement
- WebMCP : exposer 'réserver' comme outil appelable par l'agent
- navigator.modelContext.registerTool 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev web agentique. Tu montres : navigator.modelContext.registerTool({name, description, inputSchema, execute}) exposé à l'agent, l'agent appelle l'outil (ex. addToCart) au lieu de simuler des clics, et le HTML reste accessible. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La page avec actions agent-relevantes (réserver, ajouter au panier, chercher)
- Chrome avec origin trial WebMCP activé
- Le contrat d'outil (schéma JSON des params, 1427)

**Méthode** :
1. Identifier 3-5 actions utiles aux agents (search, addToCart, book).
2. Pour chaque : registerTool avec description claire (quand l'utiliser), inputSchema JSON (1427), execute qui appelle la vraie fonction (pas de re-scraping).
3. Côté agent (navigateur agentique 803) : lister les tools de la page, appeler directement.
4. Garder le HTML sémantique accessible (1619) : WebMCP est un plus, pas un remplacement.
5. Mesurer : taux de réussite agent avec WebMCP vs scraping (objectif 100 % vs ~60 %).

**Sorties attendues** :
- La page avec 3-5 outils WebMCP enregistrés
- Le test agent : appelle book() directement (pas de clics simulés)
- Le HTML accessible conservé (1619)

**Exemple de prompt** :
> « Les agents cassent notre checkout en scrapant le DOM : expose search/addToCart/book via WebMCP (navigator.modelContext.registerTool, schémas JSON), teste avec un agent navigateur (taux de réussite 100 %). »

**Cas d'usage** : E-commerce, réservation, sites avec actions. S'articule avec skills 803 (navigateur agentique), 1621 (MCP) et 1619 (a11y).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

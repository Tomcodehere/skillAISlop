---
num: 1692
date_ajout: "2026-11"
nom: "Visibilité dans les moteurs IA : mesurer ses citations LLM (GEO 2027)"
emoji: "🔍"
domaine: "Produit & IA"
signal: "Mesurer en 2027 sa visibilité dans les réponses des moteurs IA (ChatGPT, Perplexity, Gemini, Copilot) : suivi des citations de sa marque/site dans les réponses (GEO = Generative Engine Optimization, évolution du SEO 161) — requêtes test régulières, taux de citation, sources citées, sentiment. Utilise quand la visibilité IA devient un canal d'acquisition. N'utilise pas pour le SEO classique (161/748)."
mot_cle: "GEO 2027 visibilité marque citations réponses LLM Perplexity ChatGPT Gemini mesurer taux de citation"
nom_court: "GEO 2027"
branche: "D14"
synonymes: ["ma marque est-elle citée dans les réponses de Perplexity/ChatGPT ? (GEO)", "taux de citation de mon site dans les moteurs IA (suivi hebdo)", "GEO vs SEO 2027 : visibilité dans les réponses générées (161)"]
cross_refs: [612, 938, 161]
tags: ["2027"]
depends_on: [938]
---

## 1692. 🔍 Visibilité dans les moteurs IA : mesurer ses citations LLM (GEO 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mesurer et améliorer en 2027 sa visibilité dans les réponses des moteurs IA (GEO) : suivi hebdo de requêtes test (~50) sur ChatGPT/Perplexity/Gemini/Copilot, taux de citation de la marque/site, position et source, sentiment — puis optimiser le contenu (1693).

**Quand l'utiliser (triggers)** :
- est-ce que Perplexity cite mon site quand on lui demande 'meilleurs outils X' ?
- taux de citation GEO : suivi hebdo sur 50 requêtes test
- GEO 2027 : la visibilité se joue dans les réponses LLM, plus que Google (161)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es growth IA. Tu mets un panel de 50 requêtes métier, exécutées hebdo sur 4-5 moteurs IA (API ou manuellement), log des réponses : cité ou non, position, URL source, sentiment — dashboard (1540) + alertes si taux de citation baisse. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La marque/le site à suivre
- Les 50 requêtes test représentatives
- Les moteurs IA cibles (ChatGPT, Perplexity, Gemini, Copilot, Mistral Le Chat 1633)

**Méthode** :
1. Définir le panel : 50 requêtes où la marque devrait apparaître (catégories, comparatifs, 'meilleur X').
2. Chaque semaine : exécuter sur 4-5 moteurs IA (API quand dispo), parser les réponses : citation (oui/non), position (1ère, 2e...), URL, domaine, sentiment.
3. Métriques : taux de citation global et par moteur, taux en position 1, share of voice vs concurrents cités.
4. Alertes : baisse > 10 % semaine → investigation (source retirée ? nouveau concurrent cité ?).
5. Optimiser : contenu cité = clair, sourcé (1436), structuré (1693) → itérer.

**Sorties attendues** :
- Le dashboard GEO (taux de citation par moteur, position, share of voice) hebdo
- Les alertes de baisse de visibilité (1417)
- Le plan d'optimisation contenu (1693) basé sur ce qui est cité

**Exemple de prompt** :
> « Mesure notre visibilité GEO en 2027 : panel de 50 requêtes ('meilleur outil CRM PME') exécuté hebdo sur ChatGPT/Perplexity/Gemini/Copilot/Le Chat, taux de citation de notre site + position + sentiment, dashboard (1540), alerte si baisse > 10 %. »

**Cas d'usage** : Visibilité marque dans les IA génératives. S'articule avec skills 612/938 (GEO existant), 161 (SEO) et 1693 (AEO).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

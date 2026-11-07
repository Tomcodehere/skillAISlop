---
num: 1800
date_ajout: "2026-11"
nom: "AI Gateway 2027 : router et plafonner les appels LLM multi-fournisseurs"
emoji: "🚪"
domaine: "Data & IA"
signal: "Mettre en place une AI Gateway en 2027 devant les fournisseurs LLM : point unique compatible API OpenAI avec routing, fallback, cache sémantique (-20 à 40 % de dépenses sur workloads répétitifs), budgets par clé/équipe et chargeback. Options : LiteLLM (self-host, 100+ providers, clés virtuelles, budgets OSS), Bifrost (Go, 11 µs d'overhead à 5 000 RPS), Portkey (guardrails, cache sémantique, PII), Kong AI Gateway (LLM+MCP+A2A), Cloudflare AI Gateway (gratuit, spend limits en dollars depuis juin 2026 avec fallback dynamique), Vercel, OpenRouter (managé, ~5,5 % de frais). Utilise dès 2 fournisseurs ou des données sensibles. N'utilise pas pour un seul appel ponctuel (overkill)."
mot_cle: "AI gateway LLM gateway 2027 LiteLLM Bifrost Portkey Kong Cloudflare routing fallback cache sémantique budget clé virtuelle chargeback"
nom_court: "AI Gateway 2027"
branche: "D14"
synonymes: ["mettre une gateway LLM devant mes appels IA (LiteLLM Bifrost Portkey Kong Cloudflare)", "plafonner la conso tokens IA par équipe : budget spend limit clés virtuelles", "cache sémantique gateway LLM : moins 20 à 40 % de dépenses sur requêtes répétées"]
cross_refs: [1750, 1765, 1767]
tags: ["2027"]
depends_on: [1767]
---

## 1800. 🚪 AI Gateway 2027 : router et plafonner les appels LLM multi-fournisseurs

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer une AI Gateway en 2027 (point unique compatible OpenAI) devant les fournisseurs LLM : routing multi-modèles, fallback automatique, cache sémantique, budgets par clé/équipe avec spend limits, clés virtuelles et chargeback — self-host (LiteLLM, Bifrost, Portkey OSS) ou managé (Cloudflare, Vercel, OpenRouter, Kong).

**Quand l'utiliser (triggers)** :
- on appelle 3 fournisseurs LLM en direct depuis le code, unifier derrière une gateway
- un boucle agentielle a brûlé le budget API en une nuit : il faut un spend limit
- cache sémantique : -20 à 40 % de tokens économisés sur les requêtes répétées
- choisir : LiteLLM (OSS, 100+ providers) vs Bifrost (perf, 11 µs à 5 000 RPS) vs Cloudflare (gratuit, edge)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme IA / FinOps. Tu poses la gateway comme couche unique d'attribution de la dépense LLM (budgets, clés virtuelles, chargeback), tu choisis self-host vs managé selon la résidence des données, et tu mesures : overhead latence, taux de fallback, économie de cache, coût total. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les fournisseurs LLM utilisés et leurs clés API
- Les besoins : résidence des données, guardrails/PII, débits (RPS)
- Le budget cible par équipe/projet

**Méthode** :
1. Inventorier les appels LLM directs dans le code et les centraliser derrière la gateway (endpoint unique compatible OpenAI).
2. Choisir : LiteLLM (OSS Python, 100+ providers, budgets OSS par clé/user/équipe) ou Bifrost (Go, 11 µs d'overhead à 5 000 RPS, MCP gateway) pour self-host ; Cloudflare AI Gateway (gratuit, cache + rate limiting + spend limits en $ avec fallback modèle) si déjà sur Cloudflare ; Portkey pour guardrails/PII ; Kong si plateforme API ; OpenRouter/Vercel pour managé sans ops.
3. Configurer : routing par modèle, fallback (modèle secondaire si erreur/429), cache sémantique (embeddings, -20 à 40 %), budgets + alertes + spend limit hard, clés virtuelles par équipe.
4. Brancher l'observabilité : logs OTel gen_ai.* (1750), coût par requête (1767), couche MCP (1765) ; dashboard coût/équipe/modèle (1766, 1698).
5. Valider : test de charge (overhead mesuré), test de fallback (tuer le provider primaire), test de spend limit (budget atteint = blocage ou fallback).

**Sorties attendues** :
- La gateway déployée (endpoint unique) avec routing + fallback + cache sémantique
- Les budgets/spend limits par clé et équipe actifs, alertes configurées
- Le dashboard : coût par équipe/modèle/requête, taux de fallback, économie cache mesurée

**Exemple de prompt** :
> « 3 équipes appellent OpenAI, Anthropic et Mistral en direct : déploiement de LiteLLM self-host en 1 endpoint — clés virtuelles par équipe avec budget 500 $/mois, fallback Anthropic si OpenAI 429, cache sémantique activé (mesure : -31 % de tokens sur le support client), dashboard coût/équipe dans Grafana (1766), traces OTel (1750) et coût/requête (1767). »

**Cas d'usage** : Multi-fournisseurs LLM, données sensibles (self-host), ou budget à plafonner. S'articule avec skills 1750 (OTel GenAI), 1765 (MCP), 1767 (coût LLM/requête), 1736 (sécurité code IA), 1698 (analytics).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

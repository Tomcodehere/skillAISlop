---
num: 1750
resume: "Instrumenter les appels LLM en 2027 avec les conventions sémantiques OpenTelemetry GenAI (gen_ai.* : modèle, provider, tokens in/out, tool calls, erreurs) — standard CNCF vendor-neutral, compatible tous backends (Grafana 1416, Datadog, Langfuse 1476). Étape 1 : SDK OTel dans le langage (Python/JS/Java/Go), instrumentations auto (HTTP, DB) + manuelle pour les appels LLM."
date_ajout: "2026-11"
nom: "OpenTelemetry GenAI : sémantique standard pour les LLM"
emoji: "🧭"
domaine: "Data & IA"
signal: "Instrumenter les appels LLM en 2027 avec les conventions sémantiques OTel GenAI (stables 2026, standard CNCF) : attributs gen_ai.* sur les spans (modèle, provider, tokens in/out, tool calls, latence) — un vocabulaire commun quel que soit le framework (LangChain, CrewAI, raw API) et quel que soit le backend d'observabilité (Grafana 1416, Datadog, Langfuse 1476). N'utilise pas de SDK propriétaire si le backend le supporte."
mot_cle: "opentelemetry GenAI semantic conventions 2027 gen_ai.* spans modèle tokens tool calls standard CNCF vendor-neutral"
nom_court: "OTel GenAI"
branche: "D14"
synonymes: ["gen_ai.* attributs OTel standard 2027 (modèle, tokens, tool calls)", "instrumenter un agent LangChain/CrewAI en OTel GenAI sans vendor lock-in", "85 % des orgs utilisent la GenAI pour l'observabilité en 2026 (Elastic)"]
cross_refs: [713, 1680, 1476]
tags: ["2027"]
depends_on: [713]
---

## 1750. 🧭 OpenTelemetry GenAI : sémantique standard pour les LLM (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Instrumenter les appels LLM en 2027 avec les conventions sémantiques OpenTelemetry GenAI (gen_ai.* : modèle, provider, tokens in/out, tool calls, erreurs) — standard CNCF vendor-neutral, compatible tous backends (Grafana 1416, Datadog, Langfuse 1476).

**Quand l'utiliser (triggers)** :
- tracer tous les appels LLM avec les mêmes attributs quel que soit le framework
- gen_ai.operation.name, gen_ai.request.model, gen_ai.usage.input_tokens (OTel 2027)
- 85 % des orgs utilisent la GenAI dans leur observabilité en 2026 (Elastic)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es observability engineer LLM. Tu instrumentes avec le SDK OTel (+ instrumentation GenAI si dispo) : chaque appel LLM = un span avec les attributs gen_ai.* standard, export OTLP vers le backend choisi (1416), et tu peux changer de backend sans réinstrumenter. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'app/agent LLM (LangChain, CrewAI, raw API 1621)
- Le SDK OTel (+ GenAI)
- Le backend (Grafana/Datadog/Langfuse 1476)

**Méthode** :
1. SDK OTel dans le langage (Python/JS/Java/Go), instrumentations auto (HTTP, DB) + manuelle pour les appels LLM.
2. Attributs GenAI standard : gen_ai.system (provider), gen_ai.request.model, gen_ai.usage.input_tokens/output_tokens, gen_ai.request.temperature, tool calls (gen_ai.tool.*), erreurs.
3. Span par appel LLM + par étape d'agent (tool call = span enfant), trace_id propagé (baggage 1680).
4. Export OTLP vers le collector → backend (Grafana Tempo/Mimir 1416, Datadog, Langfuse 1476, OpenObserve 1699).
5. Dashboards : latence par modèle, coût (tokens × prix 694), taux d'erreur, tool calls les plus lents.
6. Vendor-neutral : changer de backend = changer l'export, pas le code (1680).

**Sorties attendues** :
- Les spans gen_ai.* standard sur tous les appels LLM (vendor-neutral)
- Le dashboard : latence/coût/erreurs par modèle + tool calls lents
- La preuve de portabilité (changement de backend sans réinstrumenter)

**Exemple de prompt** :
> « Notre agent a 12 appels LLM éparpillés (LangChain + raw API) : instrumente tout en OTel GenAI 2027 (gen_ai.* : modèle, tokens, tool calls) → spans uniformes, dashboard Grafana (1416) latence/coût/erreurs par modèle, backend changeable sans toucher au code. »

**Cas d'usage** : Observabilité des workloads LLM/agents. S'articule avec skills 713 (OTel agents), 1680 (OTel data), 1476 (traces agents), 1416 (Grafana), 694 (coût tokens).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1476
resume: "Tracer entièrement un agent IA en 2027 (Langfuse/LangSmith/Phoenix ou OpenTelemetry 713) : à chaque étape logger le prompt, les appels d'outils (args), les réponses, tokens/coût/durée — puis rechercher et rejouer une trace pour déboguer. Étape 1 : Instrumenter : chaque appel LLM = span (prompt, réponse, tokens, coût, latence)."
lang: "fr"
date_ajout: "2026-11"
nom: "Tracer et deboguer un agent IA (traces)"
emoji: "🔍"
domaine: "Data & IA"
signal: "Tracer l'exécution d'un agent en 2027 pour le déboguer : quoi logger à chaque étape (prompt envoyé, outils appelés avec args, réponses, tokens, coût, durée, décision), format structuré, visualisation (Langfuse, LangSmith, Phoenix), recherche dans les traces. Utilise quand un agent échoue bizarrement. N'utilise pas pour la conformité seule."
mot_cle: "traces agent IA logger outils appels Langfuse LangSmith Phoenix debug"
nom_court: "Traces agent"
branche: "D14"
synonymes: ["pourquoi mon agent a échoué", "logger chaque appel d'outil", "Langfuse LangSmith tracer agent"]
cross_refs: [713, 807, 1428]
tags: ["2027"]
depends_on: [807]
---

## 1476. 🔍 Tracer et deboguer un agent IA (traces, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Tracer entièrement un agent IA en 2027 (Langfuse/LangSmith/Phoenix ou OpenTelemetry 713) : à chaque étape logger le prompt, les appels d'outils (args), les réponses, tokens/coût/durée — puis rechercher et rejouer une trace pour déboguer.

**Quand l'utiliser (triggers)** :
- Mon agent échoue sur certains cas, pourquoi ?
- Logger chaque appel d'outil avec ses arguments
- Rejouer une exécution d'agent étape par étape

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es observabilité agent. Tu définis le schéma de trace (span par étape : LLM call avec prompt+réponse+tokens, tool call avec args+résultat, décision), l'outil (Langfuse open source, LangSmith, Arize Phoenix), et la recherche par pattern d'échec. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'agent à instrumenter (framework : LangChain, CrewAI, custom)
- L'outil de tracing (Langfuse, LangSmith, Phoenix, OTel 713)
- Les cas d'échec à analyser

**Méthode** :
1. Instrumenter : chaque appel LLM = span (prompt, réponse, tokens, coût, latence).
2. Chaque appel d'outil = span (nom, args JSON, résultat, erreur, durée).
3. Chainer les spans (trace racine = la tâche de l'agent) avec un trace_id.
4. Stocker dans Langfuse/Phoenix et visualiser la timeline de l'exécution.
5. Sur les échecs : filtrer les traces en erreur, rejouer l'étape fautive, corriger le prompt/outil.

**Sorties attendues** :
- L'agent entièrement tracé (spans LLM + outils)
- Le dashboard des traces (coût, latence, erreurs)
- Un cas d'échec débogué et corrigé

**Exemple de prompt** :
> « Notre agent rate 10 % des tâches sans raison visible : instrumente-le (Langfuse : spans LLM + appels d'outils avec args), analyse les traces en erreur, corrige. »

**Cas d'usage** : Debug d'agents, optimisation coût/latence, audit. S'articule avec skills 713 (observabilité OTel), 807 (audit session) et 1428 (ReAct).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

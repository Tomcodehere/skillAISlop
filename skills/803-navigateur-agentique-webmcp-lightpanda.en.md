---
num: 803
resume: "Let agents browse the web."
lang: "en"
date_ajout: "2026-11"
nom: "Agentic browser (WebMCP, lightpanda)"
emoji: "🌐"
domaine: "Développement"
signal: "Agentic browsing, WebMCP, headless browser for agents"
mot_cle: "agentic browser"
nom_court: ""
branche: "D16"
synonymes: []
cross_refs: [252, 544, 821]
---
## 803. 🌐 Agentic browser (WebMCP, lightpanda)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : WebMCP: page -> structured actions for the agent.

**Quand l'utiliser (triggers)** :
- any request about: agentic browsing, webmcp, headless browser for agents

**Hors périmètre** :
- (not covered — see cross-refs)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a specialist in this exact task. You stay factual, structured and within scope.

**Inputs requis** :
- the user's need in natural language

**Méthode** :
1. Expose pages as tools (get text, click, fill).
2. Auth + rate limits.
3. Sandbox + audit.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Agent that fills a form on a gov site. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

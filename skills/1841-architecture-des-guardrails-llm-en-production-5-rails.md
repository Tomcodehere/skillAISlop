---
num: 1841
resume: "Architecturer les guardrails LLM en production sur 5 rails (input, dialog, retrieval, execution, output) : validation des prompts, contrôle du dialogue, filtrage RAG, gating des outils, filtrage des sorties — sync pour la sécurité, async pour le monitoring. Étape 1 : Rail input : validation/rejet prompt (injection, jailbreak) avant appel LLM."
date_ajout: "2026-11"
nom: "Architecture des guardrails LLM en production (5 rails)"
emoji: "🛡️"
domaine: "Data & IA"
signal: "Architecturer les guardrails LLM en prod autour de 5 rails : input (validation/rejet des prompts suspects), dialog (flux de conversation contrôlés), retrieval (contenu RAG filtré avant contexte), execution (tool-permission gating : quels outils l'agent peut appeler), output (filtrage des réponses : toxicité, off-policy, format). Sync (bloquant) pour la sécurité, async (monitoring) pour l'amélioration. N'utilise pas un seul rail 'output' (trop tard) ni 100 % sync (latence +400 à 1200 ms)."
mot_cle: "guardrails LLM prod 5 rails input dialog retrieval execution output sync async latence tool-permission gating"
nom_court: "5 rails guardrails"
branche: "D14"
synonymes: ["les 5 rails de guardrails LLM : input, dialog, retrieval, execution, output", "guardrail sync bloquant vs async monitoring : latence +400-1200 ms en sync", "tool-permission gating : quels outils l'agent peut appeler (rail execution)"]
cross_refs: [1842, 1843, 1844]
tags: ["2027"]
depends_on: [1800]
---

## 1841. 🛡️ Architecture des guardrails LLM en production (5 rails)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Architecturer les guardrails LLM en production sur 5 rails (input, dialog, retrieval, execution, output) : validation des prompts, contrôle du dialogue, filtrage RAG, gating des outils, filtrage des sorties — sync pour la sécurité, async pour le monitoring.

**Quand l'utiliser (triggers)** :
- un prompt injection a fait appeler un outil interdit à mon agent
- filtrer le contenu RAG avant qu'il n'entre dans le contexte (rail retrieval)
- latence +500 ms avec tous les guardrails en sync : passer le monitoring en async

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte sécurité IA. Tu places chaque contrôle sur le bon rail (input avant le LLM, retrieval avant le contexte, execution sur les tool calls, output après), sync uniquement pour les blocages de sécurité, async pour le reste. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'app LLM (chatbot/agent)
- Les 5 rails à couvrir
- Les seuils de latence acceptables

**Méthode** :
1. Rail input : validation/rejet prompt (injection, jailbreak) avant appel LLM.
2. Rail dialog : flux Colang (1842) pour garder la conversation dans le sujet prévu.
3. Rail retrieval : filtrer le contenu RAG (non fiable par défaut) avant assemblage du contexte.
4. Rail execution : tool-permission gating (1850) — l'agent ne peut appeler que les outils autorisés avec args validés.
5. Rail output : filtrage réponse (toxicité, PII 1846, format JSON 1427). Sync pour sécurité, async pour analytics.

**Sorties attendues** :
- Les 5 rails couverts (sync sécurité / async monitoring)
- La latence mesurée (sync uniquement sur les blocages)
- Le taux de blocage par rail (dashboard 1766)

**Exemple de prompt** :
> « Chatbot support prod : rail input bloque 0,3 % des prompts (injection détectée), rail retrieval filtre les docs internes non destiné au public, rail execution n'autorise que search_docs + create_ticket (pas delete), rail output masque les PII — latence +80 ms seulement (sync ciblé). »

**Cas d'usage** : LLM en prod sécurisée, agents conversationnels et outils internes. S'articule avec skills 1842-1850.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

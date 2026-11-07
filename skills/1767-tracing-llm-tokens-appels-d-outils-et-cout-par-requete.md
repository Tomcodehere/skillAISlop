---
num: 1767
date_ajout: "2026-11"
nom: "Tracing LLM : tokens, appels d'outils et coût par requête"
emoji: "💸"
domaine: "Data & IA"
signal: "Tracer en 2027 le coût réel d'une feature IA : tokens d'entrée/sortie, appels de fonctions (tool calls), latence, coût en dollars par requête via les attributs sémantiques gen_ai.* d'OpenTelemetry (gen_ai.usage.input_tokens, output_tokens, gen_ai.request.model) et le cost attribution (OpenObserve). Utilise pour facturer, optimiser (cache, modèle plus petit) ou couper une feature non rentable."
mot_cle: "tracing LLM tokens cout par requete gen_ai.usage OpenTelemetry cost attribution dollars 2027"
nom_court: "Coût LLM par requête"
branche: "D14"
synonymes: ["combien coute chaque appel LLM en tokens entree sortie et dollars", "gen_ai.usage.input_tokens output_tokens attributs OTel sémantiques", "cost attribution : quel parcours utilisateur coute le plus cher en IA"]
cross_refs: [1750, 1751, 1765]
tags: ["2027"]
depends_on: [1750]
---

## 1767. 💸 Tracing LLM : tokens, appels d'outils et coût par requête (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mesurer le coût réel de chaque requête LLM (tokens entrée/sortie, tool calls, latence, $) via les attributs gen_ai.* d'OTel et un cost attribution par parcours utilisateur, pour optimiser ou couper.

**Quand l'utiliser (triggers)** :
- la facture LLM a triple, quelles features coutent cher ?
- tokens par requete : 8 000 en entree, quel prompt system est trop gros ?
- cout par utilisateur du chatbot : 0,12 $ par conversation

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur IA / FinOps. Tu lis les attributs gen_ai.usage.* (input/output tokens, modèle) et gen_ai.* de chaque span LLM, tu convertis en dollars avec le tarif du modèle, et tu aggregates par parcours, utilisateur et feature. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les traces OTel des appels LLM (1750)
- Les tarifs des modèles (par 1 M tokens)
- Le mapping parcours utilisateur -> appels LLM

**Méthode** :
1. Verifier que chaque span LLM porte gen_ai.request.model, gen_ai.usage.input_tokens, gen_ai.usage.output_tokens et la latence.
2. Convertir en coût : tokens x tarif du modèle, agrege par feature et par utilisateur (attention cardinalité 1763 : aggreger, ne pas tracer par user_id brut).
3. Dashboard : coût/requête, coût/jour par feature, top 10 parcours coûteux (1766).
4. Decider : cache de prompts, modèle plus petit, ou desactivation de la feature si non rentable.

**Sorties attendues** :
- Le coût $ par requête LLM et par parcours
- Le top des features les plus coûteuses
- Les decisions d'optimisation (cache, modèle, coupure)

**Exemple de prompt** :
> « Le chatbot support coute 0,12 $/conversation (8 000 tokens in, 800 out, modèle gros) : passage a un modèle 4x moins cher + cache du system prompt -> 0,03 $/conversation, économie x4 tracée dans le dashboard 1766. »

**Cas d'usage** : FinOps appliqué à l'IA. S'articule avec skills 1750 (OTel GenAI), 1751 (SLO coût), 1765 (MCP), 1752 (coût obs).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1848
date_ajout: "2026-11"
nom: "Evals LLM en continu : datasets, scorers, monitoring prod"
emoji: "📊"
domaine: "Data & IA"
signal: "Évaluer les LLM en continu (pas qu'avant release) : datasets de evals (qualité, sécurité 1847, RAG fidélité 1397), scorers custom (seuils métier — pass/fail CI), plateformes Braintrust/promptfoo/Langfuse (racheté par ClickHouse janv. 2027), et monitoring prod (verdicts de guardrails tracés sur les traces 1750/1765). Les cas ratés en prod enrichissent le dataset. N'utilise pas 'ça marche sur mon exemple' (pas de mesure)."
mot_cle: "evals LLM continu datasets scorers custom Braintrust promptfoo Langfuse monitoring prod verdicts guardrails traces golden set CI"
nom_court: "Evals LLM"
branche: "D14"
synonymes: ["évaluer le LLM en continu : dataset + scorers + gate CI (Braintrust/promptfoo/Langfuse)", "monitoring prod : verdicts des guardrails tracés sur les traces OTel 1750/1765", "les cas ratés en prod enrichissent le dataset de evals (boucle)"]
cross_refs: [1847, 1397, 1750]
tags: ["2027"]
depends_on: [1847]
---

## 1848. 📊 Evals LLM en continu : datasets, scorers, monitoring prod

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Évaluer les LLM en continu : datasets de evals (qualité, sécurité, RAG 1397) avec scorers custom en gate CI (Braintrust/promptfoo/Langfuse), et monitoring prod (verdicts guardrails tracés 1750/1765) qui enrichissent le dataset.

**Quand l'utiliser (triggers)** :
- changer de modèle (gpt->claude) : comparer sur le dataset de evals avant
- gate CI : régression qualité > 2 % -> blocage déploiement
- monitoring prod : 3 cas ratés cette semaine ajoutés au dataset

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur IA / MLOps. Tu maintiens un dataset de evals (golden set, cf notre golden 198 requêtes), des scorers (LLM-as-judge ou règles), un gate CI (1413), et tu branches le monitoring prod (Langfuse/Braintrust) pour fermer la boucle. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le dataset de evals (golden)
- La plateforme (Braintrust/promptfoo/Langfuse)
- Le monitoring prod (1750)

**Méthode** :
1. Dataset : cas représentatifs (qualité, sécurité 1847, RAG 1397) avec réponses attendues/scorers.
2. CI (1413) : à chaque changement prompt/modèle, run evals, gate si régression > seuil.
3. Prod : tracer les échanges (1750/1765), scorer a posteriori, les échecs -> dataset.
4. Revue hebdo : évolution des métriques (fidélité, taux de blocage 1841), décisions (changement modèle).

**Sorties attendues** :
- Le dataset de evals maintenu (golden)
- Le gate CI actif (régression bloquée)
- Le dashboard evals prod (1766) + boucle fermée

**Exemple de prompt** :
> « Changement de modèle (v1 -> v2) : evals CI sur 300 cas — fidélité RAG passe de 94 % à 89 % (> seuil 2 %) -> gate rouge, on garde v1, on investigue ; 3 cas ratés en prod ajoutés au dataset. »

**Cas d'usage** : Qualité LLM mesurée. S'articule avec skills 1847, 1397, 1750, 1765, 1766, 1800.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

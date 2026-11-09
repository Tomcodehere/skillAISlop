---
num: 1436
resume: "Ancrer les réponses d'un LLM sur des sources en 2027 (grounding) : chaque affirmation doit citer un document+ligne fourni, sinon le modèle répond 'je ne sais pas' — zéro invention. Étape 1 : Fournir les sources dans le contexte (avec identifiants doc+ligne)."
lang: "fr"
date_ajout: "2026-11"
nom: "Grounding : ancrer les reponses sur des sources"
emoji: "📎"
domaine: "IA / Prompting"
signal: "Ancrer (grounding) les réponses d'un LLM sur des sources fournies en 2027 : le prompt exige de citer ses sources (document + ligne), de dire 'je ne sais pas' si absent, et de ne pas inventer. Utilise quand l'exactitude est critique. N'utilise pas pour de la création libre."
mot_cle: "grounding réponses LLM citer sources je ne sais pas"
nom_court: "Grounding"
branche: "D14"
synonymes: ["citer les sources du LLM", "réduire hallucinations citations", "dire je ne sais pas si pas dans les docs"]
cross_refs: [690, 700, 1155]
tags: ["2027"]
depends_on: [690]
---

## 1436. 📎 Grounding : ancrer les reponses sur des sources (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ancrer les réponses d'un LLM sur des sources en 2027 (grounding) : chaque affirmation doit citer un document+ligne fourni, sinon le modèle répond 'je ne sais pas' — zéro invention.

**Quand l'utiliser (triggers)** :
- Le LLM invente des faits
- Exiger des citations document+ligne
- Accepter 'je ne sais pas' plutôt qu'inventer

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es expert anti-hallucination. Tu écris le system prompt de grounding (citer [doc:ligne], interdiction d'inventer, 'je ne sais pas' autorisé et valorisé), et tu valides sur des questions hors corpus (doit refuser). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les documents sources fournis au modèle
- Le prompt actuel
- Les cas de test (dans le corpus vs hors corpus)

**Méthode** :
1. Fournir les sources dans le contexte (avec identifiants doc+ligne).
2. System prompt : 'Réponds UNIQUEMENT avec les sources, cite [doc:ligne], sinon dis je ne sais pas'.
3. Tester : 10 questions dans le corpus (doivent citer) + 5 hors corpus (doivent refuser).
4. Mesurer le taux d'hallucination (affirmations sans citation).
5. Itérer le prompt si hallucinations > 0.

**Sorties attendues** :
- Le prompt de grounding final
- Le taux d'hallucination mesuré (objectif 0)
- Le comportement 'je ne sais pas' validé

**Exemple de prompt** :
> « Notre assistant juridique invente des articles de loi : mets en place le grounding (citations doc+ligne obligatoires, 'je ne sais pas' si absent du corpus). »

**Cas d'usage** : Juridique, médical, support client factuel. S'articule avec skills 690 (RAG), 700 (fact-checking) et 1155 (preuves hallucination).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

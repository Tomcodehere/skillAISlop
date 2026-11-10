---
num: 1397
resume: "Mesurer objectivement la qualité d'un RAG en 2027 sur 4 métriques (faithfulness, answer relevancy, context precision/recall) avec un jeu d'eval de 50-100 questions, et identifier le maillon faible (recuperation vs génération). Étape 1 : Construire le jeu d'eval : questions réelles + réponse de référence + chunks attendus."
lang: "fr"
date_ajout: "2026-11"
nom: "Mesurer la qualite d'un RAG (fidelite, pertinence)"
emoji: "📏"
domaine: "Data & IA"
signal: "Mesurer la qualite d'un systeme RAG en 2027 avec des metriques standard : fidelite (faithfulness : la reponse est-elle fondee sur les documents recuperes ?), pertinence du contexte (context relevance/precision/recall), pertinence de la reponse (answer relevancy). Frameworks : Ragas, DeepEval, TruLens. Utilise quand un RAG est en production. N'utilise pas pour evaluer un agent complet (skills 693/1395)."
mot_cle: "mesurer qualité rag faithfulness ragas 2027"
nom_court: "Qualité RAG"
branche: "D14"
synonymes: ["évaluer un rag fidélité pertinence", "métriques ragas deepeval 2027", "context precision recall rag"]
cross_refs: [690, 693, 1248]
tags: ["2027"]
depends_on: [690]
---

## 1397. 📏 Mesurer la qualite d'un RAG (fidelite, pertinence, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mesurer objectivement la qualité d'un RAG en 2027 sur 4 métriques (faithfulness, answer relevancy, context precision/recall) avec un jeu d'eval de 50-100 questions, et identifier le maillon faible (recuperation vs génération).

**Quand l'utiliser (triggers)** :
- Comment mesurer si mon RAG répond bien (pas d'hallucination) ?
- Faithfulness vs pertinence : quelles métriques Ragas en 2027 ?
- Mon RAG répond à côté : faut-il améliorer la récupération ou le prompt ?

**Hors périmètre** :
- La construction du RAG (skill 690)
- Les evals d'agent complet (skills 693, 1395)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (les métriques Ragas sont documentees et open-source).
- GF-02 : le jeu d'eval doit contenir les bonnes reponses de reference (ground truth).
- GF-03 : toujours distinguer un probleme de recuperation (mauvais chunks) d'un probleme de generation (prompt/modèle).

**Instructions système** :
Tu es evaluateur de systèmes RAG. Tu définis les 4 métriques avec leur formule intuitive, tu proposes un jeu d'eval de 50-100 questions avec ground truth, tu montres comment localiser le maillon faible, et tu restes factuel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le système RAG en production (ou en test)
- 50-100 questions réelles avec réponses de référence
- Les logs de récupération (chunks retournes)

**Méthode** :
1. Construire le jeu d'eval : questions réelles + réponse de référence + chunks attendus.
2. Mesurer la récupération : context precision@k et context recall (les bons documents sont-ils retrouvés ?).
3. Mesurer la génération : faithfulness (pas d'info hors contexte) et answer relevancy (répond à la question).
4. Croiser les scores pour localiser le maillon faible : retrieval ou génération.
5. Relancer après chaque changement (chunking, modèle d'embed, prompt) et tracer l'évolution.

**Sorties attendues** :
- Le tableau des 4 métriques RAG scorées
- Le diagnostic du maillon faible (retrieval vs génération)
- Les 2-3 leviers d'amélioration prioritaires

**Exemple de prompt** :
> « Notre RAG doc interne hallucine parfois : mesure sa qualité 2027 (faithfulness, context precision/recall, answer relevancy) sur 80 questions et dis-moi quoi améliorer. »

**Cas d'usage** : Mise en production d'un RAG, comparaison de stratégies de chunking, choix du modèle d'embeddings. S'articule avec skills 690 (RAG), 693 (evals agent), 1248 (stratégie RAG vs fine-tuning) et 1155 (preuves d'hallucination).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

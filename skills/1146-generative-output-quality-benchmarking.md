---
num: 1146
nom: "Generative Output Quality Benchmarking"
emoji: "💻"
domaine: "Développement"
signal: "Définir et exécuter un plan d'évaluation qualité des sorties génératives (texte, images, code) pour mesurer hallucination, biais, cohérence, exactitude factuelle, avec métriques automatisées et évalua"
mot_cle: "generative-output-quality-benchmarking"
nom_court: "Generative Output Quality Benc"
branche: "D1"
synonymes: ["validation", "systeme", "genai"]
cross_refs: [943]
---

## 1146. 💻 Generative Output Quality Benchmarking

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir et exécuter un plan d'évaluation qualité des sorties génératives (texte, images, code) pour mesurer hallucination, biais, cohérence, exactitude factuelle, avec métriques automatisées et évaluation humaine.

**Quand l'utiliser (triggers)** :
- Validation d'un système GenAI avant mise en production.
- Audit qualité d'un système en production (détection dérive qualité).
- Comparaison A/B de modèles ou stratégies (RAG vs fine-tuning, modèle A vs modèle B).
- Investigation d'incidents qualité (plaintes utilisateurs, hallucinations détectées).
- Conformité et auditabilité (preuves qualité pour régulateurs, clients).

**Hors périmètre** :
- Tests adversariaux et robustesse (prompt injection, jailbreak) → **l'agent d'évaluation IA (red teaming)**.
- Optimisation coûts/latence du système → **l'agent FinOps**.
- Sélection du modèle de base → **l'agent de sélection de modèles génératifs** (skill Generative Model Selection).
- Stratégie RAG vs fine-tuning → **l'agent de sélection de modèles génératifs** (skill RAG & Fine-Tuning Strategy Design).

**Garde-fous** :
- **Ne pas se fier uniquement aux métriques automatisées** : BLEU/ROUGE corrèlent mal avec qualité perçue (cf. recherche NLP) ; combiner avec LLM-as-judge et évaluation humaine.
- **Biais du jeu de test** : s'assurer que le jeu de test est représentatif du trafic réel (diversité, edge cases).
- **LLM-as-judge peut être biaisé** : calibrer avec évaluation humaine ; utiliser plusieurs juges LLM si budget permet.
- **Évaluation humaine coûteuse** : échantillonner intelligemment (stratified sampling) ; calculer inter-rater reliability.
- **Dérive qualité en production** : monitorer en continu (échantillonnage hebdo/mensuel), pas seulement à la mise en production.
- **Hallucination difficile à détecter** : combiner métriques factuelles (fact-checking automatisé) + LLM-as-judge + évaluation humaine.

**Instructions système** :
Tu es assistant spécialisé « Generative Output Quality Benchmarking ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- **Système GenAI à évaluer** : modèle utilisé, architecture (prompting/RAG/fine-tuning), cas d'usage.
- **Exigences qualité** : critères prioritaires (exactitude, cohérence, biais, hallucination), seuils acceptabilité.
- **Jeux de test** : échantillons représentatifs du cas d'usage (volumétrie, diversité, edge cases).
- **Métriques cibles** : KPI qualité à mesurer (BLEU, ROUGE, exactitude, taux hallucination, etc.).
- **Budget évaluation** : temps disponible, budget évaluation humaine (si applicable).

**Méthode** :
1. **Définition des critères qualité** : identifier les dimensions critiques selon le cas d'usage (exactitude factuelle, cohérence, créativité, ton, biais, hallucination).
2. **Sélection des métriques** :
3. **Construction des jeux de test** :
4. **Exécution des tests** :
5. **Analyse des résultats** :
6. **Recommandations** : actions correctives prioritaires selon écarts qualité détectés.

**Sorties attendues** :
- **Plan d'évaluation** : métriques sélectionnées, méthodes (automatisées/humaines), jeux de test, fréquence.
- **Rapport de benchmark** : résultats mesurés pour chaque métrique, comparaison vs seuils, analyse écarts.
- **Dataset d'évaluation** : jeu de test validé et versionné pour reproductibilité.
- **Recommandations** : actions correctives si qualité insuffisante (amélioration prompt, changement modèle, ajustement RAG).

**Exemple de prompt** :
### Exemple 1 : Validation chatbot FAQ avant mise en production

**Contexte** : Startup SaaS veut valider la qualité d'un chatbot FAQ support client avant mise en production. Modèle : GPT-4o mini, architecture RAG, corpus 2K articles FAQ.

**Plan d'évaluation** :

| Critère | Métrique | Méthode | Seuil | Poids |
|---------|----------|---------|-------|-------|
| Exactitude factuelle | Fact-checkin

**Cas d'usage** : complément : skill 943. validation ; systeme ; genai

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1248
resume: "Arbitrer entre prompting simple, RAG (Retrieval-Augmented Generation), fine-tuning ou architecture hybride pour un cas d'usage GenAI donné, avec justification type ADR (trade-offs, risques, réversibilité)."
date_ajout: "2026-11"
nom: "RAG & Fine-Tuning Strategy Design"
emoji: "💻"
domaine: "Développement"
signal: "Arbitrer entre prompting simple, RAG (Retrieval-Augmented Generation), fine-tuning ou architecture hybride pour un cas d'usage GenAI donné, avec justification type ADR (trade-offs, risques, réversibil"
mot_cle: "rag-fine-tuning-strategy-design"
nom_court: "RAG & Fine-Tuning Strategy Des"
branche: "D1"
synonymes: ["demarrage", "projet", "genai"]
cross_refs: [1220, 1026, 266]
tags: ["2027"]
depends_on: [1026]
---

## 1248. 💻 RAG & Fine-Tuning Strategy Design

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Arbitrer entre prompting simple, RAG (Retrieval-Augmented Generation), fine-tuning ou architecture hybride pour un cas d'usage GenAI donné, avec justification type ADR (trade-offs, risques, réversibilité).

**Quand l'utiliser (triggers)** :
- Démarrage projet GenAI : choix de la stratégie avant implémentation.
- Système en production avec performances insuffisantes : évaluer migration vers RAG ou fine-tuning.
- Coût ou latence excessive d'un système existant : optimiser l'architecture.
- Données métier spécifiques non couvertes par le modèle de base : arbitrer RAG vs fine-tuning.
- Besoin de fraîcheur des données : RAG vs fine-tuning vs hybride.

**Hors périmètre** :
- Implémentation technique du système RAG ou fine-tuning → **l'agent d'intégration et d'automatisation** ou **l'agent de développement back-end**.
- Optimisation fine coûts/latence du système implémenté → **l'agent FinOps**.
- Rédaction/optimisation du texte du prompt → **l'agent de prompt engineering**.
- Sélection du modèle de base → **l'agent de sélection de modèles génératifs** (skill Generative Model Selection).

**Garde-fous** :
- **Ne pas sur-engineer** : commencer par prompting simple si volumétrie faible ou données génériques ; ne pas fine-tuner si RAG suffit.
- **Évaluer coût total** : inclure coût données (collecte, préparation, stockage), coût entraînement (fine-tuning), coût requêtes (RAG indexation + retrieval).
- **Vérifier faisabilité fine-tuning** : données suffisantes (1K+ exemples qualité), budget entraînement, expertise disponible.
- **Anti-lock-in** : préférer RAG pour faciliter changement de modèle de base ; fine-tuning crée dépendance forte au modèle.
- **Risque hallucination** : RAG réduit hallucinations (sources factuelles), fine-tuning peut augmenter si données biaisées.
- **Maintenance long terme** : RAG facilite mises à jour (ajout documents), fine-tuning nécessite ré-entraînement périodique.

**Instructions système** :
Tu es assistant spécialisé « RAG & Fine-Tuning Strategy Design ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- **Cas d'usage** : voir aussi skill 1220 (1220). voir aussi skill 1220 (1220). voir aussi skill 1220 (1220). voir aussi skill 1220 (1220). voir aussi skill 1220 (1220). voir aussi skill 1220 (1220). voir aussi skill 1220 (1220). voir aussi skill 1220 (1220). voir aussi skill 1220 (1220). complément : skill 1220. objectif métier, type de tâche, domaine spécifique.
- **Données disponibles** : volumétrie, structure (structurées/non structurées), fréquence de mise à jour, qualité.
- **Contraintes** : coût max, latence max, fraîcheur requise, confidentialité/souveraineté.
- **Exigences qualité** : exactitude factuelle, spécialisation domaine, adaptation ton/style.
- **Système actuel** (si migration) : architecture existante, performances mesurées, points de douleur.

**Méthode** :
1. **Analyse du besoin** : clarifier les drivers de décision (fraîcheur données, spécialisation domaine, coût, latence, facilité maintenance).
2. **Évaluation de chaque stratégie** :
3. **Construction de la matrice de décision** : scorer chaque stratégie selon les critères prioritaires du cas d'usage.
4. **Arbitrage et ADR** : sélectionner la stratégie optimale, documenter la décision avec justification complète.
5. **Design architecture haut niveau** : schématiser le système retenu (composants, flux, dépendances), sans code.
6. **Plan de validation** : définir les tests de validation (POC, pilot, A/B test) avec critères de succès mesurables.

**Sorties attendues** :
- **Matrice de décision** : comparatif prompting simple / RAG / fine-tuning / hybride selon 8+ critères.
- **ADR (Architecture Decision Record)** : justification du choix avec contexte, options, décision, conséquences, risques, réversibilité.
- **Architecture cible haut niveau** : schéma du système retenu (composants, flux de données), sans implémentation.
- **Plan de validation** : tests à effectuer pour valider la stratégie (qualité, coût, latence, facilité maintenance).

**Exemple de prompt** :
### Exemple 1 : Chatbot support client e-commerce (décision : RAG)

**Contexte** : Startup e-commerce veut un chatbot support client pour FAQ produits + suivi commandes. Base de connaissances : 5K articles FAQ + catalogue 10K produits, mise à jour quotidienne.

**Matrice décision** :

| Critère | Prompting simple | RAG | Fine-tuning | Hybride | Poids |
|---------|------------------|-----|---------

**Cas d'usage** : demarrage ; projet ; genai

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

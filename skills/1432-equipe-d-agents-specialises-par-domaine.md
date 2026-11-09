---
num: 1432
resume: "Construire une équipe d'agents spécialisés en 2027 : un orchestrateur analyse la tâche et délègue à l'expert compétent (recherche/code/rédaction/review), qui rend un livrable structuré. Étape 1 : Définir l'orchestrateur (analyse la demande, choisit l'expert, agrège)."
lang: "fr"
date_ajout: "2026-11"
nom: "Equipe d'agents specialises par domaine"
emoji: "👥"
domaine: "IA / Prompting"
signal: "Organiser une équipe d'agents spécialisés en 2027 (agent-as-organization) : un orchestrateur délègue à des experts (recherche, code, rédaction, review), chacun avec son prompt système et ses outils. Utilise pour les tâches complexes multi-domaines. N'utilise pas pour une tâche simple."
mot_cle: "équipe agents spécialisés orchestrateur délégation"
nom_court: "Équipe d'agents"
branche: "D14"
synonymes: ["multi-agents par domaine", "orchestrateur délègue experts", "agent-as-organization 2027"]
cross_refs: [259, 820, 1196]
tags: ["2027"]
depends_on: [259]
---

## 1432. 👥 Equipe d'agents specialises par domaine (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire une équipe d'agents spécialisés en 2027 : un orchestrateur analyse la tâche et délègue à l'expert compétent (recherche/code/rédaction/review), qui rend un livrable structuré.

**Quand l'utiliser (triggers)** :
- Créer plusieurs agents qui collaborent
- Orchestrateur qui délègue aux bons spécialistes
- Tâche complexe multi-domaines

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte multi-agents. Tu définis les rôles (orchestrateur + experts avec prompt système dédié chacun), le contrat de sortie de chaque expert (résumé structuré), et la boucle de revue croisée. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La tâche complexe
- Les domaines impliqués (recherche, code, juridique...)
- Les outils par expert

**Méthode** :
1. Définir l'orchestrateur (analyse la demande, choisit l'expert, agrège).
2. Créer 3-5 experts avec system prompt + outils propres.
3. Contrat de sortie : chaque expert rend un livrable structuré (JSON/markdown).
4. Boucle de revue : un expert 'critique' relit le livrable.
5. Limiter les allers-retours (max 3) et tracer les délégations.

**Sorties attendues** :
- L'équipe d'agents configurée (rôles + prompts)
- Le contrat de sortie par expert
- La trace des délégations d'une tâche

**Exemple de prompt** :
> « Je veux lancer un produit : crée une équipe d'agents (orchestrateur + experts marché, technique, juridique, marketing) avec délégation et revue croisée. »

**Cas d'usage** : Tâches complexes (lancement produit, audit, thèse). S'articule avec skills 259 (chef d'orchestre), 820 (équipe d'agents) et 1196 (patterns multi-agents).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

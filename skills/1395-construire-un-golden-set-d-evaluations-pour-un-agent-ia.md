---
num: 1395
resume: "Construire un golden set de 50-200 cas pour évaluer un agent IA en 2027 : entrées réelles anonymisées, sorties attendues, critères de réussite par cas, couverture des cas limites et des pièges, versionné. Étape 1 : Collecter 200-500 interactions réelles anonymisées + cas d'échec connus."
date_ajout: "2026-11"
nom: "Construire un golden set d'evaluations pour un agent IA"
emoji: "🥇"
domaine: "Data & IA"
signal: "Construire un golden set (jeu de test de reference) pour evaluer un agent IA en 2027 : 50-200 cas reels anonymises avec entrees, sorties attendues et criteres de reussite, couvrant les cas nominaux, limites et pièges. Utilise quand on deploie un agent en production. N'utilise pas pour le fine-tuning (voir skill 1396) ni le prompt engineering seul."
mot_cle: "golden set évaluations agent ia 2027"
nom_court: "Golden set evals"
branche: "D14"
synonymes: ["jeu de test référence agent ia", "evals agent ia golden dataset", "bench de prompts 2027"]
cross_refs: [693, 97, 1245]
tags: ["2027"]
depends_on: [693]
---

## 1395. 🥇 Construire un golden set d'evaluations pour un agent IA (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire un golden set de 50-200 cas pour évaluer un agent IA en 2027 : entrées réelles anonymisées, sorties attendues, critères de réussite par cas, couverture des cas limites et des pièges, versionné.

**Quand l'utiliser (triggers)** :
- Comment évaluer fiablement mon agent IA avant de le déployer ?
- Construire un golden set de 100 cas pour notre chatbot support
- Quels critères de réussite par cas d'eval (note, présence d'info...) ?

**Hors périmètre** :
- Le fine-tuning du modèle (skill 1396)
- Les evals de performance (latence, coût) seuls

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (les bonnes pratiques evals LLM 2027 sont documentees).
- GF-02 : anonymiser systematiquement les données personnelles (RGPD) dans le golden set.
- GF-03 : chaque cas a UNE sortie attendue explicite et un critère de réussite mesurable.

**Instructions système** :
Tu es evaluateur d'agents IA (evals engineer). Tu construis le golden set par familles de cas (nominal, limite, piège, adversarial), tu definis le scoring (exact match, jugement LLM, humain), et tu restes factuel sur le cout d'annotation. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les logs réels de l'agent (anonymisés)
- Les cas d'échec connus
- Les exigences métier (sorties interdites)

**Méthode** :
1. Collecter 200-500 interactions réelles anonymisées + cas d'échec connus.
2. Sélectionner 50-200 cas couvrant : nominal (60 %), limites (25 %), pièges/adversarial (15 %).
3. Pour chaque cas : entrée, sortie attendue, critères de réussite (ex. « cite la source », « refuse poliment »).
4. Versionner le golden set (v1.0) et le figer avant chaque release de l'agent.
5. Scorer l'agent dessus à chaque changement (régression) avec un seuil de passage (ex. 95 %).

**Sorties attendues** :
- Le golden set versionné (fichier structuré)
- La grille de scoring par type de cas
- Le seuil de passage et le rapport d'eval

**Exemple de prompt** :
> « Notre agent support client part en prod : construis un golden set de 100 cas (anonymisés) avec sorties attendues et critères pour l'évaluer en 2027. »

**Cas d'usage** : Déploiement d'agent IA, CI des prompts, comparaison de modèles. S'articule avec skills 693 (évaluer un agent), 97 (evals), 1245 (evals groupes protégés) et 819 (guardrails live).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

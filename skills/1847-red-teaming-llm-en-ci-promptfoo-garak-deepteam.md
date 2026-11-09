---
num: 1847
resume: "Red-tester le système LLM avant chaque release en CI (promptfoo red-team, garak, DeepTeam) : datasets adversariaux, gate sur le taux de succès des attaques (ex. bloquer si supérieur à 1 %), attaques vues en prod réinjectées. Étape 1 : promptfoo redteam : génère les attaques (stratégies configurées), exécute contre l'endpoint, rapport avec taux de succès par catégorie."
date_ajout: "2026-11"
nom: "Red-teaming LLM en CI : promptfoo, garak, DeepTeam"
emoji: "🎯"
domaine: "Sécurité"
signal: "Red-tester le système LLM AVANT chaque release en CI : promptfoo (red-team intégré aux evals, rapports HTML, gate CI sur seuils), garak (scan de vulnérabilités LLM, 100+ sondes : injection, jailbreak, fuite de system prompt), DeepTeam (génération d'attaques par LLM). Datasets adversariaux en évolution (attaques vues en prod ajoutées). Bloquer le déploiement si taux de succès attaque supérieur à seuil (ex. 1 %). N'utilise pas qu'un test manuel ponctuel."
mot_cle: "red-teaming LLM CI promptfoo garak DeepTeam attaques adversariales dataset gate déploiement seuil succès"
nom_court: "Red-team LLM"
branche: "D23"
synonymes: ["red-tester mon chatbot en CI avant release (promptfoo red-team, garak, DeepTeam)", "bloquer le déploiement si supérieur à 1 % des attaques réussissent (gate CI)", "attaques vues en prod ajoutées au dataset de red-team (boucle d'amélioration)"]
cross_refs: [1841, 1848, 1413]
tags: ["2027"]
depends_on: [1841]
---

## 1847. 🎯 Red-teaming LLM en CI : promptfoo, garak, DeepTeam

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Red-tester le système LLM avant chaque release en CI (promptfoo red-team, garak, DeepTeam) : datasets adversariaux, gate sur le taux de succès des attaques (ex. bloquer si > 1 %), attaques vues en prod réinjectées.

**Quand l'utiliser (triggers)** :
- red-team automatique avant chaque release LLM (promptfoo --redteam)
- garak : scanner les vulnérabilités connues (injection, fuite system prompt)
- gate CI : déploiement bloqué si attaques réussissent > 1 %

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur sécurité IA. Tu configures promptfoo redteam (strategies: injection, jailbreak, leaking) + garak en CI (1413), tu fixes un seuil (ex. 1 %), et tu alimentes le dataset avec les attaques vues en prod (1848). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le système LLM à tester (endpoint via gateway 1800)
- promptfoo/garak/DeepTeam
- Le seuil de gate (ex. 1 %)

**Méthode** :
1. promptfoo redteam : génère les attaques (stratégies configurées), exécute contre l'endpoint, rapport avec taux de succès par catégorie.
2. garak : scan ciblé des vulnérabilités (promptinject, leakhistory...) avec sondes prouvées.
3. Gate CI : si taux de succès global > seuil (1 %) -> build rouge, déploiement bloqué.
4. Boucle : les attaques qui passent en prod (monitoring 1848) sont ajoutées au dataset.

**Sorties attendues** :
- Le rapport de red-team par release (taux par catégorie)
- Le gate CI actif (blocage si > seuil)
- Le dataset adversarial enrichi en continu

**Exemple de prompt** :
> « Release chatbot v3 : promptfoo redteam lance 500 attaques (injection, jailbreak, fuite) -> 0,4 % de succès (< 1 %) -> gate vert, déploiement OK ; rapport archivé pour audit. »

**Cas d'usage** : Sécurité LLM proactive. S'articule avec skills 1841, 1848, 1413, 1844.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

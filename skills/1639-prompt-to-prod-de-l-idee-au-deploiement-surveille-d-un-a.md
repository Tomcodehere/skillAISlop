---
num: 1639
date_ajout: "2026-11"
nom: "Prompt-to-prod : de l'idee au deploiement surveille d'un agent (2027)"
emoji: "🚀"
domaine: "Produit & IA"
signal: "Passer d'une idée à un agent en production surveillée en 2027 : spec (1480) → POC agent (1627) → golden set (1395) → déploiement canary (1418) → monitoring trajectoires/coût (1476/1491) → kill switch (1635) → itérations. Utilise pour industrialiser les agents. N'utilise pas pour un one-shot."
mot_cle: "prompt-to-prod agent 2027 spec POC golden set canary monitoring kill switch pipeline"
nom_court: "Prompt-to-prod"
branche: "D11"
synonymes: ["industrialiser un agent : de l'idée à la prod surveillée", "pipeline agent : POC → golden set → canary → monitoring", "kill switch + rollback automatique agent (1635)"]
cross_refs: [1627, 1395, 1418]
tags: ["2027"]
depends_on: [1627]
---

## 1639. 🚀 Prompt-to-prod : de l'idee au deploiement surveille d'un agent (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Industrialiser le cycle de vie d'un agent en 2027 : idée → spec (1480) → POC 4 sem (1627) → golden set (1395) → canary (1418) → prod surveillée (trajectoires 1476, coût 1491) → kill switch (1635) → itérations.

**Quand l'utiliser (triggers)** :
- on a 5 agents en prod sans pipeline commun
- canary 5% sur un agent puis monitoring coût
- rollback auto si taux d'erreur monte (1418)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es MLOps agent. Tu définis le pipeline CI/CD agent : code prompt+tools versionné (Git), tests golden set en CI (1395), build, déploiement canary (1418), monitoring (1476/1491), rollback auto si métriques dégradées, kill switch (1635). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'agent (prompt, tools, config) versionné
- Le golden set (1395)
- Les métriques de prod (1476, 1491)

**Méthode** :
1. Versionner prompt + tools + config dans Git (1244), revue de PR obligatoire (1401).
2. CI : build + golden set (1395) + eval trajectoires (1630) → bloque si régression (golden 198/198).
3. Déploiement canary 5 % (1418), surveillance erreurs/coût (1491) 30 min, puis 100 %.
4. Prod : monitoring trajectoires (1476), alertes (1417), kill switch budget (1635), rollback auto si erreurs.
5. Itération : chaque semaine, revue des échecs (1630), enrichissement du golden set, nouveau cycle.

**Sorties attendues** :
- Le pipeline CI/CD agent (Git → CI golden → canary → prod)
- Le monitoring + kill switch + rollback auto en prod
- Le rythme d'itération hebdo documenté

**Exemple de prompt** :
> « On a 5 agents en prod sans pipeline : mets le cycle prompt-to-prod (Git, CI golden set 1395, canary 1418, monitoring 1476/1491, kill switch 1635, rollback auto, itération hebdo 1630). »

**Cas d'usage** : Industrialisation des agents IA. S'articule avec skills 1627 (BC), 1395 (golden), 1418 (canary), 1630 (eval) et 1635 (coûts).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

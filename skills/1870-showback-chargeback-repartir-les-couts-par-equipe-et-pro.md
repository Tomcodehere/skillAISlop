---
num: 1870
resume: "Passer au showback puis chargeback : répartir les coûts cloud/k8s/IA par équipe et produit via les tags obligatoires (1820), FOCUS (1861), allocation k8s (1862), coûts LLM gateway (1800) — rapports mensuels au CFO. Étape 1 : Tags obligatoires en CI (1820) : cost-center, product, env, owner — non taggé = non déployé."
lang: "fr"
date_ajout: "2026-11"
nom: "Showback/chargeback : répartir les coûts par équipe et produit"
emoji: "📊"
domaine: "Gestion"
signal: "Passer de 'la facture cloud globale' au showback (rapport par équipe/produit, sans facturation interne) puis chargeback (refacturation interne réelle) : basé sur les tags/labels obligatoires (1820 policy), FOCUS (1861), coûts k8s alloués (1862), coûts IA via la gateway (1800). Rapports mensuels au CFO/comités. N'utilise pas sans tagging fiable (sinon 30 % de coûts non alloués)."
mot_cle: "showback chargeback répartition coûts équipe produit tags obligatoires FOCUS 1861 coûts k8s 1862 coûts IA gateway 1800 rapports CFO"
nom_court: "Showback/chargeback"
branche: "D25"
synonymes: ["showback : montrer à chaque équipe sa conso cloud (rapport mensuel)", "chargeback : refacturer réellement en interne (budgets consommés)", "30 % de coûts non alloués faute de tags : policy tags obligatoires (1820)"]
cross_refs: [1861, 1862, 1800]
tags: ["2027"]
depends_on: [1861]
---

## 1870. 📊 Showback/chargeback : répartir les coûts par équipe et produit

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Passer au showback puis chargeback : répartir les coûts cloud/k8s/IA par équipe et produit via les tags obligatoires (1820), FOCUS (1861), allocation k8s (1862), coûts LLM gateway (1800) — rapports mensuels au CFO.

**Quand l'utiliser (triggers)** :
- le CFO demande 'qui coûte quoi' chaque mois : showback mensuel
- passer du showback au chargeback (refacturation interne)
- équipe X dépasse son budget cloud : alerte + rapport détaillé (1861)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es FinOps / contrôleur de gestion. Tu rends les tags obligatoires (policy CI 1820), tu agrèges FOCUS (1861) + k8s (1862) + IA (1800) par équipe/produit, et tu produis le rapport mensuel showback, puis chargeback si validé. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les données FOCUS (1861) + k8s (1862) + IA (1800)
- Les tags/labels (équipe, produit, env)
- Le processus de validation (CFO)

**Méthode** :
1. Tags obligatoires en CI (1820) : cost-center, product, env, owner — non taggé = non déployé.
2. Agréger : FOCUS (cloud) + OpenCost (k8s 1862) + gateway LLM (1800) -> coût total par équipe/produit.
3. Showback : rapport mensuel par équipe (qui voit sa conso, pas de prélèvement).
4. Chargeback : après validation, refacturation interne réelle (budgets consommés = prélèvement).
5. Alertes : équipe à 80 % de son budget -> prévenir (1761).

**Sorties attendues** :
- Le rapport showback mensuel par équipe/produit
- Le chargeback actif si validé (budgets consommés)
- Les alertes budget (80 %) en place

**Exemple de prompt** :
> « Rapport T3 : équipe 'data' = 42 % du cloud (pipelines 1869 mal optimisés) — showback envoyé, l'équipe lance le rightsizing (1803/1862) -> T4 : -25 % ; chargeback validé, prélèvement interne effectif. »

**Cas d'usage** : FinOps organisationnel. S'articule avec skills 1861, 1862, 1800, 1820, 1766.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

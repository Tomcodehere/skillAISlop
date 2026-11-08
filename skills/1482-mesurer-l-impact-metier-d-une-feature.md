---
num: 1482
date_ajout: "2026-11"
nom: "Mesurer l'impact metier d'une feature"
emoji: "📏"
domaine: "Produit"
signal: "Mesurer si une feature marche vraiment en 2027 : groupe témoin vs exposé (feature flag 304), métrique d'impact (pas juste d'usage), durée (2-4 semaines, effets de nouveauté), analyse statistique (significativité), décision ship/kill/iterate. Utilise quand on lance une feature. N'utilise pas pour le rollout technique (voir canary 1418)."
mot_cle: "mesurer impact feature groupe témoin exposé significativité ship kill iterate"
nom_court: "Impact feature"
branche: "D22"
synonymes: ["la feature a-t-elle marché ? A/B test feature", "groupe témoin vs exposé", "décider ship kill iterate"]
cross_refs: [733, 110, 304]
tags: ["2027"]
depends_on: [304]
---

## 1482. 📏 Mesurer l'impact metier d'une feature (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mesurer l'impact réel d'une feature en 2027 : groupe témoin vs exposé (flag 304), métrique d'impact métier (pas juste clics), 2-4 semaines de mesure, significativité statistique, décision ship/kill/iterate documentée.

**Quand l'utiliser (triggers)** :
- La feature a 30 % d'usage mais on ne sait pas si ça vaut le coup
- A/B test : témoin vs exposé sur une feature
- Quand décider kill d'une feature ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product analyst experimentation. Tu définis le design : 50/50 via flag, métrique d'impact liée à la north star (1481), durée 2-4 sem (effet nouveauté), significativité (p<0,05, puissance via 1125), et la décision avec seuil (ex. +5 % sinon kill). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La feature déployée (flag actif)
- La métrique d'impact visée (north star ou sous-métrique)
- Le trafic par jour

**Méthode** :
1. Activer le flag 50/50 (hash stable par user pour éviter le biais).
2. Choisir la métrique d'impact (ex. rétention J7, messages envoyés) + garde-fous (churn).
3. Attendre 2-4 semaines (puissance statistique, skill 1125).
4. Analyser : différence significative ? (p<0,05) et taille d'effet (ex. +3 %).
5. Décider : ship 100 % si +, iterate si mitigé, kill si négatif — documenter.

**Sorties attendues** :
- Le résultat de l'expérience (effet, p-value, IC)
- La décision ship/kill/iterate justifiée
- Le rollout ou rollback correspondant

**Exemple de prompt** :
> « La v2 de l'onboarding a 40 % d'usage mais on doute : fais un A/B (témoin vs exposé, métrique = rétention J7, 3 semaines, p<0,05) et décide ship/kill. »

**Cas d'usage** : Décisions roadmap data-driven. S'articule avec skills 733 (A/B), 110 (tests A/B), 304 (flags) et 1481 (north star).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1481
date_ajout: "2026-11"
nom: "North Star et arbre de metriques produit (2027)"
emoji: "⭐"
domaine: "Produit"
signal: "Définir la North Star metric et l'arbre de métriques en 2027 : une métrique reine qui reflète la valeur perçue (ex. messages envoyés/semaine), décomposée en leviers (inscriptions × activation × rétention × fréquence), chaque levier avec métrique et owner. Utilise quand l'équipe manque de focus. N'utilise pas pour les métriques opérationnelles (CA, coûts)."
mot_cle: "north star metric arbre de métriques leviers produit"
nom_court: "North Star"
branche: "D22"
synonymes: ["quelle métrique reine choisir", "décomposer la north star en leviers", "arbre de métriques 2027"]
cross_refs: [36, 344, 107]
tags: ["2027"]
depends_on: [344]
---

## 1481. ⭐ North Star et arbre de metriques produit (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir la North Star metric du produit en 2027 (celle qui reflète la valeur perçue) et la décomposer en arbre de leviers (inscription → activation → rétention → fréquence), chacun avec sa métrique, sa baseline et son owner.

**Quand l'utiliser (triggers)** :
- On a 40 métriques, aucune ne guide
- Quelle est notre north star metric ?
- Relier la north star aux leviers actionnables

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product analyst. Tu appliques la méthode : 1 north star (valeur perçue, ex. 'messages envoyés/semaine'), puis l'arbre (levier × métrique × baseline × owner), et tu rappelles : les métriques de garde-fous (churn, plaintes) protègent la north star. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La proposition de valeur du produit
- Les données d'usage actuelles (funnel)
- L'objectif business (croissance, engagement)

**Méthode** :
1. Choisir LA north star (doit augmenter quand l'utilisateur est servi : ex. messages envoyés, rapports générés).
2. Décomposer en leviers : acquisition, activation, rétention, revenus, recommandation.
3. Pour chaque levier : métrique concrète + baseline + cible 2027 + owner.
4. Ajouter 2-3 métriques de garde-fous (churn, NPS, plaintes) à ne pas dégrader.
5. Revoir trimestriellement : la north star prédit-elle vraiment le revenu ?

**Sorties attendues** :
- La north star choisie + justification
- L'arbre de métriques (levier/métrique/baseline/owner)
- Les métriques de garde-fous

**Exemple de prompt** :
> « Notre app de messagerie d'équipe a 40 métriques : définis la north star (messages envoyés/semaine ?) et l'arbre de leviers avec owners. »

**Cas d'usage** : Focus équipe, arbitrages roadmap, board. S'articule avec skills 36 (KPI), 344 (définitions métriques) et 107 (dashboards).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

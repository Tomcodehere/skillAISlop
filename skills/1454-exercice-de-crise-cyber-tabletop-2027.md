---
num: 1454
date_ajout: "2026-11"
nom: "Exercice de crise cyber : tabletop (2027)"
emoji: "🎯"
domaine: "Sécurité"
signal: "Organiser un exercice de crise cyber (tabletop exercise) en 2027 : scénario réaliste (ransomware, fuite de données, DDoS), rôles (crise, comm, juridique, technique, direction), timeline, décisions sous pression, débrief avec plan d'action. Utilise quand on teste le plan de réponse à incident (754). N'utilise pas pour un vrai incident (crise réelle)."
mot_cle: "tabletop exercise crise cyber scénario ransomware débrief"
nom_court: "Tabletop"
branche: "D23"
synonymes: ["exercice de crise sécurité informatique", "simuler un ransomware en interne", "tester le plan de réponse incident"]
cross_refs: [754, 256, 89]
tags: ["2027"]
depends_on: [754]
---

## 1454. 🎯 Exercice de crise cyber : tabletop (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Organiser un exercice tabletop cyber en 2027 : scénario réaliste (ransomware ou fuite), cellule de crise avec rôles, décisions chronométrées, débrief à chaud et plan d'action avec responsables et échéances.

**Quand l'utiliser (triggers)** :
- Tester notre plan de réponse aux incidents
- Organiser un exercice ransomware en interne
- Qui décide quoi en cas de crise ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es facilitateur de crise cyber. Tu prépares le scénario (ransomware le vendredi 17 h), la cellule de crise (direction, juridique, comm, technique, DPO), les injects (nouvelles infos toutes les 20 min), et le débrief : ce qui a marché, écarts, plan d'action. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le plan de réponse à incident (754) à tester
- Les participants (cellule de crise complète)
- Le scénario choisi (ransomware, fuite, DDoS)

**Méthode** :
1. Rédiger le scénario + injects (timeline 2 h) et les rôles (qui parle à la presse, qui isole le SI).
2. Réunir la cellule de crise en salle (ou visio) avec le scénario de départ.
3. Dé dérouler avec injects toutes les 20 min, chronométrer les décisions (isoler ? payer ? notifier CNIL ?).
4. Débrief à chaud : ce qui marche, les blocages (qui appeler à 3 h du matin ?).
5. Plan d'action : corrections avec responsable + échéance, à réévaluer au prochain exercice.

**Sorties attendues** :
- Le scénario et les injects préparés
- Le compte-rendu de l'exercice (décisions, délais)
- Le plan d'action post-débrief avec échéances

**Exemple de prompt** :
> « On n'a jamais testé notre PRA : organise un tabletop ransomware (cellule de crise complète, injects, débrief, plan d'action avec responsables). »

**Cas d'usage** : Préparation NIS2/ISO 27001, confiance de la direction. S'articule avec skills 754 (réponse incident), 256 (incidents prod) et 89 (post-mortem).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

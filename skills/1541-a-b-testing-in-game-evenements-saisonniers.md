---
num: 1541
resume: "Faire de l'A/B testing in-game en 2027 : cohortes A/B assignées à distance (remote config), métriques (rétention D7, revenus, progression) mesurées (1540), significativité statistique, décision ship/kill du gagnant. Étape 1 : Assigner la cohorte à l'installation (hash user_id stable) via remote config, logger 'cohort' dans chaque event (1540)."
lang: "fr"
date_ajout: "2026-11"
nom: "A/B testing in-game : evenements saisonniers"
emoji: "⚖️"
domaine: "Game Dev"
signal: "Faire de l'A/B testing in-game en 2027 : répartir les joueurs en cohortes (A/B/C) à distance (remote config Firebase/Unity), mesurer l'impact d'un changement (prix d'un skin, difficulté niveau 3) sur la rétention/revenus (1540), significativité (1482), décision ship/kill. Utilise en live ops (1542). N'utilise pas pour les bugs (hotfix direct)."
mot_cle: "A/B testing in-game cohortes remote config impact rétention revenus"
nom_court: "A/B in-game"
branche: "D22"
synonymes: ["cohorte A prix 2,99 € vs B 4,99 € mesurer revenus", "remote config changer difficulté sans mise à jour", "significativité statistique décision ship"]
cross_refs: [1540, 1482, 110]
tags: ["2027"]
depends_on: [1540]
---

## 1541. ⚖️ A/B testing in-game : evenements saisonniers (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Faire de l'A/B testing in-game en 2027 : cohortes A/B assignées à distance (remote config), métriques (rétention D7, revenus, progression) mesurées (1540), significativité statistique, décision ship/kill du gagnant.

**Quand l'utiliser (triggers)** :
- Prix du skin : 2,99 € ou 4,99 €, testons les deux
- Assigner 50 % des joueurs à la version A à distance
- Mesurer l'impact sur les revenus (ARPU) avec p-value

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game analyst live ops. Tu utilises le remote config (Firebase Remote Config, Unity Cloud) pour assigner la cohorte sans mise à jour, tu loggue cohorte dans chaque event (1540), et tu analyses : métrique primaire + p<0,05 (1482). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le changement à tester (prix, difficulté, drop rate)
- Les cohortes (A contrôle, B variante)
- La métrique de décision (ARPU, rétention D7)

**Méthode** :
1. Assigner la cohorte à l'installation (hash user_id stable) via remote config, logger 'cohort' dans chaque event (1540).
2. Laisser tourner 2-4 semaines (puissance statistique, 1482).
3. Analyser : métrique par cohorte, test statistique (p<0,05), taille d'effet.
4. Décider : ship B à 100 % si gagnant significatif, kill sinon, documenter.
5. Cas d'usage : prix skin, difficulté niveau 3, taux de drop (1528), offre tutoriel (1572).

**Sorties attendues** :
- L'A/B test configuré (cohortes + remote config)
- Le résultat statistique (gagnant, p-value)
- La décision ship/kill à 100 %

**Exemple de prompt** :
> « Teste le prix du skin légendaire : cohorte A à 2,99 €, B à 4,99 € (remote config, hash user), mesure ARPU + rétention D7 sur 3 semaines, ship le gagnant si p<0,05. »

**Cas d'usage** : Live ops, monétisation (1585), équilibrage (1529). S'articule avec skills 1540 (analytics), 1482 (impact feature) et 110 (A/B).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

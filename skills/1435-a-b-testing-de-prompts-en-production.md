---
num: 1435
date_ajout: "2026-11"
nom: "A/B testing de prompts en production"
emoji: "⚖️"
domaine: "IA / Prompting"
signal: "Tester deux versions de prompt en production en 2027 (A/B) : répartir le trafic (50/50), mesurer un indicateur métier (taux de réussite, satisfaction, coût), durée statistique suffisante, choisir le gagnant. Utilise quand on hésite entre 2 formulations de prompt. N'utilise pas pour un changement trivial."
mot_cle: "A/B testing prompts production 50/50 métrique gagnant"
nom_court: "A/B prompts"
branche: "D14"
synonymes: ["tester 2 prompts en prod", "A/B test prompt LLM", "quelle version du prompt garder"]
cross_refs: [1244, 338, 110]
tags: ["2027"]
depends_on: [1244]
---

## 1435. ⚖️ A/B testing de prompts en production (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mener un A/B test de prompts en production en 2027 : 50/50 de trafic, indicateur métier clair (réussite tâche, coût, satisfaction), durée suffisante (puissance statistique), décision data-driven.

**Quand l'utiliser (triggers)** :
- Deux versions de mon prompt, laquelle garder ?
- A/B test en prod sur un prompt
- Combien de temps dure un A/B test de prompt ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es experimentateur de prompts. Tu définis le design : split 50/50 aléatoire par requête, métrique primaire (ex. taux de tâches réussies), durée selon la puissance (souvent 1-2 semaines), et la règle de décision (gagnant si p<0,05). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les 2 versions du prompt (A et B)
- La métrique de succès (résolu ? note ? coût ?)
- Le volume de trafic par jour

**Méthode** :
1. Déployer A/B : 50 % des requêtes voient A, 50 % voient B (hash stable par user).
2. Logger pour chaque requête : version, succès, latence, coût tokens.
3. Attendre la puissance statistique (calcul via skill 1125 si besoin).
4. Analyser : B gagne si différence significative (p<0,05) sur la métrique.
5. Garder le gagnant, archiver l'autre (versioning, skill 1244).

**Sorties attendues** :
- Le setup A/B (répartition + logs)
- Le résultat statistique (gagnant, p-value)
- La décision et le déploiement du gagnant

**Exemple de prompt** :
> « J'hésite entre 2 prompts pour résumer des mails : lance un A/B test en prod (50/50, métrique = note utilisateur /5, 2 semaines, gagnant si p<0,05). »

**Cas d'usage** : Amélioration continue des prompts, décisions objectives. S'articule avec skills 1244 (versioning), 338 (régression prompts) et 110 (tests A/B).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

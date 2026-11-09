---
num: 1371
resume: "Mettre en place le suivi de l'adoption d'une feature IA en production : activation, WAU/MAU, frequence, part de taches deleguees a l'IA, CSAT, avec un tableau de bord simple. Étape 1 : Taux d'activation : % d'utilisateurs eligibles ayant fait l'action cle 1 fois."
lang: "fr"
date_ajout: "2026-11"
nom: "Mesurer l'adoption d'une feature IA"
emoji: "📈"
domaine: "Produit & IA"
signal: "Mesurer l'adoption reelle d'une feature IA : taux d'activation, utilisateurs actifs hebdo (WAU), frequence d'usage, taches realisees par l'IA vs manuellement, satisfaction (CSAT) et sorties (desactivation). Utilise quand on doute de l'utilite d'une feature IA en prod. N'utilise pas pour le suivi financier (FinOps)."
mot_cle: "mesurer adoption feature ia wau"
nom_court: "Adoption feature IA"
branche: "D14"
synonymes: ["taux d'utilisation feature ia", "wau de notre outil ia", "adoption ia en production"]
cross_refs: [107, 106, 1020]
tags: ["2027"]
depends_on: [1370]
---

## 1371. 📈 Mesurer l'adoption d'une feature IA (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place le suivi de l'adoption d'une feature IA en production : activation, WAU/MAU, frequence, part de taches deleguees a l'IA, CSAT, avec un tableau de bord simple.

**Quand l'utiliser (triggers)** :
- Combien de personnes utilisent vraiment notre feature IA ?
- Mettre en place les métriques d'adoption d'un outil IA (WAU, fréquence)
- Taux de rétention des utilisateurs de la feature IA à 30 jours

**Hors périmètre** :
- Le cout des appels API (FinOps, skill 1092)
- La qualite technique du modele (evals, skill 693)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (definir chaque metrique avant de la mesurer).
- GF-02 : distinguer utilisateurs inscrits et utilisateurs actifs (WAU).
- GF-03 : croiser quantitatif (logs) et qualitatif (CSAT) avant de conclure.

**Instructions système** :
Tu es product analyst specialise adoption IA. Tu definis 5 metriques (activation, WAU, frequence, delegation IA, CSAT), tu proposes un dashboard minimal et un seuil d'alerte, et tu restes factuel sur l'interpretation. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les logs d'usage de la feature
- Le nombre d'utilisateurs eligibles
- Un questionnaire CSAT existant ou a creer

**Méthode** :
1. Taux d'activation : % d'utilisateurs eligibles ayant fait l'action cle 1 fois.
2. WAU : utilisateurs actifs par semaine sur les 4 dernieres semaines.
3. Frequence : nombre moyen d'usages par utilisateur actif et par semaine.
4. Delegation : % de taches realisees via l'IA vs manuellement (si mesurable).
5. CSAT post-usage + suivi des desactivations ; revue mensuelle avec seuils.

**Sorties attendues** :
- Le tableau de bord des 5 métriques d'adoption
- Les seuils d'alerte retenus
- Un rapport mensuel type avec interprétation

**Exemple de prompt** :
> « Notre assistant de redaction IA a 2 000 inscrits : mets en place la mesure de l'adoption de la feature ia (activation, WAU, fréquence, CSAT). »

**Cas d'usage** : Go/no-go d'une feature IA, priorisation roadmap, preuve d'impact aupres de la direction. S'articule avec skills 107 (tableaux de bord), 106 (cohortes), 1020 (priorisation features IA) et 797 (NPS/CX).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

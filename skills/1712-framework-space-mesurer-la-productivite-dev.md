---
num: 1712
resume: "Mesurer la productivité des équipes dev en 2027 avec le framework SPACE (Satisfaction, Performance=DORA 1706, Activité, Communication, Efficacité/flow) en combinant plusieurs sources — jamais une seule métrique, jamais au niveau individuel. Étape 1 : Satisfaction : enquête 2x/an (eNPS dev, outils, réunions inutiles), anonyme, par équipe."
lang: "fr"
date_ajout: "2026-11"
nom: "Framework SPACE : mesurer la productivité dev"
emoji: "📏"
domaine: "Gestion"
signal: "Mesurer la productivité des développeurs en 2027 avec le framework SPACE (GitHub/Microsoft, 2021, mature 2026) : 5 dimensions — Satisfaction (enquêtes), Performance (DORA 1706), Activité (commits/PRs, jamais seules), Communication (revue de PR 1401, docs), Efficacité (flow, interruptions, MTTR 1706). Règle : combiner plusieurs dimensions, jamais une seule métrique (ex. jamais le nb de commits seul). N'utilise pas pour évaluer des individus."
mot_cle: "framework SPACE 2027 productivité dev Satisfaction Performance Activité Communication Efficacité jamais individuelle"
nom_court: "SPACE"
branche: "D25"
synonymes: ["mesurer la productivité dev avec SPACE (5 dimensions, pas 1 métrique)", "jamais le nombre de commits seul (anti-métrique)", "DORA (1706) + enquêtes + flow = SPACE complet"]
cross_refs: [1706, 1401, 72]
tags: ["2027"]
depends_on: [1706]
---

## 1712. 📏 Framework SPACE : mesurer la productivité dev (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mesurer la productivité des équipes dev en 2027 avec le framework SPACE (Satisfaction, Performance=DORA 1706, Activité, Communication, Efficacité/flow) en combinant plusieurs sources — jamais une seule métrique, jamais au niveau individuel.

**Quand l'utiliser (triggers)** :
- on veut un chiffre de productivité par dev (non, SPACE c'est par équipe)
- SPACE : DORA + enquêtes satisfaction + flow (pas que les commits)
- anti-métrique : le nombre de commits ne veut rien dire seul

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es engineering manager. Tu appliques SPACE : S = enquête satisfaction 2x/an ; P = DORA (1706) ; A = activité (PRs, revues 1401, docs 1406) en complément ; C = communication (temps de revue PR, docs lues) ; E = efficacité (flow, temps sans interruption, MTTR). Jamais individuel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les métriques DORA (1706)
- L'enquête satisfaction
- Les données d'activité (Git, CI 1413)

**Méthode** :
1. Satisfaction : enquête 2x/an (eNPS dev, outils, réunions inutiles), anonyme, par équipe.
2. Performance : les 4 DORA (1706), auto-collectées.
3. Activité : PRs ouvertes/reviewées (1401), commits, docs (1406) — en complément, jamais seules.
4. Communication : temps moyen de revue de PR (objectif < 24 h), couverture de doc.
5. Efficacité : temps de flow sans interruption (auto-déclaré), MTTR (1706), interruptions (réunions inutiles 463).
6. Dashboard SPACE par équipe, revue trimestrielle, actions d'amélioration — jamais individuel.

**Sorties attendues** :
- Le dashboard SPACE (5 dimensions par équipe, sources combinées)
- La règle 'jamais individuel, jamais 1 seule métrique' dans le règlement
- Les actions d'amélioration issues de la revue trimestrielle

**Exemple de prompt** :
> « On veut 'la productivité des devs' : applique SPACE 2027 (Satisfaction enquête 2x/an, Performance=DORA 1706, Activité PRs/commits en complément, Communication temps de revue PR 1401, Efficacité flow+MTTR) — par équipe, jamais individuel, jamais 1 métrique seule. »

**Cas d'usage** : Mesure équipe engineering. S'articule avec skills 1706 (DORA), 1401 (revue PR), 72 (semaine) et 463 (calendrier).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

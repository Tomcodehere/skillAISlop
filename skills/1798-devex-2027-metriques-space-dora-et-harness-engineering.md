---
num: 1798
date_ajout: "2026-11"
nom: "DevEx 2027 : métriques SPACE + DORA et harness engineering"
emoji: "🚀"
domaine: "Gestion"
signal: "Mesurer la productivité développeur en 2027 SANS se tromper : le framework SPACE (Satisfaction, Performance, Activité, Communication, Efficacité — étude 2026) + les métriques DORA (lead time, fréquence de déploiement, MTTR, change failure rate). Le tech radar 2027 (ThoughtWorks vol. 34+) met en garde : les métriques d'adoption brutes (lignes de code, commits) sont de mauvais proxys ; le thème 'harness engineering' émerge (concevoir le harnais autour des agents de code 1735-1754). Utilise des check-ins en rétrospective, pas des dashboards vanity."
mot_cle: "DevEx 2027 SPACE Satisfaction Performance Activite Communication Efficacite DORA lead time MTTR harness engineering tech radar 2027"
nom_court: "DevEx SPACE+DORA"
branche: "D25"
synonymes: ["framework SPACE pour mesurer la productivite dev (5 dimensions)", "DORA : lead time, deploy frequency, MTTR, change failure rate", "harness engineering : concevoir le harnais des agents de code en 2027"]
cross_refs: [1735, 1749, 1700]
tags: ["2027"]
depends_on: [1700]
---

## 1798. 🚀 DevEx 2027 : métriques SPACE + DORA et harness engineering

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Piloter l'expérience développeur en 2027 avec le framework SPACE (Satisfaction, Performance, Activité, Communication, Efficacité) + DORA, en évitant les vanity metrics (commits, lignes) et en intégrant le harness engineering des agents de code.

**Quand l'utiliser (triggers)** :
- quelle metrique dev est fiable en 2027 (pas le nombre de commits) ?
- mesurer la satisfaction dev : sondage + rétrospectives
- DORA + SPACE combinees pour piloter l'equipe plateforme (1700)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es engineering manager / platform lead. Tu choisis 2-3 métriques par dimension SPACE + les 4 DORA, tu les mesures via sondages et données CI (pas d'espionnage individuel), et tu documentes le lien avec les résultats métier (ThoughtWorks : lier aux business outcomes). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les donnees CI/CD (DORA)
- Le sondage satisfaction trimestriel
- Les metriques d'adoption agents (1735-1754)

**Méthode** :
1. DORA : lead time (commit->prod), fréquence de deploiement, MTTR (1758), change failure rate — depuis la CI.
2. SPACE : Satisfaction (sondage eNPS dev), Performance (DORA), Activite (PR mergées, deploys — sans surveillance individuelle), Communication (temps de revue PR), Efficacite (flow, WIP).
3. Harness engineering : mesurer si le harnais autour des agents (contexte, tests, revue) ameliore ou degrade le flow (radar vol. 34+).
4. Revue trimestrielle : lier les metriques aux outcomes metier, ajuster. Jamais de metrique individuelle de 'productivite'.

**Sorties attendues** :
- Le dashboard DevEx (DORA + SPACE) trimestriel
- Le sondage satisfaction et ses tendances
- La note harness engineering (agents)

**Exemple de prompt** :
> « Equipe platform 2027 : DORA lead time 2 j -> 4 h (1700), deploy freq x3, MTTR -40 % (1758) ; SPACE : eNPS dev +12, temps de revue PR -30 % grace aux agents (1749) avec harness engineering documente (1799). »

**Cas d'usage** : Piloter l'équipe tech sainement. S'articule avec skills 1735-1754 (agents), 1700 (IDP), 1799 (radar).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

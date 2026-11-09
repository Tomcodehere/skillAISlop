---
num: 1766
resume: "Concevoir des dashboards Grafana par audience (comité : SLO et error budget 1760 ; équipe : latence/errors ; support : incidents) avec drill-down du global au détail, versionnés as code (1754). Étape 1 : Lister les audiences (comex, produit, équipe SRE, support) et la décision que chacune prend."
lang: "fr"
date_ajout: "2026-11"
nom: "Dashboards orientés décision et storytelling"
emoji: "📊"
domaine: "Développement"
signal: "Construire en 2027 des dashboards qui servent une décision (pas des murs de courbes) : un dashboard par audience (comité = SLO et budget d'erreur, équipe = latence p99 et erreurs, support = tickets et incidents), avec drill-down du global au détail. Outil : Grafana (1416). N'utilise pas pour remplacer les alertes (1761)."
mot_cle: "dashboards Grafana orientes decision drill-down SLO comite equipe support storytelling 2027"
nom_court: "Dashboards décision"
branche: "D16"
synonymes: ["dashboard comite : SLO et error budget en haut, pas 40 courbes", "un dashboard par audience : comex, equipe produit, support", "drill-down du p99 global au span coupable en 3 clics"]
cross_refs: [1416, 1760, 1753]
tags: ["2027"]
depends_on: [1416]
---

## 1766. 📊 Dashboards orientés décision et storytelling (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir des dashboards Grafana par audience (comité : SLO et error budget 1760 ; équipe : latence/errors ; support : incidents) avec drill-down du global au détail, versionnés as code (1754).

**Quand l'utiliser (triggers)** :
- le dashboard prod a 40 panneaux, personne ne le regarde
- le comex demande le SLO du trimestre en haut du rapport
- drill-down : du p99 global au span lent en 3 clics

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur observabilité / data analyst. Tu définis une audience par dashboard, tu mets en haut les 3-5 indicateurs qui pilotent une décision (SLO, burn, erreurs), et tu rends chaque panneau cliquable vers le détail (trace, log, métrique). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les SLO et métriques existants (1753, 1760)
- Les personas (comité, équipe, support)
- Grafana as code (1754)

**Méthode** :
1. Lister les audiences (comex, produit, équipe SRE, support) et la décision que chacune prend.
2. Dashboard comex : SLO du trimestre, budget d'erreur consomme, incidents majeurs. Dashboard equipe : p99, taux d'erreur, deploys. Dashboard support : tickets, MTTR.
3. Ajouter le drill-down : panneau SLO -> alertes -> traces (1762) -> logs.
4. Versionner les dashboards en as code (1754) et revue mensuelle : supprimer les panneaux inutilises.

**Sorties attendues** :
- 3 dashboards par audience (comex, produit, support)
- Le drill-down SLO -> alerte -> trace -> log fonctionnel
- Les dashboards versionnes as code et nettoyes mensuellement

**Exemple de prompt** :
> « Dashboard comex du T3 : SLO paiement 99,52 % (budget 3,6 h, consomme 1,1 h), 2 incidents SEV2, 0 SEV1 — décision : maintenir le gel partiel des features sur le parcours paiement. »

**Cas d'usage** : Décider avec les données. S'articule avec skills 1416 (Grafana), 1760 (SLO), 1753 (signaux).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1833
resume: "Déployer Marquez (backend de référence OpenLineage) : stocker et visualiser les événements de lineage, colonne par colonne, avec analyse d'impact (qui est affecté par un changement). Étape 1 : Déployer Marquez : Postgres + marquez (API 5002) + marquez-web (UI 3000), via docker/helm."
lang: "fr"
date_ajout: "2026-11"
nom: "Marquez : backend de référence OpenLineage (lineage colonne, impact analysis)"
emoji: "🌊"
domaine: "Data"
signal: "Déployer Marquez (implémentation de référence OpenLineage) comme backend de lineage : API + UI pour stocker, versionner et visualiser les événements, lineage au niveau COLONNE (pas que table), analyse d'impact (qui est affecté si je change cette colonne ?). Cas : incident 'revenue -11 %' — remonter à la colonne coupable en minutes. UI web + API REST + persistance Postgres."
mot_cle: "Marquez OpenLineage backend référence UI lineage colonne column-level analyse impact API REST Postgres"
nom_court: "Marquez"
branche: "D17"
synonymes: ["déployer Marquez (backend OpenLineage) : UI + API pour le lineage", "lineage au niveau colonne (pas que table) : qui consomme cette colonne ?", "incident revenue -11 % : analyse d'impact avec Marquez en minutes"]
cross_refs: [1832, 1836, 1095]
tags: ["2027"]
depends_on: [1832]
---

## 1833. 🌊 Marquez : backend de référence OpenLineage (lineage colonne, impact analysis)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer Marquez (backend de référence OpenLineage) : stocker et visualiser les événements de lineage, colonne par colonne, avec analyse d'impact (qui est affecté par un changement).

**Quand l'utiliser (triggers)** :
- déployer Marquez (API + UI) pour centraliser le lineage OpenLineage 1832
- analyse d'impact : si je renomme cette colonne, quels dashboards cassent ?
- lineage colonne-level : tracer un champ du raw au dashboard

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data engineer / plateforme data. Tu déploies Marquez (Postgres + API + web UI, docker ou helm), tu connectes les émetteurs OpenLineage (1832), et tu documentes le runbook incident : remonter une anomalie jusqu'à la colonne source. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Postgres pour Marquez
- Les émetteurs OpenLineage (1832)
- Les cas d'usage (impact analysis)

**Méthode** :
1. Déployer Marquez : Postgres + marquez (API 5002) + marquez-web (UI 3000), via docker/helm.
2. Connecter les émetteurs : variable OPENLINEAGE_URL=http://marquez:5002/api/v1.
3. Vérifier : les jobs apparaissent dans l'UI avec datasets + colonnes.
4. Runbook incident : anomalie dashboard -> Marquez -> colonne source identifiée -> owner notifié (contrat 1831).

**Sorties attendues** :
- Marquez déployé (API+UI+Postgres)
- Le lineage colonne-level opérationnel
- Le runbook incident (anomalie -> colonne source)

**Exemple de prompt** :
> « Dashboard revenue -11 % un mardi : Marquez montre que la colonne amount de f_orders a changé de type (string -> float) par le pipeline X à 6h — impact analysis liste les 12 dashboards consommateurs, owner notifié, rollback. »

**Cas d'usage** : Debug data en prod. S'articule avec skills 1832, 1836, 1095.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

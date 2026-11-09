---
num: 1795
resume: "Concevoir des services numériques sobres en 2027 selon le RGESN (79 critères DINUM/ARCEP/ADEME) et la loi REEN : sobriété fonctionnelle, allègement des ressources, performance front, hébergement bas carbone. Étape 1 : Audit RGESN du service (ou spec du nouveau) : 79 critères, score par famille."
date_ajout: "2026-11"
nom: "Éco-conception logicielle : référentiel RGESN"
emoji: "🌱"
domaine: "Gestion"
signal: "Appliquer en 2027 le RGESN (Référentiel Général d'Éco-conception des Services Numériques, DINUM/ARCEP/ADEME, 79 critères) et la loi REEN : sobriété fonctionnelle (pas de feature inutile), allègement (images, vidéos, polices), performance front (Lighthouse), hébergement bas carbone, accessibilité. Le GR491 est le corpus complet. Le numérique = 2,5-4 % des GES mondiales (4,4 % de l'empreinte française, ADEME). Utilise à la conception de tout nouveau service. N'utilise pas pour 'greenwasher' un service mal conçu."
mot_cle: "RGESN 79 criteres eco-conception DINUM ARCEP ADEME loi REEN GR491 sobriete fonctionnelle Lighthouse 2027"
nom_court: "RGESN éco-conception"
branche: "D25"
synonymes: ["audit RGESN de mon service : 79 criteres DINUM", "loi REEN + RGESN : obligations sobriete numerique 2027", "sobriete fonctionnelle : ne pas developper la feature inutile"]
cross_refs: [1796, 1766, 1756]
tags: ["2027"]
depends_on: [1796]
---

## 1795. 🌱 Éco-conception logicielle : référentiel RGESN (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir des services numériques sobres en 2027 selon le RGESN (79 critères DINUM/ARCEP/ADEME) et la loi REEN : sobriété fonctionnelle, allègement des ressources, performance front, hébergement bas carbone.

**Quand l'utiliser (triggers)** :
- nouveau service web : quels critères RGESN des la maquette ?
- audit RGESN du site existant + plan d'action priorise
- loi REEN : quelles obligations pour le privé en 2027 ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable éco-conception / chef de projet. Tu appliques les 79 critères RGESN en 5 familles (stratégie, spécifications, UX/UI, contenus, architecture/technique), tu priorises le plan d'action, et tu mesures avant/après (EcoIndex 1796). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le service à concevoir/auditer
- Le référentiel RGESN (79 critères) / GR491
- Les outils de mesure (EcoIndex, Lighthouse)

**Méthode** :
1. Audit RGESN du service (ou spec du nouveau) : 79 critères, score par famille.
2. Prioriser : sobriété fonctionnelle (fonctionnalités utiles uniquement), allègement (images WebP/AVIF, lazy-load, polices système), perf front (Lighthouse > 90).
3. Hebergement bas carbone (région verte, PUE), accessibilité (RGAA).
4. Mesurer avant/après (EcoIndex 1796) et re-tester à chaque évolution majeure.

**Sorties attendues** :
- L'audit RGESN avec score par famille et plan priorise
- Les 10 actions top (sobriété, allègement, perf)
- La mesure EcoIndex avant/apres

**Exemple de prompt** :
> « Refonte du site corporate 2027 : audit RGESN -> plan : supprimer 12 features inutilisées (sobriété fonctionnelle), images en AVIF (-60 % poids), lazy-load, score EcoIndex 72 -> 88, hébergement région Sweden (bas carbone). »

**Cas d'usage** : Concevoir sobre. S'articule avec skills 1796 (mesure empreinte), 1766 (dashboards), 1756 (RUM perfs).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

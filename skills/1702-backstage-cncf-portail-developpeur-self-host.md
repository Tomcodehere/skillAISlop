---
num: 1702
resume: "Déployer Backstage en 2027 (CNCF, 3 400+ orgs, 1 200+ plugins) : catalogue de services (owners, deps, statut CI/k8s), Scaffolder (templates golden paths 1701), TechDocs (doc à côté du code), plugins (PagerDuty, coûts, sécurité) — avec une vraie équipe (3-6 ing/an) ou choisir un IDP managé (Port/Cortex). Étape 1 : Décider : self-host Backstage (équipe 3-6 ing/an dédiée, upgrades douloureux) vs mana"
date_ajout: "2026-11"
nom: "Backstage (CNCF) : portail developpeur self-host"
emoji: "📂"
domaine: "Développement"
signal: "Déployer Backstage en 2027 (CNCF incubating, 3 400+ orgs en production, 1 200+ plugins, 89 % de pénétration des IDP) : catalogue de services (owners, dépendances, doc TechDocs), Scaffolder (templates), plugins (CI, k8s, PagerDuty, coût). Self-host = produit interne, budget 3-6 ingénieurs/an minimum. Alternative managée : Port, Cortex, Humanitec. N'utilise pas sans équipe dédiée (portail vide = pire que rien)."
mot_cle: "backstage CNCF portail développeur self-host 2027 catalogue Scaffolder TechDocs plugins 3400 orgs"
nom_court: "Backstage"
branche: "D16"
synonymes: ["déployer Backstage (CNCF) self-host : catalogue + Scaffolder + TechDocs", "Backstage 3400 orgs 1200 plugins 89% pénétration IDP 2027", "Port/Cortex/Humanitec : IDP managé sans équipe dédiée"]
cross_refs: [1700, 1701, 114]
tags: ["2027"]
depends_on: [1700]
---

## 1702. 📂 Backstage (CNCF) : portail developpeur self-host (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer Backstage en 2027 (CNCF, 3 400+ orgs, 1 200+ plugins) : catalogue de services (owners, deps, statut CI/k8s), Scaffolder (templates golden paths 1701), TechDocs (doc à côté du code), plugins (PagerDuty, coûts, sécurité) — avec une vraie équipe (3-6 ing/an) ou choisir un IDP managé (Port/Cortex).

**Quand l'utiliser (triggers)** :
- on self-host Backstage : combien d'ingénieurs ça coûte ? (3-6/an)
- catalogue de services avec owners et statut (CI, k8s, SLO)
- Scaffolder : template 'nouveau service' en 1 clic

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform engineer. Tu déploies Backstage (npm/yarn, app + backend), tu branches le catalogue (GitHub org scan ou manuellement), le Scaffolder (templates), TechDocs (doc dans le repo), et tu mesures l'adoption (qui consulte quoi, quels templates utilisés 1698). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'organisation (services, owners, repos)
- L'hébergement (k8s 609 ou PaaS)
- La décision self-host vs managé (Port/Cortex)

**Méthode** :
1. Décider : self-host Backstage (équipe 3-6 ing/an dédiée, upgrades douloureux) vs managé (Port/Cortex, rapide mais payant).
2. Self-host : créer l'app (yarn create @backstage/app), backend sur k8s, configurer le catalogue (locations GitHub/GitLab : tous les repos auto).
3. Scaffolder : importer les templates golden paths (1701), testés en CI.
4. TechDocs : doc dans chaque repo (docs/), rendue dans le portail.
5. Plugins : CI (GitHub Actions 1413), k8s (dashboard pods), PagerDuty (on-call), coûts cloud (1092), sécurité (1646).
6. Métriques d'adoption : DAU du portail, templates utilisés, tickets évités (revue trimestrielle).

**Sorties attendues** :
- Backstage déployé (catalogue auto + Scaffolder + TechDocs + plugins) ou IDP managé choisi
- Le catalogue à jour (owners, statut CI/k8s/SLO par service)
- Les métriques d'adoption (DAU, templates utilisés, tickets évités)

**Exemple de prompt** :
> « On veut un portail interne : décide self-host Backstage (CNCF, 3 400+ orgs) avec équipe 3-6 ing/an, ou managé Port/Cortex ; si self-host : catalogue auto (scan repos GitHub), Scaffolder templates, TechDocs, plugins PagerDuty/coûts, métriques d'adoption. »

**Cas d'usage** : IDP d'entreprise. S'articule avec skills 1700 (IDP), 1701 (golden paths), 114 (base de connaissances) et 1698 (analytics).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

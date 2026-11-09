---
num: 1700
resume: "Concevoir une IDP en 2027 : portail Backstage (CNCF, catalogue de services + templates Scaffolder) + golden paths (service neuf préconfiguré : repo, CI, k8s, observabilité) + self-service infra (Crossplane), mesuré en DORA (lead time, fréquence de déploiement). Étape 1 : Auditer la file de tickets : les 3 demandes les plus fréquentes = premiers golden paths."
date_ajout: "2026-11"
nom: "Construire une Internal Developer Platform (IDP) en"
emoji: "🏗️"
domaine: "Développement"
signal: "Concevoir une IDP (Internal Developer Platform) en 2027 : un portail développeur (Backstage CNCF, 3 400+ orgs, ou Port/Cortex) + des golden paths (templates de services préconfigurés) + de l'infrastructure self-service (Crossplane), le tout mesuré en métriques DORA. Utilise quand 10+ équipes dev demandent la même chose. N'utilise pas pour 2 équipes (overkill)."
mot_cle: "construire IDP internal developer platform 2027 Backstage golden paths DORA"
nom_court: "IDP"
branche: "D16"
synonymes: ["monter une plateforme interne développeurs (IDP) 2027", "Backstage CNCF portail développeur 3400 orgs", "golden paths : nouveau service en minutes pas en jours"]
cross_refs: [609, 82, 85]
tags: ["2027"]
depends_on: [609]
---

## 1700. 🏗️ Construire une Internal Developer Platform (IDP) en 2027

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir une IDP en 2027 : portail Backstage (CNCF, catalogue de services + templates Scaffolder) + golden paths (service neuf préconfiguré : repo, CI, k8s, observabilité) + self-service infra (Crossplane), mesuré en DORA (lead time, fréquence de déploiement).

**Quand l'utiliser (triggers)** :
- 10 équipes demandent chacune 'un nouveau service avec CI et k8s'
- Backstage vs Port vs Cortex choisir l'IDP 2027
- mesurer l'IDP : DORA (lead time 2-5 j à moins de 4 h)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform engineer. Tu poses l'IDP comme un produit interne : catalogue (Backstage), templates (Scaffolder), golden paths couvrant 80 % des cas, self-service (Crossplane pour BDD/queues), métriques DORA + NPS interne, équipe platform dédiée. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les demandes récurrentes des équipes (audit de la file tickets)
- L'infra existante (k8s 609, CI 1413, cloud)
- La taille de l'organisation (seuil ~10 équipes)

**Méthode** :
1. Auditer la file de tickets : les 3 demandes les plus fréquentes = premiers golden paths.
2. Backstage (CNCF, 3 400+ orgs, 1 200+ plugins) : catalogue de services (owners, dépendances, doc TechDocs), Scaffolder (templates).
3. Golden path 'nouveau microservice' : génère repo + CI + manifests k8s + claim Crossplane (Postgres managé) + observabilité (OTel) — déployé en minutes.
4. Self-service : Crossplane (claims k8s pour BDD/queues/buckets), politiques Kyverno/OPA en garde-fous.
5. Métriques : DORA (lead time, deploy frequency, MTTR, change failure rate) + % équipes sur golden path + NPS interne — revue trimestrielle.

**Sorties attendues** :
- L'IDP déployé (portail + 3 golden paths) avec DORA mesurés
- Le catalogue de services à jour (owners, doc)
- Le plan : couvrir 80 % des cas en golden paths

**Exemple de prompt** :
> « 10 équipes demandent 'un nouveau service avec CI/k8s/Postgres' chaque semaine : monte une IDP (Backstage + Scaffolder golden path + Crossplane), objectif lead time 2-5 j → sous 4 h mesuré en DORA. »

**Cas d'usage** : Orgs 10+ équipes dev. S'articule avec skills 609 (k8s), 82 (DevOps), 85 (IaC) et 1413 (CI).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

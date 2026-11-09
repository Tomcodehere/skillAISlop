---
num: 1817
resume: "Orchestrer plusieurs composants IaC sur plusieurs environnements avec Terraform Stacks (HCP, GA) : déploiements coordonnés, dépendances inter-composants (output -supérieur à input), plan/apply unifié. Étape 1 : Créer le Stack dans HCP : composants (source module + version) et déploiements (env + variables + provider config)."
lang: "fr"
date_ajout: "2026-11"
nom: "Terraform Stacks (HCP) : orchestration multi-environnements"
emoji: "🗂️"
domaine: "Développement"
signal: "Utiliser Terraform Stacks (GA, HCP Terraform uniquement) pour orchestrer plusieurs composants IaC déployés sur plusieurs environnements : un stack = composants (modules) + déploiements (envs) + plan/apply coordonnés avec dépendances entre composants (output d'un module = input d'un autre). Exclusivité HCP — pas d'équivalent natif OpenTofu. N'utilise pas hors HCP Terraform (licence/compte requis)."
mot_cle: "Terraform Stacks HCP Terraform composants déploiements orchestration multi-env GA exclusivité HCP"
nom_court: "TF Stacks"
branche: "D16"
synonymes: ["orchestrer 5 modules IaC sur 3 environnements avec Terraform Stacks (HCP)", "dépendance entre composants : output VPC = input cluster dans un Stack", "Stacks HCP uniquement : pas d'équivalent OpenTofu natif"]
cross_refs: [1811, 85, 1704]
tags: ["2027"]
depends_on: [1811]
---

## 1817. 🗂️ Terraform Stacks (HCP) : orchestration multi-environnements

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Orchestrer plusieurs composants IaC sur plusieurs environnements avec Terraform Stacks (HCP, GA) : déploiements coordonnés, dépendances inter-composants (output -> input), plan/apply unifié.

**Quand l'utiliser (triggers)** :
- 5 modules (réseau, BDD, k8s, IAM, app) à déployer dans l'ordre sur dev/staging/prod
- l'output du module VPC doit alimenter le module cluster
- un seul plan/apply pour tout le stack avec dépendances

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme IaC. Tu modélises le Stack (composants = modules, déploiements = envs avec variables), tu déclares les dépendances entre composants, et tu laisses HCP ordonnancer les plans dans le bon ordre. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Un compte HCP Terraform
- Les modules (registre privé 1816 ou public)
- Les variables par env

**Méthode** :
1. Créer le Stack dans HCP : composants (source module + version) et déploiements (env + variables + provider config).
2. Dépendances : l'output d'un composant alimente un autre (HCP résout l'ordre).
3. Plan : HCP calcule le plan global ordonné ; apply déploie composant par composant.
4. Rollback : redeploy d'une version antérieure d'un composant.

**Sorties attendues** :
- Le Stack déployé sur les 3 envs avec ordre respecté
- Les dépendances inter-composants résolues automatiquement
- Le plan global et l'historique des applies

**Exemple de prompt** :
> « Stack prod : composant vpc -> composant eks (prend vpc_id en input) -> composant app (prend cluster endpoint) — un apply HCP déploie dans l'ordre vpc, eks, app sur l'env prod. »

**Cas d'usage** : Grandes plateformes sur HCP. S'articule avec skills 1811, 85, 1704 (GitOps Argo).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

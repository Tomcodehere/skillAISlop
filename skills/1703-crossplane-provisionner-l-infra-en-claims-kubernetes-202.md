---
num: 1703
date_ajout: "2026-11"
nom: "Crossplane : provisionner l'infra en claims Kubernetes (2027)"
emoji: "⚙️"
domaine: "Développement"
signal: "Utiliser Crossplane en 2027 pour provisionner l'infra (BDD managée, buckets S3, queues, certificats) via des claims Kubernetes (CRD) : les devs déclarent 'je veux une Postgres 16 en prod' (un YAML), Crossplane la crée chez AWS/GCP/Azure et la gère (backups, rotation). Alternative : Terraform (85) en CLI. N'utilise pas sans IDP/golden path derrière (1700)."
mot_cle: "crossplane claims kubernetes provisionner infra BDD S3 queues CRD 2027 XRD CompositeResource"
nom_court: "Crossplane"
branche: "D16"
synonymes: ["je veux une Postgres managée : un claim YAML (Crossplane)", "Crossplane vs Terraform : l'infra en CRD k8s (GitOps)", "XRD/CompositeResource : composer les ressources (BDD + bucket + user)"]
cross_refs: [609, 85, 1700]
tags: ["2027"]
depends_on: [609]
---

## 1703. ⚙️ Crossplane : provisionner l'infra en claims Kubernetes (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Provisionner l'infra via Crossplane en 2027 : claims Kubernetes (CRD) — 'je veux une Postgres 16 prod' en YAML — Crossplane la crée chez le cloud provider, la gère (backups, rotation, upgrades), réconciliation continue (GitOps).

**Quand l'utiliser (triggers)** :
- créer une BDD managée = 15 tickets et 2 semaines, automatiser
- claim Crossplane : PostgreSQL 16 + backups quotidiens en 1 YAML
- XRD : composer BDD + bucket S3 + IAM user en 1 ressource composite

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform engineer infra. Tu installes Crossplane sur le cluster (609), les providers (AWS/GCP/Azure), tu définis les XRD (composite : BDD+bucket+secrets), les devs ne voient que les claims simples, et tu suis la réconciliation (tout drift est corrigé). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cluster k8s (609)
- Les providers cloud (AWS/GCP/Azure credentials)
- Les ressources à exposer (BDD, buckets, queues, certs)

**Méthode** :
1. Installer Crossplane (helm) + provider du cloud (ex. provider-aws), credentials via secret (Vault 1656).
2. Définir les XRD (CompositeResourceDefinition) : ex. 'Database' = RDS Postgres + secret de connexion + backup plan.
3. Exposer les claims simples aux devs (Claim = 'je veux une Database prod'), le Scaffolder Backstage (1702) les génère.
4. GitOps : les claims sont dans Git (ArgoCD/Flux), toute dérive (quelqu'un modifie la BDD à la main) est corrigée automatiquement.
5. Sécurité : pas de accès console cloud pour les devs, tout passe par claims audités (1476).

**Sorties attendues** :
- Crossplane déployé (providers + XRD + claims)
- Un claim 'Database prod' provisionné en minutes avec backups auto
- La réconciliation GitOps (drift corrigé) testée

**Exemple de prompt** :
> « Créer une Postgres managée prend 15 tickets/2 semaines : déploie Crossplane sur le cluster k8s (609), XRD 'Database' (RDS + secret + backups), les devs créent un claim YAML en 5 min, réconciliation GitOps auto. »

**Cas d'usage** : IDP self-service infra. S'articule avec skills 609 (k8s), 85 (IaC/Terraform), 1700 (IDP) et 1702 (Backstage).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

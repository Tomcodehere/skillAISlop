---
num: 1815
resume: "Exploiter les features CLI OpenTofu absentes du binaire Terraform : provider for_each (multi-région), early variable evaluation (backend dynamique), -exclude (plan ciblé), registre OCI (1.10, air-gapped). Étape 1 : provider for_each : provider 'aws' { for_each = var.regions ... } puis module avec providers map."
lang: "fr"
date_ajout: "2026-11"
nom: "OpenTofu : provider for_each, early variable evaluation, -exclude"
emoji: "🔁"
domaine: "Développement"
signal: "Utiliser les features CLI exclusives OpenTofu : provider for_each (1.9) pour instancier un provider par région/compte en boucle ; early variable evaluation (1.8) pour calculer le backend (S3 bucket dynamique selon l'env) ; tofu plan -exclude=module.x pour cibler ; registre de providers/modules en OCI (1.10) pour du air-gapped. N'existent pas dans le binaire Terraform open."
mot_cle: "OpenTofu provider for_each early variable evaluation -exclude flag registre OCI 1.10 1.8 1.9"
nom_court: "Tofu CLI+"
branche: "D16"
synonymes: ["instancier un provider AWS par région avec for_each (OpenTofu provider for_each)", "backend S3 dynamique selon l'env : early variable evaluation OpenTofu 1.8", "tofu plan -exclude=module.dev pour ne toucher qu'un module", "registre OCI privé pour providers/modules (air-gapped) OpenTofu 1.10"]
cross_refs: [1811, 85, 1816]
tags: ["2027"]
depends_on: [1811]
---

## 1815. 🔁 OpenTofu : provider for_each, early variable evaluation, -exclude

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Exploiter les features CLI OpenTofu absentes du binaire Terraform : provider for_each (multi-région), early variable evaluation (backend dynamique), -exclude (plan ciblé), registre OCI (1.10, air-gapped).

**Quand l'utiliser (triggers)** :
- 3 régions AWS : un provider par région sans dupliquer le code
- le bucket S3 du backend dépend de l'env (dev/prod) : early variable evaluation
- ne pas toucher au module prod dans ce plan : -exclude
- air-gapped : distribuer providers via registre OCI interne

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur IaC. Tu utilises for_each sur le bloc provider pour le multi-région, early variable evaluation pour le backend, -exclude pour les plans ciblés, et tu migres le registre vers OCI si air-gapped (1816). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- OpenTofu 1.9+
- Les régions/comptes
- Le besoin air-gapped ?

**Méthode** :
1. provider for_each : provider "aws" { for_each = var.regions ... } puis module avec providers map.
2. Early variable evaluation : variable utilisée dans backend { bucket = "state-${var.env}" } évaluée tôt.
3. tofu plan -exclude=module.prod -target... pour les changements ciblés.
4. Registre OCI : tofu login registry interne, publication providers/modules, consommation air-gapped.

**Sorties attendues** :
- Le multi-région en for_each fonctionnel
- Le backend dynamique par env
- Les plans ciblés (-exclude) et registre OCI si besoin

**Exemple de prompt** :
> « 3 régions (eu-west-1/3, us-east-1) : provider "aws" { for_each = toset(var.regions) alias = each.key } + module VPC avec providers = { aws = aws[each.key] } — un seul code, 3 providers. »

**Cas d'usage** : IaC multi-région avancé. S'articule avec skills 1811, 85, 1816.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

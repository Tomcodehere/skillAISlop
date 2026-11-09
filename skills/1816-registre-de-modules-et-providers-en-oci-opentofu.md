---
num: 1816
resume: "Héberger providers et modules IaC dans un registre OCI interne (Harbor/ECR/GAR) avec OpenTofu 1.10+ : air-gapped, versioning par tag, modules signés (cosign) — plus de dépendance au registre public. Étape 1 : Déployer Harbor (proxy cache public + projet interne skillaislop)."
date_ajout: "2026-11"
nom: "Registre de modules et providers en OCI (OpenTofu)"
emoji: "🏭"
domaine: "Développement"
signal: "Distribuer providers et modules Terraform/OpenTofu via un registre OCI (OpenTofu 1.10+) au lieu du registre public : miroir interne (Harbor, ECR, GAR) pour air-gapped/entreprise, versioning par tag, signature des modules (cosign 1822). tofu login + dev overrides. N'utilise pas le registre public pour des modules internes sensibles."
mot_cle: "registre OCI providers modules OpenTofu 1.10 Harbor ECR GAR air-gapped miroir interne signature cosign"
nom_court: "Registre OCI"
branche: "D16"
synonymes: ["publier mes modules terraform internes dans un registre OCI privé (Harbor/ECR)", "air-gapped : plus de registre public, miroir OCI interne OpenTofu 1.10", "signer les modules avec cosign avant publication (supply chain IaC)"]
cross_refs: [1815, 1811, 1821]
tags: ["2027"]
depends_on: [1815]
---

## 1816. 🏭 Registre de modules et providers en OCI (OpenTofu)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Héberger providers et modules IaC dans un registre OCI interne (Harbor/ECR/GAR) avec OpenTofu 1.10+ : air-gapped, versioning par tag, modules signés (cosign) — plus de dépendance au registre public.

**Quand l'utiliser (triggers)** :
- environnement air-gapped : comment distribuer les modules tofu ?
- miroir interne Harbor des providers officiels + nos modules signés
- tofu login vers le registre privé puis consommation

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme IaC. Tu configures le miroir OCI (Harbor avec proxy cache du registre public + namespace interne), tu publies les modules avec oras/tofu, tu signes avec cosign (1822), et tu configures tofu login + dev_overrides. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- OpenTofu 1.10+
- Le registre interne (Harbor/ECR/GAR)
- Les modules internes à publier

**Méthode** :
1. Déployer Harbor (proxy cache public + projet interne skillaislop).
2. Publier un module : tofu module publish ou oras push registry/internal/module:1.2.0.
3. Signer le module : cosign sign (1822), vérifier à la consommation.
4. tofu login registry.interne, puis source = "registry.interne/skillaislop/vpc/aws" version = "1.2.0".
5. En air-gapped : miroir complet des providers (aws, kubernetes...) taggés.

**Sorties attendues** :
- Le registre OCI interne opérationnel (miroir + modules signés)
- Les modules internes publiés et signés
- La config tofu login / source interne documentee

**Exemple de prompt** :
> « Module VPC interne v1.2.0 : publié sur Harbor registry.interne/skillaislop/vpc/aws:1.2.0, signé cosign — les équipes consomment source = registry.interne/... version 1.2.0, vérification de signature à l'init. »

**Cas d'usage** : IaC air-gapped/entreprise. S'articule avec skills 1815, 1811, 1821/1822 (supply chain).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

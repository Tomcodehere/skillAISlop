---
num: 1811
resume: "Décider entre OpenTofu (MPL 2.0, Linux Foundation, state encryption natif, 1.13) et Terraform (BSL 1.1, IBM, Stacks/Sentinel HCP) pour l'IaC : nouveau projet self-host = OpenTofu ; dépendance HCP = Terraform. Étape 1 : Lister les besoins : encryption du state (OpenTofu natif), ephemeral values (les deux), Stacks (HCP only), support contrat (IBM)."
date_ajout: "2026-11"
nom: "Choisir OpenTofu ou Terraform pour l'IaC"
emoji: "⚖️"
domaine: "Développement"
signal: "Choisir son outil IaC en 2027 : OpenTofu (fork MPL 2.0, gouvernance Linux Foundation/CNCF, 1.13 en sept., registre 3 900+ providers / 23 600+ modules, ~12 % d'adoption + 27 % qui évaluent) vs Terraform (BSL 1.1, IBM/HashiCorp, 1.17, exclusifs HCP : Stacks, Sentinel, support). Règle : nouveau projet self-host = OpenTofu (state encryption natif) ; dépendance HCP Stacks/Sentinel ou contrat IBM = Terraform. Même HCL, mêmes providers, state compatible."
mot_cle: "choisir OpenTofu ou Terraform IaC licence MPL 2.0 vs BSL 1.1 IBM gouvernance Linux Foundation 2027"
nom_court: "OpenTofu vs TF"
branche: "D16"
synonymes: ["opentofu ou terraform en 2027 : lequel choisir (licence MPL vs BSL IBM)", "terraform est passé BSL puis IBM : le fork opentofu vaut le coup", "mêmes providers mêmes HCL : opentofu 1.13 registre 3900 providers"]
cross_refs: [85, 1820, 1819]
tags: ["2027"]
depends_on: [85]
---

## 1811. ⚖️ Choisir OpenTofu ou Terraform pour l'IaC

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Décider entre OpenTofu (MPL 2.0, Linux Foundation, state encryption natif, 1.13) et Terraform (BSL 1.1, IBM, Stacks/Sentinel HCP) pour l'IaC : nouveau projet self-host = OpenTofu ; dépendance HCP = Terraform.

**Quand l'utiliser (triggers)** :
- on démarre un nouveau projet IaC en 2027 : tofu ou terraform ?
- notre DSI demande la licence : BSL vs MPL 2.0
- on a déjà HCP Terraform Stacks en prod

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte plateforme / DSI. Tu poses les 3 critères (licence/gouvernance, besoins HCP Stacks/Sentinel, fonctionnalités exclusives : state encryption côté OpenTofu), et tu documentes la décision dans un ADR. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les contraintes légales/licence
- L'existant HCP Terraform (Stacks, Sentinel)
- Les besoins features (state encryption, ephemeral)

**Méthode** :
1. Lister les besoins : encryption du state (OpenTofu natif), ephemeral values (les deux), Stacks (HCP only), support contrat (IBM).
2. Si nouveau projet sans HCP : OpenTofu (brew install opentofu, state compatible).
3. Si Stacks/Sentinel en prod : rester Terraform, évaluer la migration plus tard (1819).
4. ADR : décision + critères + date de revue.

**Sorties attendues** :
- La décision documentée (ADR) : OpenTofu ou Terraform
- Le critère de choix clair (HCP ? licence ? encryption ?)
- Le plan si migration (1819)

**Exemple de prompt** :
> « Nouveau projet greenfield sans HCP : OpenTofu 1.13 choisi (MPL 2.0, state encryption natif 1812) — ADR enregistré, revue à 12 mois. »

**Cas d'usage** : Standardiser l'IaC. S'articule avec skills 85 (IaC), 1819 (migration), 1820 (drift/policy).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

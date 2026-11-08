---
num: 1818
date_ajout: "2026-11"
nom: "Terraform query/list : découvrir les ressources hors du state (drift)"
emoji: "🔎"
domaine: "Développement"
signal: "Utiliser terraform query / list (Terraform 1.14+) pour demander au provider les ressources EXISTANTES hors du state (import automatique, détection de drift manuel) : ex. lister toutes les S3 buckets du compte, puis terraform query pour importer celles non gérées. Différent de l'import manuel un par un. Exclusif Terraform 1.14+ (pas dans OpenTofu à date)."
mot_cle: "terraform query list ressources hors state import automatique drift détection provider 1.14"
nom_court: "terraform query"
branche: "D16"
synonymes: ["lister toutes les S3 buckets du compte et importer celles hors state (terraform query)", "détecter le drift manuel : ressources créées en console non dans le state", "terraform list vs state : voir ce qui existe vraiment chez le cloud"]
cross_refs: [1811, 1820, 85]
tags: ["2027"]
depends_on: [1811]
---

## 1818. 🔎 Terraform query/list : découvrir les ressources hors du state (drift)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser terraform query/list (Terraform 1.14+) pour découvrir les ressources existantes chez le provider mais absentes du state, et les importer en masse (détection de drift manuel / ressources créées en console).

**Quand l'utiliser (triggers)** :
- quelqu'un a créé une S3 bucket en console, elle n'est pas dans le state
- importer 30 buckets existants d'un coup
- voir le drift : comparer state et réalité cloud

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur IaC / cloud. Tu lances terraform list pour voir les ressources réelles, terraform query pour les filtrer (CEL), puis tu génères les blocs import et tu appliques — le state rejoint la réalité. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Terraform 1.14+
- Le provider avec support query/list
- Les ressources à auditer

**Méthode** :
1. terraform list aws_s3_bucket (avec provider config du compte) : liste les buckets réels.
2. terraform query avec filtre (ex. tags) pour ne garder que les nôtres.
3. Générer les blocs import { } et tofu/terraform import ou apply avec generated config.
4. Vérifier : le state couvre maintenant 100 % des ressources auditées.
5. Planifier un audit récurrent (CI hebdo 1413) pour détecter le drift futur (1820).

**Sorties attendues** :
- La liste des ressources réelles vs state
- Les blocs import générés et appliqués
- Le rapport de drift (ressources orphelines)

**Exemple de prompt** :
> « Audit compte AWS prod : terraform list aws_s3_bucket trouve 34 buckets, le state en gère 30 — terraform query filtre les 4 orphelins (créés en console), blocs import générés, state à jour, alerte drift envoyée. »

**Cas d'usage** : Gouvernance cloud. S'articule avec skills 1811, 1820 (drift/policy), 85.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

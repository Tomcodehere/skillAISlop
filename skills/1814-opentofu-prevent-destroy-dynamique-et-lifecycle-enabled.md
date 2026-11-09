---
num: 1814
resume: "Protéger les ressources critiques (BDD prod, buckets) avec prevent_destroy dynamique (variable par workspace : true en prod, false en dev, OpenTofu 1.12) et lifecycle enabled pour les ressources zero-or-one (1.11). Étape 1 : Variable protect : true dans le workspace prod, false en dev."
date_ajout: "2026-11"
nom: "OpenTofu : prevent_destroy dynamique et lifecycle enabled"
emoji: "🛡️"
domaine: "Développement"
signal: "Protéger les ressources critiques avec prevent_destroy piloté par une VARIABLE (OpenTofu 1.12+, mai) : en prod la variable prevent_destroy=true bloque tout destroy, en dev false. Et lifecycle enabled (1.11) pour des ressources zero-or-one. Avant : prevent_destroy était hardcodé par module. N'utilise pas prevent_destroy=true en dev (bloque les itérations)."
mot_cle: "OpenTofu prevent_destroy dynamique variable lifecycle enabled 1.12 1.11 protéger ressource critique destroy"
nom_court: "prevent_destroy"
branche: "D16"
synonymes: ["empecher le destroy d'une ressource prod via une variable (prevent_destroy dynamique OpenTofu 1.12)", "lifecycle enabled pour ressource zero-or-one (OpenTofu 1.11)", "prevent_destroy hardcodé vs variable par workspace (prod vs dev)"]
cross_refs: [1811, 85, 1819]
tags: ["2027"]
depends_on: [1811]
---

## 1814. 🛡️ OpenTofu : prevent_destroy dynamique et lifecycle enabled

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Protéger les ressources critiques (BDD prod, buckets) avec prevent_destroy dynamique (variable par workspace : true en prod, false en dev, OpenTofu 1.12) et lifecycle enabled pour les ressources zero-or-one (1.11).

**Quand l'utiliser (triggers)** :
- un tofu destroy en dev a failli supprimer la BDD prod partagée
- prevent_destroy=true en dur bloque le dev : le rendre variable
- ressource optionnelle zero-or-one : lifecycle enabled

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme IaC. Tu remplaces prevent_destroy=true en dur par prevent_destroy = var.protect (variable workspace : prod=true, dev=false), et tu utilises lifecycle { enabled = var.x } pour les ressources conditionnelles. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- OpenTofu 1.12+
- Les variables par workspace (prod/dev)
- Les ressources à protéger

**Méthode** :
1. Variable protect : true dans le workspace prod, false en dev.
2. Resource critique (BDD, bucket S3) : lifecycle { prevent_destroy = var.protect }.
3. Tester : en dev tofu destroy passe, en prod bloqué avec message clair.
4. enabled = var.x pour les ressources zero-or-one (ex. DNS record optionnel).

**Sorties attendues** :
- Les ressources prod protégées (prevent_destroy variable)
- Le test : destroy bloqué en prod, OK en dev
- La liste des ressources zero-or-one (enabled)

**Exemple de prompt** :
> « BDD RDS prod : lifecycle { prevent_destroy = var.protect } — workspace prod (protect=true) : tofu destroy échoue proprement ; workspace dev (false) : destroy autorisé pour les tests. »

**Cas d'usage** : Sécuriser l'IaC. S'articule avec skills 1811, 85 (IaC), 1819 (migration).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

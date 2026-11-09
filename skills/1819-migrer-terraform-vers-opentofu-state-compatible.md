---
num: 1819
resume: "Migrer un repo Terraform vers OpenTofu : installer tofu, tofu init (state compatible réutilisé), tofu plan doit montrer 0 changement, puis remplacer terraform par tofu en CI — sans activer le chiffrement en même temps. Étape 1 : brew install opentofu (ou image CI), vérifier tofu version."
date_ajout: "2026-11"
nom: "Migrer Terraform vers OpenTofu (state compatible)"
emoji: "🔄"
domaine: "Développement"
signal: "Migrer un repo Terraform vers OpenTofu en 2027 : le state est compatible tel quel (même format) — brew install opentofu, tofu init (réutilise le state existant), tofu plan pour vérifier 0 changement, puis remplacer terraform par tofu dans la CI. Pièges : ne PAS activer la state encryption (1812) pendant la migration (2 changements risqués à la fois), vérifier required_version (OpenTofu compare différemment), et un module avec bloc OpenTofu-only ne tournera pas sous Terraform."
mot_cle: "migrer terraform vers opentofu state compatible tofu init plan zéro changement CI required_version pièges"
nom_court: "Migration tofu"
branche: "D16"
synonymes: ["migrer un repo terraform vers opentofu : le state est compatible (tofu init)", "terraform plan vs tofu plan : vérifier 0 diff après migration", "ne pas activer state encryption pendant la migration (1812 après)"]
cross_refs: [1811, 1812, 1813]
tags: ["2027"]
depends_on: [1811]
---

## 1819. 🔄 Migrer Terraform vers OpenTofu (state compatible)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Migrer un repo Terraform vers OpenTofu : installer tofu, tofu init (state compatible réutilisé), tofu plan doit montrer 0 changement, puis remplacer terraform par tofu en CI — sans activer le chiffrement en même temps.

**Quand l'utiliser (triggers)** :
- on veut quitter le BSL sans casser le state
- tofu plan après migration montre des diffs : pourquoi (required_version, providers)
- remplacer terraform par tofu dans la CI (GitHub Actions)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur DevOps. Tu suis l'ordre sûr : install tofu -> tofu init (state réutilisé) -> tofu plan (0 diff attendu) -> maj CI (tofu) -> puis SEULEMENT après, activer state encryption (1812) et ephemeral (1813). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo Terraform existant + son state
- OpenTofu installé
- La CI à mettre à jour

**Méthode** :
1. brew install opentofu (ou image CI), vérifier tofu version.
2. tofu init : le state existant est lu tel quel (compatible), providers téléchargés.
3. tofu plan : doit être vide (0 changement). Si diff : required_version, versions providers, ou blocs spécifiques — corriger.
4. Remplacer terraform par tofu dans .github/workflows et les Makefile.
5. Ensuite seulement : activer state encryption (1812) sur un workspace de test d'abord.

**Sorties attendues** :
- Le repo migré (tofu dans la CI) avec 0 diff au plan
- Le state réutilisé sans perte
- Le chiffrement activé après, séparément (1812)

**Exemple de prompt** :
> « Repo terraform prod (state S3, 200 ressources) : tofu init lit le state, tofu plan = 0 to change, CI passe en tofu, puis state encryption activé la semaine suivante sur un env de test. »

**Cas d'usage** : Sortir du BSL en sécurité. S'articule avec skills 1811, 1812, 1813, 1820.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

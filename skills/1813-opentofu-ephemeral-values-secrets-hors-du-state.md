---
num: 1813
resume: "Utiliser les ephemeral values d'OpenTofu (1.11+) pour que les secrets (ex. mot de passe BDD lu dans Secrets Manager) traversent le provider sans jamais être écrits dans le state ni les logs. Étape 1 : Déclarer ephemeral 'aws_secretsmanager_secret_version' 'db' { ... } — la valeur est éphémère."
lang: "fr"
date_ajout: "2026-11"
nom: "OpenTofu : ephemeral values (secrets hors du state)"
emoji: "🕶️"
domaine: "Sécurité"
signal: "Garder les secrets HORS du state avec les ephemeral values d'OpenTofu (1.11+, déc.) : ressources éphémères (ephemeral 'aws_secretsmanager_secret_version') et attributs write-only — la valeur traverse le provider mais n'est JAMAIS écrite dans le state ni les logs. Complète la state encryption (1812) : defense en profondeur. N'utilise pas pour des valeurs qui doivent persister entre les runs (elles sont re-lues à chaque apply)."
mot_cle: "OpenTofu ephemeral values ressources éphémères write-only secrets hors du state 1.11"
nom_court: "Ephemeral values"
branche: "D23"
synonymes: ["garder le mot de passe BDD hors du terraform state (ephemeral resource)", "ephemeral aws_secretsmanager_secret_version : la valeur n'est jamais dans le state", "write-only attributes OpenTofu 1.11 : pas de fuite dans les logs"]
cross_refs: [1812, 1851, 1853]
tags: ["2027"]
depends_on: [1812]
---

## 1813. 🕶️ OpenTofu : ephemeral values (secrets hors du state)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser les ephemeral values d'OpenTofu (1.11+) pour que les secrets (ex. mot de passe BDD lu dans Secrets Manager) traversent le provider sans jamais être écrits dans le state ni les logs.

**Quand l'utiliser (triggers)** :
- mon state contient encore un mot de passe en clair malgré le chiffrement
- ephemeral resource pour lire un secret sans le stocker
- write-only attribute : la valeur n'apparaît pas dans tofu plan

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité IaC. Tu remplaces les data sources de secrets par des ephemeral resources, tu vérifies avec tofu plan que la valeur n'apparaît ni dans le state ni dans les logs (-no-color), et tu documentes le contrat : re-lu à chaque apply. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- OpenTofu 1.11+
- Le provider avec support ephemeral (AWS, Vault...)
- Les secrets à protéger

**Méthode** :
1. Déclarer ephemeral "aws_secretsmanager_secret_version" "db" { ... } — la valeur est éphémère.
2. L'utiliser dans une resource (ex. création user BDD) : la valeur passe au provider, n'est pas dans le state.
3. Vérifier : tofu plan ne montre pas la valeur, le state non plus (tofu state show), logs propres.
4. Contrat : la valeur est re-lue à chaque apply (pas de persistance) — documenter.

**Sorties attendues** :
- Les secrets éphémères (hors state) en production
- La preuve : tofu plan/state/logs sans la valeur
- Le contrat ephemeral documente

**Exemple de prompt** :
> « Création d'un user BDD : ephemeral aws_secretsmanager_secret_version lit le password, le passe à la resource postgresql_grant — tofu state show ne contient pas le password, plan non plus. »

**Cas d'usage** : Defense en profondeur avec 1812. S'articule avec skills 1812, 1851, 1853 (dynamic secrets), 1860.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

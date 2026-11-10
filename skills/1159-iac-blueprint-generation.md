---
num: 1159
resume: "Générer des squelettes d'Infrastructure as Code (Terraform, Bicep, CloudFormation) alignés sur une architecture validée, paramétrables et documentés. Étape 1 : Traduire l'architecture cible en modules IaC."
lang: "fr"
date_ajout: "2026-11"
nom: "IaC Blueprint Generation"
emoji: "💻"
domaine: "Développement"
signal: "Générer des squelettes d'Infrastructure as Code (Terraform, Bicep, CloudFormation) alignés sur une architecture validée, paramétrables et documentés."
mot_cle: "iac-blueprint-generation"
nom_court: "IaC Blueprint Generation"
branche: "D1"
synonymes: ["genere", "terraform", "template"]
cross_refs: [313, 1160, 85]
tags: ["2027"]
depends_on: [1160]
---

## 1159. 💻 IaC Blueprint Generation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Générer des squelettes d'Infrastructure as Code (Terraform, Bicep, CloudFormation) alignés sur une architecture validée, paramétrables et documentés.

**Quand l'utiliser (triggers)** :
- « génère le Terraform/IaC », « template d'infra », « provisionne ».
- Industrialisation d'une architecture cible déjà validée.
- Standardisation de modules réutilisables.

**Hors périmètre** :
- Conception de l'architecture cible → skill Cloud Architecture Design.
- Exécution/déploiement en production → l'agent de coordination (exécution directe, sous supervision).
- Pipelines CI/CD applicatifs → l'agent d'intégration et d'automatisation.

**Garde-fous** :
- Jamais de secret en dur.
- Versions de providers/modules épinglées, stables et supportées (pas d'EOL).
- Valeurs par défaut sécurisées (moindre privilège, chiffrement activé).

**Instructions système** :
Tu es assistant spécialisé « IaC Blueprint Generation ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Architecture cible validée.
- Provider et région(s).
- Conventions de nommage et de tagging.
- Contraintes de sécurité (chiffrement, réseau, IAM).

**Méthode** :
1. Traduire l'architecture cible en modules IaC.
2. Externaliser les paramètres variables et secrets.
3. Ajouter tags, chiffrement et contrôles réseau par défaut.
4. Documenter l'usage et l'ordre d'application.

**Sorties attendues** :
- Fichiers IaC commentés et modulaires.
- Variables paramétrables et valeurs par défaut sûres.
- README d'usage (prérequis, commandes, ordre d'application).
- Aucun secret en dur (variables d'environnement / gestionnaire de secrets).

**Exemple de prompt** :
### Exemple 1 : [Titre du cas d'usage]
**Contexte** : [Description de la situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Résultat obtenu]

**Cas d'usage** : complément : skill 313. genere ; terraform ; template

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1808
date_ajout: "2026-11"
nom: "MutatingAdmissionPolicy : admission déclarative en CEL"
emoji: "✅"
domaine: "Sécurité"
signal: "Déployer des règles d'admission côté API server SANS webhook externe grâce à MutatingAdmissionPolicy (GA k8s 1.36) : expressions CEL qui modifient/valident les objets à la création (ex. forcer un label team, injecter un sidecar, bloquer une image non signée). Contrairement aux webhooks mutating (service à héberger), c'est natif dans l'apiserver. N'utilise pas pour de la logique métier complexe (limite CEL) — compléter avec Kyverno (1705) pour les policies complexes."
mot_cle: "MutatingAdmissionPolicy CEL admission déclarative apiserver GA k8s 1.36 sans webhook labels sidecar"
nom_court: "MutatingAdmission"
branche: "D23"
synonymes: ["forcer un label team= sur chaque pod à la création (MutatingAdmissionPolicy CEL)", "bloquer les images non signées à l'admission sans webhook", "admission déclarative CEL dans l'apiserver vs webhook mutating externe"]
cross_refs: [1705, 1821, 1822]
tags: ["2027"]
depends_on: [609]
---

## 1808. ✅ MutatingAdmissionPolicy : admission déclarative en CEL

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place des MutatingAdmissionPolicy (CEL, GA 1.36) natives dans l'apiserver pour modifier/valider les objets à l'admission (labels obligatoires, sidecar injecté, images non signées bloquées) sans webhook externe.

**Quand l'utiliser (triggers)** :
- chaque pod doit avoir le label team= : forcer à l'admission
- injecter automatiquement un sidecar logging
- bloquer my-registry non signé à la création du pod

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme / sécurité. Tu écris les MutatingAdmissionPolicy en CEL (matchConstraints sur les ressources), tu testes en dry-run d'abord, et tu réserves Kyverno (1705) aux policies complexes hors portée CEL. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- k8s 1.36+
- Les règles CEL à appliquer
- Le scope (namespaces concernés)

**Méthode** :
1. Rédiger la policy CEL : matchConstraints (apiGroups/kinds), expressions (ex. object.metadata.labels.team = 'x' ou ajout de label).
2. Déployer avec failurePolicy=Fail et dry-run d'abord sur un namespace test.
3. Vérifier : un pod sans label team est modifié à la volée (label ajouté) ou rejeté selon la règle.
4. Monitorer : métriques apiserver admission, logs des rejets.

**Sorties attendues** :
- Les MutatingAdmissionPolicy déployées (CEL)
- Les tests : label injecté / image non signée bloquée
- La doc des limites CEL (policies complexes -> Kyverno 1705)

**Exemple de prompt** :
> « Policy CEL : tout pod créé dans ns=prod doit avoir metadata.labels.team — à la création d'un pod sans le label, l'apiserver l'ajoute automatiquement (mutation), sinon rejet avec message clair. »

**Cas d'usage** : Gouvernance à l'admission sans webhook. S'articule avec skills 1705 (Kyverno), 1821/1822 (signature), 609.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1705
resume: "Écrire des policies as code en 2027 sur k8s avec Kyverno (YAML, simple) ou OPA/Gatekeeper (Rego, puissant) : imposer resource limits, readOnlyRootFilesystem, images signées (1457), interdire les privilèges — en mode warn d'abord, puis enforce, avec audit des violations. Étape 1 : Choisir : Kyverno (YAML natif, facile, bon pour 90 % des cas) ou OPA/Gatekeeper (Rego, pour logique complexe)."
date_ajout: "2026-11"
nom: "Kyverno / OPA : policies as code sur Kubernetes"
emoji: "🛡"
domaine: "Sécurité"
signal: "Appliquer des policies as code en 2027 sur Kubernetes avec Kyverno (YAML simple, natif k8s) ou OPA/Gatekeeper (Rego, plus puissant) : bloquer les pods sans resource limits, sans readOnlyRootFilesystem, images non signées (1457), namespaces interdits, quotas. Audit + enforce (bloquer) vs warn. Utilise en complément du GitOps (1704). N'utilise pas pour les politiques hors k8s."
mot_cle: "kyverno OPA gatekeeper policies as code kubernetes 2027 resource limits readOnlyRootFilesystem images signées"
nom_court: "Policies k8s"
branche: "D23"
synonymes: ["bloquer un pod sans resource limits (Kyverno) en admission", "Kyverno (YAML) vs OPA/Gatekeeper (Rego) choisir 2027", "policy enforce (bloque) vs warn (log) + audit des violations existantes"]
cross_refs: [609, 508, 1645]
tags: ["2027"]
depends_on: [609]
---

## 1705. 🛡 Kyverno / OPA : policies as code sur Kubernetes (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Écrire des policies as code en 2027 sur k8s avec Kyverno (YAML, simple) ou OPA/Gatekeeper (Rego, puissant) : imposer resource limits, readOnlyRootFilesystem, images signées (1457), interdire les privilèges — en mode warn d'abord, puis enforce, avec audit des violations.

**Quand l'utiliser (triggers)** :
- un pod déployé sans resource limits a fait exploser le nœud
- Kyverno : ClusterPolicy 'exige limits + readOnlyRootFilesystem'
- warn d'abord (1 mois d'audit), puis enforce (bloque à l'admission)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es platform security engineer. Tu installes Kyverno (plus simple, YAML) ou OPA Gatekeeper (Rego), tu écris les policies (validate: limits présents, image signée cosign, pas de privileged, pas de latest tag), tu démarres en warn/audit, puis enforce. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cluster k8s (609)
- Les règles de sécurité à imposer
- Le mode (warn → enforce)

**Méthode** :
1. Choisir : Kyverno (YAML natif, facile, bon pour 90 % des cas) ou OPA/Gatekeeper (Rego, pour logique complexe).
2. Écrire les ClusterPolicies : (1) resource limits obligatoires, (2) readOnlyRootFilesystem + runAsNonRoot, (3) image signée (cosign verify 1457) + pas de tag latest, (4) pas de privileged/hostPath, (5) NetworkPolicy par défaut (deny all).
3. Mode warn/audit 1 mois : lister les violations sans bloquer (rapport 1417).
4. Puis enforce : les pods non conformes sont bloqués à l'admission (erreur claire pour le dev).
5. Exemptions : namespace kube-system, procédure d'exemption documentée (label + approbation 1636).

**Sorties attendues** :
- Les ClusterPolicies (Kyverno/OPA) déployées en warn puis enforce
- Le rapport d'audit des violations + taux de conformité (objectif 100 %)
- La procédure d'exemption documentée

**Exemple de prompt** :
> « Un pod sans limits a fait planter un nœud prod : déploie Kyverno sur le cluster, ClusterPolicy 'limits + readOnlyRoot + image signée + pas de latest', warn 1 mois (rapport violations), puis enforce (bloqué à l'admission). »

**Cas d'usage** : Sécurité k8s en continu. S'articule avec skills 609 (k8s), 508 (CI sécurisée), 1645 (supply chain) et 1417 (alertes).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1829
resume: "Sécuriser la chaîne de build : OIDC workload identity au lieu des secrets longue durée, Tekton Chains pour signer automatiquement les builds (SLSA), actions CI pinnées par SHA (leçon CVE-2026-33634 Trivy). Étape 1 : OIDC : GitHub -supérieur à AWS : créer le rôle IAM avec trust policy oidc provider token.actions.githubusercontent.com, puis aws-actions/configure-aws-credentials (pas de clé)."
date_ajout: "2026-11"
nom: "Build integrity en CI : OIDC, Tekton Chains, pas de secrets longue durée"
emoji: "🔒"
domaine: "Sécurité"
signal: "Sécuriser la chaîne de build elle-même : plus de secrets longue durée dans la CI — OIDC workload identity (GitHub Actions — AWS/GCP/Azure, token 1 h) ; Tekton Chains signe automatiquement les images produites (provenance SLSA 1823) depuis le cluster de build ; builds reproductibles (pinnés par digest). Incident de référence : compromission Trivy (CVE-2026-33634, 76 tags hijackés, fuite de secrets Runner.Worker) = pin par SHA."
mot_cle: "build integrity CI OIDC workload identity GitHub Actions AWS GCP token 1h Tekton Chains SLSA pas de secrets longue durée pin SHA CVE-2026-33634 Trivy"
nom_court: "Build integrity"
branche: "D23"
synonymes: ["plus de clé AWS statique dans les secrets GitHub : OIDC workload identity (token 1h)", "Tekton Chains signe automatiquement les images du build (provenance SLSA)", "incident Trivy CVE-2026-33634 : pinner les actions GitHub par SHA, pas par tag"]
cross_refs: [1413, 1822, 1823]
tags: ["2027"]
depends_on: [1413]
---

## 1829. 🔒 Build integrity en CI : OIDC, Tekton Chains, pas de secrets longue durée

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser la chaîne de build : OIDC workload identity au lieu des secrets longue durée, Tekton Chains pour signer automatiquement les builds (SLSA), actions CI pinnées par SHA (leçon CVE-2026-33634 Trivy).

**Quand l'utiliser (triggers)** :
- notre CI a une clé AWS statique dans les secrets : migrer vers OIDC
- Tekton Chains sur le cluster de build : images signées automatiquement
- une action GitHub taggée a été compromis : passer en pin SHA

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité DevSecOps / plateforme. Tu remplaces les secrets cloud statiques par l'OIDC (role IAM trust policy sur le repo), tu déploies Tekton Chains pour la signature auto des builds, et tu pins toutes les actions par SHA avec dependabot (1884). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le CI (GitHub Actions ou Tekton)
- Les rôles IAM configurables
- Tekton Chains (si build sur k8s)

**Méthode** :
1. OIDC : GitHub -> AWS : créer le rôle IAM avec trust policy oidc provider token.actions.githubusercontent.com, puis aws-actions/configure-aws-credentials (pas de clé).
2. Tekton Chains : installé sur le cluster de build, signe chaque image produite (cosign keyless 1822) + provenance SLSA (1823).
3. Pin SHA : toutes les uses: pinnées par commit SHA (dependabot pins-actions 1884).
4. Audit : plus aucun secret longue durée dans les settings CI.

**Sorties attendues** :
- L'OIDC en place (0 secret cloud statique)
- Les builds signés automatiquement (Tekton Chains)
- Toutes les actions pinnées par SHA

**Exemple de prompt** :
> « CI release : plus de AWS_SECRET_ACCESS_KEY dans les secrets — configure-aws-credentials en OIDC (rôle assumé 1 h) ; Tekton Chains signe l'image produite (SLSA) ; actions pinnées SHA après l'incident Trivy. »

**Cas d'usage** : Sécuriser la supply chain CI. S'articule avec skills 1413, 1822, 1823, 1860, 1827.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

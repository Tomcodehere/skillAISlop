---
num: 1860
date_ajout: "2026-11"
nom: "OIDC workload identity en CI : plus de clés cloud statiques"
emoji: "🎫"
domaine: "Sécurité"
signal: "Supprimer les clés cloud statiques des secrets CI avec l'OIDC workload identity : GitHub Actions (permissions id-token: write) obtient un JWT signé, échangé contre un token cloud temporaire (1 h) via un rôle IAM en trust policy (sub = repo:org/repo, branche). Idem GitLab, Azure (federated credentials), GCP (workload identity federation). Avantage : 0 secret à fuir/révoquer/rotater. Leçon incident Trivy (CVE-2026-33634) : fuite de secrets Runner.Worker via tag compromis (1829)."
mot_cle: "OIDC workload identity CI GitHub Actions id-token JWT rôle IAM trust policy token temporaire 1h GitLab Azure federated GCP workload identity federation pas de clé statique"
nom_court: "OIDC CI"
branche: "D23"
synonymes: ["plus de AWS_SECRET_ACCESS_KEY dans les secrets GitHub : OIDC (id-token write + rôle IAM trust)", "token cloud temporaire 1 h au lieu d'une clé statique : OIDC workload identity", "incident Trivy (tags compromis, fuite Runner.Worker) : OIDC + pin SHA (1829)"]
cross_refs: [1413, 1829, 1822]
tags: ["2027"]
depends_on: [1413]
---

## 1860. 🎫 OIDC workload identity en CI : plus de clés cloud statiques

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Remplacer les clés cloud statiques des secrets CI par l'OIDC workload identity (GitHub/GitLab/Azure/GCP) : JWT du job -> rôle IAM en trust policy (repo/branche) -> token temporaire 1 h.

**Quand l'utiliser (triggers)** :
- on a AWS_SECRET_ACCESS_KEY dans les secrets GitHub : migrer vers OIDC
- trust policy IAM : sub = repo:monorg/monrepo + branche main uniquement
- Azure : federated credentials, GCP : workload identity federation

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es SRE DevOps / sécurité. Tu crées le rôle IAM avec la trust policy OIDC (audience sts.amazonaws.com, sub = repo + branche), et dans le workflow : permissions id-token write + configure-aws-credentials (pas de clé). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo CI (GitHub/GitLab/Azure/GCP)
- Le provider cloud avec support OIDC
- Les rôles IAM à créer

**Méthode** :
1. AWS : créer le provider OIDC token.actions.githubusercontent.com (aud sts.amazonaws.com), puis le rôle avec trust policy condition StringEquals sub = repo:org/repo:ref:refs/heads/main (+ audience).
2. Workflow : permissions: id-token: write + uses aws-actions/configure-aws-credentials@v4 (role-to-assume, pas de clé) -> credentials temporaires 1 h.
3. Vérifier : aws sts get-caller-identity montre le rôle assumé, pas de clé longue durée ; retirer les vieux secrets du repo (1859 scan).
4. Autres clouds : Azure federated credential, GCP workload identity federation (même principe).

**Sorties attendues** :
- L'OIDC en place (0 clé statique dans les secrets CI)
- Le token temporaire 1 h vérifié (sts get-caller-identity)
- Les vieux secrets supprimés + scan 1859 clean

**Exemple de prompt** :
> « Workflow deploy-prod : avant = AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY dans les secrets (fuite = compromission totale) ; après = id-token: write + configure-aws-credentials role-to-assume -> token 1 h ; même si le workflow fuit, aucun secret valide. »

**Cas d'usage** : CI sans secret. S'articule avec skills 1413, 1829, 1822, 1852, 1859.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

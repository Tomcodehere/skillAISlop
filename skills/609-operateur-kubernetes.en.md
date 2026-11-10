---
num: 609
resume: "Operate Kubernetes day to day."
lang: "en"
date_ajout: "2026-11"
nom: "Kubernetes operator"
emoji: "☸️"
domaine: "Développement"
signal: "Kubernetes, manifests, pods, autoscaling, deploy probes"
mot_cle: "kubernetes"
nom_court: ""
branche: "D16"
synonymes: []
cross_refs: [85, 314, 82]
---
## 609. ☸️ Kubernetes operator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Write and operate K8s manifests safely.

**Quand l'utiliser (triggers)** :
- any request about: kubernetes, manifests, pods, autoscaling, deploy probes

**Hors périmètre** :
- (not covered — see cross-refs)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a specialist in this exact task. You stay factual, structured and within scope.

**Inputs requis** :
- the user's need in natural language

**Méthode** :
1. Deployment + Service + Ingress + ConfigMap/Secret.
2. Probes (liveness/readiness), HPA.
3. Rollout + rollback runbook.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « K8s manifests for our API with autoscaling. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

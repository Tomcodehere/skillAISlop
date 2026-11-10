---
num: 1824
resume: "Bloquer à l'admission Kubernetes (Kyverno 1.13 verifyImages ou Sigstore Policy Controller) toute image non signée ou sans provenance SLSA du bon repo — après une phase Audit. Étape 1 : Choisir : Kyverno (policies riches) ou Sigstore Policy Controller (léger, greenfield)."
lang: "fr"
date_ajout: "2026-11"
nom: "Admission control supply chain : bloquer les images non vérifiées"
emoji: "⛔"
domaine: "Sécurité"
signal: "Bloquer au déploiement (admission k8s) toute image non signée ou sans provenance valide : Kyverno 1.13+ avec verifyImages (failureAction block, cosign keyless + SLSA provenance + issuer OIDC attendu) OU Sigstore Policy Controller (plus léger, greenfield). La policy vérifie signature Rekor + attestation SLSA (1823) du bon repo. N'utilise pas verifyImages sans tester d'abord en audit mode (failureAction Audit) pour éviter de bloquer la prod."
mot_cle: "Kyverno 1.13 verifyImages admission bloquer image non signée Sigstore Policy Controller failureAction block audit cosign SLSA OIDC issuer"
nom_court: "Admission images"
branche: "D23"
synonymes: ["bloquer les pods avec image non signée à l'admission (Kyverno verifyImages cosign)", "Sigstore Policy Controller vs Kyverno : lequel pour vérifier les signatures", "failureAction Audit d'abord, Block ensuite (ne pas casser la prod)"]
cross_refs: [1705, 1822, 1823]
tags: ["2027"]
depends_on: [1822]
---

## 1824. ⛔ Admission control supply chain : bloquer les images non vérifiées

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Bloquer à l'admission Kubernetes (Kyverno 1.13 verifyImages ou Sigstore Policy Controller) toute image non signée ou sans provenance SLSA du bon repo — après une phase Audit.

**Quand l'utiliser (triggers)** :
- une image non signée a été déployée en prod
- Kyverno verifyImages : vérifier signature cosign keyless + provenance SLSA + issuer
- commencer en Audit (failureAction=Audit) avant Block

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité plateforme. Tu déploies la ClusterPolicy verifyImages (cosign keyless, attestation SLSA 1823, certificate-identity du repo), d'abord en Audit (alertes 1761), puis Block quand le taux de conformité est à 100 %. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Kyverno 1.13+ ou Sigstore Policy Controller
- Les images signées (1822) + provenance (1823)
- Le namespace/prod cible

**Méthode** :
1. Choisir : Kyverno (policies riches) ou Sigstore Policy Controller (léger, greenfield).
2. Policy : pour chaque container, cosign verify (signature Rekor + issuer GitHub du repo) + verify-attestation SLSA provenance.
3. failureAction=Audit d'abord : monitorer les violations (métriques, alertes).
4. Passer à Block quand 100 % des images sont conformes ; garder une exception break-glass (image debug signée séparément).

**Sorties attendues** :
- La policy d'admission déployée (Audit puis Block)
- Le taux de conformité 100 % avant Block
- L'exception break-glass documentee

**Exemple de prompt** :
> « Policy Kyverno sur ns=prod : tout pod doit avoir une image signée par le workflow release du repo org/app (OIDC) avec attestation SLSA — Audit 2 semaines (3 violations nettoyées), puis Block : 0 image non signée déployée. »

**Cas d'usage** : Supply chain k8s. S'articule avec skills 1705, 1822, 1823, 1808, 609.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

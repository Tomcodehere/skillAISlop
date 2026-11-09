---
num: 1823
resume: "Attacher une provenance SLSA (attestation in-toto signée, slsa-github-generator keyless = SLSA L3) à chaque build : source, commit, builder, paramètres — vérifiable avec cosign verify-attestation. Étape 1 : Workflow release : permissions id-token write + builder: uses slsa-framework/slsa-github-generator/v2 avec config."
date_ajout: "2026-11"
nom: "Provenance SLSA et attestations in-toto"
emoji: "🧾"
domaine: "Sécurité"
signal: "Attacher une attestation de provenance SLSA à chaque build : slsa-github-generator (keyless, GitHub) produit une attestation in-toto (subject = digest de l'artifact, predicate = source repo, commit, builder, paramètres de build) signée et enregistrée. Niveaux SLSA : L1 build scripté, L2 provenance hébergée, L3 build isolé + source non modifiable (slsa-github-generator = L3). Vérifier : cosign verify-attestation --type slsa-provenance."
mot_cle: "SLSA provenance slsa-github-generator in-toto attestation L3 build isolé cosign verify-attestation predicate"
nom_court: "SLSA provenance"
branche: "D23"
synonymes: ["attestation de provenance SLSA L3 avec slsa-github-generator (keyless GitHub)", "in-toto : subject digest + predicate (repo, commit, builder) signé", "cosign verify-attestation --type slsa-provenance pour vérifier le build"]
cross_refs: [1822, 1824, 1821]
tags: ["2027"]
depends_on: [1822]
---

## 1823. 🧾 Provenance SLSA et attestations in-toto

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Attacher une provenance SLSA (attestation in-toto signée, slsa-github-generator keyless = SLSA L3) à chaque build : source, commit, builder, paramètres — vérifiable avec cosign verify-attestation.

**Quand l'utiliser (triggers)** :
- prouver qu'une image vient bien de notre repo/commit (SLSA provenance)
- slsa-github-generator en keyless sur GitHub Actions (SLSA L3)
- vérifier l'attestation : cosign verify-attestation --type slsa-provenance

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité DevSecOps. Tu ajoutes slasa-github-generator à la release (uses: slsa-framework/slsa-github-generator), l'attestation est générée keyless, et tu la vérifies à l'admission (1824) avec l'issuer + le repo attendus. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- GitHub Actions (OIDC)
- slsa-github-generator
- cosign pour vérifier

**Méthode** :
1. Workflow release : permissions id-token write + builder: uses slsa-framework/slsa-github-generator/v2 avec config.
2. L'attestation in-toto est émise (subject = digest image, predicateType slsa-provenance, predicate = repo/commit/builder).
3. Vérification : cosign verify-attestation --type slsa-provenance --certificate-identity-regexp ... image@digest.
4. Admission : policy (1824) exige provenance valide du bon repo.

**Sorties attendues** :
- L'attestation SLSA provenance attachée à chaque release
- La vérification cosign en CI et à l'admission
- Le niveau SLSA visé documenté (L3)

**Exemple de prompt** :
> « Release v1.4.2 : slsa-github-generator émet l'attestation (repo=org/app, commit=abc123, builder=GitHub Actions) — cosign verify-attestation confirme image@sha256 correspond bien à ce commit. »

**Cas d'usage** : Prouver l'origine des builds. S'articule avec skills 1822, 1824, 1821, 1413.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

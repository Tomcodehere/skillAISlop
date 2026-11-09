---
num: 1825
resume: "Attester des tâches de sécurité (SSDF : scan SAST, revue, scan CVE) dans des attestations CDXA (CycloneDX bom-1.7) signées, liées au SBOM par BOM-Link, enveloppées dans un bundle Sigstore. Étape 1 : Générer le CDXA : cosign attest-blob --predicate cdxa.json --type cyclonedx (bundle Sigstore)."
lang: "fr"
date_ajout: "2026-11"
nom: "Attestations CycloneDX (CDXA) et bundles Sigstore"
emoji: "🧷"
domaine: "Sécurité"
signal: "Compléter le SBOM avec des attestations CDXA (CycloneDX Attestations, bom-1.7) : claims signés par tâche SSDF (ex. 'nous avons fait un scan SAST, preuve ici'), BOM-Link pour lier un claim au SBOM lui-même, expires sur les preuves périssables. Le bundle Sigstore (DSSE) enveloppe le tout pour vérification. Air-gapped : --trusted-root local. N'utilise pas CDXA seul : combiner avec provenance SLSA (1823)."
mot_cle: "CDXA CycloneDX attestations bom-1.7 claims SSDF BOM-Link expires bundle Sigstore DSSE air-gapped trusted-root"
nom_court: "CDXA"
branche: "D23"
synonymes: ["attester des tâches SSDF dans le SBOM (CDXA bom-1.7 claims signés)", "BOM-Link pour lier une attestation au SBOM lui-même", "bundle Sigstore DSSE autour du CDXA + vérification air-gapped trusted-root"]
cross_refs: [1821, 1822, 1823]
tags: ["2027"]
depends_on: [1821]
---

## 1825. 🧷 Attestations CycloneDX (CDXA) et bundles Sigstore

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Attester des tâches de sécurité (SSDF : scan SAST, revue, scan CVE) dans des attestations CDXA (CycloneDX bom-1.7) signées, liées au SBOM par BOM-Link, enveloppées dans un bundle Sigstore.

**Quand l'utiliser (triggers)** :
- prouver à un client que le SAST a été fait sur cette release (attestation CDXA)
- BOM-Link : lier l'attestation au SBOM exact (digest)
- air-gapped : vérifier avec trusted-root local sans accès Rekor

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité / conformité. Tu génères le CDXA (cdxgen/cosign attest-blob --type cyclonedx), tu ajoutes les claims SSDF avec URLs des preuves et expires, et tu vérifies en local avec le trusted-root. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le SBOM CycloneDX (1821)
- cdxgen / cosign
- Les preuves (rapports SAST, scans)

**Méthode** :
1. Générer le CDXA : cosign attest-blob --predicate cdxa.json --type cyclonedx (bundle Sigstore).
2. Claims : chaque tâche SSDF (ex. 'scan SAST passé') avec evidence URL + expires.
3. BOM-Link : relie l'attestation au SBOM par digest (le claim porte sur CE SBOM).
4. Vérification air-gapped : cosign verify-blob --trusted-root root.json --bundle bundle.json.

**Sorties attendues** :
- Le CDXA signé (bundle Sigstore) avec claims SSDF
- Les BOM-Link vers le SBOM par digest
- La vérification air-gapped documentee

**Exemple de prompt** :
> « Release pour un client bancaire : CDXA avec claims 'SAST passé (rapport ici, expire dans 90 j)' + 'SBOM joint par BOM-Link' — le client vérifie le bundle localement (trusted-root), sans accès à Rekor. »

**Cas d'usage** : Conformité client. S'articule avec skills 1821, 1822, 1823, 1824.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

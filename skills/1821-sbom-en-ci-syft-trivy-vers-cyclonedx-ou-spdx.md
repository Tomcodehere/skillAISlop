---
num: 1821
resume: "Générer un SBOM à chaque build en CI (Syft/Trivy, CycloneDX 1.7 ou SPDX 3.0.1, conforme CISA 2026 Minimum Elements), attaché à l'image par digest sha256. Étape 1 : Step CI après le build : syft inférieur àimage@sha256:...supérieur à -o cyclonedx-json supérieur à sbom.cdx.json + spdx-json."
date_ajout: "2026-11"
nom: "SBOM en CI : Syft/Trivy vers CycloneDX ou SPDX"
emoji: "📜"
domaine: "Sécurité"
signal: "Générer un SBOM (Software Bill of Materials) à chaque build en CI avec Syft ou Trivy : format CycloneDX 1.7 (vulnérabilités, conteneurs — ECMA-424) ou SPDX 3.0.1 (licences, ISO/IEC 5962:2021), conforme CISA 2026 Minimum Elements (hashes, licences, contexte de génération, 'unknown' explicite plutôt que vide). Attaché à l'image par digest. N'utilise pas un SBOM statique : le régénérer à chaque build (source/build/runtime)."
mot_cle: "SBOM Syft Trivy CycloneDX 1.7 SPDX 3.0.1 CISA 2026 Minimum Elements CI build image digest"
nom_court: "SBOM CI"
branche: "D23"
synonymes: ["générer un SBOM de mon image en CI (syft cyclonedx-json ou trivy)", "CycloneDX vs SPDX : lequel pour le scan de vulnérabilités (CycloneDX) ou les licences (SPDX)", "CISA 2026 Minimum Elements : hashes + licences + contexte de génération obligatoires"]
cross_refs: [1413, 1822, 1826]
tags: ["2027"]
depends_on: [1413]
---

## 1821. 📜 SBOM en CI : Syft/Trivy vers CycloneDX ou SPDX

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Générer un SBOM à chaque build en CI (Syft/Trivy, CycloneDX 1.7 ou SPDX 3.0.1, conforme CISA 2026 Minimum Elements), attaché à l'image par digest sha256.

**Quand l'utiliser (triggers)** :
- quelle version de log4j est dans mon image prod ?
- SBOM CycloneDX pour grype, SPDX pour les licences
- CISA 2026 : quels champs minimum (hashes, licences, outil, contexte)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité DevSecOps. Tu ajoutes un step CI (1413) : syft image -o cyclonedx-json > sbom.cdx.json (et spdx-json), tu attaches l'SBOM à l'image par digest (cosign attest 1822), et tu valides contre le schéma CycloneDX. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'image buildée (digest)
- Syft ou Trivy en CI
- Le schéma de validation (bom-1.7.schema.json)

**Méthode** :
1. Step CI après le build : syft <image@sha256:...> -o cyclonedx-json > sbom.cdx.json + spdx-json.
2. Valider : cyclonedx validate --fail-on-errors (schéma 1.7) ; CISA 2026 : vérifier hashes/licences/contexte présents, 'unknown' explicite si manquant.
3. Attacher au registre : cosign attest --predicate sbom.cdx.json --type cyclonedx (1822).
4. Stocker aussi en artifact CI (rétention 1 an) pour audit (1830).

**Sorties attendues** :
- Le SBOM CycloneDX + SPDX généré et validé à chaque build
- L'attestation attachée à l'image par digest
- L'artifact CI archivé (rétention)

**Exemple de prompt** :
> « Build image api:v1.4.2 : syft api@sha256:abc -o cyclonedx-json -> sbom.cdx.json (412 composants, licences renseignées), cosign attest l'attache à l'image, grype le lit pour le scan CVE (1826). »

**Cas d'usage** : Inventaire des composants. S'articule avec skills 1413 (CI), 1822 (signature), 1826 (VEX), 1830 (CRA).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

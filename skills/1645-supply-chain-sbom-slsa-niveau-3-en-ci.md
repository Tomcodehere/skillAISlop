---
num: 1645
resume: "Sécuriser la supply chain en 2027 (+40 % d'attaques, ENISA) : SBOM à chaque build (Syft), build SLSA niveau 3 (infra de confiance, provenance signée), signatures vérifiées (cosign 1457), miroir interne + quarantaine, alertes OSV. Étape 1 : SBOM à chaque build : syft → spdx/json, stocké avec la release, scan CVE (grype/trivy)."
date_ajout: "2026-11"
nom: "Supply chain : SBOM + SLSA niveau 3 en CI"
emoji: "⛓️"
domaine: "Sécurité"
signal: "Sécuriser la supply chain en 2027 (attaques +40 % selon ENISA, OWASP A03) : SBOM à chaque build (Syft), SLSA niveau 3 (build sur infra de confiance, provenance signée), vérification des signatures (cosign 1457), miroir interne avec quarantaine, alertes OSV/GitHub Advisory. Utilise pour tout logiciel publié. N'utilise pas pour du code interne jetable."
mot_cle: "supply chain 2027 SBOM SLSA niveau 3 CI cosign miroir interne quarantaine ENISA +40%"
nom_court: "Supply chain"
branche: "D23"
synonymes: ["attaques supply chain +40% en 2026 (ENISA)", "SLSA niveau 3 : build sur infra de confiance provenance signée", "SBOM Syft à chaque build + cosign signature"]
cross_refs: [267, 1457, 1445]
tags: ["2027"]
depends_on: [267]
---

## 1645. ⛓️ Supply chain 2027 : SBOM + SLSA niveau 3 en CI (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser la supply chain en 2027 (+40 % d'attaques, ENISA) : SBOM à chaque build (Syft), build SLSA niveau 3 (infra de confiance, provenance signée), signatures vérifiées (cosign 1457), miroir interne + quarantaine, alertes OSV.

**Quand l'utiliser (triggers)** :
- notre dépendance a été compromise (xz-like)
- SLSA niveau 3 en CI : build vérifiable de bout en bout
- SBOM Syft + cosign à chaque release 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable supply chain. Tu mets en CI : génération SBOM (Syft), build sur runner de confiance (SLSA 3 : provenance signée avec cosign), vérification des signatures des dépendances, miroir interne (Nexus) avec quarantaine 48 h des nouvelles versions, alertes OSV. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La CI (1592) et le registry interne
- Les dépendances et leurs sources
- Les niveaux SLSA visés (3)

**Méthode** :
1. SBOM à chaque build : syft → spdx/json, stocké avec la release, scan CVE (grype/trivy).
2. SLSA 3 : build sur GitHub Actions avec provenance signée (cosign), attestation vérifiable par les clients.
3. Signatures : cosign verify sur les images et releases (1457), lockfile + hashes à l'install (npm ci).
4. Miroir interne : nouvelles versions en quarantaine 48 h (scan + tests auto) avant mise à dispo.
5. Alertes : OSV/GitHub Advisory/RSS ENISA → ticket auto si dépendance touchée (1659).

**Sorties attendues** :
- Le SBOM + provenance SLSA 3 signée à chaque release
- Le miroir interne avec quarantaine 48 h
- Les alertes CVE auto sur les dépendances

**Exemple de prompt** :
> « Une dépendance npm a été compromise (attaque +40 % en 2026) : CI avec SBOM Syft + build SLSA 3 cosigné à chaque release, miroir interne avec quarantaine 48 h, alertes OSV auto. »

**Cas d'usage** : Tout logiciel publié. S'articule avec skills 267 (SBOM), 1457 (signatures), 1445 (MAJ deps) et 1659 (DevSecOps).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

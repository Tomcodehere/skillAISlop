---
num: 1457
date_ajout: "2026-11"
nom: "Integrite des paquets : signatures et SLSA"
emoji: "✅"
domaine: "Sécurité"
signal: "Vérifier l'intégrité et la provenance des paquets en 2027 (supply chain) : signatures (Sigstore/cosign, GPG), niveaux SLSA (build traçable, provenance), lockfile + hash (npm ci, pip --require-hashes), miroirs internes vérifiés. Utilise quand on installe des dépendances tierces. N'utilise pas pour ses propres paquets internes."
mot_cle: "signature paquets cosign sigstore SLSA lockfile hash supply chain"
nom_court: "Supply chain"
branche: "D23"
synonymes: ["vérifier signature paquet npm pip", "SLSA niveau 3 provenance build", "--require-hashes pip"]
cross_refs: [267, 1445, 306]
tags: ["2027"]
depends_on: [267]
---

## 1457. ✅ Integrite des paquets : signatures et SLSA (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser la supply chain en 2027 : vérifier signatures des paquets (Sigstore/cosign ou GPG), exiger provenance SLSA, utiliser lockfile + hashes (npm ci, pip --require-hashes), et un miroir interne vérifié.

**Quand l'utiliser (triggers)** :
- Vérifier qu'un paquet npm n'est pas compromis
- Sigstore cosign signature images Docker
- pip --require-hashes pour la prod

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable supply chain. Tu donnes la chaîne de confiance : lockfile + hashes à l'install (npm ci / pip --require-hashes), vérification de signature (cosign verify pour les images, sigstore pour les releases), et SLSA provenance sur sa propre CI. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le gestionnaire de paquets et son lockfile
- Les images Docker utilisées
- La CI (pour produire la provenance SLSA)

**Méthode** :
1. Installer uniquement via lockfile + hashes (npm ci, pip --require-hashes, go mod verify).
2. Vérifier les signatures des images Docker (cosign verify) et des releases (sigstore).
3. Exiger la provenance SLSA niveau 2+ pour les images produites en interne.
4. Miroir interne (Nexus/Artifact Registry) avec scan + quarantaine des nouveaux paquets.
5. Surveiller les alertes (OSV, GitHub Advisory) sur les dépendances.

**Sorties attendues** :
- L'install verrouillée (lockfile + hashes)
- Les signatures vérifiées (images + releases)
- La provenance SLSA sur la CI interne

**Exemple de prompt** :
> « On installe des paquets npm sans vérifier : verrouille la supply chain (npm ci + lockfile, cosign sur les images Docker, alerte OSV, miroir interne). »

**Cas d'usage** : Sécurité des dépendances, conformité, incident supply chain (xz/ SolarWinds). S'articule avec skills 267 (SBOM), 1445 (MAJ deps) et 306 (secrets).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

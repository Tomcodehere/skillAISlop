---
num: 1828
resume: "Remplacer les images de base lourdes par des images distroless Chainguard (wolfi/apko, 2-10 Mo, sans shell ni package manager, signées Sigstore avec SBOM) pour réduire la surface d'attaque et les CVE. Étape 1 : Choisir la base : cgr.dev/chainguard/python:latest (ou static pour du Go) ou build apko custom."
date_ajout: "2026-11"
nom: "Images distroless Chainguard : réduire la surface d'attaque"
emoji: "🏔️"
domaine: "Sécurité"
signal: "Remplacer les images de base lourdes (debian: 200 Mo, plein de shells/outils) par des images distroless Chainguard (wolfi/apko, ~2-10 Mo, pas de shell, pas de package manager, signées Sigstore, SBOM inclus) : surface d'attaque réduite, moins de CVE, démarre plus vite. Variantes : chainguard/static, chainguard/python, chainguard/node... ou apko/wolfi custom. N'utilise pas si l'app a besoin de debug en shell (prendre la variante dev séparément)."
mot_cle: "images distroless Chainguard wolfi apko 2-10 Mo pas de shell signées Sigstore SBOM surface attaque CVE"
nom_court: "Distroless"
branche: "D23"
synonymes: ["remplacer debian:200Mo par une image distroless chainguard (2 Mo, signée)", "pas de shell dans l'image prod : chainguard/static ou wolfi", "image signée Sigstore + SBOM inclus : chainguard, vérifié à l'admission 1824"]
cross_refs: [1411, 1821, 1822]
tags: ["2027"]
depends_on: [1411]
---

## 1828. 🏔️ Images distroless Chainguard : réduire la surface d'attaque

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Remplacer les images de base lourdes par des images distroless Chainguard (wolfi/apko, 2-10 Mo, sans shell ni package manager, signées Sigstore avec SBOM) pour réduire la surface d'attaque et les CVE.

**Quand l'utiliser (triggers)** :
- mon image debian fait 200 Mo avec 150 CVE : passer en distroless
- pas de shell dans le conteneur prod (moins d'attaque)
- image signée + SBOM inclus d'office (chainguard)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur plateforme / sécurité. Tu choisis la variante Chainguard adaptée (static, python, node, java...) ou tu build une image apko/wolfi custom, tu signes (1822) et tu la fais passer à l'admission (1824). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'app et son runtime (python/node/go/java)
- Chainguard/apko
- La politique d'admission (1824)

**Méthode** :
1. Choisir la base : cgr.dev/chainguard/python:latest (ou static pour du Go) ou build apko custom.
2. Vérifier : pas de shell (docker exec sh échoue), pas de apt/apk en prod, SBOM inclus (syft 1821).
3. Signer : cosign sign (1822), SBOM attesté.
4. Déployer : admission vérifie signature (1824) ; image dev avec shell séparée pour le debug.

**Sorties attendues** :
- L'image distroless déployée (2-10 Mo vs 200 Mo)
- Le scan CVE réduit (surface minimale)
- L'image signée + SBOM + admission OK

**Exemple de prompt** :
> « API Python : debian:slim 180 Mo (150 CVE) -> cgr.dev/chainguard/python 8 Mo, signée cosign, SBOM inclus — scan grype : 3 CVE (vs 150), image admise (1824) car signée. »

**Cas d'usage** : Images prod minimales. S'articule avec skills 1411 (multi-stage), 1821, 1822, 1824.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

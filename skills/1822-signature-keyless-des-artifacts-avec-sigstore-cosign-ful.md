---
num: 1822
resume: "Signer images et artifacts en keyless avec Sigstore (cosign + OIDC du CI → Fulcio cert 10 min → Rekor), et vérifier à l'admission/déploiement par identity (workflow/branche) — aucun secret de signature à gérer. Étape 1 : CI : permissions id-token: write, puis cosign sign --yes ghcr.io/org/app@sha256:... (keyless : Fulcio + Rekor automatiques)."
date_ajout: "2026-11"
nom: "Signature keyless des artifacts avec Sigstore (cosign, Fulcio, Rekor)"
emoji: "✍️"
domaine: "Sécurité"
signal: "Signer les images/artifacts SANS clé longue durée avec Sigstore keyless : cosign obtient un token OIDC du job CI (GitHub Actions/GitLab), l'échange à Fulcio contre un certificat X.509 de ~10 min, signe, et enregistre dans le log de transparence Rekor (inclusion proof). Vérification : cosign verify avec l'issuer attendu (workflow + branche). Avantage : pas de secret à fuir. Air-gapped : --trusted-root local."
mot_cle: "Sigstore cosign keyless Fulcio certificat 10 min Rekor log transparence OIDC GitHub Actions verify issuer air-gapped trusted-root"
nom_court: "cosign keyless"
branche: "D23"
synonymes: ["signer une image sans clé privée longue durée (cosign keyless OIDC Fulcio Rekor)", "cosign verify --certificate-identity-regexp pour vérifier l'issuer du workflow", "air-gapped : cosign verify --trusted-root root.json local"]
cross_refs: [1821, 1824, 1413]
tags: ["2027"]
depends_on: [1821]
---

## 1822. ✍️ Signature keyless des artifacts avec Sigstore (cosign, Fulcio, Rekor)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Signer images et artifacts en keyless avec Sigstore (cosign + OIDC du CI → Fulcio cert 10 min → Rekor), et vérifier à l'admission/déploiement par identity (workflow/branche) — aucun secret de signature à gérer.

**Quand l'utiliser (triggers)** :
- notre clé GPG de signature a fuité : passer au keyless Sigstore
- cosign sign --yes image en CI avec OIDC GitHub Actions
- cosign verify avec certificate-identity-regexp (workflow + branche)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es responsable sécurité DevSecOps. Tu actives l'OIDC du CI (permissions: id-token: write), tu signes avec cosign sign --yes (keyless), et tu vérifies avec l'issuer exact (repo + workflow + branche) — jamais un digest seul. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le CI avec OIDC (GitHub Actions id-token: write)
- cosign installé
- L'identity attendue (repo/workflow/branche)

**Méthode** :
1. CI : permissions id-token: write, puis cosign sign --yes ghcr.io/org/app@sha256:... (keyless : Fulcio + Rekor automatiques).
2. Vérification : cosign verify --certificate-identity-regexp 'https://github.com/org/repo/.github/workflows/release.yml@refs/heads/main' --certificate-oidc-issuer https://token.actions.githubusercontent.com.
3. Air-gapped : cosign verify --trusted-root trusted-root.json (bundle local).
4. Révocation : le cert expire en 10 min — une fuite de CI ne donne pas de clé permanente.

**Sorties attendues** :
- Les images signées keyless (Rekor public)
- La vérification par identity en CI et à l'admission (1824)
- Le mode air-gapped (trusted-root) documente

**Exemple de prompt** :
> « Release image : workflow release.yml (branche main) signe keyless — cosign verify exige identity = ce workflow sur main ; un fork PR ne peut pas signer valablement (identity différente). »

**Cas d'usage** : Signature sans secret. S'articule avec skills 1821 (SBOM attest), 1824 (admission), 1413, 1860 (OIDC).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

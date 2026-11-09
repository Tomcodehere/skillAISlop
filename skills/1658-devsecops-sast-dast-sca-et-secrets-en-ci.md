---
num: 1658
resume: "Mettre le DevSecOps en CI en 2027 : SAST (semgrep, bloquant sur high/critical), SCA (grype/OSV sur les deps, CVE critique bloquante 1445), DAST (ZAP sur staging), secrets (trufflehog/detect-private-key 1403), SBOM+signature (1645) — dans chaque PR. Étape 1 : SAST : semgrep avec règles OWASP 2026 (1646) + règles maison, fail la PR sur severity high/critical, rapport en commentaire PR."
date_ajout: "2026-11"
nom: "DevSecOps : SAST, DAST, SCA et secrets en CI"
emoji: "🔒"
domaine: "Sécurité"
signal: "Intégrer la sécurité dans la CI en 2027 (DevSecOps) : SAST (semgrep/snyk code, bloquant sur high), SCA (dépendances : OSV/grype, blocage CVE critique 1445), DAST (zap sur l'app déployée en staging), secrets (detect-private-key 1403, trufflehog), SBOM (1645), signé (cosign). Utilise dans chaque PR. N'utilise pas sans séparer les seuils (bloquer vs avertir)."
mot_cle: "DevSecOps 2027 CI SAST semgrep DAST zap SCA grype OSV secrets SBOM cosign bloquant PR"
nom_court: "DevSecOps CI"
branche: "D16"
synonymes: ["SAST semgrep bloquant sur CVE high dans chaque PR", "DAST zap sur le staging à chaque déploiement", "SCA grype/OSV sur les dépendances + SBOM 1645"]
cross_refs: [1592, 1645, 1403]
tags: ["2027"]
depends_on: [1592]
---

## 1658. 🔒 DevSecOps 2027 : SAST, DAST, SCA et secrets en CI (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre le DevSecOps en CI en 2027 : SAST (semgrep, bloquant sur high/critical), SCA (grype/OSV sur les deps, CVE critique bloquante 1445), DAST (ZAP sur staging), secrets (trufflehog/detect-private-key 1403), SBOM+signature (1645) — dans chaque PR.

**Quand l'utiliser (triggers)** :
- une CVE critique en prod, pourquoi la CI ne l'a pas bloquée
- SAST semgrep + SCA grype + DAST zap dans la CI (1592)
- SBOM + cosign à chaque build (1645)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DevSecOps engineer. Tu ajoutes à la CI (1592) : job SAST (semgrep, règles OWASP 1646) bloquant sur high, job SCA (grype, fail sur CVE critique CVSS > 9), job secrets (trufflehog), DAST ZAP sur staging après déploiement, SBOM Syft + cosign (1645). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La CI (1592) et le pipeline de déploiement
- Les seuils (bloquer vs avertir)
- Les outils (semgrep, grype, zap, trufflehog)

**Méthode** :
1. SAST : semgrep avec règles OWASP 2026 (1646) + règles maison, fail la PR sur severity high/critical, rapport en commentaire PR.
2. SCA : grype sur le code + l'image Docker, fail sur CVE CVSS > 9 known-exploited (KEV CISA), sauf dérogation signée (expire 30 j).
3. Secrets : trufflehog/detect-private-key (1403) sur tout le repo + historique (rotation si trouvé 1446).
4. DAST : ZAP baseline scan sur le staging à chaque déploiement, fail sur high.
5. Artifacts : SBOM (Syft) + provenance cosignée (1645), stockés avec la release.

**Sorties attendues** :
- La CI sécurisée (SAST/SCA/secrets bloquants + DAST staging)
- Les rapports de vulnérabilités par PR avec seuils
- Le SBOM + signature par release (1645)

**Exemple de prompt** :
> « Une CVE critique est arrivée en prod : ajoute à la CI (1592) semgrep (SAST, bloquant high), grype (SCA, fail CVE > 9 KEV), trufflehog (secrets), ZAP (DAST staging), SBOM+cosign (1645) — la PR est bloquée avant merge. »

**Cas d'usage** : Tout pipeline de livraison. S'articule avec skills 1592 (CI jeu/dev), 1645 (supply chain), 1403 (pre-commit) et 1646 (OWASP).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

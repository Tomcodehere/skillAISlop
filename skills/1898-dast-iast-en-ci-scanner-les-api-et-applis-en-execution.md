---
num: 1898
resume: "Scanner les applications en exécution avec un DAST (OWASP ZAP baseline/full en CI 1413 sur le staging) + IAST si besoin — gate : bloquer le déploiement sur vulnérabilité high/critical, en complément du SAST (1885). Étape 1 : ZAP baseline : zap-baseline.py -t https://staging.example.com en CI (rapport HTML/JSON)."
date_ajout: "2026-11"
nom: "DAST/IAST en CI : scanner les API et applis en exécution"
emoji: "🕷️"
domaine: "Sécurité"
signal: "Scanner les applications EN EXÉCUTION (pas que le code statique SAST 1885) : DAST (dynamic application security testing) avec OWASP ZAP (baseline/full scan) contre l'env de staging en CI (1413) ou nuit : détecte les vraies vulnérabilités (injection SQL 1781+, XSS, config TLS 1871, headers) que le SAST rate. IAST (agent dans l'app, Contrast/Snyk Code) pour la précision. Gate : bloquer le déploiement si vulnérabilité high/critical trouvée. N'utilise pas le DAST seul (faux positifs) : compléter avec SAST (1885) + scan deps (1827)."
mot_cle: "DAST OWASP ZAP scan dynamique application en exécution CI staging IAST Contrast Snyk Code injection XSS config TLS gate déploiement vulnérabilités high SAST 1885"
nom_court: "DAST en CI"
branche: "D23"
synonymes: ["OWASP ZAP en CI contre le staging : détecte les vraies vulns (XSS, injection) que le SAST rate", "gate : vulnérabilité critical trouvée en DAST — déploiement bloqué (CI 1413)", "IAST (Contrast) pour réduire les faux positifs du DAST"]
cross_refs: [1885, 1413, 1827]
tags: ["2027"]
depends_on: [1885]
---

## 1898. 🕷️ DAST/IAST en CI : scanner les API et applis en exécution

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Scanner les applications en exécution avec un DAST (OWASP ZAP baseline/full en CI 1413 sur le staging) + IAST si besoin — gate : bloquer le déploiement sur vulnérabilité high/critical, en complément du SAST (1885).

**Quand l'utiliser (triggers)** :
- le SAST ne voit pas l'injection réelle : ajouter un DAST (ZAP) en CI sur le staging
- gate déploiement : ZAP trouve une XSS reflected (high) -> blocage CI 1413
- ZAP baseline (rapide, passif) vs full scan (actif, plus long, la nuit)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es AppSec / développeur. Tu ajoutes un job ZAP (baseline) en CI sur le staging à chaque PR (1413), full scan la nuit, et le gate bloque sur high/critical ; IAST en complément pour les faux positifs. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'env de staging déployé (1418)
- OWASP ZAP (docker) en CI (1413)
- Les seuils (bloquer sur high/critical)

**Méthode** :
1. ZAP baseline : zap-baseline.py -t https://staging.example.com en CI (rapport HTML/JSON).
2. Full scan la nuit (actif, plus complet mais plus lent) sur le staging.
3. Gate CI : parse le rapport ZAP, si high/critical -> fail (1413), déploiement bloqué (1418).
4. IAST (Contrast/Snyk Code) en option pour confirmer (moins de faux positifs).
5. Compléter : SAST 1885 (code), scan deps 1827, gitleaks 1859 — les 4 couches.

**Sorties attendues** :
- Le DAST ZAP en CI (baseline PR, full nuit)
- Le gate actif (high/critical = blocage)
- Le rapport de vulnérabilités (tendance à la baisse)

**Exemple de prompt** :
> « PR avec une nouvelle route /search?q= : SAST (1885) voit rien, ZAP baseline en CI trouve une XSS reflected (high) -> gate rouge, déploiement bloqué (1418) ; le dev corrige (échappement), ZAP vert, merge. »

**Cas d'usage** : Sécurité applicative dynamique. S'articule avec skills 1885, 1413, 1827, 1826, 1886.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

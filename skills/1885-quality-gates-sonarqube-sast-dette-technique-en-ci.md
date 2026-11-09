---
num: 1885
resume: "Bloquer les régressions qualité en CI (1413) avec SonarQube : quality gate (SAST, bugs, vulnérabilités 1826, couverture, dette) — la PR est bloquée si le nouveau code est sous les seuils. Étape 1 : SonarQube scan en CI (sonar-scanner) sur chaque PR -supérieur à rapport + quality gate."
lang: "fr"
date_ajout: "2026-11"
nom: "Quality gates : SonarQube, SAST, dette technique en CI"
emoji: "🧪"
domaine: "Développement"
signal: "Bloquer les régressions qualité en CI (1413) avec des quality gates : SonarQube (self-host ou Cloud) — SAST, bugs, vulnérabilités (1826), code smells, dette technique (temps de remboursement), couverture de tests (seuil ex. 80 %), duplication ; gate 'failed' si nouveau code inférieur à seuil. Métriques DORA (1888) + qualité dans le même dashboard (1766). N'utilise pas Sonar seul sans gate CI (rapport que personne ne lit)."
mot_cle: "SonarQube quality gate CI SAST dette technique couverture tests seuil blocage PR smells bugs vulnérabilités DORA 1888 dashboard 1766"
nom_court: "Quality gates"
branche: "D12"
synonymes: ["bloquer la PR si le nouveau code a des vulnérabilités ou couverture inférieur à 80 % (quality gate Sonar)", "dette technique Sonar : temps de remboursement en jours, à réduire chaque sprint", "SAST Sonar + scan deps 1827 + gitleaks 1859 : les 3 gates en CI 1413"]
cross_refs: [1413, 1826, 1859]
tags: ["2027"]
depends_on: [1413]
---

## 1885. 🧪 Quality gates : SonarQube, SAST, dette technique en CI

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Bloquer les régressions qualité en CI (1413) avec SonarQube : quality gate (SAST, bugs, vulnérabilités 1826, couverture, dette) — la PR est bloquée si le nouveau code est sous les seuils.

**Quand l'utiliser (triggers)** :
- une vulnérabilité critique est arrivée en prod via une PR : quality gate Sonar en CI
- couverture de tests < 80 % sur le nouveau code : bloquer le merge
- dette technique Sonar : 12 j à rembourser -> la réduire à 5 j ce sprint

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur / lead tech. Tu configures le quality gate Sonar (seuils : 0 vulnérabilité critique, couverture 80 %, dette ratio A), branché en CI (1413), avec les autres scans (1826, 1859). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- SonarQube (Cloud ou self-host)
- La CI (1413)
- Les seuils de qualité validés par l'équipe

**Méthode** :
1. SonarQube scan en CI (sonar-scanner) sur chaque PR -> rapport + quality gate.
2. Quality gate : conditions (coverage >= 80 %, 0 critical/high vuln 1826, reliability A, dette ratio < 5 %) -> status failed = PR bloquée.
3. Dashboard unifié (1766) : qualité + DORA (1888) + déploiement (1418).
4. Règle : nouveau code propre, dette legacy gérée en tickets (pas dans les PR).

**Sorties attendues** :
- Le quality gate actif (PR bloquée si sous seuil)
- Le dashboard qualité+DORA (1766)
- La dette legacy en tickets suivis

**Exemple de prompt** :
> « PR ajoute 200 lignes sans test + 1 vulnérabilité high (deps 1826) : Sonar quality gate = failed -> PR bloquée, le dev corrige, re-scan vert -> merge. Prod : 0 vulnérabilité arrivée ce trimestre. »

**Cas d'usage** : Qualité préventive. S'articule avec skills 1413, 1826, 1859, 1888, 1766, 1401.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

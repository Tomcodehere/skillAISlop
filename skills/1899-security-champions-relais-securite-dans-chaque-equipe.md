---
num: 1899
resume: "Déployer un programme de security champions : 1 relais formé par équipe (10 % de temps alloué), threat model (STRIDE) en conception, relai des alertes (1761) et bonnes pratiques (1885, 1859). Étape 1 : Nommer + former les champions (OWASP Top 10, secure coding 1736, menaces LLM 1845, RGPD 1839)."
date_ajout: "2026-11"
nom: "Security champions : relais sécurité dans chaque équipe"
emoji: "🏆"
domaine: "Gestion"
signal: "Déployer un programme de security champions : 1 volontaire par équipe produit (pas un expert à plein temps), formé (OWASP, secure coding 1736), qui fait le relais RSSI inférieur à — équipe : revue des menaces (STRIDE) en conception, relai des alertes (1761), porte les bonnes pratiques (1885, 1859) au quotidien. Réunions mensuelles, canal dédié, reconnaissance. N'utilise pas sans temps alloué (ex. 10 % du temps) — sinon le rôle meurt. Métrique : % de menaces revues en conception, délai de correction des vulnérabilités."
mot_cle: "security champions programme relais sécurité par équipe STRIDE conception formation 10 % temps canal dédié métriques menaces revues délai correction vulnérabilités"
nom_court: "Security champions"
branche: "D25"
synonymes: ["1 security champion par équipe produit (10 % de son temps, formé) : relais RSSI au quotidien", "revue de menaces STRIDE en conception avec le champion, pas après coup", "métrique : % de features avec threat model fait avant le dev"]
cross_refs: [1736, 1885, 1859]
tags: ["2027"]
---

## 1899. 🏆 Security champions : relais sécurité dans chaque équipe

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer un programme de security champions : 1 relais formé par équipe (10 % de temps alloué), threat model (STRIDE) en conception, relai des alertes (1761) et bonnes pratiques (1885, 1859).

**Quand l'utiliser (triggers)** :
- les vulnérabilités arrivent toujours après le dev : threat model STRIDE en conception avec le champion
- nommer 1 champion par équipe (formé, 10 % temps) + canal dédié + réunions mensuelles
- métrique : % de features avec threat model avant dev (objectif 80 %)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI / engineering manager. Tu recrutes 1 champion par équipe, tu le formes (OWASP, secure coding 1736, menace IA 1845), tu lui bloques 10 % de temps, et tu mesures l'adoption (threat models faits avant dev). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les volontaires par équipe
- Le programme (formation, canal, réunions)
- Le temps alloué (10 %)

**Méthode** :
1. Nommer + former les champions (OWASP Top 10, secure coding 1736, menaces LLM 1845, RGPD 1839).
2. Threat model STRIDE en conception de chaque feature (avant le dev), doc dans l'ADR (1746/1889).
3. Relais : alertes 1761 -> tri par le champion, bonnes pratiques (1885 quality gates, 1859 fuites) au quotidien.
4. Réunions mensuelles + canal dédié + reconnaissance publique.
5. Métriques : % features avec threat model (objectif 80 %), délai de correction des vuln (objectif < 7 j pour high 1826).

**Sorties attendues** :
- Le programme actif (N champions formés, 10 % temps)
- Les threat models faits avant dev (mesuré)
- Le délai de correction des vulnérabilités en baisse

**Exemple de prompt** :
> « 12 équipes = 12 champions formés ; threat model STRIDE fait sur 80 % des features (vs 10 % avant) ; une vuln high (1826) corrigée en 3 j (vs 3 semaines avant) grâce au relais champion + quality gate 1885. »

**Cas d'usage** : Sécurité distribuée. S'articule avec skills 1736, 1885, 1859, 1761, 1845.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

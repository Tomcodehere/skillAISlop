---
num: 1715
date_ajout: "2026-11"
nom: "Documentation développeur interne : TechDocs et docs-as-code"
emoji: "📖"
domaine: "Développement"
signal: "Centraliser la doc développeur en 2027 : docs dans chaque repo (docs/*.md, doc-as-code 1406) rendues dans le portail (Backstage TechDocs 1702) ou un site statique (MkDocs/Docusaurus 1406), avec owner par doc (scorecard 1711), revue à chaque PR, recherche globale. Règle : la doc vit avec le code (même repo, même PR), jamais dans un wiki séparé qui pourrit. N'utilise pas pour la doc utilisateur externe (marketing)."
mot_cle: "TechDocs Backstage doc développeur dans le repo docs/*.md doc-as-code 1406 même PR recherche globale"
nom_court: "TechDocs"
branche: "D15"
synonymes: ["la doc développeur vit dans le repo (docs/), rendue dans Backstage TechDocs", "même PR pour code et doc (jamais de wiki qui pourrit)", "recherche globale dans toute la doc interne (TechDocs)"]
cross_refs: [1702, 1406, 312]
tags: ["2027"]
depends_on: [1406]
---

## 1715. 📖 Documentation développeur interne : TechDocs et docs-as-code (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Centraliser la doc développeur en 2027 : docs/*.md dans chaque repo (même PR que le code, doc-as-code 1406), rendues dans le portail (Backstage TechDocs 1702) avec owner (scorecard 1711), recherche globale, et lien depuis le catalogue de services.

**Quand l'utiliser (triggers)** :
- la doc interne est dans 3 wikis différents et périmée
- TechDocs : la doc du repo rendue dans Backstage
- même PR pour code et doc (règle du repo)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es tech writer / platform. Tu mets docs/ dans chaque repo (architecture ADR 88, runbooks 199, onboarding 1713, API 180), mkdocs.yml pour le rendu, TechDocs dans Backstage qui le publie automatiquement, et tu relies chaque service du catalogue à sa doc. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les repos (docs/ à créer)
- Le portail (Backstage TechDocs 1702)
- Les owners de doc (scorecard 1711)

**Méthode** :
1. Structure par repo : docs/ (architecture.md avec ADR 88, runbook.md 199, api.md 180, onboarding.md 1713), mkdocs.yml, owner dans CODEOWNERS.
2. Règle : toute PR qui change du code met à jour docs/ (check CI 1413 : doc modifiée si code changé).
3. TechDocs (Backstage 1702) publie automatiquement chaque repo → recherche globale dans le portail.
4. Catalogue : chaque service pointe vers sa doc (lien direct).
5. Péremption : doc non modifiée depuis 12 mois = warning (scorecard 1711), revue forcée.

**Sorties attendues** :
- La doc dans chaque repo (docs/) publiée via TechDocs, recherchable globalement
- La règle 'même PR code+doc' avec check CI (1413)
- Le lien catalogue→doc par service + alerte péremption 12 mois

**Exemple de prompt** :
> « La doc interne est éparpillée et périmée : passe en doc-as-code (docs/ dans chaque repo, mkdocs.yml, TechDocs dans Backstage 1702), règle 'même PR code+doc' checkée en CI (1413), recherche globale, alerte si doc vieille de 12 mois (1711). »

**Cas d'usage** : Documentation interne engineering. S'articule avec skills 1702 (Backstage), 1406 (docs-as-code), 312 (README) et 1711 (scorecards).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

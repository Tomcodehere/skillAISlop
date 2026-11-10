---
num: 1406
resume: "Mettre en place une doc technique vivante en 2027 : dans le dépôt, générée depuis le code quand possible, avec check CI des liens morts et exemples testés. Étape 1 : Inventorier la doc et décider ce qui vit dans le repo."
lang: "fr"
date_ajout: "2026-11"
nom: "Documentation vivante (docs-as-code)"
emoji: "📖"
domaine: "Développement"
signal: "Maintenir une documentation technique vivante en 2027 (docs-as-code) : doc dans le dépôt (Markdown, MkDocs/Docusaurus), générée depuis le code (docstrings, OpenAPI), testée en CI (liens morts). Utilise quand la doc dérive du code. N'utilise pas pour la doc marketing."
mot_cle: "documentation vivante docs-as-code markdown docusaurus"
nom_court: "Docs-as-code"
branche: "D15"
synonymes: ["doc qui colle au code", "documentation dans le repo", "mkdocs docusaurus 2027"]
cross_refs: [23, 312, 1030]
tags: ["2027"]
depends_on: [23]
---

## 1406. 📖 Documentation vivante (docs-as-code, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place une doc technique vivante en 2027 : dans le dépôt, générée depuis le code quand possible, avec check CI des liens morts et exemples testés.

**Quand l'utiliser (triggers)** :
- Notre doc est obsolète, comment la rendre vivante ?
- Docs-as-code : quoi mettre dans le repo ?
- Vérifier les liens morts de la doc en CI

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es rédacteur technique docs-as-code. Tu proposes l'architecture (doc dans /docs, site statique MkDocs/Docusaurus, docstrings + OpenAPI générés, exemples testés via doctest) et un check CI (liens + build). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La doc existante et son outil
- Le code et ses docstrings/OpenAPI
- L'audience (dev interne ou externe/API)

**Méthode** :
1. Inventorier la doc et décider ce qui vit dans le repo.
2. Choisir l'outil (MkDocs/Docusaurus) et la structure /docs.
3. Générer depuis le code : docstrings, schéma OpenAPI, diagrammes mermaid.
4. CI : build du site + liens morts + exemples testés.
5. Règle d'équipe : toute PR code met à jour la doc correspondante.

**Sorties attendues** :
- Le site de doc généré et en ligne
- La config CI (build + liens morts)
- La règle d'équipe PR code + doc

**Exemple de prompt** :
> « Notre doc API est un PDF obsolète : mets en place une doc vivante docs-as-code (OpenAPI généré, site statique, CI liens morts). »

**Cas d'usage** : Onboarding devs, doc API publique. S'articule avec skills 23 (doc technique), 312 (README) et 1030 (doc OpenAPI).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1889
resume: "Maintenir la doc développeur interne en doc-as-code : TechDocs (Backstage 1702) publie README/ADR/runbooks (1764) du repo en site auto — même PR que le code (1401), zéro drift. Étape 1 : Chaque repo a un README + docs/ (mkdocs.yml) ; TechDocs (1702) publie sur le portail interne à chaque merge."
date_ajout: "2026-11"
nom: "Documentation développeur interne : TechDocs, doc-as-code"
emoji: "📖"
domaine: "Développement"
signal: "Maintenir la doc développeur interne en doc-as-code : TechDocs (Backstage 1702) publie les README/ADR/runbooks du repo en site interne automatiquement (mkdocs/material), + runbooks incidents (1764), ADR (1746), architecture (C4). Règle : la doc vit dans le repo (même PR que le code, revue ensemble 1401), publiée auto. N'utilise pas un wiki séparé (drift garanti)."
mot_cle: "TechDocs Backstage doc-as-code mkdocs README ADR runbooks 1764 site doc interne auto publié même PR que le code 1401 drift"
nom_court: "Doc dev interne"
branche: "D15"
synonymes: ["TechDocs (Backstage 1702) : les README du repo publiés en site doc interne auto", "un ADR par décision d'architecture (1746) dans docs/adr/, revu en PR (1401)", "runbooks incidents (1764) à côté du code, publiés dans la doc interne"]
cross_refs: [1702, 1715, 1764]
tags: ["2027"]
depends_on: [1702]
---

## 1889. 📖 Documentation développeur interne : TechDocs, doc-as-code

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Maintenir la doc développeur interne en doc-as-code : TechDocs (Backstage 1702) publie README/ADR/runbooks (1764) du repo en site auto — même PR que le code (1401), zéro drift.

**Quand l'utiliser (triggers)** :
- le README du service est obsolète depuis 6 mois : doc-as-code + revue en PR
- TechDocs Backstage : tous les repos publiés automatiquement (mkdocs)
- ADR : décision archi consignée dans docs/adr/ (1746), relue (1401)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur / tech writer. Tu mets la doc dans le repo (docs/, README par service, docs/adr/), TechDocs la publie, et la règle 'doc dans la même PR que le code' est appliquée en revue (1401). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Backstage + TechDocs (1702)
- Les repos avec mkdocs.yml / docusaurus
- La règle de revue (1401)

**Méthode** :
1. Chaque repo a un README + docs/ (mkdocs.yml) ; TechDocs (1702) publie sur le portail interne à chaque merge.
2. ADR dans docs/adr/NNN-titre.md (1746) : contexte, décision, conséquences — relu en PR.
3. Runbooks (1764) liés aux alertes (1761), publiés aussi.
4. Règle de revue (1401) : un changement de code sans sa doc = PR non mergeable.

**Sorties attendues** :
- Le portail doc interne à jour (TechDocs)
- Les ADR à jour (décisions tracées)
- La règle 'doc = même PR' appliquée

**Exemple de prompt** :
> « Nouveau service payments : README + docs/ (architecture C4, runbooks 1764) dans la PR de création — TechDocs publie automatiquement ; revue (1401) exige la doc à jour avant merge. »

**Cas d'usage** : Doc vivante. S'articule avec skills 1702, 1715, 1764, 1746, 1406, 1401.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

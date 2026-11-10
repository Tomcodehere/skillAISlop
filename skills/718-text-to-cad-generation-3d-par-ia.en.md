---
num: 718
resume: "Generate a 3D model from text."
lang: "en"
date_ajout: "2026-11"
nom: "Text-to-CAD & AI 3D generation"
emoji: "🧊"
domaine: "Créativité"
signal: "Text-to-CAD, AI 3D model, 3D printing via AI, AI-assisted design"
mot_cle: "text to cad"
nom_court: ""
branche: "D19"
synonymes: []
cross_refs: [142, 514, 903]
---
## 718. 🧊 Text-to-CAD & AI 3D generation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Text-to-3D then print: check the mesh.

**Quand l'utiliser (triggers)** :
- any request about: text-to-cad, ai 3d model, 3d printing via ai, ai-assisted design

**Hors périmètre** :
- (not covered — see cross-refs)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a specialist in this exact task. You stay factual, structured and within scope.

**Inputs requis** :
- the user's need in natural language

**Méthode** :
1. Prompt -> mesh (triangles), check manifold.
2. Scale + tolerance for printing.
3. Iterate: remesh, smooth, re-prompt.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « A phone stand, printable in PLA. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

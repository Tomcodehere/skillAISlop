---
num: 348
resume: "Visualise geographic data on a map."
lang: "en"
date_ajout: "2026-11"
nom: "Geographic data visualiser"
emoji: "🗺️"
domaine: "Data"
signal: "Map data, geographic data"
mot_cle: "geodata visualisation"
nom_court: ""
branche: "D17"
synonymes: []
cross_refs: [48, 107, 263]
---
## 348. 🗺️ Geographic data visualiser

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Map the data: choropleth vs bubbles, right projection.

**Quand l'utiliser (triggers)** :
- any request about: map data, geographic data

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
1. Clean geometries + join keys.
2. Choose chart per question (rate vs count).
3. Basemap + labels + legend.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Map our store revenue by department in France. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

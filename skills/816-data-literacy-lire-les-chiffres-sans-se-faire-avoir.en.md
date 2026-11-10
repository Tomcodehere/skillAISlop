---
num: 816
resume: "Read data critically."
lang: "en"
date_ajout: "2026-11"
nom: "Data literacy: read numbers without being fooled"
emoji: "📊"
domaine: "Apprentissage"
signal: "Data literacy, misleading charts"
mot_cle: "data literacy"
nom_court: ""
branche: "D28"
synonymes: []
cross_refs: [547, 806, 815]
---
## 816. 📊 Data literacy: read numbers without being fooled

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Base rates, correlation vs causation, chart tricks (see 547).

**Quand l'utiliser (triggers)** :
- any request about: data literacy, misleading charts

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
1. Ask: sample? compared to what? who measured?
2. Beware truncated axes.
3. Check the source.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Is this chart misleading? » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

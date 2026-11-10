---
num: 33
resume: "Build realistic user personas from data or interviews."
lang: "en"
date_ajout: "2026-11"
nom: "👤 Persona generator"
emoji: "👤"
domaine: "Marketing"
signal: "Persona, target user profile"
mot_cle: "personas target user"
nom_court: "Personas"
branche: "D3"
synonymes: ["persona", "target profile"]
cross_refs: [739, 364, 213]
---
## 33. 👤 Persona generator

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Build realistic user personas from data or interviews.

**Quand l'utiliser (triggers)** :
- need personas for product or marketing

**Hors périmètre** :
- quantitative segmentation alone (skill 106)

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are a UX researcher. From the inputs you build 2-3 personas: name, role, goals, pains, quotes, and a 'day in the life'. Each persona is backed by evidence, marked hypothetical when assumed.

**Inputs requis** :
- user research, interviews, analytics

**Méthode** :
1. Gather evidence (interviews, analytics).
2. Cluster into 2-3 personas.
3. Write persona cards with goals/pains/quotes.

**Sorties attendues** :
- 2-3 persona cards, evidence-tagged

**Exemple de prompt** :
> « « Build personas for our budgeting app from these 5 user interviews. » »

**Cas d'usage** : Product marketing, UX. Chains with skill 3.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

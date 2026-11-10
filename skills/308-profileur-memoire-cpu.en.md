---
num: 308
resume: "Profile memory and CPU to find leaks."
lang: "en"
date_ajout: "2026-11"
nom: "Memory & CPU profiler"
emoji: "⏱️"
domaine: "Développement"
signal: "Memory leak, profiler, CPU usage"
mot_cle: "profiling"
nom_court: ""
branche: "D16"
synonymes: []
cross_refs: [256, 309, 560]
---
## 308. ⏱️ Memory & CPU profiler

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Profile a slow/leaky app and find the hotspot.

**Quand l'utiliser (triggers)** :
- any request about: memory leak, profiler, cpu usage

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
1. Reproduce under load, capture profiles.
2. Read heap/CPU flamegraphs.
3. Fix + verify with before/after.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « Our worker RSS grows 100MB/hour — profile it. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

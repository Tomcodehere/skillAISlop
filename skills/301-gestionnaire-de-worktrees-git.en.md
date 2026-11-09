---
num: 301
resume: "Use git worktrees to work on two branches in parallel."
lang: "en"
date_ajout: "2026-11"
nom: "Git worktree manager"
emoji: "🌿"
domaine: "Développement"
signal: "Work on two branches in parallel, git worktree"
mot_cle: "git worktrees"
nom_court: ""
branche: "D15"
synonymes: []
cross_refs: [68, 316, 306]
---
## 301. 🌿 Git worktree manager

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Run parallel branches with worktrees.

**Quand l'utiliser (triggers)** :
- any request about: work on two branches in parallel, git worktree

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
1. git worktree add per branch.
2. One IDE window per worktree.
3. Merge + prune regularly.

**Sorties attendues** :
- the deliverable, structured and verified

**Exemple de prompt** :
> « « I need to hotfix prod while my feature branch is WIP. » »

**Cas d'usage** : Professional use of this skill.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

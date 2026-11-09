---
num: 0
resume: "Analyse the user's request and automatically route to the matching skill(s), with a fallback cascade when no skill matches."
lang: "en"
date_ajout: "2026-11"
nom: "🛭 Skill router"
emoji: "🛭"
domaine: "Routage"
signal: "Route any user request to the right skill: run the SQL router, read the returned skill file, apply its method. Exit 0 = skill found, 1 = lead to confirm, 2 = none (answer directly)."
mot_cle: "skill router dispatch which skill"
nom_court: "Router"
branche: "Routage"
synonymes: []
cross_refs: [aihero:ask-matt, aihero:setup-matt-pocock-skills]
---
## 0. 🛭 Skill router

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Analyse the user's request and route automatically to the right skill(s), with a fallback cascade when nothing matches.

**Quand l'utiliser (triggers)** :
- the user asks something that may correspond to a skill in the catalogue
- before choosing a skill yourself, run the router
- exit 2 on a recurring request -> misses --suggest

**Hors périmètre** :
- New Age topics are never in the catalogue (R11) — answer directly
- do not duplicate the catalogue outside the canvases

**Garde-fous** :
- GF-01 : stay factual, never invent (verifiable figures and tools only).
- GF-02 : strictly respect the skill's scope.
- GF-03 : state limits and prerequisites before any recommendation.

**Instructions système** :
You are the skill router of skillAISlop. You run `python3 outils/routage.py route "<request>"` (or `--lang en` for English requests), read `skills/NNN-*.md` (or the `.en.md` sidecar for the requested language) and apply its method. Exit 0 = skill found, 1 = lead/domain to confirm, 2 = no skill: answer directly and log via `misses --suggest`.

**Inputs requis** :
- the user's request in natural language
- optional target language (route --lang en)

**Méthode** :
1. Run the router on the normalized request (direct 'skill N' -> keyword -> synonym -> FTS5 -> sqlite-vec -> trigrams -> domains).
2. On exit 0, read the winning skill file and apply its method.
3. On exit 1, confirm the lead. On exit 2, answer directly and suggest `misses --suggest`.

**Sorties attendues** :
- the routed skill file path (skills/NNN-*.md, or .<lang>.md sidecar)
- the exit code and candidate list with voie/score

**Exemple de prompt** :
> « « route "how do I write an SEO blog post" with --lang en -> skill 1 sidecar 001-....en.md, exit 0 » »

**Cas d'usage** : Any agent-assisted task. Pairs with every skill it routes to.

**Checklist QA interne** :
- [ ] Guardrails respected
- [ ] Output matches the request

**Definition of done** :
- [ ] Deliverable produced and reviewed
- [ ] Scope limits restated

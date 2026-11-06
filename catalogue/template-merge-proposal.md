# Proposition de merge des deux templates de skill

Date : 2026-11-05 · Sources : `catalogue/template.md` (skillAISlop, R2, 5 sections) vs `templateSkills.md` (repo tvprodel/SkillsAI, 13 sections)

## Décision actée (2026-11-05)

- **Conservé** : frontmatter YAML + précision I/O (Inputs/Sorties) + routage R3 (SQLite)
- **11 sections obligatoires** : Objectif, Triggers, Hors périmètre, Instructions système (allégé), Inputs, Méthode, Sorties, Garde-fous, Exemple de prompt, Cas d'usage, QA + DoD
- **Optionnels** (hors audit bloquant) : KPI, Templates I/O, Références (conditionnelle, règle SkillsAI)
- Ordre primacy/recency : contraintes/triggers/garde-fous en tête, workflow au milieu, exemples après

## Conformité standards web (veille 2026-11-05)

Spec Agent Skills ouverte (agentskills.io/AAIF, 32+ outils), docs Anthropic, IBM watsonx/Bob, étude UC Irvine 2026 (238 skills) : ✅ conforme (frontmatter, triggers, garde-fous — 94 % des skills réelles en manquent, I/O, QA/DoD=evals, exemples). Améliorations retenues : kebab-case ≤ 64, signal ≤ 1024 car. « Utilise quand… », pas de `<>` dans le frontmatter, < 500 lignes, `metadata.version`, `allowed-tools`/`disable-model-invocation`/`evals` optionnels, lint spec en CI.

## Fichiers

- `documentations/skillsdocs/TEMPLATE-v2.md` — template fusionné (à appliquer vague 14)
- `outils/migrate_template.py` — audit/fix des skills existantes
- `documentations/skillsdocs/migration-v2.md` — rapport d'audit actuel

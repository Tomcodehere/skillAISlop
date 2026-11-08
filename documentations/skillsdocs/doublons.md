# Rapport de doublons — 2026-11-05

## 1. Interne (catalogue skillAISlop, 1000 skills)
- Lint R6 ✅ + scan noms/mots-clés/signaux/synonymes normalisés : **0 doublon** (noms, mot_cle, signal, synonymes tous uniques)

## 2. Cross-repo vs tvprodel/SkillsAI (311 *.skill.md, cloné localement)
- **0 doublon exact** (nom/slug identique)
- 112 recouvrements thématiques (≥2 mots communs) — la plupart sont des variantes de domaine, pas des doublons
- **33 candidats avec mot-clé/synonyme commun**, dont vrais candidats de fusion :
  - `promptInjectionBoundaryEvaluation` ↔ skill 818 (injection web) et 17 (prompts)
  - `scrapingEthicsLegalAwareness` ↔ skill 940 (scraping légal) + 91 (scraping)
  - `dynamicWebScrapingPlaywrightSelenium` / `staticWebScraping...` ↔ skill 91
  - `backupRecoveryAutomation` ↔ skill 596 (sauvegardes)
  - `aiAdoptionFeedbackDecision` / `roastMyIdea` ↔ skill 644 (feedback)
  - `onboardingInstructionDesign` ↔ skills 203/698 (onboarding)
  - `promptVersioningTesting` / `promptStructureOptimization` / `promptEngineerGuardrails` ↔ skill 17 (prompts)
  - `businessKpiAnalysisDashboardDesign` ↔ skill 107 (dashboard)
  - `dataRetentionPolicyDesign` ↔ skill 106 (rétention)
  - `productOutcomeRoadmap` ↔ skill 176 (roadmap)
  - `powerpointDesignEfficiency` ↔ skill 14 (présentations)
  - `vectorIllustrationConstruction` ↔ skill 141 (illustrations)
  - faux positifs (mot-clé trop générique) : streamingDataProcessing/perlStreamTransformation → 576, belgianVatTaxOrientation/notarialProceduresBelgium → 571, gestionEchecsRollback → 567, godot* → 524, progressionLootTableBalancing → 204, portfolioCapacityPlanner → 572

## Décision
Aucun doublon à supprimer dans notre catalogue (R6 propre). Les 33 candidats cross-repo sont des **compléments**, pas des doublons : on garde nos skills, et on peut reprendre les sections fortes de SkillsAI (garde-fous, QA, DoD) via TEMPLATE-v2 à la vague 14. Aucun merge de contenu nécessaire.

## 3. Cross-repo vs aihero.dev/skills (Matt Pocock, 39 skills, MIT, 2026-11-07)
- 39 skills analysées (repo mattpocock/skills cloné) : **100 % déjà couvertes** par notre catalogue → 0 nouvelle skill créée
- 111 tags `aihero:<slug>` ajoutés en cross-ref sur nos skills équivalentes (filtre `route --tag aihero:grill-me`)
- Aucune fusion de contenu nécessaire ; les skills aihero restent installables via `npx skills add mattpocock/skills`

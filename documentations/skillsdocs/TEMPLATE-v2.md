# TEMPLATE v2 — skill skillAISlop (proposition, à appliquer à la vague 14)

> Fusion de notre template R2 et de `templateSkills.md` (tvprodel/SkillsAI), validée contre la spec ouverte Agent Skills (agentskills.io / AAIF) et les bonnes pratiques Anthropic / IBM / étude UC Irvine 2026.
> **Conservé tel quel** : frontmatter YAML + routage R3 (SQLite). **Optionnels** : KPI, Templates I/O, Références.
> Comparaison complète : `catalogue/template-merge-proposal.md`.

## Règles de conformité (lint spec 2026)

- fichier `NNN-slug.md` en **kebab-case ≤ 64 caractères** (déjà conforme)
- `signal` : **≤ 1024 caractères, 3ᵉ personne, « Utilise quand… / N'utilise pas pour… »**
- **pas de `<` ni `>` dans le frontmatter** (injection system prompt)
- corps **< 500 lignes**, références à **1 niveau max** de profondeur
- `metadata.version` par skill ; statut déprécié possible dans `signal`
- champs optionnels : `allowed-tools`, `disable-model-invocation`, `evals`

## Squelette (11 sections obligatoires, ordre primacy/recency)

```markdown
---
num: NNN
nom: "Nom de la skill"
emoji: "🎯"
domaine: "Domaine"
signal: "Ce que fait la skill. Utilise quand… N'utilise pas pour… (≤ 1024 car.)"
mot_cle: "mot-clé canonique"
nom_court: "Nom court"
branche: "Dxx"
synonymes: ["syn1", "syn2"]
cross_refs: [12, 34]
# optionnels : allowed-tools · disable-model-invocation · metadata: {version: "13.0.0"} · evals
---

## NNN. <emoji> <Nom>

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : <1 phrase, livrable attendu>

**Quand l'utiliser (triggers)** : <3-5 déclencheurs = le signal>

**Hors périmètre** : <ce qui ne route PAS ici>

**Garde-fous** : <GF-01… contraintes dures — en tête (primacy), rappelés en fin>

**Instructions système** :
Tu es <rôle>. <2-3 règles dures max — ne pas sur-prescrire>

**Inputs requis** : <données nécessaires>

**Méthode** :
1. <collecte/clarification>
2. <production>
3. <clôture + contrôle qualité>

**Sorties attendues** : <livrables>

**Exemple de prompt** :
> « <demande réaliste avec contexte> »

**Cas d'usage** : <2-3 usages réels>

**Checklist QA interne** : <[ ] critères avant livraison>

**Definition of done** : <[ ] critères mesurables>

<!-- Optionnels (hors audit bloquant) : KPI reliés · Templates I/O · Contraintes et références (si source externe) -->
```

## Ordre des sections (pourquoi)

Contraintes/triggers/garde-fous **en tête** (primacy), workflow au milieu, exemples après le contrat, garde-fous rappelés **en fin** (recency) — recommandations 2026 sur l'attention des modèles.

## Migration

`python3 outils/migrate_template.py` (audit) / `--fix` (insère les placeholders) / `--rapport …` — rapport actuel : `migration-v2.md` (1000 skills à migrer, 7 sections manquantes partout).

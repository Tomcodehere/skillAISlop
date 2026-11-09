# skillAISlop — skillAISlop (skillAISlop)

Export du projet skillAISlop (Vibe Work, 2026-11-01 ; vagues 10-22 du 2026-11-02 au 2026-11-08) : **2001 sections** (2000 skills + routeur 0, numérotées 0-2000) organisées en **30 domaines**, avec catalogue, routeur SQL et outils d'audit.

## Installation rapide & branchement sur ton agent

```bash
python3 outils/routage.py build        # ~2 s, une seule fois (skills.db est gitignoré)
python3 outils/routage.py route "ma demande"   # exit 0 = skill trouvée, 1 = piste, 2 = rien
```
Prérequis : Python 3.12+ (stdlib seule suffit). Optionnel mais recommandé : `pip install sqlite-vec` (voie vectorielle ; sinon repli gracieux FTS5 seul).

**⭐ À ajouter dans le SKILL.md / AGENTS.md / .cursorrules de ton projet hôte** (pour que l'agent pense à consulter le routeur) :

```markdown
## skillAISlop — routeur de skills
Avant de choisir une skill toi-même, lance le routeur :
`python3 <chemin-vers-ce-dépôt>/outils/routage.py route "<demande de l'utilisateur>"`
- exit 0 → skill trouvée : lire `skills/NNN-*.md` correspondant et appliquer sa méthode
- exit 1 → piste affichée, à confirmer
- exit 2 → aucune skill : répondre en direct (`misses --suggest` si la demande revient souvent)
```

Alternative standard Agent Skills (sans routeur) : `python3 outils/routage.py skillmd --sortie agent-skills` génère 1600 dossiers `SKILL.md` + `skills.json`, installables via `npx skills add ./agent-skills` (ou copie dans `.agent/skills/`).

Pour un **pack autonome** distribuable à d'autres projets : `data/skillaislop-pack.zip` (dézipper, `python3 routage.py build --from-skills`, même ligne à ajouter avec `python3 routage.py route "..."`).

## Structure

| Chemin | Contenu |
|---|---|
| `skills/` | 2001 fichiers `.md` (une skill = un fichier, frontmatter YAML avec `date_ajout: "YYYY-MM"`) |
| `catalogue/` | sommaire, règles R1-R11, template, utilisation, sources, vue d'ensemble |
| `outils/` | `routage.py` (routeur SQL hybride FTS5 + sqlite-vec, repli gracieux si l'extension est absente), `audit_conformite.py` |
| `data/` | catalogues JSON (compact/complet/condensé) + `sonde-rapport.md` (rapport de couverture) — `catalogue-condensed.json` = index machine léger (resume + méthode + garde-fous), embarqué dans le pack |
| `canvas/` | 7 canvases d'origine (corpus, blocs de 300) |
| `AGENTS.md` / `TODO.md` / `DONE.md` | instructions agents / suivi |

## Patchs de cette branche (`vibe/fix-routeur-iot-sonde`)

1. **Correctif faux positif « IoT »** (`outils/routage.py`) : la voie mot-clé acceptait une inclusion dès 3 lettres, donc « iot » matchait « bibliothécaire » → skills 150/250. Seuil relevé à **5 lettres**.
2. **Sous-commande `sonde`** : batterie rejouable générée depuis la base (R8) → rapport couverts/partiels/gaps :
   ```
   python3 outils/routage.py build
   python3 outils/routage.py sonde --fichier data/sonde-rapport.md
   ```

## Vérifications

- `build` ✅ (2000 skills + routeur · 30 domaines · 3222 synonymes · 2001 vecteurs sqlite-vec)
- `test` ✅ **1849/1849**
- `lint` ✅ aucun problème (+ `date_ajout` YYYY-MM vérifié sur 2001/2001 skills, R13 titre sans année, R14 frontmatter sans < >)
- `golden` ✅ **198/198** requêtes stables
- `route "IoT"` → exit 2 (faux positif corrigé) ✅
- `route "domotique"` → skill 222 ✅
- `sonde` → **2400/2400 couverts (100 %), 0 partiel, 0 gap** ✅
- `audit_conformite` ✅ **2000/2000 conformes (100 %)** (8 canvases) · `score_skills` moyenne **100,0/100** · `evals` **1848/1848** (1167 skills)

## Mes skills perso (`mesSkillsPerso/`)

Dépose tes propres fichiers `.md` dans `mesSkillsPerso/` : ils **restent dans ce
dossier**, ne sont **jamais écrasés à l'upgrade** (le pack n'embarque que le
README du dossier), sont **convertis automatiquement au format TEMPLATE-v2**
(frontmatter + `date_ajout: "YYYY-MM"` + 12 sections) au prochain `build`, et
vivent dans leur **propre table** `skills_perso` de `skills.db`. Au routage, ils
sont **prioritaires** sur le catalogue dès qu'ils cadrent avec la demande
(`⭐ Perso Pn · mesSkillsPerso/<fichier>`, exit 0).

```bash
python3 outils/routage.py perso --add ma-skill.md   # copie dans mesSkillsPerso/
python3 outils/routage.py build                      # conversion auto + ingestion
python3 outils/routage.py perso                      # liste (P1, P2…)
python3 outils/routage.py route "perso 2"           # renvoi direct
python3 outils/routage.py route "ma demande"         # ⭐ Perso prioritaire si ça cadre
```

Doc complète : [documentations/skillsdocs/SKILLS-PERSO.md](documentations/skillsdocs/SKILLS-PERSO.md).

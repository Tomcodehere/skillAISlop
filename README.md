# skillAISlop — skillAISlop (skillAISlop)

Export du projet skillAISlop (Vibe Work, 2026-11-01 ; vagues 10-18 du 2026-11-02 au 2026-11-07) : **1700 sections** (1699 skills + routeur 0, numérotées 0-1699) organisées en **29 domaines**, avec catalogue, routeur SQL et outils d'audit.

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
| `skills/` | 1700 fichiers `.md` (une skill = un fichier, frontmatter YAML) |
| `catalogue/` | sommaire, règles R1-R11, template, utilisation, sources, vue d'ensemble |
| `outils/` | `routage.py` (routeur SQL hybride FTS5 + sqlite-vec, repli gracieux si l'extension est absente), `audit_conformite.py` |
| `data/` | catalogues JSON + `sonde-rapport.md` (rapport de couverture) |
| `canvas/` | 4 canvases d'origine (corpus) |
| `AGENTS.md` / `TODO.md` / `DONE.md` | instructions agents / suivi |

## Patchs de cette branche (`vibe/fix-routeur-iot-sonde`)

1. **Correctif faux positif « IoT »** (`outils/routage.py`) : la voie mot-clé acceptait une inclusion dès 3 lettres, donc « iot » matchait « bibliothécaire » → skills 150/250. Seuil relevé à **5 lettres**.
2. **Sous-commande `sonde`** : batterie rejouable générée depuis la base (R8) → rapport couverts/partiels/gaps :
   ```
   python3 outils/routage.py build
   python3 outils/routage.py sonde --fichier data/sonde-rapport.md
   ```

## Vérifications

- `build` ✅ (1699 skills + routeur · 29 domaines · 2298 synonymes · 1700 vecteurs sqlite-vec)
- `test` ✅ **449/449**
- `lint` ✅ aucun problème
- `route "IoT"` → exit 2 (faux positif corrigé) ✅
- `route "domotique"` → skill 222 ✅
- `sonde` → **1058/1058 couverts (100 %), 0 partiel, 0 gap** ✅

# skillAISlop — skillAISlop (skillAISlop)

Export du projet skillAISlop (Vibe Work, 2026-11-01 ; vagues 10-16 du 2026-11-02 au 2026-11-07) : **1500 sections** (1499 skills + routeur 0, numérotées 0-1499) organisées en **28 domaines**, avec catalogue, routeur SQL et outils d'audit.

## Structure

| Chemin | Contenu |
|---|---|
| `skills/` | 1500 fichiers `.md` (une skill = un fichier, frontmatter YAML) |
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

- `build` ✅ (1499 skills + routeur · 28 domaines · 1697 synonymes · 1500 vecteurs sqlite-vec)
- `test` ✅ **449/449**
- `lint` ✅ aucun problème
- `route "IoT"` → exit 2 (faux positif corrigé) ✅
- `route "domotique"` → skill 222 ✅
- `sonde` → **1058/1058 couverts (100 %), 0 partiel, 0 gap** ✅

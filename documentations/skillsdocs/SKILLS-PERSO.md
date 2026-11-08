# SKILLS-PERSO — tes skills perso (`mesSkillsPerso/`)

> Doc générée/maintenue avec le projet. Le dossier `mesSkillsPerso/` vit **à la racine du dépôt** (et **à côté de `routage.py` dans le pack**).

## Principe

Tu peux ajouter **toi-même** tes propres skills dans le dossier `mesSkillsPerso/`
(n'importe quel fichier `.md` : un SKILL.md, un mémo, un prompt réutilisable) :

| Garantie | Détail |
|---|---|
| **Tes fichiers restent là** | Jamais déplacés, jamais renommés, jamais supprimés par le projet |
| **Jamais écrasés à l'upgrade** | Le pack n'embarque **que** `mesSkillsPerso/README.md` — tes fichiers ne sont pas dans le zip, une mise à jour ne peut pas les toucher |
| **Prioritaires au routage** | Si une skill perso **cadrage** avec la demande, elle gagne sur tout le catalogue : `⭐ Perso Pn · … · mesSkillsPerso/<fichier>` (exit 0) |
| **Table dédiée** | `skills_perso` (+ `perso_fts`, `perso_synonymes`, `perso_mots_cles`) dans `skills.db` — séparée du catalogue |
| **Format template automatique** | Au prochain `build`, chaque fichier est **converti en place** au format TEMPLATE-v2 (frontmatter YAML + les 12 sections), ton contenu est conservé et réparti dans les sections |

## Ajouter une skill perso

```bash
# 1) déposer le fichier (ou utiliser la commande qui copie + documente)
python3 outils/routage.py perso --add mon-fichier.md
# ou simplement : cp mon-fichier.md mesSkillsPerso/

# 2) build : conversion auto au template + ingestion dans skills_perso
python3 outils/routage.py build

# 3) lister
python3 outils/routage.py perso
# ⭐ 1 skill(s) perso (prioritaires au routage) dans mesSkillsPerso/ :
#   P1 · Rapport hebdo d'équipe · [Perso] · mon-fichier.md · date_ajout 2026-11
```

Commandes :

| Commande | Effet |
|---|---|
| `python3 outils/routage.py perso` | liste les skills perso (P1, P2…) depuis `skills_perso` |
| `python3 outils/routage.py perso --add <fichier.md>` | copie le fichier dans `mesSkillsPerso/` (le dossier + README sont créés si besoin) |
| `python3 outils/routage.py perso --convert` | (re)convertit **tous** les fichiers du dossier au template, en place |
| `python3 outils/routage.py route "perso 2"` | renvoi direct vers la perso n°2 |
| `python3 outils/routage.py route "<demande>" --json` | la clé JSON `perso` contient les candidates perso |

## Conversion automatique au template

Un fichier perso est considéré « au template » s'il a un frontmatter avec
`num:` + `date_ajout: "YYYY-MM"` **et** les 12 sections TEMPLATE-v2. Sinon,
`build` le réécrit **en place** (même nom de fichier) :

- **frontmatter généré** : `num` (séquence perso P1, P2… stable), `date_ajout`
  (YYYY-MM auto, conservée si déjà présente), `nom` (titre `#` du fichier ou
  champ existant), `emoji` 🎯 par défaut, `domaine: "Perso"` par défaut,
  `signal` (champ `signal`/`description`, sinon 1ᵉ paragraphe, tronqué à
  1024 car., sans `< > "`), `mot_cle` (tokens du nom), `nom_court`,
  `branche: "K"`, `synonymes`, `tags: ["perso"]`
- **corps** : tes titres `## …` sont mappés sur les 12 sections
  (Objectif, Triggers, Hors périmètre, Garde-fous, Instructions système,
  Inputs, Méthode, Sorties, Exemple, Cas d'usage, QA, DoD) ; les sections
  manquantes reçoivent un contenu par défaut dérivé de ton texte ; rien n'est
  perdu (le contenu non mappé part dans « Instructions système »)

Tu peux aussi écrire **directement** au format TEMPLATE-v2 (voir
[TEMPLATE-v2.md](TEMPLATE-v2.md)) : le fichier est alors laissé tel quel
(sauf `date_ajout` ajoutée si absente).

## Routage : priorité perso

La cascade de `route` commence par la voie **perso** (avant mot-clé, synonyme,
FTS, vec, flou du catalogue) :

1. `perso N` dans la demande → renvoi direct `⭐ Perso PN`
2. mot-clé perso (égalité / inclusion / recouvrement de tokens ≥ 5 lettres)
3. synonyme perso (idem)
4. FTS5 sur `perso_fts` (AND puis OR validé : ≥ 2 tokens réels, ou 1 mot complet)

Si **au moins une** skill perso cadrage → elle est le gagnant (exit 0), les
candidats catalogue restent affichés en dessous pour information. Sinon, le
routage catalogue habituel s'applique (exit 0/1/2 inchangé).

Exemple :

```
$ python3 routage.py route "rédige le rapport hebdo de l'équipe projet Phoenix"
⭐ Perso P1 · Rapport hebdo d'équipe · [Perso] · mesSkillsPerso/ma-skill.md
  ↳ perso mot-clé « rapport hebdo equipe » — signal : Génère le rapport hebdo…
⤳ Section : mesSkillsPerso/ma-skill.md        (exit 0)
```

## Branchement agent (SKILL.md / AGENTS.md du projet hôte)

Ajoute dans le SKILL.md/AGENTS.md du projet hôte (le routeur gère déjà les perso) :

```markdown
## skillAISlop — routeur de skills (avec mes skills perso)
Avant de choisir une skill toi-même, lance le routeur :
`python3 <chemin>/routage.py route "<demande>"`
- exit 0 → lire la skill indiquée : `skills/NNN-*.md` **ou** `mesSkillsPerso/<fichier>` si ⭐ Perso (prioritaire)
- exit 1 → piste affichée, à confirmer
- exit 2 → aucune skill : répondre en direct
```

## Limites & FAQ

- **Les skills perso ne sont jamais dans le pack** (`pack` n'embarque que
  `mesSkillsPerso/README.md`) : elles restent locales au projet, `pack --check`
  ne les compare pas (elles ne participent pas au hash du catalogue).
- Numérotation perso indépendante : `P1, P2…` (table `skills_perso`), affichée
  `⭐ Perso Pn` pour ne pas confondre avec les skills catalogue `0-1799`.
- `lint` contrôle aussi les fichiers perso : `date_ajout` YYYY-MM valide,
  pas de `<`/`>` dans le frontmatter, `mot_cle` non vide.
- `test` / `golden` / `evals` ne portent que sur le catalogue (les tests sont
  embarqués dans `routage.py`) : une skill perso ne peut pas casser la
  non-régression du catalogue.
- Supprimer une skill perso = supprimer son fichier dans `mesSkillsPerso/` puis
  `build` (la table est reconstruite à chaque build ; le fichier n'est jamais
  touché automatiquement).
- Plusieurs dossiers : dans le dépôt, `mesSkillsPerso/` à la racine ; dans le
  pack extrait, `mesSkillsPerso/` à côté de `routage.py`. Les deux emplacements
  sont détectés automatiquement.

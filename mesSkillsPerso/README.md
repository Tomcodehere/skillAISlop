# mesSkillsPerso — tes skills perso

Dépose ici tes propres fichiers `.md` (SKILL.md ou n'importe quel markdown) :
ils restent dans ce dossier, ne sont **jamais écrasés ni supprimés** par une
mise à jour du pack/catalogue, et sont **prioritaires** au routage dès qu'ils
cadrent avec la demande de l'utilisateur.

Au prochain `python3 routage.py build` (ou `perso --add` + build), chaque fichier
est automatiquement converti au format du template (TEMPLATE-v2 : frontmatter
YAML + 12 sections) et ingéré dans sa propre table `skills_perso` de skills.db.

- `python3 routage.py perso`                -> liste tes skills perso (P1, P2...)
- `python3 routage.py perso --add ma-skill.md` -> copie + convertit dans ce dossier
- `python3 routage.py perso --convert`      -> (re)convertit tous les fichiers du dossier
- `python3 routage.py route "..."`          -> une skill perso gagnante s'affiche ⭐ Perso Pn
- `python3 routage.py route "perso 2"`      -> renvoi direct vers la perso n°2

Les skills perso ne sont jamais exportées dans le pack (elles restent locales).

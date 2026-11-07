# AGENTS.md — skillAISlop

> 🔎 **Index** : Contexte du projet · Environnement & livrables · Ajout d'une skill · Synchronisation index & routage · Audit & conformité · Mise à jour trimestrielle · Concision des sorties · Suivi des tâches TODO/DONE · Zéro sujet New Âge · Sources

Fichier d'instructions pour tout agent IA intervenant sur la **skillAISlop**, au format ouvert [AGENTS.md](https://github.com/agentsmd/agents.md) — un « README pour agents » : l'endroit prévisible où un agent trouve le contexte et les instructions nécessaires pour travailler sur ce projet.

## Contexte du projet

- La bibliothèque est un catalogue de **899 skills numérotées (0-899)** prêtes à l'emploi avec un assistant IA : la skill 0 est un routeur, les skills 1-899 sont classées par famille (rédaction, dev, data, agents IA, création visuelle & audio, marketing, vente, finance, gouvernance, RH, vie quotidienne, sécurité, quotidien & business).
- Le catalogue vit dans le canvas **« skillAISlop »**, **découpé en corpus** pour respecter le plafond de taille d'un canvas (1 024 000 octets) : le canvas principal porte sommaire, règles, template, skill 0 (carte des domaines, index inversé, table de routage, arbre décisionnel) et sections transverses ; les sections détaillées vivent dans les canvases **« corpus-skills-1-300 »**, **« corpus-skills-301-600 »** et **« corpus-skills-601-900 »**. Le script d'audit dans le canvas **« script-conformite-skills »** ; les règles durables (R1-R11) dans le règlement du catalogue et dans le Knowledge **skillaislop**.
- Chaque skill suit le **template officiel** : `## N. <emoji> <Nom>` · `> 🔎 Index` · `**Objectif** :` · `**Instructions système** :` (commencent par « Tu es ») · `**Méthode** :` (3 étapes numérotées) · `**Exemple de prompt** :` (guillemets « ») · `**Cas d'usage** :` (≥ 2 usages) · cross-refs vers d'autres skills.

## Environnement & livrables

- Toute modification du catalogue passe par le canvas principal et les canvases corpus — ne jamais dupliquer le catalogue ailleurs.
- Le **sommaire global** (canvas principal) est l'unique source de vérité pour les numéros de skill.
- Toute nouvelle skill est numérotée séquentiellement après la 899 et ne change plus de numéro ensuite ; sa section détaillée (corps R2) est ajoutée au canvas corpus couvrant son numéro (1-300, 301-600, 601-900).
- **Export JSON & compteur** : le canvas « Export JSON — skillAISlop » est un instantané machine-readable du catalogue (mode **compact** par défaut : index et métadonnées de routage ; `--complet` pour le texte intégral), le canvas « totalSkillsCount » le compteur officiel. **À chaque ajout ou suppression de skill**, les régénérer (reconstruire `routage.py` depuis le canvas « Routage SQL Skills », puis `python3 routage.py export --fichier <chemin>/catalogue.json` et `python3 routage.py count`) et recopier les résultats dans les deux canvases. Le dossier `/export` de session est éphémère ; seuls les canvases sont permanents.

## Synchronisation index & routage (R8)

- À **chaque modification** du catalogue (ajout, édition, renommage, retrait), l'index et le routage sont mis à jour **automatiquement et immédiatement** : `skills.db` (source de vérité du routage — reconstruite par `routage.py build` depuis le canvas code « routage-sql-skills », qui porte aussi `route` : recherche rapide, et `generate` : régénération des sections ; la base ne survit pas aux resets d'environnement, le canvas oui), sommaire, table de routage (bloc du domaine), carte des domaines, index inversé (mot-clé canonique de la nouvelle skill), arbre de décision, vue d'ensemble, index du document.
- Aucune entrée ne peut être manquante, orpheline ou en double : une ligne d'index sans skill, une skill sans ligne de routage ou un renvoi d'arbre vers une skill inexistante sont des non-conformités bloquantes.
- **À chaque ajout ou retrait de skill** : régénérer le compteur (`routage.py count`) et l'export JSON (`routage.py export`), et actualiser leurs canvases (« totalSkillsCount », « Export JSON — skillAISlop ») — la modification n'est pas terminée sinon.
- Une modification n'est **pas terminée** tant que le script de conformité n'a pas confirmé la synchronisation (code de sortie 0).

## Concision des sorties (R9)

- Rapports d'audit compacts par défaut : verdict en une ligne, seules les non-conformités détaillées (`--verbose` pour la table complète).
- Réponses et consignations : l'essentiel d'abord ; le détail sur demande ou en cas d'écart.

## Suivi des tâches TODO/DONE (R10)

- Toutes les choses à faire du projet vivent dans le canvas « TODO — skillAISlop » ; les tâches terminées dans le canvas « DONE — skillAISlop ». Ces deux canvases sont **permanents** (ils survivent aux resets d'environnement) — jamais de TODO/DONE dans des fichiers de session.
- **Automatique à chaque écriture** : dès qu'une tâche est terminée — sans demande explicite — la retirer du canvas TODO et l'ajouter en tête du canvas DONE avec sa date. Une tâche n'est pas terminée tant que les deux canvases ne reflètent pas son état.

## Zéro sujet New Âge (R11)

- **Aucun sujet New Âge dans le catalogue, jamais** : méditation, pleine conscience, astrologie, tarot, voyance, manifestation, cristaux, reiki, numérologie, spiritualité, affirmations positives, horoscope… — exclusion définitive, même si demandés.
- Ces sujets ne deviennent jamais des skills ni des items TODO ; les demandes utilisateurs sur ces thèmes reçoivent une réponse en direct, hors catalogue.
- Le bien-être factuel (stress, anxiété, sommeil) reste admissible tant qu'il reste laïque et fondé sur des méthodes éprouvées.

## Ajout d'une skill

- Vérifier d'abord le **zéro doublon** (R6) : noms, signaux de routage, périmètre — l'emoji doit être pertinent, sa réutilisation entre skills est permise. Si le besoin est couvert, **enrichir la skill existante** plutôt que créer ; consigner les candidats écartés.
- Rédiger la skill selon le template officiel, à l'identique : mêmes sections, même ordre, mêmes libellés.
- Brancher le routage complet (R3) : une ligne dans le **sommaire** (`| N | Nom | Domaine |`), une ligne dans la **table de routage** de la skill 0 (`| signal | N | Domaine |`, dans le bloc du domaine concerné, la table étant regroupée par domaine), une entrée dans l'**arbre de décision** (branche D1-D30 adaptée), et une branche dans la **vue d'ensemble** si nouvelle famille. Voie outillée recommandée : insérer la ligne dans `skills.db` (table `skills` : num, nom, domaine, signal, mot_cle, branche, nom_court — unicité R6 à vérifier d'abord), lancer `routage.py generate` (script du canvas « routage-sql-skills ») qui régénère sommaire, carte, index, table et arbre, puis ajouter la section de la skill (corps R2) dans le canvas corpus couvrant son numéro avant de repasser l'audit. Un faux négatif de routage (`routage.py route` → exit 2) se corrige en ajoutant un synonyme dans la liste SYNONYMES du canvas « routage-sql-skills », suivi de `routage.py build` Les exit 2 sont consignés automatiquement au journal (`routage.py misses`, tri par récurrence — `--clear` pour vider) et, sur exit 2, le routeur affiche des pistes approx en clair ; `routage.py misses --suggest` rédige pour chaque entrée la ligne de synonyme proposée (meilleur recouvrement de trigrammes) — à valider avant intégration (R6 : le synonyme doit être pertinent, pas seulement proche). Après toute modification du routeur, des synonymes ou du catalogue, repasser `routage.py lint` (qualité des synonymes et tests) puis `routage.py test` (non-régression : demandes → skill attendue, corpus TESTS_ROUTAGE dans le même canvas) ; `routage.py stats` donne l'observabilité du routage de la session et `routage.py bench` re-mesure les gains après chaque évolution du routeur.
- Ajouter au moins une cross-référence vers une skill complémentaire (R4).
- **Régénérer le compteur** (`routage.py count`) **et l'export JSON** (`routage.py export`), puis actualiser leurs canvases — **obligatoire à chaque ajout ou suppression de skill**.
- Mettre à jour l'index du document si une nouvelle section `##` apparaît (R1).

## Audit & conformité

- Après chaque ajout de règle ou vague de skills, exécuter le **script de conformité** (canvas « script-conformite-skills ») sur les **quatre fichiers** — canvas principal puis les trois corpus (`check_conformite.py <principal> <corpus-1-300> <corpus-301-600> <corpus-601-900>`) — et consigner le verdict dans la conversation (R5).
- Contrôles par skill : index présent (R1) ; objectif non vide, « Tu es », ≥ 3 étapes numérotées, exemple entre guillemets, ≥ 2 cas d'usage (R2) ; sommaire + table de routage + arbre (R3) ; ≥ 1 cross-ref dans les bornes 0-899 (R4).
- Contrôles R6 : unicité des noms et des signaux de routage sur l'ensemble du catalogue ; emoji présent et pertinent par skill (réutilisations permises).
- Une règle fraîchement ajoutée n'est active qu'une fois l'audit repassé ; corriger toute non-conformité avant toute autre évolution.

## Mise à jour trimestrielle (R7)

- La bibliothèque se met à jour **4 fois par an : janvier, avril, juillet, octobre**, sur la base du modèle [AGENTS.md](https://github.com/agentsmd/agents.md) lié et des sources d'inspiration du catalogue.
- Cycle à chaque trimestre :
  1. **Veille** : rechercher les nouvelles compétences IA du trimestre (sources : [DataCamp — Top Agent Skills](https://www.datacamp.com/fr/blog/top-agent-skills), [Lessie — Best Claude Skills](https://lessie.ai/fr/blog/best-claude-skills), dépôts awesome-claude-skills, annonces Anthropic/OpenAI…).
  2. **Dédoublonnage** : confronter chaque candidat au catalogue selon R6 ; enrichir ou écarter.
  3. **Intégration** : template (R2) + routage complet (R3) + cross-refs (R4).
  4. **Audit intégral** : repasser le script de conformité sur les 899 skills et consigner le verdict (R5).
  5. **Conservation** : mettre à jour le Knowledge skillaislop (compteur de skills, vagues, dates de mise à jour).
- La **skill 250 (Conservateur)** pilote ce cycle ; une tâche planifiée trimestrielle le déclenche.

## Sources

- [AGENTS.md — format ouvert](https://github.com/agentsmd/agents.md) — modèle de référence de ce fichier
- Section « Sources d'inspiration » du catalogue — vagues 1 à 4 et sources web liées
## Layout du dépôt (import Vibe Code)

> **Règle** : toute ligne ajoutée à ce fichier va dans cette section (documentation d'installation), jamais ailleurs.

Ce dépôt est l'export du projet skillAISlop depuis Vibe Work ; le canvas principal y est éclaté en fichiers :

- `skills/` — **une skill = un fichier** (`NNN-slug.md`, frontmatter YAML : num, nom, emoji, domaine, signal, mot_cle, nom_court, branche, synonymes, cross_refs + corps intégral) ;
- `catalogue/` — sommaire, règles (R1-R11), template, guide d'utilisation, sources, vue d'ensemble ;
- `canvas/` — copies verbatim des 4 canvases Work (provenance ; ce sont les sources des scripts) ;
- `outils/routage.py` — routeur SQL hybride (build, route, generate, export, count, lint, test, misses, stats, bench, sonde, vocab, versions, analytics), chemins relatifs au dépôt. La base `skills.db` (reconstruite par `build`, ignorée par git) embarque : `skills` (+ index `domaine`/`branche`), `domaines`, `synonymes`, `skills_fts` (FTS5 + triggers, bm25 pondéré), `skills_vec` (sqlite-vec vec0, cosinus, dim 128, embeddings locaux `embed_hash` sans dépendance externe, repli gracieux si l'extension est absente), `trigrammes` (WITHOUT ROWID, passe floue en SQL), `skills_fts_vocab`, `meta`/`versions` (snapshot JSON + diff par build), `routes`/`non_routees` (journal de session). Pragmas : WAL, cache_size=-8000, optimize + VACUUM en fin de build. Dépendance CI : `pip install sqlite-vec`.
  - **Cascade de `route`** : direct « skill N » → mot-clé → synonyme → FTS5 → sqlite-vec (cosinus ≥ 0,80) → trigrammes SQL → domaines. Chaque candidate porte sa **voie** et son **score** ; exit 0 = prendre la première candidate (voie la plus forte), exit 1 = piste/domaine à confirmer, exit 2 = consulter `misses --suggest` avant de répondre en direct.
- `.github/workflows/ci.yml` — CI sur chaque PR (build, generate --check, lint, test, audit, sonde, compteur, vocab, versions, pack --check) ;
- **Export multi-projets** : `routage.py pack` produit `data/skillaislop-pack.zip` (skills/*.md + routage.py + manifeste.json avec hash + README) ; un projet tiers fait `pip install sqlite-vec && python3 routage.py build --from-skills && python3 routage.py route "<demande>"` ; fidélité vérifiée par `routage.py pack --check` (rebuild depuis le pack, compare les tables + hash) ;
- **Interop Agent Skills** : `routage.py skillmd` génère `data/agent-skills/<NNN-slug>/SKILL.md` (frontmatter standard `name`/`description` + metadata) depuis chaque `skills/NNN-*.md`, installables via `npx skills add` dans Claude Code/Codex/Cursor ;
- **API locale** : `routage.py serve [--port 8765]` démarre une mini API **loopback uniquement** (`127.0.0.1`, bind non-loopback refusé) : `GET /health`, `GET /route?q=<demande>&top=3` (exit 0/1/2 + candidats avec voie/score), `GET /skills`, `GET /export.json` ; version sémantique du catalogue dans `meta` (`CATALOGUE_VERSION`, ex. 12.0.0) affichée par `versions` et embarquée dans le manifeste du pack ;
- `outils/audit_conformite.py (R1-R8 oui/non) et score_skills.py (score /100 + suffisance de contenu par section) ; routage : bonus cross-ref au classement, tags optionnels (route --tag), vec dim 64, fusion RRF k=60 des voies, bonus cross-ref/popularité/freshness, contextual enrichment des embeddings, commande top, evals par skill (commande evals), depends_on (skills composables, 906 chaînes auto par similarité via outils/enrichir_xrefs.py) + cross-refs complétées partout (1699/1700), noms kebab-case ≤ 64` — audit R1-R8 multi-fichiers (`python3 outils/audit_conformite.py (R1-R8 oui/non) et score_skills.py (score /100 + suffisance de contenu par section) ; routage : bonus cross-ref au classement, tags optionnels (route --tag), vec dim 64, fusion RRF k=60 des voies, bonus cross-ref/popularité/freshness, contextual enrichment des embeddings, commande top, evals par skill (commande evals), depends_on (skills composables, 906 chaînes auto par similarité via outils/enrichir_xrefs.py) + cross-refs complétées partout (1699/1700), noms kebab-case ≤ 64 canvas/*.md`) ;
- `data/` — export JSON compact et complet, compteur de skills.

Après toute modification : `python3 outils/routage.py build && python3 outils/routage.py generate --check && python3 outils/routage.py lint && python3 outils/routage.py test`, puis `python3 outils/audit_conformite.py (R1-R8 oui/non) et score_skills.py (score /100 + suffisance de contenu par section) ; routage : bonus cross-ref au classement, tags optionnels (route --tag), vec dim 64, fusion RRF k=60 des voies, bonus cross-ref/popularité/freshness, contextual enrichment des embeddings, commande top, evals par skill (commande evals), depends_on (skills composables, 906 chaînes auto par similarité via outils/enrichir_xrefs.py) + cross-refs complétées partout (1699/1700), noms kebab-case ≤ 64 canvas/bibliotheque-skills-ai.md canvas/corpus-skills-1-300.md canvas/corpus-skills-301-600.md canvas/corpus-skills-601-900.md`. La CI (`.github/workflows/ci.yml`) rejoue tout ça automatiquement sur chaque PR.

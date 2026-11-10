# AGENTS.md — skillAISlop

> 🔎 **Index** : Objectif · Quand l'utiliser (triggers) · Hors périmètre · Inputs requis · Sorties attendues · Workflow recommandé · Garde-fous · Template d'entrée · Template de sortie · Checklist QA interne · KPI reliés · Definition of done · Exemples d'usage · Contraintes et références

Fichier d'instructions pour tout agent IA intervenant sur la **skillAISlop**, au format ouvert AGENTS.md — un « README pour agents » : l'endroit prévisible où un agent trouve le contexte et les instructions nécessaires pour travailler sur ce projet. Structure conforme au **template standard 13 sections** (voir Contraintes et références).

## Objectif

Tenir à jour la bibliothèque **skillAISlop** : **1901 sections** (1900 skills numérotées 1-1900 + le routeur, skill 0, non compté) prêtes à l'emploi avec un assistant IA, classées en **29 domaines** (rédaction, dev, data, agents IA, création visuelle & audio, marketing, vente, finance, gouvernance, RH, vie quotidienne, sécurité, Game Dev, artisanat & loisirs créatifs, quotidien & business). Le catalogue vit dans le canvas **« skillAISlop »**, découpé en corpus pour respecter le plafond de taille d'un canvas (1 024 000 octets) : le canvas principal porte sommaire, règles, template, skill 0 (carte des domaines, index inversé, table de routage, arbre décisionnel) et sections transverses ; les sections détaillées vivent dans les 7 canvases **corpus-skills-1-300**, **301-600**, **601-900**, **901-1200**, **1201-1500**, **1501-1800**, **1801-2100**. Le script d'audit vit dans le canvas **« script-conformite-skills »** ; les règles durables (R1-R11) dans le règlement du catalogue (`catalogue/regles.md`). Chaque skill suit le **template officiel** : `## N. <emoji> <Nom>` · `> 🔎 Index` · `**Objectif** :` · `**Instructions système** :` (commencent par « Tu es ») · `**Méthode** :` (3 étapes numérotées) · `**Exemple de prompt** :` (guillemets « ») · `**Cas d'usage** :` (≥ 2 usages) · cross-refs vers d'autres skills.

## Quand l'utiliser (triggers)

- Avant **toute modification du catalogue** (ajout, édition, renommage, retrait d'une skill).
- Avant de choisir une skill soi-même : lancer le routeur `python3 outils/routage.py route "<demande>"` (exit 0 = skill trouvée, 1 = piste, 2 = rien).
- À chaque vague de skills, chaque ajout de règle, chaque mise à jour trimestrielle (R7).
- Après toute modification du routeur, des synonymes ou du catalogue : repasser les vérifications obligatoires.
- Pour consigner une tâche terminée (R10) ou lire la feuille de route (`TODO.md`).

## Hors périmètre

- ❌ **Zéro sujet New Âge (R11)** : aucun sujet New Âge dans le catalogue, jamais — méditation, pleine conscience, astrologie, tarot, voyance, manifestation, cristaux, reiki, numérologie, spiritualité, affirmations positives, horoscope… — exclusion définitive, même si demandés. Ces sujets ne deviennent jamais des skills ni des items TODO ; les demandes utilisateurs sur ces thèmes reçoivent une réponse en direct, hors catalogue. Le bien-être factuel (stress, anxiété, sommeil) reste admissible tant qu'il reste laïque et fondé sur des méthodes éprouvées.
- ❌ Ne jamais dupliquer le catalogue ailleurs que dans le canvas principal et les canvases corpus.
- ❌ Ne jamais éditer `skills.db` à la main : la base ne survit pas aux resets d'environnement, elle est reconstruite par `routage.py build` depuis le canvas code « routage-sql-skills ».

## Inputs requis

- `skills/` — **une skill = un fichier** (`NNN-slug.md`, frontmatter YAML : num, nom, emoji, domaine, signal, mot_cle, nom_court, branche, synonymes, cross_refs, `date_ajout: "YYYY-MM"` + corps intégral).
- `catalogue/` — sommaire (unique source de vérité pour les numéros de skill), règles R1-R11, template, guide d'utilisation, sources, vue d'ensemble.
- `canvas/` — copies verbatim des 8 canvases Work (provenance ; ce sont les sources des scripts).
- `outils/routage.py` — routeur SQL hybride (build, route, generate, export, count, lint, test, golden, misses, stats, bench, sonde, vocab, versions, analytics, pack, skillmd, serve, perso, top, evals, todo, done) ; `outils/audit_conformite.py` ; `outils/score_skills.py` ; `outils/gen_docs.py`.
- `data/` — exports JSON compact et complet, compteur de skills, sonde-rapport.md.
- `.github/workflows/ci.yml` — CI sur chaque PR (build, generate --check, lint, test, golden, audit, evals, score, sonde, vocab, compteur, versions, pack --check).
- `TODO.md` / `DONE.md` — suivi des tâches, permanents (survivent aux resets d'environnement) ; jamais de TODO/DONE dans des fichiers de session.
- Le dossier `/export` de session est éphémère ; seuls les canvases sont permanents.
- Toute nouvelle skill est numérotée séquentiellement après la 1900 et ne change plus de numéro ensuite ; sa section détaillée (corps R2) est ajoutée au canvas corpus couvrant son numéro.

### Layout du dépôt (import Vibe Code)

> **Règle** : toute ligne ajoutée à ce fichier va dans cette sous-section (documentation d'installation), jamais ailleurs.

Ce dépôt est l'export du projet skillAISlop depuis Vibe Work ; le canvas principal y est éclaté en fichiers :

- `skills/` — **une skill = un fichier** (`NNN-slug.md`, frontmatter YAML : num, nom, emoji, domaine, signal, mot_cle, nom_court, branche, synonymes, cross_refs + corps intégral) ;
- `catalogue/` — sommaire, règles (R1-R11), template, guide d'utilisation, sources, vue d'ensemble ;
- `canvas/` — copies verbatim des 8 canvases Work (provenance ; ce sont les sources des scripts) ;
- `outils/routage.py` — routeur SQL hybride (build, route, generate, export, count, lint, test, misses, stats, bench, sonde, vocab, versions, analytics), chemins relatifs au dépôt. La base `skills.db` (reconstruite par `build`, ignorée par git) embarque : `skills` (+ index `domaine`/`branche`), `domaines`, `synonymes`, `skills_fts` (FTS5 + triggers, bm25 pondéré), `skills_vec` (sqlite-vec vec0, cosinus, dim 64, embeddings locaux `embed_hash` sans dépendance externe, repli gracieux si l'extension est absente), `trigrammes` (WITHOUT ROWID, passe floue en SQL), `skills_fts_vocab`, `meta`/`versions` (snapshot JSON + diff par build), `routes`/`non_routees` (journal de session). Pragmas : WAL, cache_size=-8000, optimize + VACUUM en fin de build. Dépendance CI : `pip install sqlite-vec`.
  - **Cascade de `route`** : direct « skill N » → mot-clé → synonyme → FTS5 → sqlite-vec (cosinus ≥ seuil) → trigrammes SQL → domaines. Chaque candidate porte sa **voie** et son **score** ; exit 0 = prendre la première candidate (voie la plus forte), exit 1 = piste/domaine à confirmer, exit 2 = consulter `misses --suggest` avant de répondre en direct.
- `.github/workflows/ci.yml` — CI sur chaque PR (build, generate --check, lint, test, audit, sonde, compteur, vocab, versions, pack --check) ;
- **Export multi-projets** : `routage.py pack` produit `data/skillaislop-pack.zip` (skills/*.md + routage.py + manifeste.json avec hash + README) ; un projet tiers fait `pip install sqlite-vec && python3 routage.py build --from-skills && python3 routage.py route "<demande>"` ; fidélité vérifiée par `routage.py pack --check` (rebuild depuis le pack, compare les tables + hash) ;
- **Interop Agent Skills** : `routage.py skillmd` génère `data/agent-skills/<NNN-slug>/SKILL.md` (frontmatter standard `name`/`description` + metadata) depuis chaque `skills/NNN-*.md`, installables via `npx skills add` dans Claude Code/Codex/Cursor ;
- **API locale** : `routage.py serve [--port 8765]` démarre une mini API **loopback uniquement** (`127.0.0.1`, bind non-loopback refusé) : `GET /health`, `GET /route?q=<demande>&top=3` (exit 0/1/2 + candidats avec voie/score), `GET /skills`, `GET /export.json` ; version sémantique du catalogue dans `meta` (`CATALOGUE_VERSION`, ex. 20.0.0) affichée par `versions` et embarquée dans le manifeste du pack ;
- `outils/audit_conformite.py` (R1-R8 oui/non) et `outils/score_skills.py` (score /100 + suffisance de contenu par section) ; routage : bonus cross-ref au classement, tags optionnels (route --tag), fusion RRF k=60 des voies, bonus cross-ref/popularité/freshness, contextual enrichment des embeddings, commande top, evals par skill (commande evals), depends_on (skills composables, 906 chaînes auto par similarité via outils/enrichir_xrefs.py) + cross-refs complétées partout, noms kebab-case ≤ 64, champ `date_ajout: "YYYY-MM"` obligatoire dans le frontmatter (vérifié par lint + assert build --from-skills) ; **mesSkillsPerso/** : skills perso de l'utilisateur (jamais écrasées à l'upgrade, jamais dans le pack sauf README), converties auto au template au build, table dédiée `skills_perso`, voie prioritaire n°0b dans `chercher()`, commande `perso` (liste/--add/--convert) — doc : `documentations/skillsdocs/SKILLS-PERSO.md` ;
- `data/` — export JSON compact et complet, compteur de skills.

## Sorties attendues

- `skills.db` reconstruite par `routage.py build` + sommaire, carte des domaines, index inversé, table de routage, arbre de décision, vue d'ensemble **synchronisés** (R8).
- À chaque ajout ou retrait de skill : compteur (`routage.py count`) et export JSON (`routage.py export`) régénérés, canvases « totalSkillsCount » et « Export JSON — skillAISlop » actualisés — la modification n'est pas terminée sinon.
- Verdict de l'audit de conformité consigné (R5), **compact par défaut** (R9).
- `TODO.md` / `DONE.md` reflétant l'état réel des tâches (R10).
- Un commit par sujet ; `git diff --stat` + relecture avant chaque push (hook pre-push en place).

## Workflow recommandé

1. **Zéro doublon (R6)** : comparer noms, signaux de routage et périmètre au catalogue existant ; si le besoin est couvert, **enrichir la skill existante** plutôt que créer ; consigner les candidats écartés. Unicité des noms et des signaux de routage (un signal ne peut pas router vers deux skills distinctes pour le même besoin) ; emoji présent et pertinent (réutilisations permises).
2. **Rédaction** selon le template officiel, à l'identique : mêmes sections, même ordre, mêmes libellés.
3. **Routage complet (R3)** : une ligne dans le **sommaire** (`| N | Nom | Domaine |`), une ligne dans la **table de routage** de la skill 0 (`| signal | N | Domaine |`, dans le bloc du domaine concerné, la table étant regroupée par domaine), une entrée dans l'**arbre de décision** (branche D1-D30 adaptée), une branche dans la **vue d'ensemble** si nouvelle famille. Voie outillée recommandée : insérer la ligne dans `skills.db` (table `skills`), lancer `routage.py generate` qui régénère sommaire, carte, index, table et arbre, puis ajouter la section de la skill (corps R2) dans le canvas corpus couvrant son numéro avant de repasser l'audit.
4. **Faux négatif de routage** (`route` → exit 2) : ajouter un synonyme dans la liste SYNONYMES du canvas « routage-sql-skills », suivi de `routage.py build`. Les exit 2 sont consignés automatiquement au journal (`routage.py misses`, tri par récurrence — `--clear` pour vider) ; `routage.py misses --suggest` rédige pour chaque entrée la ligne de synonyme proposée (meilleur recouvrement de trigrammes) — **à valider avant intégration** (R6 : le synonyme doit être pertinent, pas seulement proche).
5. **Cross-refs (R4)** : au moins une cross-référence vers une skill complémentaire (bornes 0-1900) ; mettre à jour l'index du document si une nouvelle section `##` apparaît (R1).
6. **Régénération obligatoire** à chaque ajout/suppression de skill : compteur + export JSON + canvases associés.
7. **Vérifications** après toute modification du routeur, des synonymes ou du catalogue : `routage.py lint` (qualité des synonymes et tests) puis `routage.py test` (non-régression : demandes → skill attendue, corpus TESTS_ROUTAGE) ; `routage.py golden` (198 requêtes de régression) ; `routage.py stats` (observabilité de la session) ; `routage.py bench` (re-mesure après chaque évolution du routeur).
8. **Audit & conformité (R5)** : script de conformité du canvas « script-conformite-skills » sur le canvas principal puis les canvases corpus ; consigner le verdict dans la conversation. Contrôles par skill : index présent (R1) ; objectif non vide, « Tu es », ≥ 3 étapes numérotées, exemple entre guillemets, ≥ 2 cas d'usage (R2) ; sommaire + table de routage + arbre (R3) ; ≥ 1 cross-ref (R4). Corriger toute non-conformité **avant toute autre évolution** ; une règle fraîchement ajoutée n'est active qu'une fois l'audit repassé.
9. **Mise à jour trimestrielle (R7)** — janvier, avril, juillet, octobre : 1) **veille** des nouvelles compétences IA du trimestre (sources : DataCamp — Top Agent Skills, Lessie — Best Claude Skills, dépôts awesome-claude-skills, annonces Anthropic/OpenAI…) ; 2) **dédoublonnage** (chaque candidat confronté au catalogue selon R6 ; enrichir ou écarter) ; 3) **intégration** (template R2 + routage complet R3 + cross-refs R4) ; 4) **audit intégral** consigné (R5) ; 5) **conservation** (compteur de skills, vagues, dates de mise à jour). Piloté par la skill 250 (Conservateur) et une tâche planifiée trimestrielle.
10. **Après toute modification** : `python3 outils/routage.py build && python3 outils/routage.py generate --check && python3 outils/routage.py lint && python3 outils/routage.py test`.

## Garde-fous

- **R8** : aucune entrée manquante, orpheline ou en double — ce sont des non-conformités **bloquantes** (une ligne d'index sans skill, une skill sans ligne de routage, un renvoi d'arbre vers une skill inexistante). Une modification n'est **pas terminée** tant que le script de conformité n'a pas confirmé la synchronisation (code de sortie 0).
- **R9** : sorties concises par défaut — verdict en une ligne, seules les non-conformités détaillées (`--verbose` pour la table complète) ; réponses et consignations : l'essentiel d'abord, le détail sur demande ou en cas d'écart.
- **R10** : dès qu'une tâche est terminée — sans demande explicite — la retirer du canvas TODO et l'ajouter en tête du canvas DONE avec sa date (`routage.py done "<tâche>"` ou édition manuelle) ; une tâche n'est pas terminée tant que les deux canvases ne reflètent pas son état.
- **R11** : zéro sujet New Âge, y compris dans les items TODO (voir Hors périmètre).
- **Lint** : `date_ajout: "YYYY-MM"` obligatoire dans le frontmatter (R12) ; aucune année 20xx dans les titres nom/nom_court (R13) ; aucun `<`/`>` dans tout le frontmatter (R14) ; noms kebab-case ≤ 64 caractères.
- Le serveur `routage.py serve` reste **loopback uniquement** (bind 127.0.0.1 ; tout bind non-loopback est refusé).
- Ne jamais exposer de secrets (tokens, clés, cookies, .env) dans les consignations, logs ou commits.

## Template d'entrée (copier/coller)

```markdown
## skillAISlop — routeur de skills
Avant de choisir une skill toi-même, lance le routeur :
`python3 <chemin-vers-ce-dépôt>/outils/routage.py route "<demande de l'utilisateur>"`
- exit 0 → skill trouvée : lire `skills/NNN-*.md` correspondant et appliquer sa méthode
- exit 1 → piste affichée, à confirmer
- exit 2 → aucune skill : répondre en direct (`misses --suggest` si la demande revient souvent)
```

À placer dans le SKILL.md / AGENTS.md / .cursorrules du projet hôte. Alternative standard Agent Skills (sans routeur) : `routage.py skillmd --sortie agent-skills` puis `npx skills add ./agent-skills` (ou copie dans `.agent/skills/`). Pack autonome distribuable : `data/skillaislop-pack.zip`.

## Template de sortie (copier/coller)

```text
Verdict (une ligne, R9) : build ✅ 1900 skills + routeur · test 1749/1749 ✅ · lint ✅ · golden 198/198 ✅ · audit 1900/1900 (100 %) · sonde 2294/2294 (100 %, 0 gap) · pack FIDÈLE
Consignation DONE.md : - [x] **AAAA-MM-JJ** — <titre de la tâche> — <résultat chiffré>
```

## Checklist QA interne

- [ ] `routage.py build` ✅ (skills + routeur · 29 domaines · synonymes · FTS5 · vecteurs sqlite-vec)
- [ ] `routage.py generate --check` ✅ (synchronisation canvas, R8) · `lint` ✅ (R12/R13/R14) · `test` ✅ · `golden` ✅
- [ ] `audit_conformite.py` exit 0 sur les 8 canvases · `sonde` 100 % (0 gap) · `score_skills.py` ≥ 90 · `pack --check` FIDÈLE
- [ ] Sommaire + table de routage + arbre + index inversé synchronisés ; index du document à jour (R1)
- [ ] Compteur + export JSON régénérés si ajout/retrait de skill
- [ ] `TODO.md` / `DONE.md` à jour (R10)

## KPI reliés

- Couverture : audit 1900/1900 (100 %) · test 1749/1749 · golden 198/198 · sonde 2294/2294 (100 %, 0 gap) · evals par skill (commande `evals`)
- Qualité : `score_skills.py` moyenne 100,0/100 (seuil 90)
- Perf routage : `route` ~5-8 ms (`bench` pour re-mesurer) · pack FIDÈLE (~3,3 Mo)
- Catalogue : 1901 sections · 29 domaines · 2916 synonymes · version sémantique `CATALOGUE_VERSION` (20.0.0)

## Definition of done

- [ ] Audit de conformité exit 0, lint/test/golden/sonde verts, `pack --check` FIDÈLE
- [ ] Index, routage, compteur, export JSON synchronisés (R8) — sinon la modification n'est pas terminée
- [ ] `TODO.md`/`DONE.md` reflètent l'état (R10) ; index du document à jour (R1)
- [ ] Un commit par sujet ; `git diff --stat` + relecture avant chaque push ; PR CLEAN + CI verte avant merge

## Exemples d'usage

### Exemple 1 : ajouter une skill
Demande récurrente non routée (`route` → exit 2, consignée dans `misses`) → `misses --suggest` propose une ligne de synonyme → validation R6 → rédaction au template officiel → `generate` → `build` → `lint`/`test`/`golden`/audit → compteur + export JSON → consignation DONE (R10).

### Exemple 2 : corriger un faux positif de routage
« IoT » matchait « bibliothécaire » (voie mot-clé acceptait une inclusion dès 3 lettres) → seuil relevé à **5 lettres** → `route "IoT"` → exit 2 ✅, `route "domotique"` → skill 222 ✅ ; les fautes de frappe restent OK (exit 0 attendu).

### Exemple 3 : vague trimestrielle (R7)
Veille web du trimestre → candidats confrontés au catalogue (R6, zéro doublon) → rédaction TEMPLATE-v2 + routage complet (R3) + cross-refs (R4) → audit intégral consigné (R5) → bump de version sémantique + entrée DONE (vagues, dates, sources).

## Contraintes et références

- Référence officielle consultée le 2026-11-08 : [AGENTS.md — format ouvert](https://github.com/agentsmd/agents.md). Synthèse originale, sans reproduction du texte source ; vérifier les versions et l'applicabilité au contexte.
- [Template standard 13 sections — templateSkills.md (dépôt tvprodel/SkillsAI)](https://github.com/tvprodel/SkillsAI/blob/main/templateSkills.md), consulté le 2026-11-08 : structure de ce fichier (Objectif, Quand l'utiliser, Hors périmètre, Inputs requis, Sorties attendues, Workflow recommandé, Garde-fous, Templates entrée/sortie, Checklist QA interne, KPI reliés, Definition of done, Exemples d'usage + section références conditionnelle). Synthèse originale.
- Sources d'inspiration du catalogue (veille trimestrielle R7, vagues 1 à 21 et sources web liées) : `catalogue/sources.md`.

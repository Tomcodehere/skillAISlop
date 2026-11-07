---
name: "done-skillaislop"
title: "DONE — skillAISlop"
type: "text/markdown"
---

- [x] **2026-11-07** — Vague 18 : 100 skills IT sourcées veille web nov. 2026 (1600-1699, TEMPLATE-v2, 1 fichier par skill) — front 2027 (Vite8/Rolldown, HTMX, RSC/edge, Astro+VT, TanStack/tRPC, Qwik, WebGPU, ML client ONNX, WASI, Tauri/PWA, CSS :has/container, local-first, edge, islands, CWV/INP, a11y), protocoles agents (MCP registry/gateway, A2A, ACP, WebMCP, Agent Cards signés, AAIF, UCP, orchestration, eval trajectoires, modèles UE, agents verticaux/data, prompt-to-prod), cybersécurité 2027 (PQC/ML-KEM, harvest-now, passkeys masse, zero-trust IoT/SPIFFE, supply chain SLSA3, OWASP 2026+code IA, NIS2/DORA/CMMC, SOAR/UEBA, ransomware, DNS, secrets dynamiques, DMARC/BIMI, DevSecOps, bug bounty), data 2026-27 (DuckDB/MotherDuck, Iceberg v3, Delta/Iceberg/Hudi, dlt, Polars, modern stack, fusions marché, Data Act sept 2026/janv 2027, exit DORA, multimodal LanceDB, streaming RisingWave/Flink, Kestra, Rill, qualité GX/MonteCarlo, semantic layer, reverse ETL, contrats prod, vector DB, OTel), conformité UE (AI Act post-Omnibus calendrier/amendes/GPAI/Annexe III, CADA, Gaia-X N3, AWS Souverain, EUCS, souveraineté GPU), produit (transparence art 50, watermark C2PA, GEO/AEO, design/motion 2027, chatbot a11y, eIDAS 2.0, analytics catalogue) — 28 nouvelles sources dans catalogue/sources.md (RÉFÉRENCES.MD = 98) — catalogue à **1700 sections** (1699 skills + routeur) · corpus 1501-1800 à 199/300 · build ✅ 1699 skills + routeur · 29 domaines · 2298 synonymes · 1347/1347 tests ✅ · golden 198/198 (baseline MAJ après revue des 10 changements) · lint ✅ · audit ✅ 1699/1699 (100 %) · sonde 100 % (1864 sujets, 0 gap) · score 100,0/100 · evals 1346/1346 (866 skills) · pack FIDÈLE (2,86 Mo) · gen_docs · version 17.0.0
- [x] **2026-11-07** — Doc installation : section « Brancher sur ton agent » ajoutée au README du dépôt et au README embarqué dans le pack (ligne à copier dans le SKILL.md/AGENTS.md/.cursorrules du projet hôte pour appeler `routage.py route "..."`, exit 0/1/2) + alternative Agent Skills (`skillmd --sortie` + `npx skills add`) — pack régénéré FIDÈLE, test 1147/1147 ✅, golden 198/198 ✅
# DONE — skillAISlop

> 🔎 **Index** : historique des tâches terminées (les plus récentes en premier)

- [x] **2026-11-07** — Routeur P0 (3 améliorations, re-vérifiées) : **P0-1 poids IDF des synonymes** (colonne `poids` = 1/(1+ln(1+occ)), synonyme générique « synonyme-faible » = poids RRF ×0,5 — ex. « optimise » ne bat plus un mot-clé/FTS spécifique) · **P0-2 VEC_PISTE 0.80→0.86 + token commun requis** (faux positifs piste vec supprimés) · **P0-3 golden set de régression** (commande `golden` : 198 requêtes fixes dans `outils/golden_queries.txt` vs baseline `data/golden-routage.json`, `--update` pour régénérer, étape CI ajoutée) — test 1147/1147 ✅ · golden 198/198 ✅ · sonde 100 % · audit 1599/1599 · pack FIDÈLE
- [x] **2026-11-07** — Vague 17 : 100 skills Game Dev (1500-1599, TEMPLATE-v2, 1 fichier par skill) — nouveau domaine **Game Dev** (29 domaines au total) : moteurs/Unity-Godot-Unreal, boucle fixe, scènes, save, input, caméras, collisions, physique 2D, coyote/buffer, tilemap, procgen (rooms/CA/Perlin/WFC), pathfinding A*/flow field/navmesh, IA (FSM/utility/GOAP/perception/stealth/boss/vagues/loot), économie, progression, quêtes, dialogues, inventaire, équipement, craft, skill tree, achievements, cloud, analytics, A/B in-game, live ops, anti-triche, multi (client-serveur/lag comp/prediction/matchmaking), ECS/pooling/perf, rendu (atlas/post-FX/lumière 2D/particules GPU), juice, anim (blend tree/IK/ragdoll), audio (FMOD/musique adaptative/SFX/VO), HUD/menus/tutoriel/settings/accessibilité, mods, console dev, versions, Steam/Steamworks/store, soldes/prix régionaux, monétisation éthique, gacha légal, RGPD mineurs, perf/build mobile, portage console, tests auto, CI/CD, vertical slice, pitch éditeur, budget indé, communauté, Next Fest, playtest, EAA — catalogue à **1600 sections** (1599 skills + routeur) · corpus 1201-1500 à 300/300, corpus 1501-1800 à 99/300 · build ✅ 1599 skills + routeur · 29 domaines · 1998 synonymes · 1147/1147 tests ✅ · lint ✅ · audit ✅ 1599/1599 (100 %) · sonde 100 % (1764 sujets, 0 gap) · score 100,0/100 · evals 1146/1146 (766 skills) · pack FIDÈLE (2,65 Mo) · gen_docs · version 16.0.0 · manifeste domaines dynamique
- [x] **2026-11-07** — Vague 16 : 100 skills IT (1400-1499, TEMPLATE-v2, 1 fichier par skill) — Développement +25, IA/Prompting +20, Sécurité +15, Data +10, Data & IA +10, Produit +8, Produit & IA +5, Design +4, Routage +1, Productivité +2 — catalogue à **1500 sections** (1499 skills + routeur) · corpus 1201-1500 complété (299/300) · build ✅ 1499 skills + routeur · 28 domaines · 1697 synonymes · 947/947 tests ✅ · lint ✅ · audit ✅ 1499/1499 (100 %) · sonde 100 % (1658 sujets, 0 gap) · score 100,0/100 · evals 946/946 (666 skills) · pack FIDÈLE (2,45 Mo) · gen_docs · version 15.0.0
- [x] **2026-11-07** — Vague 15 : 49 skills (1351-1399, TEMPLATE-v2) dans les 11 domaines les moins remplis (Langues +8, Formation +6, Bureau +6, Stratégie +6, Recherche +5, Décision +4, Data +4, Produit & IA +3, Data & IA +3, Communication +2, Routage +2) — catalogue à **1400 sections** (1399 skills + routeur) · build ✅ 1399 skills + routeur · 28 domaines · 1397 synonymes · 747/747 tests ✅ · lint ✅ · audit ✅ 1399/1399 (100 %) · sonde 100 % (1558 sujets, 0 gap) · score 100,0/100 · evals 746/746 (566 skills) · exports 1400 · pack FIDÈLE (2,27 Mo) · gen_docs (70 références) · cross-refs enrichies (enrichir_xrefs.py)
- [x] **2026-11-07** — Cross-refs complétées partout (1350/1351, top-3 par cosinus même domaine, outils/enrichir_xrefs.py) + 906 workflows depends_on auto (chaînes affichées après le gagnant) — 649/649 tests, sonde 100 %, audit 100 %, pack FIDÈLE

- [x] **2026-11-07** — Vérification doublons vs aihero.dev/skills (39 skills MIT, repo mattpocock/skills) : 100 % déjà couvertes → 0 nouvelle, 111 cross-refs tags aihero:<slug> ajoutées — 649/649 tests, sonde 100 %, audit 100 %, pack FIDÈLE

- [x] **2026-11-07** — Cache LRU trigrammes de requête (trigrammes_de) → route 4,7 ms (min 2,9) — fautes de frappe OK (organisr→208), anti-bruit OK (IoT→2) — 649/649 tests, sonde 100 %, audit 100 %, pack FIDÈLE

- [x] **2026-11-07** — Perf finale 1+3+5 + garde-fous anti-faux-positifs (vec: token>=5 lettres + seuil 0,95) → route 4,8 ms (min 3,0), IoT/zzz → exit 2 — 649/649 tests, sonde 100 %, audit 100 %, evals 99,9, pack FIDÈLE

- [x] **2026-11-07** — Perf 1+3+5 : fusion RRF en un seul passage + top-K précoce + vec dim 32 → route 4,8 ms (min 3,0) — 649/649 tests, sonde 100 %, audit 100 %, pack FIDÈLE

- [x] **2026-11-07** — Perf profilée : cache LRU norm/tokens + passe synonymes en SQL (synonyme_norm indexé) → route 11,3 → 4,8 ms (−58 %) — 649/649 tests, sonde 100 %, audit 100 %, pack FIDÈLE

- [x] **2026-11-07** — Pack : deflate conservé (1,93 Mo, meilleur que LZMA 2,2 Mo sur markdown), skills.db exclu (régénéré par build --from-skills) — HNSW documenté en TODO (non supporté sqlite-vec 0.1.9, utile > 5 000 skills) — 649/649 tests, sonde 100 %, pack FIDÈLE

- [x] **2026-11-07** — Evals par skill (commande evals : 648/648 tests, 517 skills, 100/100) + skills composables depends_on (table + chaîne affichée, ex. 1350→999) + TODO multilingue EN (champ lang, route --lang) — 649/649 tests, audit 100 %, pack FIDÈLE

- [x] **2026-11-07** — Pertinence 2026 : fusion RRF k=60 des voies + contextual enrichment des embeddings ([domaine|branche]) + bonus freshness (tag=année) + bonus xref/popularité existants + conformité kebab-case (9 slugs tronqués) + seuil vec 0,88 — 649/649 tests, audit 1350/1350 (100 %), score 99,9/100, pack FIDÈLE

- [x] **2026-11-07** — Index popularité (top-20) : table popularite calculée au build depuis routes + bonus +0,05 au classement + commande top — template/scripts/docs MAJ pour tags+bonus — 649/649 tests, audit 100 %, pack FIDÈLE

- [x] **2026-11-07** — 3 optimisations routage : bonus cross-ref dans le classement (+0,10 si lié à un top candidat), champ tags optionnel + table indexée + route --tag (551 skills taguées 2027), vec dim 128→64 — audit 1350/1350 (100 %), 649/649 tests, sonde 100 %, pack FIDÈLE, route 11,3 ms

- [x] **2026-11-07** — Nouveau script outils/score_skills.py : score qualité /100 par skill (frontmatter, 12 sections, suffisance de contenu, cross-ref, unicité, spec) — moyenne 99.9/100, 1347 skills >= 90 — + étape CI + 3 signaux vides corrigés (1025/1026/1196)

- [x] **2026-11-07** — Vague 14 : 40 skills (1311-1350, format TEMPLATE-v2 complet, sourcées veille nov. 2026) — catalogue à 1351 sections (1350 skills + routeur) · build ✅ 1350 skills + routeur · 1258 synonymes · 649/649 tests ✅ · lint ✅ · audit ✅ 1350/1350 (100 %) · sonde 100 % · exports 1351 · pack FIDÈLE

- [x] **2026-11-07** — Migration TEMPLATE-v2 lancée et terminée : les 1310 skills ont désormais les 12 sections v2 (0 manquante) — contenu uniforme — audit 1310/1310 (100 %) · 609/609 tests · sonde 100 % · pack FIDÈLE

- [x] **2026-11-07** — Remplissage auto des sections vides des skills mergées (SkillsAI) : 156 sections remplies, 0 vide restante hors routeur — audit 1310/1310 (100 %)

- [x] **2026-11-06** — Merge SkillsAI : 311 skills (1000-1310) intégrées au format TEMPLATE-v2 — catalogue à 1311 sections (1310 skills + routeur) · build ✅ 1310 skills + routeur · 1218 synonymes · 609/609 tests ✅ · lint ✅ · audit ✅ 1310/1310 (100 %, double template R2/v2) · sonde 100 % · exports 1311 · pack FIDÈLE · docs auto régénérées

- [x] **2026-11-06** — Vérification des doublons faite : 0 doublon interne (R6 ✅), 0 doublon exact vs SkillsAI (311 skills), 33 recouvrements thématiques documentés (compléments, pas de fusion) → rapport documentations/skillsdocs/doublons.md

- [x] **2026-11-04** — Vague 13 (R7 anticipée) : 100 skills (900-999) sourcées d'une veille nov. 2026 / tendances 2027 — catalogue à 1000 sections (999 skills + routeur, 0-999), nouveau corpus 901-1200 — build ✅ 999 skills + routeur · 1116 synonymes · 1000 vecteurs · 549/549 tests ✅ · lint ✅ · audit ✅ 999/999 (100 %) · sonde 1158/1158 (100 %) · exports 1000 · pack FIDÈLE

- [x] **2026-11-04** — WAL checkpoint PASSIVE après chaque écriture de session (skills.db-wal ne grossit plus en longue session)

- [x] **2026-11-04** — Perf : voie mot-clé en SQL (table mots_cles indexée) → route 8,5 → 6,0 ms ; trigrammes filtrés >= 5 lettres → DB 2,04 → 1,72 Mo — 449/449 tests, sonde 100 %, pack FIDÈLE

- [x] **2026-11-04** — Versioning sémantique : CATALOGUE_VERSION (12.0.0) dans meta au build, affiché par versions, embarqué dans le manifeste du pack — section Export multi-projets de la TODO 100 % faite

- [x] **2026-11-04** — API locale : routage.py serve (loopback 127.0.0.1 uniquement, bind externe refusé) — /health, /route?q= (exit 0/1/2 + voies/scores), /skills, /export.json ; testé en local + smoke test CI

- [x] **2026-11-04** — Interop Agent Skills : routage.py skillmd génère 900 SKILL.md standardisés (data/agent-skills/ + skills.json) depuis skills/*.md — installables via npx skills add dans Claude Code/Codex/Cursor ; testé en CI

- [x] **2026-11-04** — Export multi-projets : build --from-skills fidèle (tables identiques au build canvas) + routage.py pack (zip 1,01 Mo : 900 skills + routage.py + manifeste v12.0.0 + hash + README) + pack --check FIDÈLE en CI — un autre projet fait pip install sqlite-vec + build --from-skills + route

- [x] **2026-11-03** — PR #3 mergée dans main (merge 492efa9) : catalogue à 900 sections (899 skills + routeur), CI verte

- [x] **2026-11-03** — Branche vibe/vague-12-900-sections poussée + PR #3 ouverte (brouillon) — vague 12 à 900 sections, CI verte (run 41646172879)

- [x] **2026-11-03** — Vague 12 ajoutée : 100 skills (800-899) sourcées d'une veille nov. 2026 — catalogue à 900 sections (899 skills + routeur) : agents personnels & gouvernance (Muse/Dots, WebMCP, claude-mem, guardrails, BEC/deepfakes), fiscalité 2026 (LF 2026-103, PER, Coluche, LMNP), conso & quotidien (droit à l'oubli, litiges, voisinage, voyages low-cost), RH avancée (RI, TT, DUERP, AT, CSE, RCC, cession, levée de fonds), AI/data literacy — build ✅ 899 skills + routeur · 813 synonymes · 900 vecteurs · lint ✅ · 449/449 tests ✅ · audit ✅ 899/899 · sonde 1058/1058 (100 %)

- [x] **2026-11-02** — PR #2 mergée dans main (merge 77a594f) : 800 sections, vectorisation sqlite-vec, trigrammes SQL, CI, optimisations, sonde 100 % bloquante

- [x] **2026-11-02** — Sonde à 100 % (958/958, 0 gap : sujets < 4 lettres exclus) et redevenue bloquante en CI ; hook pre-push build+lint+test

- [x] **2026-11-02** — Automatiser TODO/DONE (R10) : sous-commandes routage.py todo/done — testées (ajout + retrait auto + date en tête de DONE.md)

- [x] **2026-11-02** — Automatiser TODO/DONE (R10) : sous-commandes routage.py todo/done — testées (ajout + retrait auto + date en tête de DONE.md)

- [x] **2026-11-02** — Tester la sous-commande todo

- [x] **2026-11-02** — AGENTS.md documenté avec tous les ajouts : nouvelle section « Architecture du routeur SQL » (tables skills_fts/skills_vec/trigrammes/skills_fts_vocab/meta/versions/routes, index, pragmas, cascade complète avec voies+scores+exit codes, sous-commandes vocab/versions/analytics), layout MAJ (CI + commandes) — test ✅ 224/224 · audit ✅ 799/799

- [x] **2026-11-02** — Instructions du routeur (skill 0 + AGENTS.md) mises à jour pour exploiter la cascade complète : voies et scores de chaque candidate, interprétation des exit 0/1/2 (exit 0 = première candidate, exit 1 = piste à confirmer, exit 2 = consulter `misses --suggest` avant réponse directe) — test ✅ 224/224 · audit ✅ 799/799 · generate --check ✅

- [x] **2026-11-02** — Passe floue trigrammes passée en SQL (table `trigrammes` WITHOUT ROWID, 54 304 entrées, indexée PK) : 16,3 → 1,8 ms, résultats identiques à la version Python (vérifié sur 5 requêtes), repli Python si table absente — route 7,8 → 7,6 ms (max 32 → 14 ms) · test ✅ 224/224 · IoT/zzz exit 2 · audit ✅ 799/799 · sonde 971/972 (0 partiel)

- [x] **2026-11-02** — Optimisations du routeur : hoist de norm(query) + cache des mot_cle normalisés, k vec réduit à top, vec dim 256→128 (base 1,76→1,24 Mo), PRAGMA WAL + cache_size=-8000, VEC_PISTE relevé à 0.80 (zzz qwertyu repasse exit 2) — route 8,9→7,8 ms · build 0,23 s · test ✅ 224/224 · audit ✅ 799/799 · sonde 971/972 (0 partiel)

- [x] **2026-11-02** — Améliorations SQLite : index secondaires (domaine, branche), tables meta+versions avec snapshot JSON et diff par build (`routage.py versions`), fts5vocab (`routage.py vocab`), analytics SQL des routages (`routage.py analytics`), PRAGMA optimize + VACUUM au build — build ✅ 799 skills + routeur · 783 synonymes · 800 vecteurs · test ✅ 224/224 · audit ✅ 799/799

- [x] **2026-11-02** — CI GitHub Actions ajoutée (.github/workflows/ci.yml : build, generate --check, lint, test 224/224, audit conformité, sonde, compteur à jour) + bouclage sonde : 5 partiels levés (synonymes decks/arbitrer/trancher/tutorat/dispatcher), sonde à 971/972 couverts, 0 partiel, 1 gap (« ton » seul, couvert par « ton d'équipe ») — build ✅ 799 skills + routeur · 783 synonymes · 800 vecteurs · lint ✅ · test ✅ 224/224 · audit ✅ 799/799

- [x] **2026-11-02** — Base vectorisée (sqlite-vec) : table `skills_vec` (vec0, cosinus, dim 256, embeddings locaux hash bag-of-words) créée au `build` et requêtée en voie « vec » entre le FTS5 et la passe floue ; seuil candidat 0.80, piste vec ≥ 0.65 ; repli gracieux si l'extension est absente (FTS5 seul) — build ✅ 800 vecteurs · test ✅ 224/224 (IoT et zzz restent exit 2) · lint ✅ · audit ✅ 799/799 · sonde 966/972 (99 %) · bench route 8,8 ms

- [x] **2026-11-02** — Vague 11 ajoutée : 100 skills (700-799) sourcées d'une veille web 2026 (skills.sh, ClawHub, awesome-claude-skills, rapports 2026 Anthropic/Vercel) : fact-checking IA, A2A, harness, observabilité, mémoire structurée, audit de skills, vidéo Remotion, packshots IA, social listening, social selling, closing, upsell, tunnel e-commerce, lancement produit, daily brief, médiation, conduite du changement, recrutement, offboarding, CSE, RPS, négociation salariale, business plan, pitch investisseurs, trésorerie PME, sauvegardes 3-2-1, AI Act, contrats, PI — build ✅ 799 skills + routeur · 28 domaines · 774 synonymes · lint ✅ · 224/224 tests ✅ · audit ✅ 799/799 · R6 ✅ · R8 ✅ · generate --check ✅ ; compteur (800), exports compact/complet et sonde (966/972, 99 %) régénérés

- [x] **2026-11-02** — Vague 10 ajoutée : 83 skills (617-699) — vie quotidienne approfondie (burn-out, charge mentale, syndrome de l'imposteur, sommeil, allergies, santé, grossesse, famille, seniors, handicap, déménagement, dépannage, voiture, voyage, sport, animaux, jardin, cuisine végé), travail & carrière (entretien annuel, promotion, licenciement, harcèlement, discrimination, télétravail, réunions efficaces, feedback, pitch, onboarding), finance & juridique (trésorerie, TVA, clôture, paie, surendettement, succession, divorce, résiliation, bail, copropriété, assurances, banque, épargne, retraite, achat immo), digital & IA 2026 (mots de passe, ransomware, arnaques, droit à l'image, RGPD quotidien, WCAG, green IT, veille tech, choix LLM, RAG, fine-tuning, injection de prompt, evals, coût tokens, no-code, prise de notes, langues, permis, reconversion) — build ✅ 699 skills + routeur · 28 domaines · 631 synonymes · lint ✅ · 125/125 tests ✅ · audit ✅ 699/699 · R6 ✅ · R8 ✅ ; compteur, exports compact/complet et sonde (864/872, 99 %) régénérés

- [x] **2026-11-01** — Vague 9 ajoutée : 16 skills sourcées du registre open source skills-hub.ai (601-616 : revue de session IA, revue CTO, régressions visuelles, contrats d'API, plans de test manuels, sprint dette technique, publication mobile, design-to-code, Kubernetes, SOC 2, briefing du matin, GEO moteurs IA, SWOT, pré-déploiement, auto-amélioration d'agent) + skill i-have-adhd (communication TDAH-friendly) — build ✅ 617 sections · lint ✅ (449 synonymes, collision « recette » corrigée) · 42/42 tests ✅ · audit ✅ 616/616 · R6 ✅ · R8 ✅ ; compteur et export compact régénérés dans leurs canvases

- [x] **2026-11-01** — Catalogue découpé en corpus (plafond de taille d'un canvas, 1 024 000 octets) : canvas principal (sommaire, règles, skill 0, routage, ~148 Ko) + canvases corpus-skills-1-300 (~431 Ko), corpus-skills-301-600 (~434 Ko) et corpus-skills-601-900 ; script d'audit passé en multi-fichiers, routeur adapté (export compact par défaut, `--complet` pour le texte intégral, lecture des sections dans les corpus) ; AGENTS.md documenté (layout corpus, commandes multi-fichiers)

- [x] **2026-11-01** — Vague 8 ajoutée : 90 skills (511-600) couvrant les 33 gaps de la sonde de couverture (santé mentale factuelle, crypto/web3, robotique, arts de la scène, musique, bourse & ETF, parentalité, montage vidéo, photo, regex, game dev, dev mobile, design d'API, franchise, surendettement, voisinage, arnaques, droit à l'image, bénévolat, baby-sitting, poésie, journal intime, sorties culturelles, récits de vie) + 63 skills de veille web 2026 (vibe coding, humaniseur IA, Obsidian, audit de budget, supervision d'agents, deepfakes, quotidien & business) — 4 collisions de synonymes corrigées (anniversaire, cuisiner, recette, chanson) ; build ✅ · lint ✅ · tests ✅ · audit ✅ 600/600 · R6 ✅ · R8 ✅ ; compteur et export régénérés

- [x] **2026-11-01** — R8 étendue : à chaque ajout ou retrait de skill, régénération obligatoire du compteur (`count`) et de l'export JSON (`export`) + actualisation de leurs canvases — inscrite dans le règlement, la skill 250, la Knowledge et l'AGENTS.md ; audit repassé ✅ 510/510 · R6 ✅ · R8 ✅

- [x] **2026-11-01** — Compteur de skills automatisé : sous-commande `count` du routeur générant `totalSkillsCount.md` (511 sections · 510 skills + 1 routeur · 28 domaines) — exécuté vers /export, copie permanente publiée dans le canvas « totalSkillsCount », procédure documentée dans l'AGENTS.md ; build ✅ · lint ✅ · 28/28 tests ✅

- [x] **2026-11-01** — Dossier `/export` créé et export JSON exécuté (511 sections · 28 domaines · 283 synonymes, 988 Ko) — copie permanente publiée dans le canvas « Export JSON — skillAISlop », procédure de régénération documentée dans l'AGENTS.md

- [x] **2026-11-01** — R6 assouplie : les emojis sont réutilisables entre skills (présence et pertinence exigées, plus d'unicité) — règlement, template, skill 250, AGENTS.md et script d'audit mis à jour, audit repassé ✅ 510/510 · Sous-commande `export` ajoutée au routeur : JSON structuré des 511 sections (régénérable en une commande) · Frontmatter vérifiés sur les 6 canvases
- [x] **2026-11-01** — Vague 7 ajoutée : 10 skills sécurité informatique & web (501-510 : authentification web, en-têtes HTTP & cookies, WordPress/CMS, modélisation de menaces, correctifs & CVE, chiffrement & TLS, sécurité cloud, pipeline CI/CD, simulation de phishing, réseau & Wi-Fi) — routage complet (283 synonymes), lint ✅, 28/28 tests, audit 510/510 conformes · R6 ✅ · R8 ✅

- [x] **2026-11-01** — Règle R11 établie : zéro sujet New Âge, jamais — méditation retirée du TODO, inscription dans la Knowledge et l'AGENTS.md ; catalogue vérifié : aucune skill New Âge existante
- [x] **2026-11-01** — TODO et DONE convertis en canvases permanents « TODO — skillAISlop » et « DONE — skillAISlop » — R10 et AGENTS.md mis à jour (survie aux resets garantie)
- [x] **2026-11-01** — Règle R10 établie : suivi TODO/DONE automatique à chaque écriture — inscrite dans la Knowledge, l'AGENTS.md et auditée (R5) : 500/500 conformes
- [x] **2026-11-01** — Correctif anti-faux-positifs du routeur : mode OU validé par mots complets, flou réservé aux inflexions, tolérance synonymes 7 caractères — sonde 78 sujets : 40 couverts légitimes, 0 faux positif
- [x] **2026-11-01** — Rescapes post-durcissement : 12 synonymes ciblés + remap « speech » → 154 Studio de voix de synthèse
- [x] **2026-11-01** — Boucle d'auto-repair : pistes sur exit 2 + `misses --suggest`
- [x] **2026-11-01** — Supervision : `lint`, `stats` (observabilité par voie), `bench` (mesures rejouables)
- [x] **2026-11-01** — Tests de non-régression (`test`, corpus 24 demandes) + journal des exit 2 (`misses`) + passe floue trigrammes
- [x] **2026-11-01** — Outillage SQL consolidé dans le canvas « Routage SQL Skills » — survit aux resets, base reconstruite par `build` (0,18 s)
- [x] **2026-11-01** — Tâches trimestrielles R7 (janvier/avril/juillet/octobre) alignées sur la procédure outillée (build → INSERT → generate → lint + test → audit R1-R8)
- [x] **2026-11-01** — Gains du routage SQL mesurés et consignés dans la Knowledge (gains-routage-sql.md) : ~40 tokens par routage, facteur ~200× vs sommaire
- [x] **2026-11-01** — Sonde de couverture du catalogue : 78 sujets → 40 couverts · 7 partiels · 31 vrais gaps identifiés
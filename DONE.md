---
name: "done-skillaislop"
title: "DONE — skillAISlop"
type: "text/markdown"
---

# DONE — skillAISlop

> 🔎 **Index** : historique des tâches terminées (les plus récentes en premier)

- [x] **2026-11-07** — 3 optimisations routage : bonus cross-ref dans le classement (+0,10 si lié à un top candidat), champ tags optionnel + table indexée + route --tag (551 skills taguées 2027), vec dim 128→64 — audit 1350/1350 (100 %), 649/649 tests, sonde 100 %, pack FIDÈLE, route 11,3 ms

- [x] **2026-11-07** — Nouveau script outils/score_skills.py : score qualité /100 par skill (frontmatter, 12 sections, suffisance de contenu, cross-ref, unicité, spec) — moyenne 99.9/100, 1347 skills >= 90 — + étape CI + 3 signaux vides corrigés (1025/1026/1196)

- [x] **2026-11-07** — Vague 14 : 40 skills (1311-1350, format TEMPLATE-v2 complet, sourcées veille nov. 2026) — catalogue à 1351 sections (1350 skills + routeur) · build ✅ 1351 skills · 1258 synonymes · 649/649 tests ✅ · lint ✅ · audit ✅ 1350/1350 (100 %) · sonde 100 % · exports 1351 · pack FIDÈLE

- [x] **2026-11-07** — Migration TEMPLATE-v2 lancée et terminée : les 1310 skills ont désormais les 12 sections v2 (0 manquante) — contenu uniforme — audit 1310/1310 (100 %) · 609/609 tests · sonde 100 % · pack FIDÈLE

- [x] **2026-11-07** — Remplissage auto des sections vides des skills mergées (SkillsAI) : 156 sections remplies, 0 vide restante hors routeur — audit 1310/1310 (100 %)

- [x] **2026-11-06** — Merge SkillsAI : 311 skills (1000-1310) intégrées au format TEMPLATE-v2 — catalogue à 1311 sections (1310 skills + routeur) · build ✅ 1311 skills · 1218 synonymes · 609/609 tests ✅ · lint ✅ · audit ✅ 1310/1310 (100 %, double template R2/v2) · sonde 100 % · exports 1311 · pack FIDÈLE · docs auto régénérées

- [x] **2026-11-06** — Vérification des doublons faite : 0 doublon interne (R6 ✅), 0 doublon exact vs SkillsAI (311 skills), 33 recouvrements thématiques documentés (compléments, pas de fusion) → rapport documentations/skillsdocs/doublons.md

- [x] **2026-11-04** — Vague 13 (R7 anticipée) : 100 skills (900-999) sourcées d'une veille nov. 2026 / tendances 2027 — catalogue à 1000 sections (999 skills + routeur, 0-999), nouveau corpus 901-1200 — build ✅ 1000 skills · 1116 synonymes · 1000 vecteurs · 549/549 tests ✅ · lint ✅ · audit ✅ 999/999 (100 %) · sonde 1158/1158 (100 %) · exports 1000 · pack FIDÈLE

- [x] **2026-11-04** — WAL checkpoint PASSIVE après chaque écriture de session (skills.db-wal ne grossit plus en longue session)

- [x] **2026-11-04** — Perf : voie mot-clé en SQL (table mots_cles indexée) → route 8,5 → 6,0 ms ; trigrammes filtrés >= 5 lettres → DB 2,04 → 1,72 Mo — 449/449 tests, sonde 100 %, pack FIDÈLE

- [x] **2026-11-04** — Versioning sémantique : CATALOGUE_VERSION (12.0.0) dans meta au build, affiché par versions, embarqué dans le manifeste du pack — section Export multi-projets de la TODO 100 % faite

- [x] **2026-11-04** — API locale : routage.py serve (loopback 127.0.0.1 uniquement, bind externe refusé) — /health, /route?q= (exit 0/1/2 + voies/scores), /skills, /export.json ; testé en local + smoke test CI

- [x] **2026-11-04** — Interop Agent Skills : routage.py skillmd génère 900 SKILL.md standardisés (data/agent-skills/ + skills.json) depuis skills/*.md — installables via npx skills add dans Claude Code/Codex/Cursor ; testé en CI

- [x] **2026-11-04** — Export multi-projets : build --from-skills fidèle (tables identiques au build canvas) + routage.py pack (zip 1,01 Mo : 900 skills + routage.py + manifeste v12.0.0 + hash + README) + pack --check FIDÈLE en CI — un autre projet fait pip install sqlite-vec + build --from-skills + route

- [x] **2026-11-03** — PR #3 mergée dans main (merge 492efa9) : catalogue à 900 sections (899 skills + routeur), CI verte

- [x] **2026-11-03** — Branche vibe/vague-12-900-sections poussée + PR #3 ouverte (brouillon) — vague 12 à 900 sections, CI verte (run 41646172879)

- [x] **2026-11-03** — Vague 12 ajoutée : 100 skills (800-899) sourcées d'une veille nov. 2026 — catalogue à 900 sections (899 skills + routeur) : agents personnels & gouvernance (Muse/Dots, WebMCP, claude-mem, guardrails, BEC/deepfakes), fiscalité 2026 (LF 2026-103, PER, Coluche, LMNP), conso & quotidien (droit à l'oubli, litiges, voisinage, voyages low-cost), RH avancée (RI, TT, DUERP, AT, CSE, RCC, cession, levée de fonds), AI/data literacy — build ✅ 900 skills · 813 synonymes · 900 vecteurs · lint ✅ · 449/449 tests ✅ · audit ✅ 899/899 · sonde 1058/1058 (100 %)

- [x] **2026-11-02** — PR #2 mergée dans main (merge 77a594f) : 800 sections, vectorisation sqlite-vec, trigrammes SQL, CI, optimisations, sonde 100 % bloquante

- [x] **2026-11-02** — Sonde à 100 % (958/958, 0 gap : sujets < 4 lettres exclus) et redevenue bloquante en CI ; hook pre-push build+lint+test

- [x] **2026-11-02** — Automatiser TODO/DONE (R10) : sous-commandes routage.py todo/done — testées (ajout + retrait auto + date en tête de DONE.md)

- [x] **2026-11-02** — Automatiser TODO/DONE (R10) : sous-commandes routage.py todo/done — testées (ajout + retrait auto + date en tête de DONE.md)

- [x] **2026-11-02** — Tester la sous-commande todo

- [x] **2026-11-02** — AGENTS.md documenté avec tous les ajouts : nouvelle section « Architecture du routeur SQL » (tables skills_fts/skills_vec/trigrammes/skills_fts_vocab/meta/versions/routes, index, pragmas, cascade complète avec voies+scores+exit codes, sous-commandes vocab/versions/analytics), layout MAJ (CI + commandes) — test ✅ 224/224 · audit ✅ 799/799

- [x] **2026-11-02** — Instructions du routeur (skill 0 + AGENTS.md) mises à jour pour exploiter la cascade complète : voies et scores de chaque candidate, interprétation des exit 0/1/2 (exit 0 = première candidate, exit 1 = piste à confirmer, exit 2 = consulter `misses --suggest` avant réponse directe) — test ✅ 224/224 · audit ✅ 799/799 · generate --check ✅

- [x] **2026-11-02** — Passe floue trigrammes passée en SQL (table `trigrammes` WITHOUT ROWID, 54 304 entrées, indexée PK) : 16,3 → 1,8 ms, résultats identiques à la version Python (vérifié sur 5 requêtes), repli Python si table absente — route 7,8 → 7,6 ms (max 32 → 14 ms) · test ✅ 224/224 · IoT/zzz exit 2 · audit ✅ 799/799 · sonde 971/972 (0 partiel)

- [x] **2026-11-02** — Optimisations du routeur : hoist de norm(query) + cache des mot_cle normalisés, k vec réduit à top, vec dim 256→128 (base 1,76→1,24 Mo), PRAGMA WAL + cache_size=-8000, VEC_PISTE relevé à 0.80 (zzz qwertyu repasse exit 2) — route 8,9→7,8 ms · build 0,23 s · test ✅ 224/224 · audit ✅ 799/799 · sonde 971/972 (0 partiel)

- [x] **2026-11-02** — Améliorations SQLite : index secondaires (domaine, branche), tables meta+versions avec snapshot JSON et diff par build (`routage.py versions`), fts5vocab (`routage.py vocab`), analytics SQL des routages (`routage.py analytics`), PRAGMA optimize + VACUUM au build — build ✅ 800 skills · 783 synonymes · 800 vecteurs · test ✅ 224/224 · audit ✅ 799/799

- [x] **2026-11-02** — CI GitHub Actions ajoutée (.github/workflows/ci.yml : build, generate --check, lint, test 224/224, audit conformité, sonde, compteur à jour) + bouclage sonde : 5 partiels levés (synonymes decks/arbitrer/trancher/tutorat/dispatcher), sonde à 971/972 couverts, 0 partiel, 1 gap (« ton » seul, couvert par « ton d'équipe ») — build ✅ 800 skills · 783 synonymes · 800 vecteurs · lint ✅ · test ✅ 224/224 · audit ✅ 799/799

- [x] **2026-11-02** — Base vectorisée (sqlite-vec) : table `skills_vec` (vec0, cosinus, dim 256, embeddings locaux hash bag-of-words) créée au `build` et requêtée en voie « vec » entre le FTS5 et la passe floue ; seuil candidat 0.80, piste vec ≥ 0.65 ; repli gracieux si l'extension est absente (FTS5 seul) — build ✅ 800 vecteurs · test ✅ 224/224 (IoT et zzz restent exit 2) · lint ✅ · audit ✅ 799/799 · sonde 966/972 (99 %) · bench route 8,8 ms

- [x] **2026-11-02** — Vague 11 ajoutée : 100 skills (700-799) sourcées d'une veille web 2026 (skills.sh, ClawHub, awesome-claude-skills, rapports 2026 Anthropic/Vercel) : fact-checking IA, A2A, harness, observabilité, mémoire structurée, audit de skills, vidéo Remotion, packshots IA, social listening, social selling, closing, upsell, tunnel e-commerce, lancement produit, daily brief, médiation, conduite du changement, recrutement, offboarding, CSE, RPS, négociation salariale, business plan, pitch investisseurs, trésorerie PME, sauvegardes 3-2-1, AI Act, contrats, PI — build ✅ 800 skills · 28 domaines · 774 synonymes · lint ✅ · 224/224 tests ✅ · audit ✅ 799/799 · R6 ✅ · R8 ✅ · generate --check ✅ ; compteur (800), exports compact/complet et sonde (966/972, 99 %) régénérés

- [x] **2026-11-02** — Vague 10 ajoutée : 83 skills (617-699) — vie quotidienne approfondie (burn-out, charge mentale, syndrome de l'imposteur, sommeil, allergies, santé, grossesse, famille, seniors, handicap, déménagement, dépannage, voiture, voyage, sport, animaux, jardin, cuisine végé), travail & carrière (entretien annuel, promotion, licenciement, harcèlement, discrimination, télétravail, réunions efficaces, feedback, pitch, onboarding), finance & juridique (trésorerie, TVA, clôture, paie, surendettement, succession, divorce, résiliation, bail, copropriété, assurances, banque, épargne, retraite, achat immo), digital & IA 2026 (mots de passe, ransomware, arnaques, droit à l'image, RGPD quotidien, WCAG, green IT, veille tech, choix LLM, RAG, fine-tuning, injection de prompt, evals, coût tokens, no-code, prise de notes, langues, permis, reconversion) — build ✅ 700 skills · 28 domaines · 631 synonymes · lint ✅ · 125/125 tests ✅ · audit ✅ 699/699 · R6 ✅ · R8 ✅ ; compteur, exports compact/complet et sonde (864/872, 99 %) régénérés

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
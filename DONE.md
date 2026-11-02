---
name: "done-skillaislop"
title: "DONE — skillAISlop"
type: "text/markdown"
---

# DONE — skillAISlop

> 🔎 **Index** : historique des tâches terminées (les plus récentes en premier)

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
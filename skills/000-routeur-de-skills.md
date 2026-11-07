---
num: 0
nom: "🧭 Routeur de skills"
emoji: "🧭"
domaine: "Routage"
signal: ""
mot_cle: ""
nom_court: ""
branche: ""
synonymes: []
cross_refs: []
---

> 🔎 **Index** : Objectif · Instructions système · Règles de priorité · Carte des domaines · Index inversé · Table de routage complète · Arbre de décision · Variante routage léger · Exemple de routage · Cas d'usage

**Objectif** : analyser la demande de l'utilisateur et aiguiller automatiquement vers la (ou les) skill(s) adaptée(s), avec une cascade de repli si aucune skill ne correspond.

**Instructions système** :
Tu es le routeur de la bibliothèque de skills. Pour chaque message utilisateur, tu suis ce protocole en 4 étapes, sans jamais sauter l'étape 1 :

1. **Classifier** — Résous l'intention dominante en cascade, du plus rapide au plus exhaustif :
   a. **Base SQLite (si l'environnement exécute des scripts)** — extrais le script du canvas « routage-sql-skills » puis : `routage.py build` (une fois) · `routage.py route ""`. La candidate renvoyée (2-3 lignes + ancre `## N.` de sa section) évite toute lecture de table. Exit 0 : candidate trouvée, passe à l'étape 2 · exit 1 : domaine plausible renvoyé, saute en c avec ce domaine · exit 2 : aucune piste, continue en b.
   b. **Index inversé** — si la demande contient un mot-clé canonique de l'index ci-dessous (« TDD », « RACI », « README », « dbt »…), la skill est résolue directement : passe à l'étape 2.
   c. **Carte des domaines** — sinon, identifie le domaine dominant dans la carte des domaines, puis lis uniquement son bloc dans la table de routage (regroupée par domaine).
   d. **Arbre de décision** — en cas d'hésitation entre plusieurs domaines, arbitre avec l'arbre ci-dessous.
   Si la demande reste ambiguë, pose UNE question de clarification ciblée (jamais plus d'une).
2. **Annoncer** — Indique brièvement : « → Skill N : [nom] » avant de traiter. Si plusieurs skills sont nécessaires, annonce l'ordre d'exécution (ex. « → Skill 18 puis Skill 8 »).
3. **Exécuter** — Charge les instructions complètes de la skill sélectionnée et applique sa méthode. La skill a priorité sur tes habitudes : en cas de conflit, la skill gagne.
4. **Boucler** — En fin de réponse, si la demande a évolué vers un autre besoin, relance le routage (retour à l'étape 1). Sinon, indique les skills complémentaires pertinentes en une ligne.

**Règles de priorité en cas d'hésitation** :
- Demande ambiguë entre "produire" et "améliorer" → demander si c'est un nouveau contenu ou une reprise.
- Deux skills aussi valables → choisir la plus spécifique du domaine, annoncer l'alternative.
- Aucune skill ne correspond → répondre en direct, puis suggérer si pertinent de créer une nouvelle skill (via la skill 17).

**Carte des domaines** (étage 1 — repérer le domaine dominant, puis ne lire que son bloc dans la table) :

| Domaine | Mots-clés déclencheurs |
|---|---|
| Apprentissage | apprendre, mémoriser, réviser, prise de notes, cours en ligne, parcours d’apprentissage |
| Bureau | Word, Excel, PowerPoint, fichiers, présentations, decks |
| Carrière | CV, candidature, entretien, salaire, évolution de rôle |
| Communication | email, message professionnel, annonce, ton d’équipe, jargon |
| Créativité | idées, brainstorming, nommer, fiction, scénario |
| Data | données, métriques, anomalies, Excel, dbt, SLI/SLO, dashboards |
| Data & IA | datasets, évals, RAG personnel, recommandation, red-team |
| Décision | arbitrer, trancher, décider |
| Design | visuel, maquette, couleurs, accessibilité, design tokens, UI |
| Développement | code, git, tests, API, base de données, builds, fuzzing |
| Finance | comptes, bilan, marge, prévisionnel, crédit |
| Formation | expliquer, former, tutorat, e-learning |
| Gestion | projet, processus, risques, parties prenantes, RACI, business case |
| IA / Prompting | agent, prompt, modèle, tokens, biais, benchmarks, dérive |
| Juridique | contrat, clause, CGU/CGV, RGPD, rétention, NDA, archivage |
| Langues | vocabulaire, prononciation, examen de langue |
| Marketing | campagne, SEO, marque, audience, influenceurs, parcours client |
| Personnel | maison, santé, sommeil, famille, courses, expatriation |
| Productivité | agenda, focus, checklist, filtres email, estimation du temps |
| Produit | roadmap, activation, offre, bêta, dark patterns, navigation |
| Produit & IA | chatbot, produit IA |
| Recherche | veille, étude, état du marché, sources |
| Rédaction | article, texte, traduction, script, newsletter, lisibilité |
| RH & formation | recrutement, onboarding, formation, télétravail, salaires, mobilité |
| Routage | dispatcher, conservation du catalogue (méta) |
| Sécurité | audit, intrusion, menace, fuite de données, forensique, authentification, MFA, en-têtes HTTP, CMS, CVE, chiffrement, cloud, CI/CD, phishing, réseau |
| Stratégie | partenariat, positionnement |
| Vente | prospect, démo, devis, pipeline, facture, tarif |

**Index inversé** (raccourci — un mot-clé canonique de la demande renvoie directement à la skill) :

- **Apprentissage** — « tuteur socratique » → 39 · « quiz & flashcards » → 40 · « examen blanc » → 41 · « vulgarisateur pour enfants » → 132 · « langue (conversation) » → 212 · « flashcards » → 213 · « ficheur de lectures » → 226 · « soutenances » → 241 · « plans de lecture » → 494 · « atelier de mémorisation & mnémotechnie » → 495 · « répétition espacée » → 496 · « cours en ligne » → 497 · « prise de notes méthodique » → 498 · « apprentissage par l'enseignement » → 499 · « parcours d'apprentissage personnel » → 500 · « maths » → 559 · « mémoire & thèse » → 560 · « musées & art » → 569 · « devoirs » → 570 · « orientation scolaire » → 571 · « code de la route » → 580 · « bourses étudiantes » → 591
- **Bureau** — « créateur de présentations » → 14 · « reçus & factures » → 115 · « guide de démarches administratives » → 217 · « dossiers de subventions » → 240 · « manipulateur de pdf » → 268
- **Carrière** — « préparation d'entretien / interview » → 12 · « analyseur cv & lettre » → 44 · « négociation » → 45 · « conversations difficiles » → 46 · « simulateur de rôle » → 49 · « propositions freelance » → 62 · « progression » → 204 · « guide de reconversion professionnelle » → 231 · « éloquence » → 293 · « demande d'augmentation » → 294 · « marque personnelle » → 548 · « portfolio créatif » → 572 · « tarifs freelance » → 599 · « bilan de compétences » → 600
- **Communication** — « assistant email professionnel » → 4 · « discours » → 75 · « communiqués de presse » → 126 · « mémos décision » → 127 · « bios & pages « à propos » » → 128 · « communicant de crise » → 235 · « réunions multilingues » → 289 · « questions-réponses en direct » → 397 · « briefeur d'agences & prestataires » → 398 · « matrice de ton d'équipe » → 399 · « procès-verbaux » → 400 · « jargon inter-équipes » → 401 · « points presse » → 402 · « déclarations officielles » → 403 · « messages de changement » → 404 · « experts internes » → 405 · « chartes de modération » → 406 · « messages d'entreprise » → 423
- **Créativité** — « brainstorming structuré » → 6 · « générateur de noms » → 47 · « atelier d'écriture créative » → 121 · « synopsis & pitchs d'histoires » → 122 · « génération d'images » → 139 · « restaurateur de photos anciennes » → 140 · « assets 3d » → 142 · « génération vidéo » → 144 · « studio d'avatars vidéo ia » → 145 · « storyboarder » → 146 · « studio de voix de synthèse » → 154 · « compositeur musical ia » → 155 · « technicien de nettoyage audio » → 156 · « podcast ia » → 157 · « sous-titreur » → 158 · « designer sonore de marque » → 159 · « créateur d'effets sonores » → 160 · « créateur de jeux & énigmes » → 228 · « réalisateur de vidéos programmatiques » → 258 · « variantes créatives publicitaires » → 283 · « théâtre & impro » → 515 · « coach chant » → 516 · « coach danse » → 517 · « apprendre un instrument » → 518 · « montage vidéo débutant » → 521 · « photographie » → 522 · « prompt d'images » → 546 · « loisirs créatifs manuels » → 557 · « jeux de stratégie » → 567 · « écriture de chansons » → 573 · « retouche photo » → 574 · « streaming » → 576
- **Data** — « analyste de données » → 13 · « données web (scraping) » → 91 · « nettoyeur de données » → 92 · « modélisateur prédictif » → 93 · « pipelines de données » → 94 · « cartographe de données » → 95 · « cohortes & rétention » → 106 · « tableaux de bord » → 107 · « data storyteller » → 108 · « parcours & funnel » → 109 · « tests a/b » → 110 · « tracking analytics » → 186 · « guidelines d'annotation » → 238 · « données publiques » → 242 · « données synthétiques » → 263 · « automatiseur excel & tableurs » → 264 · « qualité de données » → 343 · « gouverneur de définitions de métriques » → 344 · « séries temporelles » → 345 · « anomalies métier » → 346 · « formules excel » → 347 · « visualiseur de données géographiques » → 348 · « tests de données » → 349 · « transformations dbt » → 350 · « objectifs sli/slo » → 351 · « lecteur de heatmaps & sessions » → 352 · « propension client » → 353 · « sources hétérogènes » → 354 · « verbatims à grande échelle » → 355 · « extraction de documents » → 543 · « statistiques » → 547
- **Data & IA** — « pipeline de recommandation » → 35 · « tableaux de bord & kpi » → 36 · « red-team de prompts » → 37 · « skill creator (skill.md) » → 38 · « infographie animée » → 48
- **Décision** — « avocat du diable » → 61
- **Design** — « critique ux d'interface » → 64 · « ux writer (microcopy d'interface) » → 65 · « emails transactionnels » → 138 · « créateur d'illustrations vectorielles » → 141 · « créateur de mockups produits » → 143 · « miniatures » → 147 · « mood boards » → 148 · « palettes & typographies » → 149 · « bibliothécaire de styles visuels » → 150 · « illustrateur technique » → 151 · « briefeur de direction artistique » → 152 · « maquettiste wireframe » → 153 · « accessibilité (wcag) » → 177 · « design system » → 181 · « formulaires » → 182 · « auditeur anti-look générique ia » → 449 · « états vides » → 450 · « messages d'erreur & de récupération ui » → 452 · « remédiation d'accessibilité » → 454 · « design tokens » → 455 · « expérience mobile » → 456
- **Développement** — « code commenté » → 9 · « review de code & debug » → 10 · « grill me (validation de plan) » → 19 · « débogage systématique » → 20 · « implémentation incrémentale » → 21 · « diagrammes d'architecture » → 22 · « documentation technique » → 23 · « tests unitaires » → 67 · « commits & descriptions de pr » → 68 · « assistant sql & modélisation de données » → 69 · « audit sécurité du code (owasp) » → 70 · « pilote d'agents de code cli » → 76 · « builder mcp (model context protocol) » → 77 · « prototypeur no-code » → 78 · « auditeur d'api » → 79 · « refactorer de code patrimonial » → 80 · « composants ui » → 81 · « ingénieur devops & déploiement » → 82 · « transpileur de code » → 83 · « algorithmes » → 84 · « infrastructure as code » → 85 · « migrations techniques » → 86 · « spécifications openapi » → 87 · « adr (décisions d'architecture) » → 88 · « post-mortems d'incident » → 89 · « release notes » → 129 · « documentation d'api » → 180 · « testeur e2e navigateur » → 252 · « auditeur performance web » → 253 · « mocks d'api » → 254 · « tests de charge » → 255 · « enquêteur d'incidents production » → 256 · « base de code inconnue » → 257 · « worktrees git » → 301 · « test-first (tdd) » → 302 · « versioning sémantique » → 303 · « feature flags » → 304 · « environnement de dev reproductible » → 305 · « secrets & trousseaux » → 306 · « montée de versions » → 307 · « profileur mémoire & cpu » → 308 · « benchmarkeur de code » → 309 · « cas limites & fuzzing » → 310 · « conventions de code d'équipe » → 311 · « readme » → 312 · « monorepo » → 313 · « conteneuriseur d'application » → 314 · « régression (git bisect) » → 315 · « dépôt git » → 316 · « tests d'intégration » → 317 · « requêtes sql lentes » → 318 · « files d'attente & jobs asynchrones » → 319 · « rate limits & quotas d'api » → 320 · « schémas de base de données » → 321 · « webhooks » → 322 · « builds & compilation » → 323 · « scripts cli robustes » → 324 · « robotique maker » → 514 · « regex » → 523 · « game dev » → 524 · « dev mobile » → 525 · « design d'api » → 526 · « vibe coding » → 540 · « administration bdd » → 542 · « bots discord slack » → 544 · « site statique » → 545 · « régressions visuelles » → 603 · « contrats d'api » → 604 · « sprint dette technique » → 606 · « publication mobile » → 607 · « design to code » → 608 · « kubernetes » → 609 · « pré-déploiement » → 614
- **Finance** — « analyse de documents financiers » → 59 · « optimiseur finops (coûts cloud) » → 90 · « rentabilité unitaire » → 169 · « prévisionnel financier » → 170 · « levée de fonds » → 171 · « lettres investisseurs » → 172 · « initiateur à l'investissement » → 227 · « abonnements & dépenses récurrentes » → 230 · « retraite » → 249 · « assembleur de dossier fiscal » → 297 · « crédit & amortissement » → 298 · « éducation crypto » → 512 · « web3 & defi » → 513 · « bourse & etf » → 519 · « surendettement » → 528 · « audit de budget » → 541 · « finances freelance » → 563 · « comptabilité tpe » → 588
- **Formation** — « expliqueur pédagogique » → 11 · « créateur de campagnes de sensibilisation sécurité » → 200 · « formations » → 201 · « capsules microlearning » → 295
- **Gestion** — « planificateur de projet » → 15 · « rétrospective » → 73 · « définisseur d'okr » → 74 · « enquêtes internes » → 113 · « modérateur de communauté » → 192 · « évaluateur de risques fournisseurs » → 198 · « ateliers & séances de travail » → 208 · « décisions collectives » → 210 · « team building » → 211 · « événements » → 221 · « rituels d'équipe » → 232 · « audits internes » → 243 · « plan de continuité (pra) » → 273 · « atelier de notes atomiques zettelkasten » → 287 · « chartes d'équipe » → 424 · « coûts de projet » → 425 · « parties prenantes » → 426 · « business cases » → 427 · « maturité d'équipe » → 428 · « portefeuille de projets » → 429 · « intégration post-fusion » → 430 · « sla fournisseurs » → 431 · « communautés de pratique » → 432 · « processus métier » → 433 · « rôles & responsabilités (raci) » → 434 · « registre des risques » → 435 · « sprints design » → 437 · « rapports annuels d'activité » → 438 · « franchise & reprise » → 527 · « bénévolat associatif » → 532 · « vie associative » → 552 · « auto-entrepreneur » → 562 · « logistique e-commerce » → 587
- **IA / Prompting** — « prompts (meta-prompting) » → 17 · « datasets d'entraînement llm » → 96 · « évaluations llm (evals) » → 97 · « pipelines rag » → 98 · « outils pour agents (function calling) » → 99 · « instructions d'agent » → 100 · « déployeur d'agents autonomes » → 224 · « contexte de conversation » → 236 · « débogueur de prompts » → 237 · « handoff de session » → 251 · « chef d'orchestre multi-agents » → 259 · « mémoire longue durée » → 260 · « déclenchement de skills » → 261 · « contrôleur qualité de skill.md » → 262 · « coûts & modèles llm » → 265 · « conseiller fine-tuning vs rag » → 266 · « agent vocal ivr » → 288 · « skills externes » → 325 · « tokens & budget de contexte » → 326 · « réponses ia » → 327 · « routines d'agents » → 328 · « points de contrôle humains » → 329 · « agents » → 330 · « modèles légers » → 331 · « schémas de sortie » → 332 · « benchmarks de modèles » → 333 · « prompts entre modèles » → 334 · « personnalité d'agent » → 335 · « biais de modèle & de données » → 336 · « cartes de modèle » → 337 · « régression de prompts » → 338 · « testeur fantôme d'agents » → 339 · « robustesse d'agents » → 340 · « contrats de tâche d'agent » → 341 · « dérive de modèle » → 342 · « supervision agents » → 577 · « amélioration des prompts » → 598 · « revue de session » → 601 · « auto-amélioration agent » → 615 · « communication tdah » → 616
- **Juridique** — « assistant juridique de premier niveau » → 16 · « courriers officiels & réclamations » → 137 · « anonymisateur de données (rgpd) » → 189 · « documents de conformité » → 190 · « charte ia d'entreprise » → 193 · « registres rgpd » → 196 · « veilleur réglementaire » → 239 · « conformité ai act » → 271 · « aipd (analyse d'impact) » → 272 · « conditions générales de vente » → 374 · « politiques de rétention & archivage » → 442 · « cgu & mentions légales » → 443 · « notification de violation de données » → 444 · « clauses de sous-traitance (dpa) » → 446 · « nda sur mesure » → 448 · « litiges voisinage » → 529 · « droit à l'image » → 531 · « licences open source » → 553 · « locataire & bailleur » → 554 · « droit du travail » → 555 · « séparation & divorce » → 590 · « petites créances » → 594 · « copropriété » → 595 · « soc 2 » → 610
- **Langues** — « traducteur professionnel » → 7 · « vocabulaire thématique » → 491 · « prononciation & phonétique » → 492 · « examens de langue » → 493
- **Marketing** — « copywriting publicitaire » → 3 · « script vidéo ugc & pub » → 29 · « posts sociaux » → 30 · « ghostwriter linkedin » → 31 · « analyseur concurrentiel » → 32 · « personas » → 33 · « charte de marque » → 34 · « newsletter » → 51 · « scripteur youtube long format » → 52 · « moteur de repurposing de contenu » → 53 · « fiches produits e-commerce » → 118 · « pages de vente » → 123 · « études de cas clients » → 124 · « livres blancs » → 125 · « planificateur éditorial » → 135 · « auditeur seo technique » → 161 · « conversion (cro) » → 162 · « stratège de lancement produit » → 163 · « programmes de fidélité » → 173 · « créateur de lead magnets » → 174 · « communauté » → 175 · « atelier de hooks & titres viraux » → 278 · « produits concurrents e-commerce » → 279 · « publicités concurrentes » → 356 · « séquences email d'automatisation » → 357 · « audiences & listes emailing » → 358 · « sms & messages courts » → 359 · « stratège de présence locale » → 360 · « relations influenceurs » → 361 · « cohérence de marque 360 » → 362 · « transcréateur de campagnes par marché » → 363 · « quiz marketing interactifs » → 364 · « carrousels éditoriaux » → 365 · « social listening » → 366 · « pages comparatives & alternatives » → 367 · « parcours client » → 373 · « panier & d'upsell » → 375 · « délivrabilité email » → 586 · « moteurs ia » → 612
- **Personnel** — « voyage » → 42 · « coach budget perso » → 43 · « messager d'occasions » → 136 · « coach sportif » → 214 · « conseiller nutrition » → 215 · « chef menu-maker (recettes contraintes) » → 216 · « cadeaux » → 218 · « comparateur d'achats » → 219 · « chef de projet rénovation » → 220 · « orchestrateur domotique » → 222 · « assistant de déménagement » → 225 · « potager » → 229 · « succession numérique » → 246 · « l'équilibre pro-perso » → 248 · « diagnostiqueur de pannes domestiques » → 291 · « carnet d'entretien véhicule » → 292 · « guide de visites immobilières » → 296 · « empreinte carbone numérique » → 470 · « archiviste familial » → 472 · « cahiers des charges de travaux » → 473 · « garanties & réparations » → 474 · « kits d'expatriation » → 476 · « plan d'urgence familial » → 477 · « courses & garde-manger » → 478 · « négociation d'achats importants » → 479 · « biens du foyer » → 480 · « logistique familiale » → 481 · « aidants familiaux » → 482 · « sommeil » → 483 · « ergonomie au bureau » → 484 · « bilans de santé » → 485 · « batch cooking » → 486 · « armoire à pharmacie » → 487 · « arrêt des habitudes » → 488 · « routines ancrées » → 489 · « mémoires familiales » → 490 · « gestion du stress » → 511 · « parentalité » → 520 · « arnaques en ligne » → 530 · « baby-sitting » → 533 · « sorties culturelles » → 536 · « animaux de compagnie » → 556 · « style vestimentaire » → 558 · « discours de famille » → 564 · « fêtes de famille » → 565 · « cuisine du quotidien » → 566 · « recommandations culturelles » → 568 · « plantes d'intérieur » → 578 · « désencombrement » → 579 · « numérique seniors » → 581 · « course à pied » → 582 · « randonnée » → 583 · « dégustation » → 584 · « miles & points » → 585 · « médiation familiale » → 589 · « colocation » → 592 · « mutuelles & santé » → 593
- **Productivité** — « synthèse & résumé de documents » → 5 · « compte rendu de réunion » → 24 · « tri & priorisation d'emails » → 25 · « décomposition de tâches » → 26 · « créateur de documents office » → 27 · « planification par fichiers » → 28 · « créateur de sop & playbooks » → 50 · « workflows d'automatisation » → 71 · « semaine (time blocking) » → 72 · « bases de connaissances » → 114 · « réunions » → 209 · « tâches (to-do) » → 223 · « fabricant de templates de documents » → 245 · « automatiseur de tâches web répétitives » → 269 · « orchestrateur de prise de rendez-vous » → 284 · « traqueur d'action items de réunions » → 285 · « fichiers & arborescences » → 286 · « chirurgien du calendrier de réunions » → 463 · « système de lecture personnel » → 464 · « travail profond » → 465 · « horaires atypiques » → 466 · « fabricant de checklists critiques » → 467 · « tableau de bord personnel » → 468 · « filtres & règles email » → 469 · « dictée vocale » → 471 · « temps réaliste » → 475 · « obsidian » → 539 · « briefing du matin » → 611
- **Produit** — « prd & user stories » → 63 · « narrateur de roadmap » → 176 · « tests fonctionnels (qa) » → 178 · « activation produit » → 179 · « dépréciations » → 183 · « trieur de tickets support » → 184 · « backlog » → 185 · « interviews utilisateurs » → 187 · « synthétiseur de recherche utilisateur » → 188 · « gamification » → 300 · « navigation & arborescence produit » → 451 · « parcours d'activation in-app » → 453 · « paliers d'offre » → 457 · « rôles & permissions produit » → 458 · « programme bêta » → 459 · « gardien anti-dark patterns » → 460 · « flux d'inscription & vérification » → 461 · « guides de migration clients » → 462 · « gameplay » → 575 · « plans de test manuels » → 605
- **Produit & IA** — « chatbot conversationnel » → 66
- **Recherche** — « agent de recherche approfondie » → 18 · « concepts » → 101 · « analyste rag de documents personnels » → 102 · « lecteur d'études scientifiques » → 104 · « veille hebdomadaire » → 105 · « tendances & signaux faibles » → 290
- **Rédaction** — « articles seo » → 1 · « réécriture & adaptation de ton » → 2 · « relecture & correction » → 8 · « documents longs » → 116 · « documents formatés » → 117 · « générateur de faq » → 119 · « textes ia & plagiat » → 120 · « guides utilisateurs » → 130 · « assistant de citations & bibliographies » → 133 · « définitions & glossaires » → 134 · « localisateur de contenu & d'app i18n » → 280 · « vulgarisateur de contrats en langage clair » → 281 · « créateur de pas-à-pas illustrés » → 299 · « lisibilité » → 377 · « transcriptions » → 378 · « notifications & push » → 379 · « threads éditoriaux » → 380 · « dialogues » → 381 · « atelier de fiction interactive » → 382 · « critiques & comparatifs produits » → 383 · « scripts de podcast » → 384 · « métadonnées youtube » → 385 · « pitches médias » → 386 · « kits média » → 387 · « intervieweur par écrit » → 388 · « contenu en 5 secondes » → 389 · « messages d'erreur » → 390 · « alt-text & descriptions d'images » → 391 · « scripts de webinaire » → 392 · « tribunes d'expert » → 393 · « macros de support » → 394 · « contrôleur avant publication » → 395 · « quatrièmes de couverture » → 396 · « poésie » → 534 · « journal intime » → 535 · « récits de vie » → 537 · « humaniseur de texte » → 538
- **RH & formation** — « fiches de poste » → 202 · « onboarding collaborateurs » → 203 · « compétences d'équipe » → 205 · « évaluations annuelles » → 206 · « politiques internes rh » → 207 · « employer branding » → 233 · « programme de mentorat » → 234 · « sélecteur de candidatures (screening structuré) » → 274 · « offboarding » → 275 · « grille d'entretien de recrutement » → 276 · « auto-évaluation annuelle » → 277 · « plans de développement individuel » → 407 · « offres d'emploi attractives » → 408 · « succession de talents » → 409 · « équité salariale » → 410 · « programmes de stage & alternance » → 411 · « accords de télétravail » → 412 · « entretiens de départ » → 413 · « mobilité interne » → 414 · « cycles de feedback 360 » → 415 · « dossiers de financement de formation » → 416 · « formations obligatoires » → 417 · « intégration de managers débutants » → 418 · « canaux de feedback anonyme » → 419 · « continuité d'équipe » → 420 · « charge de travail d'équipe » → 421 · « lettres de recommandation » → 422 · « interculturel » → 549 · « neurodiversité » → 550
- **Routage** — « conservateur de la bibliothèque de skills » → 250
- **Sécurité** — « fraudes & anomalies de logs » → 191 · « garde-fous d'agents » → 194 · « durcisseur anti-injection de prompt » → 195 · « permissions & accès » → 197 · « runbooks de sécurité » → 199 · « consignes de sécurité » → 244 · « hygiène numérique » → 247 · « inventoriste de dépendances (sbom) » → 267 · « tests d'intrusion » → 439 · « menaces » → 440 · « expert forensique numérique » → 441 · « sécurité physique » → 445 · « fuites de données » → 447 · « authentification web » → 501 · « en-têtes http & cookies » → 502 · « wordpress & cms » → 503 · « modélisation de menaces » → 504 · « correctifs & cve » → 505 · « chiffrement & tls » → 506 · « sécurité cloud » → 507 · « pipeline ci/cd » → 508 · « simulation de phishing » → 509 · « réseau & wi-fi » → 510 · « deepfakes » → 561 · « sauvegardes personnelles » → 596 · « contrôle parental » → 597
- **Stratégie** — « business model canvas » → 57 · « stratégie de prix » → 58 · « prémortem de projet » → 60 · « marché sectoriel » → 103 · « partenariats stratégiques » → 436 · « vision & valeurs » → 551 · « revue cto » → 602 · « swot » → 613
- **Vente** — « prospection à froid (cold outreach) » → 54 · « feedback client » → 55 · « support client » → 56 · « scorer de leads » → 111 · « analyste win/loss » → 112 · « témoignages clients » → 131 · « créateur de battlecards commerciaux » → 164 · « scripteur d'appels commerciaux » → 165 · « la gestion d'objections » → 166 · « business reviews clients » → 167 · « répondant aux appels d'offres (aapa) » → 168 · « metteur à jour de crm » → 270 · « répondant aux avis clients en ligne » → 282 · « démos personnalisées » → 368 · « grilles tarifaires » → 369 · « contrats commerciaux » → 370 · « factures impayées » → 371 · « pipeline commercial » → 372 · « reporting commercial » → 376

**Table de routage complète** (étage 2 — regroupée par domaine) :

| Signal dans la demande | → Skill | Domaine |
|---|---|---|
| **Apprentissage** | | |
| Maths, soutien scolaire mathématique, progression | 559 | Apprentissage |
| Mémoire, thèse, dissertation académique, plan de rédaction | 560 | Apprentissage |
| Musée, histoire de l'art, comprendre une exposition, mouvements artistiques | 569 | Apprentissage |
| Aide aux devoirs, accompagnement scolaire à la maison | 570 | Apprentissage |
| Orientation scolaire, choix d'études, filières | 571 | Apprentissage |
| Code de la route, permis, révision, préparation examen | 580 | Apprentissage |
| Bourses d'études, aides étudiantes, financement des études | 591 | Apprentissage |
| Apprendre par questions guidées, socratique | 39 | Apprentissage |
| Quiz, flashcards, réviser, mémoriser | 40 | Apprentissage |
| Examen blanc, épreuve d'entraînement | 41 | Apprentissage |
| Vulgarisation pour enfants | 132 | Apprentissage |
| Conversation en langue étrangère, coaching oral | 212 | Apprentissage |
| Flashcards, cartes de révision | 213 | Apprentissage |
| Fiche de lecture, synthèse de livre | 226 | Apprentissage |
| Soutenance, défense orale de mémoire | 241 | Apprentissage |
| Pile de livres à lire, plan de lecture | 494 | Apprentissage |
| Retenir par cœur, palais de mémoire | 495 | Apprentissage |
| Spaced repetition, calendrier de révisions | 496 | Apprentissage |
| Choisir un MOOC, cursus en ligne | 497 | Apprentissage |
| Méthode Cornell, notes structurées | 498 | Apprentissage |
| Apprendre en enseignant, effet protégé | 499 | Apprentissage |
| Que apprendre cette année, curriculum perso | 500 | Apprentissage |
| **Bureau** | | |
| Deck, slides, présentation | 14 | Bureau |
| Reçus et factures, extraction de dépenses | 115 | Bureau |
| Démarche administrative, paperasse pas à pas | 217 | Bureau |
| Dossier de subvention, demande de prime | 240 | Bureau |
| Extraire un tableau PDF, fusionner des PDF, OCR | 268 | Bureau |
| **Carrière** | | |
| Marque personnelle, visibilité professionnelle, positionnement expert | 548 | Carrière |
| Portfolio, book créatif, sélection de travaux, présentation designer | 572 | Carrière |
| Tarifs freelance, prix de journée, devis, augmentation tarifaire | 599 | Carrière |
| Bilan de compétences, point carrière, projet professionnel | 600 | Carrière |
| Entretien, simulation, pitch oral | 12 | Carrière |
| CV, lettre de motivation, candidature | 44 | Carrière |
| Négocier : salaire, prix, contrat | 45 | Carrière |
| Conversation difficile, conflit, feedback dur | 46 | Carrière |
| Simuler un client / prospect / utilisateur | 49 | Carrière |
| Proposition, devis, réponse à un besoin client freelance | 62 | Carrière |
| Plan de progression, développement personnel | 204 | Carrière |
| Reconversion professionnelle, changement de métier | 231 | Carrière |
| Éloquence, tics de langage, parler en public | 293 | Carrière |
| Demander une augmentation, négocier son salaire | 294 | Carrière |
| **Communication** | | |
| Email, lettre, message professionnel | 4 | Communication |
| Discours de mariage, keynote, toast, éloge | 75 | Communication |
| Communiqué de presse, annonce média | 126 | Communication |
| Mémo décision, note courte pour décider | 127 | Communication |
| Bio, page « à propos », profil d'auteur | 128 | Communication |
| Communication de crise, bad buzz, incident public | 235 | Communication |
| Réunion multilingue, interprétation d'équipe | 289 | Communication |
| AMA, questions-réponses en direct | 397 | Communication |
| Brief d'agence, cahier des charges de prestataire | 398 | Communication |
| Ton par contexte, communication interne | 399 | Communication |
| Procès-verbal, assemblée générale | 400 | Communication |
| Faire comprendre le jargon, tech contre métier | 401 | Communication |
| Point presse, interview de journaliste | 402 | Communication |
| Déclaration officielle, communiqué de position | 403 | Communication |
| Annonce de changement, réorganisation | 404 | Communication |
| Recueillir l'expertise, expert qui part | 405 | Communication |
| Charte de modération, règles de communauté | 406 | Communication |
| Vœux d'entreprise, message de direction | 423 | Communication |
| **Créativité** | | |
| Théâtre, impro, jeu d'acteur, prise de scène | 515 | Créativité |
| Chant, voix chantée, justesse, respiration | 516 | Créativité |
| Danse, chorégraphie, apprendre à danser | 517 | Créativité |
| Apprendre un instrument, guitare, piano, violon | 518 | Créativité |
| Montage vidéo débutant, premier film, logiciels simples | 521 | Créativité |
| Photographie, cadrage, lumière, appareil photo | 522 | Créativité |
| Prompt d'images avancé, Midjourney, paramètres de génération | 546 | Créativité |
| Loisirs créatifs, tricot, couture, céramique, projets manuels | 557 | Créativité |
| Échecs, go, jeux de stratégie, progresser au jeu | 567 | Créativité |
| Écrire une chanson, paroles, structure, composition | 573 | Créativité |
| Retouche photo, Lightroom, développement raw, traitement d'images | 574 | Créativité |
| Streaming, Twitch, chaîne live, setup de stream | 576 | Créativité |
| Idées, créativité, atelier, naming | 6 | Créativité |
| Nommer une marque, un produit, un projet | 47 | Créativité |
| Écriture créative, nouvelle, scénario co-écrit | 121 | Créativité |
| Synopsis, pitch d'histoire, arche narrative | 122 | Créativité |
| Prompt de génération d'images | 139 | Créativité |
| Restauration de photos anciennes, colorisation | 140 | Créativité |
| Asset 3D, modèle pour jeu ou rendu | 142 | Créativité |
| Génération vidéo IA | 144 | Créativité |
| Avatar vidéo IA, présentateur multilingue | 145 | Créativité |
| Storyboard, script en plans visuels | 146 | Créativité |
| Voix de synthèse, texte en audio réaliste | 154 | Créativité |
| Musique IA, composition originale | 155 | Créativité |
| Nettoyage audio, bruit de fond à supprimer | 156 | Créativité |
| Podcast IA, article en dialogue audio | 157 | Créativité |
| Sous-titres, transcription alignée | 158 | Créativité |
| Identité sonore, jingle de marque | 159 | Créativité |
| Effets sonores (SFX), bruitage | 160 | Créativité |
| Jeu, énigme, chasse au trésor sur mesure | 228 | Créativité |
| Vidéo programmatique, récap en vidéo, Remotion | 258 | Créativité |
| Variantes publicitaires, décliner une créa | 283 | Créativité |
| **Data** | | |
| OCR, extraction de documents, factures, tableaux depuis PDF | 543 | Data |
| Statistiques, significativité, taille d'échantillon, incertitude | 547 | Data |
| Chiffres, données, tendances, KPIs | 13 | Data |
| Scraping web, pages en données structurées | 91 | Data |
| Nettoyage de données, doublons et anomalies | 92 | Data |
| Modèle prédictif, forecast, scoring de données | 93 | Data |
| Pipeline de données, orchestration ETL | 94 | Data |
| Cartographie de données, dictionnaire, lignage | 95 | Data |
| Analyse de cohortes, rétention, churn | 106 | Data |
| Tableau de bord, KPI à suivre | 107 | Data |
| Data storytelling, chiffres en récit | 108 | Data |
| Parcours utilisateur, funnel, conversion | 109 | Data |
| Test A/B, protocole d'expérimentation | 110 | Data |
| Plan de tracking analytics, événements produit | 186 | Data |
| Guidelines d'annotation, consignes de labeling | 238 | Data |
| Données publiques, open data à exploiter | 242 | Data |
| Données synthétiques, jeu de données de test | 263 | Data |
| Formule Excel, tableau croisé dynamique | 264 | Data |
| Qualité de données, valeurs manquantes | 343 | Data |
| Définition de métrique, dictionnaire KPI | 344 | Data |
| Saisonnalité, prévision de série temporelle | 345 | Data |
| Anomalie dans les données métier, pic inexpliqué | 346 | Data |
| Formule Excel cassée, erreur #REF | 347 | Data |
| Carte de données, données géographiques | 348 | Data |
| Test de données, contrainte de table, dbt | 349 | Data |
| Couche de transformation, modèle dbt | 350 | Data |
| SLO, engagement de disponibilité | 351 | Data |
| Heatmap, session recording, rage click | 352 | Data |
| Score de propension, probabilité d'achat | 353 | Data |
| Fusionner plusieurs sources de données | 354 | Data |
| Mille verbatims, coder des réponses ouvertes | 355 | Data |
| **Data & IA** | | |
| Recommandation, ranking, feed, top-K | 35 | Data & IA |
| Dashboard, KPI, indicateurs de suivi | 36 | Data & IA |
| Red-team, faille d'un prompt, détournement | 37 | Data & IA |
| Créer un package de skill SKILL.md | 38 | Data & IA |
| Infographie animée, visuel de données | 48 | Data & IA |
| **Décision** | | |
| Avocat du diable, contredire, challenger une décision | 61 | Décision |
| **Design** | | |
| Audit UX, heuristiques, friction de parcours | 64 | Design |
| Microcopy, textes d'interface, boutons, messages d'erreur | 65 | Design |
| Email transactionnel, message automatisé produit | 138 | Design |
| Illustration vectorielle, logo, icône éditable | 141 | Design |
| Mockup produit, packaging avec logo | 143 | Design |
| Miniature YouTube, thumbnail cliquable | 147 | Design |
| Mood board, planche d'inspiration | 148 | Design |
| Palette de couleurs, choix typographique | 149 | Design |
| Style visuel cohérent, charte d'illustration | 150 | Design |
| Illustration technique, schéma didactique | 151 | Design |
| Brief de direction artistique, shooting photo | 152 | Design |
| Wireframe, maquette basse fidélité | 153 | Design |
| Accessibilité (WCAG), interface inclusive | 177 | Design |
| Design system, composants et tokens | 181 | Design |
| Formulaire, champs et taux d'abandon | 182 | Design |
| Design trop IA, éviter le look générique | 449 | Design |
| Écran vide, empty state, première utilisation | 450 | Design |
| Message d'erreur utile, écran d'échec UI | 452 | Design |
| Plan WCAG, remédier l'accessibilité | 454 | Design |
| Design tokens, variables de thème | 455 | Design |
| Parcours mobile, ergonomie une main | 456 | Design |
| **Développement** | | |
| Régressions visuelles, comparaison de captures, CSS cassé, rendu | 603 | Développement |
| Contrats d'API, tests consommateur, breaking changes, compatibilité | 604 | Développement |
| Sprint dette technique, inventaire des TODOs, code mort, objets dieux | 606 | Développement |
| Publication App Store, Google Play, fiche de store, release mobile | 607 | Développement |
| Design to code, intégration de maquettes, Figma vers composants, handoff | 608 | Développement |
| Kubernetes, manifests, pods, autoscaling, probes de déploiement | 609 | Développement |
| Pré-déploiement, verdict READY NOT READY, vérifications avant mise en production | 614 | Développement |
| Robotique, Arduino, Raspberry Pi, électronique embarquée | 514 | Développement |
| Regex, expressions régulières, patterns de texte | 523 | Développement |
| Game dev, premier jeu vidéo, Godot, Unity | 524 | Développement |
| App mobile, iOS, Android, React Native, Flutter | 525 | Développement |
| Design d'API, REST, GraphQL, contrats de ressources | 526 | Développement |
| Vibe coding, construire une app en pilotage naturel, agent de code | 540 | Développement |
| Administration base de données, Postgres, MySQL, index | 542 | Développement |
| Bot Discord, Slack, Telegram, agent conversationnel automatisé | 544 | Développement |
| Site statique, blog personnel, Hugo, Astro, déploiement simple | 545 | Développement |
| Écrire du code / script neuf | 9 | Développement |
| Bug, review, sécurité, audit de code | 10 | Développement |
| Stress-tester un plan avant de coder, « grill me » | 19 | Développement |
| Erreur complexe, investigation de bug | 20 | Développement |
| Grosse fonctionnalité à découper, pas-à-pas | 21 | Développement |
| Schéma d'architecture, diagramme de système | 22 | Développement |
| README, documentation, guide technique | 23 | Développement |
| Tests unitaires, TDD, couverture | 67 | Développement |
| Message de commit, description de PR | 68 | Développement |
| Requête SQL, modélisation de base de données | 69 | Développement |
| Vulnérabilités, OWASP, audit sécurité du code | 70 | Développement |
| Agent de code CLI, session de pilotage terminal | 76 | Développement |
| Serveur MCP, connecter une IA à un outil externe | 77 | Développement |
| Prototype no-code, app rapide sans coder | 78 | Développement |
| Audit d'API, sécurité et contrat de requêtes | 79 | Développement |
| Refactoring de code patrimonial (legacy) | 80 | Développement |
| Génération de composants UI réutilisables | 81 | Développement |
| Déploiement cloud, CI/CD, conteneurs | 82 | Développement |
| Transpilation de code, migration de langage | 83 | Développement |
| Optimisation d'algorithme, complexité temps/mémoire | 84 | Développement |
| Infrastructure as code, environnement reproductible | 85 | Développement |
| Migration technique, plan de bascule | 86 | Développement |
| Spécification OpenAPI, contrat d'API | 87 | Développement |
| ADR, décision d'architecture consignée | 88 | Développement |
| Post-mortem d'incident, retour sur panne | 89 | Développement |
| Release notes, changelog de version | 129 | Développement |
| Documentation d'API développeur | 180 | Développement |
| Test E2E navigateur, scénario Playwright | 252 | Développement |
| Core Web Vitals, page lente, audit Lighthouse | 253 | Développement |
| Mock d'API, fixtures depuis un contrat OpenAPI | 254 | Développement |
| Test de charge, montée en charge d'un service | 255 | Développement |
| Incident production, taux d'erreur, cause première | 256 | Développement |
| Découvrir une base de code inconnue, onboarding repo | 257 | Développement |
| Travailler sur deux branches en parallèle, worktree Git | 301 | Développement |
| TDD, écrire le test avant le code | 302 | Développement |
| Semver, numéro de version, breaking change | 303 | Développement |
| Feature flag, rollout progressif, désactiver en prod | 304 | Développement |
| Devcontainer, environnement de dev reproductible | 305 | Développement |
| Stocker un secret, rotation de clé, trousseau | 306 | Développement |
| Monter de version une dépendance, upgrade risqué | 307 | Développement |
| Fuite mémoire, profiler, consommation CPU | 308 | Développement |
| Benchmark de fonction, mesurer avant/après optimisation | 309 | Développement |
| Fuzzing, entrée invalide, cas limite de code | 310 | Développement |
| Convention de code, style de nommage d'équipe | 311 | Développement |
| README de repo, page d'accueil d'un dépôt | 312 | Développement |
| Monorepo, organisation multi-packages | 313 | Développement |
| Dockerfile, conteneuriser une application | 314 | Développement |
| Régression, git bisect, retrouver le commit fautif | 315 | Développement |
| Nettoyer un dépôt Git, branches mortes | 316 | Développement |
| Test d'intégration, contrat entre services | 317 | Développement |
| Requête SQL lente, plan d'exécution, index | 318 | Développement |
| File d'attente de jobs, retry, traitement asynchrone | 319 | Développement |
| Rate limit, quota d'API, erreur 429 | 320 | Développement |
| Migration de schéma, base sans interruption | 321 | Développement |
| Webhook, callback d'API, réception d'événements | 322 | Développement |
| Build lent, temps de compilation | 323 | Développement |
| Script shell robuste, mode strict, gestion d'erreur | 324 | Développement |
| **Finance** | | |
| Crypto, blockchain, comprendre les fondamentaux sans acheter | 512 | Finance |
| Web3, DeFi, wallets, NFT en pratique sécurisée | 513 | Finance |
| Bourse, ETF, premier investissement prudent | 519 | Finance |
| Surendettement, crédits qui s'accumulent, rétablissement | 528 | Finance |
| Audit de budget, cohérence prévisionnel, revue de chiffres | 541 | Finance |
| Finances freelance, provisionnement, trésorerie irrégulière | 563 | Finance |
| Comptabilité TPE, bilan simplifié, obligations petites entreprises | 588 | Finance |
| Comptes annuels, bilan, compte de résultat à analyser | 59 | Finance |
| FinOps, optimisation des coûts cloud | 90 | Finance |
| Rentabilité unitaire, marge par offre | 169 | Finance |
| Prévisionnel financier, projection à 3 ans | 170 | Finance |
| Levée de fonds, pitch deck investisseur | 171 | Finance |
| Lettre investisseurs, update trimestrielle | 172 | Finance |
| Bases de l'investissement, éducation financière | 227 | Finance |
| Abonnements, dépenses récurrentes à auditer | 230 | Finance |
| Retraite, projection et projet de vie | 249 | Finance |
| Dossier fiscal, justificatifs de déclaration | 297 | Finance |
| Tableau d'amortissement, TAEG, comparer deux crédits | 298 | Finance |
| **Formation** | | |
| Comprendre un concept, apprendre | 11 | Formation |
| Sensibilisation sécurité, campagne phishing | 200 | Formation |
| Formation, module pédagogique, e-learning | 201 | Formation |
| Capsule microlearning, unité pédagogique de 5 minutes | 295 | Formation |
| **Gestion** | | |
| Franchise, reprise de commerce, installation commerçant | 527 | Gestion |
| Bénévolat, association, engagement de bénévole | 532 | Gestion |
| Association, statuts, assemblée générale, compte-rendu associatif | 552 | Gestion |
| Auto-entrepreneur, micro-entreprise, statut freelance, obligations | 562 | Gestion |
| Logistique e-commerce, stock, expédition, retours boutique | 587 | Gestion |
| Planifier, estimer, backlog, risques | 15 | Gestion |
| Rétrospective, rétro d'équipe, bilan de sprint | 73 | Gestion |
| OKR, objectifs trimestriels, key results | 74 | Gestion |
| Enquête interne, questionnaire d'équipe | 113 | Gestion |
| Modération de communauté, contenus toxiques | 192 | Gestion |
| Risque fournisseur, évaluation tierce | 198 | Gestion |
| Atelier, séance de travail facilitée | 208 | Gestion |
| Décision collective, choix de groupe structuré | 210 | Gestion |
| Team building, cohésion d'équipe | 211 | Gestion |
| Événement, organisation de soirée ou séminaire | 221 | Gestion |
| Rituels d'équipe, standup, réunions récurrentes | 232 | Gestion |
| Audit interne, préparation de certification | 243 | Gestion |
| PRA, plan de reprise d'activité, RTO RPO | 273 | Gestion |
| Zettelkasten, note atomique, second cerveau | 287 | Gestion |
| Charte d'équipe, règles du jeu collectives | 424 | Gestion |
| Estimer le budget d'un projet | 425 | Gestion |
| Parties prenantes, stakeholder map | 426 | Gestion |
| Business case, justifier un investissement | 427 | Gestion |
| Maturité d'équipe, où on en est | 428 | Gestion |
| Trop de projets, prioriser le portefeuille | 429 | Gestion |
| Intégration post-fusion, consolidation d'équipes | 430 | Gestion |
| SLA, engagement de service fournisseur | 431 | Gestion |
| Communauté de pratique, partage entre pairs | 432 | Gestion |
| Cartographier un processus, goulot d'étranglement | 433 | Gestion |
| Qui fait quoi, matrice RACI | 434 | Gestion |
| Registre des risques, suivre les menaces | 435 | Gestion |
| Design sprint, atelier d'innovation | 437 | Gestion |
| Rapport annuel, bilan d'activité | 438 | Gestion |
| **IA / Prompting** | | |
| Revue de session IA, travail à moitié fait, dérive avant commit | 601 | IA / Prompting |
| Auto-amélioration de l'agent, leçons persistantes, règles de fonctionnement, mémoire curée | 615 | IA / Prompting |
| Communication TDAH-friendly, réponses action d'abord, sans préambule, étapes numérotées | 616 | IA / Prompting |
| Agents IA en production, tracing, coûts, alertes | 577 | IA / Prompting |
| Amélioration continue des prompts, itération, feedback | 598 | IA / Prompting |
| Créer un prompt, améliorer un prompt | 17 | IA / Prompting |
| Dataset d'entraînement LLM, paires prompt-réponse | 96 | IA / Prompting |
| Évaluations LLM (evals), mesure de qualité | 97 | IA / Prompting |
| Pipeline RAG, recherche augmentée de documents | 98 | IA / Prompting |
| Function calling, outil d'agent, schéma JSON | 99 | IA / Prompting |
| Instructions d'agent, system prompt de comportement | 100 | IA / Prompting |
| Agent autonome, bot multi-étapes | 224 | IA / Prompting |
| Contexte de conversation longue, compaction | 236 | IA / Prompting |
| Prompt qui échoue, débogage d'instruction | 237 | IA / Prompting |
| Handoff de session, reprise après coupure de contexte | 251 | IA / Prompting |
| Système multi-agents, passage de relais entre agents | 259 | IA / Prompting |
| Mémoire longue durée, préférences persistantes | 260 | IA / Prompting |
| Test de déclenchement, matrice de routage de skills | 261 | IA / Prompting |
| Audit de SKILL.md, qualité d'une skill | 262 | IA / Prompting |
| Facture LLM, coût par tâche, descente de modèle | 265 | IA / Prompting |
| Fine-tuning ou RAG, arbitrage d'architecture LLM | 266 | IA / Prompting |
| Agent vocal, IVR, arbre d'appel téléphonique | 288 | IA / Prompting |
| Installer une skill externe, registre de skills | 325 | IA / Prompting |
| Budget de tokens, contexte qui déborde | 326 | IA / Prompting |
| Réponse trop longue, compresser la sortie | 327 | IA / Prompting |
| Routine planifiée d'agent, tâche récurrente IA | 328 | IA / Prompting |
| Approbation humaine, validation avant action d'agent | 329 | IA / Prompting |
| Tracer un agent, journal d'exécution d'agent | 330 | IA / Prompting |
| Modèle léger, petit modèle, on-device | 331 | IA / Prompting |
| Sortie JSON stricte, structured output | 332 | IA / Prompting |
| Choisir un modèle, leaderboard, benchmark de modèles | 333 | IA / Prompting |
| Porter un prompt vers un autre modèle | 334 | IA / Prompting |
| Personnalité d'agent, ton de l'assistant | 335 | IA / Prompting |
| Biais de modèle, équité des données | 336 | IA / Prompting |
| Model card, documenter un modèle | 337 | IA / Prompting |
| Régression de prompt, comparer deux versions | 338 | IA / Prompting |
| Shadow run, tester un agent en parallèle | 339 | IA / Prompting |
| Agent qui échoue en conditions réelles, stresser un agent | 340 | IA / Prompting |
| Contrat de tâche, brief d'agent | 341 | IA / Prompting |
| Dérive du modèle, drift en production | 342 | IA / Prompting |
| **Juridique** | | |
| SOC 2, critères TSC, preuves de conformité, audit sécurité organisation | 610 | Juridique |
| Litige de voisinage, bruit, mitoyenneté, médiation | 529 | Juridique |
| Droit à l'image, autorisation photo, publication d'image | 531 | Juridique |
| Licence open source, MIT, GPL, conformité dépendances | 553 | Juridique |
| Bail, location, caution, état des lieux, droits locataire | 554 | Juridique |
| Droit du travail, contrat, licenciement, congés, litige employé | 555 | Juridique |
| Séparation, divorce, procédure, garde, partage | 590 | Juridique |
| Petites créances, litige consommateur, réclamation, recours | 594 | Juridique |
| Copropriété, AG de copropriétaires, charges, travaux immeuble | 595 | Juridique |
| Contrat, clause, question juridique | 16 | Juridique |
| Courrier officiel, réclamation administrative | 137 | Juridique |
| Anonymisation RGPD de données | 189 | Juridique |
| Document de conformité, politique, registre | 190 | Juridique |
| Charte IA d'entreprise, usage responsable | 193 | Juridique |
| Registre RGPD, traitement de données | 196 | Juridique |
| Veille réglementaire, nouvelle règle du secteur | 239 | Juridique |
| AI Act, classification des risques IA | 271 | Juridique |
| AIPD, analyse d'impact protection des données | 272 | Juridique |
| CGV, conditions de vente | 374 | Juridique |
| Durée de conservation, archivage RGPD | 442 | Juridique |
| CGU, mentions légales de site | 443 | Juridique |
| Violation de données, notifier l'autorité | 444 | Juridique |
| Clause sous-traitant, DPA RGPD | 446 | Juridique |
| NDA, accord de confidentialité | 448 | Juridique |
| **Langues** | | |
| Traduire | 7 | Langues |
| Liste de vocabulaire par thème | 491 | Langues |
| Phonétique, accent, prononcer | 492 | Langues |
| DELF, TOEFL, examen de langue | 493 | Langues |
| **Marketing** | | |
| Moteurs IA, GEO, citations ChatGPT & Perplexity, visibilité dans les réponses | 612 | Marketing |
| Délivrabilité email, SPF, DKIM, DMARC, arrivée en boîte | 586 | Marketing |
| Accroche, pub, promo, conversion | 3 | Marketing |
| Script vidéo courte, UGC, TikTok, pub vidéo | 29 | Marketing |
| Post social à optimiser, portée, engagement | 30 | Marketing |
| Post LinkedIn, personal branding, autorité | 31 | Marketing |
| Benchmark, concurrents, positionnement | 32 | Marketing |
| Persona, profil cible utilisateur | 33 | Marketing |
| Respect de la charte, cohérence de marque | 34 | Marketing |
| Newsletter, email récurrent, liste email | 51 | Marketing |
| Script vidéo long format, chaîne YouTube | 52 | Marketing |
| Décliner, repurposer un contenu, semaine multi-canal | 53 | Marketing |
| Fiche produit e-commerce, description SEO en série | 118 | Marketing |
| Page de vente, landing copywriting | 123 | Marketing |
| Étude de cas client, success story | 124 | Marketing |
| Livre blanc, guide expert long | 125 | Marketing |
| Calendrier éditorial, planning de contenus | 135 | Marketing |
| Audit SEO technique, santé du site | 161 | Marketing |
| Optimisation de conversion (CRO) | 162 | Marketing |
| Lancement produit, go-to-market | 163 | Marketing |
| Programme de fidélité, rétention client | 173 | Marketing |
| Lead magnet, contenu contre email | 174 | Marketing |
| Animation de communauté, croissance de base | 175 | Marketing |
| Hook TikTok, titre viral, trois premières secondes | 278 | Marketing |
| Fiche produit e-commerce, avis des concurrents | 279 | Marketing |
| Publicité concurrente, bibliothèque de créas | 356 | Marketing |
| Séquence d'emails, drip campaign | 357 | Marketing |
| Segmentation de liste, hygiène d'audience | 358 | Marketing |
| SMS marketing, message court | 359 | Marketing |
| Fiche établissement, SEO local | 360 | Marketing |
| Campagne influence, brief de créateur | 361 | Marketing |
| Cohérence de marque cross-canal | 362 | Marketing |
| Transcréation, adapter une campagne à un marché | 363 | Marketing |
| Quiz lead magnet, formulaire interactif | 364 | Marketing |
| Carrousel LinkedIn, slides éditoriaux | 365 | Marketing |
| Social listening, mention de marque | 366 | Marketing |
| Page VS, alternative à, comparatif SEO | 367 | Marketing |
| Parcours client, journey map | 373 | Marketing |
| Panier moyen, upsell, cross-sell | 375 | Marketing |
| **Personnel** | | |
| Stress, anxiété, gestion des tensions au quotidien | 511 | Personnel |
| Parentalité, éducation des enfants, cadres bienveillants | 520 | Personnel |
| Arnaque en ligne, sms frauduleux, faux support, fraude grand public | 530 | Personnel |
| Baby-sitting, premiers jobs adolescents, garde d'enfants | 533 | Personnel |
| Sorties culturelles, expo, concert, programme culturel | 536 | Personnel |
| Animaux, chien, chat, éducation canine, santé animale | 556 | Personnel |
| Style vestimentaire, garde-robe, couleurs, silhouette | 558 | Personnel |
| Discours de mariage, toast familial, hommage, anniversaire | 564 | Personnel |
| Fête de famille, mariage, anniversaire, organisation réception | 565 | Personnel |
| Apprendre à cuisiner, techniques de base, repas de la semaine | 566 | Personnel |
| Films, séries, livres, recommandations culturelles personnalisées | 568 | Personnel |
| Plantes d'intérieur, arrosage, rempotage, plantes qui souffrent | 578 | Personnel |
| Désencombrement, rangement, organisation maison, tri | 579 | Personnel |
| Seniors, numérique, premiers pas smartphone, assistance aînés | 581 | Personnel |
| Course à pied, plan d'entraînement, 10 km, semi-marathon | 582 | Personnel |
| Randonnée, itinéraire, équipement outdoor, sécurité en montagne | 583 | Personnel |
| Dégustation, vin, café, initiation, accords | 584 | Personnel |
| Miles, points fidélité, programmes voyageurs, billets avantage | 585 | Personnel |
| Médiation familiale, conflit famille, succession, dialogue | 589 | Personnel |
| Colocation, contrat colocation, vie commune, loyers partagés | 592 | Personnel |
| Mutuelle, remboursements santé, frais médicaux, choix de couverture | 593 | Personnel |
| Voyage, itinéraire, séjour sur mesure | 42 | Personnel |
| Budget, dépenses, finances personnelles | 43 | Personnel |
| Message d'occasion, vœux, faire-part | 136 | Personnel |
| Programme sportif, plan d'entraînement | 214 | Personnel |
| Plan nutritionnel, alimentation équilibrée | 215 | Personnel |
| Recettes avec contraintes, menu du frigo | 216 | Personnel |
| Cadeau personnalisé, liste d'idées | 218 | Personnel |
| Comparateur d'achat, quel produit choisir | 219 | Personnel |
| Rénovation, travaux de logement | 220 | Personnel |
| Domotique, scénarios d'objets connectés | 222 | Personnel |
| Déménagement, logistique et checklist | 225 | Personnel |
| Potager, calendrier de semis | 229 | Personnel |
| Succession numérique, comptes et volontés | 246 | Personnel |
| Équilibre pro-perso, charge et récupération | 248 | Personnel |
| Panne domestique, diagnostiquer lave-linge ou chaudière | 291 | Personnel |
| Entretien voiture, échéancier kilométrique | 292 | Personnel |
| Visite immobilière, checklist d'appartement | 296 | Personnel |
| Impact carbone du numérique, sobriété | 470 | Personnel |
| Trier les photos de famille, sauvegarder les souvenirs | 472 | Personnel |
| Devis travaux, cahier des charges artisan | 473 | Personnel |
| Garantie, ticket SAV, devis de réparation | 474 | Personnel |
| Déménager à l'étranger, visa, installation | 476 | Personnel |
| Plan d'urgence, contacts, kit de crise | 477 | Personnel |
| Liste de courses, inventaire de la maison | 478 | Personnel |
| Négocier une voiture, un devis d'artisan | 479 | Personnel |
| Inventaire pour l'assurance, valeur des biens | 480 | Personnel |
| Planning familial, gardes, activités des enfants | 481 | Personnel |
| Accompagner un parent âgé, charge d'aidant | 482 | Personnel |
| Hygiène du sommeil, insomnie | 483 | Personnel |
| Poste de travail, douleurs assis | 484 | Personnel |
| Dépistage, vaccins, suivi médical | 485 | Personnel |
| Batch cooking, repas de la semaine | 486 | Personnel |
| Péremption des médicaments, trousse | 487 | Personnel |
| Arrêter de fumer, sucre, écrans | 488 | Personnel |
| Routine matinale, habitudes qui tiennent | 489 | Personnel |
| Souvenirs des grands-parents, histoire orale | 490 | Personnel |
| **Productivité** | | |
| Briefing du matin, digest multi-projets, point du jour, standup écrit | 611 | Productivité |
| Obsidian, vault, notes liées, markdown, Dataview | 539 | Productivité |
| Résumer, condenser un document | 5 | Productivité |
| Compte rendu, PV, notes de réunion | 24 | Productivité |
| Boîte mail débordante, prioriser des emails | 25 | Productivité |
| Tâche trop grosse, procrastination, où commencer | 26 | Productivité |
| Document Word / Excel / PowerPoint à produire | 27 | Productivité |
| Suivi de mission multi-sessions documenté | 28 | Productivité |
| SOP, procédure, playbook, workflow répétable | 50 | Productivité |
| Automatisation, workflow entre outils, n8n/Make/Zapier | 71 | Productivité |
| Planifier ma semaine, time blocking, planning perso | 72 | Productivité |
| Base de connaissances, architecture d'infos | 114 | Productivité |
| Préparation de réunion, ordre du jour | 209 | Productivité |
| To-do list, priorisation de journée | 223 | Productivité |
| Template de document, modèle réutilisable | 245 | Productivité |
| Saisie web répétitive, automatiser un formulaire | 269 | Productivité |
| Trouver un créneau à plusieurs, rendez-vous multi-fuseaux | 284 | Productivité |
| Suivi des actions de réunion, registre d'action items | 285 | Productivité |
| Trier mes dossiers, renommer mes fichiers, doublons | 286 | Productivité |
| Trop de réunions, audit du calendrier | 463 | Productivité |
| Read-it-later, pile de lectures, flux RSS | 464 | Productivité |
| Deep work, concentration longue | 465 | Productivité |
| Horaires tournants, planning d'équipe | 466 | Productivité |
| Checklist d'aviateur, tâche à ne pas rater | 467 | Productivité |
| Suivi perso, habitudes, temps | 468 | Productivité |
| Règles de tri, filtres automatiques | 469 | Productivité |
| Dicter au lieu d'écrire, workflow vocal | 471 | Productivité |
| Combien de temps ça prendra vraiment | 475 | Productivité |
| **Produit** | | |
| Plan de test manuel, scénarios de recette, critères d'acceptation vérifiables | 605 | Produit |
| Gameplay, équilibrage, boucle de jeu, game design | 575 | Produit |
| PRD, user stories, exigences produit, backlog | 63 | Produit |
| Roadmap produit, narration de priorités | 176 | Produit |
| Plan de tests fonctionnels, recette QA | 178 | Produit |
| Activation produit, premier moment de valeur | 179 | Produit |
| Dépréciation, retrait propre de fonctionnalité | 183 | Produit |
| Tri de tickets support, file de demandes | 184 | Produit |
| Priorisation de backlog, ordre de travail | 185 | Produit |
| Interview utilisateur, guide d'entretien | 187 | Produit |
| Synthèse de recherche utilisateur | 188 | Produit |
| Gamification, mécaniques d'engagement | 300 | Produit |
| Arborescence de site, navigation, menus | 451 | Produit |
| Guide in-app, tooltip d'onboarding | 453 | Produit |
| Freemium, paliers d'abonnement, packaging | 457 | Produit |
| Rôles utilisateur, qui voit quoi | 458 | Produit |
| Bêta-testeurs, recrutement de testeurs | 459 | Produit |
| Dark pattern, désinscription honnête | 460 | Produit |
| Parcours d'inscription, KYC | 461 | Produit |
| Guide de migration, changement côté client | 462 | Produit |
| **Produit & IA** | | |
| Chatbot, intents, flux conversationnel | 66 | Produit & IA |
| **Recherche** | | |
| Rechercher un sujet, veille, état du marché | 18 | Recherche |
| Cartographie de concepts, explicateur visuel d'idées | 101 | Recherche |
| Interroger ses documents personnels (RAG local) | 102 | Recherche |
| Lecture d'études scientifiques, papier de recherche | 104 | Recherche |
| Veille hebdomadaire consolidée | 105 | Recherche |
| Signaux faibles, tendance émergente | 290 | Recherche |
| **Rédaction** | | |
| Poésie, écrire des poèmes, atelier d'écriture | 534 | Rédaction |
| Journal intime, écriture réflexive, journaling | 535 | Rédaction |
| Récit de vie, biographie familiale, mémoire d'un proche | 537 | Rédaction |
| Humaniser un texte IA, tics d'écriture IA, voix naturelle | 538 | Rédaction |
| Écrire un article, blog, contenu web | 1 | Rédaction |
| Adapter le ton / reformuler un texte existant | 2 | Rédaction |
| Corriger, relire, améliorer style | 8 | Rédaction |
| Document long, rapport de 50 pages | 116 | Rédaction |
| Traduction en conservant le format du document | 117 | Rédaction |
| FAQ, foire aux questions depuis un guide | 119 | Rédaction |
| Détection de texte IA, plagiat, authenticité | 120 | Rédaction |
| Guide utilisateur, manuel pas à pas | 130 | Rédaction |
| Citations, bibliographie, références académiques | 133 | Rédaction |
| Définitions, glossaire de termes métier | 134 | Rédaction |
| Localisation i18n, traduire une application | 280 | Rédaction |
| Contrat en langage clair, vulgariser une clause | 281 | Rédaction |
| Tutoriel pas-à-pas, procédure illustrée | 299 | Rédaction |
| Niveau de lecture, phrase trop longue | 377 | Rédaction |
| Transcription à nettoyer, verbatim d'interview | 378 | Rédaction |
| Notification push, message système | 379 | Rédaction |
| Thread long, post enchaîné éditorial | 380 | Rédaction |
| Dialogue de jeu vidéo, réplique de fiction | 381 | Rédaction |
| Aventure interactive, histoire à choix | 382 | Rédaction |
| Critique produit, comparatif d'achat | 383 | Rédaction |
| Script d'épisode de podcast | 384 | Rédaction |
| Titre et description YouTube, tags | 385 | Rédaction |
| Pitcher un journaliste, media pitch | 386 | Rédaction |
| Kit média, dossier de presse | 387 | Rédaction |
| Interview par email, questions à distance | 388 | Rédaction |
| Test 5 secondes, premier rendu d'un contenu | 389 | Rédaction |
| Message d'erreur utile, écran d'échec | 390 | Rédaction |
| Alt-text, description d'image accessible | 391 | Rédaction |
| Webinaire, script de présentation en ligne | 392 | Rédaction |
| Tribune, op-ed, prise de position | 393 | Rédaction |
| Macro de réponse, gabarit de support | 394 | Rédaction |
| Avant de publier, vérifier un contenu sensible | 395 | Rédaction |
| Texte de couverture, résumé de livre | 396 | Rédaction |
| **RH & formation** | | |
| Interculturel, travailler entre cultures, équipes multiculturelles | 549 | RH & formation |
| Neurodiversité, TDAH, dys, aménagements au travail | 550 | RH & formation |
| Fiche de poste, offre d'emploi | 202 | RH & formation |
| Onboarding collaborateur, parcours d'arrivée | 203 | RH & formation |
| Compétences d'équipe à cartographier | 205 | RH & formation |
| Évaluation annuelle, entretien d'objectifs | 206 | RH & formation |
| Politique interne RH, télétravail, congés | 207 | RH & formation |
| Employer branding, marque employeur | 233 | RH & formation |
| Programme de mentorat, appariement et jalons | 234 | RH & formation |
| Screening de CV, short-list de candidatures | 274 | RH & formation |
| Offboarding, départ d'un collaborateur | 275 | RH & formation |
| Grille d'entretien de recrutement, échelle de notation | 276 | RH & formation |
| Auto-évaluation annuelle, bilan de réalisations | 277 | RH & formation |
| Plan de développement, PDI, progression | 407 | RH & formation |
| Annonce d'emploi, offre d'emploi | 408 | RH & formation |
| Plan de succession, relève des managers | 409 | RH & formation |
| Écart salarial, équité de rémunération | 410 | RH & formation |
| Programme de stage, alternance | 411 | RH & formation |
| Télétravail, accord de travail hybride | 412 | RH & formation |
| Exit interview, pourquoi il part | 413 | RH & formation |
| Changer de poste en interne, mobilité | 414 | RH & formation |
| Évaluation 360, retours multi-sources | 415 | RH & formation |
| Financer une formation, budget formation | 416 | RH & formation |
| Formation obligatoire, recyclage sécurité | 417 | RH & formation |
| Nouveau manager, premiers 90 jours | 418 | RH & formation |
| Feedback anonyme, boîte à idées | 419 | RH & formation |
| Couvrir les congés, planning de remplacement | 420 | RH & formation |
| Surcharge de travail, répartition | 421 | RH & formation |
| Lettre de recommandation, référence d'ancien | 422 | RH & formation |
| **Routage** | | |
| Faire évoluer le catalogue, ajouter une skill | 250 | Routage |
| **Sécurité** | | |
| Deepfake, désinformation, vérification d'image, fiabilité source | 561 | Sécurité |
| Sauvegarde personnelle, règle 3-2-1, perte de données, restauration | 596 | Sécurité |
| Contrôle parental, filtrage, temps d'écran, protections enfants | 597 | Sécurité |
| Détection de fraude, anomalies de logs | 191 | Sécurité |
| Garde-fous d'agent, limites d'autonomie | 194 | Sécurité |
| Injection de prompt, durcissement anti-piège | 195 | Sécurité |
| Audit de permissions, contrôle d'accès | 197 | Sécurité |
| Runbook de sécurité, réponse à incident | 199 | Sécurité |
| Consignes de sécurité, affiche d'atelier | 244 | Sécurité |
| Hygiène numérique, comptes à assainir | 247 | Sécurité |
| SBOM, inventaire de dépendances, licence | 267 | Sécurité |
| Pentest, test d'intrusion planifié | 439 | Sécurité |
| Chasse aux menaces, IOC, règles Sigma | 440 | Sécurité |
| Forensique numérique, chronologie d'incident | 441 | Sécurité |
| Contrôle d'accès physique, badges | 445 | Sécurité |
| Données exposées, credentials fuittés | 447 | Sécurité |
| Authentification, MFA, SSO, sessions | 501 | Sécurité |
| En-têtes HTTP, CSP, cookies, CORS | 502 | Sécurité |
| WordPress, CMS piraté, plugins | 503 | Sécurité |
| Modélisation de menaces, STRIDE, scénarios d'attaque | 504 | Sécurité |
| Correctifs, CVE, plan de remédiation | 505 | Sécurité |
| Chiffrement, TLS, certificats, clés | 506 | Sécurité |
| Sécurité cloud, buckets exposés, IAM cloud | 507 | Sécurité |
| Pipeline CI/CD, supply chain, artefacts signés | 508 | Sécurité |
| Simulation de phishing, faux emails, résilience | 509 | Sécurité |
| Réseau local, Wi-Fi, segmentation, VPN | 510 | Sécurité |
| **Stratégie** | | |
| Revue CTO, arbitrages techniques, scalabilité, build vs buy | 602 | Stratégie |
| SWOT, forces faiblesses opportunités menaces, analyse de position | 613 | Stratégie |
| Vision, mission, valeurs d'entreprise, cadre stratégique | 551 | Stratégie |
| Modèle économique, business model, BMC | 57 | Stratégie |
| Prix, tarification, paliers, abonnement à chiffrer | 58 | Stratégie |
| Prémortem, risques projet avant lancement | 60 | Stratégie |
| Analyse de marché sectoriel, acteurs et taille | 103 | Stratégie |
| Partenariat stratégique, alliance | 436 | Stratégie |
| **Vente** | | |
| Prospection, cold email, démarchage commercial | 54 | Vente |
| Verbatims, avis clients, analyse de feedback, NPS | 55 | Vente |
| Macros support, réponses types, base de connaissances client | 56 | Vente |
| Scoring de leads, priorisation commerciale | 111 | Vente |
| Analyse win/loss, deals perdus | 112 | Vente |
| Témoignages clients à collecter | 131 | Vente |
| Battlecard commercial, argumentaire concurrentiel | 164 | Vente |
| Script d'appel commercial, cold call | 165 | Vente |
| Gestion d'objections, entraînement commercial | 166 | Vente |
| Business review client, réunion de suivi | 167 | Vente |
| Réponse à appel d'offres, proposition technique | 168 | Vente |
| Mise à jour du CRM, compte rendu d'appel client | 270 | Vente |
| Répondre aux avis Google, Trustpilot | 282 | Vente |
| Démo client personnalisée, démonstration ciblée | 368 | Vente |
| Grille tarifaire, paliers d'offre | 369 | Vente |
| Négocier un contrat client, clauses commerciales | 370 | Vente |
| Facture impayée, relance client, recouvrement | 371 | Vente |
| Prévision du pipeline, forecast commercial | 372 | Vente |
| Reporting commercial, chiffres de vente hebdo | 376 | Vente |

**Arbre de décision** :

```mermaid
flowchart TD
    S[Message utilisateur] --> Q1{Produire du neuf ?}
    Q1 -->|Oui| Q1a{Texte ?}
    Q1a -->|Article/contenu web| K1[Skill 1]
    Q1a -->|Publicité| K3[Skill 3]
    Q1a -->|Email| K4[Skill 4]
    Q1a -->|Code| K9[Skill 9]
    Q1a -->|Deck| K14[Skill 14]
    Q1 -->|Non| Q2{Améliorer l'existant ?}
    Q2 -->|Oui| Q2a{Quel support ?}
    Q2a -->|Texte : ton/réécriture| K2[Skill 2]
    Q2a -->|Orthographe/style| K8[Skill 8]
    Q2a -->|Langue différente| K7[Skill 7]
    Q2a -->|Code : bug/review| K10[Skill 10]
    Q2 -->|Non| Q3{Comprendre / analyser ?}
    Q3 -->|Concept à apprendre| K11[Skill 11]
    Q3 -->|Document à condenser| K5[Skill 5]
    Q3 -->|Données à interpréter| K13[Skill 13]
    Q3 -->|Question juridique| K16[Skill 16]
    Q3 -->|Recherche sur un sujet| K18[Skill 18]
    Q3 -->|Non| Q4{Décider / organiser ?}
    Q4 -->|Idées| K6[Skill 6]
    Q4 -->|Plan projet| K15[Skill 15]
    Q4 -->|Entretien à préparer| K12[Skill 12]
    Q4 -->|Non| Q5{Optimiser l'IA elle-même ?}
    Q5 -->|Oui| K17[Skill 17]
    Q5 -->|Non| Q6{Autre besoin métier ?}
    Q6 -->|Dev avancé| D1[19 Grill Me · 20 Debug · 21 Incrémental · 22 Diagrammes · 23 Doc]
    Q6 -->|Bureau & suivi| D2[24 CR · 25 Inbox · 26 Découpage · 27 Office · 28 Fichiers]
    Q6 -->|Marketing & marque| D3[29 UGC · 30 Social · 31 LinkedIn · 32 Benchmark · 33 Personas · 34 Charte]
    Q6 -->|Data & méta-IA| D4[35 Reco · 36 KPI · 37 Red-team · 38 Skill Creator · 48 Infographie]
    Q6 -->|Apprendre & perso| D5[39 Socrate · 40 Quiz · 41 Examen · 42 Voyage · 43 Budget]
    Q6 -->|Carrière & relations| D6[44 CV · 45 Négociation · 46 Conflits · 49 Rôle]
    Q6 -->|Structurer & nommer| D7[47 Naming · 50 SOP]
    Q6 -->|Contenus & créateurs| D8[51 Newsletter · 52 YouTube · 53 Repurposing · 75 Discours]
    Q6 -->|Vendre & servir le client| D9[54 Prospection · 55 Feedback · 56 Support · 62 Propositions]
    Q6 -->|Stratégie & pilotage| D10[57 BMC · 58 Prix · 59 Finances · 60 Prémortem · 61 Diable · 74 OKR · 602 Revue CTO · 613 SWOT]
    Q6 -->|Produit & design| D11[63 PRD · 64 Critique UX · 65 Microcopy · 66 Chatbot]
    Q6 -->|Dev qualité & ops| D12[67 Tests · 68 Commits/PR · 69 SQL · 70 Sécurité · 71 Workflows]
    Q6 -->|Organisation d'équipe| D13[72 Semaine · 73 Rétro · 611 Briefing du matin]
    Q6 -->|Agents & IA| D14[76 Agents CLI · 77 MCP · 96 Datasets · 97 Evals · 98 RAG · 99 Outils · 100 Instructions · 224 Autonomes · 236 Contexte · 237 Debug prompts · 238 Annotation · 251 Handoff · 259 Multi-agents · 260 Mémoire · 261 Déclenchement · 262 Audit skills · 288 Vocal · 325 Curateur skills · 326 Budget tokens · 327 Compresseur réponses · 328 Routines agents · 329 Contrôle humain · 330 Observateur agents · 331 Modèles légers · 332 Schémas sortie · 333 Benchmarks · 334 Traducteur prompts · 335 Personnalité agent · 336 Biais modèles · 337 Cartes modèle · 338 Régression prompts · 339 Test fantôme · 340 Robustesse agents · 341 Contrats tâche · 342 Dérive modèle · 601 Revue session · 615 Auto-amélioration · 616 TDAH-friendly]
    Q6 -->|Craft & data| D15[79 API · 83 Transpile · 84 Algos · 85 IaC · 86 Migrations · 87 OpenAPI · 88 ADR · 91 Scraping · 92 Nettoyage · 94 Pipelines · 95 Carto data · 242 Open data · 254 Mocks · 255 Charge · 257 Explorateur · 263 Synthétiques · 267 SBOM · 269 Web répétitif · 301 Worktrees · 303 SemVer · 304 Feature flags · 306 Secrets · 307 Montée versions · 311 Conventions code · 312 README · 313 Monorepo · 316 Jardinier Git · 318 SQL lentes · 319 Jobs async · 320 Rate limits · 321 Schémas BDD · 322 Webhooks · 324 Scripts CLI · 343 Qualité données · 349 Tests données · 350 dbt · 354 Sources hétérogènes]
    Q6 -->|Ops & qualité| D16[78 No-code · 80 Legacy · 82 DevOps · 89 Post-mortem · 90 FinOps · 178 QA · 184 Tickets · 199 Runbooks · 243 Audits internes · 244 Sécurité atelier · 252 E2E · 253 Perfs web · 256 Incidents · 302 TDD · 305 Env reproductible · 308 Profileur · 309 Bench code · 310 Fuzzing · 314 Conteneurisation · 315 Bisect · 317 Tests intégration · 323 Builds · 603 Régressions visuelles · 604 Contrats d'API · 605 Plans de test · 606 Sprint dette · 607 Publication mobile · 609 Kubernetes · 614 Pré-déploiement]
    Q6 -->|Analyse & pilotage| D17[93 Prédictif · 101 Concepts · 102 RAG perso · 103 Marché · 104 Études · 105 Veille · 106 Cohortes · 107 Dashboards · 108 Storytelling · 109 Funnels · 110 A/B · 113 Enquêtes · 115 Reçus · 186 Tracking · 264 Excel · 265 Coûts LLM · 266 FT vs RAG · 344 Métriques · 345 Séries temporelles · 346 Anomalies · 347 Formules Excel · 348 Données géo · 351 SLI/SLO · 352 Heatmaps · 353 Propension · 355 Verbatims · 427 Business cases]
    Q6 -->|Rédaction experte| D18[116 Longs · 117 Traduction · 118 Fiches · 119 FAQ · 120 Plagiat · 121 Créative · 122 Pitchs · 127 Mémos · 128 Bios · 129 Release notes · 130 Guides · 133 Citations · 134 Glossaires · 137 Courriers · 226 Lectures · 245 Templates · 268 PDF · 280 i18n · 281 Contrats clairs · 299 Pas-à-pas · 377 Lisibilité · 378 Transcriptions · 379 Notifications · 380 Threads · 381 Dialogues · 382 Fiction interactive · 383 Comparatifs · 384 Scripts podcast · 385 Métadonnées YouTube · 386 Pitches médias · 387 Kits média · 388 Interview écrit · 389 Test 5 secondes · 390 Messages d erreur · 391 Alt-text · 392 Webinaires · 393 Tribunes · 394 Macros support · 395 Pré-publication · 396 Quatrièmes couverture]
    Q6 -->|Visuel & audio| D19[139 Images · 140 Photos · 141 Vectoriel · 142 3D · 143 Mockups · 144 Vidéo · 145 Avatars · 146 Storyboard · 147 Miniatures · 148 Moodboards · 149 Palettes · 150 Styles · 151 Illustrations · 152 Briefs DA · 153 Wireframes · 154 Voix · 155 Musique · 156 Audio · 157 Podcasts · 158 Sous-titres · 159 Jingles · 160 SFX · 258 Vidéo programmatique · 283 Variantes]
    Q6 -->|Marketing & croissance| D20[123 Pages de vente · 124 Cas clients · 125 Livres blancs · 126 Presse · 135 Éditorial · 136 Occasions · 161 SEO · 162 CRO · 163 Lancement · 173 Fidélité · 174 Lead magnets · 175 Communauté · 278 Hooks · 279 Concurrents · 290 Signaux faibles · 356 Ads concurrentes · 357 Séquences email · 358 Audiences · 359 SMS courts · 360 Présence locale · 361 Influenceurs · 362 Marque 360 · 363 Transcréation · 364 Quiz marketing · 365 Carrousels · 366 Social listening · 367 Alternatives · 373 Parcours client · 375 Upsell · 402 Points presse · 403 Déclarations · 612 GEO moteurs IA]
    Q6 -->|Vente & finance| D21[111 Leads · 112 Win/loss · 131 Témoignages · 164 Battlecards · 165 Appels · 166 Objections · 167 Reviews · 168 Appels d'offres · 169 Marges · 170 Prévisionnel · 171 Levée · 172 Investisseurs · 270 CRM · 282 Avis · 298 Crédit · 368 Démos · 369 Grilles tarifaires · 370 Contrats commerciaux · 371 Factures impayées · 372 Pipeline · 376 Reporting commercial]
    Q6 -->|Produit & design| D22[81 Composants UI · 138 Emails transactionnels · 176 Roadmap · 177 Accessibilité · 179 Activation · 180 Doc API · 181 Design system · 182 Formulaires · 183 Dépréciation · 185 Backlog · 187 Interviews · 188 Synthèse UX · 300 Gamification · 449 Anti générique · 450 États vides · 451 Navigation · 452 Erreurs UI · 453 Activation in-app · 454 Accessibilité · 455 Design tokens · 456 Expérience mobile · 457 Paliers offre · 458 Rôles produit · 459 Bêta · 460 Dark patterns · 461 Inscription · 462 Migration clients · 608 Design to code]
    Q6 -->|Sécurité & conformité| D23[189 Anonymisation · 190 Conformité · 191 Fraudes · 192 Modération · 193 Charte IA · 194 Garde-fous · 195 Injection · 196 Registres · 197 Permissions · 198 Fournisseurs · 200 Sensibilisation · 239 Réglementaire · 271 AI Act · 272 AIPD · 273 PRA · 374 CGV · 406 Chartes modération · 439 Pentest · 440 Menaces · 441 Forensique · 442 Archivage · 443 CGU · 444 Violation données · 445 Sécurité physique · 446 DPA · 447 Fuites données · 448 NDA · 501 Auth · 502 En-têtes · 503 WordPress · 504 Menaces · 505 Correctifs · 506 Chiffrement · 507 Cloud · 508 CI/CD · 509 Phishing · 510 Réseau · 610 SOC 2]
    Q6 -->|RH & formation| D24[132 Enfants · 201 Formations · 202 Postes · 203 Onboarding · 204 Progression · 205 Compétences · 206 Évaluations · 207 Politiques RH · 231 Reconversion · 233 Employer branding · 234 Mentorat · 274 Screening · 275 Offboarding · 276 Grilles entretien · 277 Auto-éval · 295 Microlearning · 407 Plans dev · 408 Offres emploi · 409 Succession · 410 Équité salariale · 411 Stages · 412 Télétravail · 413 Départs · 414 Mobilité · 415 Feedback 360 · 416 Financement formation · 417 Formations obligatoires · 418 Managers débutants · 419 Feedback anonyme · 420 Continuité · 421 Charge travail · 422 Recommandations]
    Q6 -->|Organisation & équipe| D25[114 Bases de connaissances · 208 Ateliers · 209 Réunions · 210 Décisions · 211 Team building · 232 Rituels · 235 Crise · 284 RDV · 285 Actions · 286 Nettoyage · 287 Zettelkasten · 289 Multilingue · 397 Q&A live · 398 Briefs agences · 399 Matrice ton · 400 PV · 401 Jargon · 404 Messages changement · 405 Experts internes · 423 Messages entreprise · 424 Chartes équipe · 425 Coûts projet · 426 Parties prenantes · 428 Maturité équipe · 429 Portefeuille · 430 Post-fusion · 431 SLA fournisseurs · 432 Communautés pratique · 433 Processus métier · 434 RACI · 435 Registre risques · 436 Partenariats · 437 Sprints design · 438 Rapports annuels · 463 Calendrier réunions · 464 Système lecture · 465 Travail profond · 466 Horaires atypiques · 467 Checklists · 468 Dashboard perso · 469 Filtres email · 471 Dictée vocale · 475 Estimation temps]
    Q6 -->|Vie quotidienne & divers| D26[212 Langues · 213 Flashcards · 214 Sport · 215 Nutrition · 216 Recettes · 217 Démarches · 218 Cadeaux · 219 Achats · 220 Rénovation · 221 Événements · 222 Domotique · 223 To-do · 225 Déménagement · 227 Investissement · 228 Jeux · 229 Potager · 230 Abonnements · 240 Subventions · 241 Soutenances · 246 Succession · 247 Hygiène numérique · 248 Équilibre · 249 Retraite · 250 Conservateur · 291 Pannes · 292 Auto · 293 Éloquence · 294 Augmentation · 296 Immobilier · 297 Fiscal · 470 Empreinte carbone · 472 Archiviste familial · 473 Cahiers travaux · 474 Garanties · 476 Expatriation · 477 Plan urgence · 478 Garde-manger · 479 Négociation achats · 480 Inventaire foyer · 481 Logistique familiale · 482 Aidants · 483 Sommeil · 484 Ergonomie · 485 Bilans santé · 486 Batch cooking · 487 Pharmacie · 488 Arrêt habitudes · 489 Routines · 490 Mémoires familiales · 491 Vocabulaire · 492 Prononciation · 493 Examens langue · 494 Plans lecture · 495 Mémorisation · 496 Répétition espacée · 497 Cours en ligne · 498 Notes méthodiques · 499 Enseigner · 500 Parcours perso]
    Q6 -->|Quotidien, santé & famille (vague 8)| D27[511 Stress · 520 Parentalité · 530 Arnaques · 533 Baby-sitting · 536 Sorties culturelles · 556 Animaux · 558 Style · 564 Discours famille · 565 Fêtes famille · 566 Cuisine · 568 Culture · 578 Plantes · 579 Désencombrement · 581 Seniors numériques · 582 Running · 583 Rando · 584 Dégustation · 585 Miles · 589 Médiation famille · 592 Colocation · 593 Mutuelles · 596 Sauvegardes · 597 Contrôle parental]
    Q6 -->|Créativité & apprentissage (vague 8)| D28[515 Théâtre · 516 Chant · 517 Danse · 518 Instrument · 521 Montage vidéo · 522 Photo · 546 Prompt images · 557 Créatifs manuels · 559 Maths · 560 Thèse · 567 Stratégie jeux · 569 Musées · 570 Devoirs · 571 Orientation · 573 Chansons · 574 Retouche · 576 Streamer · 580 Code · 591 Bourses]
    Q6 -->|Pro, business & droit (vague 8)| D29[512 Crypto · 513 Web3 · 519 Bourse · 527 Franchise · 528 Surendettement · 529 Voisinage · 531 Droit image · 532 Bénévolat · 534 Poésie · 535 Journal intime · 537 Récits de vie · 538 Humaniseur IA · 539 Obsidian · 541 Audit budget · 548 Marque perso · 549 Interculturel · 550 Neurodiversité · 551 Vision · 552 Association · 553 Licences OSS · 554 Location · 555 Droit travail · 562 Micro-entreprise · 563 Finances freelance · 572 Portfolio · 586 Délivrabilité · 587 Logistique e-com · 588 Compta TPE · 590 Séparation · 594 Petites créances · 595 Copropriété · 599 Tarifs freelance · 600 Bilan]
    Q6 -->|Dev, data, IA & produit (vague 8)| D30[514 Robotique · 523 Regex · 524 Game dev · 525 Dev mobile · 526 API design · 540 Vibe coding · 542 Admin BDD · 543 Extraction OCR · 544 Bots · 545 Site statique · 547 Stats · 561 Deepfakes · 575 Gameplay · 577 Supervision IA · 598 Boucle prompts]
    Q6 -->|Aucun| F[Réponse directe+ suggestion de créer une skill]
```

**Variante « routage léger »** (pour petits modèles, à copier comme instruction système à la place du protocole complet) :

```text
Pour chaque demande, si un mot-clé canonique figure dans l'index inversé, route directement vers cette skill ; sinon identifie le domaine dominant via la carte des domaines, puis cherche la skill uniquement dans le bloc de ce domaine de la table de routage. Annonce « → Skill N » avant de répondre.
Si aucune skill ne convient, réponds directement.
À la fin, propose en une ligne une skill complémentaire si pertinent.
```

**Exemple de prompt** (message utilisateur → comportement du routeur) :
> Utilisateur : « J'ai un rapport de 40 pages sur nos ventes, fais-moi un truc pour le comité de direction. »
> Routeur : intentions = condenser (5) → deck (14). Annonce : « → Skill 5 puis Skill 14 ». Exécute la synthèse, puis construit le deck à partir du résumé, et termine en proposant la skill 8 si le texte doit être peaufiné.

**Cas d'usage** : assistant unique multi-usages, agent conversationnel, intégration de plusieurs skills dans un même chat sans que l'utilisateur ait à les choisir manuellement.

---

## 🧩 Comment utiliser ce catalogue

0. **Routage** (recommandé) : installez la skill 0 comme instruction système principale et ajoutez les 50 autres en bibliothèque consultable — l'assistant choisit et enchaîne les skills tout seul.
1. **Copier** le bloc « Instructions système » de la skill choisie comme prompt système (ou instruction de départ) de votre assistant IA.
2. **Personnaliser** : ajuster le ton, la langue et les contraintes à votre contexte.
3. **Combiner** : plusieurs skills se complètent (ex. 18 → 1 → 8 pour une étude publiée en article).
4. **Itérer** : ajoutez au prompt les corrections souhaitées après les premières sorties — c'est le principe de la skill 17.
5. **Corpus** : le sommaire, la carte des domaines, la table de routage et l'arbre décisionnel (skill 0) vivent dans ce canvas ; les sections détaillées sont réparties dans les canvases « corpus-skills-1-300 », « corpus-skills-301-600 » et « corpus-skills-601-900 » (plafond de taille d'un canvas oblige).

## 🌍 Sources d'inspiration

> 🔎 **Index** : Collections communautaires · Skills officielles & populaires · Articles & analyses

Les skills 19-50 s'inspirent des skills, prompts et workflows les plus populaires de la communauté IA ; les skills 51-75 d'une troisième vague de recherche web (créateurs, PM, sécurité, productivité) ; les skills 76-250 d'une quatrième vague : les « 100 compétences IA 2026 » (agents autonomes, MCP, data, création visuelle et audio, growth, gouvernance, RH, vie quotidienne). Sources principales :

**Collections communautaires de skills** :

- [awesome-claude-skills (ComposioHQ)](https://github.com/ComposioHQ/awesome-claude-skills) — 1000+ skills de production, toutes plateformes
- [awesome-claude-skills (travisvn)](https://github.com/travisvn/awesome-claude-skills) — liste consolidée, ressources et templates
- [awesome-agent-skills (VoltAgent)](https://github.com/VoltAgent/awesome-agent-skills) — 1000+ skills multi-agents (Claude, Codex, Cursor, Gemini CLI)
- [Awesome Claude (annuaire)](https://awesomeclaude.ai/awesome-claude-skills) — 241 skills avec commandes d'installation
- [Awesomeskill.ai](https://awesomeskill.ai/) — marketplace open-source de SKILL.md
- [AgenticSkills](https://agenticskills.io/skills) — annuaire filtrable, 16 catégories

**Skills officielles & populaires** :

- [Anthropic Skills (dépôt officiel)](https://github.com/anthropics/skills) — standard SKILL.md + skills de documents (docx/xlsx/pptx), charte de marque, diagrammes → skills 27, 34, 22, 38
- [Grill Me (Matt Pocock, AI Hero)](https://www.aihero.dev/skills-grill-me) — interview impitoyable de validation de plan → skill 19
- [Karpathy Behavioural Skill](https://composio.dev/content/top-claude-skills) — règles comportementales pour agents de code → skill 21
- [Superpowers (writing-skills)](https://github.com/obra/superpowers) — qualité des skills et échecs courants → skill 38
- [superCMO-skills](https://github.com/VoltAgent/awesome-agent-skills) — production vidéo UGC/publicité → skill 29

**Articles & analyses** :

- [Firecrawl — 14 Best Claude Code Skills](https://www.firecrawl.dev/blog/best-claude-code-skills) — patterns de qualité : description = règle de routage, code déterministe, exemples > règles
- [AGNT — The 100 Best AI Agent Skills](https://agnt.gg/articles/agents/100-best-ai-agent-skills) — diagrammes d'architecture, brand compliance → skills 22, 34
- [ODSC — The Ten Best Agent Skills](https://odsc.medium.com/the-ten-best-agent-skills-to-teach-your-ai-agent-in-2026-82bca1d1ffa0) — debugging systématique en 4 phases → skill 20
- [LogRocket — 10 best AI agent skills for senior engineers](https://blog.logrocket.com/top-ai-agent-skills-engineers/) — implémentation incrémentale → skill 21
- [AI UX Playground — grill-me](https://aiuxplayground.com/skills/grill-me) — la skill SKILL.md originale de stress-test de plans → skill 19
- [AlphaMatch — Grill Me Skill](https://www.alphamatch.ai/blog/grill-me-skill-ai-prompt-code-design-2026) — analyse du prompt complet et de ses limites → skill 19

**Vague 3 (skills 51-75) — création, produit, dev, pilotage** :

- [CreatorSkills — Best AI Prompts for Content Creators](https://creatorskills.co/blog/best-ai-prompts-content-creators-complete-guide-2026) — systèmes de newsletter et de scripts long format → skills 51, 52
- [AgentVolt — 12 Best AI Skills for YouTube Creators](https://www.agentvolt.ai/blog/12-best-ai-skills-for-youtube-creators-in-2026-ideas-scripts-thumbnails-sponsors) — scripts, miniatures, moteur de repurposing → skills 52, 53
- [ParallelHQ — Chatbot UX Design](https://www.parallelhq.com/blog/chatbot-ux-design) — conversation design : intents, repli humain, ton → skill 66
- [skills.rest — write-ux-microcopy](https://skills.rest/skill/write-ux-microcopy-dineshrevunuru) — microcopy d'interface : labels, erreurs, états vides → skill 65
- [CleverX — ChatGPT Prompts for Product Managers](https://cleverx.com/blog/chatgpt-prompts-for-product-managers/) — PRD, user stories, rétrospectives → skills 63, 73
- [deanpeters/product-manager-prompts](https://github.com/deanpeters/product-manager-prompts) — prémortem et exigences produit → skills 60, 63
- [AI PM Tools — OKR Drafting Prompts](https://aipmtools.org/ai-prompts/okr-drafting/) — OKR mesurables, baseline → cible, anti-triche → skill 74
- [Snyk — Top Claude Skills cybersécurité](https://snyk.io/fr/articles/top-claude-skills-cybersecurity-hacking-vulnerability-scanning/) — audit de vulnérabilités, scans OWASP → skill 70
- [TimOnWeb — 5 security skills pour Claude Code](https://timonweb.com/ai/i-checked-5-security-skills-for-claude-code-only-one-is-worth-installing/) — audit contextuel vs checklist aveugle → skill 70
- [bestclaudecodeskills — Testing & Security](https://bestclaudecodeskills.com/categories/testing-security) — skills de tests, approche test-first → skill 67

**Vague 4 (skills 76-250) — le grand élargissement, inspiré des « 100 compétences IA 2026 »** :

- [DataCamp — Top Agent Skills](https://www.datacamp.com/fr/blog/top-agent-skills) — agents de code, MCP, skills d'automatisation → skills 76, 77, 78, 82
- [Lessie — Best Claude Skills](https://lessie.ai/fr/blog/best-claude-skills) — veille concurrentielle, extraction d'insights, skill creator → skills 91, 105, 250
- [Jedha — 15 logiciels IA gratuits](https://www.jedha.co/formation-ia/les-15-meilleurs-logiciels-dintelligence-artificielle-gratuits) — transpilation, refactoring, présentations automatiques → skills 80, 83, 14
- [École Cube — Outils IA](https://www.ecole.cube.fr/blog/outils-ia) — prospection B2B, synthèse d'études, modération de communauté → skills 111, 104, 192
- [Sortlist — Meilleure IA](https://www.sortlist.fr/blog/meilleure-ia/) — RAG local, data mining prédictif, détection de plagiat → skills 102, 93, 120
- [Aixploria — Top 100 IA](https://www.aixploria.com/top-100-ia/) — génération vidéo, upscaling, mockups produits → skills 144, 140, 143
- [Skills4All — Quelle est l'IA la plus utilisée](https://www.skills4all.com/quelle-est-lia-la-plus-utilisee/) — dictée intelligente, filtrage d'emails, planification de voyages → skills 225, 25, 42
- [Yes-We-Prompt — Skills Claude](https://yes-we-prompt.fr/megaprompts-ia/skills-claude/) — lead scoring, buyer personas, ad copy → skills 111, 33, 3
- [Top-100 AI Tools (Scribd)](https://fr.scribd.com/document/700102207/Top-100-Ai-Tools-Fr-v2) — panorama des 100 compétences : longs documents, storytelling de données, recettes contraintes → skills 116, 108, 216

**Vague 5 (skills 251-300) — l'agentique et le quotidien, sourcée du web 2026** :

- [Firecrawl — Best Claude Code Skills](https://www.firecrawl.dev/blog/best-claude-code-skills) — handoff de session, tests E2E navigateur, incidents production, exploration de code → skills 251, 252, 256, 257
- [BrowserAct — Best Claude Skills](https://www.browseract.com/blog/best-claude-skills) — automatisation web répétitive, mocks d'API, mémoire longue durée, multi-agents → skills 269, 254, 260, 259
- [Powerdrill — Best AI Agent Skills](https://powerdrill.ai/blog/best-ai-agent-skills-to-automate-your-work) — manipulation de PDF, mise à jour de CRM, i18n, gamification → skills 268, 270, 280, 300

**Vague 6 (skills 301-500) — le cap des 500, sourcée du web 2026** :

- [AGNT — 100 Best AI Agent Skills](https://agnt.gg/articles/agents/100-best-ai-agent-skills) — worktrees Git, feature flags, secrets, tests d'intégration, SLI/SLO → skills 301, 304, 306, 317, 351
- [dev.to — I Tried 100 Claude Skills (Suraj Khaitan)](https://dev.to/suraj_khaitan) — profiling mémoire/CPU, fuzzing, benchmarks de code, README → skills 308, 310, 309, 312
- [BrowserAct — Best Claude Skills](https://www.browseract.com/blog/best-claude-skills) — rate limits, webhooks, monorepo, files d'attente → skills 320, 322, 313, 319
- [Walma AI — The best Claude skills in 2026](https://walma.ai/en/guides/skills/best-claude-skills) — hygiène de dépôt, tests de données, worktrees, README → skills 316, 349, 301, 312

**Vague 8 (skills 511-600) — les gaps de la sonde + le web 2026** :

- [Harvard Business Review — How People Are Really Using AI in 2026](https://hbr.org/2026/06/how-people-are-really-using-ai-in-2026) — vibe coding, usages réels du grand public → skills 540, 566, 581
- [Walma AI — The best Claude skills in 2026](https://walma.ai/en/guides/skills/best-claude-skills) — humaniseur de texte, pilote de vault Obsidian, compteur de tâches → skills 538, 539
- [DailyDime — AI Use Cases](https://dailydime.com/ai-use-cases/) — audit de budget, finances personnelles outillées → skill 541
- [Taskade — Best Claude Code Skills](https://www.taskade.com/blog/claude-code-skills) — curation de l'écosystème, bots, automatisations → skills 544, 545
- Sonde de couverture du catalogue (01/11/2026) — 33 sujets non routés identifiés → skills 511-537

**Vague 9 (skills 601-616) — registre open source skills-hub.ai (14 300+ skills)** :

- [skills-hub.ai — Top 50 AI coding skills 2026](https://skills-hub.ai/blog/top-50-ai-coding-skills-2026) — revue de session, revue CTO, régressions visuelles, contrats d'API, plans de test, sprint dette, publication mobile, design-to-code, Kubernetes, pré-déploiement → skills 601-609, 614
- [skills-hub.ai — Best data skills](https://skills-hub.ai/best/data) — GEO et visibilité dans les moteurs IA → skill 612
- [skills-hub.ai — Best product skills](https://skills-hub.ai/best/product) — SWOT et analyse de position → skill 613
- [skills-hub.ai — Best migrations skills](https://skills-hub.ai/best/migrations) — auto-amélioration de l'agent et mémoire de leçons → skill 615
- [skills-hub.ai — Skill Stacks](https://skills-hub.ai/) — briefing du matin multi-projets → skill 611
- [i-have-adhd (GitHub, ayghri)](https://github.com/ayghri/i-have-adhd) — communication TDAH-friendly : action d'abord, étapes numérotées, état rappelé chaque tour → skill 616

## 🗺️ Vue d'ensemble

```mermaid
flowchart TD
    A[Entrée utilisateur] --> B{Nature du besoin}
    B -->|Produire du texte| C[1 SEO · 2 Ton · 3 Copy · 4 Email · 7 Traduction\n27 Office · 29 UGC · 30 Social · 31 LinkedIn · 24 CR]
    B -->|Améliorer l'existant| D[8 Relecture · 10 Review · 2 Réécriture\n34 Charte · 30 Optimisation]
    B -->|Comprendre| E[11 Expliqueur · 5 Synthèse · 13 Data · 16 Juridique\n32 Benchmark · 39 Socrate]
    B -->|Décider & planifier| F[15 Projet · 6 Brainstorming · 14 Deck · 12 Entretien\n19 Grill Me · 26 Découpage · 28 Fichiers · 36 KPI · 50 SOP]
    B -->|Créer & construire| H[9 Code · 21 Incrémental · 20 Debug · 22 Diagrammes\n23 Doc · 35 Reco · 38 Skill Creator · 48 Infographie · 47 Naming]
    B -->|Se former & progresser| I[40 Quiz · 41 Examen · 44 CV · 45 Négociation\n46 Conflits · 49 Rôle · 42 Voyage · 43 Budget]
    B -->|Augmenter la puissance IA| G[17 Meta-prompting · 18 Recherche · 37 Red-team]
    B -->|Contenus & prise de parole| M[51 Newsletter · 52 YouTube\\n53 Repurposing · 75 Discours]
    B -->|Vendre & servir| J[54 Prospection · 55 Feedback\\n56 Support · 62 Propositions]
    B -->|Piloter & décider| K[57 BMC · 58 Prix · 59 Finances\\n60 Prémortem · 61 Diable · 74 OKR · 73 Rétro]
    B -->|Produit & design| L[63 PRD · 64 Critique UX\\n65 Microcopy · 66 Chatbot]
    B -->|Qualité dev & automatisation| N[67 Tests · 68 Commits · 69 SQL\\n70 Sécurité · 71 Workflows · 72 Semaine]
    B -->|Agents & IA industrielle| O[76 Agents CLI · 77 MCP · 96 Datasets · 97 Evals\n98 RAG · 99 Outils · 100 Instructions · 224 Autonomes · 236 Contexte · 237 Debug prompts]
    B -->|Analyser & piloter| P[91 Scraping · 93 Prédictif · 101 Concepts · 103 Marché\n106 Cohortes · 107 Dashboards · 108 Storytelling · 109 Funnels · 186 Tracking]
    B -->|Rédaction experte| Q[116 Longs · 117 Traduction · 119 FAQ · 120 Plagiat\n124 Cas clients · 125 Livres blancs · 130 Guides · 137 Courriers · 226 Lectures]
    B -->|Visuel, vidéo & audio| R[139 Images · 140 Photos · 144 Vidéo · 145 Avatars · 146 Storyboard\n147 Miniatures · 154 Voix · 155 Musique · 157 Podcasts · 158 Sous-titres · 160 SFX]
    B -->|Marketing & croissance| S[118 Fiches produits · 123 Pages de vente · 135 Éditorial\n161 SEO · 162 CRO · 163 Lancement · 173 Fidélité · 174 Lead magnets · 175 Communauté]
    B -->|Vendre & financer| T[111 Leads · 112 Win/loss · 131 Témoignages · 164 Battlecards\n166 Objections · 168 Appels d'offres · 169 Marges · 170 Prévisionnel · 171 Levée]
    B -->|Produit & design| U[176 Roadmap · 177 Accessibilité · 179 Activation · 180 Doc API\n181 Design system · 182 Formulaires · 185 Backlog · 187 Interviews · 188 Synthèse UX]
    B -->|Gouvernance & conformité| V[189 RGPD · 190 Conformité · 191 Fraudes · 192 Modération\n193 Charte IA · 195 Injection · 197 Permissions · 199 Runbooks · 239 Réglementaire]
    B -->|RH & formation| W[132 Enfants · 201 Formations · 202 Postes · 203 Onboarding\n204 Progression · 205 Compétences · 231 Reconversion · 233 Employer branding · 234 Mentorat]
    B -->|Organisation & équipe| X[114 Connaissances · 208 Ateliers · 209 Réunions · 210 Décisions\n211 Team building · 232 Rituels · 235 Crise · 243 Audits internes]
    B -->|Vie quotidienne & perso| Y[214 Sport · 215 Nutrition · 216 Recettes · 218 Cadeaux · 221 Événements\n225 Déménagement · 227 Investissement · 230 Abonnements · 246 Succession · 248 Équilibre · 249 Retraite]
    B -->|Agentique & quotidien (vague 5)| Z[251 Handoff · 252 E2E · 256 Incidents · 259 Multi-agents\n261 Déclenchement · 268 PDF · 271 AI Act · 278 Hooks · 284 RDV · 293 Éloquence · 300 Gamification]
    B -->|Dev, data & quotidien (vague 6)| W6[301 Worktrees · 308 Profileur · 326 Budget tokens · 339 Test fantôme\n343 Qualité données · 368 Démos · 408 Offres emploi · 427 Business cases · 447 Fuites données · 465 Travail profond · 483 Sommeil · 500 Parcours perso]
    B -->|Sécurité info & web (vague 7)| V7[501 Auth · 502 En-têtes · 503 WordPress · 504 Menaces\n505 Correctifs · 506 Chiffrement · 507 Cloud · 508 CI/CD · 509 Phishing · 510 Réseau]
    B -->|Gaps sonde + web 2026 (vague 8)| V8[511 Stress · 519 Bourse · 523 Regex · 530 Arnaques\n538 Humaniseur IA · 540 Vibe coding · 546 Prompt images · 561 Deepfakes\n577 Supervision IA · 590 Séparation · 600 Bilan]
    B -->|skills-hub.ai + i-have-adhd (vague 9)| V9[601 Revue session · 602 Revue CTO · 606 Sprint dette\n612 GEO · 614 Pré-déploiement · 615 Auto-amélioration · 616 TDAH-friendly]
```


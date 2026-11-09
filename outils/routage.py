
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""routage.py — outillage SQL du routage de la skillAISlop.

Ce script vit dans le canvas « routage-sql-skills » : le corps du canvas EST
le script. Pour l'utiliser : sed -n '7,$p' CANVAS.md > routage.py puis :
    python3 routage.py build                 # canvas -> skills.db
    python3 routage.py route "ta demande"    # recherche rapide (--top N, --json)
    python3 routage.py generate [--check]    # base -> sections de routage du canvas
    python3 routage.py test                  # non-régression du routage
    python3 routage.py misses [--clear]      # journal des demandes non routées
    python3 routage.py lint                  # qualité des synonymes + tests
    python3 routage.py stats [--clear]       # observabilité du routage
    python3 routage.py bench [--tours N]     # mesure build/route + gain tokens
    python3 routage.py sonde [--fichier R.md]  # couverture : couverts/partiels/gaps
    python3 routage.py vocab [--limit N]        # top tokens FTS5 (fts5vocab) — lint sémantique
    python3 routage.py versions                 # historique des builds (ajouts/supprimes/modifies)
    python3 routage.py analytics                # stats SQL des routages de session (exit, voie, domaine)

Sous-commandes :
  build    (re)construit skills.db depuis le canvas : tables skills, domaines,
           synonymes + index full-text FTS5 (unicode61) avec triggers.
  route    cascade : renvoi direct -> mot-clé canonique -> synonyme ->
           full-text FTS5 (bm25 pondéré : mot-clé > signal > nom court > nom)
           -> passe vectorielle sqlite-vec (cosinus, embeddings locaux)
           -> passe floue par trigrammes (fautes de frappe) -> domaines
           plausibles. Chaque candidate porte l'ancre « ## N. » de sa section
           dans le canvas. Exit 0 : candidate trouvée · exit 1 : domaine
           plausible seulement · exit 2 : aucune candidate — des pistes
           approx sont affichées, la demande est consignée au journal.
  test    non-régression : rejoue TESTS_ROUTAGE (demande -> skill attendue ;
           None = exit 2 attendu). Échec = exit 1.
  misses  journal des demandes non routées (exit 2), triées par récurrence
           (clé = demande normalisée). --clear vide le journal. --suggest
           propose pour chaque entrée le synonyme exact à ajouter dans
           SYNONYMES (meilleur recouvrement de trigrammes) ; sans piste :
           besoin non couvert, envisager une nouvelle skill. Un exit 2
           récurrent = un synonyme à ajouter puis rebuild.
  lint     contrôle qualité des données éditables du canvas : synonymes
           dupliqués ou à cibles contradictoires, trop courts, cibles
           inexistantes, tests dupliqués. Exit 1 si problème.
           Seuil : synonyme >= 2 caractères (les acronymes comme « pv »
           sont légitimes).
  stats    observabilité : routages de la session par exit code et par voie
           (direct, mot-clé, synonyme, fts, approx). --clear remet à zéro.
           Session only (vit dans skills.db, effacé aux resets).
  bench    mesure : temps de build, latence route (moy/min/max sur le corpus
           TESTS_ROUTAGE), gain en tokens vs lecture du canvas complet.
           Rejouer à chaque évolution du routeur pour actualiser les gains.
  generate régénère depuis la base les sections de routage du canvas :
           sommaire, carte des domaines, index inversé, table complète,
           branches D1-D26 de l'arbre. --check : sans écrire, exit 1 si
           désynchronisé. Toujours repasser l'audit R1-R8 ensuite.

Ajouter une skill : INSERT dans skills (num, nom, domaine, signal, mot_cle,
branche, nom_court) puis generate — cf. AGENTS.md du projet.
Ajouter un synonyme : une ligne dans SYNONYMES ci-dessous puis build.
Ajouter un test : un couple (demande, N attendu) dans TESTS_ROUTAGE.
Toute sortie « exit 2 » rencontrée en production = un synonyme à ajouter ;
le journal (misses) montre lesquelles reviennent le plus, et --suggest le
rédige. Après ajout : build puis test (non-régression).
"""
import argparse
import json
import re
import sqlite3
import importlib.util
import sys
import sys
import time
import unicodedata
from pathlib import Path

DB_PATH = Path(__file__).with_name("skills.db")
RACINE = Path(__file__).resolve().parent.parent
CANVAS_PAR_DEFAUT = RACINE / "canvas/bibliotheque-skills-ai.md"
# Le canvas principal porte sommaire + carte + routage + arbre ; les corpus portent
# les sections détaillées (découpage pour respecter le plafond de taille d'un canvas).
CANVAS_CORPUS = [
    RACINE / "canvas/corpus-skills-1-300.md",
    RACINE / "canvas/corpus-skills-301-600.md",
    RACINE / "canvas/corpus-skills-601-900.md",
    RACINE / "canvas/corpus-skills-901-1200.md",
    RACINE / "canvas/corpus-skills-1201-1500.md",
    RACINE / "canvas/corpus-skills-1501-1800.md",
    RACINE / "canvas/corpus-skills-1801-2100.md",
]

# ---------------------------------------------------------------------------
# Synonymes (édition : ajouter une ligne, puis relancer `build`)
# ---------------------------------------------------------------------------
SYNONYMES = [
    ("ads", 3),
    ("annonce pub", 3),
    ("campagne pub", 3),
    ("publicité", 3),
    ("condenser", 5),
    ("faire court", 5),
    ("résumer", 5),
    ("synthétiser", 5),
    ("traduction", 7),
    ("traduire", 7),
    ("corriger un texte", 8),
    ("fautes", 8),
    ("orthographe", 8),
    ("code review", 10),
    ("revue de code", 10),
    ("embauche", 12),
    ("powerpoint", 14),
    ("presentation", 14),
    ("slides", 14),
    ("clause", 16),
    ("contrat", 16),
    ("ameliorer un prompt", 17),
    ("prompt", 17),
    ("etat de l'art", 18),
    ("recherche approfondie", 18),
    ("bug", 20),
    ("debug", 20),
    ("erreur de code", 20),
    ("ça marche pas", 20),
    ("compte rendu", 24),
    ("cr de reunion", 24),
    ("par où commencer", 26),
    ("procrastination", 26),
    ("procrastiner", 26),
    ("remettre à demain", 26),
    ("post instagram", 30),
    ("réseaux sociaux", 30),
    ("social media", 30),
    ("linkedin", 31),
    ("persona", 33),
    ("profil cible", 33),
    ("qcm", 40),
    ("quiz", 40),
    ("itinéraire", 42),
    ("séjour", 42),
    ("vacances", 42),
    ("voyage", 42),
    ("curriculum", 44),
    ("resume", 44),
    ("playbook", 50),
    ("procedure", 50),
    ("sop", 50),
    ("infolettre", 51),
    ("newsletter", 51),
    ("cold email", 54),
    ("demarchage", 54),
    ("business model", 57),
    ("business plan", 57),
    ("pricing", 58),
    ("tarification", 58),
    ("chiffrage", 62),
    ("devis", 62),
    ("audit ux", 64),
    ("critique ux", 64),
    ("assistant conversationnel", 66),
    ("chatbot", 66),
    ("couverture de tests", 67),
    ("test unitaire", 67),
    ("retro", 73),
    ("retrospective", 73),
    ("objectifs trimestriels", 74),
    ("okr", 74),
    ("discours", 75),
    ("prise de parole", 75),
    ("speech", 154),
    ("post-mortem", 89),
    ("postmortem", 89),
    ("scraper", 91),
    ("scraping", 91),
    ("suivre l'actualité", 105),
    ("veille", 105),
    ("veille hebdo", 105),
    ("churn", 106),
    ("cohortes", 106),
    ("rétention", 106),
    ("dashboard", 107),
    ("tableau de bord", 107),
    ("funnel", 109),
    ("tunnel de conversion", 109),
    ("a/b test", 110),
    ("split test", 110),
    ("facturation", 115),
    ("facture", 115),
    ("landing page", 123),
    ("page d'atterrissage", 123),
    ("contes", 132),
    ("enfants", 132),
    ("vulgariser", 132),
    ("carte de vœux", 136),
    ("occasions spéciales", 136),
    ("vœux", 136),
    ("illustration", 141),
    ("logo", 141),
    ("vectoriel", 141),
    ("mockup", 143),
    ("prototype", 143),
    ("maquette", 153),
    ("mockup d'écran", 153),
    ("wireframe", 153),
    ("sous titrer", 158),
    ("sous-titres", 158),
    ("référencement", 161),
    ("seo", 161),
    ("feuille de route", 176),
    ("roadmap", 176),
    ("backlog", 185),
    ("tickets a faire", 185),
    ("conformité", 190),
    ("données personnelles", 190),
    ("rgpd", 190),
    ("integration nouvelle equipe", 203),
    ("onboarding", 203),
    ("animation de groupe", 208),
    ("atelier", 208),
    ("workshop", 208),
    ("organiser une réunion", 209),
    ("préparer une réunion", 209),
    ("réunion", 209),
    ("courir", 214),
    ("entraînement", 214),
    ("fitness", 214),
    ("musculation", 214),
    ("sport", 214),
    ("calories", 215),
    ("nutrition", 215),
    ("perdre du poids", 215),
    ("regime", 215),
    ("cuisiner", 216),
    ("menu", 216),
    ("recette", 216),
    ("demarches administratives", 217),
    ("papiers", 217),
    ("anniversaire", 218),
    ("cadeau", 218),
    ("idee cadeau", 218),
    ("liste de taches", 223),
    ("to-do", 223),
    ("todo", 223),
    ("demenagement", 225),
    ("demenager", 225),
    ("jardin", 229),
    ("potager", 229),
    ("semis", 229),
    ("abonnement", 230),
    ("desabonnement", 230),
    ("resilier", 230),
    ("changer de metier", 231),
    ("reconversion", 231),
    ("mentor", 234),
    ("mentorat", 234),
    ("bad buzz", 235),
    ("communication de crise", 235),
    ("crise", 235),
    ("après-décès", 246),
    ("héritage", 246),
    ("hériter", 246),
    ("succession", 246),
    ("crash", 256),
    ("incident production", 256),
    ("panne prod", 256),
    ("feuille de calcul", 264),
    ("tableur", 264),
    ("screening cv", 274),
    ("trier les cv", 274),
    ("avis clients negatifs", 282),
    ("avis google", 282),
    ("prendre rendez-vous", 284),
    ("rdv", 284),
    ("rendez-vous", 284),
    ("appareil en panne", 291),
    ("panne", 291),
    ("reparer", 291),
    ("entretien auto", 292),
    ("vehicule", 292),
    ("voiture", 292),
    ("augmentation de salaire", 294),
    ("negocier une augmentation", 294),
    ("un salarié s'est blessé sur une machine", 886), ("salarié blessé machine déclaration", 886), ("mon pc fait un clic et rame", 873), ("disque dur qui clique pc", 873), ("déclaration AT 48h", 886), ("accident du travail déclaration", 886), ("declaration", 297),
    ("fiscalite", 297),
    ("impot", 297),
    ("impots", 297),
    ("conteneur", 314),
    ("conteneurisation", 314),
    ("docker", 314),
    ("impaye", 371),
    ("relance paiement", 371),
    ("transcription", 378),
    ("transcrire", 378),
    ("ghostwriter", 393),
    ("ghostwriting", 393),
    ("tribune", 393),
    ("q&a en direct", 397),
    ("questions reponses en direct", 397),
    ("proces verbal", 400),
    ("proces-verbal", 400),
    ("pv", 400),
    ("alternance", 411),
    ("apprentissage en entreprise", 411),
    ("stage", 411),
    ("teletravail", 412),
    ("travail a distance", 412),
    ("demission", 413),
    ("quitter l'entreprise", 413),
    ("mobilite interne", 414),
    ("mutation", 414),
    ("burnout", 421),
    ("surcharge de travail", 421),
    ("agenda", 463),
    ("calendrier", 463),
    ("planifier ma semaine", 463),
    ("concentration", 465),
    ("deep work", 465),
    ("expatriation", 476),
    ("expatrie", 476),
    ("vivre a l'etranger", 476),
    ("courses", 478),
    ("provisions", 478),
    ("supermarche", 478),
    ("aidant", 482),
    ("parent age", 482),
    ("dormir", 483),
    ("sommeil", 483),
    ("insomnie", 483),
    ("bilan de sante", 485),
    ("check-up", 485),
    ("checkup", 485),
    ("batchcooking", 486),
    ("meal prep", 486),
    ("medicaments", 487),
    ("pharmacie maison", 487),
    ("arreter de fumer", 488),
    ("mauvaise habitude", 488),
    ("rituel du matin", 489),
    ("routine", 489),
    ("histoire de famille", 490),
    ("souvenirs de famille", 490),
    ("accent", 492),
    ("prononcer", 492),
    ("memorisation", 495),
    ("memoriser", 495),
    ("retenir par coeur", 495),
    # rescues mono-mot (2026-11, après durcissement mode OU / flou)
    ("composer", 155),
    ("testing", 110),
    # rescues supplémentaires (2026-11) — sujets légitimes perdus au durcissement
    ("podcast", 157),
    ("no-code", 78),
    ("e-commerce", 279),
    ("examen", 41),
    ("chanson", 155),
    ("cartographie", 95),
    ("grignoter", 488),
    ("assurance habitation", 480),
    ("relation presse", 361),
    ("authentification", 501),
    ("mfa", 501),
    ("sso", 501),
    ("csp", 502),
    ("en-têtes http", 502),
    ("hsts", 502),
    ("wordpress", 503),
    ("cms", 503),
    ("modélisation de menaces", 504),
    ("cve", 505),
    ("correctifs", 505),
    ("chiffrement", 506),
    ("tls", 506),
    ("sécurité cloud", 507),
    ("ci/cd", 508),
    ("supply chain", 508),
    ("phishing", 509),
    ("faux email", 509),
    ("wi-fi", 510),
    ("wifi", 510),
    ("vpn", 510),

    # --- Vague 8 (skills 511-600) ---
    ("stress", 511),
    ("anxiété", 511),
    ("respiration", 511),
    ("crypto", 512),
    ("blockchain", 512),
    ("web3", 513),
    ("wallet", 513),
    ("nft", 513),
    ("robotique", 514),
    ("arduino", 514),
    ("raspberry", 514),
    ("théâtre", 515),
    ("impro", 515),
    ("chanter", 516),
    ("karaoké", 516),
    ("danser", 517),
    ("chorégraphie", 517),
    ("guitare", 518),
    ("piano", 518),
    ("violon", 518),
    ("bourse", 519),
    ("etf", 519),
    ("parentalité", 520),
    ("punir", 520),
    ("montage", 521),
    ("capcut", 521),
    ("imovie", 521),
    ("photographie", 522),
    ("cadrage", 522),
    ("regex", 523),
    ("godot", 524),
    ("unity", 524),
    ("flutter", 525),
    ("android", 525),
    ("franchise", 527),
    ("commerçant", 527),
    ("surendettement", 528),
    ("dettes", 528),
    ("clarifier les rôles d'un projet avec raci", 847), ("trouver un vol low cost pas cher", 865), ("préparer mon entretien d'embauche en visio", 872), ("préavis de grève déposé par les syndicats", 890), ("apprendre l'ai literacy pour mon équipe", 815), ("affiner un prompt par dialogue itératif", 817), ("rendre mon interface adaptative au niveau utilisateur", 823), ("mail du dg en déplacement demandant un virement urgent", 824), ("mon frère répond à notre appel d'offres, conflit d'intérêts", 848), ("mon artisan a bâclé la rénovation, quelles étapes", 855), ("faire ma liste de courses anti gaspi", 860), ("donner un smartphone à mon ado de 12 ans en sécurité", 871), ("bruit voisin le matin", 864), ("voisinage", 529),
    ("mon voisin fait du bruit", 864), ("voisin travaux 7h", 864), ("voisin bruyant", 864), ("voisin", 529),
    ("arnaque", 530),
    ("escroquerie", 530),
    ("photographier", 531),
    ("bénévolat", 532),
    ("baby", 533),
    ("sitter", 533),
    ("poème", 534),
    ("poésie", 534),
    ("journal", 535),
    ("exposition", 536),
    ("concert", 536),
    ("biographie", 537),
    ("humaniser", 538),
    ("obsidian", 539),
    ("vault", 539),
    ("hugo", 545),
    ("astro", 545),
    ("midjourney", 546),
    ("statistique", 547),
    ("significativité", 547),
    ("visibilité", 548),
    ("positionnement", 548),
    ("interculturel", 549),
    ("neurodiversité", 550),
    ("dyslexie", 550),
    ("statuts", 552),
    ("licence", 553),
    ("mit", 553),
    ("gpl", 553),
    ("caution", 554),
    ("locataire", 554),
    ("bailleur", 554),
    ("licenciement", 555),
    ("les syndicats ont déposé un préavis de grève", 890), ("préavis de grève NAO", 890), ("préavis de grève syndicats", 890), ("conflit salarial collectif", 890), ("préavis", 555),
    ("chat", 556),
    ("chien", 556),
    ("vétérinaire", 556),
    ("tricot", 557),
    ("couture", 557),
    ("céramique", 557),
    ("vêtements", 558),
    ("garde", 558),
    ("maths", 559),
    ("mathématiques", 559),
    ("thèse", 560),
    ("doctorat", 560),
    ("deepfake", 561),
    ("désinformation", 561),
    ("micro", 562),
    ("entrepreneur", 562),
    ("toast", 564),
    ("réception", 565),
    ("échecs", 567),
    ("échec", 567),
    ("film", 568),
    ("série", 568),
    ("musée", 569),
    ("devoirs", 570),
    ("orientation", 571),
    ("portfolio", 572),
    ("lightroom", 574),
    ("retouche", 574),
    ("gameplay", 575),
    ("équilibrage", 575),
    ("twitch", 576),
    ("stream", 576),
    ("tracing", 577),
    ("plantes", 578),
    ("arrosage", 578),
    ("désencombrement", 579),
    ("rangement", 579),
    ("permis", 580),
    ("seniors", 581),
    ("marathon", 582),
    ("footing", 582),
    ("randonnée", 583),
    ("trek", 583),
    ("dégustation", 584),
    ("vin", 584),
    ("miles", 585),
    ("délivrabilité", 586),
    ("dmarc", 586),
    ("spf", 586),
    ("stock", 587),
    ("expédition", 587),
    ("comptabilité", 588),
    ("fratrie", 589),
    ("divorce", 590),
    ("séparation", 590),
    ("colocation", 592),
    ("mutuelle", 593),
    ("créance", 594),
    ("copropriété", 595),
    ("syndic", 595),
    ("sauvegarde", 596),
    ("backup", 596),
    ("filtrage", 597),

    # --- Vague 9 (skills 601-616 : skills-hub.ai + i-have-adhd) ---
    ("revue de session", 601),
    ("session", 601),
    ("cto", 602),
    ("build vs buy", 602),
    ("captures", 603),
    ("breaking change", 604),
    ("compatibilité", 604),
    ("critères d'acceptation", 605),
    ("dette", 606),
    ("app store", 607),
    ("google play", 607),
    ("figma", 608),
    ("handoff", 608),
    ("kubernetes", 609),
    ("k8s", 609),
    ("pods", 609),
    ("soc 2", 610),
    ("tsc", 610),
    ("briefing", 611),
    ("standup", 611),
    ("geo", 612),
    ("perplexity", 612),
    ("swot", 613),
    ("preflight", 614),
    ("not ready", 614),
    ("auto-amélioration", 615),
    ("leçons", 615),
    ("tdah", 616),
    ("préambule", 616),

    # --- Vague 10 (skills 617-699) ---
    ("épuisement professionnel", 617),
    ("burnout au travail", 617),
    ("charge mentale parentale", 618),
    ("syndrome imposteur", 619),
    ("réveils nocturnes", 621),
    ("allergies alimentaires", 622),
    ("prise de médicaments", 623),
    ("orthodontie", 624),
    ("lunettes", 625),
    ("maternité", 626),
    ("diversification", 627),
    ("garde d'enfants", 628),
    ("activités enfants", 629),
    ("aide à domicile", 630),
    ("aménagement logement", 631),
    ("évaluation annuelle", 632),
    ("évolution interne", 633),
    ("rupture conventionnelle", 634),
    ("changement de poste en interne", 635),
    ("harcèlement moral", 636),
    ("sexisme", 637),
    ("prévisionnel trésorerie", 638),
    ("déclaration fiscale", 639),
    ("bilan comptable", 640),
    ("fiche de paie", 641),
    ("full remote", 642),
    ("réunionite", 643),
    ("retour d'expérience", 644),
    ("se présenter brièvement", 645),
    ("page de conversion", 646),
    ("avis google maps", 647),
    ("délai de rétractation", 648),
    ("règlement amiable", 649),
    ("fichage banque de france", 650),
    ("testament", 651),
    ("héritage familial", 651),
    ("pension alimentaire", 652),
    ("garde alternée", 652),
    ("mise en service", 653),
    ("bricolage", 654),
    ("vidange", 655),
    ("contrôle technique", 655),
    ("préparer un voyage", 656),
    ("bagages", 656),
    ("organiser un repas", 657),
    ("liste de naissance", 658),
    ("préparer un marathon", 659),
    ("musculation maison", 659),
    ("yoga débutant", 659),
    ("programme vélo", 659),
    ("vaccination chien", 660),
    ("stérilisation", 660),
    ("toilettage", 660),
    ("potager maison", 661),
    ("compostage", 661),
    ("vegan", 662),
    ("médecin en ligne", 663),
    ("téléservice", 664),
    ("gestionnaire de mots de passe", 665),
    ("virus", 666),
    ("malware", 666),
    ("photo de quelqu'un", 667),
    ("publier une photo", 667),
    ("sasu", 668),
    ("eurl", 668),
    ("zapier", 669),
    ("make", 669),
    ("second cerveau", 670),
    ("cours de langue", 671),
    ("conduite accompagnée", 672),
    ("réviser efficacement", 673),
    ("changer de voie professionnelle", 674),
    ("offre d'achat", 675),
    ("crédit immobilier", 675),
    ("état des lieux", 676),
    ("quittance de loyer", 676),
    ("conseil syndical", 677),
    ("assemblée générale copro", 677),
    ("pompe à chaleur", 678),
    ("panneaux solaires", 678),
    ("dpe", 678),
    ("résilier un abonnement", 679),
    ("mobilité bancaire", 680),
    ("livret a", 681),
    ("pea", 681),
    ("relevé de carrière", 682),
    ("protection juridique", 683),
    ("comparatif assurances", 683),
    ("partir vivre à l'étranger", 684),
    ("faux sms", 685),
    ("usurpation d'identité", 685),
    ("wcag", 686),
    ("empreinte carbone numérique", 687),
    ("veille ia", 688),
    ("comparatif modèles ia", 689),
    ("recherche sémantique", 690),
    ("embeddings", 690),
    ("lora", 691),
    ("entraîner un modèle", 691),
    ("prompt injection", 692),
    ("jailbreak", 692),
    ("evals", 693),
    ("évaluation llm", 693),
    ("optimiser les tokens", 694),
    ("mes données personnelles", 695),
    ("gestion des cookies", 695),
    ("buzz négatif", 696),
    ("questions entretien", 697),
    ("parcours d'intégration", 698),
    ("douane déménagement", 699),
    ("conteneur maritime", 699),
    ("allergique", 622),
    ("allergie alimentaire", 622),
    ("médicaments", 623),
    ("oubli médicaments", 623),
    ("enceinte", 626),
    ("suivi de grossesse", 626),
    ("éducation des enfants", 629),
    ("écrans ado", 629),
    ("entretien préalable", 634),
    ("télétravail hybride", 642),
    ("fuite d'eau", 654),
    ("réparation maison", 654),
    ("reprendre le sport", 659),
    ("programme sportif", 659),
    ("adopter un animal", 660),
    ("chat adulte", 660),
    ("carte d'identité", 664),
    ("démarches administratives", 664),
    ("automatiser", 669),
    ("workflow no-code", 669),
    ("notion obsidian", 670),
    ("organisation personnelle", 670),
    ("apprendre l'espagnol", 671),
    ("cours de langue adulte", 671),
    ("brevet", 673),
    ("méthodologie scolaire", 673),
    ("reconversion professionnelle", 674),
    ("caution locative", 676),
    ("état des lieux litige", 676),
    ("appel de fonds", 677),
    ("s'expatrier", 684),
    ("départ à l'étranger", 684),
    ("viral", 696),
    ("incident médiatique", 696),
    ("déménagement à l'étranger", 699),
    ("expatriation déménagement", 699),
    ("changer de poste", 635),
    ("chasse d'eau", 654),
    ("wc qui fuit", 654),
    ("courir un 10 km", 659),
    ("10 km", 659),
    ("un seul système de notes", 670),
    ("second cerveau organisation", 670),
    ("changer de métier", 674),
    ("proprio retient caution", 676),
    ("litige caution", 676),
    ("expatriation 2 ans", 684),
    ("fine-tuning", 691),
    ("déménager à lisbonne", 699),
    ("mes notes sont partout", 670),
    ("prise de notes éparpillée", 670),
    ("reconversion dans l'environnement", 674),
    ("bilan de compétences financé", 674),
    ("mon proprio bloque ma caution", 676),
    ("retenue abusive caution", 676),
    ("expatriation professionnelle", 684),
    ("expat singapour", 684),
    ("fine-tuner", 691),
    ("spécialiser un llm", 691),
    ("vivre à lisbonne", 699),
    ("déménagement lisbonne", 699),
    ("j'ai des notes partout", 670),
    ("je veux me reconvertir", 674),
    ("mon proprio retient ma caution", 676),
    ("on s'expatrie", 684),
    ("fine-tuner un modèle", 691),
    ("on déménage vivre", 699),
    ("ado", 629),
    ("écrans en famille", 629),
    ("hybride", 642),
    ("2 jours de tt", 642),

    # --- Vague 11 (skills 700-799 : veille web 2026) ---
    ("hallucination ia", 700),
    ("vérifier les sources", 700),
    ("résumé de ma journée", 701),
    ("prépa call", 702),
    ("répondre à un email", 703),
    ("protéger mon focus", 704),
    ("action items", 705),
    ("suivi des réponses", 706),
    ("point d'avancement", 707),
    ("rapport de recherche", 708),
    ("surveiller mes concurrents", 709),
    ("bilan de la semaine", 710),
    ("agent-to-agent", 711),
    ("orchestration agents", 712),
    ("traces llm", 713),
    ("mémoire sémantique", 714),
    ("installer une skill", 715),
    ("skill malveillante", 716),
    ("remotion", 717),
    ("modèle 3d par ia", 718),
    ("réponse courte", 719),
    ("critiquer mon approche", 720),
    ("connaissances en réseau", 721),
    ("hébergement ue", 722),
    ("agents de sécurité", 723),
    ("règles karpathy", 724),
    ("réponses ancrées dans mes documents", 725),
    ("tendances temps réel", 726),
    ("planifier mes contenus", 727),
    ("slides éducatifs", 728),
    ("script tiktok", 729),
    ("photo produit ia", 730),
    ("texte bouton", 731),
    ("bibliothèque de composants", 732),
    ("expérimentation", 733),
    ("retours utilisateurs", 734),
    ("première utilisation", 735),
    ("sous-titres vidéo", 736),
    ("rcorcf", 737),
    ("chaîne de pensée", 738),
    ("client idéal", 739),
    ("prospection linkedin", 740),
    ("démo personnalisée", 741),
    ("c'est trop cher", 742),
    ("demander la signature", 743),
    ("cross-sell", 744),
    ("bouche-à-oreille", 745),
    ("campagne emailing", 746),
    ("google ads", 747),
    ("meta ads", 747),
    ("core web vitals", 748),
    ("référencement naturel", 749),
    ("cgv", 750),
    ("registre des traitements", 751),
    ("droit d'auteur", 752),
    ("règlement ia européen", 753),
    ("cyberattaque", 754),
    ("plan de reprise", 755),
    ("nettoyer mon pc", 756),
    ("mail frauduleux", 757),
    ("3-d secure", 758),
    ("embaucher quelqu'un", 759),
    ("visioconférence", 760),
    ("confier une mission", 761),
    ("désamorcer une tension", 762),
    ("matrice eisenhower", 763),
    ("installer une habitude", 764),
    ("rumination", 765),
    ("communication non violente", 766),
    ("defense de mémoire", 767),
    ("plan dialectique", 768),
    ("grand oral", 769),
    ("soutien scolaire", 770),
    ("apprendre en faisant", 771),
    ("live coding", 772),
    ("demande d'augmentation", 773),
    ("candidature spontanée", 774),
    ("prévisionnel 3 ans", 775),
    ("deck de levée", 776),
    ("board meeting", 777),
    ("bfr", 778),
    ("relance impayé", 779),
    ("proposition commerciale", 780),
    ("comparer des outils", 781),
    ("changer d'outil", 782),
    ("macro excel", 783),
    ("documenter un processus", 784),
    ("veille réglementaire", 785),
    ("rc pro", 786),
    ("décennale", 786),
    ("risques psychosociaux", 787),
    ("équipe remote", 788),
    ("départ d'un salarié", 789),
    ("entretien d'embauche employeur", 790),
    ("compétences à développer", 791),
    ("comité social", 792),
    ("scrum", 793),
    ("registre des risques", 794),
    ("adhésion équipe", 795),
    ("réclamation client", 796),
    ("satisfaction client", 797),
    ("taux de conversion e-commerce", 798),
    ("go-to-market", 799),
    ("fact-checker une ia", 700),
    ("hallucinations", 700),
    ("relance prestataire", 706),
    ("suivi des engagements", 706),
    ("closer", 743),
    ("obtenir un engagement", 743),
    ("forfait pro", 744),
    ("expansion de compte", 744),
    ("emails de bienvenue", 746),
    ("séquence de bienvenue", 746),
    ("optimiser un article seo", 749),
    ("seo contenu", 749),
    ("vendre ma pme dans 3 ans", 891), ("vendre ma pme", 891), ("cession entreprise", 891), ("cession pme 30 personnes", 891), ("embaucher", 759),
    ("premier salarié", 759),
    ("conflit entre collègues", 762),
    ("médiation interne", 762),
    ("je rumine", 765),
    ("cours particuliers 4e", 770),
    ("expliquer les équations", 770),
    ("migrer emails proton", 782),
    ("migration de données", 782),
    ("offboarding développeur", 789),
    ("check-list offboarding", 789),
    ("recrutement commercial", 790),
    ("process de recrutement", 790),
    ("embarquer l'équipe", 795),
    ("conduite du changement crm", 795),
    ("plan de lancement", 799),
    ("lancer une appli", 799),
    ("vérifie les chiffres", 700),
    ("texte généré par ia", 700),
    ("ne répond plus", 706),
    ("relance-le", 706),
    ("optimise cet article", 749),
    ("se disputent", 762),
    ("je médie", 762),
    ("migre mes emails", 782),
    ("10 ans d'emails", 782),
    ("recrutement de notre", 790),
    ("notre commercial", 790),
    ("ton d'équipe", 399), ("ton de communication", 399), ("changer de ton", 399), ("adapter son ton", 399),
    ("decks", 14),
    ("arbitrer", 266),
    ("trancher", 266),
    ("tutorat", 39),
    ("dispatcher", 0),
    # --- Bouclage sonde (gap/partiels, 2026-11-02) ---
    # --- Vague 13 (skills 900-999 : tendances 2027) ---
    ("conformité ai act", 900),
    ("contenu généré par ia obligatoire", 901),
    ("ia qui évalue mon travail", 902),
    ("ollama local", 903),
    ("llm local", 903),
    ("standard ia 2027", 904),
    ("malware clawhub", 905),
    ("lets encrypt 2027", 906),
    ("piratage par ia", 907),
    ("gouvernance identités ia", 908),
    ("scraping ia 2027", 909),
    ("plf 2027", 910),
    ("plf 2027 licenciement", 911),
    ("directive salaire 2027", 912),
    ("autorisation voyage europe", 913),
    ("ligne munich rome", 914),
    ("vague de chaleur 2027", 915),
    ("micro-rituels anti stress", 916),
    ("glycémie continue 2027", 917),
    ("4 jours par semaine", 918),
    ("changer de métier 2027", 919),
    ("ne pas répondre le soir", 920),
    ("ennui au travail", 921),
    ("marque employeur 2027", 922),
    ("téléphone sans internet", 923),
    ("données en europe", 924),
    ("byo agent", 925),
    ("ui générative", 926),
    ("budget ia 2027", 927),
    ("ia non déclarée entreprise", 928),
    ("simulation ia recherche", 929),
    ("suno udio", 930),
    ("robot usine 2027", 931),
    ("contrôle biométrique aéroport", 932),
    ("étudier travailler royaume-uni 2027", 933),
    ("batterie avion 2027", 934),
    ("maprimerenov 2027", 935),
    ("pacte papin", 936),
    ("bien-être au travail 2027", 937),
    ("geo moteurs ia", 938),
    ("verifiability karpathy", 939),
    ("llms.txt 2027", 940),
    ("créatine 2027", 941),
    ("voyage sommeil", 942),
    ("apple intelligence 2027", 943),
    ("fact-check ia sources", 944),
    ("réduire tokens ia", 945),
    ("ne pas entraîner ia sur mon contenu", 946),
    ("tâche ponctuelle agent", 947),
    ("contrôle cnil 2027", 948),
    ("bilan 2026 objectifs 2027", 949),
    ("plan de licenciement collectif", 950),
    ("prime résultats salariés", 951),
    ("addiction paris en ligne", 952),
    ("carte piratée", 953),
    ("perdu passeport voyage", 954),
    ("carte grise en ligne", 955),
    ("love scam", 956),
    ("mon compte a été hacké", 957),
    ("vivre à l'étranger 2027", 958),
    ("acheter tesla occasion", 959),
    ("installer wallbox", 960),
    ("dpe 2027 interdiction location", 961),
    ("fausse annonce immo", 962),
    ("faire son testament", 963),
    ("compte-titres 2027", 964),
    ("multirisque habitation", 965),
    ("taux crédit 2027", 966),
    ("vérifier employeur", 967),
    ("méthode star entretien", 968),
    ("négocier sa rupture", 969),
    ("tms bureau 2027", 970),
    ("dispute au travail", 971),
    ("événement équipe 2027", 972),
    ("comprendre bulletin salaire", 973),
    ("impots.gouv.fr 2027", 974),
    ("reconnaissance AT MP", 975),
    ("acheter neuf 2027", 976),
    ("meublé ou nu 2027", 977),
    ("calcul retraite 2027", 978),
    ("dpe 2027 avant travaux", 979),
    ("sci immobilière", 980),
    ("travaux bâclés 2027", 981),
    ("ficp inscription", 982),
    ("back market 2027", 983),
    ("van aménagé 2027", 984),
    ("mariage pas cher 2027", 985),
    ("randonnée gr 2027", 986),
    ("evg 2027", 987),
    ("eurovélo 2027", 988),
    ("canoë 2027", 989),
    ("pvt 2027", 990),
    ("déménagement international 2027", 991),
    ("résidence secondaire 2027", 992),
    ("vol annulé remboursement", 993),
    ("rapatriement sanitaire", 994),
    ("voyage moto 2027", 995),
    ("team building 2027", 996),
    ("évolution interne 2027", 997),
    ("pause carrière 2027", 998),
    ("nouvelle année 2027 résolutions", 999),
    ("préparer l'ai act haut risque avant décembre 2027", 900),
    ("mon chatbot doit-il dire qu'il est une ia", 901),
    ("notre appli évalue la productivité avec une ia", 902),
    ("faire tourner un petit modèle ia en local", 903),
    ("déployer un agent vocal sur notre hotline", 904),
    ("installer une skill clawhub en sécurité", 905),
    ("mon certificat lets encrypt passe à 64 jours en février 2027", 906),
    ("se défendre des attaques ia autonomes", 907),
    ("gouverniser les agents ia comme des identités", 908),
    ("protéger mon api du scraping de bots ia", 909),
    ("don d'argent à 6 % au premier semestre 2027", 910),
    ("mon indemnité de rupture sera plafonnée à 1 pass", 911),
    ("afficher les salaires dans nos offres dès 2027", 912),
    ("partir en europe en 2027, faut-il l'etias", 913),
    ("nouvelle ligne de train munich rome en 2027", 914),
    ("se préparer à la canicule de l'été 2027", 915),
    ("adopter des micro-rituels de régulation nerveuse", 916),
    ("suivre ma glycémie avec un capteur cgm", 917),
    ("négocier la semaine de 4 jours", 918),
    ("me reconvertir dans la cybersécurité en 2027", 919),
    ("ne pas répondre aux mails le soir, mon droit", 920),
    ("je m'ennuie au travail, c'est le bore-out", 921),
    ("recruter par compétences plutôt que diplômes", 922),
    ("passer à un dumbphone en 2027", 923),
    ("héberger nos données en europe en 2027", 924),
    ("brancher plusieurs agents dans rabbit 2", 925),
    ("faire générer des formulaires par l'ia", 926),
    ("prévoir le coût des logiciels ia dans le budget 2027", 927),
    ("mes collègues utilisent chatgpt perso au bureau", 928),
    ("tester nos scénarios logistique avec un world model", 929),
    ("générer un jingle avec suno", 930),
    ("les robots humanoïdes arrivent dans mon usine", 931),
    ("contrôle biométrique à la frontière schengen en 2027", 932),
    ("visa graduate uk à 18 mois en 2027", 933),
    ("powerbank en cabine avion en 2027", 934),
    ("aides anah recentrées en 2027", 935),
    ("reprise de mon entreprise par les salariés en 2027", 936),
    ("prévenir les rps comme indicateur 2027", 937),
    ("être cité par chatgpt quand on cherche un comparatif", 938),
    ("vérifier les sorties de mon agent avant prod", 939),
    ("scraper des données publiques légalement", 940),
    ("créatine et santé cardiaque, quelles preuves en 2027", 941),
    ("choisir un hôtel optimisé pour le sommeil", 942),
    ("faire tourner siri en local sur mon téléphone", 943),
    ("vérifier une info avec notebooklm ancré", 944),
    ("le prompt caveman pour des réponses courtes", 945),
    ("empêcher les llm d'entraîner sur mon contenu", 946),
    ("lancer un agent jetable pour une tâche ponctuelle", 947),
    ("se préparer aux 1,5 million de contrôles cnil en 2027", 948),
    ("faire mon bilan 2026 et mes objectifs 2027", 949),
    ("on doit faire un pse", 950),
    ("mettre en place un accord d'intéressement", 951),
    ("prévenir l'addiction aux paris en ligne", 952),
    ("fraude sur ma carte bancaire ce matin", 953),
    ("mon passeport a été volé à l'étranger", 954),
    ("renouveler mon passeport sur ants en 2027", 955),
    ("arnaque sur un site de rencontre", 956),
    ("mon compte instagram a été piraté", 957),
    ("je m'expatrie au portugal en 2027", 958),
    ("acheter une voiture électrique d'occasion en 2027", 959),
    ("installer une borne de recharge chez moi", 960),
    ("rénovation énergétique globale de ma maison", 961),
    ("arnaque à l'annonce de colocation", 962),
    ("rédiger mon testament", 963),
    ("ouvrir un pea en 2027", 964),
    ("comparer deux assurances habitation", 965),
    ("simuler un crédit immobilier en 2027", 966),
    ("vérifier une entreprise avant d'y postuler", 967),
    ("préparer mon entretien d'embauche avec la méthode star", 968),
    ("négocier ma rupture conventionnelle", 969),
    ("j'ai mal au poignet au bureau depuis 6 mois", 970),
    ("conflit avec un collègue qui prend mes idées", 971),
    ("organiser le pot de départ de mon collègue", 972),
    ("mon net a baissé sans explication sur ma paie", 973),
    ("déclarer mes revenus en mai 2027", 974),
    ("faire reconnaître ma tendinite comme maladie pro", 975),
    ("acheter en vefa un appartement neuf en 2027", 976),
    ("louer mon bien en meublé ou en nu en 2027", 977),
    ("préparer ma retraite à 64 ans", 978),
    ("faire un audit énergétique avant de louer", 979),
    ("créer une sci avec ma famille en 2027", 980),
    ("mon artisan a bâclé la toiture", 981),
    ("je suis en surendettement, que faire", 982),
    ("acheter un iphone reconditionné en sécurité", 983),
    ("road-trip en van aménagé cet été 2027", 984),
    ("mariage écolo à petit budget en 2027", 985),
    ("faire le gr20 en trek en 2027", 986),
    ("organiser l'evjf de ma sœur en 2027", 987),
    ("faire la vélodyssée à vélo en 2027", 988),
    ("expédition kayak sur la dordogne", 989),
    ("partir en volontariat international vsi en 2027", 990),
    ("déménager au canada en 2027", 991),
    ("acheter un appartement au portugal en 2027", 992),
    ("mon vol a 5h de retard, quelle indemnisation", 993),
    ("quelle assurance voyage pour la thaïlande", 994),
    ("road-trip moto dans les alpes en 2027", 995),
    ("organiser notre séminaire d'entreprise en 2027", 996),
    ("changer de poste en interne en 2027", 997),
    ("prendre un congé sabbatique d'un an", 998),
    ("faire mon bilan 2026 et poser mes objectifs 2027", 999),

    ("préparer l'ai act haut risque annexe iii décembre 2027", 900), ("ai act haut risque annexe iii", 900), ("préparer l'ai act haut risque décembre 2027", 900),
    ("étiquetage contenu généré ia", 901),
    ("management algorithmique ia au travail", 902),
    ("modèle ia local ollama", 903),
    ("agent vocal support client 2027", 904),
    ("skill agent malveillante clawhub", 905),
    ("certificat tls 64 jours lets encrypt", 906),
    ("attaque ia autonome 2027", 907),
    ("zero trust agents identités", 908),
    ("protéger api scraping bots ia", 909),
    ("don argent 50 000 euros taux 6 pourcent 2027", 910),
    ("indemnité rupture plafonnée pass 2027", 911),
    ("transparence salariale directive ue 2027", 912),
    ("etias 2027 autorisation voyage", 913),
    ("train munich rome 2027", 914),
    ("canicule été 2027 se préparer", 915),
    ("micro-rituels régulation nerveuse", 916),
    ("capteur glycémie cgm suivi", 917),
    ("semaine 4 jours négocier", 918),
    ("reconversion cybersécurité 2027", 919),
    ("droit déconnexion mails soir", 920),
    ("bore-out ennui travail", 921),
    ("skills-based hiring recrutement compétences", 922),
    ("dumbphone réduire écran", 923),
    ("hébergement européen souveraineté données", 924),
    ("agent client protocol acp rabbit 2", 925),
    ("intelligent ui formulaires générés ia", 926),
    ("tarification hybride logiciels ia budget", 927),
    ("shadow ia outils non déclarés", 928),
    ("world model simulation logistique", 929),
    ("musique ia suno jingle", 930),
    ("robots humanoïdes usine 2027", 931),
    ("ees contrôle biométrique frontière", 932),
    ("graduate visa uk 18 mois", 933),
    ("powerbank cabine avion 2027", 934),
    ("anah aides rénovation recentrées 2027", 935),
    ("pacte papin reprise salariés", 936),
    ("prévention rps indicateur 2027", 937),
    ("geo aeo être cité moteurs ia", 938),
    ("verifiability vérifier sorties agent", 939),
    ("scraping légal robots.txt rgpd", 940),
    ("nutrition cardiovasculaire créatine preuves", 941),
    ("sleep tourism hôtel sommeil", 942),
    ("ia on-device téléphone local", 943),
    ("notebooklm ancré fact-check", 944),
    ("prompt caveman concision", 945),
    ("opt-out llms.txt entraînement ia", 946),
    ("agent one-shot jetable", 947),
    ("audit cnil 1,5 million contrôles", 948),
    ("bilan 2026 objectifs 2027 smart", 949),
    ("pse plan sauvegarde emploi", 950),
    ("accord intéressement participation", 951),
    ("addiction paris écrans prévention", 952),
    ("fraude carte bancaire opposition", 953),
    ("passeport volé consulat laissez-passer", 954),
    ("ants démarche passeport en ligne", 955),
    ("love scam site rencontre arnaque", 956),
    ("compte piraté récupération 2fa", 957),
    ("expatriation portugal visa 2027", 958),
    ("voiture électrique occasion soh batterie", 959),
    ("borne recharge wallbox domicile aides", 960),
    ("rénovation globale dpe passoire", 961),
    ("arnaque annonce location logement", 962),
    ("testament olographe notaire", 963),
    ("pea compte-titres etf monde", 964),
    ("assurance habitation multirisque comparer", 965),
    ("simulation crédit immobilier taeg", 966),
    ("due diligence vérifier entreprise", 967),
    ("entretien embauche méthode star", 968),
    ("rupture conventionnelle négocier indemnité", 969),
    ("tms usure professionnelle ergonomie", 970),
    ("conflit collègue dispute travail", 971),
    ("pot de départ organiser équipe", 972),
    ("fiche de paie lire comprendre", 973),
    ("déclaration revenus mai 2027 impots", 974),
    ("maladie professionnelle reconnaissance cpam", 975),
    ("achat vefa appartement neuf", 976),
    ("lmnp meublé vs location nue", 977),
    ("préparer retraite 64 ans trimestres", 978),
    ("audit énergétique dpe avant travaux", 979),
    ("créer sci société civile immobilière", 980),
    ("litige artisan garantie décennale", 981),
    ("surendettement dossier banque de france", 982),
    ("acheter reconditionné back market", 983),
    ("van aménagé road-trip park4night", 984),
    ("mariage écolo petit budget", 985),
    ("trek gr20 randonnée plusieurs jours", 986),
    ("evjf evg organiser", 987),
    ("expédition vélo eurovélo", 988),
    ("kayak canoë expédition rivière", 989),
    ("vsi volontariat international", 990),
    ("déménagement international conteneur douane", 991),
    ("achat immobilier étranger portugal", 992),
    ("vol retardé indemnisation 261", 993),
    ("assurance voyage rapatriement sanitaire", 994),
    ("road-trip moto équipement casque", 995),
    ("séminaire entreprise team-building", 996),
    ("mobilité interne changement de poste", 997),
    ("congé sabbatique pause carrière", 998),
    ("résolutions nouvelle année 2027", 999),

    # --- Merge SkillsAI (skills 1000-1310, tvprodel/SkillsAI) ---
    ("demande", 1000),
    ("utilisateur", 1003),
    ("architecture", 1004),
    ("active", 1005),
    ("migration", 1006),
    ("replication", 1007),
    ("securite", 1008),
    ("campagnes", 1011),
    ("definir", 1012),
    ("evaluer", 1019),
    ("prioriser", 1020),
    ("valider", 1023),
    ("anti-bot", 1029),
    ("documentation", 1030),
    ("demarre", 1032),
    ("migrer", 1033),
    ("controllers", 1039),
    ("construire", 1041),
    ("backups", 1043),
    ("utilisateurs", 1045),
    ("blazor", 1049),
    ("modelise", 1055),
    ("construction", 1059),
    ("limite", 1060),
    ("capacity", 1062),
    ("certificat", 1063),
    ("taches", 1064),
    ("concois", 1067),
    ("optimise", 1068),
    ("verifie", 1073),
    ("charge", 1077),
    ("cartographier", 1078),
    ("comparer", 1079),
    ("audits", 1080),
    ("nouveau", 1087),
    ("baisse", 1089),
    ("constitution", 1091),
    ("derive", 1092),
    ("incoherents", 1097),
    ("conception", 1098),
    ("exploration", 1103),
    ("debian", 1104),
    ("reprise", 1108),
    ("docker-compose", 1109),
    ("dockerfile", 1110),
    ("js-rendered", 1113),
    ("deployer", 1117),
    ("migrations", 1118),
    ("execution", 1124),
    ("auditer", 1127),
    ("preparation", 1128),
    ("entreprise", 1129),
    ("regles", 1132),
    ("specification", 1134),
    ("chutes", 1139),
    ("demarrage", 1143),
    ("validation", 1146),
    ("export", 1150),
    ("complexe", 1151),
    ("relecture", 1152),
    ("grill-me", 1154),
    ("i-have-adhd", 1158),
    ("automatise", 1160),
    ("incident", 1161),
    ("accessibilite", 1162),
    ("workflows", 1169),
    ("reponses", 1173),
    ("alternative", 1177),
    ("integrer", 1183),
    ("requetes", 1184),
    ("comprendre", 1185),
    ("comparaison", 1192),
    ("production", 1193),
    ("compare", 1197),
    ("integration", 1198),
    ("nestjs", 1202),
    ("segmentation", 1203),
    ("pannes", 1209),
    ("installe", 1220),
    ("elaborer", 1221),
    ("preparer", 1223),
    ("surcharge", 1228),
    ("latence", 1229),
    ("configure", 1231),
    ("processus", 1233),
    ("modification", 1244),
    ("recueil", 1254),
    ("registre", 1259),
    ("roast-my-idea", 1260),
    ("uipath", 1261),
    ("vulnerabilites", 1266),
    ("realiser", 1269),
    ("traitement", 1280),
    ("monitoring", 1282),
    ("service", 1284),
    ("glossaire", 1286),
    ("defauts", 1287),
    ("typescript", 1292),
    ("transition", 1294),
    ("refonte", 1299),
    ("hypotheses", 1300),
    ("opquast", 1308),
    # --- Vague 14 (skills 1311-1350) ---
    ("pelouse alternative", 1311),
    ("haie fleurie", 1312),
    ("smart cooking", 1313),
    ("preparation repas semaine", 1314),
    ("maison connectée sobre", 1315),
    ("tendance déco 2027", 1316),
    ("cni électronique", 1317),
    ("permis numérique contrôle", 1318),
    ("programme sport ia", 1319),
    ("nutrition ia", 1320),
    ("apprendre avec l'ia", 1321),
    ("idée cadeau ia", 1322),
    ("agent voyage ia", 1323),
    ("gestionnaire dépenses ia", 1324),
    ("mieux dormir ia", 1325),
    ("agenda intelligent 2027", 1326),
    ("santé mentale ia", 1327),
    ("liste de courses ia", 1328),
    ("actualités ia 2027", 1329),
    ("changer d'appartement", 1330),
    ("check-up annuel", 1331),
    ("autonomie senior", 1332),
    ("vaccins chien chat", 1333),
    ("alarme maison", 1334),
    ("trousse secours", 1335),
    ("faux courrier impôts", 1336),
    ("passkey fido2", 1337),
    ("dossier vital numérique", 1338),
    ("prévenir cambriolage vacances", 1339),
    ("entretien vélo 2027", 1340),
    ("rédiger un mail pro", 1341),
    ("parler en public", 1342),
    ("espagnol ia", 1343),
    ("mémoriser un livre", 1344),
    ("augmentation 2027", 1345),
    ("morning routine", 1346),
    ("faire le tri", 1347),
    ("revue annuelle évaluation", 1348),
    ("cuisiner les restes", 1349),
    ("objectifs 2028", 1350),
    ("immersion quotidienne", 1351),
    ("vivre en immersion", 1351),
    ("shadowing audio", 1352),
    ("repéter à voix haute", 1352),
    ("cartes mémoire espacées", 1353),
    ("anki vocabulaire", 1353),
    ("business english", 1354),
    ("anglais professionnel réunion", 1354),
    ("apprendre 3 langues en même temps", 1355),
    ("plusieurs langues parallèles", 1355),
    ("écouter sans sous-titres", 1356),
    ("podcasts en langue étrangère", 1356),
    ("lire en anglais", 1357),
    ("graded readers", 1357),
    ("romans en langue originale", 1357),
    ("job interview in english", 1358),
    ("entretien d'embauche en anglais", 1358),
    ("mon compte formation", 1359),
    ("reste à charge cpf 150 euros", 1359),
    ("plafond cpf", 1359),
    ("certification utiliser l'ia", 1360),
    ("explore ia janvier 2027", 1360),
    ("impulsion ia", 1360),
    ("formation hybride présentiel distanciel", 1361),
    ("parcours mixte e-learning", 1361),
    ("atelier ia entreprise", 1362),
    ("sensibiliser collègues ia", 1362),
    ("formation ia collègues", 1362),
    ("mesurer l'impact d'une formation", 1363),
    ("kirkpatrick 4 niveaux", 1363),
    ("roi formation", 1363),
    ("apprendre l'ia seul", 1364),
    ("se former à l'ia gratuitement", 1364),
    ("parcours perso ia", 1364),
    ("decision tree choix complexe", 1365),
    ("schéma branches probabilités", 1365),
    ("qui décide dans l'équipe", 1366),
    ("rôles clairs décision", 1366),
    ("une seule personne responsable", 1366),
    ("conséquences à 10 minutes 10 mois 10 ans", 1367),
    ("comment je me sentirai dans 10 ans", 1367),
    ("biais de confirmation", 1368),
    ("coût de l'inaction", 1368),
    ("décision en environnement VUCA", 1368),
    ("effet d'ancrage", 1368),
    ("ai product vision", 1369),
    ("promesse feature ia", 1369),
    ("pourquoi cette feature ia maintenant", 1369),
    ("time to value feature ia", 1370),
    ("premier succès utilisateur ia", 1370),
    ("activer une feature ia", 1370),
    ("taux d'utilisation feature ia", 1371),
    ("wau de notre outil ia", 1371),
    ("adoption ia en production", 1371),
    ("quelle skill utiliser pour ça", 1372),
    ("trouver la bonne skill", 1372),
    ("le routeur ne trouve rien", 1372),
    ("enchaîner plusieurs skills", 1373),
    ("chaîne de skills", 1373),
    ("dépendances entre skills", 1373),
    ("zoning bureau primaire secondaire tertiaire", 1374),
    ("bureau encombré ranger", 1374),
    ("un tiroir une catégorie", 1374),
    ("traiter le courrier immédiatement", 1375),
    ("ne toucher qu'une fois un document", 1375),
    ("tas de papiers qui grossit", 1375),
    ("scanner ses papiers 2027", 1376),
    ("coffre-fort numérique papiers", 1376),
    ("se débarrasser du papier", 1376),
    ("sauvegarde 3-2-1", 1376),
    ("trier ses papiers 15 min par semaine", 1377),
    ("corbeille à papier chaque vendredi", 1377),
    ("entretien hebdomadaire du bureau", 1377),
    ("réunion hybride bien équipée", 1378),
    ("micro de salle visio", 1378),
    ("certains en salle d'autres en visio", 1378),
    ("donner procuration en ligne", 1379),
    ("faire une démarche à ma place", 1379),
    ("mandat pour démarche administrative", 1379),
    ("business model saas", 1380),
    ("revenus récurrents modèle", 1380),
    ("usage-based pricing", 1380),
    ("cac vs ltv", 1381),
    ("fidélité client plutôt que nouveaux clients", 1381),
    ("réduire le churn", 1381),
    ("feuille de route entreprise 2027-2029", 1382),
    ("objectifs stratégiques 3 ans", 1382),
    ("stratégie 2029", 1382),
    ("se développer à l'international", 1383),
    ("pays cibles export", 1383),
    ("team france export aides", 1383),
    ("racheter une entreprise valorisation", 1384),
    ("multiples ebitda valorisation", 1384),
    ("audit avant rachat", 1384),
    ("développement durable entreprise", 1385),
    ("conformité csrd 2027", 1385),
    ("empreinte carbone entreprise", 1385),
    ("gérer ses références zotero", 1386),
    ("citer en apa vancouver", 1386),
    ("bibliographie mémoire propre", 1386),
    ("lire un papier scientifique critique", 1387),
    ("p-value intervalle de confiance expliqué", 1387),
    ("biais de publication étude", 1387),
    ("systematic review prisma 2027", 1388),
    ("protocole pico revue littérature", 1388),
    ("diagramme prisma sélection études", 1388),
    ("chercher les sources contraires", 1389),
    ("recherche d'information sans biais", 1389),
    ("méthode du contradicteur recherche", 1389),
    ("trouver un décret au journal officiel", 1390),
    ("loi en vigueur 2027 légifrance", 1390),
    ("code consolidé article", 1390),
    ("modèle en étoile data warehouse", 1391),
    ("table de faits et dimensions", 1391),
    ("star schema 2027", 1391),
    ("quel graphique pour mes données", 1392),
    ("barres camembert courbe 2027", 1392),
    ("visualisation de données claire", 1392),
    ("fiche dataset documentation", 1393),
    ("datasheet données biais licence", 1393),
    ("documenter avant de partager un csv", 1393),
    ("trouver un dataset public 2027", 1394),
    ("data.gouv insee eurostat", 1394),
    ("dataset hugging face licence", 1394),
    ("jeu de test référence agent ia", 1395),
    ("evals agent ia golden dataset", 1395),
    ("bench de prompts 2027", 1395),
    ("nettoyer données entraînement llm", 1396),
    ("format jsonl chat template 2027", 1396),
    ("détecter les fuites train test", 1396),
    ("évaluer un rag fidélité pertinence", 1397),
    ("métriques ragas deepeval 2027", 1397),
    ("context precision recall rag", 1397),
    ("question hostile journaliste technique du pont", 1398),
    ("ne pas répondre à une accusation en interview", 1398),
    ("interview difficile 2027", 1398),
    ("annoncer un licenciement avec humanité", 1399),
    ("communiquer une fusion difficile 2027", 1399),
    ("message de changement douloureux", 1399),
    ("squash mes commits", 1400),
    ("historique git propre", 1400),
    ("rebase avant push", 1400),
    ("review une PR", 1401),
    ("donner du feedback code", 1401),
    ("approuver une pull request", 1401),
    ("git conflict", 1402),
    ("merge conflict", 1402),
    ("résoudre un conflit git", 1402),
    ("pre-commit automatique", 1403),
    ("hook git avant commit", 1403),
    ("husky precommit", 1403),
    ("gitflow ou trunk based", 1404),
    ("workflow git équipe", 1404),
    ("github flow vs gitflow", 1404),
    ("refactorer code legacy", 1405),
    ("petits pas refactoring", 1405),
    ("characterization tests", 1405),
    ("doc qui colle au code", 1406),
    ("documentation dans le repo", 1406),
    ("mkdocs docusaurus 2027", 1406),
    ("quand commenter le code", 1407),
    ("pourquoi pas quoi commentaire", 1407),
    ("commentaires morts", 1407),
    ("try catch ciblé", 1408),
    ("exceptions métier", 1408),
    ("message erreur actionnable", 1408),
    ("logs en JSON structurés", 1409),
    ("niveaux de log debug info warn error", 1409),
    ("correlation id log", 1409),
    ("variables d'environnement app", 1410),
    ("config par environnement dev prod", 1410),
    ("12 factor app", 1410),
    ("image docker petite taille", 1411),
    ("multi-stage build docker", 1411),
    ("dockerfile optimisé 2027", 1411),
    ("déployer sur kubernetes", 1412),
    ("manifests yaml k8s", 1412),
    ("configmap secret k8s 2027", 1412),
    ("accélérer github actions", 1413),
    ("cache dépendances CI", 1413),
    ("jobs parallèles matrix", 1413),
    ("consumer contract testing", 1414),
    ("pact tests API microservices", 1414),
    ("éviter rupture API entre services", 1414),
    ("k6 test de performance", 1415),
    ("locust charge test", 1415),
    ("p95 latence seuil CI", 1415),
    ("monitoring app prometheus", 1416),
    ("dashboards grafana alertes", 1416),
    ("métriques custom promql 2027", 1416),
    ("alertes qui ne spamment pas", 1417),
    ("réduire le bruit des alertes", 1417),
    ("alert fatigue 2027", 1417),
    ("canary deployment", 1418),
    ("rollout 5 25 50 100%", 1418),
    ("flagger nouvelle version", 1418),
    ("créer un index composite", 1419),
    ("covering index", 1419),
    ("explain analyze requête lente", 1419),
    ("partition by sql", 1420),
    ("row_number rank sql", 1420),
    ("lag lead sql", 1420),
    ("niveau isolation read committed serializable", 1421),
    ("deadlock base de données", 1421),
    ("éviter les deadlocks", 1421),
    ("mongodb ou redis", 1422),
    ("cassandra scylla écriture massive", 1422),
    ("base NoSQL choisir 2027", 1422),
    ("mettre en cache avec redis", 1423),
    ("TTL invalidation cache", 1423),
    ("cache-aside lazy loading", 1423),
    ("valider entrées pydantic zod", 1424),
    ("contraintes BDD check fk", 1424),
    ("requêtes paramétrées", 1424),
    ("organiser ses prompts", 1425),
    ("composants de prompt réutilisables", 1425),
    ("prompts versionnés git", 1425),
    ("exemples dans le prompt LLM", 1426),
    ("few shot prompting", 1426),
    ("guider le format avec des exemples", 1426),
    ("forcer le JSON en sortie LLM", 1427),
    ("valider la sortie JSON du modèle", 1427),
    ("json schema prompt", 1427),
    ("boucle react agent", 1428),
    ("thought action observation", 1428),
    ("agent qui planifie ses étapes", 1428),
    ("function calling bien nommé", 1429),
    ("décrire un outil pour LLM", 1429),
    ("outils idempotents agent", 1429),
    ("gros contexte LLM 1M tokens", 1430),
    ("lost in the middle", 1430),
    ("résumer les vieilles parties", 1430),
    ("résumer une longue conversation LLM", 1431),
    ("quand compacter le contexte", 1431),
    ("garder décisions et code en cours", 1431),
    ("multi-agents par domaine", 1432),
    ("orchestrateur délègue experts", 1432),
    ("agent-as-organization 2027", 1432),
    ("validation humaine agent avant action", 1433),
    ("points d'approbation agent", 1433),
    ("agent qui demande avant d'agir", 1433),
    ("mémoire long terme agent", 1434),
    ("vector store préférences utilisateur", 1434),
    ("mémoire épisodique sessions", 1434),
    ("tester 2 prompts en prod", 1435),
    ("A/B test prompt LLM", 1435),
    ("quelle version du prompt garder", 1435),
    ("citer les sources du LLM", 1436),
    ("réduire hallucinations citations", 1436),
    ("dire je ne sais pas si pas dans les docs", 1436),
    ("le LLM se relit et corrige", 1437),
    ("vérification en 2 passes", 1437),
    ("grille de relecture réponse", 1437),
    ("modèle local téléphone 2027", 1438),
    ("llama.cpp mobile offline", 1438),
    ("quantization GGUF Q4 batterie", 1438),
    ("afficher la réponse LLM en streaming", 1439),
    ("état thinking du modèle", 1439),
    ("annuler une génération en cours", 1439),
    ("bloquer données perso avant LLM", 1440),
    ("masquer email IBAN CNI automatiquement", 1440),
    ("guardrail PII entreprise 2027", 1440),
    ("petit modèle puis grand modèle", 1441),
    ("router tâche au bon LLM", 1441),
    ("réduire coût inférence cascade", 1441),
    ("réponses LLM en cache sémantique", 1442),
    ("requêtes similaires même réponse", 1442),
    ("éviter réinférer questions proches", 1442),
    ("quel modèle embedding 2027", 1443),
    ("MTEB benchmark embeddings", 1443),
    ("dimension 384 ou 3072", 1443),
    ("découper documents pour RAG", 1444),
    ("overlap 20% chunking", 1444),
    ("chunking hiérarchique résumé parent", 1444),
    ("PR auto dépendances Dependabot", 1445),
    ("renovate bot mises à jour", 1445),
    ("CVE corriger en priorité", 1445),
    ("renouveler clés API automatiquement", 1446),
    ("vault hashicorp rotation 90 jours", 1446),
    ("fuite de clé détection", 1446),
    ("réduire permissions admin cloud", 1447),
    ("audit accès AWS trop larges", 1447),
    ("clés longue durée supprimer", 1447),
    ("Signal ou Proton Mail 2027", 1448),
    ("vérifier les clés E2EE", 1448),
    ("messagerie confidentielle équipe", 1448),
    ("déployer passkeys entreprise 2027", 1449),
    ("YubiKey clés matérielles", 1449),
    ("remplacer mot de passe par passkey", 1449),
    ("authorization code PKCE 2027", 1450),
    ("jamais le flow implicit", 1450),
    ("scopes OAuth minimaux", 1450),
    ("protéger mon site d'une attaque DDoS", 1451),
    ("Cloudflare WAF règles OWASP", 1451),
    ("rate limiting par IP 2027", 1451),
    ("content security policy 2027", 1452),
    ("script-src nonce hash", 1452),
    ("bloquer XSS avec CSP", 1452),
    ("centraliser logs sécurité Wazuh", 1453),
    ("détecter brute force dans les logs", 1453),
    ("corrélation alertes sécurité", 1453),
    ("exercice de crise sécurité informatique", 1454),
    ("simuler un ransomware en interne", 1454),
    ("tester le plan de réponse incident", 1454),
    ("RGPD dès la conception", 1455),
    ("minimiser données collectées", 1455),
    ("droit à l'effacement facile", 1455),
    ("certificate pinning mobile", 1456),
    ("stockage sécurisé Keychain Android Keystore", 1456),
    ("détecter root jailbreak", 1456),
    ("vérifier signature paquet npm pip", 1457),
    ("SLSA niveau 3 provenance build", 1457),
    ("--require-hashes pip", 1457),
    ("détecter les scans sur mon réseau", 1458),
    ("cowrie honeypot SSH", 1458),
    ("canary token faux fichier", 1458),
    ("obtenir la certification ISO 27001", 1459),
    ("gap analysis ISO 27001 2027", 1459),
    ("préparer audit certification sécurité", 1459),
    ("airflow ou prefect choisir 2027", 1460),
    ("dagster assets data-aware", 1460),
    ("orchestrer ETL complexe", 1460),
    ("colonne supprimée en amont casse mon ETL", 1461),
    ("data contracts entre producteurs et consommateurs", 1461),
    ("monitoring schéma Soda 2027", 1461),
    ("influxdb ou timescaledb 2027", 1462),
    ("hypertable postgresql séries temps", 1462),
    ("downsampling agrégation métriques", 1462),
    ("snowflake ou databricks 2027", 1463),
    ("delta lake iceberg lakehouse", 1463),
    ("éviter le data swamp", 1463),
    ("consumer group kafka lag", 1464),
    ("combien de partitions topic", 1464),
    ("exactly-once kafka 2027", 1464),
    ("k-anonymat k=5 dataset", 1465),
    ("hash avec sel pseudonymisation", 1465),
    ("test ré-identification risque", 1465),
    ("d'où vient cette colonne", 1466),
    ("impact analysis si source casse", 1466),
    ("OpenLineage Marquez 2027", 1466),
    ("baisser coût requêtes BigQuery", 1467),
    ("partitionnement clustering Snowflake", 1467),
    ("archivage froid Glacier", 1467),
    ("feast ou tecton 2027", 1468),
    ("éviter le train/serve skew", 1468),
    ("features ML réutilisables online offline", 1468),
    ("ELK ou Loki choisir 2027", 1469),
    ("rechercher dans tous les logs d'un coup", 1469),
    ("logs distribués ClickHouse rapide", 1469),
    ("versionner un modèle ML", 1470),
    ("MLflow model registry 2027", 1470),
    ("DVC données versionnées S3", 1470),
    ("déployer LLM interne vLLM 2027", 1471),
    ("endpoint OpenAI compatible local", 1471),
    ("Ollama vs vLLM débit", 1471),
    ("faire tourner LLM en local 2027", 1472),
    ("ollama pull mistral Q4", 1472),
    ("llama.cpp CPU embarqué", 1472),
    ("entraîner petit modèle qui imite GPT", 1473),
    ("distillation chain-of-thought", 1473),
    ("SLM maison spécialisé", 1473),
    ("DPO vs RLHF choisir 2027", 1474),
    ("paires préférées non préférées", 1474),
    ("aligner un modèle sur le ton sécurité", 1474),
    ("exécuter code agent en sécurité", 1475),
    ("conteneur jetable par tâche agent", 1475),
    ("réseau allowlist agent IA", 1475),
    ("pourquoi mon agent a échoué", 1476),
    ("logger chaque appel d'outil", 1476),
    ("Langfuse LangSmith tracer agent", 1476),
    ("BM25 plus embeddings combinés", 1477),
    ("fusion RRF scores retrieval", 1477),
    ("RAG hybride lexical sémantique", 1477),
    ("extraire graphe de connaissances corpus", 1478),
    ("Neo4j ou Kuzu 2027", 1478),
    ("requêtes multi-sauts RAG graphe", 1478),
    ("fine-tuner 70B sur 1 GPU 24 Go", 1479),
    ("LoRA rang 8 ou 16", 1479),
    ("QLoRA Q4 + LoRA mémoire", 1479),
    ("écrire une spec de feature", 1480),
    ("one-pager produit", 1480),
    ("pas un PRD de 30 pages", 1480),
    ("quelle métrique reine choisir", 1481),
    ("décomposer la north star en leviers", 1481),
    ("arbre de métriques 2027", 1481),
    ("la feature a-t-elle marché ? A/B test feature", 1482),
    ("groupe témoin vs exposé", 1482),
    ("décider ship kill iterate", 1482),
    ("tester un parcours avec Maze", 1483),
    ("5 utilisateurs ça suffit (Nielsen)", 1483),
    ("recruter testeurs panel 2027", 1483),
    ("WCAG 2.2 niveau AA dès le design", 1484),
    ("contraste 4,5:1 couleurs", 1484),
    ("navigation clavier complète", 1484),
    ("préparer mon app au multilingue", 1485),
    ("pluriels et dates par locale", 1485),
    ("RTL arabe hébreu support", 1485),
    ("répondre aux utilisateurs qui donnent un avis", 1486),
    ("changelog 'vous avez demandé'", 1486),
    ("taux de fermeture des feedbacks", 1486),
    ("arrêter une feature proprement", 1487),
    ("prévenir 90 jours avant fermeture", 1487),
    ("migrer les utilisateurs d'une feature supprimée", 1487),
    ("ajouter un assistant IA dans mon app", 1488),
    ("copilote contextuel voit l'écran", 1488),
    ("suggestions IA non intrusives", 1488),
    ("l'IA dit je ne sais pas dans l'UI", 1489),
    ("indicateur de confiance réponse IA", 1489),
    ("avertissement sujets sensibles IA", 1489),
    ("modérer contenus générés IA en prod", 1490),
    ("filtre LLM toxicité PII classification", 1490),
    ("file de modération humaine cas limites", 1490),
    ("coût d'une feature IA par user", 1491),
    ("combien coûte notre chatbot par requête", 1491),
    ("seuil rentabilité feature IA", 1491),
    ("couper une feature IA en 1 clic", 1492),
    ("désactiver proprement une IA en prod", 1492),
    ("message utilisateurs si IA down", 1492),
    ("notre UI est incohérente audit", 1493),
    ("composants réels vs design system", 1493),
    ("combien de boutons différents avons-nous ?", 1493),
    ("v0 ou lovable pour prototyper", 1494),
    ("maquette en app cliquable en 1 jour", 1494),
    ("tester une idée sans dev", 1494),
    ("désactiver animations si OS demande", 1495),
    ("pas de flash plus de 3 par seconde", 1495),
    ("animation réduite accessible", 1495),
    ("dark mode produit 2027", 1496),
    ("high contrast WCAG AAA 7:1", 1496),
    ("prefers-color-scheme détecter OS", 1496),
    ("exit 2 trop fréquent routeur", 1497),
    ("demandes non routées récurrentes", 1497),
    ("misses --suggest ajouter synonyme", 1497),
    ("automatiser sans SaaS US n8n", 1498),
    ("n8n sur mon serveur 2027", 1498),
    ("workflows n8n templates communauté", 1498),
    ("transcrire une réunion automatiquement", 1499),
    ("Fireflies ou Otter 2027", 1499),
    ("extraire décisions et actions d'une réunion", 1499),
    ("unity ou godot ou unreal", 1500),
    ("quel moteur pour mon jeu 2027", 1500),
    ("godot 4 vs unity 2027", 1500),
    ("boucle de jeu fixe 60 hz", 1501),
    ("interpolation render entre deux états", 1501),
    ("delta time vs fixed dt", 1501),
    ("charger un niveau sans freeze", 1502),
    ("scènes additives menu + hud + niveau", 1502),
    ("transition fondu entre niveaux", 1502),
    ("3 slots de sauvegarde", 1503),
    ("sérialiser l'état du jeu en JSON", 1503),
    ("migration de save entre versions", 1503),
    ("remapper les contrôles par le joueur", 1504),
    ("input actions unity ou inputmap godot", 1504),
    ("AZERTY et QWERTY supportés", 1504),
    ("caméra qui suit le joueur en 2D", 1505),
    ("deadzone caméra zone morte", 1505),
    ("lookahead caméra selon direction", 1505),
    ("caméra qui ne traverse pas les murs", 1506),
    ("lock-on ennemi caméra 3D", 1506),
    ("FOV qui augmente en sprint", 1506),
    ("AABB rectangle aligné collision", 1507),
    ("cercle vs cercle collision", 1507),
    ("SAT rectangles orientés", 1507),
    ("séparer hitbox et hurtbox", 1508),
    ("i-frames après un coup", 1508),
    ("knockback directionnel", 1508),
    ("saut variable selon appui long court", 1509),
    ("gravité custom plateformer", 1509),
    ("friction au sol glisser", 1509),
    ("sauter 0,1 s après avoir quitté le sol", 1510),
    ("jump buffer appuyer avant d'atterrir", 1510),
    ("tolérance de saut plateformer", 1510),
    ("diagonale pas plus rapide normaliser", 1511),
    ("dash avec cooldown et i-frames", 1511),
    ("top-down 2D déplacement fluide", 1511),
    ("peindre un niveau avec des tuiles", 1512),
    ("autotiling 47 tuiles selon voisins", 1512),
    ("collision auto par tuile tilemap", 1512),
    ("générer un donjon aléatoire rooms corridors", 1513),
    ("roguelike niveau procédural 2027", 1513),
    ("salles sans chevauchement + MST", 1513),
    ("générer une grotte naturelle automate cellulaire", 1514),
    ("lissage 4-5 itérations 45% remplissage", 1514),
    ("garder la plus grande zone connexe", 1514),
    ("générer une île avec Perlin noise", 1515),
    ("heightmap terrain 3D procédural", 1515),
    ("octaves fractal bruit Perlin 2027", 1515),
    ("générer niveau WFC wave function collapse", 1516),
    ("propagation des contraintes tuiles voisines", 1516),
    ("entropie choisir cellule la plus contrainte", 1516),
    ("A* sur grille open set heap", 1517),
    ("flow field pour 100 unités même chemin", 1517),
    ("poids terrain route herbe eau", 1517),
    ("baker la navigation 3D sur le niveau", 1518),
    ("NavigationAgent suit le navmesh", 1518),
    ("obstacles dynamiques navmesh local", 1518),
    ("machine à états ennemi patrouille attaque", 1519),
    ("FSM simple lisible debuggable", 1519),
    ("transition si joueur à moins de 8 m", 1519),
    ("ennemi qui voit dans un cône 90°", 1520),
    ("l'ennemi entend le joueur courir", 1520),
    ("mémoire : dernier point vu puis chercher", 1520),
    ("IA par utilité score 0-1 choisir action", 1521),
    ("PNJ avec besoins faim sommeil social", 1521),
    ("évaluer chaque action toutes les 0,5 s", 1521),
    ("PNJ autonome qui planifie pour atteindre un objectif", 1522),
    ("actions avec préconditions et effets", 1522),
    ("plan le moins cher avec A* sur les états", 1522),
    ("garde avec cône de vision mesh translucide", 1523),
    ("3 raycasts tête corps pieds visibilité", 1523),
    ("jauge de détection qui monte descend", 1523),
    ("joueur visible si aucun mur entre (raycast)", 1524),
    ("tir hitscan raycast premier hit", 1524),
    ("clic souris vers position monde 3D", 1524),
    ("ennemis qui flanquent le joueur", 1525),
    ("tous attaquent la même cible (focus)", 1525),
    ("tank + dps + soigneur rôles", 1525),
    ("boss 3 phases selon PV transition cinématique", 1526),
    ("attaque télégraphiée marque au sol 1 s avant", 1526),
    ("fenêtre de dégâts après l'attaque du boss", 1526),
    ("vagues d'ennemis qui durcissent", 1527),
    ("budget de points par vague (slime 1, brute 5)", 1527),
    ("delai 10 s entre deux vagues", 1527),
    ("tirage pondéré commun 60 rare 30 épique 9 légendaire 1", 1528),
    ("pity timer après 20 monstres sans rare", 1528),
    ("drop garanti tous les 50 monstres", 1528),
    ("l'or s'inflate dans mon jeu", 1529),
    ("sources vs sinks de gold équilibrés", 1529),
    ("prix objets scalés par niveau joueur", 1529),
    ("xp niveau = 100 * 1,15^n exponentiel", 1530),
    ("déblocage donjon niveau 5 monture niveau 10", 1530),
    ("respec payant des compétences", 1530),
    ("journal de quêtes avec compteur 3/5", 1531),
    ("quête principale chaînée quêtes secondaires", 1531),
    ("récompense XP gold objet à la validation", 1531),
    ("choix de dialogue avec condition (si quête faite)", 1532),
    ("PNJ qui se souvient de ce qu'on a dit", 1532),
    ("réputation qui change selon les réponses", 1532),
    ("traduire les textes du jeu en 5 langues", 1533),
    ("clés ui.title quest.desc par langue JSON", 1533),
    ("pseudo-localisation détecter débordements UI", 1533),
    ("inventaire 5x4 slots drag drop souris manette", 1534),
    ("potions stackées x99 dans un slot", 1534),
    ("tri auto et tooltip au survol", 1534),
    ("slots arme armure anneaux", 1535),
    ("stats selon rareté x1 à x2,5", 1535),
    ("comparer avec l'objet équipé (flèche verte rouge)", 1535),
    ("recette épée = 3 fer + 1 bois à la forge", 1536),
    ("maîtrise craft : chance de +10% stats", 1536),
    ("démonter un objet récupère 50% matériaux", 1536),
    ("arbre de talents 3 branches guerrier mage voleur", 1537),
    ("points de talent gagnés par niveau", 1537),
    ("respec payant reset des talents", 1537),
    ("succès 'tuer 100 monstres' avec toast", 1538),
    ("succès caché easter egg", 1538),
    ("progression 12/50 succès et intégration Steam", 1538),
    ("sauvegarder dans le cloud automatiquement", 1539),
    ("jouer sur PC puis téléphone même progression", 1539),
    ("conflit de save : garder le plus récent", 1539),
    ("funnel tutoriel étape par étape", 1540),
    ("rétention D1 D7 D30 dashboard", 1540),
    ("envoyer événements custom à Unity Analytics", 1540),
    ("cohorte A prix 2,99 € vs B 4,99 € mesurer revenus", 1541),
    ("remote config changer difficulté sans mise à jour", 1541),
    ("significativité statistique décision ship", 1541),
    ("organiser un event Halloween 2 semaines skins niveau temporaire", 1542),
    ("battle pass 30 paliers gratuit payant", 1542),
    ("rotation mensuelle des events avec analytics", 1542),
    ("ne jamais faire confiance au client (serveur autorité)", 1543),
    ("détecter un aimbot (tirs trop précis trop vite)", 1543),
    ("shadowban : banir sans prévenir le tricheur", 1543),
    ("serveur dédié vs P2P pour mon jeu coop", 1544),
    ("relais Steam Network (pas cher, pas d'anti-triche)", 1544),
    ("client-serveur autoritaire pour un compétitif", 1544),
    ("le serveur rejoue le monde 200 ms en arrière au tir", 1545),
    ("toucher quelqu'un qui a déjà bougé (lag)", 1545),
    ("réconciliation serveur après coup", 1545),
    ("RTS en lockstep : inputs au même tick déterministe", 1546),
    ("action : snapshots serveur 20 Hz interpolés client", 1546),
    ("un joueur lent bloque tout en lockstep", 1546),
    ("mon perso répond instantanément malgré 100 ms de ping", 1547),
    ("réconciliation : état serveur + rejouer mes inputs non ack", 1547),
    ("input sequence number et acquittement serveur", 1547),
    ("filtrer les insultes automatiquement", 1548),
    ("rate limit 1 message 2 secondes anti-spam", 1548),
    ("signaler un joueur toxique → mute/ban vote", 1548),
    ("MMR qui monte de 25 si victoire", 1549),
    ("file qui accepte ±100 après 30 s ±400 après 2 min", 1549),
    ("match trouvé en moins de 2 min", 1549),
    ("composants = données pures, systèmes = logique", 1550),
    ("pas d'héritage : un ennemi = Position + Health + AI", 1550),
    ("Unity DOTS / Flecs / Bevy ECS 2027", 1550),
    ("ne plus Instantiate/Destroy à chaque tir (GC lag)", 1551),
    ("pool de 50 balles pré-allouées réutilisées", 1551),
    ("Get() depuis le pool, Release() retour au pool", 1551),
    ("fuite mémoire : +50 Mo par niveau chargé", 1552),
    ("quel système prend 8 ms de CPU ?", 1552),
    ("draw calls 2000 → batching pour passer à 200", 1552),
    ("2000 objets = 2000 draw calls trop lent", 1553),
    ("sprite atlas tout en 1 texture = 1 draw call", 1553),
    ("occlusion culling ne pas rendre caché + LOD loin", 1553),
    ("packer 500 sprites dans 2 textures 2048x2048", 1554),
    ("padding 2 px éviter le bleeding entre sprites", 1554),
    ("TexturePacker ou atlas intégré au moteur", 1554),
    ("vignette + grain pour le look film", 1555),
    ("bloom léger sur les lumières sans lag", 1555),
    ("1 seul passe post-FX sur mobile (URP)", 1555),
    ("torches qui éclairent et les murs font ombre", 1556),
    ("normal map 2D pour le relief des sprites", 1556),
    ("light occluders bloquent la lumière 2D", 1556),
    ("10 000 particules en 1 draw call (GPU instancing)", 1557),
    ("VFX Graph Unity ou shaders de particules custom", 1557),
    ("pluie/neige/explosions sans lag", 1557),
    ("caméra qui tremble 0,2 s à l'explosion", 1558),
    ("shake fort 0,5 faible 0,2 decay rapide", 1558),
    ("désactivable dans l'accessibilité (1575)", 1558),
    ("squash & stretch au saut et atterrissage", 1559),
    ("hitstop freeze 50 ms à l'impact", 1559),
    ("flash blanc + particules + son à chaque hit", 1559),
    ("états Idle Run Jump Attack avec transitions", 1560),
    ("condition vitesse superieure a 0,1 passe en Run", 1560),
    ("crossfade 0,1 s entre deux animations", 1560),
    ("9 clips (idle + 8 directions) interpolés selon X Y", 1561),
    ("déplacement 3D fluide selon la direction de la caméra", 1561),
    ("blend tree 2D vs transitions conditionnelles", 1561),
    ("pieds qui suivent le terrain (IK)", 1562),
    ("main qui tient l'arme (IK deux os)", 1562),
    ("FABRIK ou Two Bone IK sans coder la rotation", 1562),
    ("la tête du PNJ regarde le joueur (look-at)", 1563),
    ("le torse se penche vers l'objet (spine IK)", 1563),
    ("Full Body IK Unity Animator.SetIKPosition", 1563),
    ("le perso s'effondre crédiblement à la mort", 1564),
    ("chaque membre = rigidbody + joint charnière", 1564),
    ("explosion projette le ragdoll (AddForce)", 1564),
    ("mur qui se casse en morceaux Voronoi", 1565),
    ("couper un mesh en N morceaux procéduralement", 1565),
    ("cap 20 morceaux + pool pour les perfs", 1565),
    ("intégrer FMOD Studio dans Unity 2027", 1566),
    ("Wwise authoring banques sons événements", 1566),
    ("bus audio ducking (musique baisse quand dialogue)", 1566),
    ("la musique passe en combat quand un ennemi approche", 1567),
    ("layers : calm → explore → combat → boss (1526)", 1567),
    ("transition musicale douce entre les couches", 1567),
    ("chaque tir a un pitch légèrement différent (0,9-1,1)", 1568),
    ("pool de 16 voix pour les tirs (pas d'alloc)", 1568),
    ("cooldown : max 10 sons de tir par seconde", 1568),
    ("enregistrer les voix du jeu en studio (fichiers vo_quest01_03)", 1569),
    ("sous-titres synchronisés avec la VO", 1569),
    ("TTS IA de secours marqué comme tel", 1569),
    ("barre de PV rouge qui clignote sous 30 %", 1570),
    ("minimap avec marqueurs de quêtes (1531)", 1570),
    ("HUD désactivable (mode minimaliste 1575)", 1570),
    ("naviguer au clavier dans les menus (tab + entrée)", 1571),
    ("focus visible sur le bouton sélectionné", 1571),
    ("manette : A valider, B retour, croix directionnelle", 1571),
    ("astuce qui apparaît au bon moment (premier saut)", 1572),
    ("bouton 'Passer le tutoriel' toujours visible", 1572),
    ("tutoriel rejouable depuis les settings", 1572),
    ("barre de progression au chargement du niveau", 1573),
    ("charger la zone autour du joueur, décharger le loin (100 m)", 1573),
    ("monde ouvert sans écran de chargement entre les zones", 1573),
    ("preset qualité Bas Moyen Haut + résolution VSync FOV", 1574),
    ("sliders de volume Master/Music/SFX/VO séparés", 1574),
    ("remap des contrôles + sensibilité + invert Y", 1574),
    ("filtre daltonisme deutéranopie sur les barres PV/ennemis", 1575),
    ("taille de l'UI 100 à 200 %", 1575),
    ("réduire les secousses (1558) et les flashs (1495)", 1575),
    ("sous-titres des dialogues et des SFX importants", 1575),
    ("données du jeu en JSON modifiables (armes, quêtes)", 1576),
    ("dossier /mods chargé au boot avec liste on/off", 1576),
    ("API Lua pour les mods + sandbox sécurité", 1576),
    ("console / avec god noclip give tp killall", 1577),
    ("timescale 0,5 pour déboguer au ralenti", 1577),
    ("cachée en build release (anti-triche 1543)", 1577),
    ("SemVer 1.2.3 : quoi en majeur mineur patch ?", 1578),
    ("patch notes publiques lisibles par les joueurs", 1578),
    ("branche beta Steam pour tester avant prod (1581)", 1578),
    ("uploader un build Steam avec SteamPipe (branches 1578)", 1579),
    ("configurer les dépôts (fichiers Windows/Mac/Linux)", 1579),
    ("checklist de validation Steam avant mise en ligne", 1579),
    ("leaderboard Steam (top 100 mondial + amis)", 1580),
    ("cloud saves Steam (1539) + succès (1538)", 1580),
    ("lobby Steam + invitation ami + matchmaking 1549", 1580),
    ("10 captures d'écran ordonnées (loop → combat)", 1581),
    ("prix psychologique 9,99 14,99 19,99 €", 1581),
    ("objectif 20 000 wishlists avant le lancement", 1581),
    ("pub rewarded choisie par le joueur max 3/jour", 1582),
    ("IAP cosmétiques uniquement jamais pay-to-win", 1582),
    ("pas de pop-up forcée (dark patterns interdits UE 2027)", 1582),
    ("taux de drop affichés obligatoires (1528) dans le gacha", 1583),
    ("Belgique/Pays-Bas : loot box interdite sans licence 2027", 1583),
    ("pas de ciblage des mineurs (1587) par le gacha", 1583),
    ("consentement parental vérifiable pour les moins de 16 ans (13 en France)", 1584),
    ("analytics anonymisés pas de tracking des mineurs (1540)", 1584),
    ("droit à l'effacement des données d'un compte mineur", 1584),
    ("60 fps stables sur téléphone milieu de gamme", 1585),
    ("textures ASTC compressées (mémoire GPU divisée)", 1585),
    ("throttling thermique après 10 min de jeu", 1585),
    ("IL2CPP au lieu de Mono (build plus lent mais app plus rapide)", 1586),
    ("Addressables pour des patchs de 5 Mo au lieu de 200 Mo", 1586),
    ("taille de l'app inferieure a 150 Mo (ASTC + OGG + stripping)", 1586),
    ("demander le kit de dev Nintendo/Sony/Microsoft", 1587),
    ("certification TRC (Nintendo) / XR (Xbox) : checklist 2 semaines", 1587),
    ("Switch : 30 fps et 4 Go de RAM partagés, UI manette TV", 1587),
    ("soldes Steam printemps été automne hiver -50%", 1588),
    ("prix régional Steam : -70% en Inde Turquie Brésil", 1588),
    ("pas de solde dans les 30 jours après la sortie", 1588),
    ("répondre aux avis Steam négatifs en 24 h calmement", 1589),
    ("hotfix sous 48 h si bug bloquant au lancement", 1589),
    ("devlog transparent (1596) + patch notes claires (1578)", 1589),
    ("patch de 5 Mo sans re-télécharger les 150 Mo (Addressables)", 1590),
    ("DLC vérifié via Steam (1580) puis contenu débloqué", 1590),
    ("groupes remote : VO (1569), textures HD, niveaux (1573)", 1590),
    ("playmode test : simuler un tir et vérifier les PV (1508)", 1591),
    ("test save/load (1503) : round-trip identique", 1591),
    ("CI qui fait tourner les tests à chaque PR (1593)", 1591),
    ("build auto Windows Linux Mac Android à chaque commit", 1592),
    ("upload auto sur la branche beta Steam (1580)", 1592),
    ("notif Discord si le build échoue (1596)", 1592),
    ("1 niveau final poli pour montrer le jeu (pas un prototype gris)", 1593),
    ("le loop complet : exploration → combat → loot → progression", 1593),
    ("convaincre un éditeur (1594) avec le vertical slice", 1593),
    ("10-12 slides : accroche concept marché équipe budget planning", 1594),
    ("démo jouable du vertical slice (1593) pendant le pitch", 1594),
    ("combien demander à l'éditeur (1595) : 200k-2M € selon le scope", 1594),
    ("combien coûte un jeu indé en 2027 (équipe x mois + marketing + imprévus)", 1595),
    ("scope ajusté au budget : MVP (1593) d'abord", 1595),
    ("crowdfunding Kickstarter + aides régionales (CNC France)", 1595),
    ("devlog hebdo honnête (avancées + blocages)", 1596),
    ("Discord avec salon #feedback et #bugs", 1596),
    ("TikTok : 3 GIF de gameplay par semaine (juice 1559)", 1596),
    ("soumettre ma démo au Steam Next Fest (février/juin/oct 2027)", 1597),
    ("stand à un salon (PGW, PAX) : démo jouable + presse", 1597),
    ("objectif : 10k wishlists + 500 retours (1598) via la démo", 1597),
    ("8-12 testeurs du profil cible (Discord 1596 ou Prolific)", 1598),
    ("session 60 min : 30 jeu + 30 interview + questionnaire SUS 1483", 1598),
    ("enregistrement écran+visage avec consentement RGPD (1584)", 1598),
    ("European Accessibility Act en vigueur juin 2025 pour les jeux (UE)", 1599),
    ("rapport d'accessibilité publié avec le jeu", 1599),
    ("jeu jouable au clavier seul (1571) et avec lecteur d'écran", 1599),
    ("accélérer mon build vite rolldown rust", 1600),
    ("build 2,5 min à 40 s", 1600),
    ("vite 8 environment api 2027", 1600),
    ("interface dynamique sans écrire de JS (htmx)", 1601),
    ("django-htmx tokens CSRF auto", 1601),
    ("remplacer une SPA par du serveur + htmx", 1601),
    ("moins de JavaScript envoyé au client (RSC)", 1602),
    ("edge functions latence 50 ms", 1602),
    ("streaming SSR Suspense 2027", 1602),
    ("site rapide sans framework lourd (astro)", 1603),
    ("transitions animées entre pages nativement", 1603),
    ("astro islands hydratation partielle", 1603),
    ("API type-safe de bout en bout (tRPC)", 1604),
    ("tanstack start react full-stack 2027", 1604),
    ("trpc vs REST vs GraphQL choisir", 1604),
    ("app qui charge instantanément (qwik resumability)", 1605),
    ("pas de réhydratation (resumability)", 1605),
    ("qwik optimizer lazy loading auto", 1605),
    ("webgpu dans tous les navigateurs fin 2025", 1606),
    ("calcul GPU côté client compute shaders", 1606),
    ("webgpu vs webgl choisir 2027", 1606),
    ("faire tourner un modèle ML dans le navigateur", 1607),
    ("onnx runtime web backend webgpu", 1607),
    ("classification image côté client zéro serveur", 1607),
    ("faire tourner du Rust compilé en wasm partout (WASI)", 1608),
    ("component model wasm échange typé entre langages", 1608),
    ("wasm sur serveur edge CLI 2027", 1608),
    ("app desktop 600 kB avec tauri (pas electron)", 1609),
    ("PWA installable offline notifications push", 1609),
    ("tauri backend rust webview système", 1609),
    ("sélecteur CSS :has() parent selon enfant", 1610),
    ("container queries style selon conteneur", 1610),
    ("animations pilotées par le scroll @scroll-timeline", 1610),
    ("app qui marche offline puis se synchro (CRDT)", 1611),
    ("replicache ou yjs synchro sans conflit", 1611),
    ("données en local d'abord IndexedDB", 1611),
    ("latence sous 50 ms avec cloudflare workers", 1612),
    ("vercel edge functions 2027", 1612),
    ("edge vs serveur régional classique", 1612),
    ("CI front sous 3 min (rolldown + turbo cache)", 1613),
    ("build parallèle multi-cœurs rust", 1613),
    ("cache distant turbo remote caching", 1613),
    ("migrer mon projet webpack legacy vers vite", 1614),
    ("loaders webpack vers plugins vite équivalent", 1614),
    ("vite proxy dev server remplace webpack-dev-server", 1614),
    ("transitions animées entre pages sans SPA (View Transitions)", 1615),
    ("document.startViewTransition navigation fluide", 1615),
    ("::view-transition-old new group animation", 1615),
    ("page statique + îles interactives hydratées (astro)", 1616),
    ("client:load client:idle client:visible choisir", 1616),
    ("plusieurs mini-frameworks sur une page (îles)", 1616),
    ("next.js vs nuxt vs sveltekit choisir 2027", 1617),
    ("react router 7 framework mode ex-remix", 1617),
    ("quel framework pour une app métier interne", 1617),
    ("INP interaction to next paint sous 200 ms", 1618),
    ("LCP sous 2,5 s chargement plus grand élément", 1618),
    ("RUM données réelles utilisateurs vs labo Lighthouse", 1618),
    ("focus clavier visible uniquement :focus-visible", 1619),
    ("contraste automatique prefers-contrast more", 1619),
    ("ARIA 1.3 nouveaux attributs 2027", 1619),
    ("une source de tokens pour web iOS Android", 1620),
    ("style dictionary génère CSS Swift Kotlin", 1620),
    ("tokens studio synchronisé avec Figma", 1620),
    ("registry officiel MCP 40 965 serveurs vérifiés", 1621),
    ("gateway MCP entreprise audit scopes rate limit", 1621),
    ("MCP 97M téléchargements SDK 2026", 1621),
    ("protocole A2A agents de fournisseurs différents", 1622),
    ("agent card .well-known/agent.json découverte", 1622),
    ("A2A vs MCP : agent-agent vs agent-outil", 1622),
    ("MCP ou A2A pour mon agent ?", 1623),
    ("ACP fusionné dans A2A août 2025", 1623),
    ("UCP protocole paiement agent 2027", 1623),
    ("exposer ma page aux agents IA (WebMCP)", 1624),
    ("navigator.modelContext déclarer des outils JS", 1624),
    ("site agent-friendly sans scraping", 1624),
    ("signer son Agent Card A2A (clé publique)", 1625),
    ("Web Bot Auth : signer les requêtes agent web", 1625),
    ("vérifier l'identité d'un agent appelant (JWK)", 1625),
    ("AAIF fondation linux héberge MCP et A2A depuis 2026", 1626),
    ("réduire le lock-in : standards ouverts gouvernance AAIF", 1626),
    ("anthropic block openai co-fondateurs déc 2025", 1626),
    ("40% des projets agents annulés fin 2027 (Gartner)", 1627),
    ("POC agent 4 semaines avant scale", 1627),
    ("coût par tâche agent vs humain", 1627),
    ("mon agent achète pour moi (UCP mandat signé)", 1628),
    ("plafond de dépense par mandat agent", 1628),
    ("vérification cryptographique du mandat marchand", 1628),
    ("plusieurs agents qui collaborent (langgraph crewai)", 1629),
    ("graphe de tâches agents avec reprise sur erreur", 1629),
    ("mémoire partagée entre agents (1434)", 1629),
    ("mon agent réussit 60% des tâches en prod, pourquoi", 1630),
    ("rejouer les trajectoires réelles sur golden set", 1630),
    ("taux d'escalade HITL à surveiller", 1630),
    ("un seul point d'entrée MCP pour toute l'entreprise", 1631),
    ("audit log chaque appel tool (args user agent)", 1631),
    ("bloquer les tools shell/fichiers sensibles", 1631),
    ("j'ai 1M de tokens de contexte, quoi y mettre", 1632),
    ("lost in the middle : ne pas tout charger", 1632),
    ("retrieval : injecter seulement les k passages pertinents", 1632),
    ("héberger mon LLM en Europe (Mistral, OVH)", 1633),
    ("données IA qui restent en UE (Cloud Act évité)", 1633),
    ("Mistral vs GPT qualité coût 2027", 1633),
    ("agent juridique spécialisé vs ChatGPT généraliste", 1634),
    ("domaine médical : agent vertical réglementé (AI Act)", 1634),
    ("distillation d'un gros modèle en vertical (1473)", 1634),
    ("mon agent a coûté 3000€ en une nuit", 1635),
    ("budget tokens par agent alerte à 80%", 1635),
    ("kill switch auto si dépassement budget", 1635),
    ("file d'attente des approbations agents (UI/Slack)", 1636),
    ("routage par criticité : montant risque SLA 15 min", 1636),
    ("approbation en 1 clic avec contexte audit", 1636),
    ("mémoire graphe agent (Zep, Graphiti) vs vector store", 1637),
    ("entités + relations + épisodes dans un graphe temporel", 1637),
    ("l'agent se souvient des liens entre faits (1478)", 1637),
    ("snowflake cortex code génère mes pipelines", 1638),
    ("agent databricks débugue mon pipeline et propose un fix en sandbox", 1638),
    ("comparer old vs new pipeline (row counts, schéma) avant merge", 1638),
    ("industrialiser un agent : de l'idée à la prod surveillée", 1639),
    ("pipeline agent : POC → golden set → canary → monitoring", 1639),
    ("kill switch + rollback automatique agent (1635)", 1639),
    ("prompt injection indirecte via page web lue par l'agent (818)", 1640),
    ("l'agent exfiltre des données via un tool (fichier/email)", 1640),
    ("mémoire empoisonnée : l'agent apprend un faux fait (1637)", 1640),
    ("inventaire de ma cryptographie (CBOM) avant 2027", 1641),
    ("ML-KEM standard NIST 2024, migration 2027", 1641),
    ("ANSSI : PQC obligatoire dès 2027 en France", 1641),
    ("données volées aujourd'hui, déchiffrées en 2035 par quantique", 1642),
    ("quelles données protéger en PQC dès maintenant", 1642),
    ("réduire la rétention des données sensibles (RGPD)", 1642),
    ("déployer les passkeys pour tous les comptes sensibles en 2027", 1643),
    ("800M+ comptes passkeys en 2026, adoption entreprise", 1643),
    ("fallback mot de passe + MFA pendant la transition", 1643),
    ("identité par objet (certificat embarqué) pas de mot de passe par défaut", 1644),
    ("micro-segmentation réseau des objets (1203)", 1644),
    ("mises à jour OTA signées (SBOM 1457)", 1644),
    ("attaques supply chain +40% en 2026 (ENISA)", 1645),
    ("SLSA niveau 3 : build sur infra de confiance provenance signée", 1645),
    ("SBOM Syft à chaque build + cosign signature", 1645),
    ("92% des devs utilisent l'IA : le code IA est le blindspot n°1", 1646),
    ("OWASP 2026 : nouvelle catégorie supply chain renforcée (A03)", 1646),
    ("revue systématique du code généré par IA (1401)", 1646),
    ("télécharger un modèle Hugging Face : quels risques (backdoor, pickle)", 1647),
    ("vérifier la licence d'un modèle open source (1177)", 1647),
    ("scanner un repo de modèle (pickle, code au chargement) avant déploiement", 1647),
    ("cette vidéo est-elle un deepfake ? (détecteurs 2027)", 1648),
    ("voix clonée au téléphone : vérifier hors bande (rappeler le numéro connu)", 1648),
    ("vérifier les Content Credentials C2PA (1691) d'un média reçu", 1648),
    ("NIS2 : déclarer un incident sous 24 h, responsabilité dirigeant", 1649),
    ("DORA banque/assurance : tests de résilience + registres fournisseurs ICT", 1649),
    ("CMMC défense US : certification niveau 2", 1649),
    ("changer d'algorithme de chiffrement sans tout casser", 1650),
    ("ne pas appeler RSA directement (abstraction vault)", 1650),
    ("trust anchors upgradeables (changer la racine de confiance)", 1650),
    ("le SOC est noyé sous les alertes (fatigue)", 1651),
    ("playbook SOAR : isolaer le poste, bloquer l'IP automatiquement", 1651),
    ("shuffle SOAR open source 2027", 1651),
    ("compte dormant qui se réveille à 3h et télécharge 2 Go", 1652),
    ("exfiltration lente indétectable aux règles (quelques Mo/jour)", 1652),
    ("baseline de comportement par utilisateur (UEBA)", 1652),
    ("double extorsion : chiffrement + vol de données + publication", 1653),
    ("sauvegardes immuables Object Lock S3 (le ransomware les efface sinon)", 1653),
    ("décider de payer ou non (assurance, légal) playbook testé 1454", 1653),
    ("chaque conteneur a son identité crypto (SPIFFE SVID)", 1654),
    ("mTLS automatique entre services (SPIRE)", 1654),
    ("plus de clés API longue durée entre services (1446)", 1654),
    ("chiffrer mes requêtes DNS (DoH Cloudflare 1.1.1.1)", 1655),
    ("DNSSEC authentifier les réponses anti-spoofing", 1655),
    ("bloquer malware/phishing au niveau DNS (Quad9)", 1655),
    ("plus de mot de passe de BDD en dur : credential temporaire TTL (Vault)", 1656),
    ("IAM AWS temporaire par rôle (pas de clé longue durée)", 1656),
    ("certificats PKI courts générés à la demande", 1656),
    ("DMARC p=reject pour bloquer le spoofing de notre domaine", 1657),
    ("BIMI : notre logo certifié affiché dans Gmail/Outlook", 1657),
    ("MTA-STS : chiffrement TLS obligatoire en transit", 1657),
    ("SAST semgrep bloquant sur CVE high dans chaque PR", 1658),
    ("DAST zap sur le staging à chaque déploiement", 1658),
    ("SCA grype/OSV sur les dépendances + SBOM 1645", 1658),
    ("ouvrir un VDP (divulgation responsable) interne 2027", 1659),
    ("récompense par criticité CVSS, délai 90 j critique", 1659),
    ("HackerOne ou Bugcrowd pour un programme payant", 1659),
    ("requêter un Parquet sur S3 en SQL sans rien installer (DuckDB)", 1660),
    ("DuckDB embarqué dans mon app (analytics in-process)", 1660),
    ("joindre un CSV local et une table Postgres en une requête", 1660),
    ("DuckDB en cloud sans gérer d'infra (MotherDuck)", 1661),
    ("catalogues DuckDB partagés entre collègues", 1661),
    ("hybride : données locales + cloud MotherDuck", 1661),
    ("Iceberg v3 : suppressions efficaces (deletion vectors)", 1662),
    ("row lineage : traçabilité de chaque ligne (audit, RGPD)", 1662),
    ("format ouvert Iceberg vs Delta vs Hudi (1664)", 1662),
    ("Delta Lake vs Iceberg vs Hudi en 2027", 1663),
    ("Iceberg multi-moteurs (Spark Trino DuckDB Snowflake)", 1663),
    ("Delta Lake si écosystème Databricks dominant", 1663),
    ("pipeline d'ingestion en Python déclaratif (dlt)", 1664),
    ("REST API → DuckDB en 20 lignes (dlt)", 1664),
    ("incremental (last_value) + schéma qui évolue auto (1461)", 1664),
    ("pandas rame sur 5 Go, passer à Polars (Rust)", 1665),
    ("Polars lit Parquet/DuckDB nativement lazy evaluation", 1665),
    ("pandas si écosystème scikit-learn existant", 1665),
    ("stack data PME sans infra : dlt + DuckDB + dbt + Superset", 1666),
    ("Superset open source pour le BI (107)", 1666),
    ("dbt pour les transformations SQL versionnées (350)", 1666),
    ("Fivetran a racheté dbt en juin 2026", 1667),
    ("IBM a racheté Confluent pour 11 Md$ (streaming)", 1667),
    ("SAP a racheté Dremio (lakehouse ouvert) — éviter le lock-in (Iceberg 1663)", 1667),
    ("nos objets connectés vendus en UE doivent exposer leurs données (12 sept 2026)", 1668),
    ("API standardisée d'accès aux données générées par le produit", 1668),
    ("partage des données avec des tiers choisis par l'utilisateur (Data Act)", 1668),
    ("plus de frais de sortie cloud depuis janvier 2027 (Data Act)", 1669),
    ("egress gratuit : changer de cloud ne coûte plus rien", 1669),
    ("préavis de résiliation cloud max 2 mois (Data Act)", 1669),
    ("DORA : mon plan de sortie cloud doit être testé, pas juste écrit", 1670),
    ("sortir d'AWS : quoi exporter, où, comment restaurer", 1670),
    ("runbook de migration cloud avec RTO/RPO", 1670),
    ("stocker des images + leurs embeddings + le texte dans un lakehouse", 1671),
    ("LanceDB format Lance : vectoriel columnnaire natif 2027", 1671),
    ("recherche hybride image+texte (1477) sur mon catalogue produits", 1671),
    ("RisingWave : des materialized views PostgreSQL en streaming", 1672),
    ("Flink exactement-once stateful pour la détection de fraude", 1672),
    ("Bytewax dataflow Python pour le streaming simple", 1672),
    ("orchestrer en YAML sans coder (Kestra) vs Airflow Python", 1673),
    ("trigger webhook + schedule + fichier dans Kestra", 1673),
    ("UI visuelle des exécutions (Kestra) 2027", 1673),
    ("dashboards en YAML/SQL versionnés dans Git (Rill)", 1674),
    ("Rill sur DuckDB : BI as code sans serveur lourd", 1674),
    ("rill deploy en un clic (cloud ou self-host)", 1674),
    ("alerte auto si la table clients est vide à 6h du matin", 1675),
    ("Great Expectations : tests déclaratifs en CI (1592)", 1675),
    ("Monte Carlo : détection ML de l'anomalie de volume (1652? non)", 1675),
    ("3 définitions du CA selon l'équipe, semantic layer pour unifier", 1676),
    ("dbt Semantic Layer : métriques versionnées Git (350)", 1676),
    ("Cube : semantic layer open source avec API metrics", 1676),
    ("pousser mes segments clients du warehouse vers Salesforce automatiquement", 1677),
    ("plus d'export CSV manuel vers les ads (747)", 1677),
    ("Hightouch ou Census : sync warehouse → SaaS 2027", 1677),
    ("le producteur change le schéma sans prévenir, la CI bloque", 1678),
    ("contrat signé : schéma + qualité + SLA, versionné v1→v2", 1678),
    ("dépréciation avec date : 3 mois avant suppression de colonne", 1678),
    ("pgvector suffit sous 1M de vecteurs (déjà dans Postgres 1229)", 1679),
    ("Qdrant ou Milvus pour 100M vecteurs avec filtres metadata", 1679),
    ("LanceDB embarqué pour l'edge/offline (1671)", 1679),
    ("tracer mon pipeline dlt/dbt de bout en bout (OpenTelemetry)", 1680),
    ("pourquoi le pipeline de 3h a pris 2h aujourd'hui (traces OTel)", 1680),
    ("corréler une alerte data quality (1675) avec la trace du pipeline (1466)", 1680),
    ("quand s'applique l'AI Act en 2027 (post-Omnibus)", 1681),
    ("2 août 2026 : transparence art 50 + enforcement AI Office", 1681),
    ("2 déc 2027 haut risque annexe III, 2 août 2028 annexe I produits", 1681),
    ("nous fournissons un modèle GPAI : obligations 2027 (Code of Practice)", 1682),
    ("résumé public du dataset d'entraînement (droit d'auteur 2026)", 1682),
    ("modèle à risque systémique : évaluation + incident grave déclaré sous 24 h", 1682),
    ("sanction AI Act : 35 M€ ou 7 % du CA pour pratiques interdites", 1683),
    ("GPAI non conforme : 15 M€ ou 3 % du CA mondial", 1683),
    ("haut risque non conforme : 7,5 M€ ou 1,5 %", 1683),
    ("notre IA de tri de CV est haut risque Annexe III : deadline 2 déc 2027", 1684),
    ("obligations haut risque : gestion risques, logs, supervision humaine (329), cybersécurité", 1684),
    ("système en service avant août 2026 : transition jusqu'au 2 août 2027", 1684),
    ("CADA : quels niveaux de souveraineté cloud exigés en 2027 ?", 1685),
    ("marché public banque/énergie : évaluation risque souveraineté obligatoire avant contrat", 1685),
    ("Gaia-X niveaux 3-4 comme base du CADA (1686)", 1685),
    ("fournisseur Gaia-X niveau 3 = siège UE, droit UE, hors CLOUD Act", 1686),
    ("180 espaces de données sectoriels Gaia-X en 2026 (santé, auto, énergie)", 1686),
    ("certification via le Digital Clearing House (GXDCH) 2027", 1686),
    ("AWS European Sovereign Cloud lancé janv 2026 (7,8 Md€, Allemagne)", 1687),
    ("est-ce hors CLOUD Act ? (analyse juridique requise)", 1687),
    ("AWS souverain vs OVH/Gaia-X niveau 3 (1686) comparatif", 1687),
    ("tous les GPU viennent des US (NVIDIA), souveraineté calcul 2027", 1688),
    ("EU Cloud and AI Development Act 12 juin 2026 : tripler les datacenters UE", 1688),
    ("modèle UE (1633) + hébergement UE (1686) + calcul UE quand possible", 1688),
    ("certification EUCS du cloud en 2027 (niveaux basic/substantial/high)", 1689),
    ("EUCS vs Gaia-X vs CADA : quel label viser ?", 1689),
    ("cloud santé/finance UE : exiger EUCS high + Gaia-X N3 (1686)", 1689),
    ("indiquer à l'utilisateur qu'il parle à une IA (art 50, août 2026)", 1690),
    ("contenu généré (texte image vidéo) : marquage lisible + détectable", 1690),
    ("watermarking obligatoire pour les systèmes existants depuis déc 2026 (1691)", 1690),
    ("signer mes images générées (C2PA Content Credentials) 2027", 1691),
    ("vérifier si une image est générée par IA (C2PA verify)", 1691),
    ("AI Act art 50(2) : watermarking obligatoire, délai 2 déc 2026 systèmes existants", 1691),
    ("ma marque est-elle citée dans les réponses de Perplexity/ChatGPT ? (GEO)", 1692),
    ("taux de citation de mon site dans les moteurs IA (suivi hebdo)", 1692),
    ("GEO vs SEO 2027 : visibilité dans les réponses générées (161)", 1692),
    ("être cité par ChatGPT/Perplexity : structurer son contenu (AEO 2027)", 1693),
    ("réponse directe en 2-3 phrases en début de section (cité par les LLM)", 1693),
    ("FAQ schema.org + E-E-A-T + sources fraîches pour les moteurs IA", 1693),
    ("bento grid pour la landing 2027 (cartes modulaires)", 1694),
    ("glassmorphism sobre (flou léger, bordure fine, lisible)", 1694),
    ("dark mode auto + haut contraste (1496/1575) tendances 2027", 1694),
    ("animations au scroll natives (scroll-driven 1610)", 1695),
    ("micro-interactions hover focus 150-300 ms easing spring", 1695),
    ("view transitions entre pages (1615) + prefers-reduced-motion (1495)", 1695),
    ("les réponses du chatbot annoncées au lecteur d'écran (aria-live polite)", 1696),
    ("chatbot navigable au clavier seul (1571) sans piège", 1696),
    ("proposer un humain (251) + contraste 4,5:1 (1484) EAA 1599", 1696),
    ("signature qualifiée SEQ pour un contrat (eIDAS 2.0, 2027)", 1697),
    ("EUDI Wallet européen : l'identité numérique UE en 2027", 1697),
    ("Docaposte/Universign/Yousign : choisir un QTSP qualifié", 1697),
    ("quelles sont les 20 skills les plus utilisées ? (top popularité 1416)", 1698),
    ("taux d'exit 2 du routeur par semaine (misses 1497)", 1698),
    ("évolution du routage par version (versions)", 1698),
    ("5 outils d'observabilité data qui se contredisent, unifier (2027)", 1699),
    ("Monte Carlo ou Datafold : monitoring ML des pipelines", 1699),
    ("corrélation incident qualité (1675) ↔ trace OTel (1680) ↔ lineage (1466)", 1699),
    ("monter une plateforme interne développeurs (IDP) 2027", 1700),
    ("Backstage CNCF portail développeur 3400 orgs", 1700),
    ("golden paths : nouveau service en minutes pas en jours", 1700),
    ("golden path : nouveau service en 1 clic dans l'IDP", 1701),
    ("couvrir 80 % des cas en golden paths, le reste en dérogation documentée", 1701),
    ("réduire la charge cognitive des devs (Team Topologies)", 1701),
    ("déployer Backstage (CNCF) self-host : catalogue + Scaffolder + TechDocs", 1702),
    ("Backstage 3400 orgs 1200 plugins 89% pénétration IDP 2027", 1702),
    ("Port/Cortex/Humanitec : IDP managé sans équipe dédiée", 1702),
    ("je veux une Postgres managée : un claim YAML (Crossplane)", 1703),
    ("Crossplane vs Terraform : l'infra en CRD k8s (GitOps)", 1703),
    ("XRD/CompositeResource : composer les ressources (BDD + bucket + user)", 1703),
    ("déployer sur k8s via PR Git (Argo CD) pas de kubectl apply manuel", 1704),
    ("Argo CD vs Flux choisir 2027 (CNCF graduated)", 1704),
    ("rollback = git revert (l'état revient à la version Git)", 1704),
    ("bloquer un pod sans resource limits (Kyverno) en admission", 1705),
    ("Kyverno (YAML) vs OPA/Gatekeeper (Rego) choisir 2027", 1705),
    ("policy enforce (bloque) vs warn (log) + audit des violations existantes", 1705),
    ("lead time commit→prod sous 4 h en 2027 (DORA)", 1706),
    ("change failure rate sous 5 % mesuré", 1706),
    ("DORA jamais pour évaluer des individus (équipe uniquement)", 1706),
    ("équipe platform dédiée à l'IDP (Team Topologies)", 1707),
    ("stream-aligned : équipe produit autonome de bout en bout", 1707),
    ("charge cognitive : enquête interne sur la complexité perçue", 1707),
    ("demander un service en langage naturel dans l'IDP (92 % des CIO 2027)", 1708),
    ("l'IDP génère repo + CI + k8s depuis un golden path", 1708),
    ("l'IA génère, l'humain valide la PR (1401) avant merge", 1708),
    ("combien coûte une IDP en 2027 (3-6 ing/an self-host vs licence managée)", 1709),
    ("gains IDP : lead time 2-5j à 4h, déploiements x3-5, tickets -70%", 1709),
    ("présenter l'IDP au comité financier avec les métriques DORA 1706", 1709),
    ("Port ou Cortex managé : scorecards et catalogue auto en semaines", 1710),
    ("Humanitec : orchestrateur multi-cluster (Kratix promises)", 1710),
    ("Backstage sans équipe dédiée = portail vide, choisir managé", 1710),
    ("scorecard par service : bronze/argent/or (observabilité, sécurité, SLO)", 1711),
    ("Port/Cortex scorecards automatiques 2027", 1711),
    ("jamais de scorecard sur des personnes, uniquement des services", 1711),
    ("mesurer la productivité dev avec SPACE (5 dimensions, pas 1 métrique)", 1712),
    ("jamais le nombre de commits seul (anti-métrique)", 1712),
    ("DORA (1706) + enquêtes + flow = SPACE complet", 1712),
    ("nouveau dev : premier commit en prod le jour 1", 1713),
    ("environnement en 1 commande (devcontainer/docker compose 1109)", 1713),
    ("accès lecture seule d'abord, droits progressifs, buddy 234", 1713),
    ("l'environnement de dev marche en 1 clic (devcontainer)", 1714),
    (".devcontainer/devcontainer.json : image + extensions + postCreateCommand seed BDD", 1714),
    ("GitHub Codespaces : le devcontainer dans le cloud", 1714),
    ("la doc développeur vit dans le repo (docs/), rendue dans Backstage TechDocs", 1715),
    ("même PR pour code et doc (jamais de wiki qui pourrit)", 1715),
    ("recherche globale dans toute la doc interne (TechDocs)", 1715),
    ("une 'promise' Kratix = contrat d'infra (redis, env prod) réalisé sur chaque cluster", 1716),
    ("Kratix + state store S3 : la promise se propage sur 10 clusters", 1716),
    ("Kratix vs Crossplane : multi-cluster (Kratix) vs single (Crossplane 1703)", 1716),
    ("roadmap IDP par trimestre : v1 catalogue+golden path, v2 self-service, v3 IA", 1717),
    ("traiter l'IDP comme un produit interne (clients = devs, NPS)", 1717),
    ("métriques à chaque version : DORA 1706 + adoption % + NPS", 1717),
    ("accès au portail IDP via SSO + passkeys (1643)", 1718),
    ("service-to-service en mTLS (SPIFFE 1655), pas de clés longues", 1718),
    ("CI : OIDC (pas de clés cloud en dur) + runners éphémères", 1718),
    ("changelog mensuel de l'IDP (1578) + démo trimestrielle aux devs", 1719),
    ("canal #platform dédié + FAQ vivante (119)", 1719),
    ("roadmap publique (1717) + NPS interne 2x/an (1712)", 1719),
    ("exécuter du code dans le noyau Linux sans le recompiler (eBPF)", 1720),
    ("eBPF standard en 2026 : Meta Google Netflix Cloudflare l'utilisent", 1720),
    ("kernel 5.8 minimum 5.15+ idéal pour eBPF (uname -r)", 1720),
    ("remplacer kube-proxy/iptables par Cilium (eBPF) en 2027", 1721),
    ("Cilium NetworkPolicy L7 : filtrer sur méthode HTTP path header", 1721),
    ("Hubble : carte des flux réseau en temps réel + Cilium service mesh sans sidecar -50%", 1721),
    ("service map temps réel : quel pod parle à quel pod (Hubble)", 1722),
    ("filtrer les flux par méthode HTTP path ou topic Kafka (Hubble)", 1722),
    ("métriques de flux (bytes drops retransmits) exportées vers Grafana 1416", 1722),
    ("détecter un shell ouvert dans un conteneur (Falco, syscall execve)", 1723),
    ("lire /etc/shadow depuis un pod = alerte immédiate (Falco)", 1723),
    ("Falco eBPF (kernel 5.8+) plutôt que module kernel en prod", 1723),
    ("tracer une appli legacy sans toucher au code (Pixie/Beyla eBPF)", 1724),
    ("Beyla : OTel auto pour n'importe quel langage (Go Rust Java Python)", 1724),
    ("Pixie : requêtes SQL live + service map k8s sans SDK (1680)", 1724),
    ("bloquer (pas juste alerter) un binaire dans un conteneur (Tetragon)", 1725),
    ("TracingPolicy : interdire l'exec de /tmp/x, le write sur /etc, la connexion vers IP externe", 1725),
    ("Tetragon (Cilium) vs Falco (1723) : enforce vs detect", 1725),
    ("compter les syscalls par process en 1 ligne (bpftrace)", 1726),
    ("mesurer la latence des reads disque en live (bpftrace)", 1726),
    ("qui ouvre /etc/passwd en ce moment ? (bpftrace)", 1726),
    ("supprimer les sidecars Envoy (Istio) : Cilium Service Mesh eBPF (-50 % ressources)", 1727),
    ("mTLS automatique entre pods sans rien configurer (Cilium)", 1727),
    ("L7 routing (retries, circuit breaker) dans le noyau, pas dans un proxy", 1727),
    ("passer la certification Cilium CCAE en 2027 (eBPF, Cilium)", 1728),
    ("CKA/CKS (609) puis CCAE : la roadmap réseau k8s 2027", 1728),
    ("cilium bpf policy list / cilium service list : les commandes de l'exam", 1728),
    ("quels outils eBPF adopter en entreprise en 2027 (pas 15)", 1729),
    ("overhead eBPF inferieur a 5% de CPU mesuré avant adoption", 1729),
    ("Cilium enterprise (Isovalent/Cisco) vs open source : le TCO", 1729),
    ("load balancer kernel bypass (XDP eBPF) : Katran (Meta) 2027", 1730),
    ("maglev consistent hashing : même backend pour le même client", 1730),
    ("Katran vs ALB/NLB cloud : L4 pur ultra-perf vs managé L7", 1730),
    ("qui fait les I/O disque et avec quelle latence ? (eBPF)", 1731),
    ("latence des reads par device (nvme0 vs sda) en live (eBPF)", 1731),
    ("fichiers les plus lus sur le serveur (eBPF, pas iostat)", 1731),
    ("chaque pod a une identité réseau (pas une IP qui tourne) : Cilium eBPF", 1732),
    ("egress control : ce pod ne peut sortir que vers api.exemple.com (Cilium)", 1732),
    ("filtrer par nom de domaine DNS (pas juste IP) : Cilium DNS-aware", 1732),
    ("dropper les paquets d'une IP blacklistée dans le noyau (XDP)", 1733),
    ("DDoS volumineux : filtrer en XDP avant la stack réseau (eBPF)", 1733),
    ("WAF L7 (SQLi) reste applicatif 1451, eBPF fait le L3-L4", 1733),
    ("pourquoi eBPF plutôt qu'un module kernel en 2027 (pas de panic)", 1734),
    ("module kernel = un bug = kernel panic (risque)", 1734),
    ("eBPF par défaut, module seulement pour les drivers/subsystems", 1734),
    ("quel outil IA pour coder en 2027 (Cursor vs Claude Code vs Copilot vs Devin)", 1735),
    ("Copilot Business 19 $/siège + crédits depuis juin 2026", 1735),
    ("Claude Code CLI : SWE-bench 88,6 %, Opus 4.7 64,3 % SWE-bench Pro (avril 2026)", 1735),
    ("mon code part sur les serveurs de l'outil IA gratuit (fuite)", 1736),
    ("revue systématique des PR générées par IA (1401) + SAST (1658)", 1736),
    ("licence du code généré (1177) + pas de secrets dans les prompts (1440)", 1736),
    ("refacto de 50 fichiers avec Claude Code (plan mode) en CLI", 1737),
    ("/loop : tâches récurrentes programmées dans Claude Code (cron 2026)", 1737),
    ("Claude Code Analytics API : métriques d'usage par équipe (org)", 1737),
    ("assigner une issue GitHub à Devin : il ouvre une PR (agent autonome 2027)", 1738),
    ("Codex cloud (OpenAI) en parallèle sur plusieurs tâches", 1738),
    ("l'agent code en sandbox, je ne fais que la revue de PR (1401)", 1738),
    ("les outils IA font gagner +20-30 % sur l'écriture (mesuré 2026), on le prouve comment ?", 1739),
    ("Analytics API Claude Code + crédits Copilot (juin 2026) : usage réel par équipe", 1739),
    ("jamais de métrique individuelle de productivité IA (règle absolue)", 1739),
    ("édition multi-fichiers avec Cursor Composer (Cmd+K) 2027", 1740),
    ("chat avec toute la codebase indexée (Cursor)", 1740),
    ("agents cloud en arrière-plan (Cursor) + choix de modèle (Claude/GPT/Composer)", 1740),
    ("Copilot Business 19 $/siège + crédits d'usage depuis juin 2026", 1741),
    ("revue de PR automatique par Copilot (821) en entreprise", 1741),
    ("DPA Copilot : pas de rétention du code, opt-out, filtres code public protégé", 1741),
    ("agent de codage 100 % gratuit et open source (OpenCode) 2027", 1742),
    ("Jules (Google) : 15 tâches background gratuites par jour", 1742),
    ("OpenCode avec un modèle local (1633) : le code ne sort jamais", 1742),
    ("Aider : agent CLI open source qui commit tout seul (git intégré) 2027", 1743),
    ("Cline : l'agent dans VS Code (plan/act), open source", 1743),
    ("modèle local dans Aider/Cline (1633) : le code reste chez moi", 1743),
    ("trouver tous les appels à l'ancienne API auth dans 100k fichiers (Cody AST)", 1744),
    ("navigation par symboles cross-repo (définitions/références) 2027", 1744),
    ("Cody self-host (1633) pour du code interne qui ne sort pas", 1744),
    ("créer une app complète en 2 h avec Lovable (chat → déployé)", 1745),
    ("Bolt.new : éditer l'app générée en live dans le navigateur (StackBlitz)", 1745),
    ("v0 (Vercel) : composants shadcn + déploiement Vercel en 1 clic", 1745),
    ("générer les docstrings de tout un module (IA) + revue (1401)", 1746),
    ("README/ADR générés depuis le code et les PR (88) automatiquement", 1746),
    ("changelog auto depuis les commits conventionnels (68) 2027", 1746),
    ("générer les tests d'un module (IA) puis mutation testing pour vérifier qu'ils testent vraiment", 1747),
    ("couverture 80% sur le nouveau code (CI 1658 bloque sinon)", 1747),
    ("mocker la BDD et l'API externe (254) dans les tests générés", 1747),
    ("refactorer un god object de 3000 lignes avec Claude Code (plan mode 1737)", 1748),
    ("1 module de dette par semaine, tests auto (1747) avant/après, jamais tout d'un coup", 1748),
    ("détecter les duplications dans le code (IA) pour la dette (606)", 1748),
    ("qu'est-ce que l'IA peut coder en 2027 et qu'est-ce que je garde ?", 1749),
    ("l'IA fait le boilerplate, moi l'archi (88) et la sécurité (1646)", 1749),
    ("tout code IA = relu (1401) + testé (1747) + SAST (1658), responsabilité humaine", 1749),
    ("gen_ai.* attributs OTel standard 2027 (modèle, tokens, tool calls)", 1750),
    ("instrumenter un agent LangChain/CrewAI en OTel GenAI sans vendor lock-in", 1750),
    ("85 % des orgs utilisent la GenAI pour l'observabilité en 2026 (Elastic)", 1750),
    ("SLO d'une feature IA : TTFT sous 1 s, latence fin sous 10 s (streaming 1439)", 1751),
    ("budget d'erreur : SLO 99,5 % sur 28 j = 3,6 h de panne permise par mois", 1751),
    ("SLO qualité : score eval 1630 + hallucinations 1155 sous seuil + coût/requête 1491", 1751),
    ("ma facture Prometheus explose à cause des labels user_id (cardinalité)", 1752),
    ("traces : head sampling 10% + tail sampling 100% sur erreurs (2027)", 1752),
    ("stockage objet 0,50 $/Go (OpenObserve 1699) vs disque cher", 1752),
    ("golden signals : latence trafic erreurs saturation (Google SRE 2027)", 1753),
    ("RED par endpoint (Rate Errors Duration) vs USE par ressource (Utilization Saturation Errors)", 1753),
    ("commencer par golden signals avant les métriques custom", 1753),
    ("mes dashboards Grafana sont en code (Terraform/JSON), plus de clic-bouton", 1754),
    ("alertes Prometheus en YAML dans Git, déployées par CI (1413)", 1754),
    ("SLO (351) as code + revue de PR (1401) avant déploiement", 1754),
    ("trouver la cause racine d'un incident en moins de 60 s (AIOps 2027)", 1755),
    ("corrélation auto traces+métriques+logs+events k8s par ML (RCA)", 1755),
    ("l'IA propose la cause, l'humain valide et agit (HITL 1636)", 1755),
    ("les métriques réelles des utilisateurs (RUM web-vitals), pas que Lighthouse (labo)", 1756),
    ("INP réel p75 par page et par navigateur (Chrome vs Safari)", 1756),
    ("anonymiser le RUM (pas d'ID user 1440)", 1756),
    ("burn rate 14x sur 1h = alerte urgente (le budget brûle en 2 jours)", 1757),
    ("6x sur 6h = ticket, 1x sur 3j = info (Google SRE 2027)", 1757),
    ("moins d'alertes, plus pertinentes (anti fatigue 1417)", 1757),
    ("SEV1 client down : war room en 15 min, rôles clairs (IC 1161, comm, scribe)", 1758),
    ("post-mortem blameless (89) : jamais de faute individuelle, actions suivies", 1758),
    ("timeline de l'incident pour la communication client (235)", 1758),
    ("tuer un pod au hasard en prod et vérifier que ça tient (chaos 2027)", 1759),
    ("latence réseau 100 ms entre 2 services (expérience chaos)", 1759),
    ("blast radius 5 % + abort auto si le SLO brûle (1751/1757)", 1759),
    ("99,5 % de disponibilite = 3,6 h de downtime autorisees par mois", 1760),
    ("politique d'error budget : quoi faire quand le budget est grille", 1760),
    ("SLO interne 99,9 % vs SLO externe 99,5 % deux niveaux", 1760),
    ("alertes basees SLO burn rate au lieu de pics CPU", 1761),
    ("dedoublonnage groupement des alertes avant notification", 1761),
    ("routage alerte vers la bonne equipe avec escalade auto", 1761),
    ("tracer une requete de bout en bout front API BDD", 1762),
    ("propagation contexte W3C traceparent entre microservices", 1762),
    ("tail-based sampling : garder les traces lentes automatiquement", 1762),
    ("pourquoi mon Prometheus coute 10x plus cher ce mois-ci", 1763),
    ("label user_id sur une metrique = explosion du nombre de series", 1763),
    ("limiter la cardinalite : buckets bornes, jamais d'identifiant brut en label", 1763),
    ("runbook pour l'alerte disque plein : etapes commandes escalade", 1764),
    ("auto-remediation : redemarrer le pod tout seul sans reveil humain", 1764),
    ("action automatique sure vs action destructive qui demande validation", 1764),
    ("tracer chaque tool call de mon agent IA (MCP, fichiers, shell)", 1765),
    ("7 plateformes d'observabilité agent : self-host vs managé vs proxy", 1765),
    ("cout par requete agent : tokens entree sortie et appels d'outils", 1765),
    ("dashboard comite : SLO et error budget en haut, pas 40 courbes", 1766),
    ("un dashboard par audience : comex, equipe produit, support", 1766),
    ("drill-down du p99 global au span coupable en 3 clics", 1766),
    ("combien coute chaque appel LLM en tokens entree sortie et dollars", 1767),
    ("gen_ai.usage.input_tokens output_tokens attributs OTel sémantiques", 1767),
    ("cost attribution : quel parcours utilisateur coute le plus cher en IA", 1767),
    ("post-incident blameless : on ne blame pas la personne, on repare le systeme", 1768),
    ("5 pourquoi pour trouver la cause racine de l'incident", 1768),
    ("actions correctives avec responsable et echeance dans le backlog", 1768),
    ("simuler une panne de BDD primaire en prod controlee pour tester le failover", 1769),
    ("game day trimestriel avec l'equipe d'astreinte et les runbooks 1764", 1769),
    ("tabletop 1454 sans toucher au systeme vs game day live", 1769),
    ("Rust n'est plus experimental dans le noyau depuis decembre 2025", 1770),
    ("496 fichiers 120 019 SLOC de Rust dans le kernel 7.3 (24,6x vs 6.1)", 1770),
    ("premiers drivers Rust livres depuis 6.8 : Binder, NVMe, Asahi, Nova", 1770),
    ("garantir qu'un objet Rust ne bouge pas en memoire (Pin) dans le noyau", 1771),
    ("pourquoi les pointeurs intrusifs du noyau exigent pinned-init", 1771),
    ("API pinned-init disponible depuis le kernel 6.4", 1771),
    ("Binder IPC Android ecrit en Rust dans le noyau", 1772),
    ("preuve qu'un driver critique peut passer en Rust", 1772),
    ("coexistence C et Rust dans Binder, pas de remplacement total", 1772),
    ("driver NVMe porte en Rust preuve de faisabilite stockage", 1773),
    ("Rust sur le chemin I/O critique : pas d'allocation surprise", 1773),
    ("nouveau driver SSD en Rust en 2027 sur kernel 7.x", 1773),
    ("driver GPU Apple Silicon (M1/M2/M3) ecrit en Rust par Asahi", 1774),
    ("plus gros driver GPU Rust du noyau linux", 1774),
    ("nouveau driver graphique moderne en Rust en 2027", 1774),
    ("Nova : driver NVIDIA en Rust pour les GPU recents Blackwell", 1775),
    ("alternative open source au pilote proprietaire NVIDIA en Rust", 1775),
    ("anciens GPU NVIDIA restent sur nouveau (C), pas Nova", 1775),
    ("Rust dans le noyau : ajout de nouveaux drivers, jamais remplacement du C", 1776),
    ("Torvalds : Rust evite la stagnation du noyau (mainteneurs vieillissants)", 1776),
    ("pas de réécriture massive du code C existant en Rust", 1776),
    ("comment contribuer au Rust du noyau : tree rust-for-linux d'Ojeda", 1777),
    ("RFC sur rust-for-linux avant tout design nouveau", 1777),
    ("patchs petits testes KUnit + clippy + rustfmt obligatoires", 1777),
    ("70 % des CVE kernel sont des bugs memoire que Rust elimine par construction", 1778),
    ("use-after-free et buffer overflow impossibles en Rust safe", 1778),
    ("Rust safe n'elimine pas les bugs de logique metier", 1778),
    ("2027-2030 : nettoyer les API C 1-2 ans avant d'exposer plus de Rust", 1779),
    ("nouveaux drivers en Rust par defaut quand pertinent d'ici 2030", 1779),
    ("eviter la stagnation du noyau : attirer les jeunes contributeurs Rust", 1779),
    ("quelles nouveautes dans PostgreSQL 18 en 2027 ?", 1780),
    ("PG18 GA 25 sept 2025 PG19 RC1 15 oct 2026", 1780),
    ("monter en PG18 : AIO uuidv7 skip scan OAuth 2.0 temporal", 1780),
    ("io_uring dans PG18 : io_method=io_uring pour les scans", 1781),
    ("gros heap scan 3x plus rapide grace a l'AIO PG18", 1781),
    ("AIO utile quand le dataset depasse shared_buffers", 1781),
    ("uuidv7() au lieu de uuidv4() pour les nouvelles tables PG18", 1782),
    ("UUID v7 monotone = insertions en fin d'index, moins de page splits", 1782),
    ("uuidv7 = timestamp ms + aleatoire, localite d'index garantie", 1782),
    ("requete WHERE date=... utilise l'index (categorie, date) grace au skip scan PG18", 1783),
    ("plus besoin d'index separe sur la 2e colonne si la 1re a peu de valeurs", 1783),
    ("skip scan inutile si colonne a = milliers de valeurs distinctes", 1783),
    ("GENERATED ALWAYS AS (prix_ht * 1.2) VIRTUAL dans PG18", 1784),
    ("colonne calculee a la lecture, zero stockage disque", 1784),
    ("VIRTUAL pas indexable directement vs STORED stockee", 1784),
    ("historiser les prix avec une periode de validite WITHOUT OVERLAPS PG18", 1785),
    ("requete etat au 15 mars 2027 : WHERE periode couvre la date", 1785),
    ("PG18 interdit les chevauchements de periode sur la PK", 1785),
    ("se connecter a PG18 avec un JWT bearer token de Keycloak", 1786),
    ("pg_hba.conf : hostssl ... oauth issuer jwks audience", 1786),
    ("mapper le claim role du JWT vers le role PG (ex. app_readonly)", 1786),
    ("montee PG16 vers PG18 en quelques secondes avec pg_upgrade --swap", 1787),
    ("les stats pg_statistic sont conservees apres upgrade (plus d'ANALYZE massif)", 1787),
    ("--swap echange atomique des repertoires de donnees", 1787),
    ("SCRAM-SHA-256 par defaut PG18, md5 desactive", 1788),
    ("ssl_min_protocol_version = TLSv1.3 dans postgresql.conf", 1788),
    ("RLS row level security sur table multi-tenant + policy", 1788),
    ("plan de migration PG16 vers PG18 : check recette pgbench swap rollback", 1789),
    ("pg_upgrade --check avant toute montee de version", 1789),
    ("rollback : garder l'ancien cluster 1 semaine apres le swap 1787", 1789),
    ("inventaire de toute la crypto asymétrique : PKI TLS VPN SSH certificats HSM (CBOM)", 1790),
    ("ANSSI : plus de qualification sans PQC a partir de 2027, haut risque 2030", 1790),
    ("Harvest Now Decrypt Later : chiffrer aujourd'hui ne protege pas contre le quantique de demain", 1790),
    ("activer X25519MLKEM768 dans nginx/Apache/OpenSSL 3.5 pour le TLS 1.3 hybride", 1791),
    ("handshake hybride : X25519 + ML-KEM-768, protection dans les deux mondes", 1791),
    ("clés PQC volumineuses : handshake plus gros, acceptable en 2027", 1791),
    ("signer un binaire avec ML-DSA-65 (openssl genpkey -algorithm ML-DSA-65)", 1792),
    ("certificat X.509 hybride : double signature ECDSA + ML-DSA", 1792),
    ("FN-DSA pour des cles plus petites que ML-DSA, SLH-DSA en secours", 1792),
    ("cargo build --target wasm32-wasip2 pour compiler en WASI 0.3", 1793),
    ("Component Model WIT : composer des modules Rust+Go+Python en un binaire", 1793),
    ("WASI 1.0 fige l'ABI long terme fin 2026 debut 2027", 1793),
    ("wasmtime run --dir=. ./app.wasm : seul le dossier courant est accessible", 1794),
    ("deny-by-default : pas d'acces reseau/dossiers/env sans --tcplisten/--env explicites", 1794),
    ("cold start 1 ms Wasm vs 500 ms Docker pour les fonctions serverless/edge", 1794),
    ("audit RGESN de mon service : 79 criteres DINUM", 1795),
    ("loi REEN + RGESN : obligations sobriete numerique 2027", 1795),
    ("sobriete fonctionnelle : ne pas developper la feature inutile", 1795),
    ("Scaphandre mesure la conso electrique W/kWh des serveurs en temps reel", 1796),
    ("Boavizta evalue l'impact fabrication du materiel (78 % de l'empreinte terminaux)", 1796),
    ("CSRD scope 3 categorie 11 : empreinte du numerique dans le reporting 2027", 1796),
    ("Cloudflare Workers : cold start sous 5 ms sur 330+ PoP", 1797),
    ("D1 base SQLite a l'edge + R2 stockage sans frais d'egress", 1797),
    ("80 % de l'inference IA se fait a l'edge en 2027 (Workers AI)", 1797),
    ("framework SPACE pour mesurer la productivite dev (5 dimensions)", 1798),
    ("DORA : lead time, deploy frequency, MTTR, change failure rate", 1798),
    ("harness engineering : concevoir le harnais des agents de code en 2027", 1798),
    ("mon radar interne : anneaux Adopt/Trial/Assess/Hold comme ThoughtWorks", 1799),
    ("blip 'edge computing' passe de Trial a Adopt en 2027", 1799),
    ("revue semestrielle du radar avec les leads tech, decisions tracees", 1799),
    ("automatiser mon formulaire typeform vers mon crm", 1677),
    ("préparer ma présentation au comité", 879),
    ("qui décide : mettre en place les rôles clairs", 434),
    ("créer index composite explain analyze", 1419),
    ("mesurer ARPU rétention D7 p-value ship kill", 1540),
    ("compare les forfaits mobiles 2027", 219),
    ("mettre une gateway LLM devant mes appels IA (LiteLLM Bifrost Portkey Kong Cloudflare)", 1800),
    ("plafonner la conso tokens IA par équipe : budget spend limit clés virtuelles", 1800),
    ("cache sémantique gateway LLM : moins 20 à 40 % de dépenses sur requêtes répétées", 1800),
    ("quel est le meilleur VPN", 1304),
    ("migrer ingress-nginx vers la Gateway API (HTTPRoute Gateway)", 1801),
    ("ingress-nginx est retiré du projet Kubernetes : quoi mettre à la place", 1801),
    ("HTTPRoute routage avancé path host header TLS poids backends", 1801),
    ("allouer un GPU H100 à un pod via ResourceClaim DRA k8s", 1802),
    ("DRA vs extended resources nvidia.com/gpu : la différence", 1802),
    ("preferences ordonnees H100 sinon A100 avec fallback DRA", 1802),
    ("changer les requests CPU d'un pod sans le recréer (in-place resize)", 1803),
    ("VPA recommande des ressources mais le pod n'est pas resizé : activer InPlacePodVerticalScaling", 1803),
    ("stateful pod resizé à chaud : pas de perte de session", 1803),
    ("tous les pods d'un job ML démarrent ensemble ou aucun (gang scheduling PodGroup)", 1804),
    ("eviter le deadlock : des pods attendent des peers jamais schedulés", 1804),
    ("PodGroup scheduling.k8s.io v1beta1 k8s 1.37 beta", 1804),
    ("ma pod critique a été preempte par un batch : protéger avec PDB + workload-aware preemption", 1805),
    ("placer les pods selon la topologie (zone, noeud, GPU) : topology-aware scheduling", 1805),
    ("la preemption evite maintenant les pods gang scheduling", 1805),
    ("pourquoi mes pods sont lents sans OOM : lire le PSI (pressure stall) du nœud", 1806),
    ("cpu some avg10 supérieur à 5 % alerte saturation PSI", 1806),
    ("PSI mémoire IO aussi, pas que le CPU", 1806),
    ("monter une image OCI comme volume dans un pod (OCI VolumeSource)", 1807),
    ("distribuer une config signée via registre OCI + volume", 1807),
    ("SBOM ou modèle en artifact OCI monté read-only dans le pod", 1807),
    ("forcer un label team= sur chaque pod à la création (MutatingAdmissionPolicy CEL)", 1808),
    ("bloquer les images non signées à l'admission sans webhook", 1808),
    ("admission déclarative CEL dans l'apiserver vs webhook mutating externe", 1808),
    ("faire tourner un .wasm comme pod k8s (kwasm containerd shim)", 1809),
    ("SpinKube Spin operator pour workloads wasmCloud dans k8s", 1809),
    ("pod wasm : image 2 Mo cold start 1 ms isolation forte vs conteneur", 1809),
    ("provisionner automatiquement le bon nœud pour un pod pending (Karpenter vs cluster-autoscaler)", 1810),
    ("consolidation automatique des nœuds sous-utilisés pour réduire la facture", 1810),
    ("NodePool GPU spot vs on-demand avec Karpenter", 1810),
    ("opentofu ou terraform en 2027 : lequel choisir (licence MPL vs BSL IBM)", 1811),
    ("terraform est passé BSL puis IBM : le fork opentofu vaut le coup", 1811),
    ("mêmes providers mêmes HCL : opentofu 1.13 registre 3900 providers", 1811),
    ("chiffrer le terraform state (OpenTofu state encryption KMS) : le state contient des secrets", 1812),
    ("state S3 non chiffré = risque : activer state encryption OpenTofu 1.7+", 1812),
    ("clés externes KMS pour le state : aws:kms, gcp:kms, azurerm:keyvault, age, fichier", 1812),
    ("garder le mot de passe BDD hors du terraform state (ephemeral resource)", 1813),
    ("ephemeral aws_secretsmanager_secret_version : la valeur n'est jamais dans le state", 1813),
    ("write-only attributes OpenTofu 1.11 : pas de fuite dans les logs", 1813),
    ("empecher le destroy d'une ressource prod via une variable (prevent_destroy dynamique OpenTofu 1.12)", 1814),
    ("lifecycle enabled pour ressource zero-or-one (OpenTofu 1.11)", 1814),
    ("prevent_destroy hardcodé vs variable par workspace (prod vs dev)", 1814),
    ("instancier un provider AWS par région avec for_each (OpenTofu provider for_each)", 1815),
    ("backend S3 dynamique selon l'env : early variable evaluation OpenTofu 1.8", 1815),
    ("tofu plan -exclude=module.dev pour ne toucher qu'un module", 1815),
    ("registre OCI privé pour providers/modules (air-gapped) OpenTofu 1.10", 1815),
    ("publier mes modules terraform internes dans un registre OCI privé (Harbor/ECR)", 1816),
    ("air-gapped : plus de registre public, miroir OCI interne OpenTofu 1.10", 1816),
    ("signer les modules avec cosign avant publication (supply chain IaC)", 1816),
    ("orchestrer 5 modules IaC sur 3 environnements avec Terraform Stacks (HCP)", 1817),
    ("dépendance entre composants : output VPC = input cluster dans un Stack", 1817),
    ("Stacks HCP uniquement : pas d'équivalent OpenTofu natif", 1817),
    ("lister toutes les S3 buckets du compte et importer celles hors state (terraform query)", 1818),
    ("détecter le drift manuel : ressources créées en console non dans le state", 1818),
    ("terraform list vs state : voir ce qui existe vraiment chez le cloud", 1818),
    ("migrer un repo terraform vers opentofu : le state est compatible (tofu init)", 1819),
    ("terraform plan vs tofu plan : vérifier 0 diff après migration", 1819),
    ("ne pas activer state encryption pendant la migration (1812 après)", 1819),
    ("détecter le drift : plan -detailed-exitcode en CI hebdo + terraform query 1818", 1820),
    ("OPA Conftest pour valider les plans terraform (open source) vs Sentinel (HCP only)", 1820),
    ("bloquer en CI un plan avec une S3 publique ou sans tag cost-center", 1820),
    ("générer un SBOM de mon image en CI (syft cyclonedx-json ou trivy)", 1821),
    ("CycloneDX vs SPDX : lequel pour le scan de vulnérabilités (CycloneDX) ou les licences (SPDX)", 1821),
    ("CISA 2026 Minimum Elements : hashes + licences + contexte de génération obligatoires", 1821),
    ("signer une image sans clé privée longue durée (cosign keyless OIDC Fulcio Rekor)", 1822),
    ("cosign verify --certificate-identity-regexp pour vérifier l'issuer du workflow", 1822),
    ("air-gapped : cosign verify --trusted-root root.json local", 1822),
    ("attestation de provenance SLSA L3 avec slsa-github-generator (keyless GitHub)", 1823),
    ("in-toto : subject digest + predicate (repo, commit, builder) signé", 1823),
    ("cosign verify-attestation --type slsa-provenance pour vérifier le build", 1823),
    ("bloquer les pods avec image non signée à l'admission (Kyverno verifyImages cosign)", 1824),
    ("Sigstore Policy Controller vs Kyverno : lequel pour vérifier les signatures", 1824),
    ("failureAction Audit d'abord, Block ensuite (ne pas casser la prod)", 1824),
    ("attester des tâches SSDF dans le SBOM (CDXA bom-1.7 claims signés)", 1825),
    ("BOM-Link pour lier une attestation au SBOM lui-même", 1825),
    ("bundle Sigstore DSSE autour du CDXA + vérification air-gapped trusted-root", 1825),
    ("412 CVE dans mon image : lesquelles bloquer ? (KEV CISA + VEX non applicable)", 1826),
    ("VEX statement 'not_affected' avec justification pour une CVE", 1826),
    ("re-scanner le SBOM attesté toutes les nuits (CVE post-build)", 1826),
    ("bloquer un paquet malveillant avant le merge (Socket/Phylum comportement)", 1827),
    ("OpenSSF Scorecard : santé du projet (signed releases, SAST, branch protection)", 1827),
    ("GUAC : graphe SBOM + SLSA + VEX pour savoir si on est affecté", 1827),
    ("remplacer debian:200Mo par une image distroless chainguard (2 Mo, signée)", 1828),
    ("pas de shell dans l'image prod : chainguard/static ou wolfi", 1828),
    ("image signée Sigstore + SBOM inclus : chainguard, vérifié à l'admission 1824", 1828),
    ("plus de clé AWS statique dans les secrets GitHub : OIDC workload identity (token 1h)", 1829),
    ("Tekton Chains signe automatiquement les images du build (provenance SLSA)", 1829),
    ("incident Trivy CVE-2026-33634 : pinner les actions GitHub par SHA, pas par tag", 1829),
    ("le CRA européen exige un SBOM pour notre produit : quoi livrer (CycloneDX + VEX + VDP)", 1830),
    ("questionnaire client sécurité : fournir SBOM + attestations SSDF + processus VDP", 1830),
    ("CRA en vigueur : calendrier et amendes si pas de SBOM/VDP", 1830),
    ("rédiger un data contract : schéma + sémantique + SLA entre producteur et consommateur", 1831),
    ("enforcement du contrat au pipeline (dbt tests, GX, Soda) : violation = blocage", 1831),
    ("contrat lisible par les agents IA (MCP dbt) pour éviter les hallucinations de sens", 1831),
    ("instrumenter mes pipelines avec OpenLineage (events start/complete, inputs/outputs)", 1832),
    ("OpenLineage vs format propriétaire : standard ouvert Linux Foundation", 1832),
    ("activer OpenLineage dans dbt/Airflow/Dagster/Spark en 2027", 1832),
    ("déployer Marquez (backend OpenLineage) : UI + API pour le lineage", 1833),
    ("lineage au niveau colonne (pas que table) : qui consomme cette colonne ?", 1833),
    ("incident revenue -11 % : analyse d'impact avec Marquez en minutes", 1833),
    ("contrat de schéma dbt (schema.yml columns data_type) : violation = fail à l'exécution", 1834),
    ("tests dbt : unique not_null relationships accepted_values + tests custom singular métier", 1834),
    ("dbt Fusion (moteur Rust) : parse 10x plus rapide sur les gros projets", 1834),
    ("SLA fraîcheur : alerte si la table a plus de 1 h de retard", 1835),
    ("volume : alerte si nb lignes inférieur à 80 % de la médiane hebdo", 1835),
    ("distribution : alerte si une valeur sort des bornes historiques", 1835),
    ("DataHub vs OpenMetadata vs Marquez : lequel pour le catalogage data", 1836),
    ("Amundsen archivé sept 2026 : migrer vers quoi", 1836),
    ("lineage technique (Marquez/OpenLineage) vs gouvernance métier (OpenMetadata/DataHub)", 1836),
    ("passer au data mesh : domaines métier propriétaires de leurs data products", 1837),
    ("data product : contrat 1831 + SLA 1835 + discoverable (catalog 1836) + self-serve", 1837),
    ("ne pas faire de data mesh sans plateforme self-serve (risque de chaos)", 1837),
    ("une seule définition de 'revenu net' partout (semantic layer dbt/LookML/Cube)", 1838),
    ("les agents IA consomment les métriques via MCP (1765) : définition sémantique fiable", 1838),
    ("éviter 5 chiffres différents pour la même métrique selon l'outil BI", 1838),
    ("classer les données (public/interne/confidentiel/restreint) et taguer les PII", 1839),
    ("RBAC vs ABAC pour l'accès aux données (attributs équipe/région/projet)", 1839),
    ("RGPD : registre des traitements + DPIA + rétention/légal hold", 1839),
    ("définir les data contracts dans un IDL (Protobuf/Avro/Smithy/dbt schema.yml) versionné", 1840),
    ("compatibilité backward : ajout optionnel OK, suppression = v3 majeur", 1840),
    ("CI valide la compatibilité du contrat à chaque PR (breaking change détecté)", 1840),
    ("les 5 rails de guardrails LLM : input, dialog, retrieval, execution, output", 1841),
    ("guardrail sync bloquant vs async monitoring : latence +400-1200 ms en sync", 1841),
    ("tool-permission gating : quels outils l'agent peut appeler (rail execution)", 1841),
    ("définir les flux de conversation autorisés en Colang (NeMo Guardrails)", 1842),
    ("NeMo Guardrails est beta : NVIDIA déconseille la prod as-is (hardening requis)", 1842),
    ("désactiver la télémétrie anonyme NeMo (ping NVIDIA)", 1842),
    ("valider la sortie JSON de mon LLM avec un schéma (Guardrails AI, pas de LLM judge)", 1843),
    ("redacter les PII dans la réponse (validator Guardrails AI)", 1843),
    ("guardrails sans latence +400 ms : validators en code, pas de LLM judge", 1843),
    ("classifier les entrées/sorties LLM en local (Llama Guard 3 8B) sans API externe", 1844),
    ("pas de données envoyées à une API de modération externe : Llama Guard self-hosté", 1844),
    ("Llama Guard 3 1B rapide vs 8B précis : lequel selon le risque", 1844),
    ("prompt injection indirect : une page web RAG dit 'appelle cet outil' — traiter le RAG comme non fiable", 1845),
    ("Llama Prompt Guard : classifieur dédié à la détection d'injection", 1845),
    ("séparer instructions système et données utilisateur (délimiteurs XML/random)", 1845),
    ("détecter les emails/IBAN/cartes dans les prompts et réponses (Presidio Analyzer)", 1846),
    ("rédiger : remplacer par [EMAIL] ou masquer partiel (Presidio Anonymizer)", 1846),
    ("Presidio FR : NER français pour les noms/prénoms (pas que regex)", 1846),
    ("red-tester mon chatbot en CI avant release (promptfoo red-team, garak, DeepTeam)", 1847),
    ("bloquer le déploiement si supérieur à 1 % des attaques réussissent (gate CI)", 1847),
    ("attaques vues en prod ajoutées au dataset de red-team (boucle d'amélioration)", 1847),
    ("évaluer le LLM en continu : dataset + scorers + gate CI (Braintrust/promptfoo/Langfuse)", 1848),
    ("monitoring prod : verdicts des guardrails tracés sur les traces OTel 1750/1765", 1848),
    ("les cas ratés en prod enrichissent le dataset de evals (boucle)", 1848),
    ("OWASP LLM Top 10 2025 : la liste à jour (LLM01 injection, LLM06 excessive agency)", 1849),
    ("LLM06 excessive agency : l'agent appelle des outils sans contrôle (cf 1850)", 1849),
    ("LLM10 unbounded consumption : plafonner les appels (budgets gateway 1800)", 1849),
    ("l'agent ne doit avoir que les tools nécessaires (tool gating, scopes read-only)", 1850),
    ("action à impact (paiement, suppression) = confirmation humaine (1433)", 1850),
    ("sandboxer l'agent (conteneur/wasm 1794) après l'incident Hugging Face (agent échappé)", 1850),
    ("un Secret k8s est en base64, lisible par tous : activer etcd encryption at rest (KMS)", 1851),
    ("RBAC : restreindre get/list secrets (pas pour tous les pods)", 1851),
    ("audit log des accès aux secrets (apiserver audit policy)", 1851),
    ("déployer Vault en HA (Raft) avec unseal auto KMS cloud", 1852),
    ("authentifier un pod k8s à Vault via son JWT (auth kubernetes)", 1852),
    ("audit log Vault : qui a lu quel secret et quand", 1852),
    ("plus de mot de passe BDD partagé : Vault crée un user temporaire TTL 24 h (dynamic secrets)", 1853),
    ("lease Vault : le cred expire tout seul, re-lu à la volée", 1853),
    ("moteur database Vault : Postgres/MySQL/MongoDB avec rôles SQL", 1853),
    ("synchroniser Vault dans des Secrets k8s avec ESO (ExternalSecret refreshInterval 1h)", 1854),
    ("ClusterSecretStore pour partager le backend Vault entre namespaces", 1854),
    ("15+ backends ESO : Vault, AWS SM, GCP SM, Azure KV, Doppler, Infisical", 1854),
    ("changer un secret sans redémarrer manuellement : ESO refreshInterval + Reloader rolling restart", 1855),
    ("secret en volume : le kubelet propage en ~1 min sans restart de pod", 1855),
    ("Vault dynamic secrets TTL : la rotation est automatique (1853)", 1855),
    ("commiter un secret chiffré dans Git (kubeseal — SealedSecret) pour ArgoCD/Flux", 1856),
    ("backup de la clé privée Sealed Secrets : sans elle, tout est perdu", 1856),
    ("re-encrypt après rotation de clé : kubeseal --re-encrypt", 1856),
    ("chiffrer un .env avant de le committer (sops + age ou KMS)", 1857),
    ("sops en pre-commit (1403) : bloque un commit avec secret en clair", 1857),
    ("déchiffrer en CI : sops -d avec la clé KMS (OIDC 1860)", 1857),
    ("injecter un secret Vault dans le pod sans objet Secret k8s (agent injector, annotation)", 1858),
    ("Vault CSI Provider : volume CSI avec le secret, 0 trace dans etcd", 1858),
    ("le sidecar Vault réécrit le fichier à la rotation (l'app re-lit)", 1858),
    ("gitleaks en pre-commit (1403) : bloque un commit avec une clé AWS", 1859),
    ("trufflehog en CI : scan de tout l'historique git (pas que le dernier commit)", 1859),
    ("fuite détectée : révoquer le secret immédiatement (1855) + purger l'historique (BFG)", 1859),
    ("plus de AWS_SECRET_ACCESS_KEY dans les secrets GitHub : OIDC (id-token write + rôle IAM trust)", 1860),
    ("token cloud temporaire 1 h au lieu d'une clé statique : OIDC workload identity", 1860),
    ("incident Trivy (tags compromis, fuite Runner.Worker) : OIDC + pin SHA (1829)", 1860),
    ("lire la facture AWS et Azure avec la même requête SQL (FOCUS, 65 colonnes standardisées)", 1861),
    ("EffectiveCost pour l'analyse vs BilledCost pour la réconciliation facture", 1861),
    ("exports FOCUS natifs : AWS Data Exports, Azure Cost Management, GCP BigQuery", 1861),
    ("combien coûte le namespace prod ce mois-ci ? (OpenCost/Kubecost allocation)", 1862),
    ("mes requests sont à 30 % du réel : rightsizing VPA 1803 + PSI 1806", 1862),
    ("coût réseau egress entre namespaces (Cilium Hubble 1722)", 1862),
    ("Airflow 3.2 vs Dagster vs Prefect en 2027 : lequel choisir", 1863),
    ("Prefect a racheté Dagster Labs (13 juillet) : les deux continuent, risque roadmap", 1863),
    ("Temporal pour les workflows long-running des agents IA (durable execution)", 1863),
    ("@asset Dagster : matérialiser une table avec ses dépendances en arguments", 1864),
    ("tester un asset localement (pytest) avant de le déployer", 1864),
    ("Dagster UI : voir quels assets sont stale (pas matérialisés à temps)", 1864),
    ("@flow @task Prefect : le pipeline en pur Python (pas de DAG YAML)", 1865),
    ("Prefect Cloud vs self-host (worker + serveur) : coût à l'usage ~50 $/M actions", 1865),
    ("Prefect rachète Dagster Labs : évaluer le risque avant nouveau projet", 1865),
    ("capturer les INSERT/UPDATE/DELETE d'une BDD en temps réel (CDC log-based, pas de polling)", 1866),
    ("Debezium sur Kafka vs Airbyte (embarque Debezium) vs Fivetran managé", 1866),
    ("le polling updated_at rate les DELETE : passer au CDC", 1866),
    ("ingérer Salesforce/Postgres/S3 dans le warehouse : Airbyte (300+ connecteurs)", 1867),
    ("Airbyte self-host vs Cloud : OSS ou managé", 1867),
    ("Airbyte + Dagster : les syncs Airbyte deviennent des assets (1864)", 1867),
    ("mon agent IA tourne 6 h et crash à 5 h — tout perdu : Temporal (durable execution)", 1868),
    ("Temporal vs Airflow/Dagster : quand l'utiliser (long-running, crash-safe)", 1868),
    ("heartbeat Temporal : détecter qu'un worker est mort et reprendre ailleurs", 1868),
    ("déclencher le pipeline quand le fichier arrive en S3 (sensor/event), pas toutes les heures en cron", 1869),
    ("Airflow 3.2 asset events : un DAG se déclenche quand l'asset amont est prêt", 1869),
    ("moins de runs vides : event-driven vs cron (coût + fraîcheur)", 1869),
    ("showback : montrer à chaque équipe sa conso cloud (rapport mensuel)", 1870),
    ("chargeback : refacturer réellement en interne (budgets consommés)", 1870),
    ("30 % de coûts non alloués faute de tags : policy tags obligatoires (1820)", 1870),
    ("certificat TLS auto Let's Encrypt sur HTTPRoute (cert-manager + ACME)", 1871),
    ("wildcard *.example.com : DNS-01 (Cloudflare/Route53) pas HTTP-01", 1871),
    ("certificat Vault PKI interne (cert-manager issuer vault)", 1871),
    ("créer automatiquement l'enregistrement DNS quand un Ingress est créé (external-dns)", 1872),
    ("annotation external-dns.alpha.kubernetes.io/hostname: api.example.com", 1872),
    ("policy upsert-only + dry-run d'abord (ne pas toucher aux DNS existants)", 1872),
    ("scaler les consumers Kafka selon le lag (KEDA), pas selon le CPU", 1873),
    ("scale to zero quand la file est vide (KEDA) : économie de nœuds", 1873),
    ("ScheduledJob KEDA : cron au niveau k8s (scale 0 la nuit)", 1873),
    ("créer un cluster k8s sur AWS avec CAPI (CAPA) comme une ressource k8s (Cluster + MachineDeployment)", 1874),
    ("upgrade déclaratif du control plane k8s (CAPI : changer la version = changer le CR)", 1874),
    ("CAPI vs EKS/GKE managé : quand CAPI (multi-cloud, on-prem, contrôle total)", 1874),
    ("OS immutable pour k8s : Talos (API-only, pas de shell) vs Flatcar vs Bottlerocket", 1875),
    ("mise à jour atomique A/B de Talos : rollback en 1 commande si boot échoue", 1875),
    ("Talos + CAPI 1874 : provisionner un cluster Talos déclaratif", 1875),
    ("Linkerd (léger, simple) vs Istio (complet, complexe) : lequel en 2027", 1876),
    ("Cilium service mesh sans sidecar (eBPF 1721/1727) si Cilium déjà déployé", 1876),
    ("mTLS automatique entre services + traffic splitting pour canary 1418", 1876),
    ("canary auto 10 % — pause — analyse Prometheus (erreur 5xx, p99) — abort ou promote (Argo Rollouts)", 1877),
    ("AnalysisTemplate : requête PromQL sur les métriques du canary avant de passer à 100 %", 1877),
    ("blue-green avec Argo Rollouts (switch instantané du trafic)", 1877),
    ("plusieurs NodePool Karpenter : général + GPU (DRA 1802) + spot, avec weight (priorité)", 1878),
    ("consolidation WhenUnderutilized : vider et supprimer les nœuds sous-utilisés (économie)", 1878),
    ("drift Karpenter : nœud non conforme (mauvaise image) — remplacé automatiquement", 1878),
    ("ApplicationSet : déployer la même app sur 10 clusters/envs depuis un template (Argo CD)", 1879),
    ("sync waves : la DB se déploie avant l'API (wave 0 puis wave 1)", 1879),
    ("générateur clusters (CAPI 1874) : une Application par cluster automatiquement", 1879),
    ("backuper tout le cluster k8s (ressources + volumes) avec Velero vers S3", 1880),
    ("restore dans un autre cluster/région : tester régulièrement (game day 1769)", 1880),
    ("snapshot etcd régulier (etcdctl snapshot save) + vérification (snapshot status)", 1880),
    ("kill switch : désactiver une feature en prod en 1 clic (LaunchDarkly)", 1881),
    ("rollout graduel 1 % — 100 % avec auto-rollback si erreur (guarded rollout)", 1881),
    ("Unleash AGPL / GrowthBook MIT / Flagsmith BSD : flags OSS self-host", 1881),
    ("une API de flags unique (OpenFeature) + provider LaunchDarkly/Unleash : changer de vendor sans toucher au code", 1882),
    ("hooks OpenFeature (before/after/error) pour logger chaque évaluation de flag", 1882),
    ("OpenFeature CNCF Incubating : standard 2027 des feature flags", 1882),
    ("quand utiliser un flag vs un canary vs du blue-green ? (déploiement vs release)", 1883),
    ("Flagger (Flux) v1.45 : canary/blue-green auto sur k8s sans Argo Rollouts", 1883),
    ("blue-green : switch instantané du trafic + rollback instantané (2 stacks)", 1883),
    ("Renovate : PRs de deps groupées par écosystème, automerge des patchs après CI verte", 1884),
    ("Dependabot (GitHub) : config .github/dependabot.yml, plus simple que Renovate", 1884),
    ("semaine lock avant release : gel des mises à jour de deps (renovate schedule)", 1884),
    ("bloquer la PR si le nouveau code a des vulnérabilités ou couverture inférieur à 80 % (quality gate Sonar)", 1885),
    ("dette technique Sonar : temps de remboursement en jours, à réduire chaque sprint", 1885),
    ("SAST Sonar + scan deps 1827 + gitleaks 1859 : les 3 gates en CI 1413", 1885),
    ("définir l'API en OpenAPI 3.2 d'abord, générer le code ensuite (spec-first)", 1886),
    ("AsyncAPI pour les événements Kafka (1866) : contrat des messages aussi", 1886),
    ("breaking change d'API détecté en CI par diff de la spec OpenAPI (1840)", 1886),
    ("Nx affected : ne builder/tester que les projets impactés par le commit (CI -70 %)", 1887),
    ("Turborepo (Vercel) : pipeline turbo.json + remote cache, plus simple que Nx", 1887),
    ("Bazel : remote execution + cache hermetic pour les très gros repos (Google-scale)", 1887),
    ("nos 4 métriques DORA vs le benchmark elite 2026 : où on se situe", 1888),
    ("lead time inférieur à 1 jour, deploy on-demand, MTTR inférieur à 1 h, change failure rate inférieur à 15 % (elite)", 1888),
    ("DORA + SPACE 1798 : mesurer l'équipe sans surveillance individuelle", 1888),
    ("TechDocs (Backstage 1702) : les README du repo publiés en site doc interne auto", 1889),
    ("un ADR par décision d'architecture (1746) dans docs/adr/, revu en PR (1401)", 1889),
    ("runbooks incidents (1764) à côté du code, publiés dans la doc interne", 1889),
    ("Copilot en revue de PR (1741) : résumé auto + détection de bugs/risques, puis humain sur la logique métier", 1890),
    ("checklist de revue 1401 : sécurité 1826, perfs, cas limites, tests", 1890),
    ("SLA revue inférieur à 4 h ouvrées : file de PR triée par ancienneté", 1890),
    ("CrowdStrike vs SentinelOne vs Defender en 2027 : lequel selon le threat model", 1891),
    ("SentinelOne : rollback ransomware en 1 clic (Complete tier)", 1891),
    ("Defender P2 ~5,20 $/user/mo inclus E5 : suffisant pour 75 % des orgs (Microsoft stack)", 1891),
    ("une attaque BEC corrélée en 1 incident (mail + IdP + endpoint) au lieu de 3 alertes séparées", 1892),
    ("Defender XDR si stack Microsoft 1891 : corrélation native M365/Entra/Cloud", 1892),
    ("rétention 1-3 ans des données XDR pour la conformité (1839)", 1892),
    ("pas de SOC 24/7 interne : souscrire un MDR avec réponse (pas juste alerte)", 1893),
    ("MDR Elite : threat hunting proactif + réponse autonome, vs Essentials (alertes+playbooks)", 1893),
    ("coût MDR vs analyste interne 60-90 k€/an : comparer avant de recruter", 1893),
    ("déployer MISP pour partager/recevoir des IOCs (communautés de confiance, TLP)", 1894),
    ("STIX/TAXII : importer des flux TI commerciaux dans le SIEM 1453 automatiquement", 1894),
    ("un IOC (hash malveillant) bloque auto sur tous les endpoints (EDR 1891) via le SIEM", 1894),
    ("activer DNSSEC chez le registrar + valider côté resolver (anti-spoofing DNS)", 1895),
    ("DoH/DoT : chiffrer les requêtes DNS (confidentialité) — navigateur auto ou unbound local", 1895),
    ("DNS filtering : bloquer malware/phishing au niveau DNS (Quad9 ou liste interne)", 1895),
    ("déployer les passkeys (FIDO2) pour tous les admins (phishing-resistant)", 1896),
    ("remplacer le MFA SMS (SIM swap) par des passkeys ou TOTP app", 1896),
    ("Entra ID / Okta / Google : passkeys en beta puis GA 2027", 1896),
    ("retainer forensics pré-contracté (disponible 24/7, tarifs d'avance) vs appeler en urgence", 1897),
    ("playbook ransomware : étapes (isolation 1891, restauration 1880, comms, CNIL 72 h)", 1897),
    ("tabletop 1769 + exercice live annuel : le plan IR testé, pas juste écrit", 1897),
    ("OWASP ZAP en CI contre le staging : détecte les vraies vulns (XSS, injection) que le SAST rate", 1898),
    ("gate : vulnérabilité critical trouvée en DAST — déploiement bloqué (CI 1413)", 1898),
    ("IAST (Contrast) pour réduire les faux positifs du DAST", 1898),
    ("1 security champion par équipe produit (10 % de son temps, formé) : relais RSSI au quotidien", 1899),
    ("revue de menaces STRIDE en conception avec le champion, pas après coup", 1899),
    ("métrique : % de features avec threat model fait avant le dev", 1899),
    ("VDP : security.txt (RFC 9116) + security@ + réponse sous 5 j, pas de poursuites (bonne foi)", 1900),
    ("bug bounty HackerOne/Bugcrowd/YesWeHack : périmètre, récompenses selon SSVC 1826", 1900),
    ("CRA 2027 : VDP obligatoire pour les produits numériques (1830)", 1900),
    ("fine-tuner un modèle sur notre ton de marque", 691),
    ("cette étude observationnelle prouve-t-elle quelque chose ?", 1387),
    ("désactiver proprement IA message utilisateurs", 1881),
    ("journal quêtes compteur 3/5 temps réel", 1280),
    ("signalement 3 = mute 24h 10 = ban 7j", 1548),
    ("explique la différence entre SAS et SARL", 668),
    ("notre ton de marque", 691),

    ("micro-entreprise BTP", 1901),
    ("démarrer artisan bâtiment", 1901),
    ("immatriculation RNE artisan", 1901),
    ("obligations légales artisan", 1902),
    ("checklist conformité BTP", 1902),
    ("amende RNE 15 000", 1902),
    ("rédiger un devis travaux", 1903),
    ("mentions obligatoires devis BTP", 1903),
    ("acompte devis max 30", 1903),
    ("mentions obligatoires facture 2026", 1904),
    ("Factur-X obligatoire", 1904),
    ("amende facture 75 000", 1904),
    ("micro entreprise ou SARL artisan", 1905),
    ("quel statut pour artisan BTP", 1905),
    ("EURL ou SASU travaux", 1905),
    ("devenir RGE artisan", 1906),
    ("label qualibat coût 2026", 1906),
    ("MaPrimeRénov condition RGE", 1906),
    ("assurance décennale obligatoire artisan", 1907),
    ("prix RC Pro BTP 2026", 1907),
    ("décennale loi Spinetta", 1907),
    ("équipements protection individuelle obligatoires chantier", 1908),
    ("harnais EN 361 longe EN 355", 1908),
    ("durée de vie harnais 10 ans", 1908),
    ("rédiger un PPSPS", 1909),
    ("coordination SPS obligatoire quand", 1909),
    ("DUERP artisan solo obligatoire", 1909),
    ("norme électrique NF C 15-100 2026", 1910),
    ("attestation Consuel obligatoire", 1910),
    ("volumes salle de bain électricité", 1910),
    ("normes plomberie DTU évacuation", 1911),
    ("disconnecteur BA obligatoire", 1911),
    ("test étanchéité plomberie", 1911),
    ("faire un métré chantier", 1912),
    ("calculer prix main d'œuvre BTP", 1912),
    ("déboursé sec définition", 1912),
    ("tri déchets chantier obligatoire 7 flux", 1913),
    ("bordereau BSD déchets dangereux", 1913),
    ("déchetterie chantier benne", 1913),
    ("louer ou acheter nacelle", 1914),
    ("prix location échafaudage 2026", 1914),
    ("VGP engins levage vérification", 1914),
    ("lire plan architecte échelle", 1915),
    ("cotes chaînage plan bâtiment", 1915),
    ("symboles plan construction DCE", 1915),
    ("préparer un chantier travaux étapes", 1916),
    ("DT-DICT obligatoire avant travaux", 1916),
    ("implantation piquetage chantier", 1916),
    ("procès-verbal réception travaux réserves", 1917),
    ("DOE dossier ouvrages exécutés contenu", 1917),
    ("garantie décennale date début", 1917),
    ("litige travaux artisan client que faire", 1918),
    ("mise en demeure LRAR chantier", 1918),
    ("déclarer sinistre décennale 5 jours", 1918),
    ("reprendre entreprise artisanale BTP", 1919),
    ("valorisation fonds de commerce artisan", 1919),
    ("garantie actif passif cession", 1919),
    ("préparer vente entreprise artisanale", 1920),
    ("valoriser PME travaux 2026", 1920),
    ("trouver repreneur artisan", 1920),
    ("aménager atelier bois garage", 1921),
    ("aspirateur poussière bois classe M", 1921),
    ("électricité atelier menuiserie 380V", 1921),
    ("quels outils électroportatifs acheter menuiserie", 1922),
    ("scie circulaire plongeante rail", 1922),
    ("défonceuse à quoi ça sert", 1922),
    ("quelle essence bois choisir meuble", 1923),
    ("classe emploi bois extérieur classe 3 4", 1923),
    ("prix m3 chêne pin douglas 2026", 1923),
    ("comment dégauchir une planche", 1924),
    ("ordre dégauchisseuse raboteuse", 1924),
    ("scier bois sens du fil éclats", 1924),
    ("tenon mortaise comment faire", 1925),
    ("queue d'aronde à la défonceuse", 1925),
    ("lamello biscuit assemblage", 1925),
    ("quelle colle bois choisir PVA PU", 1926),
    ("temps séchage colle à bois", 1926),
    ("serrage collage serre-joints combien", 1926),
    ("huile ou vernis plan de travail bois", 1927),
    ("lasurer bois extérieur fréquence", 1927),
    ("céruser un meuble comment", 1927),
    ("restaurer meuble ancien étapes", 1928),
    ("décaper meuble bois sans l'abîmer", 1928),
    ("traitement trous de vers bois", 1928),
    ("fixer étagère mur placo cheville molly", 1929),
    ("fabriquer étagère bois plan étapes", 1929),
    ("charge max étagère équerres", 1929),
    ("fabriquer un meuble en bois soi-même plan", 1930),
    ("assembler caisson meuble vis colle", 1930),
    ("ajuster porte meuble jeu 2 mm", 1930),
    ("poser charnière meuble réglage 3 vis", 1931),
    ("coulisse tiroir soft close installer", 1931),
    ("loquet magnétique meuble pose", 1931),
    ("poussières bois cancérogènes atelier aspiration", 1932),
    ("EPI atelier menuiserie masque lunettes", 1932),
    ("règles sécurité scie circulaire défonceuse", 1932),
    ("trusquin à quoi ça sert traçage", 1933),
    ("vérifier équerre meuble diagonales", 1933),
    ("cotes fonctionnelles assemblage jeu", 1933),
    ("scie japonaise dozuki utilisation", 1934),
    ("couper un tenon à la main", 1934),
    ("ciseau à bois maillet biseau", 1934),
    ("quel grain ponçage bois ordre 80 120 240", 1935),
    ("poncer dans le sens du fil pourquoi", 1935),
    ("épongeage bois avant finition", 1935),
    ("teinture bois à l'eau ou alcool différence", 1936),
    ("céruser bois chêne effet blanc", 1936),
    ("vieillir le bois thé vinaigre", 1936),
    ("poser parquet stratifié soi-même étapes", 1937),
    ("jeu dilatation parquet 10 mm pourquoi", 1937),
    ("sous-couche parquet pare-vapeur obligatoire", 1937),
    ("plan de travail bois massif poser soi-même", 1938),
    ("huile dure alimentaire plan cuisine", 1938),
    ("jonction plan de travail angle 45", 1938),
    ("porte qui frotte comment régler paumelles", 1939),
    ("changer joint fenêtre bois EPDM", 1939),
    ("restaurer vieille fenêtre bois étapes", 1939),
    ("lasure bois terrasse fréquence réapplication", 1940),
    ("classe emploi 3 ou 4 différence", 1940),
    ("bois autoclave classe 4 c'est quoi", 1940),
    ("débuter tournage sur bois tour à bois", 1941),
    ("gouge à ébaucher à quoi ça sert", 1941),
    ("vitesse tour bois selon diamètre", 1941),
    ("cintrer bois à la vapeur moule", 1942),
    ("lamellé collé cintré comment faire", 1942),
    ("rebond élastique cintrage bois", 1942),
    ("poser placage bois soi-même fer à repasser", 1943),
    ("placage de chant thermocollant poser", 1943),
    ("marqueterie débutant essences couleurs", 1943),
    ("boucher trou dans bois pâte à bois teinte", 1944),
    ("flipot réparer fissure panneau", 1944),
    ("nœud sauté bois remplacer goujon", 1944),
    ("calculer prix meuble sur mesure artisan", 1945),
    ("taux horaire menuisier 2026", 1945),
    ("marge à prendre devis menuiserie", 1945),
    ("lire plan meuble avant fabrication", 1946),
    ("nomenclature meuble c'est quoi", 1946),
    ("dessiner plan meuble SketchUp gratuit", 1946),
    ("défonceuse rainure languette réglage profondeur", 1947),
    ("fraise à feuillure à quoi ça sert", 1947),
    ("sens avance défonceuse sécurité", 1947),
    ("insert fileté bois poser démontable", 1948),
    ("écrou à frapper bois assembler meuble démontable", 1948),
    ("assembler lit démontable ferrures", 1948),
    ("vernis au pistolet HVLP réglage pression buse", 1949),
    ("diluer vernis polyuréthane combien", 1949),
    ("masque vapeurs organiques vernis A2P3", 1949),
    ("affûter ciseau à bois pierre à eau grain", 1950),
    ("angle affûtage ciseau menuisier 25 degrés", 1950),
    ("test fil lame ciseau coupe cheveu", 1950),
    ("comment tricoter pour débutant", 1951),
    ("première paire aiguilles laine débutant", 1951),
    ("écharpe tricot première projet", 1951),
    ("aiguilles droites ou circulaires différence", 1952),
    ("lire étiquette pelote laine DK worsted", 1952),
    ("laine mérinos ou acrylique débutant", 1952),
    ("faire un échantillon tricot gauge", 1953),
    ("mesurer mailles 10 cm après blocage", 1953),
    ("changer taille aiguilles tricot tension", 1953),
    ("point mousse tricot comment faire", 1954),
    ("différence jersey et point mousse", 1954),
    ("côtes 1/1 tricot bordure élastique", 1954),
    ("tricoter bonnet en rond sans couture", 1955),
    ("magic loop tricot aiguilles circulaires", 1955),
    ("diminutions bonnet tricot régulièrement", 1955),
    ("abréviations patron tricot français M1L", 1956),
    ("choisir taille patron tricot selon mensurations", 1956),
    ("patron raglan tricot explications", 1956),
    ("premier projet tricot facile bonnet", 1957),
    ("tricoter snood tube rond débutant", 1957),
    ("chaussettes tricot talon comment faire", 1957),
    ("laver un pull en laine machine comment", 1958),
    ("bloquer tricot épingler dimensions sécher", 1958),
    ("laine superwash différence lavage", 1958),
    ("enlever bouloches pull laine rasoir", 1959),
    ("repriser un trou dans un pull technique", 1959),
    ("maille tombée pull remonter aiguille", 1959),
    ("monter des mailles tricot méthode longue queue", 1960),
    ("rabattre mailles souplement tricot bonnet", 1960),
    ("cast on cast off tricot français", 1960),
    ("quelle machine à coudre acheter débutant 2026", 1961),
    ("Brother FS40 ou Singer 3232 avis", 1961),
    ("régler tension fil machine à coudre", 1961),
    ("enfiler machine à coudre étape par étape", 1962),
    ("canette mal enfilée symptômes fil dessous", 1962),
    ("tension 4 ou 5 machine coudre défaut", 1962),
    ("point zigzag à quoi ça sert couture", 1963),
    ("boutonnière machine 4 temps régler taille", 1963),
    ("point d'arrêt début couture machine", 1963),
    ("surfiler un bord au zigzag serré comment", 1964),
    ("ourlet invisible machine à coudre point", 1964),
    ("pré-laver tissu avant couture rétrécissement", 1964),
    ("poser zip invisible robe pied spécial", 1965),
    ("fermeture éclair qui bloque coincée réparer", 1965),
    ("zip séparable veste coudre étapes", 1965),
    ("endroit contre endroit coudre pourquoi", 1966),
    ("valeur de couture 1 cm repère plaque machine", 1966),
    ("cranter courbe couture retourner à plat", 1966),
    ("pré-laver tissu coton rétrécissement pourcentage", 1967),
    ("droit-fil tissu couture c'est quoi", 1967),
    ("entoilage thermocollant quand l'utiliser", 1967),
    ("lire patron couture Fait Main symboles", 1968),
    ("quelle taille choisir patron 34 36 38 mensurations", 1968),
    ("métrage tissu patron selon laize 140 cm", 1968),
    ("premier projet couture tote bag tutoriel", 1969),
    ("coussin zip coudre débutant étapes", 1969),
    ("tablier couture patron gratuit simple", 1969),
    ("coudre un bouton 4 trous à la main tige", 1970),
    ("point arrière couture main quand l'utiliser", 1970),
    ("ourlet invisible à la main point espacé 1 cm", 1970),
    ("feutrage à l'aiguille comment débuter", 1971),
    ("aiguilles 36 38 40 à feutrer différence", 1971),
    ("laine cardée roving mérinos acheter", 1971),
    ("laine cardée ou peignée feutrage différence", 1972),
    ("roving mérinos acheter 50g prix", 1972),
    ("laine corriedale feutrage boule cœur", 1972),
    ("faire une boule laine feutrée serrée", 1973),
    ("cône feutrage chapeau gabarit mousse", 1973),
    ("feutrage rétrécit combien pourcentage", 1973),
    ("figurine kawaii feutrage patron proportions", 1974),
    ("yeux figurine feutrée sécurité enfant", 1974),
    ("tête grosse corps petit style kawaii", 1974),
    ("feutrer un pull à l'eau chaude savon", 1975),
    ("chapeau feutré à l'eau 40 degrés méthode", 1975),
    ("laine superwash ne feutre pas pourquoi", 1975),
    ("faire une broche en feutre aiguille attache", 1976),
    ("boucles d'oreilles feutrine découper coudre", 1976),
    ("barrette feutre pince croco DIY", 1976),
    ("faire des chaussons en feutre soi-même forme pied", 1977),
    ("sac en laine feutrée à l'eau anses cuir", 1977),
    ("semelle chausson feutre coudre cuir", 1977),
    ("boucher trou pull laine avec feutre patch", 1978),
    ("réparer trou mite laine feutré aiguille", 1978),
    ("feutrer un patch réparation laine 40G", 1978),
    ("aiguille à feutrer dans le doigt que faire", 1979),
    ("doigtier cuir feutrage acheter", 1979),
    ("ranger aiguilles à feutrer étui sécurité", 1979),
    ("kit débutant feutrage aiguille acheter 20 euros", 1980),
    ("où acheter laine cardée roving mérinos", 1980),
    ("budget premier mois loisirs créatifs feutrage", 1980),
    ("apprendre macramé nœuds débutant tutoriel", 1981),
    ("porte-plante macramé patron gratuit corde 5mm", 1981),
    ("nœud carré spirale macramé différence", 1981),
    ("cuire Fimo à quelle température combien de temps", 1982),
    ("Fimo Soft ou Professional différence", 1982),
    ("effet marbré pâte polymère technique", 1982),
    ("perles Fimo rouler cuire trou avant cuisson", 1983),
    ("montage boucles d'oreilles pâte polymère crochets", 1983),
    ("effet marbré ou canne Fimo bijou technique", 1983),
    ("cire de soja ou paraffine bougie DIY différence", 1984),
    ("taux huile essentielle dans bougie 5 8 pourcent", 1984),
    ("mèche coton centrer socle métal bougie", 1984),
    ("recette savon saponification à froid débutant", 1985),
    ("soude caustique NaOH savon sécurité EPI gants", 1985),
    ("cure savon 4 6 semaines pH 9 10 test", 1985),
    ("scrapbooking débuter quel matériel acheter", 1986),
    ("washi tape à quoi ça sert scrapbooking", 1986),
    ("colle sans acide photos pourquoi", 1986),
    ("Cricut Explore 3 ou Maker 3 différence prix", 1987),
    ("vinyle adhésif poser mur lettrage étapes", 1987),
    ("tapis de coupe Cricut nettoyer colle résidu", 1987),
    ("quelle peinture acrylique acheter débutant couleurs de base", 1988),
    ("toile cartonnée ou chassis entoilé différence", 1988),
    ("médium acrylique à quoi ça sert glacis", 1988),
    ("papier aquarelle 300g bloc collé ou feuille à coller", 1989),
    ("godets ou tubes aquarelle que choisir débutant", 1989),
    ("lavis dégradé aquarelle technique mouillé sur mouillé", 1989),
    ("points de broderie de base apprendre point arrière tige", 1990),
    ("tambour broderie 15 cm quel tissu tendre", 1990),
    ("fil mouliné DMC combien de brins séparer", 1990),
    ("quel appareil pyrogravure acheter débutant 50 euros", 1991),
    ("pyrogravure sur quel bois tilleul peuplier", 1991),
    ("transférer un dessin sur bois papier carbone", 1991),
    ("kintsugi kit acheter débutant laque urushi", 1992),
    ("réparer bol cassé doré wabi-sabi", 1992),
    ("laque urushi allergie précaution kintsugi", 1992),
    ("yarn bombing légal autorisation mairie", 1993),
    ("tricoter autour d'un poteau yarn bombing tutoriel", 1993),
    ("quel fil acrylique pour yarn bombing extérieur UV", 1993),
    ("relooker meuble sans décaper chalk paint", 1994),
    ("customiser un jean peinture tissu patches", 1994),
    ("transformer vieux t-shirt en tote bag couture", 1994),
    ("art journal débuter quelle carnet papier 300g", 1995),
    ("mixed media page exemple collage pochoir gesso", 1995),
    ("idée page art journal semaine thème", 1995),
    ("bracelet perles rocailles fil élastique nœud chirurgien", 1996),
    ("technique wrapped loop tige œil pince ronde", 1996),
    ("fermoir collier installer pince plate tutoriel", 1996),
    ("sériraphie kit débutant 50 euros tee-shirt imprimer", 1997),
    ("risographie c'est quoi effet grain machine Riso", 1997),
    ("encre sérigraphie à l'eau papier carton tirage manuel", 1997),
    ("peindre sur un t-shirt avec peinture tissu fixer fer", 1998),
    ("patch thermocollant poser fer 150 degrés combien temps", 1998),
    ("broder directement sur un jean troué", 1998),
    ("vendre sur Etsy frais commission 2026 auto-entrepreneur", 1999),
    ("marché de créateurs autorisation mairie assurance RC Pro", 1999),
    ("calculer prix vente création artisanale matière temps marge x2", 1999),
    ("organiser coin loisirs créatifs petit appartement rangement", 2000),
    ("combien de temps par semaine pour progresser hobby", 2000),
    ("budget mensuel loisirs créatifs 30 50 euros", 2000),
    ("exercer mon droit de rétractation", 850),  # rescue golden vague 22
    ("classement papier hebdomadaire vendredi", 862),  # rescue golden vague 22
    ("lag compensation rewind raycast état ancien", 1545),  # rescue golden vague 22
    ("comparer assurances habitation", 965),  # rescue golden vague 22

    ("session hebdomadaire classement papier 15 min vendredi", 862),  # rescue golden vague 22
    ("compare les assurances habitation 2027", 965),  # rescue golden vague 22 (965 = assurance habitation, meilleur gagnant que 1360)

]

# ---------------------------------------------------------------------------
# Tests de non-régression (édition : un couple (demande, N attendu) par ligne ;
# None attendu = aucune candidate, exit 2). Rejouer `routage.py test` après
# toute modification du routeur, des synonymes ou du catalogue.
# ---------------------------------------------------------------------------
TESTS_ROUTAGE = [
    ("montre-moi la skill 447", 447),
    ("j'ai du mal à dormir", 483),
    ("je procrastine trop", 26),
    ("mon code bug", 20),
    ("organiser un atelier", 208),
    ("impôts", 297),
    ("traduire un texte", 7),
    ("résumer un document", 5),
    ("procrastinnation", 26),   # faute de frappe -> passe floue
    ("organisr un atelier", 208),  # faute de frappe -> passe floue
    ("zzz qwertyu", None),     # exit 2 attendu
    ("durcir l'authentification de mon site web", 501),
    ("mon wordpress a été piraté", 503),
    ("plan de correctifs cve", 505),
    ("simuler une campagne de phishing", 509),
    # anti-faux-positifs (durcissement mode OU / flou, 2026-11)
    ("budget personnel et dépenses", 43),   # et non 33 (persona/personnel)
    ("composer de la musique", 155),        # rescue synonyme mono-mot
    ("divorce et garde d'enfant", 590),    # couvert depuis la vague 8 (skill 590)
    ("signaler une arnaque", 530),         # couvert depuis la vague 8 (skill 530)
    ("architecture d'API REST", 526),      # couvert depuis la vague 8 (skill 526)
    ("gestion du stress et anxiété", 511), # couvert depuis la vague 8 (skill 511)
    ("lancer un podcast", 157),            # rescue synonyme
    ("assurance habitation", 480),         # rescue synonyme
    ("text-to-speech et voix", 154),       # synonyme speech remappé (was 75)
    ("arrêter de grignoter", 488),         # rescue synonyme
    ("examen et révisions", 41),           # rescue synonyme
    # vague 8 (skills 511-600)
    ("apprendre la guitare", 518),
    ("écrire des regex", 523),
    ("humaniser ce texte", 538),
    ("mon chat vomit", 556),
    ("mon locataire ne paie plus", 554),
    ("organiser la fête de famille des 70 ans de ma mère", 565),
    ("est-ce une arnaque", 530),

    # --- Vague 9 (skills 601-616) ---
    ("revue de ma session avant commit", 601),
    ("fais une SWOT de notre position", 613),
    ("notre cluster kubernetes plante", 609),
    ("sprint de dette technique", 606),
    ("contrôle pré-déploiement", 614),
    ("notre positionnement dans les réponses de ChatGPT", 612),
    ("adapte tes réponses pour un lecteur TDAH", 616),

    # --- Vague 10 (skills 617-699) ---
    ("je fais un burn-out au travail", 617),
    ("on veut répartir la charge mentale à la maison", 618),
    ("j'ai le syndrome de l'imposteur", 619),
    ("je bloque à cause du perfectionnisme", 620),
    ("je fais des cauchemars toutes les nuits", 621),
    ("mon fils est allergique aux arachides", 622),
    ("j'oublie de prendre mes médicaments", 623),
    ("mes gencives saignent", 624),
    ("je dois renouveler mes lunettes", 625),
    ("je suis enceinte de 12 semaines", 626),
    ("comment organiser l'allaitement et la diversification", 627),
    ("on cherche une nounou pour bébé", 628),
    ("mon ado en CM1 et les écrans", 629),
    ("maintien à domicile de ma mère de 84 ans", 630),
    ("dossier MDPH pour mon fils autiste", 631),
    ("préparer mon entretien annuel", 632),
    ("je veux demander une promotion", 633),
    ("convocation à un entretien préalable", 634),
    ("je veux changer de poste en interne", 635),
    ("harcèlement moral par mon manager", 636),
    ("discrimination salariale homme femme", 637),
    ("mon entreprise est en difficulté de trésorerie", 638),
    ("déclaration de TVA en CA3", 639),
    ("lire mon bilan comptable de fin d'année", 640),
    ("expliquer ma fiche de paie", 641),
    ("on passe en hybride 2 jours de TT", 642),
    ("trop de réunions inutiles au bureau", 643),
    ("donner un feedback à un collègue", 644),
    ("prépare mon pitch elevator", 645),
    ("refaire notre landing page de conversion", 646),
    ("répondre à un avis négatif sur google", 647),
    ("exercer mon droit de rétractation", 648),
    ("médiation avec mon voisin", 649),
    ("dossier de surendettement à la banque de france", 650),
    ("la succession de mon père", 651),
    ("garde alternée et pension alimentaire", 652),
    ("déménagement et ouverture de compteur edf", 653),
    ("la chasse d'eau fuit", 654),
    ("vidange et contrôle technique de ma voiture", 655),
    ("préparer notre voyage au japon", 656),
    ("organiser un dîner pour 8 samedi", 657),
    ("trouver un cadeau pour les 30 ans de ma sœur", 658),
    ("je veux courir un 10 km dans 6 mois", 659),
    ("adopter un chat adulte", 660),
    ("mon potager de 20 m2 cet été", 661),
    ("menus végétariens pour toute la famille", 662),
    ("téléconsultation pour renouveler mon ordonnance", 663),
    ("renouveler ma carte d'identité en ligne", 664),
    ("sécuriser mes mots de passe", 665),
    ("mon pc est infecté par un ransomware", 666),
    ("publier la photo de classe de mon fils", 667),
    ("choisir entre auto-entrepreneur et sasu", 668),
    ("automatiser mon formulaire typeform vers mon crm", 669),
    ("j'ai des notes partout, un seul système svp", 670),
    ("apprendre l'espagnol en 8 mois", 671),
    ("passer le permis à 17 ans", 672),
    ("mon fils révise mal pour le brevet", 673),
    ("je veux me reconvertir dans l'environnement", 674),
    ("négocier une offre d'achat immobilier", 675),
    ("appel de fonds de ma copropriété", 677),
    ("isoler ma maison classée F au dpe", 678),
    ("faire le tri dans mes abonnements", 679),
    ("changer de banque sans perdre mes prélèvements", 680),
    ("livret A ou PEA pour mon épargne", 681),
    ("à quel âge partir à la retraite à taux plein", 682),
    ("quelle assurance habitation en colocation", 683),
    ("on s'expatrie 2 ans à singapour", 684),
    ("ce sms de la douane est-il une arnaque", 685),
    ("notre site doit être conforme wcag", 686),
    ("réduire l'empreinte carbone de notre site", 687),
    ("organiser ma veille technologique ia", 688),
    ("quel llm choisir pour notre chatbot", 689),
    ("monter un rag sur nos procédures internes", 690),
    ("fine-tuner un modèle sur notre ton de marque", 691),
    ("sécuriser notre agent contre l'injection de prompt", 692),
    ("mettre en place des evals sur notre agent", 693),
    ("notre facture api llm a triplé", 694),
    ("un client demande l'effacement de ses données rgpd", 695),
    ("notre livreur maltraite un colis, c'est viral", 696),
    ("préparer mon entretien d'embauche de jeudi", 697),
    ("onboarding — exemple concret d'utilisation", 698),
    ("on déménage vivre 2 ans à lisbonne", 699),

    # --- Vague 11 (skills 700-799) ---
    ("vérifie les chiffres de ce texte généré par une ia", 700),
    ("donne-moi mon briefing du matin", 701),
    ("prépare ma fiche pour le call de 14 h", 702),
    ("rédige un brouillon de réponse à ce mail client", 703),
    ("mon agenda est un bazar, optimise ma semaine", 704),
    ("rédige le compte rendu de cette réunion avec les action items", 705),
    ("mon prestataire ne répond plus, relance-le", 706),
    ("rédige mon statut d'équipe pour demain", 707),
    ("fais une recherche approfondie sur ce marché avec sources", 708),
    ("mets en place une veille sur mes concurrents", 709),
    ("prépare mon rapport hebdo pour mon manager", 710),
    ("explique-moi le protocole a2a entre agents", 711),
    ("comment structurer le harness de mon agent", 712),
    ("instrumente les appels llm de mon agent", 713),
    ("structure la mémoire persistante de mon agent", 714),
    ("trouve et installe une skill pour connecter notion", 715),
    ("audite cette skill avant de l'installer", 716),
    ("crée une vidéo de démo produit avec remotion", 717),
    ("génère un modèle 3d imprimable from texte", 718),
    ("donne-moi la version courte caveman de cette réponse", 719),
    ("challenge mon plan de migration avant que je code", 720),
    ("transforme mes 200 notes en graphe de connaissances", 721),
    ("quelles solutions ia souveraines hébergées en ue", 722),
    ("quels playbooks confier à des agents de sécurité", 723),
    ("applique les règles de vérifiabilité au code ia", 724),
    ("réponds-moi uniquement depuis mes pdf avec citations", 725),
    ("que dit-on de ma marque sur reddit cette semaine", 726),
    ("construis mon calendrier éditorial du mois", 727),
    ("écris le texte d'un carrousel de 8 slides", 728),
    ("script un reels de 30 secondes avec hook", 729),
    ("packshot ia — exemple concret d'utilisation", 730),
    ("rédige tous les textes de notre page d'inscription", 731),
    ("par quoi commencer notre design system", 732),
    ("comment mener ce test a/b proprement", 733),
    ("prépare le guide de nos interviews utilisateurs", 734),
    ("onboarding produit SaaS : 70 % des inscrits partent après l'accueil", 735),
    ("donne-moi la check-list accessibilité de mes contenus", 736),
    ("transforme ce prompt brouillon en rcorcf", 737),
    ("explique-moi étape par étape ce raisonnement", 738),
    ("définis mes 3 personas clients", 739),
    ("cible-moi 20 profils linkedin et écris la séquence", 740),
    ("prépare le script de ma démo de 15 min", 741),
    ("le prospect dit que c'est trop cher, quelles réponses", 742),
    ("comment closer pour obtenir un engagement daté", 743),
    ("quand proposer le forfait pro à ce client", 744),
    ("crée la séquence de 5 emails de bienvenue", 746),
    ("lance une campagne google ads à 30 euros par jour", 747),
    ("fais l'audit seo technique de mon site", 748),
    ("optimise cet article pour le mot-clé choisi", 749),
    ("contrat client — exemple concret d'utilisation", 750),
    ("quelles obligations rgpd pour notre pme", 751),
    ("faut-il déposer notre marque avant le lancement", 752),
    ("sommes-nous concernés par l'ai act pour le tri de cv", 753),
    ("notre serveur a été compromis, procédure d'incident", 754),
    ("mets en place la sauvegarde 3-2-1", 755),
    ("fais la routine de nettoyage de mes appareils", 756),
    ("forme mon équipe au phishing", 757),
    ("est-ce que ce site marchand est sûr pour payer", 758),
    ("quelles démarches pour embaucher mon premier salarié", 759),
    ("réunion à distance — exemple concret d'utilisation", 760),
    ("comment déléguer cette refonte sans micromanager", 761),
    ("deux collègues se disputent, je médie", 762),
    ("aide-moi à prioriser avec la matrice d'eisenhower", 763),
    ("comment installer l'habitude de lire le soir", 764),
    ("je rumine la nuit, que faire maintenant", 765),
    ("comment lui dire en cnv qu'il laisse la vaisselle", 766),
    ("prépare ma soutenance de master en 10 jours", 767),
    ("aide-moi à construire le plan de ma dissertation", 768),
    ("prépare mon grand oral de 5 minutes", 769),
    ("comment expliquer les équations à mon fils en 4e", 770),
    ("quel projet concret pour apprendre le dev web", 771),
    ("prépare mon entretien technique live coding", 772),
    ("négocie mon salaire de 45k à 52k", 773),
    ("rédige une candidature spontanée convaincante", 774),
    ("structure le business plan de ma marketplace", 775),
    ("prépare mon deck de levée de 300k", 776),
    ("prépare mon premier board investisseurs", 777),
    ("ma pme est souvent à découvert, gère la trésorerie", 778),
    ("ce client me doit 3 factures, quelles relances", 779),
    ("structure ce devis e-commerce avec options", 780),
    ("quel crm choisir pour 8 commerciaux", 781),
    ("migre mes 10 ans d'emails vers proton mail", 782),
    ("automatise mon rapport vendredi qui consolide 5 excel", 783),
    ("créons une base de connaissances pour l'équipe", 784),
    ("veille juridique : quelles lois 2026 nous concernent", 785),
    ("quelles assurances pro pour mon agence web", 786),
    ("actions rps immédiates, deux collègues en arrêt", 787),
    ("mon équipe full remote se désagrège, quels rituels", 788),
    ("check-list offboarding de mon développeur qui part", 789),
    ("déroule le recrutement de notre commercial", 790),
    ("plan de formation ia générative pour mon équipe", 791),
    ("je suis élu cse, quelles réunions obligatoires", 792),
    ("quels rituels scrum dès la semaine 1", 793),
    ("risques prioritaires de notre projet de migration", 794),
    ("comment embarquer l'équipe sur le nouveau crm", 795),
    ("litige client : 5000 euros de dommages sur une livraison en retard", 796),
    ("analyse notre nps de 32 et agis", 797),
    ("78 % de paniers abandonnés, diagnostique le tunnel", 798),
    ("plan de lancement de notre appli dans 6 semaines", 799),
    ("déléguer à un agent ia", 800),
    ("gouvernance agents ia", 801),
    ("claude-mem", 802),
    ("webmcp", 803),
    ("lightpanda", 803),
    ("studio de jeu ia", 804),
    ("hallmark design", 805),
    ("bullshit detector", 806),
    ("agenttrace", 807),
    ("voicebox", 808),
    ("coder à la voix", 809),
    ("muse vs dots", 810),
    ("loi 2026-103", 811),
    ("optimisation fiscale légale 2026 pour un particulier", 812),
    ("temps d'écran", 813),
    ("rythme circadien", 814),
    ("comprendre l'ia", 815),
    ("apprendre la data literacy pour lire les chiffres", 816),
    ("affiner un prompt", 817),
    ("page web malveillante agent", 818),
    ("monitoring agent prod", 819),
    ("agent as organization", 820),
    ("coderabbit", 821),
    ("revue de pr avec agent hq github", 821),
    ("doc to test", 822),
    ("agentic ui", 823),
    ("business email compromise", 824),
    ("obtenir une remise", 825),
    ("estimation immobilière", 826),
    ("locataire ne paie plus", 827),
    ("règlement coloc", 828),
    ("lettre de démission", 829),
    ("are pôle emploi", 830),
    ("tarif journalier freelance", 831),
    ("recouvrement amiable d'un impayé de 45 jours", 832),
    ("loi lemoine", 833),
    ("rachat de crédit", 834),
    ("fonds euros", 835),
    ("pierre papier", 836),
    ("donation partage", 837),
    ("déréférencement", 838),
    ("mail ciblé", 839),
    ("vidéo truquée", 840),
    ("synchroniser mes photos téléphone et pc en chiffré", 841),
    ("arnaque influenceur", 842),
    ("check-list audit", 843),
    ("pondérer des critères", 844),
    ("expression de besoin", 845),
    ("post-mortem blameless", 846),
    ("clarifier les rôles d'un projet avec raci", 847),
    ("déclaration d'intérêt", 848),
    ("visio importante", 849),
    ("lettre de réclamation", 850),
    ("arnaque leboncoin", 851),
    ("répondre à un aap", 852),
    ("relire un contrat", 853),
    ("arnaque airbnb", 854),
    ("médiation consommation", 855),
    ("s'engager association", 856),
    ("démarches après décès", 857),
    ("mécénat", 858),
    ("numéros d'urgence", 859),
    ("anti gaspi", 860),
    ("préparer ses repas de la semaine", 861),
    ("archivage familial", 862),
    ("organiser un mariage", 863),
    ("nuisances sonores voisin", 864),
    ("trouver un vol low cost pas cher", 865),
    ("permis 17 ans", 866),
    ("cours de guitare adulte", 867),
    ("cuisine italienne", 868),
    ("check-list déménagement", 869),
    ("arnaque annonce immobilière", 870),
    ("contrôle parental", 871),
    ("préparer mon entretien d'embauche en visio", 872),
    ("pc ne démarre plus", 873),
    ("arnaque recrutement", 874),
    ("contre-offre salaire", 875),
    ("évaluation annuelle équipe", 876),
    ("équipe hybride", 877),
    ("concentration bureau", 878),
    ("préparer un pitch", 879),
    ("client toxique", 880),
    ("enquête anonyme", 881),
    ("renégocier contrat fournisseur", 882),
    ("charte informatique", 883),
    ("charte télétravail", 884),
    ("document unique risques", 885),
    ("déclaration accident travail", 886),
    ("contrat apprentissage", 887),
    ("plan de départs volontaires", 888),
    ("protocole préélectoral", 889),
    ("préavis de grève déposé par les syndicats", 890),
    ("transmission entreprise", 891),
    ("statuts association", 892),
    ("syndic défaillant", 893),
    ("pinel 2026", 894),
    ("assurance décennale", 895),
    ("révision loyer commercial", 896),
    ("rc dirigeant", 897),
    ("levée amorçage 2026", 898),
    ("rétrospective perso", 899),
    # --- Vague 12 (skills 800-899) ---
    ("déléguer des tâches à mon agent personnel", 800),
    ("quelles permissions donner à un agent ia", 801),
    ("donner une mémoire persistante à mon agent", 802),
    ("faire naviguer un agent avec webmcp", 803),
    ("organiser un studio de jeu avec des agents ia", 804),
    ("mon site ressemble à tous les sites ia", 805),
    ("vérifier les claims de cet article", 806),
    ("auditer ma dernière session avec l'agent de code", 807),
    ("créer un standard téléphonique vocal en local", 808),
    ("piloter mon agent de code à la voix", 809),
    ("quel agent personnel choisir en 2026", 810),
    ("qu'est-ce qui change dans la loi de finances 2026", 811),
    ("optimiser mes impôts légalement en 2026", 812),
    ("faire un digital detox réaliste", 813),
    ("régulariser mon sommeil", 814),
    ("apprendre l'ai literacy pour mon équipe", 815),
    ("lire un graphique sans me faire avoir", 816),
    ("affiner un prompt par dialogue itératif", 817),
    ("mon agent a suivi une instruction d'une page web", 818),
    ("quels guardrails avant de déployer un agent", 819),
    ("organiser une équipe de 5 agents ia", 820),
    ("revue de pr auto — exemple concret d'utilisation", 821),
    ("générer des tests depuis ma spec api", 822),
    ("rendre mon interface adaptative au niveau utilisateur", 823),
    ("j'ai reçu un mail du dg en déplacement demandant un virement urgent", 824),
    ("négocier ma facture hébergeur", 825),
    ("vendre mon appartement au meilleur prix", 826),
    ("mon locataire ne paie plus depuis 2 mois", 827),
    ("rédiger un règlement de colocation", 828),
    ("j'ai reçu une offre et je veux démissionner", 829),
    ("ai-je droit au chômage après une rupture conventionnelle", 830),
    ("calculer mon tjm de freelance", 831),
    ("relance amiable avant mise en demeure", 832),
    ("changer d'assurance emprunteur loi lemoine", 833),
    ("rembourser mon crédit par anticipation", 834),
    ("arbitrer mon assurance vie", 835),
    ("investir en scpi en 2026", 836),
    ("préparer ma succession avec des donations", 837),
    ("faire valoir mon droit à l'oubli", 838),
    ("j'ai reçu un mail ciblé avec mes vraies infos", 839),
    ("c'était un appel vidéo deepfake", 840),
    ("sauvegarder et synchroniser en chiffré", 841),
    ("vérifier cet influenceur avant d'acheter", 842),
    ("préparer notre audit iso 27001", 843),
    ("choisir un crm avec une matrice de décision", 844),
    ("rédiger le cdc de notre nouveau site", 845),
    ("faire la rétro blameless de l'incident", 846),
    ("clarifier qui fait quoi avec raci", 847),
    ("mon frère répond à notre appel d'offres, conflit d'intérêts", 848),
    ("préparer ma visio avec le comité", 849),
    ("rédiger une lettre de réclamation", 850),
    ("acheter sur leboncoin en sécurité", 851),
    ("répondre à un appel d'offres mairie", 852),
    ("lire ce bail avant de signer", 853),
    ("louer un airbnb sans me faire arnaquer", 854),
    ("mon artisan a bâclé la rénovation, quelles étapes", 855),
    ("m'engager comme bénévole dans une asso", 856),
    ("démarches après le décès de mon père", 857),
    ("faire un don défiscalisé à une asso", 858),
    ("préparer notre plan d'urgence incendie", 859),
    ("faire ma liste de courses anti gaspi", 860),
    ("faire du batch cooking le dimanche", 861),
    ("classer tous mes papiers admin", 862),
    ("organiser le baptême de ma fille", 863),
    ("trouver un billet de train pas cher", 865),
    ("ma fille de 16 ans veut le permis en aac", 866),
    ("apprendre la guitare à 40 ans", 867),
    ("apprendre la cuisine italienne", 868),
    ("déménager à 3 en colocation", 869),
    ("vérifier cette annonce immo avant de visiter", 870),
    ("donner un smartphone à mon ado de 12 ans en sécurité", 871),
    ("mon pc fait un clic et rame", 873),
    ("cette offre d'emploi à 4000 euros sans entretien", 874),
    ("négocier mon offre d'emploi", 875),
    ("préparer les entretiens annuels de mon équipe", 876),
    ("mon équipe est moitié présentiel moitié remote", 877),
    ("je n'arrive plus à me concentrer en open space", 878),
    ("préparer ma présentation au comité", 879),
    ("gérer ce client qui hurle au téléphone", 880),
    ("mettre en place un feedback anonyme", 881),
    ("négocier avec mon fournisseur d'hébergement", 882),
    ("on passe à 55 salariés, le règlement intérieur", 883),
    ("rédiger notre accord de télétravail", 884),
    ("mettre à jour notre duerp", 885),
    ("recruter notre premier alternant", 887),
    ("on veut faire une rupture conventionnelle collective", 888),
    ("organiser nos élections cse", 889),
    ("les syndicats ont déposé un préavis de grève", 890),
    ("vendre ma pme dans 3 ans", 891),
    ("créer une association loi 1901", 892),
    ("changer de syndic, il ne répond plus", 893),
    ("acheter en lmnp en 2026", 894),
    ("souscrire la dommages-ouvrage avant les travaux", 895),
    ("mon bail commercial arrive à 9 ans", 896),
    ("protéger mon entreprise avec une assurance homme clé", 897),
    ("préparer notre levée de fonds amorçage", 898),
    ("faire mon bilan de l'année", 899),
    # --- Vague 12 (skills 800-899) ---
    ("disque dur qui clique", 873),
    ("un salarié s'est blessé sur une machine", 886),
    ("accident travail machine", 886),
    ("grève naO syndicats", 890),
    ("cession pme 30 personnes", 891),
    ("accident du travail déclaration", 886),
    ("déclaration AT 48h", 886),
    ("médiation conflit collectif", 890),
    ("préparer cession entreprise", 891),
    ("vendre entreprise", 891),
    ("voisin travaux 7h", 864),
    ("trouble anormal voisinage", 864),
    ("enfant ado smartphone règles", 871),
    ("e-sécurité enfants ligne", 871),
    ("disque dur clique récupération", 873),
    ("panne pc disque dur", 873),
    ("accident du travail", 886),
    ("gestion accident travail", 886),
    ("conflit salarial", 890),
    ("négociation annuelle obligatoire", 890),
    ("litige de voisinage", 864),
    ("médiation voisinage", 864),
    ("panne informatique", 873),
    ("mon ordinateur ne démarre plus", 873), ("récupérer données disque dur", 873),
    
    ("mon ordinateur ne démarre plus, que faire", 873),
    ("récupérer les données d'un disque dur qui clique", 873),
    ("disque dur qui clique pc", 873),


    ("mon voisin fait du bruit à 7h du matin", 864),
    # --- Vague 13 (skills 900-999) ---
    # --- Vague 13 (skills 900-999) ---
    ("préparer l'ai act haut risque avant décembre 2027", 900),
    ("mon chatbot doit-il dire qu'il est une ia", 901),
    ("notre appli évalue la productivité avec une ia", 902),
    ("faire tourner un petit modèle ia en local", 903),
    ("déployer un agent vocal sur notre hotline", 904),
    ("installer une skill clawhub en sécurité", 905),
    ("mon certificat lets encrypt passe à 64 jours en février 2027", 906),
    ("se défendre des attaques ia autonomes", 907),
    ("gouverniser les agents ia comme des identités", 908),
    ("protéger mon api du scraping de bots ia", 909),
    ("don d'argent à 6 % au premier semestre 2027", 910),
    ("mon indemnité de rupture sera plafonnée à 1 pass", 911),
    ("afficher les salaires dans nos offres dès 2027", 912),
    ("partir en europe en 2027, faut-il l'etias", 913),
    ("nouvelle ligne de train munich rome en 2027", 914),
    ("se préparer à la canicule de l'été 2027", 915),
    ("adopter des micro-rituels de régulation nerveuse", 916),
    ("suivre ma glycémie avec un capteur cgm", 917),
    ("négocier la semaine de 4 jours", 918),
    ("me reconvertir dans la cybersécurité en 2027", 919),
    ("ne pas répondre aux mails le soir, mon droit", 920),
    ("je m'ennuie au travail, c'est le bore-out", 921),
    ("recruter par compétences plutôt que diplômes", 922),
    ("passer à un dumbphone en 2027", 923),
    ("héberger nos données en europe en 2027", 924),
    ("brancher plusieurs agents dans rabbit 2", 925),
    ("faire générer des formulaires par l'ia", 926),
    ("prévoir le coût des logiciels ia dans le budget 2027", 927),
    ("mes collègues utilisent chatgpt perso au bureau", 928),
    ("tester nos scénarios logistique avec un world model", 929),
    ("générer un jingle avec suno", 930),
    ("les robots humanoïdes arrivent dans mon usine", 931),
    ("contrôle biométrique à la frontière schengen en 2027", 932),
    ("visa graduate uk à 18 mois en 2027", 933),
    ("powerbank en cabine avion en 2027", 934),
    ("aides anah recentrées en 2027", 935),
    ("reprise de mon entreprise par les salariés en 2027", 936),
    ("prévenir les rps comme indicateur 2027", 937),
    ("être cité par chatgpt quand on cherche un comparatif", 938),
    ("vérifier les sorties de mon agent avant prod", 939),
    ("scraper des données publiques légalement", 940),
    ("créatine et santé cardiaque, quelles preuves en 2027", 941),
    ("choisir un hôtel optimisé pour le sommeil", 942),
    ("faire tourner siri en local sur mon téléphone", 943),
    ("vérifier une info avec notebooklm ancré", 944),
    ("le prompt caveman pour des réponses courtes", 945),
    ("empêcher les llm d'entraîner sur mon contenu", 946),
    ("lancer un agent jetable pour une tâche ponctuelle", 947),
    ("se préparer aux 1,5 million de contrôles cnil en 2027", 948),
    ("faire mon bilan 2026 et mes objectifs 2027", 949),
    ("on doit faire un pse", 950),
    ("mettre en place un accord d'intéressement", 951),
    ("prévenir l'addiction aux paris en ligne", 952),
    ("fraude sur ma carte bancaire ce matin", 953),
    ("mon passeport a été volé à l'étranger", 954),
    ("renouveler mon passeport sur ants en 2027", 955),
    ("arnaque sur un site de rencontre", 956),
    ("mon compte instagram a été piraté", 957),
    ("je m'expatrie au portugal en 2027", 958),
    ("acheter une voiture électrique d'occasion en 2027", 959),
    ("installer une borne de recharge chez moi", 960),
    ("rénovation énergétique globale de ma maison", 961),
    ("arnaque à l'annonce de colocation", 962),
    ("rédiger mon testament", 963),
    ("ouvrir un pea en 2027", 964),
    ("comparer deux assurances habitation", 965),
    ("simuler un crédit immobilier en 2027", 966),
    ("vérifier une entreprise avant d'y postuler", 967),
    ("préparer mon entretien d'embauche avec la méthode star", 968),
    ("négocier ma rupture conventionnelle", 969),
    ("j'ai mal au poignet au bureau depuis 6 mois", 970),
    ("conflit avec un collègue qui prend mes idées", 971),
    ("organiser le pot de départ de mon collègue", 972),
    ("mon net a baissé sans explication sur ma paie", 973),
    ("déclarer mes revenus en mai 2027", 974),
    ("faire reconnaître ma tendinite comme maladie pro", 975),
    ("acheter en vefa un appartement neuf en 2027", 976),
    ("louer mon bien en meublé ou en nu en 2027", 977),
    ("préparer ma retraite à 64 ans", 978),
    ("faire un audit énergétique avant de louer", 979),
    ("créer une sci avec ma famille en 2027", 980),
    ("mon artisan a bâclé la toiture", 981),
    ("je suis en surendettement, que faire", 982),
    ("acheter un iphone reconditionné en sécurité", 983),
    ("road-trip en van aménagé cet été 2027", 984),
    ("mariage écolo à petit budget en 2027", 985),
    ("faire le gr20 en trek en 2027", 986),
    ("organiser l'evjf de ma sœur en 2027", 987),
    ("faire la vélodyssée à vélo en 2027", 988),
    ("expédition kayak sur la dordogne", 989),
    ("partir en volontariat international vsi en 2027", 990),
    ("déménager au canada en 2027", 991),
    ("acheter un appartement au portugal en 2027", 992),
    ("mon vol a 5h de retard, quelle indemnisation", 993),
    ("quelle assurance voyage pour la thaïlande", 994),
    ("road-trip moto dans les alpes en 2027", 995),
    ("organiser notre séminaire d'entreprise en 2027", 996),
    ("changer de poste en interne en 2027", 997),
    ("prendre un congé sabbatique d'un an", 998),
    ("faire mon bilan 2026 et poser mes objectifs 2027", 999),

    # --- Merge SkillsAI ---
    ("acceptance-scenario-derivation", 1000),
    ("accessibility-evidence-register", 1001),
    ("accessible-alternative-text-review", 1002),
    ("accountant-meeting-document-preparation", 1003),
    ("active-directory-architecture-design", 1004),
    ("active-directory-management", 1005),
    ("ad-migration-consolidation", 1006),
    ("ad-replication-sites-management", 1007),
    ("ad-security-tiering", 1008),
    ("adaptive-audio-implementation", 1009),
    ("adaptive-interactive-music-stems", 1010),
    ("adversarial-testing-robustness", 1011),
    ("advertising-measurement-experimentation", 1012),
    ("agent-role-regression-campaign", 1013),
    ("agent-state-boundary-design", 1014),
    ("ai-act-technical-oversight-mapping", 1015),
    ("ai-adoption-feedback-decision", 1016),
    ("ai-capability-interface-specification", 1017),
    ("ai-ethical-impact-decision-record", 1018),
    ("skill-ai-explainability-transparency", 1019),
    ("ai-feature-prioritization-metrics", 1020),
    ("ai-feature-success-contract", 1021),
    ("ai-model-release-value-decision", 1022),
    ("ai-product-discovery-adoption", 1023),
    ("ai-product-strategy-roadmap", 1024),
    ("ai-si-integration-strategy", 1025),
    ("ai-system-architecture-design", 1026),
    ("ai-system-failure-recovery-design", 1027),
    ("ai-transparency-audience-plan", 1028),
    ("anti-bot-evasion-scraping-best-practices", 1029),
    ("api-documentation-openapi-specification", 1030),
    ("api-and-webhook-contract-mapping", 1031),
    ("application-diagnostics-troubleshooting", 1032),
    ("application-migration-data-transfer", 1033),
    ("application-synchronization-conflict-policy", 1034),
    ("appsec-trust-boundary-review", 1035),
    ("apt-and-pacman-recovery-planning", 1036),
    ("architecture-quality-scenario", 1037),
    ("artifact-dependency-inventory", 1038),
    ("asp-net-core-api-development", 1039),
    ("audit-coherence-logique-brief", 1040),
    ("b2b-prospecting-lead-qualification", 1041),
    ("backend-transaction-consistency", 1042),
    ("backup-recovery-automation", 1043),
    ("bash-exit-and-signal-safety", 1044),
    ("behavioral-pattern-analysis-analyse-patterns-comportementaux", 1045),
    ("belgian-accounting-bookkeeping-basics", 1046),
    ("belgian-vat-tax-orientation", 1047),
    ("bitmap-texture-sprite-sheet-preparation", 1048),
    ("blazor-component-design", 1049),
    ("blender-game-ready-export-pipeline", 1050),
    ("blender-hard-surface-organic-modeling", 1051),
    ("blender-rigging-animation-workflow", 1052),
    ("blender-uv-unwrap-pbr-material-setup", 1053),
    ("bounded-utility-specification", 1054),
    ("bpmn-process-modeling", 1055),
    ("brand-positioning-strategy", 1056),
    ("brief-assumption-ledger", 1057),
    ("business-insight-narrative", 1058),
    ("business-kpi-analysis-dashboard-design", 1059),

    # --- Vague 14 (skills 1311-1350) ---
    ("prairie fleurie jardin", 1311),
    ("haie variée biodiversité", 1312),
    ("cuisine connectée 2027", 1313),
    ("batch cooking 2027", 1314),
    ("domotique matter 2027", 1315),
    ("déco 2027 vert saule", 1316),
    ("france identité cnie", 1317),
    ("contrôle routier numérique", 1318),
    ("coach sportif ia", 1319),
    ("diététicien ia 2027", 1320),
    ("tuteur ia personnalisé", 1321),
    ("trouver un cadeau ia", 1322),
    ("organiser voyage ia 2027", 1323),
    ("budget perso ia 2027", 1324),
    ("coach sommeil ia", 1325),
    ("planifier semaine ia", 1326),
    ("bien-être mental ia 2027", 1327),
    ("courses ia 2027", 1328),
    ("veille ia personnalisée", 1329),
    ("déménagement local 2027", 1330),
    ("bilan santé préventif", 1331),
    ("bien vieillir 2027", 1332),
    ("santé animale 2027", 1333),
    ("sécurité domicile 2027", 1334),
    ("premiers secours 2027", 1335),
    ("arnaque qr code 2027", 1336),
    ("gestionnaire mots de passe 2027", 1337),
    ("coffre numérique familial", 1338),
    ("vacances tranquilles 2027", 1339),
    ("réparer son vélo", 1340),
    ("email pro percutant", 1341),
    ("prise de parole public", 1342),
    ("apprendre une langue ia", 1343),
    ("lecture rapide mémorisation", 1344),
    ("négocier salaire 2027", 1345),
    ("routine matinale 2027", 1346),
    ("désencombrer 2027", 1347),
    ("entretien annuel 2027", 1348),
    ("anti-gaspi cuisine", 1349),
    ("bilan 2027 objectifs 2028", 1350),
    ("routine d'immersion linguistique quotidienne pour progresser en espagnol", 1351),
    ("vivre en immersion dans une langue etrangere", 1351),
    ("séance de shadowing prononciation orale", 1352),
    ("shadowing audio pour l'anglais", 1352),
    ("répétition espacée vocabulaire avec anki", 1353),
    ("cartes mémoire espacées pour retenir l'italien", 1353),
    ("rédiger des emails en langue des affaires anglais professionnel", 1354),
    ("business english pour une réunion", 1354),
    ("plan polyglotte pour apprendre 2 langues", 1355),
    ("apprendre 3 langues en même temps sans les mélanger", 1355),
    ("améliorer ma compréhension orale podcasts sans sous-titres", 1356),
    ("plan de compréhension orale podcasts sans sous-titres pour passer B2", 1356),
    ("lire des romans en langue étrangère sans traduire", 1357),
    ("graded readers pour mon niveau d'anglais", 1357),
    ("préparer un entretien d'embauche en langue étrangère anglais", 1358),
    ("job interview in english tell me about yourself", 1358),
    ("financer ma formation ia cpf 2027 reste à charge", 1359),
    ("mon compte formation plafond 2027", 1359),
    ("choisir une formation ia certifiante 2027", 1360),
    ("certification utiliser l'ia anssi afpa comparatif", 1360),
    ("concevoir un parcours formation blended pour mon équipe", 1361),
    ("formation hybride présentiel distanciel planning", 1361),
    ("former ses équipes à l'ia atelier interne 90 min", 1362),
    ("sensibiliser mes collègues à l'ia", 1362),
    ("évaluer l'efficacité d'une formation kirkpatrick", 1363),
    ("mesurer l'impact d'une formation à 3 mois", 1363),
    ("auto-formation ia parcours personnel 30 min par jour", 1364),
    ("apprendre l'ia seul gratuitement", 1364),
    ("construire un arbre de décision pour lancer un produit", 1365),
    ("decision tree avec probabilités et valeurs attendues", 1365),
    ("daci raci pour décider en équipe sur un projet", 1366),
    ("qui décide : mettre en place les rôles clairs", 1366),
    ("règle 10-10-10 pour ma décision de démissionner", 1367),
    ("conséquences à 10 mois et 10 ans de ce choix", 1367),
    ("biais cognitifs ancrage confirmation dans ma décision", 1368),
    ("coût de l'inaction de reporter ce choix", 1368),
    ("rédiger la vision produit d'une feature ia chatbot", 1369),
    ("ai product vision pourquoi maintenant en 2027", 1369),
    ("concevoir l'onboarding d'une feature ia en 3 étapes", 1370),
    ("time to value de moins de 5 minutes pour notre ia", 1370),
    ("mesurer l'adoption de notre feature ia wau mensuel", 1371),
    ("mesurer adoption feature ia wau en production", 1371),
    ("choisir la bonne skill pour préparer un bilan de compétences", 1372),
    ("choisir la bonne skill pour une tâche : un communiqué de presse", 1372),
    ("composer un workflow de skills en chaine depends_on", 1373),
    ("enchaîner recherche puis rédaction avec les skills", 1373),
    ("organiser mon bureau physique avec les 3 zones", 1374),
    ("un tiroir une catégorie rangement bureau", 1374),
    ("règle des 5 minutes pour vider mon courrier papier", 1375),
    ("ne toucher qu'une fois chaque document", 1375),
    ("dématérialiser mes documents avec scan et digiposte", 1376),
    ("coffre-fort numérique pour mes papiers 2027", 1376),
    ("session hebdomadaire classement papier 15 min vendredi", 1377),
    ("classement papier hebdomadaire 15 minutes chaque vendredi", 1377),
    ("organiser une visioconférence hybride salle et distanciel", 1378),
    ("équipement micro caméra pour réunion hybride 2027", 1378),
    ("donner procuration en ligne pour une démarche mairie", 1379),
    ("faire une démarche administrative à ma place en 2027", 1379),
    ("choisir le modèle économique saas ou licence pour mon appli", 1380),
    ("passer en usage-based pricing en 2027", 1380),
    ("acquisition vs rétention : où mettre mon budget 2027", 1381),
    ("calculer cac ltv ratio ltv cac", 1381),
    ("rédiger le plan stratégique 3 ans 2027-2029", 1382),
    ("objectifs stratégiques avec KPI pour 2029", 1382),
    ("préparer ma stratégie export international 2027 pays cibles", 1383),
    ("aides team france export bpifrance 2027", 1383),
    ("évaluer une cible acquisition m&a multiples ebitda 2027", 1384),
    ("checklist due diligence avant rachat d'entreprise", 1384),
    ("intégrer l'esg rse au business model 2027", 1385),
    ("sommes-nous soumis à la csrd en 2027 ?", 1385),
    ("organiser ma bibliographie académique zotero apa", 1386),
    ("gérer mes références de thèse dans zotero", 1386),
    ("critiquer une étude scientifique p-value biais 2027", 1387),
    ("cette étude observationnelle prouve-t-elle quelque chose ?", 1387),
    ("revue de littérature systématique prisma protocole pico", 1388),
    ("diagramme prisma sélection des études 2027", 1388),
    ("éviter le biais de confirmation dans ma recherche d'info", 1389),
    ("trouver des sources contraires à mon hypothèse", 1389),
    ("trouver le décret au journal officiel 2027 légifrance", 1390),
    ("loi en vigueur en 2027 code consolidé", 1390),
    ("modéliser un schéma en étoile table de faits dimensions", 1391),
    ("star schema data warehouse 2027", 1391),
    ("choisir le bon graphique pour mon ca mensuel 2027", 1392),
    ("camembert ou barres pour 6 catégories", 1392),
    ("rédiger une data card pour mon dataset 2027", 1393),
    ("documenter un dataset : licence biais colonnes", 1393),
    ("benchmark de datasets publics pour mon projet ml 2027", 1394),
    ("data.gouv kaggle hugging face licence données", 1394),
    ("construire un golden set d'évaluations pour mon agent ia 2027", 1395),
    ("evals agent ia jeu de test de référence", 1395),
    ("préparer un dataset propre pour le fine-tuning jsonl 2027", 1396),
    ("préparer dataset propre fine-tuning jsonl sans fuite rgpd", 1396),
    ("mesurer la qualité de mon rag faithfulness ragas 2027", 1397),
    ("évaluer la pertinence context precision recall de mon rag", 1397),
    ("gérer une question piège en interview média 2027", 1398),
    ("technique du pont pour ne pas répéter l'accusation", 1398),
    ("annoncer une fusion difficile à l'équipe avec humanité 2027", 1399),
    ("annoncer un changement sensible fusion licenciement humanité", 1399),
    ("git rebase interactif pour squash mes commits", 1400),
    ("historique git propre avant PR", 1400),
    ("méthode de revue de code constructive PR", 1401),
    ("comment formuler mes commentaires de review", 1401),
    ("résoudre un conflit de merge git ours theirs", 1402),
    ("git conflict que faire", 1402),
    ("mettre en place pre-commit framework hooks", 1403),
    ("hook git pre-commit lint automatique", 1403),
    ("gitflow ou trunk-based pour mon équipe", 1404),
    ("stratégie de branching github flow comparatif", 1404),
    ("refactorer du code legacy en sécurité", 1405),
    ("characterization tests puis petits pas", 1405),
    ("mettre en place docs-as-code documentation vivante", 1406),
    ("documentation vivante docs-as-code markdown docusaurus — exemple concret d'utilisation", 1406),
    ("commentaires code utiles : pourquoi pas quoi dans le code", 1407),
    ("nettoyer les commentaires morts", 1407),
    ("gestion propre des erreurs try catch niveaux", 1408),
    ("exceptions métier nommées message actionnable", 1408),
    ("logging structuré JSON niveaux request_id", 1409),
    ("passer mes logs en format JSON", 1409),
    ("configuration 12-factor variables d'environnement", 1410),
    ("configuration 12-factor variables environnement — exemple concret d'utilisation", 1410),
    ("docker multi-stage pour image légère", 1411),
    ("dockerfile optimisé distroless non-root", 1411),
    ("déployer sur kubernetes manifests yaml deployment", 1412),
    ("configmap secret k8s sondes liveness", 1412),
    ("accélérer ma pipeline CI github actions cache", 1413),
    ("jobs parallèles matrix CI rapide", 1413),
    ("tests de contrat pact consumer provider", 1414),
    ("consumer contract testing API microservices", 1414),
    ("test de charge k6 script seuils p95", 1415),
    ("k6 ou locust test de performance 2027", 1415),
    ("monitoring prometheus grafana golden signals", 1416),
    ("alertes grafana sur SLO taux erreur", 1416),
    ("réduire le bruit des alertes alert fatigue", 1417),
    ("alertes actionnables avec runbook SLO", 1417),
    ("déploiement canary 5% rollout progressif", 1418),
    ("rollback auto si erreurs canary", 1418),
    ("créer index composite explain analyze", 1419),
    ("requête lente 4s quel index", 1419),
    ("window functions sql partition by row_number", 1420),
    ("calculer cumul et rank en SQL", 1420),
    ("deadlock base de données éviter", 1421),
    ("niveau isolation serializable read committed", 1421),
    ("choisir mongodb redis cassandra nosql", 1422),
    ("choisir base nosql mongodb redis cassandra selon le cas", 1422),
    ("cache redis cache-aside TTL invalidation", 1423),
    ("mettre en cache les profils utilisateurs", 1423),
    ("validation entrées pydantic zod API", 1424),
    ("contraintes BDD check fk not null", 1424),
    ("bibliothèque de prompts modulaires composants", 1425),
    ("versionner mes prompts dans git", 1425),
    ("few-shot exemples dans le prompt LLM", 1426),
    ("fixer le format de sortie avec 4 exemples", 1426),
    ("sortie JSON fiable LLM validation pydantic", 1427),
    ("forcer le JSON en sortie du modèle", 1427),
    ("agent react boucle thought action observation", 1428),
    ("limiter itérations agent max 10", 1428),
    ("concevoir outils agent function calling noms", 1429),
    ("concevoir outils agent function calling noms et descriptions", 1429),
    ("contexte long LLM 200k quoi garder", 1430),
    ("lost in the middle placer info clé début fin", 1430),
    ("compaction conversation résumé seuil 80%", 1431),
    ("quoi garder dans le résumé de session", 1431),
    ("équipe agents spécialisés orchestrateur délégation", 1432),
    ("multi-agents par domaine 2027", 1432),
    ("human in the loop approbation multi-niveaux", 1433),
    ("agent qui demande validation avant action externe", 1433),
    ("mémoire agent sémantique épisodique vector store", 1434),
    ("préférences utilisateur retenues d'une session à l'autre", 1434),
    ("A/B testing prompts production 50/50", 1435),
    ("quelle version du prompt garder p-value", 1435),
    ("grounding réponses LLM citer sources", 1436),
    ("grounding réponses LLM citer les sources je ne sais pas si absent", 1436),
    ("self-check vérification 2 passes LLM", 1437),
    ("self-check vérification multi-passes grille de relecture LLM", 1437),
    ("déployer SLM on-device mobile offline llama.cpp", 1438),
    ("modèle quantizé Q4 latence batterie 2027", 1438),
    ("streaming réponses LLM UX tokens au fur et à mesure", 1439),
    ("annuler une génération LLM en cours", 1439),
    ("détecter PII données perso dans prompt LLM", 1440),
    ("masquer IBAN CNI automatiquement guardrail", 1440),
    ("cascade modèles router tâche petit grand LLM", 1441),
    ("réduire coût inférence fallback SLM", 1441),
    ("cache sémantique réponses LLM seuil 0,95", 1442),
    ("requêtes similaires servies depuis le cache", 1442),
    ("choisir modèle embeddings 2027 MTEB", 1443),
    ("benchmark embeddings sur 50 requêtes réelles", 1443),
    ("chunking RAG overlap 20% sémantique", 1444),
    ("chunking RAG overlap sémantique hiérarchique 200-500 tokens", 1444),
    ("dependabot renovate PR auto dépendances", 1445),
    ("CVE corriger en priorité merge rapide", 1445),
    ("rotation automatique secrets clés API vault", 1446),
    ("révoquer une clé en urgence fuite", 1446),
    ("audit IAM cloud moindre privilège AWS", 1447),
    ("supprimer clés accès longue durée", 1447),
    ("messagerie E2EE Signal Proton choisir 2027", 1448),
    ("vérifier empreintes clés chiffrement bout en bout", 1448),
    ("déployer passkeys FIDO2 entreprise 2027", 1449),
    ("YubiKey vs passkeys plateforme choisir", 1449),
    ("oauth2 PKCE authorization code 2027", 1450),
    ("flow implicit interdit PKCE obligatoire", 1450),
    ("WAF Cloudflare protection DDoS applicative", 1451),
    ("rate limiting /login anti-bruteforce", 1451),
    ("CSP content security policy nonce anti-XSS", 1452),
    ("report-only puis enforcement CSP", 1452),
    ("SIEM Wazuh centraliser logs sécurité", 1453),
    ("détecter brute force SSH règles alerte", 1453),
    ("organiser tabletop exercice crise cyber ransomware", 1454),
    ("plan de réponse incident testé en exercice", 1454),
    ("privacy by design RGPD art 25 feature", 1455),
    ("minimisation données + purge auto 30 jours", 1455),
    ("certificate pinning app mobile 2027", 1456),
    ("Keychain Keystore stockage sécurisé token", 1456),
    ("vérifier signature paquet cosign sigstore", 1457),
    ("SLSA provenance build niveau 3", 1457),
    ("déployer honeypot cowrie détection scans", 1458),
    ("canary token faux fichier alerte SIEM", 1458),
    ("préparer certification ISO 27001 gap analysis", 1459),
    ("annexe A 93 mesures SMSI preuves", 1459),
    ("airflow prefect dagster choisir orchestrateur 2027", 1460),
    ("migrer scripts cron vers orchestrateur", 1460),
    ("détecter schema drift colonne supprimée", 1461),
    ("data contracts monitoring Soda alerte", 1461),
    ("timescaledb influxdb choisir TSDB 2027", 1462),
    ("downsampling agrégation métriques anciennes", 1462),
    ("warehouse vs lakehouse choisir 2027", 1463),
    ("delta lake iceberg ACID time travel", 1463),
    ("kafka consumer group lag alerte", 1464),
    ("partitions clé user_id ordre garanti", 1464),
    ("anonymiser dataset RGPD k-anonymat k=5", 1465),
    ("pseudonymisation hash salé réversible", 1465),
    ("lineage provenance données OpenLineage DataHub", 1466),
    ("impact analysis si source CRM en panne", 1466),
    ("réduire facture BigQuery partitionnement date", 1467),
    ("clustering Snowflake user_id coût requête", 1467),
    ("feature store Feast train serve skew", 1468),
    ("features online offline point-in-time", 1468),
    ("centraliser logs Loki vs ELK 2027", 1469),
    ("rechercher erreur dans logs 50 serveurs", 1469),
    ("MLflow model registry staging prod 2027", 1470),
    ("DVC versionner dataset entraînement S3", 1470),
    ("déployer vLLM API LLM interne 2027", 1471),
    ("endpoint OpenAI compatible self-host", 1471),
    ("ollama servir modèle local GGUF Q4 2027", 1472),
    ("llama.cpp CPU tokens/s mesuré", 1472),
    ("distillation petit modèle imite grand LLM", 1473),
    ("SFT LoRA sur exemples générés qualité", 1473),
    ("DPO alignement modèle paires préférées", 1474),
    ("RLHF vs DPO choisir 2027", 1474),
    ("sandbox agent conteneur jetable gVisor", 1475),
    ("réseau allowlist proxy agent IA", 1475),
    ("tracer agent IA Langfuse spans outils args", 1476),
    ("déboguer agent avec les traces d'échec", 1476),
    ("recherche hybride BM25 embeddings RRF", 1477),
    ("fusion scores retrieval lexical sémantique", 1477),
    ("graphrag neo4j extraire entités relations corpus", 1478),
    ("requête multi-sauts graphe vs RAG classique", 1478),
    ("QLoRA fine-tuner 70B sur 24 Go VRAM", 1479),
    ("LoRA r=16 alpha=32 réglages 2027", 1479),
    ("rédiger une spec produit légère one-pager", 1480),
    ("métriques de succès d'une feature chiffrées", 1480),
    ("définir north star metric produit 2027", 1481),
    ("arbre de métriques leviers owners", 1481),
    ("mesurer impact feature A/B témoin exposé", 1482),
    ("décider ship kill iterate p-value", 1482),
    ("tests utilisateurs distance Maze 5 testeurs", 1483),
    ("questionnaire SUS après test parcours", 1483),
    ("WCAG 2.2 AA dès le design check contraste", 1484),
    ("navigation clavier testée sur maquette", 1484),
    ("préparer produit multilingue i18n clés pluriels", 1485),
    ("dates devises par locale Intl API", 1485),
    ("répondre aux feedbacks utilisateurs boucle fermée", 1486),
    ("changelog vous avez demandé on a livré", 1486),
    ("sunsetting feature annonce J-90 alternative", 1487),
    ("export données utilisateurs avant arrêt", 1487),
    ("intégrer copilote IA in-app panneau contextuel", 1488),
    ("suggestions proactives avec action 1 clic", 1488),
    ("afficher confiance réponse IA badge je ne sais pas", 1489),
    ("sources citées cliquables UI", 1489),
    ("modération sorties IA hybride LLM file humaine", 1490),
    ("classifier toxicité contenu généré seuils", 1490),
    ("coût feature IA par utilisateur mois projection", 1491),
    ("seuil rentabilité revenu > 3x coût IA", 1491),
    ("kill switch feature IA flag off 1 min", 1492),
    ("désactiver proprement IA message utilisateurs", 1492),
    ("audit cohérence visuelle 12 variantes bouton", 1493),
    ("écarts Figma vs code plan convergence", 1493),
    ("prototype cliquable v0 lovable 1 jour", 1494),
    ("tester idée feature sans dev", 1494),
    ("prefers-reduced-motion CSS animations", 1495),
    ("flashs 3 par seconde max WCAG 2.3.1", 1495),
    ("dark mode prefers-color-scheme tokens sémantiques", 1496),
    ("high contrast 7:1 WCAG AAA", 1496),
    ("analyser misses exit 2 suggestions synonymes", 1497),
    ("misses demandes non routées exit 2 suggestions synonymes à boucler", 1497),
    ("installer n8n auto-hébergé docker 2027", 1498),
    ("workflow webhook lead vers CRM alerte Slack", 1498),
    ("résumé auto réunion actions responsables fireflies", 1499),
    ("transcription recherchable qui a dit quoi", 1499),
    ("choisir moteur unity godot unreal 2027", 1500),
    ("godot 4 vs unity comparatif débutant", 1500),
    ("fixed timestep 60 hz accumulateur boucle jeu", 1501),
    ("interpolation rendu entre deux états alpha", 1501),
    ("gestion des scènes chargement asynchrone additif entre niveaux", 1502),
    ("scènes additives menu hud niveau", 1502),
    ("sauvegarder partie en JSON 3 slots auto-save", 1503),
    ("migration vieille save v1 vers v2", 1503),
    ("input actions remappable sauvegardé JSON", 1504),
    ("AZERTY QWERTY auto + manette xbox ps", 1504),
    ("caméra 2D deadzone lookahead clamp niveau", 1505),
    ("caméra 2D follow deadzone lookahead sans trembler", 1505),
    ("caméra 3D raycast anti mur lock-on", 1506),
    ("FOV sprint lerp 70 85 degrés", 1506),
    ("collision AABB MTV résolution séparation", 1507),
    ("collision 2D AABB cercles SAT test cercle vs cercle distance", 1507),
    ("hitbox hurtbox séparés i-frames 0,3 s", 1508),
    ("knockback directionnel hitstop 50 ms", 1508),
    ("saut variable appui long court couper vélocité", 1509),
    ("gravité custom 2500 px/s2 plateformer", 1509),
    ("coyote time 0,1 s après le sol", 1510),
    ("jump buffer appui avant atterrissage", 1510),
    ("diagonale normalisée pas plus rapide", 1511),
    ("dash cooldown 1 s i-frames trail", 1511),
    ("tilemap autotiling 47 tuiles voisins bits", 1512),
    ("peindre niveau éditeur collision auto", 1512),
    ("donjon procédural salles corridors seed", 1513),
    ("12 salles sans chevauchement corridors en L", 1513),
    ("cavernes automate cellulaire 45% 5 itérations", 1514),
    ("flood fill garder plus grande zone connexe", 1514),
    ("île Perlin 5 octaves persistence 0,5", 1515),
    ("biomes seuils eau herbe roche neige", 1515),
    ("WFC wave function collapse entropie propagation", 1516),
    ("règles compatibilité tuiles backtrack", 1516),
    ("A* grille heap f=g+h 8 directions poids terrain", 1517),
    ("flow field 200 unités 1 ms/frame", 1517),
    ("baker navmesh 3D pente 45 hauteur agent", 1518),
    ("NavigationAgent évitement RVO obstacles dynamiques", 1518),
    ("FSM patrouille poursuite attaque fuite transitions", 1519),
    ("IA ennemie FSM patrouille poursuite attaque fuite debug affiché", 1519),
    ("cône vision 90° 10 m occlusion raycast", 1520),
    ("ouïe course 8 m tir 20 m mémoire last_seen", 1520),
    ("utility AI besoins score choisir action max", 1521),
    ("utility AI score actions besoins faim PV choisir meilleure hystérésis", 1521),
    ("GOAP préconditions effets plan A* états", 1522),
    ("PNJ autonome planifie pour objectif épée", 1522),
    ("stealth 3 raycasts tête corps pieds occlusion", 1523),
    ("jauge détection 0-100 ombre -30% états", 1523),
    ("raycast LOS entre garde et joueur layer murs", 1524),
    ("tir hitscan raycast premier hit tracer", 1524),
    ("ennemis flanquent par le côté path latéral", 1525),
    ("focus fire cible marquée rôles tank dps", 1525),
    ("boss 3 phases PV transition invincible 2 s", 1526),
    ("attaque télégraphiée marque au sol puis dégâts", 1526),
    ("spawner 10 vagues budget 5+3n points composition", 1527),
    ("délai 10 s entre vagues boss vague 10", 1527),
    ("loot pondéré 60/30/9/1 pity x2 à 20 kills", 1528),
    ("drop épique garanti tous les 50", 1528),
    ("inflation gold sources vs sinks 60-80%", 1529),
    ("prix objets paliers x10 tous les 10 niveaux", 1529),
    ("courbe XP 100*1,15^n temps par niveau", 1530),
    ("paliers déblocage monture niveau 10", 1530),
    ("journal quêtes compteur 3/5 temps réel", 1531),
    ("récompenses XP gold objet à la validation", 1531),
    ("choix dialogue conditionné quête faite", 1532),
    ("arbre de dialogue nœuds choix conditions conséquences persistées save", 1532),
    ("textes jeu en 5 langues clés + fichiers JSON", 1533),
    ("pluriels ICU pseudo-localisation débordements", 1533),
    ("inventaire drag drop grille 5x4 souris manette", 1534),
    ("stack potions x99 tri auto tooltip", 1534),
    ("équiper arme comparatif flèche verte rouge", 1535),
    ("set bonus 2/4 pièces stats x2,5 légendaire", 1535),
    ("recette craft forge 3 fer 1 bois épée", 1536),
    ("démontage récupère 50% matériaux maîtrise bonus", 1536),
    ("skill tree prérequis parent débloquer nœud", 1537),
    ("1 point talent par niveau respec payant", 1537),
    ("toast succès débloqué 100 kills en jeu", 1538),
    ("achievements cachés % global sync Steam", 1538),
    ("save cloud upload auto fermeture conflit timestamp", 1539),
    ("sync Steam Cloud PC mobile même progression", 1539),
    ("funnel tutoriel taux passage par étape", 1540),
    ("rétention D1 D7 D30 dashboard analytics jeu", 1540),
    ("A/B test prix skin cohortes A B remote config", 1541),
    ("mesurer ARPU rétention D7 p-value ship kill", 1541),
    ("event saisonnier 2 semaines remote config skins niveau", 1542),
    ("battle pass 30 paliers gratuit payant 9,99 €", 1542),
    ("serveur autorité client envoie inputs uniquement", 1543),
    ("détection aimbot précision 95% shadowban ban", 1543),
    ("client-serveur dédié vs P2P vs relais choisir", 1544),
    ("architecture multijoueur client-serveur dédié P2P relais protocole UDP TCP", 1544),
    ("lag compensation rewind t-RTT/2 raycast état ancien", 1545),
    ("lag compensation rewind 200 ms ring buffer snapshots 50 ms", 1545),
    ("lockstep RTS inputs tick N déterministe replay", 1546),
    ("snapshots 20 Hz interpolation client 60 fps", 1546),
    ("prédiction client input seq immédiat 0 latence perçue", 1547),
    ("réconciliation rejouer inputs non ack snapshot serveur", 1547),
    ("chat in-game filtre insultes rate limit 1/2s", 1548),
    ("signalement 3 = mute 24h 10 = ban 7j", 1548),
    ("matchmaking MMR +25 victoire plage ±400 après 2 min", 1549),
    ("file d'attente match trouvé moins de 2 min", 1549),
    ("ECS composants données pures systèmes query", 1550),
    ("ECS entity component system composants données pures 10k entités 60 fps", 1550),
    ("object pool Get Release prewarm cap 500", 1551),
    ("object pooling pré-allouer réutiliser 0 allocation GC steady state", 1551),
    ("fuite mémoire Memory Profiler snapshot avant après", 1552),
    ("draw calls 2000 à 200 batching frame debugger", 1552),
    ("draw calls 2000 à 250 atlas batching occlusion LOD", 1553),
    ("frame debugger compter draw calls 60 fps mobile", 1553),
    ("atlas 500 sprites 2 textures 2048 padding 4px", 1554),
    ("draw calls UI 300 à 5 atlas 2048x2048", 1554),
    ("post-processing vignette grain bloom 1 passe URP", 1555),
    ("< 1 ms GPU mesuré profilé 60 fps stable", 1555),
    ("torche PointLight2D occluders murs font ombre", 1556),
    ("normal map 2D relief max 16 lights actifs mobile", 1556),
    ("10 000 particules GPU 1 draw call compute buffer", 1557),
    ("cap 5000 LOD divise spawn au loin < 1 ms GPU", 1557),
    ("screen shake explosion 0,5 decay exponentiel 0,4 s", 1558),
    ("screen shake caméra tremble decay exponentiel option réduire secousses", 1558),
    ("squash stretch saut scale 1,2 0,8 atterrissage", 1559),
    ("hitstop 50 ms timeScale 0 flash blanc particules", 1559),
    ("anim FSM Idle Run Jump conditions crossfade 0,1 s", 1560),
    ("state machine animation Animator transitions crossfade events frame 12", 1560),
    ("blend tree 2D 9 clips X Y interpolation fluide", 1561),
    ("déplacement relatif caméra 3D strafe fluide", 1561),
    ("IK 2 os pieds suivent le sol en pente raycast", 1562),
    ("mains sur poignée arme poids IK lissé 0-1", 1562),
    ("look-at tête regarde joueur SetLookAtPosition weight 1", 1563),
    ("spine IK torse penché hand IK ramasser objet", 1563),
    ("ragdoll mort 11 membres CharacterJoint animator off", 1564),
    ("explosion AddExplosionForce projette le corps", 1564),
    ("fracture Voronoi mur 12 morceaux rigidbody AddForce", 1565),
    ("cap 20 morceaux navmesh carving passage ouvert", 1565),
    ("FMOD Studio banques bus ducking intégration Unity", 1566),
    ("middleware audio FMOD Wwise banques bus ducking occlusion 32 voix", 1566),
    ("musique adaptative intensité 0-100 couches mixées", 1567),
    ("transition 2 s stinger alerte boss phase", 1567),
    ("SFX pitch aléatoire 0,9-1,1 volume ±3 dB jamais identique", 1568),
    ("pool 16 voix priorité caméra cooldown 100 ms", 1568),
    ("pipeline VO script CSV studio fichiers vo_id.wav FMOD", 1569),
    ("sous-titres synchronisés .srt 5 langues TTS secours marqué", 1569),
    ("HUD barre PV clignote rouge sous 30% minimap marqueurs", 1570),
    ("mode HUD minimal désactivable accessibilité 1575", 1570),
    ("menus navigables clavier tab entrée focus visible", 1571),
    ("manette A valider B retour test 100% sans souris", 1571),
    ("tutoriel contextuel toast au bon moment skippable", 1572),
    ("funnel analytics étapes où on perd les joueurs", 1572),
    ("streaming zones 100 m autour du joueur sans freeze", 1573),
    ("barre de chargement progression réelle pas bloquée 90%", 1573),
    ("preset qualité auto selon GPU sliders audio 4 bus live", 1574),
    ("remap contrôles sensibilité invert Y sauvegarde auto", 1574),
    ("filtres daltonisme 3 types jamais couleur seule icône forme", 1575),
    ("sous-titres SFX secousses réduites taille UI 200%", 1575),
    ("mods JSON data + API Lua sandbox /mods mod.json", 1576),
    ("liste mods on/off settings 1574 compatibilité version", 1576),
    ("console dev /give /tp /killall /timescale autocomplétion", 1577),
    ("absente en build release anti-triche 1543", 1577),
    ("SemVer majeur si save cassée patch notes 5 lignes", 1578),
    ("branches Steam beta previous rollback migration save 1503", 1578),
    ("SteamPipe upload build par branche beta Windows Linux", 1579),
    ("checklist validation Steam succès cloud manette lancement 1.0", 1579),
    ("leaderboard Steam top 100 mondial amis UploadScore", 1580),
    ("lobby Steam invitation ami cloud saves succès 1538", 1580),
    ("page store 10 captures ordonnées vidéo 15 s gameplay", 1581),
    ("prix 14,99 € tags 20 max wishlist 20k objectif", 1581),
    ("rewarded opt-in max 3/jour jamais forcée", 1582),
    ("IAP cosmétique uniquement pas pay-to-win conformité UE 2027", 1582),
    ("taux gacha affichés obligatoires légal 2027 pity 1528", 1583),
    ("interdit Belgique Pays-Bas sans licence mineurs 1587 exclus", 1583),
    ("consentement parental vérifiable moins de 16 ans 13 FR", 1584),
    ("analytics anonymisés mineurs pas de pub ciblée droit effacement", 1584),
    ("60 fps stables device réel Snapdragon 7 profilé", 1585),
    ("textures ASTC 0 alloc frame pool 1551 mode batterie", 1585),
    ("build IL2CPP ARM64 Addressables APK < 150 Mo ASTC", 1586),
    ("CI build auto symboles Crashlytics smoke test device", 1586),
    ("devkit console demandé 6-12 mois avant portage Switch PS5", 1587),
    ("certification TRC XR stabilité saves succès pas de crash", 1587),
    ("prix régionaux Steam Inde -70% Brésil -65% Japon -10%", 1588),
    ("soldes Steam 4 annuels -50% cooldown 30 jours règle sortie", 1588),
    ("répondre avis Steam négatifs 24h hotfix 48h jamais supprimé", 1589),
    ("devlog crise 1596 ratio avis surveiller remonter 70%", 1589),
    ("Addressables remote patch 5 Mo au lieu de 200 Mo cache hash", 1590),
    ("DLC Steam 1580 BoughtDLC débloque groupe contenu", 1590),
    ("playmode test tir PV -20 assertion CI 1593", 1591),
    ("test unitaire dégâts loot XP save round-trip 1503", 1591),
    ("CI build auto multi-OS upload beta Steam 1580", 1592),
    ("tests 1591 avant build check taille 150 Mo notif Discord", 1592),
    ("vertical slice 1 niveau poli loop complet 10 min", 1593),
    ("démo vidéo 3 min build jouable pitch éditeur 1594", 1593),
    ("pitch deck 12 slides démo live slice 1593 budget 1595", 1594),
    ("Q/R préparées relance 48 h build jouable éditeur", 1594),
    ("budget jeu indé équipe 4 18 mois calcul 2027", 1595),
    ("planning milestones démo 6 mois slice 12 mois aides CNC", 1595),
    ("Discord jeu salons devlog feedback bugs rôles modération 1548", 1596),
    ("devlog hebdo 3 GIF/semaine playtest mensuel 1598 newsletter", 1596),
    ("démo Steam Next Fest juin 2027 branche démo 30 min slice 1593", 1597),
    ("stand salon PGW 2 bornes RV presse éditeurs 1594 wishlist 1581", 1597),
    ("playtest 10 joueurs session 60 min SUS 1483 consentement RGPD 1584", 1598),
    ("synthèse 1 page priorités P0 P1 P2 backlog 1531", 1598),
    ("European Accessibility Act 2027 conformité jeu UE rapport publié", 1599),
    ("jouable clavier seul 1571 store section accessibilité 1581", 1599),
    ("vite 8 rolldown build 2,5 min à 40 s mesuré", 1600),
    ("vite 8 rolldown rust build rapide migration — exemple concret d'utilisation", 1600),
    ("htmx formulaire hx-post fragment serveur CSRF django", 1601),
    ("htmx UI dynamique sans javascript django-htmx fragments — exemple concret d'utilisation", 1601),
    ("react server components bundle client réduit mesuré", 1602),
    ("server actions mutation sans API + Suspense streaming", 1602),
    ("astro site 0 JS par défaut îles client:load", 1603),
    ("view transitions API entre pages MPA natif chrome", 1603),
    ("trpc procédure typée appelée comme fonction zod", 1604),
    ("tanstack start vs next.js comparatif 2027", 1604),
    ("qwik resumability TTI sous 1 s mesuré", 1605),
    ("lazy loading auto optimizer chunks par interaction", 1605),
    ("webgpu compute shader WGSL gain x10 vs CPU", 1606),
    ("three.js webgpu cross-browser fin 2025 safari", 1606),
    ("onnx runtime web webgpu inférence 50 ms image", 1607),
    ("modèle pytorch export onnx navigateur zéro serveur", 1607),
    ("rust compilé wasm32-wasip2 tourne avec wasmtime", 1608),
    ("component model WIT échange typé plugin wasm", 1608),
    ("tauri app 600 kB vs electron 150 Mo mesuré", 1609),
    ("PWA installable offline service worker notifs push", 1609),
    ("css :has() parent selon enfant sans JS", 1610),
    ("container queries @container composant responsive", 1610),
    ("app offline total synchro CRDT yjs replicache", 1611),
    ("2 appareils offline modifient puis merge sans conflit", 1611),
    ("cloudflare worker latence p95 50 ms 3 continents", 1612),
    ("KV Durable Objects D1 stockage edge 2027", 1612),
    ("CI front sous 3 min turbo remote cache mesurée", 1613),
    ("rolldown CI build parallèle cache turbo remote 2027 — exemple concret d'utilisation", 1613),
    ("migrer webpack vers vite loaders plugins mapping", 1614),
    ("migrer webpack vers vite guide loaders plugins alias env proxy — exemple concret d'utilisation", 1614),
    ("view transitions API meta same-origin MPA fade", 1615),
    ("view-transition-name héros morphing liste détail", 1615),
    ("astro islands client:load idle visible priorités", 1616),
    ("JS total somme des îles sous 50 kB vs 300 kB SPA", 1616),
    ("next nuxt sveltekit react router 7 matrice choix 2027", 1617),
    ("choisir meta-framework 2027 next.js nuxt sveltekit react router 7 comparatif — exemple concret d'utilisation", 1617),
    ("LCP 2,5 s INP 200 ms CLS 0,1 p75 RUM CrUX", 1618),
    ("core web vitals 2027 LCP INP CLS RUM real user monitoringCrUX — exemple concret d'utilisation", 1618),
    (":focus-visible clavier seul prefers-contrast 7:1", 1619),
    ("ARIA 1.3 composants custom tests NVDA VoiceOver", 1619),
    ("tokens JSON style dictionary génère CSS Swift Kotlin", 1620),
    ("design tokens multi-plateformes style dictionary tokens studio JSON CSS Swift Kotlin 2027 — exemple concret d'utilisation", 1620),
    ("registry officiel MCP serveurs vérifiés versions épinglées", 1621),
    ("gateway MCP audit scopes rate limit secrets env", 1621),
    ("agent card .well-known/agent.json publié découvert", 1622),
    ("A2A task délégation statut SSE artifacts reçus", 1622),
    ("matrice MCP vs A2A vs UCP choisir 2027", 1623),
    ("ACP absorbé par A2A ne pas démarrer dessus", 1623),
    ("webmcp navigateur agentique origin trial chrome 2026 navigator.modelContext outils page — exemple concret d'utilisation", 1624),
    ("webmcp navigateur agentique origin trial chrome 2026 navigator.modelContext outils page — variante 2 (taux de réussite mesuré)", 1624),
    ("agent card signé JWKS vérifié côté serveur", 1625),
    ("web bot auth requêtes signées anti-rejeu nonce timestamp", 1625),
    ("vérifier MCP A2A sous gouvernance AAIF Linux 2026", 1626),
    ("AAIF agentic AI foundation linux foundation gouvernance MCP A2A 2026 2027 lock-in — exemple concret d'utilisation", 1626),
    ("POC agent 4 semaines seuils go no-go chiffrés", 1627),
    ("Gartner 40% annulés : métriques précision coût tâche éviter", 1627),
    ("mandat UCP signé plafond marchand durée vérification", 1628),
    ("UCP universal commerce protocol mandat signé paiement agent plafond audit 2027 — exemple concret d'utilisation", 1628),
    ("langgraph graphe agents state checkpoints reprise crash", 1629),
    ("crewAI rôles tâches mémoire partagée monitoring trajectoires", 1629),
    ("rejouer trajectoires réelles golden set taux réussite 60% trouvé", 1630),
    ("métriques étapes coût escalade hallucinations rapport hebdo", 1630),
    ("gateway MCP auth agent scopes rate limit déployée", 1631),
    ("audit immuable chaque appel tool + blocage shell 403 alerte", 1631),
    ("retrieval top-k 8 passages dans contexte 1M anti lost-in-the-middle", 1632),
    ("question en début et fin de contexte éval précision", 1632),
    ("mistral OVH hébergement UE vs API US contrat DPA", 1633),
    ("modèles souverains européens Mistral OVH Scaleway hébergement UE conformité 2027 — exemple concret d'utilisation", 1633),
    ("matrice agent vertical vs généraliste risque volume coût", 1634),
    ("vertical juridique RAG distillation golden set conformité AI Act", 1634),
    ("budget 50€/jour agent alerte 80% kill switch 100% testé", 1635),
    ("contrôle coûts agents entreprise 2027 budget tokens par tâche alerte 80% kill switch auto — exemple concret d'utilisation", 1635),
    ("file approbation Slack boutons 1 clic routage criticité SLA", 1636),
    ("audit décisions + métriques taux délai moyen % refusés", 1636),
    ("Zep Graphiti ingestion entités relations épisodes Neo4j", 1637),
    ("requête liens + similarité + filtre temporel validée", 1637),
    ("agent génère pipeline S3 Iceberg testé en sandbox", 1638),
    ("comparaison old/new row counts schéma avant validation humaine", 1638),
    ("pipeline CI/CD agent Git CI golden canary prod monitoring", 1639),
    ("rollback auto si erreurs + kill switch budget testés", 1639),
    ("injection indirecte page web bloquée (data vs prompt)", 1640),
    ("sécurité agent IA production 2027 injection indirecte exfiltration mémoire empoisonnée — exemple concret d'utilisation", 1640),
    ("inventaire CBOM scanner TLS certificats PKI clés HSM", 1641),
    ("hybrid TLS X25519MLKEM testé compatibilité perf 2027", 1641),
    ("classer données par durée de vie PQC pour 10-30 ans", 1642),
    ("rétention réduite purge auto dossiers sensibles 2027", 1642),
    ("comptes sensibles d'abord passkeys 2 clés par user", 1643),
    ("dashboard adoption 50% connexions passkey 6 mois fallback mdp MFA", 1643),
    ("certificat X.509 unique par objet secure boot pas de mdp défaut", 1644),
    ("zero trust IoT edge objets connectés certificats X.509 SPIFFE micro-segmentation OTA signés 2027 — exemple concret d'utilisation", 1644),
    ("SBOM Syft + SLSA 3 cosigné chaque release CI", 1645),
    ("miroir interne quarantaine 48h nouvelles versions scan auto", 1645),
    ("code IA marqué PR revue obligatoire + SAST semgrep CI bloquant", 1646),
    ("rapport OWASP 2026 par release plan remédiation", 1646),
    ("hash sha256 modèle vérifié vs manifeste 1457 provenance officielle", 1647),
    ("scan pickle interdit sandbox 1475 + golden set 1395 avant prod", 1647),
    ("C2PA verify 1691 + 2 détecteurs + heuristiques sur vidéo suspecte", 1648),
    ("règle hors bande : rappel numéro connu avant virement 824 testée", 1648),
    ("NIS2 déclaration incident 24h procédure testée amendes 10M", 1649),
    ("DORA registre fournisseurs ICT RTO RPO tests résilience annuels", 1649),
    ("abstraction vault plus d'appel RSA direct dans le code", 1650),
    ("migration staging puis prod par vagues rollback prêt runbook", 1650),
    ("SOAR shuffle connecté SIEM playbooks phishing EDR actifs", 1651),
    ("SOAR SOC automation 2027 playbooks tines XSOAR shuffle tri auto alertes fatigue alertes — exemple concret d'utilisation", 1651),
    ("baseline UEBA 4 semaines anomalies z-score multi-dimensions", 1652),
    ("exfiltration lente 1 Go/jour détectée régression 30 jours", 1652),
    ("sauvegardes immuables Object Lock restauration testée mensuelle", 1653),
    ("playbook testé 1454 canaris UEBA décision payer non NIS2 24h", 1653),
    ("SPIRE déployé SVID certificat 1h renouvelé auto par workload", 1654),
    ("mTLS Envoy entre services révocation attestation retirée", 1654),
    ("DoH DoT activé DNSSEC validation réponses signées", 1655),
    ("Quad9 bloque domaine malware testé logs SIEM 1453", 1655),
    ("vault database user postgres temporaire TTL 1h révoqué auto", 1656),
    ("AWS STS rôle temporaire plus de clé longue durée audit loggé", 1656),
    ("DMARC p=reject BIMI VMC MTA-STS publiés monitoring dmarcian", 1657),
    ("sandbox pièces jointes Safe Links liens revérifiés au clic", 1657),
    ("semgrep SAST fail PR sur high + grype CVE 9 KEV bloquant", 1658),
    ("DAST zap staging + trufflehog secrets + SBOM cosign 1645", 1658),
    ("policy VDP publiée périmètre hors-périmètre safe harbor grille CVSS", 1659),
    ("bug bounty VDP divulgation responsable 2027 périmètre récompense CVSS délai réponse correction HackerOne — exemple concret d'utilisation", 1659),
    ("read_parquet s3:// direct httpfs credentials AWS", 1660),
    ("jointure CSV local + Postgres + API JSON une requête", 1660),
    ("ATTACH md: catalogue cloud partagé rôles lecture équipe", 1661),
    ("requête hybride local + cloud MotherDuck fonctionnelle", 1661),
    ("Iceberg v3 DELETE deletion vectors compaction efficace", 1662),
    ("row lineage provenance ligne audit RGPD effacement prouvé", 1662),
    ("matrice Delta Iceberg Hudi POC benchmark requête ingestion coût", 1663),
    ("Iceberg v3 multi-moteurs Spark Trino DuckDB Snowflake même table", 1663),
    ("dlt pipeline API REST paginée vers DuckDB 20 lignes Python", 1664),
    ("incremental last_value updated_at seul le delta chargé schéma auto", 1664),
    ("polars lazy scan_parquet streaming benchmark x10 vs pandas", 1665),
    ("jointure DuckDB via Arrow zéro copie polars 2027", 1665),
    ("stack dlt duckdb dbt superset déployé PME sans infra", 1666),
    ("dashboards superset KPIs en ligne CI 1592 seuils migration 1463", 1666),
    ("cartographie fusions 2026 Fivetran dbt IBM Confluent SAP Dremio MS Osmos", 1667),
    ("règle achat ouvert d'abord exit testé Data Act 1671 POC 6 mois", 1667),
    ("API Data Act produit connecté format ouvert OAuth2 doc 1406", 1668),
    ("consentement RGPD partage tiers scopé temporaire registre accès", 1668),
    ("egress gratuit 12 janv 2027 Data Act préavis 2 mois max contrat", 1669),
    ("exit préparé export ouvert 1663 test restauration nouveau 1672", 1669),
    ("inventaire lock-in par service + RTO/RPO DORA", 1670),
    ("restauration testée 2e fournisseur OVH 1688 RTO mesuré annuel 1454", 1670),
    ("LanceDB table vecteur+scalaires+image requête hybride filtre prix", 1671),
    ("lakehouse multimodal LanceDB lance images embeddings texte recherche hybride 2027 — exemple concret d'utilisation", 1671),
    ("RisingWave materialized view SQL streaming topic Kafka 1464", 1672),
    ("Flink stateful exactly-once latence p99 benchmark vs RisingWave", 1672),
    ("flow Kestra YAML trigger webhook fichier schedule exécuté", 1673),
    ("kestra orchestration YAML déclaratif UI visuelle triggers webhook schedule fichier 2027 — exemple concret d'utilisation", 1673),
    ("rill project init models SQL duckdb 1660 metrics YAML", 1674),
    ("rill deploy dashboard partagé équipe alerte 1417", 1674),
    ("GX expectations CI 1592 bloquant sur table critique", 1675),
    ("Monte Carlo alerte auto fraîcheur 6h + drift schéma 1461 Slack 1417", 1675),
    ("dbt Semantic Layer métrique CA YAML versionné Git API", 1676),
    ("Superset 1666 + Excel 264 connectés même définition CA plus d'écart", 1676),
    ("Hightouch sync auto segment warehouse vers Salesforce CRM 270", 1677),
    ("audience propension 353 dispo dans ads 747 email 357 fraîcheur 1675", 1677),
    ("CI 1592 bloque changement schéma cassant sans v2 période grâce", 1678),
    ("monitoring SLA prod 1675 alerte bilatérale dépréciation datée", 1678),
    ("matrice pgvector vs Qdrant Milvus Weaviate LanceDB 2027", 1679),
    ("POC 1M vecteurs filtres hybrides p99 latence mesurée Qdrant retenu", 1679),
    ("spans OTel par étape pipeline dlt dbt latence lignes/s", 1680),
    ("OpenTelemetry data pipelines 2027 traces spans extract load transform latence erreurs lineage 1466 — exemple concret d'utilisation", 1680),
    ("frise post-Omnibus 2026/1744 dates clés 2027 2028 annexe III I", 1681),
    ("AI Act calendrier 2026 2028 post-Omnibus 2026/1744 2 août 2026 2 déc 2026 2 déc 2027 2 août 2028 annexe III — exemple concret d'utilisation", 1681),
    ("art 53 doc technique + résumé public training data droit d'auteur 2026", 1682),
    ("risque systémique art 55 evals incident grave 24h AI Office testé", 1682),
    ("barème amendes AI Act 35M 7% 15M 3% 7,5M 1,5% appliqué au CA", 1683),
    ("vérification art 5 aucune pratique interdite documentée comité", 1683),
    ("plan conformité annexe III art 9-15 échéance 2 déc 2027", 1684),
    ("supervision humaine 329 logs 713 doc enregistrement base UE fait", 1684),
    ("matrice données sensibles niveau CADA 3-4 cible 2027", 1685),
    ("évaluation risque souveraineté marché public documentée contrat SLA exit 1671", 1685),
    ("vérifier niveau 3 Gaia-X au GXDCH (pas le logo) hors CLOUD Act", 1686),
    ("contrat niveau 3 + audit annuel + exit 1671 espace sectoriel rejoint", 1686),
    ("analyse juridique CLOUD Act AWS Souverain GmbH validée ou non", 1687),
    ("comparatif AWS souverain vs OVH Gaia-X N3 coût régions conformité ADR 88", 1687),
    ("cartographie chaîne souveraineté IA modèle données calcul GPU", 1688),
    ("stratégie 2030 documentée ADR 88 suivi CADA EUCS", 1688),
    ("niveau EUCS vérifié registre officiel exigé SLA contrat santé high", 1689),
    ("matrice sensibilité EUCS Gaia-X CADA + renouvellement annuel vérifié", 1689),
    ("badge IA affiché art 50 test utilisateurs 100% reconnaissent", 1690),
    ("watermarking C2PA 1691 détectable machine contenu généré délai 2 déc 2026", 1690),
    ("signature C2PA auto à la génération vérifiée (C2PA verify)", 1691),
    ("art 50(2) lisible + détectable conforme délai 2 déc 2026", 1691),
    ("panel 50 requêtes hebdo 5 moteurs IA taux citation dashboard 1540", 1692),
    ("GEO 2027 visibilité marque citations réponses LLM Perplexity ChatGPT Gemini mesurer taux de citation — exemple concret d'utilisation", 1692),
    ("réponse directe 50 mots intro + FAQ schema.org E-E-A-T sources 1436", 1693),
    ("taux de citation LLM avant/après mesuré panel 1692", 1693),
    ("bento grid 12 col cartes hiérarchisées verre blur 10px bordure fine", 1694),
    ("dark auto 1496 + haut contraste 1575 + contraste 4,5:1 validé 1484", 1694),
    ("micro-interactions 150-300 ms spring hover focus clic", 1695),
    ("scroll-driven 1610 + view transitions 1615 + reduced-motion 1495 testé", 1695),
    ("role=log aria-live=polite réponses annoncées NVDA VoiceOver 1619", 1696),
    ("clavier complet 1571 sans piège + contraste 1484 + bouton humain 251", 1696),
    ("SEQ QTSP qualifié liste UE horodatage qualifié archivage 10 ans 1376", 1697),
    ("EUDI Wallet eIDAS 2.0 identité UE 2027 déployé", 1697),
    ("dashboard top 20 skills domaines voies exit 0/1/2 anonymisé 1584", 1698),
    ("dashboard usage catalogue skills analytics routes top skills exit 0 1 2 misses récurrents par domaine — exemple concret d'utilisation", 1698),
    ("plateforme unifiée Monte Carlo ou Soda+OTel 1680 déployée", 1699),
    ("alerte avec trace 1680 + lignage 1466 + SLA 1678 corrélation testée 1454", 1699),
    ("IDP Backstage + golden path nouveau service en minutes DORA lead time < 4h", 1700),
    ("catalogue services owners doc TechDocs + Crossplane claims self-service", 1700),
    ("golden path service Node+Postgres en 5 min template Scaffolder", 1701),
    ("taux adoption 80% mesuré + dérogation documentée tickets -70%", 1701),
    ("backstage déployé catalogue auto scan repos GitHub owners statut", 1702),
    ("scaffolder template + techdocs + plugins pagerduty coûts métriques DAU", 1702),
    ("crossplane claim Database prod provisionné en minutes backups auto", 1703),
    ("XRD composite BDD+bucket+IAM + réconciliation drift corrigée gitops", 1703),
    ("argo cd sync auto self-heal déploiement par PR review 1401", 1704),
    ("rollback git revert 2 min + drift OutOfSync alerte Slack 1417", 1704),
    ("kyverno ClusterPolicy limits+readOnly+image signée warn puis enforce", 1705),
    ("kyverno OPA gatekeeper policies as code kubernetes 2027 resource limits readOnlyRootFilesystem images signées — exemple concret d'utilisation", 1705),
    ("métriques DORA 2027 lead time deploy frequency MTTR change failure rate mesurer livraison — exemple concret d'utilisation", 1706),
    ("lead time < 4h failure rate < 5% seuils atteints règle jamais individuel", 1706),
    ("4 types équipes stream-aligned platform enabling subsystem interactions XaaS", 1707),
    ("enquête charge cognitive baseline baisse visée revue annuelle", 1707),
    ("chat IDP 'service Node+Postgres' en LN → PR golden path en minutes", 1708),
    ("revue humaine 1401 + CI 1413 obligatoires jamais auto-merge métriques", 1708),
    ("TCO 3 ans self-host vs managé vs hybride avec coûts ETP licence", 1709),
    ("gains DORA mesurés tickets -70% point mort < 18 mois comité 775", 1709),
    ("comparatif Port Cortex Humanitec Backstage POC 4 semaines TCO 1709", 1710),
    ("décision ADR 88 : managé si équipe < 3 ETP sinon backstage custom", 1710),
    ("scorecards auto bronze argent or depuis APIs k8s CI Grafana 200 services", 1711),
    ("dashboard équipe objectif 0 bronze 6 mois jamais personnes", 1711),
    ("dashboard SPACE 5 dimensions par équipe sources combinées jamais 1 métrique", 1712),
    ("règle jamais individuel dans le règlement revue trimestrielle actions", 1712),
    ("devcontainer 1 commande BDD seedée + golden path 1ère PR commit J1", 1713),
    ("accès lecture puis progressifs buddy 234 métriques J1 semaine 2", 1713),
    ("devcontainer.json build CI 1413 tests dedans à chaque PR", 1714),
    ("codespaces même env cloud + local zéro install 'ça marche sur ma machine' fini", 1714),
    ("docs/ par repo + TechDocs publié recherche globale portail", 1715),
    ("check CI 1413 même PR code+doc + alerte péremption 12 mois 1711", 1715),
    ("kratix promise redis déployée sur 10 clusters workers statut remonté hub", 1716),
    ("state store S3 + drift resync auto + gitops 1704 review 1401", 1716),
    ("roadmap v1 v2 v3 par trimestre livrables métriques DORA NPS adoption", 1717),
    ("revue trimestrielle devs clients NPS changelog mensuel 1578 démo 1418", 1717),
    ("SSO+passkeys portail mTLS SPIFFE services secrets vault ESO kyverno OIDC CI", 1718),
    ("zero trust plateforme interne IDP 2027 SSO passkeys mTLS SPIFFE secrets vault policies kyverno audit CI OIDC — exemple concret d'utilisation", 1718),
    ("changelog mensuel 1578 démo trimestrielle 1418 canal #platform FAQ 119", 1719),
    ("roadmap publique 1717 NPS 2x/an 1712 métriques adoption 1698 ciblées", 1719),
    ("uname -r 5.15+ verifier + eBPF zero-instrumentation Pixie Beyla déployé", 1720),
    ("eBPF 2027 programmer noyau linux sandboxé sans modifier kernel Cilium Falco bpftrace Pixie Beyla kernel 5.8+ — exemple concret d'utilisation", 1720),
    ("cilium install kube-proxy remplacé status OK pod test connectivité", 1721),
    ("CiliumNetworkPolicy L7 + Hubble service map + benchmark +30-40% débit", 1721),
    ("hubble enable UI CLI service map flux L3-L7 identités workloads", 1722),
    ("filtres HTTP method path DNS Kafka + métriques prometheus grafana 1416 alertes 1417", 1722),
    ("falco eBPF daemonset shell conteneur alerte 1s MTTR < 60s SIEM 1453", 1723),
    ("règles custom /etc/shadow + faux positifs < 5% playbook SOAR isolation 1651", 1723),
    ("beyla daemonset eBPF app legacy java traces OTel 1680 zéro code modifié", 1724),
    ("overhead < 5% CPU + pixie service map requêtes SQL live k8s", 1724),
    ("tetragon TracingPolicy bloque exec /tmp + egress deny SAUF allowlist testé log puis enforce", 1725),
    ("tetragon cilium eBPF enforcement policies blocage runtime 2027 TracingPolicy exec write network kill — exemple concret d'utilisation", 1725),
    ("bpftrace one-liner top syscalls par process + latence I/O hist timeout 30", 1726),
    ("règle lecture seule filtre pid overhead < 5% jamais permanent en prod", 1726),
    ("cilium service mesh mTLS auto L7 retries sans sidecar activé", 1727),
    ("benchmark -50% ressources -30% latence vs istio sidecars hubble 1722", 1727),
    ("lab kind+cilium CCAE : NetworkPolicy L7 hubble mesh tetragon", 1728),
    ("commandes debug cilium bpf policy list service list status examen proctored 2h", 1728),
    ("stack eBPF standard 2-3 outils anti-fragmentation documentée 1715", 1729),
    ("POC overhead < 5% CPU + TCO 3 ans open vs enterprise 1709 + CCAE 1728", 1729),
    ("katran VIP + maglev + health checks + DSR déployé benchmark vs haproxy x5-10", 1730),
    ("katran load balancer L4 eBPF XDP Meta 2027 maglev consistent hashing DSR milliards requêtes jour — exemple concret d'utilisation", 1730),
    ("bpftrace latence read par process top + par device + top fichiers ouverts", 1731),
    ("eBPF monitoring I/O disque 2027 latence par device par process top fichiers lus bpftrace block layer — exemple concret d'utilisation", 1731),
    ("cilium identité pod policies par labels stables malgré IPs + egress toFQDNs stripe", 1732),
    ("eBPF isolation réseau conteneurs 2027 identité pod policies L7 egress control DNS-aware micro-segmentation Cilium — exemple concret d'utilisation", 1732),
    ("XDP eBPF drop blacklist dynamique SIEM 1453 débit Gbps mesuré 0 faux positif", 1733),
    ("architecture XDP L3-L4 + WAF L7 1451 + CSP 1452 documentée", 1733),
    ("matrice eBPF vs module (vérifié/dynamique vs accès total/panic) règle écrite", 1734),
    ("eBPF vs module kernel choisir 2027 sandboxé vérifié dynamique vs accès total perf panic noyau LKML — exemple concret d'utilisation", 1734),
    ("matrice outils IA 2027 Cursor Claude Code Copilot Devin OpenCode Jules + profils", 1735),
    ("POC 2 sem +20-30% productivité mesuré politique sécurité 1736 appliquée", 1735),
    ("politique outil IA par classe de code publiée appliquée (gratuit/interne/HIPAA/self-host)", 1736),
    ("PR IA taguées revue 1401 + SAST 1658 + SCA 1645 bloquants 0 fuite DLP 1440", 1736),
    ("claude code plan mode migration express fastify 50 fichiers diffs validés 1401", 1737),
    ("/loop cron audit deps lundi 9h + Analytics API dashboard équipe 1698", 1737),
    ("issue bien cadrée → Devin/Codex PR sandbox testée en heures revue 1401 SAST 1658", 1738),
    ("taux merge 70% direct temps issue→PR mesuré pas d'archi critique 1736", 1738),
    ("dashboard gain DORA avant/après Analytics API 1737 % code IA bugs 256 SAST 1658 SPACE 1712", 1739),
    ("ROI coût vs gain 1709 décision ADR 88 jamais individuel règle écrite", 1739),
    ("cursor indexation codebase chat @fichier #symbole réponses sourcées", 1740),
    ("composer multi-fichiers 10 fichiers plan+diffs validés 1401 tests 67", 1740),
    ("copilot business sièges crédits juin 2026 SSO 1450 policies rétention filtres 1177", 1741),
    ("revue PR auto 821 + SAST 1658 + dashboard usage 1698 DORA 1706", 1741),
    ("opencode + modèle local ollama 1472 code jamais envoyé (vérifié réseau)", 1742),
    ("jules 15 tâches/jour PR github ouverte revue 1401 règle cloud=public 1736", 1742),
    ("aider CLI /add /edit multi-fichiers commit auto 68 message propre", 1743),
    ("cline VSCode plan puis act diffs validés + modèle local 1633 testé 1736", 1743),
    ("sourcegraph indexé recherche AST tous appels ancienne API cross-repo liste exacte", 1744),
    ("cody @repo @file chat contextuel + self-host 1633 code interne jamais envoyé", 1744),
    ("lovable chat → app full-stack supabase déployée URL testée 5 users 1483", 1745),
    ("code exporté github revue 1401 + SAST 1658 avant prod pas de lock-in", 1745),
    ("docstrings module générées IA relues 1401 vs code hallucination 1155 corrigée", 1746),
    ("changelog auto commits 68 + doc API 87 testée 822 publiée 1406 + check CI 1715", 1746),
    ("tests IA générés passent 67 coverage 80% CI 1658 + mutation stryker mutants tués", 1747),
    ("revue 1401 tests couvrent vraiment la logique pas des tests qui passent toujours", 1747),
    ("plan dette top10 1 module/semaine tests 1747 avant/après couverture 1658", 1748),
    ("god object 3000 lignes découpé plan 1737 petits lots 1405 revue 1401 0 bug 256", 1748),
    ("charte publiée frontière IA/humain 3 garde-fous 1401 1747 1658 obligatoires", 1749),
    ("vibe coding responsable 2027 frontière IA/humain archi 88 sécurité 1646 revue 1401 tests 1747 SAST 1658 responsabilité humaine — exemple concret d'utilisation", 1749),
    ("spans gen_ai.* modèle tokens tool calls sur appels LangChain + raw API uniformes", 1750),
    ("dashboard latence coût erreurs par modèle grafana 1416 + portabilité backend testée", 1750),
    ("SLI TTFT p95 500ms p99 10s erreurs qualité coût SLO 99,5% budget 3,6h/mois calcul", 1751),
    ("SLO feature LLM 2027 latence p99 TTFT qualité hallucinations coût requête escalade HITL budget erreur 99,5% 3,6h/mois — exemple concret d'utilisation", 1751),
    ("audit cardinalité labels sans ID 1440 séries/métrique réduites + sampling head 10% tail erreurs", 1752),
    ("rétention 7j chaud 90j S3 1469 + stockage 0,50$/Go 1699 + budget équipe 1092 alerte 1417", 1752),
    ("golden signals service + RED endpoint + USE ressource dashboards 1416 alertes 1417", 1753),
    ("règle signaux de base d'abord custom métier 351 ensuite documentée", 1753),
    ("repo observability/ alertes YAML dashboards JSON SLO 351 CI 1413 promtool + PR 1401", 1754),
    ("observability as code 2027 dashboards alertes SLO en Git JSON Terraform grafana CRD CI 1413 revue PR 1401 — exemple concret d'utilisation", 1754),
    ("RCA < 60s corrélation 4 signaux preuves deploy+OOM+5xx MTTR -50% mesuré", 1755),
    ("HITL 1636 validation humaine avant action + % RCA correctes > 80% feedback ML 1395", 1755),
    ("web-vitals RUM LCP INP CLS p75 par page navigateur zone analytics 1540 anonymisé 1440", 1756),
    ("alertes 1417 INP > 200ms + corrélation conversion 1698 + convergence labo/RUM < 20%", 1756),
    ("règles burn rate 14x/1h urgent 6x/6h ticket 1x/3j info alertmanager 1417 déployées", 1757),
    ("burn rate SLO 2027 alertes intelligentes budget erreur 14x 1h page urgente 6x 6h ticket 1x 3j info anti fatigue 1417 — exemple concret d'utilisation", 1757),
    ("matrice SEV SLA rôles IC 1161 comm 235 scribe war room 15 min testé 1454", 1758),
    ("post-mortem blameless 89 5j 3 actions suivies 100% MTTR par SEV mesuré", 1758),
    ("expérience pod-kill blast radius 5% abort auto burn SLO 1757 hypothèse validée ou faille fix", 1759),
    ("chaos engineering 2027 Litmus Chaos Mesh Gremlin tuer pod latence réseau panne AZ hypothesis blast radius 5% abort auto SLO 1751 — exemple concret d'utilisation", 1759),
    ("SLO 99,5 % = 3,6 h/mois par parcours critique + politique error budget ecrite + revue mensuelle", 1760),
    ("deux niveaux SLO interne 99,9 % et externe 99,5 % avec actions de gel documentées", 1760),
    ("alertes SLO burn rate multi-window sans alerte CPU brute + groupement dedoublonnage", 1761),
    ("matrice routage equipe + escalade 15 min sans ack + baisse du nombre d'alertes/semaine", 1761),
    ("traceparent propage de bout en bout + tail-based sampling garde 100 % traces lentes/erreurs", 1762),
    ("tracing distribué OpenTelemetry W3C traceparent head-based tail-based sampling 2027 — exemple concret d'utilisation", 1762),
    ("audit labels + suppression label url brut remplace par route normalisee + alerte 10 000 series", 1763),
    ("cout stockage metriques stabilise apres bucketification des labels haute cardinalite", 1763),
    ("runbook alerte CrashLoopBackOff avec etapes commandes + lien depuis l'alerte 1761", 1764),
    ("auto-remediation scale +2 replicas sur file > 1000 messages avec log audit + escalade 30 min", 1764),
    ("spans gen_ai.tool.call sur chaque MCP tool + detection boucle 20x search_docs + cout tokens par requete", 1765),
    ("plateforme self-host Langfuse vs proxy Helicone choisie selon donnees sensibles", 1765),
    ("dashboard comex SLO + error budget + incidents SEV + decision gel features documentee", 1766),
    ("drill-down panneau p99 -> alerte 1761 -> trace span 1762 -> log en 3 clics", 1766),
    ("attributs gen_ai.usage.input_tokens/output_tokens + cout 0,12 $/conversation calcule", 1767),
    ("tracing LLM tokens cout par requete gen_ai.usage OpenTelemetry cost attribution dollars 2027 — exemple concret d'utilisation", 1767),
    ("postmortem blameless publie sous 72 h avec chronologie + 5 pourquoi cause racine systeme", 1768),
    ("5 actions correctives avec responsable echeance backlog + revue J+30 avancement", 1768),
    ("game day panne AZ primaire : failover 4 min + communication crise 10 min + rapport ecarts runbooks", 1769),
    ("prochain game day planifie T4 fuite de secrets + corrections runbooks 1764 appliquees", 1769),
    ("bilan 2027 : plus experimental dec 2025, 496 fichiers 120 019 SLOC kernel 7.3 x24,6 vs 6.1", 1770),
    ("Rust for Linux noyau 2027 bilan plus experimental 496 fichiers 120 000 SLOC kernel 7.3 — exemple concret d'utilisation", 1770),
    ("objet embarque dans struct C avec list_head initialise via pinned_init! champ Pin", 1771),
    ("pinned-init Pin adresse fixe mémoire kernel Rust 6.4 pointeurs intrusifs listes chainees 2027 — exemple concret d'utilisation", 1771),
    ("cartographie C/Rust Binder + pattern nouveau code Rust interfaces C stables", 1772),
    ("tests CTS Android OK avec driver Rust + objets IPC pinnes 1771", 1772),
    ("driver NVMe Rust + audit allocations fast path zero-alloc + benchmark p99 ecart < 5 % vs C", 1773),
    ("decision nouveau SSD en Rust validee sur kernel 7.x avec profil allocation maitrise", 1773),
    ("driver GPU M3 en Rust suivant Asahi + interface DRM C stable + tests materiel M3 OK", 1774),
    ("benchmark perfs documentees vs reference + reset GPU apres erreur teste", 1774),
    ("matrice Nova vs nouveau selon materiel Blackwell+ vs ancien + etat avancement Nova documente", 1775),
    ("benchmark Nova vs nouveau + plan rollback sur nouveau (C) si regression", 1775),
    ("initiative rewrite C refusee + nouveau driver GPU accepte en Rust (ajout) ADR documentee", 1776),
    ("argument stagnation mainteneurs + turnover contributeurs Rust quantifie", 1776),
    ("RFC design nouveau envoyee sur rust-for-linux avant code + patch 40 lignes 3 tests KUnit", 1777),
    ("clippy -D warnings + rustfmt + git send-email cover letter sur la ML revue par Ojeda", 1777),
    ("argument 70 % CVE memoire noyau cite + garanties Rust safe listees (UAF overflow race null)", 1778),
    ("decision driver parsing reseau en Rust avec blocs unsafe audites + surface attaque documentee", 1778),
    ("plan 2027-2030 : phase 1 nettoyage API C 2027-28 + phase 2 drivers Rust defaut 2028-30 + jalons SLOC/contributeurs", 1779),
    ("revue annuelle mainteneurs C + tree rust-for-linux 1777 + anti-stagnation objectif recrutement", 1779),
    ("fiche PG18 6 nouveautes avec skills 1781-1786 + PG19 RC1 15 oct 2026 teste en recette", 1780),
    ("montee PG16 vers PG18 planifiee via 1789 avec AIO et uuidv7 retenus", 1780),
    ("io_method=io_uring active + fallback sync + seq scan 200 Go 45 s vers 15 s mesure EXPLAIN ANALYZE", 1781),
    ("PostgreSQL 18 AIO io_uring io_method async I/O scans 3x plus rapide shared_buffers 2027 — exemple concret d'utilisation", 1781),
    ("table events PK uuidv7() : index 8 Go vs 22 Go v4 + inserts 2x plus rapides + splits /5 pgstattuple", 1782),
    ("regle v7 defaut v4 si timestamp sensible documentee + migration uuidv4 existante via 1789", 1782),
    ("EXPLAIN skip scan pris sur index (categorie, date) avec 12 categories + seq scan avant", 1783),
    ("index sur date seul supprime + 30 % d'index en moins + n_distinct seuil documente", 1783),
    ("prix_ttc VIRTUAL PG18 : SELECT OK + taille table identique 0 octet stockage vs STORED 8 oct/ligne", 1784),
    ("regle VIRTUAL derive simple vs STORED expression lourde lue souvent documentee", 1784),
    ("table tarifs PK (produit_id, periode) WITHOUT OVERLAPS + chevauchement refuse par PG", 1785),
    ("requete prix au 15 mars 2027 = 10 EUR via periode @> date + update historise auto", 1785),
    ("pg_hba oauth issuer/jwks/audience/claim=role + connexion JWT OK avant exp et KO apres exp", 1786),
    ("mapping claim role vers app_readonly documente + rotation cles JWKS geree", 1786),
    ("pg_upgrade --check + --swap downtime 8 s mesure + pg_statistic conserve (pas d'ANALYZE massif)", 1787),
    ("rollback ancien repertoire pret et teste selon plan 1789", 1787),
    ("scram-sha-256 par defaut + md5 refuse + TLSv1.3 min + hostssl uniquement dans pg_hba", 1788),
    ("RLS orders policy tenant_id testee (count tenant 42 uniquement) + pg_audit log connexions/DDL actif", 1788),
    ("plan 4 etapes : check + recette pgbench 2000 req/s p99 identique + swap 8 s + rollback 7 jours teste", 1789),
    ("rapport recette OK + migration prod fenetre nuit + ancien cluster PG16 garde 7 jours", 1789),
    ("CBOM 340 certificats 80 % RSA-2048 + VPN/SSH/HSM inventories classes par risque", 1790),
    ("plan jalons 2027 inventaire -> 2030 haut risque -> 2035 complet + HNDL documente", 1790),
    ("nginx OpenSSL 3.5 ssl_ecdh_curve X25519MLKEM768 + s_client -groups prouve handshake hybride", 1791),
    ("fallback X25519 pour vieux clients + taux fallback 3 % mesure + overhead handshake documente", 1791),
    ("cle ML-DSA-65 generee (openssl genpkey) + certificat X.509 hybride ECDSA+ML-DSA emis et verifie", 1792),
    ("diversification SLH-DSA secours documentee + regle jamais PQC seul (hybride ANSSI)", 1792),
    ("cargo build --target wasm32-wasip2 OK + composant WIT Rust+Python compose et execute par Wasmtime", 1793),
    ("choix runtime documente : Wasmtime perf / WasmEdge edge / wazero embarque Go", 1793),
    ("wasmtime --dir=./workspace --env=API_KEY plugin.wasm + lecture /etc/shadow refusee (deny-by-default)", 1794),
    ("cold start 1 ms vs 500 ms conteneur mesure + comparaison conteneur si OS complet requis", 1794),
    ("audit RGESN 79 criteres + plan 10 actions priorisees (sobriete fonctionnelle, AVIF, lazy-load)", 1795),
    ("EcoIndex 72 -> 88 apres refonte + hebergement region bas carbone choisi", 1795),
    ("Scaphandre deploye : 180 MWh/an + facteur France = 9 t CO2 + Boavizta 120 t fabrication", 1796),
    ("dashboard empreinte totale 132 t CO2eq + volet CSRD scope 3 cat. 11 renseigne", 1796),
    ("Workers deploye Sydney PoP + D1 edge : latence Melbourne 800 ms -> 12 ms mesuree RUM 1756", 1797),
    ("anti-pattern documente : edge appelant origine mono-region = 50-200 ms, a eviter", 1797),
    ("dashboard DORA (lead time 4 h, MTTR -40 %) + SPACE (eNPS +12, revue PR -30 %) trimestriel", 1798),
    ("harness engineering note : flow ameliore/degrade documente + jamais de metrique individuelle", 1798),
    ("radar interne a jour : eBPF 1720 Assess->Adopt + Wasm 1793 Trial->Adopt + framework Y Hold traces", 1799),
    ("revue semestrielle compte-rendu avec responsables par blip + justification ecrite", 1799),
    ("LiteLLM déployé endpoint unique OpenAI + clés virtuelles équipe budget 500 $/mois + fallback 429 teste", 1800),
    ("cache sémantique mesuré -31 % tokens + dashboard coût/équipe + spend limit hard bloque au plafond", 1800),
    ("HTTPRoute host api.example.com path /v1 backend api:8080 + curl 200 + Gateway TLS OK", 1801),
    ("migration ingress-nginx vers Gateway API : inventaire Ingress convertis + rollback 1 release documente", 1801),
    ("ResourceClaim preferences H100 fallback A100 2 devices + allocation OK sur gpu-worker-01", 1802),
    ("DeviceTaintRule maintenance GPU + preemption propre documentee + health status surveille", 1802),
    ("VPA Auto + InPlacePodVerticalScaling : pod resizé 2 CPU vers 4 CPU sans restart (uptime conservé)", 1803),
    ("InPlacePodVerticalScaling resize pod à chaud VPA sans restart stateful k8s GA 1.35 — exemple concret d'utilisation", 1803),
    ("Workload minAvailable=8 PodGroup : 8 pods démarrent ensemble via DRA ou job en queue (0 partiel)", 1804),
    ("gang scheduling PodGroup Workload scheduling.k8s.io all-or-nothing job ML distribué training multi-GPU — exemple concret d'utilisation", 1804),
    ("PDB minAvailable=2 sur API + preemption batch-low : 0 pod API tué, victimes = pods batch", 1805),
    ("workload-aware preemption topology-aware scheduling PDB priorité pods k8s 1.36 — exemple concret d'utilisation", 1805),
    ("dashboard PSI cpu/mem/io par nœud + alerte some avg10 > 5 % testee", 1806),
    ("diagnostic : PSI cpu 12 % + 3 pods throttlés CFS -> limits augmentés ou nœud ajouté 1810", 1806),
    ("volume OCI ref registry/config@sha256:abc monte read-only + contenu vérifié", 1807),
    ("cosign verify sur l'artifact + re-pull au restart du pod documente (digest pas tag)", 1807),
    ("policy CEL label team injecté à la création du pod (mutation) verifiee en dry-run puis prod", 1808),
    ("image non signée bloquée à l'admission (failurePolicy=Fail) + métriques apiserver", 1808),
    ("pod wasm via kwasm RuntimeClass : cold start 1 ms mesuré + isolation capabilities 1794 verifiee", 1809),
    ("SpinKube wasmCloud déployé + policies 1705/1808 appliquées + benchmark vs conteneur", 1809),
    ("NodePool provisionne 5 nœuds spot en 40 s pour 40 pods pending + consolidation à 6h (nœuds supprimés, PDB 1805 respectés)", 1810),
    ("dashboard coût/nœud + temps scheduling pod->nœud + mix spot/on-demand documente", 1810),
    ("ADR décision OpenTofu vs Terraform avec critères licence/HCP/encryption documentés", 1811),
    ("projet greenfield : opentofu 1.13 installé + state compatible + revue 12 mois planifiee", 1811),
    ("state chiffré AES-256-GCM local + S3 SSE-KMS distant, contenu illisible sans KMS", 1812),
    ("migration state existant via tofu init -reconfigure OK + rotation clé KMS documentee", 1812),
    ("ephemeral aws_secretsmanager_secret_version : tofu state show + plan sans le password (preuve)", 1813),
    ("resource postgresql_grant créée avec le secret éphémère + contrat re-lu à chaque apply documente", 1813),
    ("workspace prod protect=true : tofu destroy BDD bloqué ; workspace dev : destroy OK", 1814),
    ("lifecycle enabled=var.x ressource zero-or-one creee/supprimee selon la variable", 1814),
    ("provider for_each 3 régions : 3 providers instanciés, un seul code module", 1815),
    ("backend bucket state-dev/state-prod selon var.env (early evaluation) + tofu plan -exclude=module.prod testé", 1815),
    ("Harbor miroir + module interne publié tag 1.2.0 signé cosign + tofu login et source interne OK", 1816),
    ("air-gapped : providers miroirs taggés consommés sans accès public", 1816),
    ("Stack 3 composants 2 envs : plan global ordonné (vpc->eks->app) + apply OK sur dev et prod", 1817),
    ("Terraform Stacks HCP Terraform composants déploiements orchestration multi-env GA exclusivité HCP — exemple concret d'utilisation", 1817),
    ("terraform list aws_s3_bucket : 34 réels vs 30 dans le state + 4 orphelins identifiés", 1818),
    ("blocs import générés et appliqués + audit hebdo CI 1413 planifié (drift 1820)", 1818),
    ("tofu init sur state existant + tofu plan = 0 changement + CI migrée (terraform->tofu)", 1819),
    ("state encryption activé après coup sur env test (pas pendant la migration)", 1819),
    ("CI hebdo drift : plan -detailed-exitcode exit 2 detecté + ticket auto + query 1818", 1820),
    ("conftest deny S3 publique/sans tag en PR (check rouge) + 0 ressource non conforme en prod", 1820),
    ("step CI syft cyclonedx-json + spdx-json validés (schéma 1.7, CISA 2026 fields) + cosign attest par digest", 1821),
    ("SBOM Syft Trivy CycloneDX 1.7 SPDX 3.0.1 CISA 2026 Minimum Elements CI build image digest — exemple concret d'utilisation", 1821),
    ("cosign sign --yes keyless en CI (Fulcio+Rekor) + cosign verify identity workflow main OK", 1822),
    ("fork PR : signature invalide (identity différente) + air-gapped trusted-root testé", 1822),
    ("slsa-github-generator v2 en release : attestation in-toto emise (subject digest + predicate repo/commit)", 1823),
    ("cosign verify-attestation OK en CI + policy admission 1824 exige provenance du bon repo", 1823),
    ("Kyverno verifyImages Audit : 3 violations detectées et nettoyées puis Block actif : 0 image non signée", 1824),
    ("Sigstore Policy Controller testé en greenfield + exception break-glass documentee", 1824),
    ("CDXA bom-1.7 généré + claim SSDF signé (cosign attest-blob) + BOM-Link vers SBOM digest", 1825),
    ("vérification air-gapped : cosign verify-blob --trusted-root OK sans réseau", 1825),
    ("grype --vex : 412 -> 22 (390 not_affected VEX) + 1 KEV = P0 alerte 1761 + patch 24 h", 1826),
    ("job nocturne re-scan SBOM attesté cosign verify-attestation + grype sur image prod", 1826),
    ("PR avec paquet malveillant (install script exfil) : Socket bloque le merge en CI", 1827),
    ("Scorecard dep critique < 5 : revue sécurité obligatoire documentee + GUAC query impact CVE OK", 1827),
    ("image chainguard 8 Mo vs debian 180 Mo + docker exec sh échoue (pas de shell) + SBOM inclus", 1828),
    ("images distroless Chainguard wolfi apko 2-10 Mo pas de shell signées Sigstore SBOM surface attaque CVE — exemple concret d'utilisation", 1828),
    ("OIDC GitHub->AWS : 0 secret statique, rôle assumé token 1h testé", 1829),
    ("Tekton Chains signe l'image du build (cosign verify OK) + actions pinnées SHA (grep uses:)", 1829),
    ("release avec package SBOM+VEX+CDXA signé livré automatiquement + vérifiable offline (trusted-root)", 1830),
    ("security.txt VDP publié + matrice CRA (obligations/échéances/responsables) documentée", 1830),
    ("contrat YAML v2 (schéma+sémantique+SLA) publié + dbt test échoue sur violation (colonne manquante) + alerte 1761", 1831),
    ("contrat exposé via MCP 1765 + compatibilité backward v1->v2 documentee (1840)", 1831),
    ("dbt natif OpenLineage : events reçus dans Marquez avec inputs/outputs du modèle stg_orders", 1832),
    ("Airflow + Dagster + Snowflake instrumentés : graphe complet column-level 1833 vérifié", 1832),
    ("Marquez déployé (Postgres+API+UI) + events dbt reçus, graphe column-level visible", 1833),
    ("runbook incident testé : anomalie -> colonne source identifiée -> 12 consommateurs listés + owner notifié", 1833),
    ("schema.yml contrat data_type numeric sur amount + dbt build échoue si string (violation) + CI 1413 bloque", 1834),
    ("tests singular métier (ex. remise entre 0 et 30 %) + dbt docs generate avec lineage 1832 OK", 1834),
    ("4 SLA mesurés (fraîcheur/volume/schéma/distribution) + alerte fraîcheur 45 min testée via 1761", 1835),
    ("SLA data quality fraîcheur volume schéma distribution Monte Carlo Soda Great Expectations dbt tests alerte dépassement — exemple concret d'utilisation", 1835),
    ("architecture documentée : Marquez lineage + OpenMetadata gouvernance déployés et connectés via OpenLineage", 1836),
    ("migration Amundsen -> OpenMetadata : glossaire + owners réimportés et vérifiés", 1836),
    ("3 domaines avec data products publiés (contrat+SLA+catalog) + plateforme self-serve 1700 opérationnelle", 1837),
    ("gouvernance fédérée PII 1839 : standards communs appliqués, 0 fuite de PII en audit", 1837),
    ("métrique 'revenu net' définie dans dbt Semantic Layer + testée (réconciliation faits) + exposée via MCP 1765", 1838),
    ("dashboard 1766 + agent IA MCP retournent le même chiffre (4,2 M€)", 1838),
    ("scan PII + tags dans le catalog 1095/1836 + ABAC équipe/région + RLS owner_id=1788 vérifié", 1839),
    ("registre RGPD à jour + DPIA nouveau projet + rétention/legal hold documentés", 1839),
    ("repo contrats IDL (protobuf) versionné semver + buf breaking en CI bloque v2 sans bump majeur", 1840),
    ("ajout champ optionnel = v1.3.0 accepté + consommateurs notifiés via catalog 1095", 1840),
    ("5 rails déployés : input bloque injection, retrieval filtre RAG, execution gating tools, output masque PII 1846", 1841),
    ("latence +80 ms (sync ciblé) + taux de blocage par rail dans dashboard 1766", 1841),
    ("flow Colang déployé : hors-sujet -> refus poli ; jailbreak bloqué rail input", 1842),
    ("200 attaques garak 1847 : 0 succès + télémétrie désactivée + rate limiting actif", 1842),
    ("validator json_schema sur sortie LLM : texte libre -> rework -> JSON valide, 0 invalide livré", 1843),
    ("latence +12 ms (pas de LLM judge) + redaction PII validator 1846 testée", 1843),
    ("Llama Guard 8B déployé vLLM GPU : verdict unsafe sur prompt injection -> blocage rail 1841", 1844),
    ("Llama Guard 3 Meta classifieur judge self-hosté 1B 8B open weights labels sécurité input output AILuminate local GPU confidentialité — exemple concret d'utilisation", 1844),
    ("Prompt Guard bloque injection directe + indirecte (email RAG) en rail input 1841", 1845),
    ("canary system prompt non divulgué + tools least-privilege 1850 + confirmation 1433 sur action sensible", 1845),
    ("Presidio FR : IBAN/email/nom détectés + anonymisés [IBAN] sur rail output 1841", 1846),
    ("Presidio Microsoft détection PII redaction anonymizer NER regex multilingue email téléphone IBAN CB masque rails LLM RAG — exemple concret d'utilisation", 1846),
    ("promptfoo redteam 500 attaques en CI : 0,4 % succès < 1 % -> gate vert + rapport archivé", 1847),
    ("attaque passée en prod réinjectée dans le dataset + garak scan (fuite system prompt) OK", 1847),
    ("dataset 300 cas + gate CI (régression fidélité -5 % -> blocage) + changement modèle v1->v2 testé", 1848),
    ("monitoring prod Langfuse : 3 cas ratés -> dataset enrichi + dashboard 1766 hebdo", 1848),
    ("matrice OWASP 2025 complète (10 risques -> mitigation -> owner -> statut) + LLM06 corrigé via 1850", 1849),
    ("revue trimestrielle planifiée + LLM10 spend limit 1800 testé", 1849),
    ("agent réduit à 3 tools read-only + HITL 1433 sur action > 1000 € + sandbox wasm 1794 actif", 1850),
    ("audit 1765 : 100 % des tool calls loggés avec args + résultat ; 0 action destructive auto", 1850),
    ("etcd chiffré KMS + 200 secrets réencryptés (kubectl replace) + lecture fichier etcd illisible", 1851),
    ("RBAC : SA lambda ne peut pas get secrets (403) + audit log des accès secrets actif", 1851),
    ("Vault HA 3 nœuds Raft + auto-unseal KMS + 1 nœud down : service OK", 1852),
    ("auth kubernetes : SA app lit son secret, SA autre = 403 + audit log requêtable", 1852),
    ("role database Vault : user créé TTL 24 h via database/creds/app + supprimé auto à expiration", 1853),
    ("ESO 1854 sync le cred k8s + rotation 1855 + audit Vault des délivrances requêtable", 1853),
    ("ESO helm installé + ClusterSecretStore vault + ExternalSecret api -> Secret k8s créé et sync à refreshInterval 1h testé", 1854),
    ("changement côté Vault -> Secret k8s mis à jour + Reloader 1855 restart pod (0 downtime)", 1854),
    ("Vault TTL 24 h + ESO 1h + Reloader : 12 pods rolling restart sans downtime (métriques 1416) + nouveau secret actif", 1855),
    ("mode volume : kubelet propage en ~1 min sans restart (vérifié sur 1 pod)", 1855),
    ("kubeseal chiffre un secret (SealedSecret committable, contenu chiffré) + controller le déchiffre in-cluster", 1856),
    ("clé privée backupée dans Vault 1852 + rotation : kubeseal --re-encrypt testé", 1856),
    ("sops -e --kms : fichier chiffré committé (valeurs illisibles) + sops -d en CI via OIDC 1860 OK", 1857),
    ("pre-commit 1403 bloque un commit avec secret en clair (testé)", 1857),
    ("pod annoté agent-inject : /vault/secrets/db présent + kubectl get secrets vide (0 objet) + etcd sans le secret", 1858),
    ("rotation dynamic 1853 : fichier réécrit à renouvellement + app re-lit (ou Reloader 1855)", 1858),
    ("gitleaks pre-commit bloque un commit avec clé AWS test + trufflehog CI scan historique clean", 1859),
    ("tabletop fuite 1769 : révoquer 1855 + purger BFG + postmortem 1768 — procédure testée en 30 min", 1859),
    ("rôle IAM trust OIDC (sub repo+main) + workflow id-token: write -> sts get-caller-identity = rôle assumé, token 1 h", 1860),
    ("0 secret statique restant dans les settings (scan 1859) + Azure/GCP équivalents documentés", 1860),
    ("exports FOCUS natifs AWS/Azure/GCP actifs + landés dans 1 schéma + requête multi-cloud uniforme testée", 1861),
    ("dashboard coût multi-cloud 1766 + EffectiveCost vs BilledCost réconciliés à 0,1 % près", 1861),
    ("OpenCost déployé : coût par namespace/équipe affiché + namespace data-pipelines à 35 % identifié", 1862),
    ("rightsizing VPA 1803 : pods 8 CPU -> 2 CPU réels (PSI 1806) -> -60 % coût mesuré + export FOCUS 1861 OK", 1862),
    ("ADR comparatif (Airflow/Dagster/Prefect/Temporal, 4 axes) + 1 orchestrateur standard par équipe déployé", 1863),
    ("migration Airflow 2 -> 3.2 : asset partitioning activé + footprint mesuré", 1863),
    ("@asset daily_revenue(raw_orders) : plan d'exécution auto + test pytest local OK", 1864),
    ("UI : asset stale détecté -> alerte 1835 + lineage OpenLineage 1832 visible dans Marquez 1833", 1864),
    ("@flow avec @task retries=3 + cache 24h : 2e run skip la tâche cachée (-40 % temps) + UI flow runs OK", 1865),
    ("Prefect Cloud déployé (coût actions suivi) ou self-host worker+serveur testé", 1865),
    ("Debezium CDC Postgres->Kafka->warehouse : INSERT/UPDATE/DELETE capturés, latence 3 s mesurée", 1866),
    ("alerte latence > 5 min (1835/1761) testée + comparaison polling vs CDC documentee", 1866),
    ("3 connexions Airbyte (Salesforce, Postgres CDC, S3) -> warehouse OK + sync Dagster asset 1864 dans le graphe 1833", 1867),
    ("Airbyte 300+ connecteurs ingestion CDC Debezium embarqué open source Cloud marketplace Airflow Dagster assets 1866 — exemple concret d'utilisation", 1867),
    ("workflow Temporal avec activité qui échoue 2x puis réussit (retry backoff) + crash simulé du worker -> reprise à l'activité en cours", 1868),
    ("Temporal durable execution workflow long-running agents IA reprise après crash retries backoff heartbeats timers signaux état persistant — exemple concret d'utilisation", 1868),
    ("sensor S3 (fichier arrivé) -> run en 2 min + fallback cron 6 h configuré + 0 run vide sur 24 h", 1869),
    ("Airflow 3.2 asset event : DAG aval déclenché quand asset amont matérialisé (1864)", 1869),
    ("tags obligatoires CI 1820 (non taggé = non déployé) + rapport showback T3 par équipe/produit généré", 1870),
    ("alerte budget 80 % testée (1761) + chargeback validé CFO avec prélèvements effectifs T4", 1870),
    ("ClusterIssuer ACME staging puis prod + Certificate *.example.com émis (DNS-01) + renouvellement auto testé (date -30 j)", 1871),
    ("alerte expiration < 15 j via 1417 + HTTPRoute 1801 branchée sur le secret TLS", 1871),
    ("HTTPRoute annotée -> CNAME créé dans Route53 en 1 min (dig OK) + policy upsert-only (DNS existants intacts)", 1872),
    ("suppression ressource -> enregistrement supprimé (txt owner vérifié) + credentials via ESO 1854", 1872),
    ("ScaledObject Kafka lag>100 : scale 0->5 pods mesuré + scale to 0 quand file vide + ScheduledJob cron testé", 1873),
    ("TriggerAuthentication via ESO 1854 (cred Vault) + métriques 1416 + économie -70 % mesurée 1862", 1873),
    ("CAPI + CAPA : Cluster + MachineDeployment -> 3 nœuds provisionnés et joints (kubectl get nodes sur le nouveau cluster)", 1874),
    ("upgrade version 1.36->1.37 déclaratif (rolling) + 0 downtime mesuré", 1874),
    ("nœuds Talos joints au cluster (talosctl, pas de shell) + scan CVE -80 % vs Ubuntu (1826)", 1875),
    ("upgrade atomique A/B : boot fail simulé -> rollback auto OK + CAPI 1874 provisionne un nœud Talos", 1875),
    ("mesh Cilium 1727 activé : mTLS vérifié entre 2 pods + 0 sidecar + latence +0,3 ms mesurée", 1876),
    ("comparatif Linkerd vs Istio documenté (CRDs, overhead) + canary 1418 fonctionnel sur le mesh", 1876),
    ("Rollout canary 10 % + AnalysisTemplate PromQL (5xx, p99) : métriques OK -> promotion 100 % auto ; KO simulé -> abort + rollback 30 s", 1877),
    ("blue-green testé (switch + rollback instantanés) + Argo CD 1704 sync OK", 1877),
    ("NodePool spot weight 10 + GPU DRA 1802 : batch sur spot (-70 %), fallback on-demand testé", 1878),
    ("consolidation WhenUnderutilized : -40 % nœuds dimanche + drift : nœud vieille image remplacé auto + PDB 1805 respecté", 1878),
    ("ApplicationSet générateur clusters CAPI 1874 : 3 Applications créées (dev/staging/prod) + sync OK", 1879),
    ("sync waves : DB wave 0 déployée avant API wave 1 (ordre vérifié dans l'UI) + progressive sync canary 1877 sur staging", 1879),
    ("Velero schedule quotidien -> S3 + snapshot etcd vérifié (etcdctl snapshot status OK)", 1880),
    ("game day 1769 : restore cross-cluster en 22 min (RTO 30 min OK, RPO 1 h OK) + plan DR documenté", 1880),
    ("flag kill switch : feature off en prod en < 30 s sans redéploiement (testé)", 1881),
    ("feature flags kill switch rollout graduel A/B test ciblage LaunchDarkly Statsig Unleash GrowthBook Flagsmith PostHog audit dette flags — exemple concret d'utilisation", 1881),
    ("code OpenFeature (0 appel SDK vendor direct, vérifié par grep) + provider Unleash branché (flag évalué OK)", 1882),
    ("migration provider LaunchDarkly->Unleash en 1 ligne + hooks audit loggent les évaluations", 1882),
    ("matrice flag/canary/blue-green publiée + Flagger v1.45 canary auto testé (métriques KO -> abort)", 1883),
    ("blue-green : switch + rollback instantanés mesurés (< 30 s)", 1883),
    ("renovate.json : groupe npm (8 patchs -> 1 PR auto-mergée après CI 1413 verte + scan 1827 clean)", 1884),
    ("schedule hebdo + semaine lock configurés + actions GitHub pinnées SHA (1829)", 1884),
    ("quality gate Sonar en CI 1413 : PR avec vuln high + coverage 60 % -> bloquée (rouge), corrigée -> verte", 1885),
    ("dashboard 1766 : qualité (Sonar) + DORA 1888 + deploys 1418 réunis", 1885),
    ("openapi.yaml linté en CI 1413 + client TS généré + breaking change v3 bloqué (diff 1840)", 1886),
    ("AsyncAPI Kafka 1866 : schéma message versionné + tests Pact 1414 consommateurs OK", 1886),
    ("nx affected -t test : seul app-web testé après commit sur packages/ui (CI 6 min vs 45 min)", 1887),
    ("remote cache Nx Cloud/Turborepo actif + build reproductible (hermetic Bazel si choisi)", 1887),
    ("dashboard DORA 1766 : 4 métriques mesurées depuis CI/deploys/incidents + position vs benchmark elite affichée", 1888),
    ("revue mensuelle tenue + accélérateurs 1404/1877 choisis -> T+2 lead 5 j -> 2 j, CFR 30 % -> 12 % mesuré", 1888),
    ("TechDocs 1702 : 50 repos publiés auto, portail à jour après merge", 1889),
    ("règle revue 1401 : PR code sans doc -> bloquée (testé) + ADR 1746 dans docs/adr/ relu", 1889),
    ("revue IA 1741 active : résumé PR + 2 risques sécu 1826 signalés et corrigés avant merge", 1890),
    ("checklist 1401 cochée + SLA < 4 h mesuré sur 20 PR (file triée par ancienneté)", 1890),
    ("ADR choix EDR (threat model + PoC MITRE sur 3 candidats + coûts) + déploiement 100 % parc en 1 semaine", 1891),
    ("playbook réponse ransomware 1897 testé en tabletop 1769", 1891),
    ("règle corrélation (IdP+endpoint+réseau) : attaque simulée -> 1 incident auto priorité haute + blocage SOAR 1651", 1892),
    ("rétention XDR 2 ans configurée (1839) + timeline d'un incident réel rejouée", 1892),
    ("contrat MDR signé (SLA 15 min critique, périmètre complet) + tabletop 1769 : faux incident -> réponse mesurée < 15 min", 1893),
    ("rapport mensuel MDR reçu + 0 incident non répondu ce trimestre", 1893),
    ("MISP déployé + communauté rejointe (TLP) + IOC reçu -> règle SIEM 1453 créée auto", 1894),
    ("blocage auto : domaine/hash -> EDR 1891 + firewall en 5 min + 0 faux positif cette semaine (revue 1761)", 1894),
    ("DNSSEC : zone signée + validation unbound (réponse spoofée = SERVFAIL testé) + DS chez le registrar", 1895),
    ("DoH/DoT : requêtes chiffrées vérifiées (tcpdump : 0 DNS en clair) + filtering Quad9 bloque un domaine test + alerte 1453", 1895),
    ("passkeys obligatoires admins (conditional access Entra) : 100 % des 40 admins enrolled en 2 semaines", 1896),
    ("SMS désactivé + TOTP secours + taux adoption 90 % en 3 mois + incidents phishing -85 % (1892)", 1896),
    ("retainer signé + contact 24/7 testé (appel test < 15 min) + playbooks 4 scénarios à jour", 1897),
    ("exercice live 1769 documenté : ransomware simulé -> RTO 3 h respecté + écarts corrigés", 1897),
    ("ZAP baseline en CI 1413 sur staging : XSS trouvée (high) -> gate rouge + déploiement bloqué 1418 ; corrigée -> vert", 1898),
    ("full scan nuit + rapport ZAP + tendance vulnérabilités à la baisse sur 3 mois", 1898),
    ("12 champions nommés+formés (10 % temps alloué, vérifié) + canal + réunions mensuelles tenues", 1899),
    ("métriques : 80 % features avec threat model STRIDE avant dev + délai correction vuln high 3 j (vs 21 j)", 1899),
    ("security.txt RFC 9116 publié + security@ répond < 5 j (testé avec un faux rapport)", 1900),
    ("triage : rapport high SSVC 1826 -> patch en 5 j (canary 1418) + re-test + clôture + métrique publiée", 1900),

    ("auto-entrepreneur BTP", 1901),
    ("obligations légales artisan BTP", 1902),
    ("devis BTP conforme", 1903),
    ("facture artisan mentions obligatoires", 1904),
    ("statut juridique artisan comparatif", 1905),
    ("label Qualibat RGE artisan", 1906),
    ("assurance décennale RC Pro chantier", 1907),
    ("EPI chantier obligations 2026", 1908),
    ("PPSPS coordination SPS DUERP", 1909),
    ("NF C 15-100 Consuel électricien", 1910),
    ("plomberie normes DTU sanitaire", 1911),
    ("devis quantitatif estimatif métré", 1912),
    ("déchets chantier tri 7 flux BSD", 1913),
    ("location matériel chantier nacelle échafaudage", 1914),
    ("lire plan construction échelle cotes DCE", 1915),
    ("préparer chantier implantation réseaux accès", 1916),
    ("réception chantier procès-verbal réserves DOE", 1917),
    ("litige chantier BTP expertise médiation", 1918),
    ("reprise cession entreprise artisanale BTP", 1919),
    ("vendre son entreprise artisanale valorisation", 1920),
    ("installer atelier menuiserie amateur", 1921),
    ("outillage électroportatif menuiserie scie défonceuse", 1922),
    ("choisir essence bois chêne hêtre pin durabilité", 1923),
    ("dégauchir raboter bois scie à ruban sens du fil", 1924),
    ("assemblages bois tenon mortaise queue aronde lamello", 1925),
    ("colle bois vinylique PU serrage temps séchage", 1926),
    ("finition bois huile vernis cire lasure lasurer", 1927),
    ("restaurer meuble ancien décapage recollage", 1928),
    ("fabriquer étagère murale bois fixation chevilles", 1929),
    ("fabriquer meuble caisson bois DIY plan", 1930),
    ("quincaillerie ferrures charnières coulisses serrures pose", 1931),
    ("sécurité atelier bois aspiration poussières EPI stop urgence", 1932),
    ("traçage bois trusquin équerre cotes fonctionnelles", 1933),
    ("scie manuelle bois scie à dos japonaise coupe nette", 1934),
    ("poncer bois grain 80 240 sens du fil cale", 1935),
    ("teindre bois teinture eau alcool patine cérusé", 1936),
    ("poser parquet flottant clipsé sous-couche plinthes", 1937),
    ("plan de travail bois lamellé collé huile dure jonction", 1938),
    ("régler porte bois paumelles joint rénovation fenêtre", 1939),
    ("bois extérieur lasure classe 3 4 autoclave entretien", 1940),
    ("tour à bois tourner bol entre-pointes", 1941),
    ("cintrer bois vapeur lamellé cintré cintreuse", 1942),
    ("placage bois marqueterie fer à repasser colle contact", 1943),
    ("réparer fissure bois mastic greffe flipot", 1944),
    ("chiffrer ouvrage menuiserie prix matière temps vente", 1945),
    ("lire plan meuble nomenclature cotes découpe", 1946),
    ("défonceuse fraises rainure feuillure languette guide parallèle", 1947),
    ("assemblage démontable inserts filetés écrous à frapper", 1948),
    ("vernis pistolet HVLP dilution couches ponçage", 1949),
    ("affûter ciseau burin pierre angle 25 30 degrés", 1950),
    ("apprendre à tricoter débutant", 1951),
    ("choisir laine aiguilles tricot droites circulaires doubles pointes", 1952),
    ("échantillon tricot gauge 10x10 mesurer tension ajuster", 1953),
    ("points tricot base endroit envers mousse jersey côtes", 1954),
    ("tricot en rond circulaire marqueur bonnet sans couture", 1955),
    ("lire patron tricot abréviations tailles augmentations diminutions raglan", 1956),
    ("projet tricot débutant bonnet écharpe snood moufles chaussettes", 1957),
    ("bloquer ouvrage tricot laver laine sécher à plat finition", 1958),
    ("repriser pull laine reprise de mailles boulochage anti-peluches", 1959),
    ("monter mailles tricot longue queue rabattre souple", 1960),
    ("choisir machine à coudre débutant Brother Singer réglage", 1961),
    ("enfiler machine à coudre canette bobine tension fil", 1962),
    ("points couture machine droit zigzag boutonnière ourlet", 1963),
    ("surfiler ourlet machine zigzag overlock ourlet invisible double pli", 1964),
    ("poser fermeture éclair zip centrale invisible séparable", 1965),
    ("assembler vêtement couture endroit contre endroit valeur 1 cm point arrêt", 1966),
    ("choisir tissu couture droit-fil bâtir prélavage entoilage", 1967),
    ("lire patron couture Fait Main tailles 34 54 symboles marges", 1968),
    ("projet couture débutant tote bag coussin tablier 30 min par jour", 1969),
    ("coudre bouton à la main point arrière surjet main ourlet invisible", 1970),
    ("feutrage à l'aiguille débutant aiguilles 36 38 40", 1971),
    ("laine cardée roving peignée mérinos corriedale feutrage", 1972),
    ("forme base feutrage boule cylindre cône bloc mousse gabarit", 1973),
    ("figurine kawaii feutrage 3D yeux détails finition 40G", 1974),
    ("feutrage à l'eau chaude savon Marseille friction rétrécissement", 1975),
    ("bijoux feutre broche boucles d'oreilles barrette chapeau feutré", 1976),
    ("chaussons feutre semelle moule doublure sac feutré à l'eau", 1977),
    ("repriser pull laine feutré patch trou reprise feutrée", 1978),
    ("sécurité aiguilles à feutrer pointe acérée doigtier rangement", 1979),
    ("kit débutant feutrage 20 25 euros fournisseurs spécialisés", 1980),
    ("macramé débutant nœuds plat carré spirale porte-plante", 1981),
    ("pâte polymère Fimo Cernit cuisson four 110 130 degrés marbré", 1982),
    ("bijoux Fimo perles boucles pendentifs montage", 1983),
    ("faire bougie parfumée cire végétale soja mèche huile essentielle", 1984),
    ("savon naturel saponification à froid soude huile surgraissage cure", 1985),
    ("scrapbooking album vacances papiers tampons washi tape", 1986),
    ("machine de coupe Cricut Explore 3 Maker 3 Joy vinyle sticker", 1987),
    ("peinture acrylique débutant toile pinceaux glacis médium couches", 1988),
    ("aquarelle débutant papier 300g godets lavis sel masque liquide", 1989),
    ("broderie moderne tambour fils moulinés points base droit arrière nœud coulé tige", 1990),
    ("pyrogravure bois appareil pyrograveur essences tendres gabarits", 1991),
    ("kintsugi réparer céramique laque poudre or wabi-sabi", 1992),
    ("yarn bombing tricoter autour objets urbains autorisation fils acrylique", 1993),
    ("upcycling meuble relooker customiser textile jean peinture chalk paint", 1994),
    ("art journal carnet créatif mixed media collage pochoirs gesso", 1995),
    ("perles rocailles bijoux fantaisie montage fil élastique fermoirs", 1996),
    ("sériraphie risographie petites séries encres écrans tirage manuel", 1997),
    ("customiser vêtement jean tee-shirt peinture tissu patches thermocollants broderie", 1998),
    ("vendre créations artisanales Etsy A Little Market marchés prix fiches produit", 1999),
    ("organiser atelier loisirs créatifs rangement lumière budget temps", 2000),
]

# Tests EN (pilote multilingue) : routés avec lang="en" sur les sidecars .en.md
TESTS_ROUTAGE_EN = [
    ("how do I write an SEO blog post", 1),
    ("rewrite this text in a different tone", 2),
    ("write an advertising headline that converts", 3),
    ("write a professional email to decline politely", 4),
    ("summarize a long document in 5 bullet points", 5),
    ("run a structured brainstorming session", 6),
    ("translate this text professionally", 7),
    ("proofread and correct my text", 8),
    ("generate commented code", 9),
    ("review and debug my code", 10),
    ("which skill should I use for this", 0),
    ("explain a concept simply to a beginner", 11),
    ("prepare for my job interview", 12),
    ("analyse sales data trends and KPIs", 13),
    ("create a presentation deck with slides for the board", 14),
    ("plan a project with milestones and risks", 15),
    ("what does this contract clause mean", 16),
    ("help me improve this prompt", 17),
    ("deep research on the EV market", 18),
    ("grill me on my migration plan", 19),
    ("debug this intermittent bug", 20),
    ("write meeting minutes", 24),
    ("my inbox is overflowing", 25),
    ("I procrastinate on big tasks", 26),
    ("write a 30s TikTok ad script", 29),
    ("optimise my LinkedIn post", 30),
    ("write a LinkedIn post about my product launch", 31),
    ("benchmark our 3 main competitors", 32),
    ("build user personas for our app", 33),
    ("create a skill package in SKILL.md format", 38),
    ("make flashcards from this chapter", 40),
    ("run a mock exam with grading", 41),
    ("plan a 10-day trip to Japan", 42),
    ("write cold emails that get replies", 54),
    ("fill a business model canvas", 57),
    ("design our pricing tiers", 58),
    ("run a project premortem", 60),
    ("challenge this decision, play devil's advocate", 61),
    ("write a PRD with user stories", 63),
    ("audit this interface for UX issues", 64),
    ("write unit tests for this function", 67),
    ("write the commit message and PR description", 68),
    ("write a SQL query for our schema", 69),
    ("security audit of this code", 70),
    ("design OKRs for next quarter", 74),
    ("write a wedding speech", 75),
    ("build an MCP server for our database", 77),
    ("scrape these public pages into structured data", 91),
    ("remove duplicates and anomalies from this dataset", 92),
    ("design a RAG pipeline over our documents", 98),
    ("write the system prompt for our agent", 100),
    ("map these concepts visually", 101),
    ("answer questions over my personal documents", 102),
    ("analyse a market sector", 103),
    ("summarise this scientific paper", 104),
    ("analyse cohort retention and churn", 106),
    ("design an A/B test properly", 110),
    ("prioritise my sales pipeline with lead scoring", 111),
    ("write a client case study", 124),
    ("write a press release", 126),
    ("write a one-page decision memo", 127),
    ("write a step-by-step user guide", 130),
    ("explain this to kids simply", 132),
    ("format APA citations and a bibliography", 133),
    ("plan our editorial calendar", 135),
    ("write transactional emails", 138),
    ("write an image generation prompt", 139),
    ("design a colour palette and fonts", 149),
    ("write a technical SEO audit", 161),
    ("conversion rate optimisation cro strategy for our website", 162),
    ("plan a product launch", 163),
    ("write a cold call script", 165),
    ("prepare an investor pitch deck", 171),
    ("audit accessibility WCAG", 177),
    ("write developer API docs", 180),
    ("design a design system", 181),
    ("design a form with fewer fields and less drop-off", 182),
    ("prioritise the product backlog", 185),
    ("anonymise this customer dataset for GDPR", 189),
    ("write our company AI charter", 193),
    ("harden our bot against prompt injection", 195),
    ("audit access rights in our cloud", 197),
    ("write a security incident runbook", 199),
    ("design an employee onboarding", 203),
    ("write an internal remote work policy", 207),
    ("plan a facilitated workshop agenda for the team", 208),
    ("plan a home renovation project", 220),
    ("design home automation scenarios", 222),
    ("prioritise my daily todo list", 223),
    ("plan my moving checklist and logistics", 225),
    ("build a workout plan for a 5k", 214),
    ("audit my subscriptions to save money", 230),
    ("plan a career change into UX", 231),
    ("crisis communication holding statement", 235),
    ("debug a failing prompt", 237),
    ("write annotation guidelines", 238),
    ("write a grant application", 240),
]


# ---------------------------------------------------------------------------
# Outils communs
# ---------------------------------------------------------------------------

from functools import lru_cache

@lru_cache(maxsize=200_000)
def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


STOPWORDS = set("""
le la les l un une des du de d a au aux cet cette ces mon ma mes ton ta tes son sa ses
nos vos leur leurs je tu il elle on nous vous ils elles me te se lui leur y en
ai as avez avons ete est etait sont soit comment pourquoi quand que quoi qui ou par
avec sans dans sur sous pas ne plus tres bien moi toi faire fait fais veux voudrais
besoin aide peux peut pour svp et
""".split())


@lru_cache(maxsize=100_000)
def tokens(s: str) -> list:
    return [t for t in re.findall(r"[a-z0-9]+", norm(s)) if t not in STOPWORDS]


def dkey(domaine: str) -> str:
    s = unicodedata.normalize("NFKD", domaine)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


# ---------------------------------------------------------------------------
# Extraction canvas -> données (build)
# ---------------------------------------------------------------------------
RE_SOMMAIRE = re.compile(r"(?m)^\| (\d+) \| (.*?) \| (\S[^|]*) \|$")
RE_ROUTAGE = re.compile(r"(?m)^\| (.+) \| (\d+) \| (\S[^|]*) \|$")
RE_BULLET_INDEX = re.compile(r"^- \*\*(.+?)\*\* — (.+)$")
RE_MOT_CLE = re.compile(r"« (.+?) » → (\d+)")
RE_CARTE_HDR = "| Domaine | Mots-clés déclencheurs |"
RE_Q6 = re.compile(r"(?m)^(\s*)Q6 -->\|([^|]+)\| D(\d+)\[(.*)\]\s*$")
RE_ITEM_ARBRE = re.compile(r"(\d+) ([^·\]]+?)\s*$")
RE_KNODE = re.compile(r"K\d+\[Skill (\d+)\]")


def resume_auto(corps: str) -> str:
    """Condensé 2-3 lignes d'une skill, dérivé du corps (Objectif + étape 1 de la
    Méthode) — déterministe, identique entre build canvas et build --from-skills."""
    blocs = _blocs_canoniques(corps)
    obj = re.sub(r"\s+", " ", (blocs.get("Objectif") or "").strip())
    m = re.search(r"(?m)^1\.\s+(.+)$", blocs.get("Méthode") or "")
    etape = re.sub(r"\s+", " ", m.group(1).strip()) if m else ""
    r = f"{obj} Étape 1 : {etape}" if etape else obj
    r = r.replace("<", "inférieur à").replace(">", "supérieur à").replace('"', "'")
    return re.sub(r"\s+", " ", r).strip()[:400]


def lire_resumes(dossier_skills: Path) -> dict[int, str]:
    """Lit le champ `resume` du frontmatter de chaque skills/*.md ; si absent,
    le dérive du corps via resume_auto."""
    out = {}
    for f in sorted(Path(dossier_skills).glob("*.md")):
        txt = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
        if not m:
            continue
        fm = m.group(1)
        num = int(re.search(r"^num: (\d+)$", fm, re.M).group(1))
        mr = re.search(r'^resume: "(.*)"$', fm, re.M)
        out[num] = mr.group(1) if (mr and mr.group(1).strip()) else resume_auto(txt[m.end():])
    return out


def _skills_dir() -> Path:
    """Dossier skills/ : à côté de routage.py (pack) ou à la racine du dépôt."""
    here = Path(__file__).resolve().parent
    for cand in (here / "skills", here.parent / "skills"):
        if cand.is_dir():
            return cand
    return here / "skills"


def extraire_frontmatter(dossier_skills: Path):
    """Reconstruit sommaire/signaux/mot_cles/branches/noms_courts/cartes depuis
    skills/*.md (frontmatter YAML) — source de vérité autonome du canvas."""
    import re as _re
    sommaire, signaux, mot_cles, branches, noms_courts = {}, {}, {}, {}, {}
    syns_par_num = {}
    cartes = {}
    for f in sorted(dossier_skills.glob("*.md")):
        txt = f.read_text(encoding="utf-8")
        m = _re.match(r"---\n(.*?)\n---\n", txt, _re.S)
        assert m, f"{f.name} : pas de frontmatter"
        fm = m.group(1)
        g = lambda k: _re.search(rf'^{k}: "(.*)"$', fm, _re.M).group(1)
        num = int(_re.search(r"^num: (\d+)$", fm, _re.M).group(1))
        da = _re.search(r'^date_ajout: "(\d{4})-(\d{2})"$', fm, _re.M)
        assert da and 1 <= int(da.group(2)) <= 12, \
            f"{f.name} : date_ajout absente ou invalide (attendu: date_ajout: \"YYYY-MM\")"
        nom, dom = g("nom"), g("domaine")
        sommaire[num] = [nom, dom]
        signaux[num] = g("signal")
        mot_cles[num] = g("mot_cle")
        noms_courts[num] = g("nom_court")
        branches[num] = g("branche")
        syns_par_num[num] = _re.search(r'^synonymes: \[(.*)\]$', fm, _re.M).group(1)
        syns_par_num[num] = [s.strip().strip('"') for s in syns_par_num[num].split(",") if s.strip()]
        cartes.setdefault(dom, []).append(g("mot_cle"))
    carte = None  # résolue par l'appelant (canvas si dispo, sinon reconstruite)
    return sommaire, signaux, mot_cles, branches, noms_courts, carte, syns_par_num, cartes


def extraire(canvas: str):
    sommaire = {}
    for num, nom, dom in RE_SOMMAIRE.findall(canvas):
        sommaire[int(num)] = [nom.strip(), dom.strip()]
    assert len(sommaire) == 2001, f"sommaire : {len(sommaire)} lignes"

    signaux = {}
    for sig, num, dom in RE_ROUTAGE.findall(canvas):
        n = int(num)
        assert n not in signaux, f"signal dupliqué pour {n}"
        signaux[n] = sig.strip()
        assert sommaire[n][1] == dom.strip(), f"domaine incohérent pour {n}"
    assert len(signaux) == 2000

    mot_cles, cartes, bullets = {}, [], False
    dans_carte = False
    for ligne in canvas.splitlines():
        s = ligne.strip()
        if s == RE_CARTE_HDR:
            dans_carte = "hdr"
            continue
        if dans_carte == "hdr" and s and set(s) <= {"|", "-"}:
            dans_carte = True
            continue
        if dans_carte and s.startswith("|") and "|" in s[1:]:
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) == 2 and cells[0] != "Domaine":
                cartes.append((cells[0], cells[1]))
                continue
        if dans_carte:
            dans_carte = False
        if s.startswith("**Index inversé**"):
            bullets = True
            continue
        if bullets and s.startswith("- **"):
            m = RE_BULLET_INDEX.match(s)
            dom = m.group(1)
            for kw, num in RE_MOT_CLE.findall(m.group(2)):
                n = int(num)
                assert n not in mot_cles, f"mot-clé dupliqué : {n}"
                assert sommaire[n][1] == dom, f"index : domaine incohérent pour {n}"
                mot_cles[n] = kw
        elif bullets and s and not s.startswith("- **"):
            bullets = False
    assert len(cartes) == 30, f"carte : {len(cartes)}"
    assert len(mot_cles) == 2000, f"index : {len(mot_cles)}"

    branches, noms_courts = {}, {}
    for m in RE_Q6.finditer(canvas):
        for item in m.group(4).split(" · "):
            mi = RE_ITEM_ARBRE.match(item.strip())
            assert mi, f"arbre D{m.group(3)} : item non parsé « {item} »"
            n = int(mi.group(1))
            branches[n] = f"D{m.group(3)}"
            noms_courts[n] = mi.group(2).strip()
    for n in RE_KNODE.findall(canvas):
        branches.setdefault(int(n), "K")
    assert len(branches) == 2000, f"arbre : {len(branches)} skills couvertes"
    return sommaire, signaux, mot_cles, branches, noms_courts, cartes


def _json_dumps(x) -> str:
    import json
    return json.dumps(x, ensure_ascii=False)


VEC_DIM = 32  # 32 suffit à 1 351 skills (hash bag-of-words) — 2x moins de calcul vec
CATALOGUE_VERSION = "21.0.0"  # version sémantique du catalogue (vague 22 = 2001 sections)
VEC_SEUIL = 0.95  # seuil très strict : hash 32 dims monte les cosinus sur requêtes courtes
VEC_PISTE = 0.86  # P0-2 : relevé de 0.80 (faux positifs à 0.803) + au moins un token commun avec la requête requis ci-dessous


def charger_vec(db: sqlite3.Connection) -> bool:
    """Charge l'extension sqlite-vec si disponible. Retourne True si la
    recherche vectorielle est active."""
    try:
        import sqlite_vec
        db.enable_load_extension(True)
        sqlite_vec.load(db)
        return True
    except Exception:
        return False


def _embed_texte(item):
    """Worker multiprocessing : (num, texte) -> (num, embedding)."""
    num, texte = item
    return (num, embed_hash(texte))


def embed_hash(texte: str, dim: int = VEC_DIM) -> bytes:
    """Embedding local déterministe et sans dépendance externe : chaque token
    est hashé (sha256) dans un vecteur de `dim` cases, pondéré, puis normalisé
    (cosinus). Assez pour rapprocher des formulations proches (synonymes,
    périphrases légères) sans appeler de modèle externe."""
    import hashlib
    import math
    import struct
    toks = tokens(texte)
    v = [0.0] * dim
    for t in toks:
        h = int(hashlib.sha256(t.encode("utf-8")).hexdigest(), 16)
        v[h % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return struct.pack(f"{dim}f", *(x / n for x in v))


def _lang_sidecars(sk_dir: Path) -> dict[str, dict[int, dict]]:
    """Sidecars multilingues skills/NNN-slug.<lang>.md -> {lang: {num: entry}}.
    Mécanisme générique : tout code langue 2 lettres (en, nl, ...)."""
    out: dict[str, dict[int, dict]] = {}
    for f in sorted(Path(sk_dir).glob("*.md")):
        m = re.match(r"^(\d+)-(.+)\.([a-z]{2})\.md$", f.name)
        if not m:
            continue
        lang = m.group(3)
        if lang == "fr":
            continue
        txt = f.read_text(encoding="utf-8")
        mm = re.match(r"---\n(.*?)\n---\n", txt, re.S)
        assert mm, f"{f.name} : pas de frontmatter"
        fm = mm.group(1)
        def g(k):
            r = re.search(rf'^{k}: "(.*)"$', fm, re.M)
            return r.group(1) if r else ""
        num = int(re.search(r"^num: (\d+)$", fm, re.M).group(1))
        ml = re.search(r'^lang: "(.*)"$', fm, re.M)
        assert ml and ml.group(1) == lang, f"{f.name} : lang incohérent avec le suffixe"
        ms = re.search(r'^synonymes: \[(.*)\]$', fm, re.M)
        syns = [x.strip().strip('"') for x in ms.group(1).split(",") if x.strip()] if ms else []
        mc = re.search(r'^cross_refs: \[(.*)\]$', fm, re.M)
        refs = [int(r) for r in re.findall(r"\d+", mc.group(1))] if mc else []
        mr = re.search(r'^resume: "(.*)"$', fm, re.M)
        resume = mr.group(1) if (mr and mr.group(1).strip()) else resume_auto(txt[mm.end():])
        out.setdefault(lang, {})[num] = {
            "nom": g("nom"), "domaine": g("domaine"), "signal": g("signal"),
            "mot_cle": g("mot_cle"), "branche": g("branche"), "nom_court": g("nom_court"),
            "emoji": g("emoji"), "resume": resume, "synonymes": syns, "cross_refs": refs,
            "fichier": f.name,
        }
    return out


def cmd_build(chemin: Path, db_path: Path = DB_PATH, from_skills: bool = False) -> None:
    if from_skills:
        sommaire, signaux, mot_cles, branches, noms_courts, _, syns_par_num, cartes_brutes = \
            extraire_frontmatter(_skills_dir())
        # source unique des synonymes = SYNONYMES (embarquée dans routage.py, donc dans le pack)
        SYN_A_UTILISER = {n: [s for s, num in SYNONYMES if num == n] for n in set(num for _, num in SYNONYMES)}
        # si le canvas existe : noms + carte des domaines depuis le canvas (source de vérité)
        if chemin.exists():
            canvas_txt = chemin.read_text(encoding="utf-8")
            try:
                s_c, sig_c, mc_c, br_c, nc_c, cartes = extraire(canvas_txt)
                for num in sommaire:
                    if num in s_c:
                        sommaire[num][0] = s_c[num][0]
            except AssertionError:
                # pack autonome (pas de canvas) : noms du frontmatter, carte reconstruite
                cartes = [(dom, ", ".join(mcs[:5])) for dom, mcs in sorted(cartes_brutes.items())]
        else:
            cartes = [(dom, ", ".join(mcs[:5])) for dom, mcs in sorted(cartes_brutes.items())]
    else:
        sommaire, signaux, mot_cles, branches, noms_courts, cartes = extraire(
            chemin.read_text(encoding="utf-8"))
        SYN_A_UTILISER = {n: [s for s, num in SYNONYMES if num == n] for n in set(num for _, num in SYNONYMES)}
    old_snapshot = None
    if db_path.exists():
        try:
            _old = sqlite3.connect(db_path)
            old_snapshot = _old.execute(
                "SELECT v FROM meta WHERE k='snapshot'").fetchone()
            _old.close()
        except sqlite3.Error:
            pass
        db_path.unlink()
    db = sqlite3.connect(db_path)
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA cache_size=-8000")
    vec_ok = charger_vec(db)
    if vec_ok:
        db.execute(f"CREATE VIRTUAL TABLE skills_vec USING vec0("
                   f"num INTEGER PRIMARY KEY, embedding float[{VEC_DIM}] "
                   f"distance_metric=cosine)")
    db.executescript("""
        CREATE TABLE skills (
            num       INTEGER PRIMARY KEY,
            nom       TEXT NOT NULL,
            domaine   TEXT NOT NULL,
            signal    TEXT NOT NULL DEFAULT '',
            mot_cle   TEXT NOT NULL DEFAULT '',
            branche   TEXT NOT NULL DEFAULT '',
            nom_court TEXT NOT NULL DEFAULT '',
            resume    TEXT NOT NULL DEFAULT ''
        );
        CREATE TABLE domaines (
            domaine   TEXT PRIMARY KEY,
            mots_cles TEXT NOT NULL
        );
        CREATE TABLE synonymes (
            synonyme      TEXT NOT NULL,
            synonyme_norm TEXT NOT NULL DEFAULT '',
            num           INTEGER NOT NULL,
            poids         REAL NOT NULL DEFAULT 1.0,  -- P0-1 : poids IDF, synonyme générique = poids faible
            lang          TEXT NOT NULL DEFAULT 'fr',
            PRIMARY KEY (synonyme, lang)
        );
        CREATE INDEX IF NOT EXISTS idx_synonymes_norm ON synonymes(synonyme_norm);
        CREATE TABLE non_routees (
            demande TEXT PRIMARY KEY,
            nb      INTEGER NOT NULL DEFAULT 1,
            dernier TEXT NOT NULL DEFAULT (datetime('now'))
        );
        CREATE TABLE routes (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            demande TEXT NOT NULL,
            code    INTEGER NOT NULL,
            voie    TEXT NOT NULL,
            num     INTEGER,
            date    TEXT NOT NULL DEFAULT (datetime('now'))
        );
        CREATE VIRTUAL TABLE skills_fts USING fts5(
            num UNINDEXED, nom, signal, mot_cle, nom_court, domaine,
            tokenize='unicode61'
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS skills_fts_vocab USING fts5vocab(skills_fts, row);
        CREATE TRIGGER skills_ai AFTER INSERT ON skills BEGIN
            INSERT INTO skills_fts(num, nom, signal, mot_cle, nom_court, domaine)
            VALUES (new.num, new.nom, new.signal, new.mot_cle, new.nom_court, new.domaine);
        END;
        CREATE TRIGGER skills_ad AFTER DELETE ON skills BEGIN
            DELETE FROM skills_fts WHERE num = old.num;
        END;
        CREATE TRIGGER skills_au AFTER UPDATE ON skills BEGIN
            DELETE FROM skills_fts WHERE num = old.num;
            INSERT INTO skills_fts(num, nom, signal, mot_cle, nom_court, domaine)
            VALUES (new.num, new.nom, new.signal, new.mot_cle, new.nom_court, new.domaine);
        END;
        CREATE INDEX IF NOT EXISTS idx_skills_domaine ON skills(domaine);
        CREATE INDEX IF NOT EXISTS idx_skills_branche ON skills(branche);
        CREATE TABLE IF NOT EXISTS meta (
            k TEXT PRIMARY KEY,
            v TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS cross_refs (
            num  INTEGER PRIMARY KEY,
            refs TEXT NOT NULL DEFAULT ''
        );
        CREATE TABLE IF NOT EXISTS popularite (
            num   INTEGER PRIMARY KEY,
            score REAL NOT NULL DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS depends_on (
            num  INTEGER NOT NULL,
            next INTEGER NOT NULL,
            PRIMARY KEY (num, next)
        ) WITHOUT ROWID;
        CREATE TABLE IF NOT EXISTS tags (
            tag TEXT NOT NULL,
            num INTEGER NOT NULL,
            PRIMARY KEY (tag, num)
        ) WITHOUT ROWID;
        CREATE TABLE IF NOT EXISTS mots_cles (
            mot_cle_norm TEXT NOT NULL,
            num          INTEGER NOT NULL,
            lang         TEXT NOT NULL DEFAULT 'fr',
            PRIMARY KEY (mot_cle_norm, num, lang)
        ) WITHOUT ROWID;
        CREATE TABLE IF NOT EXISTS lang (
            num    INTEGER NOT NULL,
            lang   TEXT NOT NULL,
            fichier TEXT NOT NULL DEFAULT '',
            PRIMARY KEY (num, lang)
        );
        CREATE TABLE IF NOT EXISTS trigrammes (
            trigramme TEXT NOT NULL,
            num       INTEGER NOT NULL,
            lang      TEXT NOT NULL DEFAULT 'fr',
            PRIMARY KEY (trigramme, num, lang)
        ) WITHOUT ROWID;
        CREATE TABLE IF NOT EXISTS versions (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            date      TEXT NOT NULL DEFAULT (datetime('now')),
            nb_skills INTEGER NOT NULL,
            ajouts    TEXT NOT NULL DEFAULT '[]',
            supprimes TEXT NOT NULL DEFAULT '[]',
            modifies  TEXT NOT NULL DEFAULT '[]'
        );
        -- skills perso (mesSkillsPerso/) : table dédiée, jamais dans le pack
        CREATE TABLE IF NOT EXISTS skills_perso (
            num        INTEGER PRIMARY KEY,
            nom        TEXT NOT NULL DEFAULT '',
            domaine    TEXT NOT NULL DEFAULT 'Perso',
            signal     TEXT NOT NULL DEFAULT '',
            mot_cle    TEXT NOT NULL DEFAULT '',
            nom_court  TEXT NOT NULL DEFAULT '',
            branche    TEXT NOT NULL DEFAULT 'K',
            synonymes  TEXT NOT NULL DEFAULT '',
            date_ajout TEXT NOT NULL DEFAULT '',
            fichier    TEXT NOT NULL DEFAULT ''
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS perso_fts USING fts5(
            num UNINDEXED, nom, signal, mot_cle, nom_court, domaine,
            tokenize='unicode61'
        );
        CREATE TABLE IF NOT EXISTS perso_synonymes (
            synonyme      TEXT PRIMARY KEY,
            synonyme_norm TEXT NOT NULL DEFAULT '',
            num           INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS perso_mots_cles (
            mot_cle_norm TEXT NOT NULL,
            num          INTEGER NOT NULL,
            PRIMARY KEY (mot_cle_norm, num)
        ) WITHOUT ROWID;
    """)
    if old_snapshot:
        db.execute("INSERT OR REPLACE INTO meta VALUES ('snapshot', ?)",
                   (old_snapshot[0],))
    db.executemany("INSERT INTO domaines VALUES (?, ?)", cartes)
    if from_skills:
        resumes = lire_resumes(_skills_dir())
    else:
        resumes = {n: resume_auto(corps)
                   for n, (_e, _nom, corps, _lbl) in _sections_multi(chemin).items()}
    for num in sorted(sommaire):
        nom, dom = sommaire[num]
        sig = signaux.get(num, "")
        mc = mot_cles.get(num, "")
        br = branches.get(num, "")
        nc = noms_courts.get(num, "")
        db.execute("INSERT INTO skills VALUES (?,?,?,?,?,?,?,?)",
                   (num, nom, dom, sig, mc, br, nc, resumes.get(num, "")))
    # embeddings : séquentiel suffit à 1 351 skills (hash rapide) — le multiprocessing
    # (testé) coûte plus cher en spawn de workers qu'il ne gagne. À paralléliser > ~20 000 skills.
    if vec_ok:
        vecs = []
        for num in sorted(sommaire):
            nom, dom = sommaire[num]
            sig = signaux.get(num, ""); mc = mot_cles.get(num, "")
            br = branches.get(num, ""); nc = noms_courts.get(num, "")
            ctx = f"[{dom} | {br}] " if (dom or br) else ""
            vecs.append((num, embed_hash(ctx + " ".join(x for x in (nom, sig, mc, nc) if x))))
        db.executemany("INSERT INTO skills_vec(num, embedding) VALUES (?,?)", vecs)
    connus = {n for (n,) in db.execute("SELECT num FROM skills")}
    if 0 not in connus:  # pack autonome : recréer la skill 0 (routeur)
        db.execute("INSERT INTO skills VALUES (0, '🧭 Routeur de skills', 'Routage', '', '', '', '', '')")
        db.execute("INSERT INTO skills_fts VALUES (0, 'Routeur de skills', '', '', 'Routeur', 'Routage')")
        db.commit()
        connus = {n for (n,) in db.execute("SELECT num FROM skills")}
    # P0-1 : poids IDF des synonymes — un synonyme présent partout dans le catalogue
    # (ex. « optimise » dans 200 signaux) ne doit pas battre un mot-clé exact spécifique
    import math as _math
    _big = " ".join(norm(str(x)) for num in sommaire
                    for x in (sommaire[num][0], signaux.get(num, ""), mot_cles.get(num, ""), noms_courts.get(num, "")))
    def _poids_syn(syn):
        occ = _big.count(norm(syn))
        return 1.0 / (1.0 + _math.log1p(occ))
    for num, syns in SYN_A_UTILISER.items():
        for syn in syns:
            assert num in connus, f"synonyme « {syn} » -> skill inexistante {num}"
            db.execute("INSERT OR IGNORE INTO synonymes VALUES (?,?,?,?,?)", (syn, norm(syn), num, _poids_syn(syn), "fr"))
    # popularité : top-N des skills les plus routées (table routes), sert de bonus de classement
    # et de cache chaud. Recalculée à chaque build si la table routes existe.
    try:
        rows = db.execute(
            "SELECT num, COUNT(*) c, SUM(CASE WHEN code=0 THEN 1 ELSE 0 END) ok "
            "FROM routes GROUP BY num").fetchall()
        db.executemany("INSERT OR REPLACE INTO popularite VALUES (?,?)",
                       [(r["num"], round(r["ok"] * 1.0 + r["c"] * 0.1, 3)) for r in rows])
        db.commit()
    except sqlite3.OperationalError:
        pass
    # table depends_on (skills composables : chaîne de dépendances) et tags
    dep = []
    for f in sorted((RACINE / "skills").glob("*.md")):
        import re as _re
        fm = f.read_text(encoding="utf-8").split("---")[1]
        num = int(_re.search(r"^num: (\d+)$", fm, _re.M).group(1))
        md = _re.search(r"^depends_on: \[(.*)\]$", fm, _re.M)
        if md:
            for x in md.group(1).split(","):
                x = x.strip()
                if x: dep.append((num, int(x)))
    db.executemany("INSERT OR IGNORE INTO depends_on VALUES (?,?)", dep)
    db.commit()
    # table cross_refs (bonus de classement) et tags (filtre optionnel)
    xr, tg = [], []
    for f in sorted((RACINE / "skills").glob("*.md")):
        import re as _re
        fm = f.read_text(encoding="utf-8").split("---")[1]
        num = int(_re.search(r"^num: (\d+)$", fm, _re.M).group(1))
        cr = _re.search(r"^cross_refs: \[(.*)\]$", fm, _re.M).group(1)
        xr.append((num, cr))
        mt = _re.search(r"^tags: \[(.*)\]$", fm, _re.M)
        if mt:
            for t in mt.group(1).split(","):
                t = t.strip().strip('"')
                if t: tg.append((norm(t), num))
    db.executemany("INSERT OR REPLACE INTO cross_refs VALUES (?,?)", xr)
    db.executemany("INSERT OR IGNORE INTO tags VALUES (?,?)", tg)
    db.commit()
    # table des mots-clés normalisés (voie mot-clé en SQL, indexée)
    mcs = []
    for r in db.execute("SELECT num, mot_cle FROM skills WHERE mot_cle != ''"):
        mcs.append((norm(r[1]), r[0], "fr"))
    db.executemany("INSERT OR IGNORE INTO mots_cles VALUES (?,?,?)", mcs)
    db.commit()
    # table des trigrammes (passe floue en SQL) : mêmes champs que la version Python
    tg = []
    for r in db.execute("SELECT num, nom, signal, mot_cle, nom_court FROM skills"):
        # trigrammes des tokens >= 5 lettres seulement (la passe floue ne matche que qt_forts >= 5)
        mots = [t for t in tokens(" ".join(str(x) for x in (r[1], r[2], r[3], r[4]))) if len(t) >= 5]
        seen = set()
        for t in mots:
            for i in range(len(t) - 2):
                tri = t[i:i+3]
                if tri not in seen:
                    seen.add(tri)
                    tg.append((tri, r[0], "fr"))
    db.executemany("INSERT OR IGNORE INTO trigrammes VALUES (?,?,?)", tg)
    db.commit()
    # table lang(num, lang, fichier) : FR (fichiers racine) + sidecars .<lang>.md
    sk = _skills_dir()
    for f in sorted(sk.glob("*.md")):
        if re.match(r"^\d+-.*\.[a-z]{2}\.md$", f.name):
            continue  # sidecar
        m2 = re.match(r"^(\d+)-.+\.md$", f.name)
        if m2:
            db.execute("INSERT OR REPLACE INTO lang VALUES (?,?,?)", (int(m2.group(1)), "fr", f.name))
    for lang, entrees in _lang_sidecars(sk).items():
        sfx = "_" + re.sub(r"[^a-z0-9]", "", lang.lower())
        db.execute(f"CREATE TABLE IF NOT EXISTS skills{sfx} (num INTEGER PRIMARY KEY, nom TEXT NOT NULL, domaine TEXT NOT NULL, signal TEXT NOT NULL DEFAULT '', mot_cle TEXT NOT NULL DEFAULT '', branche TEXT NOT NULL DEFAULT '', nom_court TEXT NOT NULL DEFAULT '', resume TEXT NOT NULL DEFAULT '')")
        db.execute(f"CREATE VIRTUAL TABLE IF NOT EXISTS skills_fts{sfx} USING fts5(num UNINDEXED, nom, signal, mot_cle, nom_court, domaine, tokenize='unicode61')")
        if vec_ok:
            db.execute(f"CREATE VIRTUAL TABLE IF NOT EXISTS skills_vec{sfx} USING vec0(num INTEGER PRIMARY KEY, embedding float[{VEC_DIM}] distance_metric=cosine)")
        for num, e in sorted(entrees.items()):
            db.execute(f"INSERT OR REPLACE INTO skills{sfx} VALUES (?,?,?,?,?,?,?,?)",
                       (num, e["nom"], e["domaine"], e["signal"], e["mot_cle"], e["branche"], e["nom_court"], e["resume"]))
            db.execute(f"INSERT INTO skills_fts{sfx} VALUES (?,?,?,?,?,?)",
                       (num, e["nom"], e["signal"], e["mot_cle"], e["nom_court"], e["domaine"]))
            if vec_ok:
                ctx = f"[{e['domaine']} | {e['branche']}] "
                db.execute(f"INSERT INTO skills_vec{sfx} VALUES (?,?)",
                           (num, embed_hash(ctx + " ".join(x for x in (e["nom"], e["signal"], e["mot_cle"], e["nom_court"]) if x))))
            if e["mot_cle"]:
                db.execute("INSERT OR IGNORE INTO mots_cles VALUES (?,?,?)", (norm(e["mot_cle"]), num, lang))
            for syn in e["synonymes"]:
                db.execute("INSERT OR IGNORE INTO synonymes VALUES (?,?,?,?,?)", (syn, norm(syn), num, 1.0, lang))
            mots = [t for t in tokens(" ".join((e["nom"], e["signal"], e["mot_cle"], e["nom_court"]))) if len(t) >= 5]
            seen = set()
            for t in mots:
                for i in range(len(t) - 2):
                    tri = t[i:i+3]
                    if tri not in seen:
                        seen.add(tri)
                        db.execute("INSERT OR IGNORE INTO trigrammes VALUES (?,?,?)", (tri, num, lang))
            db.execute("INSERT OR REPLACE INTO lang VALUES (?,?,?)", (num, lang, e["fichier"]))
        db.commit()
    np_ = ingerer_perso(db)  # mesSkillsPerso/ -> skills_perso (conversion auto au template)
    n = db.execute("SELECT COUNT(*) FROM skills").fetchone()[0]
    d = db.execute("SELECT COUNT(*) FROM domaines").fetchone()[0]
    s = db.execute("SELECT COUNT(*) FROM synonymes").fetchone()[0]
    f = db.execute("SELECT COUNT(*) FROM skills_fts").fetchone()[0]
    v = db.execute("SELECT COUNT(*) FROM skills_vec").fetchone()[0] if vec_ok else 0
    # historique des versions : snapshot JSON + diff vs version précédente
    snapshot = db.execute(
        "SELECT json_group_array(json_object('num', num, 'nom', nom, "
        "'domaine', domaine, 'signal', signal, 'mot_cle', mot_cle)) "
        "FROM (SELECT * FROM skills ORDER BY num)").fetchone()[0]
    old_snap = db.execute("SELECT v FROM meta WHERE k='snapshot'").fetchone()
    ajouts, supprimes, modifies = [], [], []
    if old_snap:
        import json as _json
        old_map = {e["num"]: e for e in _json.loads(old_snap[0])}
        new_map = {e["num"]: e for e in _json.loads(snapshot)}
        for num in sorted(set(new_map) - set(old_map)):
            ajouts.append(num)
        for num in sorted(set(old_map) - set(new_map)):
            supprimes.append(num)
        for num in sorted(set(old_map) & set(new_map)):
            if old_map[num] != new_map[num]:
                modifies.append(num)
    db.execute("INSERT INTO versions(nb_skills, ajouts, supprimes, modifies) "
               "VALUES (?,?,?,?)",
               (n - 1, _json_dumps(ajouts), _json_dumps(supprimes), _json_dumps(modifies)))  # -1 : skill 0 = routeur, jamais comptée
    db.execute("INSERT OR REPLACE INTO meta VALUES ('snapshot', ?)", (snapshot,))
    db.execute("INSERT OR REPLACE INTO meta VALUES ('version', ?)", (CATALOGUE_VERSION,))
    db.commit()
    db.execute("PRAGMA optimize")
    db.execute("VACUUM")
    db.close()
    if db_path == DB_PATH:
        print(f"skills.db reconstruit : {n - 1} skills + 1 routeur (skill 0) · {d} domaines · "
              f"{s} synonymes · {f} lignes FTS · {v} vecteurs · {np_} perso (mesSkillsPerso/)")  # -1 : le routeur n'est pas une skill


# ---------------------------------------------------------------------------
# route : base -> candidates
# ---------------------------------------------------------------------------

@lru_cache(maxsize=50_000)
def trigrammes_de(mot: str) -> frozenset:
    """Trigrammes d'un mot (>= 5 lettres), mis en cache LRU — la requête revient souvent."""
    return frozenset(mot[i:i + 3] for i in range(len(mot) - 2))


def proches_trigrammes_sql(db: sqlite3.Connection, qt, ratio_mini=0.6,
                           vus=None, lang="fr"):
    """Passe floue par trigrammes en SQL (table `trigrammes` indexée).
    Même contrat que proches_trigrammes : liste triée (ratio, nb, mot, row).
    Repli sur la version Python si la table est absente (base ancienne)."""
    req_tri = {t: trigrammes_de(t) for t in qt if len(t) >= 5}
    if not req_tri:
        return []
    if not db.execute("SELECT 1 FROM sqlite_master WHERE name='trigrammes'").fetchone():
        return proches_trigrammes(db, qt, ratio_mini, vus)
    best = {}
    for t, tri in req_tri.items():
        ph = ",".join("?" * len(tri))
        for num, c in db.execute(
                f"SELECT num, COUNT(*) FROM trigrammes WHERE trigramme IN ({ph}) AND lang = ? "
                f"GROUP BY num", (*tri, lang)):
            if vus and num in vus:
                continue
            ratio = c / len(tri)
            if c >= 2 and ratio >= ratio_mini:
                key = (num, t)
                if key not in best or (ratio, c) > best[key]:
                    best[key] = (ratio, c)
    if not best:
        return []
    nums = sorted({num for num, _ in best})
    ph = ",".join("?" * len(nums))
    sfx = "" if lang == "fr" else "_" + re.sub(r"[^a-z0-9]", "", lang.lower())
    if not db.execute("SELECT 1 FROM sqlite_master WHERE name=?", (f"skills{sfx}",)).fetchone():
        sfx = ""
    skills = {r["num"]: r for r in db.execute(
        f"SELECT num, nom, domaine, signal, mot_cle, nom_court FROM skills{sfx} "
        f"WHERE num IN ({ph})", tuple(nums))}
    out = [(ratio, c, t, skills[num]) for (num, t), (ratio, c) in best.items()]
    out.sort(key=lambda x: (-x[0], -x[1]))
    return out


def proches_trigrammes(db: sqlite3.Connection, qt, ratio_mini=0.6,
                       vus=None):
    """Recouvrements de trigrammes entre les mots de la demande (>= 5
    lettres) et le texte des skills. Retourne (ratio, nb_trigrammes,
    mot, row) triés par ratio décroissant."""
    req_tri = {t: {t[i:i + 3] for i in range(len(t) - 2)}
               for t in qt if len(t) >= 5}
    proches = []
    if not req_tri:
        return proches
    for r in db.execute("SELECT num, nom, domaine, signal, mot_cle, "
                        "nom_court FROM skills"):
        if vus and r["num"] in vus:
            continue
        texte = norm(" ".join(str(r[k]) for k in
                    ("nom", "signal", "mot_cle", "nom_court")))
        tri_txt = {texte[i:i + 3] for i in range(len(texte) - 2)}
        for t, tri in req_tri.items():
            commun = tri & tri_txt
            ratio = len(commun) / len(tri)
            if len(commun) >= 2 and ratio >= ratio_mini:
                proches.append((ratio, len(commun), t, r))
    proches.sort(key=lambda x: (-x[0], -x[1]))
    return proches


RE_MOTS = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def mots_de(r) -> set:
    """Mots d'une skill (composés à trait lié : « garde-fous » reste un seul
    mot, pour que « garde » ne compte pas comme mot complet)."""
    champs = ("nom", "signal", "mot_cle", "nom_court")
    return set(RE_MOTS.findall(norm(" ".join(str(r[k]) for k in champs
                if k in r.keys()))))


def mot_match(t: str, mots: set) -> bool:
    """Correspondance au mot complet ou à l'inflexion près (6 premiers
    caractères communs) — jamais un simple préfixe court : « rest » ne
    matche pas « restaurateur », « signal » pas « signaux faibles »."""
    return t in mots or (len(t) >= 6
                         and any(w[:6] == t[:6] for w in mots))


def mot_match_large(t: str, mots: set) -> bool:
    """Version stricte pour le flou : mot complet ou racine de 7 caractères
    (à 6, « stress » matchait « stresser un agent »)."""
    return t in mots or (len(t) >= 7
                         and any(w[:7] == t[:7] for w in mots))


def _fts_valide(r, qt_forts) -> bool:
    """Anti-faux-positifs en mode OU du FTS : avec plusieurs tokens, une
    skill n'est retenue que si >= 2 tokens la matchent réellement ; en
    mono-token, il faut un mot complet ou une racine commune (pas un
    préfixe court)."""
    uniques = set(qt_forts)
    n = sum(1 for t in uniques if mot_match(t, mots_de(r)))
    return n >= 2 if len(uniques) >= 2 else n >= 1


# ---------------------------------------------------------------------------
# mesSkillsPerso : skills personnelles de l'utilisateur
# - dossier mesSkillsPerso/ (à côté de routage.py dans le pack, à la racine
#   du dépôt sinon) : l'utilisateur y dépose ses propres fichiers .md
# - jamais écrasé/supprimé à l'upgrade (le pack n'embarque que le README)
# - converti automatiquement au format du template (TEMPLATE-v2) au prochain
#   build (réécrit en place, même nom de fichier)
# - table dédiée skills_perso (+ perso_fts / perso_synonymes / perso_mots_cles)
# - PRIORITAIRE au routage : si une skill perso cadrage avec la demande, elle gagne
# ---------------------------------------------------------------------------
PERSO_README = """# mesSkillsPerso — tes skills perso

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
"""

SECTIONS_PERSO_RE = [
    r"^\*\*Objectif\*\*", r"^\*\*Quand l'utiliser", r"^\*\*Hors périmètre\*\*",
    r"^\*\*Garde-fous\*\*", r"^\*\*Instructions système\*\*", r"^\*\*Inputs requis\*\*",
    r"^\*\*Méthode\*\*", r"^\*\*Sorties attendues\*\*", r"^\*\*Exemple de prompt\*\*",
    r"^\*\*Cas d'usage\*\*", r"^\*\*Checklist QA interne\*\*", r"^\*\*Definition of done\*\*",
]


def dossiers_perso() -> list[Path]:
    """Dossiers mesSkillsPerso/ trouvés (pack : à côté de routage.py ; dépôt : racine)."""
    here = Path(__file__).resolve().parent
    cands = [here / "mesSkillsPerso", here.parent / "mesSkillsPerso"]
    return [d for d in dict.fromkeys(cands) if d.is_dir()]


def _assurer_readme_perso(d: Path) -> None:
    r = d / "README.md"
    if not r.exists():
        r.write_text(PERSO_README, encoding="utf-8")


def _sanitize_fm(v: str) -> str:
    """Nettoie une valeur de frontmatter : pas de < > \" (injection), espaces tassés."""
    return re.sub(r"\s+", " ", v.replace("<", " ").replace(">", " ").replace('"', " ")).strip()


def normaliser_perso(txt: str, fname: str, num: int) -> str:
    """Convertit un fichier utilisateur quelconque en skill TEMPLATE-v2 complète."""
    import datetime
    m = re.match(r"---\n(.*?)\n---\n?", txt, re.S)
    fm, body = (m.group(1), txt[m.end():]) if m else ("", txt)
    g = lambda k: (re.search(rf'^{k}: "(.*)"$', fm, re.M) or [None, ""])[1]
    def gl(k):
        mm = re.search(rf"^{k}: \[(.*)\]$", fm, re.M)
        return [x.strip().strip('"') for x in mm.group(1).split(",") if x.strip()] if mm else []
    h = re.search(r"^#{1,3}\s+(.+)$", body, re.M)
    nom = _sanitize_fm(g("nom") or (h.group(1) if h else Path(fname).stem))[:120] or Path(fname).stem
    emoji = g("emoji") or "\U0001f3af"
    domaine = _sanitize_fm(g("domaine") or "Perso") or "Perso"
    signal = _sanitize_fm(g("signal") or g("description") or "")
    if not signal:
        paras = [p.strip() for p in re.split(r"\n\s*\n", body)
                 if p.strip() and not p.lstrip().startswith("#")]
        signal = re.sub(r"\s+", " ", paras[0]) if paras else nom
    if len(signal) > 1024:
        signal = signal[:1021] + "..."
    mot_cle = _sanitize_fm(g("mot_cle") or " ".join(t for t in tokens(nom) if len(t) >= 4)[:120] or norm(nom))
    nom_court = _sanitize_fm(g("nom_court") or nom)[:30]
    syns = [s for s in gl("synonymes") if s and not any(c in s for c in '<>"')][:8] or [norm(nom)]
    date_ajout = g("date_ajout") or datetime.date.today().strftime("%Y-%m")
    if not re.fullmatch(r"\d{4}-\d{2}", date_ajout):
        date_ajout = datetime.date.today().strftime("%Y-%m")
    # sections du body -> mapping par titres
    secs, cur, buf = {}, None, []
    for line in body.splitlines():
        hh = re.match(r"^#{2,4}\s+(.+)$", line)
        if hh:
            if cur is not None:
                secs[cur] = "\n".join(buf).strip()
            cur, buf = hh.group(1).strip().lower(), []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        secs[cur] = "\n".join(buf).strip()

    def trouve(*cles):
        for k, v in secs.items():
            if any(c in k for c in cles):
                return v
        return ""

    def bullets(s, defaut):
        if not s:
            return f"- {defaut}"
        lignes = [l.strip().lstrip("- ").strip() for l in s.splitlines() if l.strip()]
        return "\n".join(f"- {l}" for l in lignes) if len(lignes) > 1 else f"- {lignes[0]}"

    objectif = trouve("objectif", "description", "but") or signal
    triggers = bullets(trouve("trigger", "quand", "utilise"), f"la demande concerne : {nom_court}")
    hors = bullets(trouve("hors", "périmètre", "perimetre", "pas pour"),
                   "ce qui ne relève pas de cette skill perso")
    gardes = bullets(trouve("garde", "règle", "regle", "sécurité", "securite"),
                     "GF-01 : rester factuel, ne rien inventer")
    instr = trouve("instruction", "système", "system", "comportement", "rôle", "role")
    if instr and not instr.startswith("Tu es"):
        instr = "Tu es l'assistant perso de l'utilisateur sur ce sujet. " + instr
    elif not instr:
        instr = f"Tu es l'assistant perso de l'utilisateur pour « {nom_court} ». Tu appliques strictement le contenu de cette skill."
    inputs = bullets(trouve("input", "entrée", "donnée", "donnee"), "la demande de l'utilisateur et son contexte")
    methode = trouve("méthode", "etape", "étape", "process", "procédure", "procedure")
    if not re.search(r"(?m)^\s*1\.", methode):
        methode = "1. Comprendre précisément la demande.\n2. Appliquer la méthode décrite dans cette skill.\n3. Livrer une réponse claire, factuelle et vérifiable."
    sorties = bullets(trouve("sortie", "livrable"), "la réponse attendue par l'utilisateur")
    exemple = trouve("exemple", "prompt")
    if "«" not in exemple:
        exemple = f"« {nom_court} : <demande concrète de l'utilisateur> »"
    cas = trouve("cas", "usage")
    if "skill" not in cas.lower():
        cas = (cas + "\n" if cas else "") + f"Usage perso : {nom_court} ; le catalogue skillAISlop complète (skills 0-1799)."
    syns_s = ", ".join(f'"{s}"' for s in syns)
    L = ["---", f"num: {num}", f'date_ajout: "{date_ajout}"', f'nom: "{nom}"', f'emoji: "{emoji}"',
         f'domaine: "{domaine}"', f'signal: "{signal}"', f'mot_cle: "{mot_cle}"',
         f'nom_court: "{nom_court}"', 'branche: "K"', f"synonymes: [{syns_s}]",
         "cross_refs: []", 'tags: ["perso"]', "---", "",
         f"## {num}. {emoji} {nom}", "",
         "> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD", "",
         f"**Objectif** : {objectif}", "",
         "**Quand l'utiliser (triggers)** :", triggers, "",
         "**Hors périmètre** :", hors, "",
         "**Garde-fous** :", gardes, "",
         "**Instructions système** :", instr, "",
         "**Inputs requis** :", inputs, "",
         "**Méthode** :", methode, "",
         "**Sorties attendues** :", sorties, "",
         "**Exemple de prompt** :", f"> « {exemple.strip('« »')} »", "",
         f"**Cas d'usage** : {cas}", "",
         "**Checklist QA interne** :", "- [ ] Garde-fous respectés", "- [ ] Livrable conforme à la demande", "",
         "**Definition of done** :", "- [ ] Livrable produit et relu", "- [ ] Limites du périmètre rappelées", "",
         "---"]
    return "\n".join(L) + "\n"


def perso_conforme(txt: str) -> bool:
    """Un fichier perso est déjà au template (frontmatter num + date_ajout + 12 sections)."""
    m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
    if not m:
        return False
    fm = m.group(1)
    if not (re.search(r"^num: \d+$", fm, re.M) and re.search(r'^date_ajout: "\d{4}-\d{2}"$', fm, re.M)):
        return False
    return all(re.search(p, txt, re.M) for p in SECTIONS_PERSO_RE)


def ingerer_perso(db: sqlite3.Connection) -> int:
    """Ingère mesSkillsPerso/*.md dans skills_perso (conversion auto au template)."""
    fichiers = []
    for d in dossiers_perso():
        _assurer_readme_perso(d)
        fichiers += [f for f in sorted(d.glob("*.md")) if not f.name.lower().startswith("readme")]
    if not fichiers:
        return 0
    maxnum = db.execute("SELECT COALESCE(MAX(num),0) FROM skills_perso").fetchone()[0]
    n = 0
    for f in fichiers:
        txt = f.read_text(encoding="utf-8")
        if not perso_conforme(txt):
            maxnum += 1
            txt = normaliser_perso(txt, f.name, maxnum)
            f.write_text(txt, encoding="utf-8")  # auto-format au template, en place (jamais supprimé)
        fm = re.match(r"---\n(.*?)\n---\n", txt, re.S).group(1)
        g = lambda k: (re.search(rf'^{k}: "(.*)"$', fm, re.M) or [None, ""])[1]
        def gl(k):
            mm = re.search(rf"^{k}: \[(.*)\]$", fm, re.M)
            return [x.strip().strip('"') for x in mm.group(1).split(",") if x.strip()] if mm else []
        num = int(re.search(r"^num: (\d+)$", fm, re.M).group(1))
        nom, dom = g("nom"), g("domaine") or "Perso"
        sig, mc, nc, da = g("signal"), g("mot_cle"), g("nom_court"), g("date_ajout")
        syns = [s for s in gl("synonymes") if s and not any(c in s for c in '<>"')]
        db.execute("INSERT OR REPLACE INTO skills_perso VALUES (?,?,?,?,?,?,?,?,?,?)",
                   (num, nom, dom, sig, mc, nc, "K", ";".join(syns), da, f.name))
        db.execute("INSERT INTO perso_fts(num, nom, signal, mot_cle, nom_court, domaine) VALUES (?,?,?,?,?,?)",
                   (num, nom, sig, mc, nc, dom))
        for s in syns:
            db.execute("INSERT OR REPLACE INTO perso_synonymes VALUES (?,?,?)", (s, norm(s), num))
        if mc:
            db.execute("INSERT OR REPLACE INTO perso_mots_cles VALUES (?,?)", (norm(mc), num))
        n += 1
    db.commit()
    return n


def cmd_perso(add: str | None, convert: bool) -> int:
    if add:
        src = Path(add)
        if not src.exists():
            print(f"❌ {add} introuvable")
            return 1
        dirs = dossiers_perso()
        d = dirs[0] if dirs else (Path(__file__).resolve().parent / "mesSkillsPerso")
        d.mkdir(parents=True, exist_ok=True)
        _assurer_readme_perso(d)
        dst = d / src.name
        dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"✅ copié dans {dst}")
        print("   conversion au template + ingestion au prochain : python3 routage.py build")
        return 0
    if convert:
        n = 0
        for d in dossiers_perso():
            _assurer_readme_perso(d)
            maxnum = 0
            for f in sorted(d.glob("*.md")):
                if f.name.lower().startswith("readme"):
                    continue
                txt = f.read_text(encoding="utf-8")
                if not perso_conforme(txt):
                    m = re.search(r"^num: (\d+)$", txt.split("---")[1] if txt.startswith("---") else "", re.M)
                    maxnum += 1
                    num = int(m.group(1)) if m else maxnum
                    f.write_text(normaliser_perso(txt, f.name, num), encoding="utf-8")
                    n += 1
                    print(f"   converti : {f.name} (P{num})")
        print(f"✅ {n} fichier(s) converti(s) au template — puis : python3 routage.py build")
        return 0
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    try:
        rows = db.execute("SELECT * FROM skills_perso ORDER BY num").fetchall()
    except sqlite3.OperationalError:
        rows = []
    db.close()
    print(f"⭐ {len(rows)} skill(s) perso (prioritaires au routage) dans mesSkillsPerso/ :")
    for r in rows:
        print(f"  P{r['num']} · {r['nom']} · [{r['domaine']}] · {r['fichier']} · date_ajout {r['date_ajout']}")
    if not rows:
        print("  (vide — dépose un .md dans mesSkillsPerso/ ou : routage.py perso --add ma-skill.md)")
    return 0


def chercher(db: sqlite3.Connection, query: str, top: int, lang: str = "fr") -> dict:
    q = norm(query)
    qt = tokens(query)
    qn = q  # forme normalisée hoistée (évite de re-normaliser dans les boucles)
    qt_forts = [t for t in qt if len(t) >= 3]
    res = {"exact": [], "fts": [], "vec": [], "flou": [], "pistes": [],
           "domaines": [], "direct": None, "perso": []}
    vus = set()
    sfx = "" if lang == "fr" else "_" + re.sub(r"[^a-z0-9]", "", lang.lower())
    t_sk, t_fts, t_vec = f"skills{sfx}", f"skills_fts{sfx}", f"skills_vec{sfx}"
    if lang != "fr" and not db.execute("SELECT 1 FROM sqlite_master WHERE name=?", (t_sk,)).fetchone():
        lang = "fr"  # aucune traduction pour cette langue -> FR
        sfx = ""
        t_sk, t_fts, t_vec = "skills", "skills_fts", "skills_vec"
    res["lang"] = lang

    def cand(num, nom, domaine, signal, voie, cible, score=None):
        d = {"num": num, "nom": nom, "domaine": domaine, "signal": signal,
             "voie": voie, "cible": cible, "section": f"## {num}."}
        if score is not None:
            d["score"] = score
        return d

    # 0) renvoi direct « skill N » (n'importe où dans la demande)
    m = re.search(r"skill (\d+)", q)
    if m:
        r = db.execute(f"SELECT num, nom, domaine, signal FROM {t_sk} WHERE num=?",
                       (int(m.group(1)),)).fetchone() \
            or db.execute("SELECT num, nom, domaine, signal FROM skills WHERE num=?",
                          (int(m.group(1)),)).fetchone()
        if r:
            res["direct"] = cand(r["num"], r["nom"], r["domaine"],
                                 r["signal"] or "(routeur)", "direct", None)

    # 0b) skills perso (mesSkillsPerso/) : PRIORITAIRES si elles cadrent avec la demande
    # (tables petites : on scanne tout et on valide par recouvrement de tokens,
    #  robuste aux apostrophes qui cassent instr())
    try:
        mp = re.search(r"perso (\d+)", q)
        if mp:
            r = db.execute("SELECT num, nom, domaine, signal, fichier FROM skills_perso WHERE num=?",
                           (int(mp.group(1)),)).fetchone()
            if r:
                res["perso"].append({**cand(r["num"], r["nom"], r["domaine"],
                                            r["signal"] or "(perso)", "direct perso", None),
                                     "perso": True, "fichier": r["fichier"]})
        pvus = {c["num"] for c in res["perso"]}
        qts = set(qt_forts)

        def perso_hit(r, voie, cible, score=None):
            res["perso"].append({**cand(r["num"], r["nom"], r["domaine"], r["signal"],
                                        voie, cible, score),
                                 "perso": True, "fichier": r["fichier"]})
            pvus.add(r["num"])

        if qn:
            for r in db.execute(
                "SELECT m.mot_cle_norm AS mc, p.num, p.nom, p.domaine, p.signal, p.fichier "
                "FROM perso_mots_cles m JOIN skills_perso p ON p.num = m.num").fetchall():
                if r["num"] in pvus:
                    continue
                mc = r["mc"]
                if mc == qn or (len(qn) >= 5 and mc in qn) or (len(mc) >= 5 and qn in mc):
                    perso_hit(r, "perso mot-clé", mc)
                    continue
                inter = set(tokens(mc)) & qts
                if inter and any(len(t) >= 5 for t in inter):
                    perso_hit(r, "perso mot-clé", mc)
            for r in db.execute(
                "SELECT s.synonyme, s.synonyme_norm AS sn, p.num, p.nom, p.domaine, p.signal, p.fichier "
                "FROM perso_synonymes s JOIN skills_perso p ON p.num = s.num").fetchall():
                if r["num"] in pvus:
                    continue
                sn = r["sn"]
                inter = set(tokens(r["synonyme"])) & qts
                if (qn and (sn in qn or qn in sn)) or (inter and any(len(t) >= 5 for t in inter)):
                    perso_hit(r, "perso synonyme", r["synonyme"])
        if qt_forts:
            for op, match in (("AND", " ".join(f'"{t}"*' for t in qt_forts)),
                              ("OR", " OR ".join(f'"{t}"*' for t in qt_forts))):
                try:
                    hits = db.execute(
                        "SELECT perso_fts.num, perso_fts.nom, perso_fts.domaine, perso_fts.signal, "
                        "p.fichier, bm25(perso_fts, 0.0, 2.0, 6.0, 10.0, 3.0, 1.0) AS score "
                        "FROM perso_fts JOIN skills_perso p ON p.num = perso_fts.num "
                        "WHERE perso_fts MATCH ? ORDER BY score LIMIT ?",
                        (match, top)).fetchall()
                except sqlite3.OperationalError:
                    continue
                for r in hits:
                    if r["num"] in pvus:
                        continue
                    if op == "OR" and not _fts_valide(r, qt_forts):
                        continue
                    perso_hit(r, "perso fts", None, round(r["score"], 2))
                if res["perso"]:
                    break
    except sqlite3.OperationalError:
        pass  # base sans tables perso (vieux skills.db) : aucune skill perso

    # 1) mot-clé canonique : égalité puis inclusion, en SQL sur mots_cles (indexé)
    if qn:
        rows_mc = db.execute(
            "SELECT m.num, s.nom, s.domaine, s.signal, m.mot_cle_norm AS mot_cle FROM mots_cles m "
            "JOIN " + t_sk + " s ON s.num = m.num "
            "WHERE (m.mot_cle_norm = ? OR (length(?) >= 5 AND instr(m.mot_cle_norm, ?) > 0) "
            "   OR (length(m.mot_cle_norm) >= 5 AND instr(?, m.mot_cle_norm) > 0)) AND m.lang = ?",
            (qn, qn, qn, qn, lang)).fetchall()
        for r in rows_mc:
            res["exact"].append(cand(r["num"], r["nom"], r["domaine"],
                                     r["signal"], "mot-clé", r["mot_cle"]))
            vus.add(r["num"])
    for r in db.execute("SELECT m.num, s.nom, s.domaine, s.signal, m.mot_cle_norm AS mot_cle FROM mots_cles m "
                       "JOIN " + t_sk + " s ON s.num = m.num WHERE m.lang = ?", (lang,)):
        if r["num"] in vus:
            continue
        kwt = set(tokens(r["mot_cle"]))
        if kwt and kwt <= set(qt):
            res["exact"].append(cand(r["num"], r["nom"], r["domaine"],
                                     r["signal"], "mot-clé", r["mot_cle"]))
            vus.add(r["num"])
    res["exact"] = res["exact"][:top]

    # 2) synonymes : d'abord en SQL (inclusion dans la requête normalisée), puis
    #    affinage Python uniquement sur les candidats SQL (évite de scanner 1258 lignes en Python)
    if qn:
        rows_syn = db.execute(
            "SELECT s.synonyme, s.poids, k.num, k.nom, k.domaine, k.signal FROM synonymes s "
            "JOIN " + t_sk + " k ON k.num = s.num "
            "WHERE (instr(?, s.synonyme_norm) > 0 OR instr(s.synonyme_norm, ?) > 0) AND s.lang = ?",
            (qn, qn, lang)).fetchall()
    else:
        rows_syn = []
    for r in rows_syn:
        sn = r["synonyme_norm"] if "synonyme_norm" in r.keys() else norm(r["synonyme"])
        touche = sn in qn or (len(sn) >= 6 and any(len(t) >= 7 and t[:7] == sn[:7] for t in qt))
        if not touche:
            continue
        poids = r["poids"] if "poids" in r.keys() else 1.0
        if r["num"] in vus:
            # plusieurs synonymes matchent la même skill : garder le MEILLEUR poids
            # (un synonyme spécifique fort prime sur un synonyme générique faible)
            for lst in (res["exact"], res.get("exact_faible", [])):
                for c in lst:
                    if c["num"] == r["num"] and poids >= 0.5 and c["voie"] == "synonyme-faible":
                        c["voie"] = "synonyme"
                        c["cible"] = r["synonyme"]
                        if c in res.get("exact_faible", []):
                            res["exact_faible"].remove(c)
                            res["exact"].append(c)
            continue
        c = cand(r["num"], r["nom"], r["domaine"], r["signal"],
                 "synonyme" if poids >= 0.5 else "synonyme-faible", r["synonyme"])
        # P0-1 : synonyme générique (poids IDF faible) reste dans exact (exit 0)
        # mais classé APRÈS les synonymes spécifiques → perd le rang RRF face au mot-clé/FTS
        (res["exact"] if poids >= 0.5 else res.setdefault("exact_faible", [])).append(c)
        vus.add(r["num"])
    res["exact"] = (res["exact"] + res.pop("exact_faible", []))[:top]

    # 3) FTS5 : préfixes, ET puis OU, bm25 pondéré
    if qt_forts:
        poids = f"bm25({t_fts}, 0.0, 2.0, 6.0, 10.0, 3.0, 1.0)"
        for op in ("AND", "OR"):
            match = (" ".join(f'"{t}"*' for t in qt_forts) if op == "AND"
                     else " OR ".join(f'"{t}"*' for t in qt_forts))
            try:
                hits = db.execute(
                    "SELECT num, nom, domaine, signal, mot_cle, nom_court, "
                    + poids + " AS score "
                    f"FROM {t_fts} WHERE {t_fts} MATCH ? "
                    "ORDER BY score LIMIT ?", (match, top + len(vus))).fetchall()
            except sqlite3.OperationalError:
                continue
            for r in hits:
                if r["num"] in vus:
                    continue
                if op == "OR" and not _fts_valide(r, qt_forts):
                    continue
                res["fts"].append(cand(r["num"], r["nom"], r["domaine"],
                                        r["signal"], "fts", None,
                                        round(r["score"], 2)))
                vus.add(r["num"])
            if res["fts"]:
                break
        res["fts"] = res["fts"][:top]

    # 3a) passe vectorielle sqlite-vec (cosinus sur embeddings locaux) :
    #     capture les périphrases sans mot-clé exact, en complément du FTS5
    try:
        has_vec = db.execute(
            "SELECT 1 FROM sqlite_master WHERE name=?", (t_vec,)).fetchone()
    except sqlite3.Error:
        has_vec = None
    if has_vec and any(len(t) >= 5 for t in qt):  # hash 32 dims bruité sur requêtes < 5 lettres
        qvec = embed_hash(query)
        try:
            hits = db.execute(
                "SELECT v.num, s.nom, s.domaine, s.signal, 1 - distance AS cos "
                f"FROM {t_vec} v JOIN {t_sk} s ON s.num = v.num "
                "WHERE v.embedding MATCH ? AND k = ? "
                "ORDER BY distance LIMIT ?",
                (qvec, top, top)).fetchall()
            for r in hits:
                if r["num"] in vus:
                    continue
                cos = r["cos"]
                if cos < VEC_SEUIL:
                    continue
                res["vec"].append(cand(r["num"], r["nom"], r["domaine"],
                                       r["signal"], "vec", None, round(cos, 3)))
                vus.add(r["num"])
        except sqlite3.OperationalError:
            pass  # extension absente ou table manquante : on ignore
        res["vec"] = res["vec"][:top]
        if not res["vec"]:
            try:
                r0 = db.execute(
                    "SELECT v.num, s.nom, s.domaine, s.signal, 1 - distance AS cos "
                    f"FROM {t_vec} v JOIN {t_sk} s ON s.num = v.num "
                    "WHERE v.embedding MATCH ? AND k = 1 ORDER BY distance",
                    (qvec,)).fetchone()
                if r0 and r0["cos"] >= VEC_PISTE and r0["num"] not in vus:
                    # P0-2 : une piste vec doit partager au moins un token avec la requête
                    if set(qt) & set(tokens(r0["nom"] + " " + r0["signal"])):
                        res["pistes"].append(cand(r0["num"], r0["nom"], r0["domaine"],
                                                  r0["signal"], "piste-vec", None,
                                                  round(r0["cos"], 3)))
            except sqlite3.OperationalError:
                pass

    # 3b) passe floue : trigrammes communs (fautes de frappe), si rien trouvé ;
    #     en dessous du seuil, les meilleurs recouvrements deviennent pistes
    if not res["exact"] and not res["fts"] and not res["vec"] and not res["pistes"]:
        pistes_vues = set()
        for ratio, nb, t, r in proches_trigrammes_sql(db, qt_forts, 0.65, vus, lang):
            mots = mots_de(r)
            uniques = set(qt_forts)
            n = sum(1 for t2 in uniques if mot_match_large(t2, mots))
            garde = (n >= 2 if len(uniques) >= 2 else n >= 1)
            if nb >= 3 and ratio >= 0.6 and len(res["flou"]) < top and garde:
                res["flou"].append(cand(r["num"], r["nom"], r["domaine"],
                                        r["signal"], "approx", t,
                                        round(ratio, 2)))
                vus.add(r["num"])
            elif r["num"] not in pistes_vues and len(res["pistes"]) < top:
                res["pistes"].append(cand(r["num"], r["nom"], r["domaine"],
                                          r["signal"], "piste", t,
                                          round(ratio, 2)))
                pistes_vues.add(r["num"])

    # 4) domaines plausibles
    if not res["exact"] and not res["fts"] and not res["vec"] and not res["flou"] and not res["pistes"]:
        for d in db.execute("SELECT domaine, mots_cles FROM domaines"):
            dt = set(tokens(d["domaine"])) | set(tokens(d["mots_cles"]))
            commun = dt & set(qt)
            if commun:
                n = db.execute(f"SELECT COUNT(*) FROM {t_sk} WHERE domaine=?",
                               (d["domaine"],)).fetchone()[0]
                res["domaines"].append({"domaine": d["domaine"], "nb": n,
                                        "mots": sorted(commun)[:4]})
        res["domaines"] = sorted(res["domaines"],
                                 key=lambda x: -len(x["mots"]))[:3]

    # 4a) bonus freshness : si la requête contient une année (ex. 2027) et la skill a ce tag
    try:
        annees = set(re.findall(r"\b(20\d\d)\b", q))
        if annees:
            for c in (res["exact"] + res["fts"] + res["vec"] + res["flou"] + res["pistes"]):
                tags_c = {r["tag"] for r in db.execute("SELECT tag FROM tags WHERE num=?", (c["num"],))}
                if annees & tags_c and "score" in c:
                    c["score"] = round(c["score"] + 0.03, 3)
                    c["bonus_fresh"] = 0.03
    except sqlite3.OperationalError:
        pass

    # 4b) bonus popularité : les skills du top-N (les plus utilisées) gagnent un léger bonus
    try:
        top_pop = {r["num"] for r in db.execute(
            "SELECT num FROM popularite ORDER BY score DESC LIMIT 20")}
        for c in (res["exact"] + res["fts"] + res["vec"] + res["flou"] + res["pistes"]):
            if c["num"] in top_pop and "score" in c:
                c["score"] = round(c["score"] + 0.05, 3)
                c["bonus_pop"] = 0.05
    except sqlite3.OperationalError:
        pass

    # 5) bonus cross-ref : un candidat référencé par un autre candidat bien placé gagne un bonus
    tous = res["exact"] + res["fts"] + res["vec"] + res["flou"] + res["pistes"]
    if tous:
        refs = {}
        for c in tous:
            for r in db.execute("SELECT refs FROM cross_refs WHERE num=?", (c["num"],)):
                pass
        # lire cross_refs depuis la table dédiée (créée au build) ou le champ texte
        try:
            rows = db.execute("SELECT num, refs FROM cross_refs").fetchall()
            for row in rows:
                refs[row["num"]] = {int(x) for x in row["refs"].split(",") if x.strip()}
        except sqlite3.OperationalError:
            pass
        top_nums = {c["num"] for c in (res["exact"][:2] + res["fts"][:2])}
        for c in tous:
            bonus = 0.0
            for t in top_nums:
                if c["num"] in refs.get(t, set()) or t in refs.get(c["num"], set()):
                    bonus += 0.10
            if bonus and "score" in c:
                c["score"] = round(c["score"] + bonus, 3)
                c["bonus_xref"] = round(bonus, 3)
        # re-trier les listes principales par score décroissant
        for k in ("exact", "fts", "vec", "flou"):
            res[k] = sorted(res[k], key=lambda c: -(c.get("score") or 0))[:top]

    # 6) fusion RRF (k=60) en UN SEUL passage avec top-K précoce (évite un 2e parcours + tri complet)
    K_RRF = 60
    fusion = {}
    for voie, liste in (("exact", res["exact"][:top]), ("fts", res["fts"][:top]),
                        ("vec", res["vec"][:top]), ("flou", res["flou"][:top])):
        for rang, c in enumerate(liste):
            e = fusion.get(c["num"])
            if e is None:
                if len(fusion) >= top * 3:  # top-K précoce : on garde 3x top candidats max
                    continue
                e = fusion[c["num"]] = {"c": c, "rrf": 0.0, "voies": []}
            # P0-1 : un synonyme générique (poids IDF faible) contribue moitié moins au RRF
            w = 0.5 if c.get("voie") == "synonyme-faible" else 1.0
            e["rrf"] += w / (K_RRF + rang)
            e["voies"].append(voie)
    res["fusion"] = [e["c"] for e in sorted(fusion.values(), key=lambda v: -v["rrf"])[:top]
                     for e in [dict(e, c=dict(e["c"], rrf=round(e["rrf"], 4)))]]
    return res


def _journaliser(db: sqlite3.Connection, query: str) -> None:
    """Consigne une demande non routée (exit 2) — clé = demande normalisée."""
    try:
        db.execute(
            "INSERT INTO non_routees(demande, nb, dernier) "
            "VALUES (?, 1, datetime('now')) "
            "ON CONFLICT(demande) DO UPDATE "
            "SET nb = nb + 1, dernier = datetime('now')", (norm(query),))
        db.commit()
    except sqlite3.OperationalError:
        pass  # base ancienne sans journal


def detect_lang(q: str) -> str:
    """Heuristique stdlib (stopwords FR/EN/NL) -> code langue 2 lettres, défaut fr."""
    ql = q.lower()
    fr = len(re.findall(r"\b(le|la|les|un|une|des|du|et|est|pas|comment|pourquoi|quand|où|écrire|créer|faire|aider|avec|pour|dans|sur|je|tu|il|nous|vous|mon|ma|mes|ton|son|notre|votre)\b", ql))
    en = len(re.findall(r"\b(the|and|is|are|was|not|how|what|why|when|where|write|rewrite|create|make|help|with|for|from|this|that|please|can|could|i|you|he|she|we|they|my|your|his|her|our|their)\b", ql))
    nl = len(re.findall(r"\b(de|het|een|en|is|zijn|hoe|wat|waarom|wanneer|schrijven|maken|helpen|met|voor|van|deze|dat|kun|kunt|ik|jij|hij|wij|jullie|mijn|jouw|zijn|hun)\b", ql))
    if fr >= max(en, nl):
        return "fr"
    return "en" if en >= nl else "nl"


def cmd_route(query: str, top: int, as_json: bool, tag: str | None = None, lang: str | None = None) -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA cache_size=-8000")
    charger_vec(db)
    lang = (lang or detect_lang(query)).lower()
    if not re.fullmatch(r"[a-z]{2}", lang):
        lang = "fr"
    res = chercher(db, query, top, lang)
    if lang != "fr" and not any(res.get(k) for k in ("direct", "exact", "fts", "vec", "flou", "pistes", "perso")):
        res = chercher(db, query, top, "fr")  # fallback FR si rien en langue cible
        res["lang_fallback"] = "fr"
        lang = "fr"
    if tag:
        # pré-filtre optionnel par tag : ne garder que les skills taguées
        try:
            tag_nums = {r["num"] for r in db.execute("SELECT num FROM tags WHERE tag=?", (norm(tag),))}
            for k in ("exact", "fts", "vec", "flou", "pistes"):
                res[k] = [c for c in res[k] if c["num"] in tag_nums]
        except sqlite3.OperationalError:
            pass
    if res.get("perso"):
        candidats = res["perso"]  # mesSkillsPerso/ : prioritaires si elles cadrent
    else:
        candidats = ([res["direct"]] if res["direct"] else []) + res.get("fusion") \
            or ([res["direct"]] if res["direct"] else []) + res["exact"] + res["fts"] + res["vec"] + res["flou"]
    # chaîne de skills composables : si le gagnant a des depends_on, les proposer ensuite
    if candidats:
        try:
            nxt = [r["next"] for r in db.execute("SELECT next FROM depends_on WHERE num=? ORDER BY next", (candidats[0]["num"],))]
            if nxt:
                noms = {r["num"]: r["nom"] for r in db.execute("SELECT num, nom FROM skills WHERE num IN (%s)" % ",".join(map(str, nxt)))}
                res["chaine"] = [{"num": n, "nom": noms.get(n, "")} for n in nxt]
        except sqlite3.OperationalError:
            pass
    if candidats:
        try:
            lf = db.execute("SELECT fichier FROM lang WHERE num=? AND lang=?", (candidats[0]["num"], lang)).fetchone()
            if lf:
                candidats[0]["fichier"] = f"skills/{lf['fichier']}"
        except sqlite3.OperationalError:
            pass
    pistes_vec = any(p["voie"] == "piste-vec" for p in res["pistes"])
    code = 0 if candidats else (1 if (res["domaines"] or pistes_vec) else 2)
    if code == 2:
        _journaliser(db, query)
    try:
        db.execute("PRAGMA wal_checkpoint(PASSIVE)")  # checkpoint WAL après écriture de session
        db.execute("INSERT INTO routes(demande, code, voie, num) "
                   "VALUES (?,?,?,?)",
                   (norm(query), code,
                    candidats[0]["voie"] if candidats else
                    ("domaine" if code == 1 else "rien"),
                    candidats[0]["num"] if candidats else None))
        db.commit()
    except sqlite3.OperationalError:
        pass
    db.close()
    if as_json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return code
    for r in res.get("perso", []):
        print(f"⭐ Perso P{r['num']} · {r['nom']} · [{r['domaine']}] · mesSkillsPerso/{r['fichier']}")
        cible = f" « {r['cible']} »" if r.get("cible") else ""
        print(f"  ↳ {r['voie']}{cible} — signal : {r['signal']}")
    if res["direct"]:
        d = res["direct"]
        print(f"◆ Skill {d['num']} · {d['nom']} · [{d['domaine']}]")
        print(f"  ↳ renvoi direct — signal : {d['signal']}")
    if res.get("chaine"):
        print("  ↳ ensuite : " + " → ".join(f"skill {c['num']} ({c['nom']})" for c in res["chaine"]))
    for r in res["exact"]:
        print(f"◆ Skill {r['num']} · {r['nom']} · [{r['domaine']}]")
        print(f"  ↳ {r['voie']} « {r['cible']} » — signal : {r['signal']}")
    for r in res["fts"]:
        print(f"◇ Skill {r['num']} · {r['nom']} · [{r['domaine']}]")
        print(f"  ↳ full-text (score {r['score']}) — signal : {r['signal']}")
    for r in res["vec"]:
        print(f"◈ Skill {r['num']} · {r['nom']} · [{r['domaine']}]")
        print(f"  ↳ vectoriel (cosinus {r['score']}) — signal : {r['signal']}")
    for r in res["flou"]:
        print(f"◇ Skill {r['num']} · {r['nom']} · [{r['domaine']}]")
        print(f"  ↳ approx (trigrammes « {r['cible']} », {r['score']}) "
              f"— signal : {r['signal']}")
    if code == 0:
        c0 = candidats[0]
        sec = ('mesSkillsPerso/' + c0['fichier']) if c0.get('perso') else (c0.get('fichier') or c0['section'])
        print(f"⤳ Section : {sec}  (lang: {lang})")
    elif res["domaines"]:
        for d in res["domaines"]:
            print(f"◎ Domaine plausible : {d['domaine']} ({d['nb']} skills) "
                  f"— mots reconnus : {', '.join(d['mots'])}")
    else:
        for p in res["pistes"]:
            print(f"○ Piste : skill {p['num']} · {p['nom']} — approx "
                  f"({p['score']}, « {p['cible']} »)")
        print("✖ Aucune correspondance — consigné au journal "
              "(misses --suggest pour un synonyme proposé). "
              "Répondre en direct, puis suggérer la skill 17 (création) si "
              "le besoin est récurrent ; ajouter un synonyme dans "
              "routage-sql-skills si récurrent.")
    return code


# ---------------------------------------------------------------------------
# generate : base -> canvas
# ---------------------------------------------------------------------------
RE_SOMMAIRE_LIGNE = re.compile(r"^\| (\d+) \| .* \| \S[^|]* \|$")
RE_LIGNE_TABLE = re.compile(r"^\| .+ \| \d+ \| \S[^|]* \|$")
RE_SEPARATEUR = re.compile(r"^\| \*\*[^*]+\*\* \| \| \|$")
RE_LIGNE_CARTE = re.compile(r"^\| [^|]+ \| [^|]+ \|$")
RE_Q6_LIGNE = re.compile(r"^(\s*Q6 -->\|[^|]+\| D(\d+)\[).*(\])\s*$")
HDR_CARTE = "| Domaine | Mots-clés déclencheurs |"
HDR_TABLE = "| Signal dans la demande | → Skill | Domaine |"


def charger():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    skills = {r["num"]: dict(r) for r in db.execute("SELECT * FROM skills")}
    domaines = [(r["domaine"], r["mots_cles"])
                for r in db.execute("SELECT * FROM domaines")]
    db.close()
    nums = sorted(skills)
    assert nums == list(range(0, max(nums) + 1)), "numéros non contigus"
    assert len(domaines) == len(set(d for d, _ in domaines)), "domaines dupliqués"
    doms_db = {d for d, _ in domaines}
    for n in nums:
        s = skills[n]
        assert s["domaine"] in doms_db, f"skill {n} : domaine inconnu"
        if n == 0:
            continue
        for champ in ("signal", "mot_cle", "branche"):
            assert s[champ], f"skill {n} : champ « {champ} » vide"
        assert re.fullmatch(r"D\d+|K", s["branche"]), f"skill {n} : branche invalide"
        if s["branche"].startswith("D"):
            assert s["nom_court"], f"skill {n} : nom_court vide"
    return skills, sorted(domaines, key=lambda x: dkey(x[0]))


def cmd_generate(canvas_path: Path, check: bool) -> int:
    skills, domaines = charger()
    ordre_dom = [d for d, _ in domaines]
    carte = [f"| {d} | {kw} |" for d, kw in domaines]
    bullets = []
    for d in ordre_dom:
        nums = sorted(n for n, s in skills.items() if n != 0 and s["domaine"] == d)
        assert nums, f"domaine « {d} » sans skill"
        entrees = " · ".join(f"« {skills[n]['mot_cle']} » → {n}" for n in nums)
        bullets.append(f"- **{d}** — {entrees}")
    table = []
    for d in ordre_dom:
        table.append(f"| **{d}** | | |")
        for n in sorted(n for n, s in skills.items()
                        if n != 0 and s["domaine"] == d):
            table.append(f"| {skills[n]['signal']} | {n} | {d} |")

    src = canvas_path.read_text(encoding="utf-8")
    lines = src.splitlines()
    changes = []

    # 1) sommaire (bloc contigu, ordonné par numéro — gère aussi les ajouts)
    idx = [i for i, l in enumerate(lines) if RE_SOMMAIRE_LIGNE.match(l)]
    assert idx, "sommaire : aucune ligne trouvée"
    assert idx == list(range(idx[0], idx[0] + len(idx))), "sommaire non contigu"
    nouvelles = [f"| {n} | {skills[n]['nom']} | {skills[n]['domaine']} |"
                 for n in sorted(skills)]
    if lines[idx[0]:idx[-1] + 1] != nouvelles:
        lines[idx[0]:idx[-1] + 1] = nouvelles
        changes.append(f"sommaire : {len(nouvelles)} lignes")

    # 2) carte des domaines
    start = None
    for i, l in enumerate(lines):
        if l == HDR_CARTE:
            assert start is None, "carte : ancre en double"
            start = i
    assert start is not None, "carte : ancre introuvable"
    end = start + 2
    while end < len(lines) and RE_LIGNE_CARTE.match(lines[end]):
        end += 1
    if lines[start + 2:end] != carte:
        lines[start + 2:end] = carte
        changes.append(f"carte des domaines : {len(carte)} lignes")

    # 3) index inversé
    idx = [i for i, l in enumerate(lines) if l.startswith("**Index inversé**")]
    assert len(idx) == 1, "index inversé : ancre introuvable"
    start = idx[0] + 1
    while not lines[start].startswith("- **"):
        start += 1
    end = start
    while end < len(lines) and lines[end].startswith("- **"):
        end += 1
    if lines[start:end] != bullets:
        lines[start:end] = bullets
        changes.append(f"index inversé : {len(bullets)} lignes")

    # 4) table de routage complète
    start = None
    for i, l in enumerate(lines):
        if l == HDR_TABLE:
            assert start is None, "table : ancre en double"
            start = i
    assert start is not None, "table : ancre introuvable"
    end = start + 2
    while end < len(lines) and (RE_LIGNE_TABLE.match(lines[end])
                                or RE_SEPARATEUR.match(lines[end])):
        end += 1
    if lines[start + 2:end] != table:
        lines[start + 2:end] = table
        changes.append(f"table de routage : {len(table) - len(ordre_dom)} lignes")

    # 5) branches D1-D26 de l'arbre de décision
    nb = 0
    for i, l in enumerate(lines):
        m = RE_Q6_LIGNE.match(l)
        if not m:
            continue
        branche = f"D{m.group(2)}"
        nums = sorted(n for n, s in skills.items() if s["branche"] == branche)
        assert nums, f"arbre : branche {branche} vide dans la base"
        contenu = " · ".join(f"{n} {skills[n]['nom_court']}" for n in nums)
        neuf = m.group(1) + contenu + "]"
        if l != neuf:
            lines[i] = neuf
            nb += 1
    if nb:
        changes.append(f"arbre de décision : {nb} branches mises à jour")

    nouveau = "\n".join(lines) + ("\n" if src.endswith("\n") else "")
    modifie = nouveau != src
    if modifie and not check:
        canvas_path.write_text(nouveau, encoding="utf-8")
    if modifie:
        print("⚠ Canvas désynchronisé :" if check else "✅ Canvas régénéré :")
        for c in changes:
            print("  -", c)
    else:
        print("✅ Canvas déjà synchronisé avec skills.db")
    return 1 if (check and modifie) else 0


# ---------------------------------------------------------------------------
# test : non-régression · misses : journal des exit 2
# ---------------------------------------------------------------------------

GOLDEN_Q = RACINE / "outils/golden_queries.txt"
GOLDEN_B = RACINE / "data/golden-routage.json"

def _gagnant(res):
    """Même logique que cmd_route : direct, sinon tête de la fusion RRF, sinon 1er candidat."""
    if res["direct"]:
        return res["direct"]["num"]
    if res.get("fusion"):
        return res["fusion"][0]["num"]
    for k in ("exact", "fts", "vec", "flou"):
        if res.get(k):
            return res[k][0]["num"]
    return None

def cmd_golden(update: bool) -> int:
    """P0-3 — golden set de régression du routage : rejoue des requêtes fixes et
    compare le gagnant courant au baseline data/golden-routage.json.
    --update régénère le baseline (à faire après une vague, tests au vert)."""
    import json
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    if not GOLDEN_Q.exists():
        raise SystemExit(f"{GOLDEN_Q} introuvable")
    queries = [l.strip() for l in GOLDEN_Q.read_text(encoding="utf-8").splitlines()
               if l.strip() and not l.startswith("#")]
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    charger_vec(db)
    if update:
        base = {q: _gagnant(chercher(db, q, 5)) for q in queries}
        GOLDEN_B.parent.mkdir(parents=True, exist_ok=True)
        GOLDEN_B.write_text(json.dumps(base, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        db.close()
        n = sum(1 for v in base.values() if v is not None)
        print(f"✅ golden baseline écrit : {len(base)} requêtes ({n} routées) -> {GOLDEN_B}")
        return 0
    if not GOLDEN_B.exists():
        db.close()
        raise SystemExit("baseline absent — lance : routage.py golden --update")
    base = json.loads(GOLDEN_B.read_text(encoding="utf-8"))
    ok, reg, errs = 0, [], 0
    for q in queries:
        if q not in base:
            continue
        num = _gagnant(chercher(db, q, 5))
        if num == base[q]:
            ok += 1
        elif num is None:
            errs += 1
            reg.append((q, base[q], "RIEN (exit 2)"))
        else:
            reg.append((q, base[q], num))
    db.close()
    total = ok + len(reg)
    if reg:
        print(f"❌ golden : {len(reg)}/{total} régressions de routage (gagnant attendu → obtenu) :")
        for q, attendu, obtenu in reg[:20]:
            print(f"  - « {q} » : attendu {attendu} → obtenu {obtenu}")
        print("→ si le changement est voulu (nouvelle skill légitime), régénère : routage.py golden --update")
        return 1
    print(f"✅ golden : {ok}/{total} requêtes stables (aucune régression)")
    return 0


def cmd_test() -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    echecs = []
    for demande, attendu in TESTS_ROUTAGE:
        res = chercher(db, demande, 5, "fr")
        trouves = ({r["num"] for r in res["exact"]}
                   | {r["num"] for r in res["fts"]}
                   | {r["num"] for r in res.get("vec", [])}
                   | {r["num"] for r in res["flou"]}
                   | ({res["direct"]["num"]} if res["direct"] else set()))
        if attendu is None:
            if trouves:
                echecs.append((demande, "aucune skill",
                               "des candidates trouvées"))
        elif attendu not in trouves:
            echecs.append((demande, attendu, sorted(trouves) or "rien"))
    for demande, attendu in TESTS_ROUTAGE_EN:
        res = chercher(db, demande, 5, "en")
        trouves = ({r["num"] for r in res["exact"]}
                   | {r["num"] for r in res["fts"]}
                   | {r["num"] for r in res.get("vec", [])}
                   | {r["num"] for r in res["flou"]}
                   | ({res["direct"]["num"]} if res["direct"] else set()))
        if attendu is None:
            if trouves:
                echecs.append((demande, "aucune skill", "des candidates trouvées"))
        elif attendu not in trouves:
            echecs.append((demande, attendu, sorted(trouves) or "rien"))
    total = len(TESTS_ROUTAGE) + len(TESTS_ROUTAGE_EN)
    db.close()
    if echecs:
        print(f"✖ {len(echecs)}/{total} tests en échec :")
        for demande, attendu, obtenu in echecs:
            print(f"  - « {demande} » : attendu {attendu}, obtenu {obtenu}")
        return 1
    print(f"✅ {total}/{total} tests de routage passés (fr: {len(TESTS_ROUTAGE)} · en: {len(TESTS_ROUTAGE_EN)})")
    return 0


def cmd_sonde(fichier, top):
    if not DB_PATH.exists():
        raise SystemExit('skills.db introuvable')
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    sujets = []
    for d in db.execute('SELECT domaine, mots_cles FROM domaines ORDER BY domaine'):
        for kw in re.findall('[a-z0-9-]+', norm(d['mots_cles'])):
            # sujets < 4 lettres ou stopwords = artefacts de sonde (ex. « ton », « pour »)
            if len(kw) >= 4 and kw not in STOPWORDS:
                sujets.append((kw, d['domaine']))
    for r in db.execute('SELECT num, signal, domaine FROM skills WHERE signal != "" ORDER BY num'):
        sujets.append((r['signal'], r['domaine']))
    couverts, partiels, gaps = [], [], []
    for sujet, domaine in sujets:
        res = chercher(db, sujet, top)
        nums = sorted({r['num'] for r in res['exact'] + res['fts'] + res.get('vec', []) + res['flou']}
                      | ({res['direct']['num']} if res['direct'] else set()))
        if nums:
            couverts.append((sujet, domaine, nums[:top]))
        elif res['pistes'] or res['domaines']:
            partiels.append((sujet, domaine, [q['num'] for q in res['pistes'][:top]],
                             [dd['domaine'] for dd in res['domaines']]))
        else:
            gaps.append((sujet, domaine))
    db.close()
    total = len(sujets)
    pc = len(couverts) * 100 // max(1, total)
    sep = chr(10)
    lignes = ['# Sonde de couverture', '',
              f'Total {total} sujets · Couverts {len(couverts)} ({pc}%) · Partiels {len(partiels)} · Gaps {len(gaps)}',
              '', '## Gaps (aucune candidate)', '']
    lignes += [f'- [{d}] {s}' for s, d in gaps] or ['- aucun']
    lignes += ['', '## Partiels (pistes/domaines seulement)', '']
    if partiels:
        for s, d, pistes, doms in partiels:
            lignes.append(f'- [{d}] {s} -> pistes {pistes} domaines {doms}')
    else:
        lignes.append('- aucun')
    lignes += ['', '## Echantillon couverts', '']
    for s, d, nums in couverts[:25]:
        lignes.append(f'- [{d}] {s} -> {nums}')
    rapport = sep.join(lignes) + sep
    if fichier:
        Path(fichier).write_text(rapport, encoding='utf-8')
        print(f'sonde: {len(couverts)}/{total} couverts ({pc}%) · {len(partiels)} partiels · {len(gaps)} gaps -> {fichier}')
    else:
        print(rapport)
    return 1 if gaps else 0

def cmd_misses(clear: bool, suggest: bool) -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    try:
        if clear:
            db.execute("DELETE FROM non_routees")
            db.commit()
            print("Journal des demandes non routées vidé.")
            return 0
        rows = db.execute("SELECT demande, nb, dernier FROM non_routees "
                          "ORDER BY nb DESC, dernier").fetchall()
        if suggest:
            if not rows:
                print("✅ Aucune demande non routée enregistrée.")
                return 0
            print("Suggestions (à ajouter dans SYNONYMES, puis build + test) :")
            code = 0
            for r in rows:
                print(f"  {r['nb']:>2}×  {r['demande']}")
                proches = proches_trigrammes(db, tokens(r["demande"]), 0.4)
                if proches:
                    ratio, nb, t, s = proches[0]
                    print(f"        → ajouter (\"{t}\", {s['num']})  "
                          f"# {s['nom']} — recouvrement {ratio:.0%}")
                else:
                    print("        → aucune piste : besoin non couvert, "
                          "envisager la skill 17 (création)")
                    code = 1
            return code
    except sqlite3.OperationalError:
        print("Journal absent (base ancienne) — relancer build.")
        return 2
    finally:
        db.close()
    if not rows:
        print("✅ Aucune demande non routée enregistrée.")
        return 0
    print(f"Demandes non routées ({len(rows)}) :")
    for r in rows:
        print(f"  {r['nb']:>2}×  {r['demande']}  (dernière : {r['dernier']})")
    print("→ exit 2 récurrent = ajouter un synonyme dans SYNONYMES puis "
          "build, ou `misses --suggest` pour une suggestion automatique.")
    return 1


def cmd_stats(clear: bool) -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    try:
        if clear:
            db.execute("DELETE FROM routes")
            db.commit()
            print("Statistiques de routage remises à zéro.")
            return 0
        total = db.execute("SELECT COUNT(*) FROM routes").fetchone()[0]
        if not total:
            print("✅ Aucun routage enregistré — stats alimentées par `route`.")
            return 0
        codes = dict(db.execute("SELECT code, COUNT(*) FROM routes "
                                "GROUP BY code"))
        voies = db.execute("SELECT voie, COUNT(*) FROM routes WHERE code = 0 "
                           "GROUP BY voie ORDER BY 2 DESC").fetchall()
        print(f"Routages de la session : {total}")
        print(f"  ✓ exit 0 : {codes.get(0, 0)} ({codes.get(0, 0) * 100 // total} %)"
              + (" — " + " · ".join(f"{v} {n}" for v, n in voies) if voies else ""))
        print(f"  ◐ exit 1 : {codes.get(1, 0)} (domaine plausible seulement)")
        print(f"  ✖ exit 2 : {codes.get(2, 0)} (cf. misses)")
    except sqlite3.OperationalError:
        print("Table des routages absente (base ancienne) — relancer build.")
        return 2
    finally:
        db.close()
    return 0


def cmd_bench(tours: int) -> int:
    if not CANVAS_PAR_DEFAUT.exists():
        raise SystemExit(f"canvas introuvable : {CANVAS_PAR_DEFAUT}")
    tmp = DB_PATH.with_name("bench.db")
    t0 = time.perf_counter()
    cmd_build(CANVAS_PAR_DEFAUT, tmp)
    build_s = time.perf_counter() - t0
    db = sqlite3.connect(tmp)
    db.row_factory = sqlite3.Row
    requetes = [d for d, _ in TESTS_ROUTAGE]
    tours = max(1, tours)
    durees = []
    for _ in range(tours):
        for q in requetes:
            t = time.perf_counter()
            chercher(db, q, 5)
            durees.append(time.perf_counter() - t)
    db.close()
    tmp.unlink()
    taille = len(CANVAS_PAR_DEFAUT.read_text(encoding="utf-8"))
    print(f"bench — {len(requetes)} demandes × {tours} tours :")
    print(f"  build : {build_s:.2f} s")
    print(f"  route : {1000 * sum(durees) / len(durees):.1f} ms en moyenne "
          f"(min {1000 * min(durees):.1f} · max {1000 * max(durees):.1f})")
    print(f"  gain  : ~{taille // 4 // 40}× en tokens vs lecture du canvas "
          f"complet ({taille:,} caractères)")
    return 0


def _langs_map(sk_dir: Path) -> dict[int, list[str]]:
    """num -> langues disponibles (fr + sidecars .<lang>.md), fr en premier."""
    out: dict[int, list[str]] = {}
    for f in sorted(Path(sk_dir).glob("*.md")):
        m = re.match(r"^(\d+)-(.+)\.([a-z]{2})\.md$", f.name)
        if m and m.group(3) != "fr":
            out.setdefault(int(m.group(1)), []).append(m.group(3))
            continue
        m2 = re.match(r"^(\d+)-.+\.md$", f.name)
        if m2:
            ls = out.setdefault(int(m2.group(1)), [])
            if "fr" not in ls:
                ls.append("fr")
    for ls in out.values():
        ls[:] = sorted(set(ls), key=lambda l: (l != "fr", l))
    return out


def cmd_lint() -> int:
    problemes = []
    vus = {}
    for syn, num in SYNONYMES:
        if syn in vus:
            detail = "en double" if vus[syn] == num else \
                f"cibles contradictoires : {vus[syn]} et {num}"
            problemes.append(f"synonyme « {syn} » {detail}")
        vus[syn] = num
        if len(syn) < 2:
            problemes.append(f"synonyme « {syn} » trop court (1 lettre ou vide)")
    tests_vus = set()
    for demande, attendu in TESTS_ROUTAGE:
        if demande in tests_vus:
            problemes.append(f"test « {demande} » dupliqué")
        tests_vus.add(demande)
    # R12 : date_ajout (YYYY-MM) présente et valide sur toutes les skills/*.md
    # (repo : <racine>/skills, pack : skills/ à côté de routage.py)
    here = Path(__file__).resolve().parent
    sk_dirs = [d for d in (here / "skills", here.parent / "skills") if d.is_dir()]
    for sk_dir in sk_dirs:
        n_da = 0
        n_re = 0
        n_lg = 0
        fr_nums = set()
        for f in sk_dir.glob("*.md"):
            if re.match(r"^\d+-.*\.[a-z]{2}\.md$", f.name):
                continue  # sidecar multilingue, contrôlé à part
            txt = f.read_text(encoding="utf-8")
            fm = txt.split("---")[1]
            mn = re.search(r"^num: (\d+)$", fm, re.M)
            if mn:
                fr_nums.add(int(mn.group(1)))
            m = re.search(r'^date_ajout: "(\d{4})-(\d{2})"$', fm, re.M)
            if not (m and 1 <= int(m.group(2)) <= 12):
                problemes.append(f"{f.name} : date_ajout absente ou invalide (YYYY-MM)")
            else:
                n_da += 1
            # R15 : resume présent dans le frontmatter (1-400 car. ; R14 couvre < >)
            mr = re.search(r'^resume: "(.+)"$', fm, re.M)
            if not mr or len(mr.group(1)) > 400:
                problemes.append(f"{f.name} : resume absent ou invalide (1-400 car.)")
            else:
                n_re += 1
            # R16 : lang présent et = fr sur les fichiers racine
            ml = re.search(r'^lang: "([a-z]{2})"$', fm, re.M)
            if not ml or ml.group(1) != "fr":
                problemes.append(f"{f.name} : lang absent ou != fr (R16)")
            else:
                n_lg += 1
            # R13 : aucune année (20xx) dans le titre (nom / nom_court)
            for k in ("nom", "nom_court"):
                mv = re.search(rf'^{k}: "(.*)"$', fm, re.M)
                if mv and re.search(r"\b20\d{2}\b", mv.group(1)):
                    problemes.append(f"{f.name} : année 20xx dans le titre ({k} = « {mv.group(1)} »)")
            # R14 : pas de < ni > dans tout le frontmatter (injection system prompt)
            if re.search(r"[<>]", fm):
                problemes.append(f"{f.name} : frontmatter contient < ou >")
        print(f"  date_ajout : {n_da} skills conformes (YYYY-MM) dans {sk_dir}")
        print(f"  resume : {n_re} skills conformes (R15, 1-400 car.) dans {sk_dir}")
        print(f"  lang : {n_lg} fichiers fr conformes (R16) dans {sk_dir}")
        # sidecars multilingues NNN-slug.<lang>.md : lang cohérent, num FR existant, mêmes contrôles
        n_sc = 0
        par_lang: dict[str, int] = {}
        for f in sk_dir.glob("*.md"):
            m = re.match(r"^(\d+)-(.+)\.([a-z]{2})\.md$", f.name)
            if not m:
                continue
            lang = m.group(3)
            txt = f.read_text(encoding="utf-8")
            fm = txt.split("---")[1]
            ml = re.search(r'^lang: "(.*)"$', fm, re.M)
            if not ml or ml.group(1) != lang:
                problemes.append(f"{f.name} : lang frontmatter != suffixe .{lang}.md")
            if int(m.group(1)) not in fr_nums:
                problemes.append(f"{f.name} : num {m.group(1)} sans fichier FR correspondant")
            mda = re.search(r'^date_ajout: "(\d{4})-(\d{2})"$', fm, re.M)
            if not (mda and 1 <= int(mda.group(2)) <= 12):
                problemes.append(f"{f.name} : date_ajout absente ou invalide")
            mr = re.search(r'^resume: "(.+)"$', fm, re.M)
            if not mr or len(mr.group(1)) > 400:
                problemes.append(f"{f.name} : resume absent ou invalide (1-400 car.)")
            if re.search(r"[<>]", fm):
                problemes.append(f"{f.name} : frontmatter contient < ou >")
            n_sc += 1
            par_lang[lang] = par_lang.get(lang, 0) + 1
        print(f"  sidecars multilingues : {n_sc} dans {sk_dir} ({', '.join(f'{l}: {n}' for l, n in sorted(par_lang.items())) or 'aucun'})")
    # skills perso (mesSkillsPerso/) : date_ajout + pas de < > + au moins un mot_cle
    for pd in dossiers_perso():
        n_p = 0
        for f in pd.glob("*.md"):
            if f.name.lower().startswith("readme"):
                continue
            txt = f.read_text(encoding="utf-8")
            fm = txt.split("---")[1] if txt.startswith("---") else ""
            m = re.search(r'^date_ajout: "(\d{4})-(\d{2})"$', fm, re.M)
            if not (m and 1 <= int(m.group(2)) <= 12):
                problemes.append(f"perso {f.name} : date_ajout absente ou invalide (YYYY-MM)")
            if fm and re.search(r"[<>]", fm):
                problemes.append(f"perso {f.name} : frontmatter contient < ou >")
            if not re.search(r'^mot_cle: ".+"$', fm, re.M):
                problemes.append(f"perso {f.name} : mot_cle vide")
            mr = re.search(r'^resume: "(.+)"$', fm, re.M)
            if not mr or len(mr.group(1)) > 400:
                problemes.append(f"perso {f.name} : resume absent ou invalide (1-400 car.)")
            n_p += 1
        print(f"  perso : {n_p} skill(s) dans {pd} (date_ajout + frontmatter contrôlés)")
    if DB_PATH.exists():
        db = sqlite3.connect(DB_PATH)
        nums = {r[0] for r in db.execute("SELECT num FROM skills")}
        db.close()
        for syn, num in SYNONYMES:
            if num not in nums:
                problemes.append(f"synonyme « {syn} » → skill inexistante {num}")
        for demande, attendu in TESTS_ROUTAGE:
            if attendu is not None and attendu not in nums:
                problemes.append(f"test « {demande} » → skill inexistante "
                                 f"{attendu}")
    if problemes:
        print(f"✖ Lint : {len(problemes)} problème(s)")
        for p in problemes:
            print("  -", p)
        return 1
    print(f"✅ Lint : {len(SYNONYMES)} synonymes · {len(TESTS_ROUTAGE)} tests — "
          "aucun problème")
    return 0


# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Export JSON du catalogue complet (sections parsées + métadonnées de routage)
# ---------------------------------------------------------------------------
RE_SECTION_EXPORT = re.compile(r"^## (\d+)\. (\S+) (.+)$", re.M)


def _blocs_canoniques(corps: str) -> dict:
    """Extrait les blocs « **Libellé** : contenu » d'une section de skill."""
    blocs: dict[str, str] = {}
    matches = list(re.finditer(r"\*\*([^*]+)\*\* :?", corps))
    for i, m in enumerate(matches):
        fin = matches[i + 1].start() if i + 1 < len(matches) else len(corps)
        contenu = re.split(r"\n---", corps[m.end():fin])[0].strip()
        blocs[m.group(1).strip()] = contenu
    return blocs


def _sections_multi(canvas: Path) -> dict[int, tuple[str, str, str, str]]:
    """Réunit les sections « ## N. » du canvas principal et des canvases corpus."""
    sections: dict[int, tuple[str, str, str, str]] = {}
    chemins = [(Path(canvas), "principal")] + [(p, p.parent.name) for p in CANVAS_CORPUS]
    for chemin, label in chemins:
        if not chemin.exists():
            continue
        texte_f = chemin.read_text(encoding="utf-8")
        limites = list(RE_SECTION_EXPORT.finditer(texte_f))
        for i, m in enumerate(limites):
            fin = limites[i + 1].start() if i + 1 < len(limites) else len(texte_f)
            sections[int(m.group(1))] = (m.group(2), m.group(3).strip(),
                                         texte_f[m.end():fin], label)
    return sections


def _entree_condensee(num, nom, nom_court, emoji, domaine, branche, mot_cle, resume,
                      synonymes, cross_refs, corps, langs=None) -> dict:
    """Entrée condensée machine d'une skill : métadonnées + resume + étapes de la
    Méthode + garde-fous GF (sans le corps complet)."""
    blocs = _blocs_canoniques(corps)
    methode = [re.sub(r"\s+", " ", m).strip()[:240]
               for m in re.findall(r"(?m)^\d+\. (.+)$", blocs.get("Méthode") or "")]
    gf = [re.sub(r"\s+", " ", l).strip()[2:].strip()
          for l in (blocs.get("Garde-fous") or "").splitlines()
          if re.match(r"^- GF-", l.strip())]
    return {"num": num, "nom": nom, "nom_court": nom_court, "emoji": emoji,
            "domaine": domaine, "branche": branche, "mot_cle": mot_cle,
            "resume": resume, "methode": methode, "garde_fous": gf,
            "synonymes": sorted(synonymes), "cross_refs": sorted(set(cross_refs)),
            "langs": langs or ["fr"]}


def _json_condense(entrees: list[dict]) -> str:
    export = {"catalogue": "skillAISlop", "version": CATALOGUE_VERSION,
              "mode": "condensé",
              "stats": {"sections": len(entrees),
                        "domaines": len({e["domaine"] for e in entrees}),
                        "synonymes": sum(len(e["synonymes"]) for e in entrees),
                        "tests_routage": len(TESTS_ROUTAGE)},
              "skills": sorted(entrees, key=lambda e: e["num"])}
    return json.dumps(export, ensure_ascii=False, indent=2) + "\n"


def _condensed_json_repo(canvas: Path) -> str:
    """Index condensé depuis le canvas (dépôt) : extraire + sections corpus + resumes."""
    texte = Path(canvas).read_text(encoding="utf-8")
    sommaire, _sig, mot_cles, branches, noms_courts, cartes = extraire(texte)
    sections = _sections_multi(canvas)
    synonymes: dict[int, list[str]] = {}
    for syn, num in SYNONYMES:
        synonymes.setdefault(num, []).append(syn)
    sk = _skills_dir()
    resumes = lire_resumes(sk)
    langs = _langs_map(sk)
    fm_refs: dict[int, list[int]] = {}
    for f in sorted(sk.glob("*.md")):
        txt = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
        if not m:
            continue
        fm = m.group(1)
        num = int(re.search(r"^num: (\d+)$", fm, re.M).group(1))
        mc = re.search(r'^cross_refs: \[(.*)\]$', fm, re.M)
        if mc:
            fm_refs[num] = [int(r) for r in re.findall(r"\d+", mc.group(1))]
    entrees = []
    for num in sorted(sections):
        emoji, nom, corps, _f = sections[num]
        dom = sommaire.get(num, ["", ""])[1]
        cas = _blocs_canoniques(corps).get("Cas d'usage", "")
        refs = {int(r) for r in re.findall(r"(\d+) \(", cas)} | {int(r) for r in re.findall(r"skills? (\d+)", cas)}
        refs |= set(fm_refs.get(num, []))
        entrees.append(_entree_condensee(num, nom, noms_courts.get(num), emoji, dom,
                                         branches.get(num), mot_cles.get(num),
                                         resumes.get(num), synonymes.get(num, []), refs, corps,
                                         langs.get(num, ["fr"])))
    return _json_condense(entrees)


def _condensed_json_from_skills(sk_dir: Path) -> str:
    """Index condensé depuis skills/*.md (pack autonome, sans canvas)."""
    entrees = []
    for f in sorted(Path(sk_dir).glob("*.md")):
        txt = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
        if not m:
            continue
        fm = m.group(1)
        def _g(k):
            mm = re.search(rf'^{k}: "(.*)"$', fm, re.M)
            return mm.group(1) if mm else ""
        num = int(re.search(r"^num: (\d+)$", fm, re.M).group(1))
        ms = re.search(r'^synonymes: \[(.*)\]$', fm, re.M)
        syns = [x.strip().strip('"') for x in ms.group(1).split(",") if x.strip()] if ms else []
        mc = re.search(r'^cross_refs: \[(.*)\]$', fm, re.M)
        refs = [int(r) for r in re.findall(r"\d+", mc.group(1))] if mc else []
        mr = re.search(r'^resume: "(.*)"$', fm, re.M)
        resume = mr.group(1) if (mr and mr.group(1).strip()) else resume_auto(txt[m.end():])
        entrees.append(_entree_condensee(num, _g("nom"), _g("nom_court"), _g("emoji"),
                                         _g("domaine"), _g("branche"), _g("mot_cle"),
                                         resume, syns, refs, txt[m.end():],
                                         _langs_map(sk_dir).get(num, ["fr"])))
    return _json_condense(entrees)


def cmd_export(canvas: Path, fichier: Path | None = None, complet: bool = False,
               condense: bool = False) -> int:
    """Exporte toutes les sections du catalogue en JSON (compact par défaut, --complet
    pour le texte intégral, --condensé pour l'index machine léger)."""
    if condense:
        sortie = _condensed_json_repo(canvas)
        if fichier is None:
            fichier = RACINE / "data" / "catalogue-condensed.json"
        Path(fichier).write_text(sortie, encoding="utf-8")
        n = sortie.count('"num":')
        print(f"✅ {n} sections exportées (mode condensé) vers {fichier}")
        return 0
    texte = Path(canvas).read_text(encoding="utf-8")
    sommaire, signaux, mot_cles, branches, noms_courts, cartes = extraire(texte)

    sections = _sections_multi(canvas)
    assert sections, "aucune section « ## N. » trouvée"

    synonymes: dict[int, list[str]] = {}
    for syn, num in SYNONYMES:
        synonymes.setdefault(num, []).append(syn)

    resumes: dict[int, str] = {}
    langs: dict[int, list[str]] = {}
    for cand in (Path(canvas).resolve().parent.parent / "skills",
                 Path(canvas).resolve().parent / "skills"):
        if cand.is_dir():
            resumes = lire_resumes(cand)
            langs = _langs_map(cand)
            break

    skills = []
    for num in sorted(sections):
        emoji, nom, corps, fichier_section = sections[num]
        blocs = _blocs_canoniques(corps)
        cas = blocs.get("Cas d'usage", "")
        refs = sorted(
            {int(r) for r in re.findall(r"(\d+) \(", cas)}
            | {int(r) for r in re.findall(r"skill (\d+)", cas)}
        )
        dom = sommaire.get(num, ["", ""])
        entree: dict = {
            "num": num,
            "emoji": emoji,
            "nom": nom,
            "domaine": dom[1],
            "signal_routage": signaux.get(num),
            "mot_cle_index": mot_cles.get(num),
            "nom_court": noms_courts.get(num),
            "branche_arbre": branches.get(num),
            "cross_refs": refs,
            "synonymes": sorted(synonymes.get(num, [])),
            "resume": resumes.get(num),
            "langs": langs.get(num, ["fr"]),
            "fichier": fichier_section,
        }
        if complet:
            idx = re.search(r"> 🔎 \*\*Index\*\* : (.+)", corps)
            methode = re.findall(r"^\d+\. .+$", blocs.get("Méthode", ""), re.M)
            entree.update({
                "nom_sommaire": dom[0],
                "index_section": idx.group(1).strip() if idx else None,
                "objectif": blocs.get("Objectif"),
                "instructions_systeme": blocs.get("Instructions système"),
                "methode": methode,
                "exemple_prompt": blocs.get("Exemple de prompt"),
                "cas_usage": cas or None,
            })
        skills.append(entree)

    export = {
        "catalogue": "skillAISlop",
        "genere_le": time.strftime("%Y-%m-%d"),
        "mode": "complet" if complet else "compact",
        "stats": {
            "sections": len(skills),
            "domaines": len(cartes),
            "synonymes": len(SYNONYMES),
            "tests_routage": len(TESTS_ROUTAGE),
        },
        "domaines": [{"domaine": d, "mots_cles": k} for d, k in cartes],
        "skills": skills,
    }
    sortie = json.dumps(export, ensure_ascii=False, indent=2)
    if fichier:
        Path(fichier).write_text(sortie + "\n", encoding="utf-8")
        print(f"✅ {len(skills)} sections exportées (mode {'complet' if complet else 'compact'}) vers {fichier}")
    else:
        print(sortie)
    return 0


def _todo_done_paths():
    return RACINE / "TODO.md", RACINE / "DONE.md"


def cmd_todo(texte: str) -> int:
    """Ajoute une tâche en fin de TODO.md (R10)."""
    todo, _ = _todo_done_paths()
    t = todo.read_text(encoding="utf-8").rstrip("\n")
    t += f"\n\n- [ ] {texte}\n"
    todo.write_text(t, encoding="utf-8")
    print(f"✅ TODO ajouté : {texte}")
    return 0


def cmd_done(texte: str) -> int:
    """R10 automatique : retire la tâche de TODO.md (si elle y est) et l'ajoute
    en tête de DONE.md avec sa date."""
    import datetime
    todo, done = _todo_done_paths()
    date = datetime.date.today().isoformat()
    # retirer de TODO (ligne contenant le texte, insensible à la casse)
    lines = todo.read_text(encoding="utf-8").splitlines()
    reste = [l for l in lines if texte.lower() not in l.lower()]
    if len(reste) != len(lines):
        todo.write_text("\n".join(reste).rstrip("\n") + "\n", encoding="utf-8")
    # ajouter en tête de DONE (après le bloc frontmatter + index)
    d = done.read_text(encoding="utf-8")
    ancre = "(les plus récentes en premier)\n\n"
    assert ancre in d
    ligne = f"- [x] **{date}** — {texte}\n\n"
    d = d.replace(ancre, ancre + ligne, 1)
    done.write_text(d, encoding="utf-8")
    print(f"✅ DONE ajouté ({date}) : {texte}")
    return 0


def _hash_skills() -> str:
    import hashlib
    h = hashlib.sha256()
    for f in sorted((RACINE / "skills").glob("*.md")):
        h.update(f.name.encode())
        h.update(f.read_bytes())
    return h.hexdigest()


README_PACK = """# Pack skillAISlop — catalogue de skills pour agent IA

## Installation
```bash
pip install sqlite-vec   # extension vectorielle SQLite (repli gracieux sinon)
python3 routage.py build --from-skills   # construit skills.db depuis skills/*.md
python3 routage.py route "ma demande"   # route vers la bonne skill (exit 0/1/2)
```

## Brancher sur ton agent (SKILL.md / AGENTS.md du projet hôte)
Ajoute cette section dans le SKILL.md (ou AGENTS.md / .cursorrules) de ton projet :
```markdown
## skillAISlop — routeur de skills
Avant de choisir une skill toi-même, lance le routeur :
`python3 <chemin-vers-ce-pack>/routage.py route "<demande de l'utilisateur>"`
- exit 0 → skill trouvée : lire `skills/NNN-*.md` et appliquer sa méthode
- exit 1 → piste affichée, à confirmer
- exit 2 → aucune skill : répondre en direct (`misses --suggest` si récurrent)
```
Alternative standard Agent Skills (sans routeur) : `python3 routage.py skillmd --sortie agent-skills` puis `npx skills add ./agent-skills`.

## Mes skills perso (`mesSkillsPerso/`)
Dépose tes propres fichiers `.md` dans `mesSkillsPerso/` (à côté de `routage.py`) :
- ils **restent dans ce dossier** et ne sont **jamais écrasés ni supprimés** par une mise à jour du pack (le pack n'embarque que `mesSkillsPerso/README.md`)
- au prochain `build` (ou `perso --add` + build), ils sont **convertis automatiquement au format du template** (frontmatter YAML avec `date_ajout: "YYYY-MM"` + les 12 sections TEMPLATE-v2) et ingérés dans leur **propre table** `skills_perso` de `skills.db`
- au routage, ils sont **prioritaires** sur le catalogue : s'ils cadrent avec la demande, la réponse affiche `⭐ Perso Pn · mesSkillsPerso/<fichier>` (exit 0)
- commandes : `perso` (liste) · `perso --add ma-skill.md` · `perso --convert` · `route "perso 2"` (renvoi direct)
- les skills perso ne sont jamais exportées dans le pack (elles restent locales au projet)

## Contenu
- `skills/` — {nb} skills + routeur 0, soit {nbf} fichiers `NNN-slug.md` (frontmatter YAML complet : num, date_ajout YYYY-MM, nom, domaine, signal, mot_cle, synonymes, cross_refs)
- `mesSkillsPerso/` — dossier de tes skills perso (README + tes fichiers, jamais touché par les mises à jour)
- `routage.py` — routeur autonome (build, route, test, lint, perso, export, sonde, vocab, versions, analytics)
- `manifeste.json` — version sémantique (meta), nombre de skills, domaines, hash sha256 des fichiers skills

## Commandes utiles
- `route "<demande>"` → skill 0/1/2 (0 = trouvée, 1 = piste, 2 = rien)
- `route "<demande>" --json` → candidats avec voie et score (clé `perso` pour les skills perso)
- `perso` · `perso --add <fichier.md>` · `perso --convert`
- `test` · `lint` · `sonde` · `vocab` · `versions` · `misses` · `analytics`
"""


def cmd_pack(sortie: Path, check: bool) -> int:
    import json, zipfile, hashlib, tempfile, shutil
    nb = len(list((RACINE / "skills").glob("*.md")))
    h = _hash_skills()
    version = CATALOGUE_VERSION
    manifeste = {
        "name": "skillaislop",
        "version": version,
        "skills": nb - 1,  # -1 : skill 0 = routeur, non comptée
        "sections": nb,
        "domaines": len({_m.group(1) for _f in (RACINE / "skills").glob("*.md") if (_m := re.search(r'^domaine: "(.*)"$', _f.read_text(encoding="utf-8")[:600], re.M))}),
        "skills_hash_sha256": h,
        "build_from": "skills/*.md (frontmatter) — build --from-skills",
        "license": "voir dépôt source",
    }
    if check:
        # test de fidélité : extraire le pack, rebuild, comparer les tables clés
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            with zipfile.ZipFile(sortie) as z:
                z.extractall(td)
                cond_zip = z.read("catalogue-condensed.json").decode("utf-8")
            import sqlite3 as _sq
            sys_path_backup = list(sys.path)
            sys.path.insert(0, str(td))
            try:
                spec = importlib.util.spec_from_file_location("rt_pack", td / "routage.py")
                rt = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(rt)
                rt.cmd_build(td / "routage.py", db_path=td / "skills.db", from_skills=True)
                db = _sq.connect(td / "skills.db")
                try:
                    import sqlite_vec as _sv
                    db.enable_load_extension(True)
                    _sv.load(db)
                except Exception:
                    pass
                base = ["skills", "synonymes", "domaines", "skills_fts", "trigrammes", "lang"]
                for f in (td / "skills").glob("*.md"):
                    m = re.match(r"^\d+-.*\.([a-z]{2})\.md$", f.name)
                    if m and m.group(1) != "fr":
                        l = re.sub(r"[^a-z0-9]", "", m.group(1))
                        base += [f"skills_{l}", f"skills_fts_{l}", f"skills_vec_{l}"]
                def _counts(conn):
                    return {t: conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
                            for t in base
                            if conn.execute("SELECT 1 FROM sqlite_master WHERE name=?", (t,)).fetchone()}
                got = _counts(db)
                gh = hashlib.sha256()
                for f in sorted((td / "skills").glob("*.md")):
                    gh.update(f.name.encode()); gh.update(f.read_bytes())
                hash_ok = gh.hexdigest() == h
                cond_ok = cond_zip == rt._condensed_json_from_skills(td / "skills")
            finally:
                sys.path[:] = sys_path_backup
            ref = sqlite3.connect(Path(__file__).resolve().with_name("skills.db"))  # DB du dépôt courant
            try:
                import sqlite_vec as _sv
                ref.enable_load_extension(True)
                _sv.load(ref)
            except Exception:
                pass
            attendu = {t: ref.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
                       for t in got if ref.execute("SELECT 1 FROM sqlite_master WHERE name=?", (t,)).fetchone()}
            ref.close()
            # trigrammes : tolérance 1 % (source canvas vs fichiers peut différer marginalement)
            tri_ok = abs(got["trigrammes"] - attendu["trigrammes"]) <= max(1, attendu["trigrammes"] // 100)
            autres = {k: v for k, v in attendu.items() if k != "trigrammes"}
            ok = all(got[k] == v for k, v in autres.items()) and tri_ok and hash_ok and cond_ok
            print("pack check:", "✅ FIDÈLE" if ok else f"❌ écart {got} vs {attendu}, hash_ok={hash_ok}, cond_ok={cond_ok}")
            return 0 if ok else 1
    sortie.parent.mkdir(parents=True, exist_ok=True)
    # deflate reste le meilleur sur du markdown (testé : LZMA 2,2 Mo vs deflate 1,93 Mo) ;
    # aucun impact runtime — la décompression ne se fait qu'à l'extraction du pack
    with zipfile.ZipFile(sortie, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in sorted((RACINE / "skills").glob("*.md")):
            # (skills.db est régénéré par build --from-skills : exclu du pack)
            z.write(f, f"skills/{f.name}")
        z.write(RACINE / "outils" / "routage.py", "routage.py")
        z.writestr("catalogue-condensed.json", _condensed_json_from_skills(RACINE / "skills"))
        # mesSkillsPerso/ : JAMAIS les fichiers perso de l'utilisateur (ils restent
        # locaux, jamais écrasés à l'upgrade) — uniquement le README explicatif
        pr = RACINE / "mesSkillsPerso" / "README.md"
        if pr.exists():
            z.write(pr, "mesSkillsPerso/README.md")
        else:
            z.writestr("mesSkillsPerso/README.md", PERSO_README)
        z.writestr("manifeste.json", json.dumps(manifeste, ensure_ascii=False, indent=2))
        z.writestr("README.md", README_PACK.format(nb=nb - 1, nbf=nb))
    print(f"✅ pack exporté : {sortie} ({sortie.stat().st_size/1e6:.2f} Mo, {nb - 1} skills + 1 routeur, hash {h[:12]}…)")
    print(f"   test de fidélité : python3 outils/routage.py pack --check")
    return 0


def cmd_skillmd(sortie: Path, lang: str | None = None) -> int:
    """Génère un dossier de SKILL.md (standard ouvert Agent Skills : frontmatter
    name/description + corps) depuis skills/*.md — installable via `npx skills add`."""
    import re as _re, unicodedata
    def norm(s):
        s = unicodedata.normalize("NFKD", s)
        return "".join(c for c in s if not unicodedata.combining(c)).lower()
    sortie.mkdir(parents=True, exist_ok=True)
    n = 0
    sk = _skills_dir()
    if lang:
        files = sorted(sk.glob(f"*.{lang}.md"))
    else:
        files = [f for f in sorted(sk.glob("*.md"))
                 if not re.match(r"^\d+-.*\.[a-z]{2}\.md$", f.name)]
    for f in files:
        txt = f.read_text(encoding="utf-8")
        fm = _re.match(r"---\n(.*?)\n---\n(.*)", txt, _re.S)
        meta, corps = fm.group(1), fm.group(2)
        g = lambda k: _re.search(rf'^{k}: "(.*)"$', meta, _re.M).group(1)
        num = int(_re.search(r"^num: (\d+)$", meta, _re.M).group(1))
        nom, signal, dom, mc = g("nom"), g("signal"), g("domaine"), g("mot_cle")
        syns = _re.search(r'^synonymes: \[(.*)\]$', meta, _re.M).group(1)
        desc = f"{signal or nom} [{dom}]"[:200]
        # nom de dossier conforme au standard : kebab-case, prefix numérique gardé
        slug = _re.sub(r"[^a-z0-9]+", "-", norm(nom)).strip("-")[:40]
        d = sortie / f"{num:03d}-{slug}"
        d.mkdir(exist_ok=True)
        skill_md = f"""---
name: "{num:03d}-{slug}"
description: "{desc}"
metadata:
  skillAISlop_num: {num}
  domaine: "{dom}"
  mot_cle: "{mc}"
  synonymes: [{syns}]
---

{corps.strip()}
"""
        (d / "SKILL.md").write_text(skill_md, encoding="utf-8")
        n += 1
    # manifeste global pour npx skills add
    import json
    (sortie / "skills.json").write_text(json.dumps({
        "name": "skillaislop", "version": "12.0.0", "skills": n,
        "source": "github:Tomcodehere/skillAISlop",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ {n} SKILL.md générés dans {sortie} (+ skills.json pour npx skills add)")
    return 0


def cmd_serve(host: str, port: int) -> int:
    """Mini API HTTP de routage, bind loopback UNIQUEMENT (127.0.0.1 par défaut)."""
    if host not in ("127.0.0.1", "localhost", "::1"):
        print(f"⛔ refus : bind {host} interdit — loopback uniquement (127.0.0.1)")
        return 1
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA cache_size=-8000")
    charger_vec(db)

    class H(BaseHTTPRequestHandler):
        def _json(self, obj, code=200):
            import json
            body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        def do_GET(self):
            u = urlparse(self.path)
            if u.path == "/health":
                n = db.execute("SELECT COUNT(*) FROM skills").fetchone()[0]
                return self._json({"ok": True, "skills": n})
            if u.path == "/route":
                q = parse_qs(u.query).get("q", [""])[0]
                top = int(parse_qs(u.query).get("top", ["3"])[0])
                res = chercher(db, q, top)
                cands = [dict(r) for r in res["exact"] + res["fts"] + res["vec"] + res["flou"]]
                code = 0 if cands else (1 if (res["pistes"] or res["domaines"]) else 2)
                return self._json({"query": q, "exit": code, "candidates": cands,
                                   "pistes": [dict(x) for x in res["pistes"]],
                                   "domaines": [dict(x) for x in res["domaines"]]})
            if u.path in ("/skills", "/export.json"):
                rows = db.execute("SELECT num, nom, domaine, signal, mot_cle, nom_court FROM skills ORDER BY num").fetchall()
                return self._json({"skills": [dict(r) for r in rows]})
            return self._json({"error": "not found", "endpoints": ["/health", "/route?q=", "/skills", "/export.json"]}, 404)
        def log_message(self, *a):
            pass

    srv = HTTPServer((host, port), H)
    print(f"🟢 API locale sur http://{host}:{port} (loopback uniquement — Ctrl+C pour arrêter)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\narrêt.")
    return 0


def cmd_evals(num: int | None = None) -> int:
    """Eval par skill : exécute TESTS_ROUTAGE et rapporte couverture + score par skill.
    Score /100 = % de tests de la skill passés (ou 100 si aucun test)."""
    import sqlite3 as _sq
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = _sq.connect(DB_PATH); db.row_factory = _sq.Row
    db.execute("PRAGMA cache_size=-8000")
    charger_vec(db)
    par_skill = {}
    ok_total = 0
    for demande, attendu in TESTS_ROUTAGE:
        if num is not None and attendu != num: continue
        res = chercher(db, demande, 5)
        candidats = [res["direct"]] if res["direct"] else res["exact"] + res["fts"] + res["vec"] + res["flou"] + res["fusion"]
        ok = attendu in [c["num"] for c in candidats if c]
        if attendu is None: continue
        par_skill.setdefault(attendu, [0, 0])
        par_skill[attendu][1] += 1
        if ok: par_skill[attendu][0] += 1; ok_total += 1
    lignes = []
    for n in sorted(par_skill):
        ok, tot = par_skill[n]
        score = round(ok / tot * 100) if tot else 100
        nom = db.execute("SELECT nom FROM skills WHERE num=?", (n,)).fetchone()
        lignes.append((score, n, nom["nom"] if nom else "?", ok, tot))
    lignes.sort()
    total_tests = sum(t for _, _, _, _, t in lignes)
    print(f"evals : {ok_total}/{total_tests} tests OK · {len(lignes)} skills couvertes · moyenne {sum(s for s,*_ in lignes)/len(lignes):.1f}/100")
    if num is not None:
        for s, n, nom, ok, tot in lignes:
            if n == num: print(f"  skill {n} « {nom} » : {ok}/{tot} = {s}/100")
        return 0
    for s, n, nom, ok, tot in lignes[:15]:
        print(f"  {s:3d}/100  #{n} {nom[:45]}  ({ok}/{tot})")
    return 0


def cmd_top(n: int) -> int:
    """Affiche le top-N des skills les plus routées (table popularite)."""
    import sqlite3 as _sq
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = _sq.connect(DB_PATH); db.row_factory = _sq.Row
    try:
        rows = db.execute(
            "SELECT p.num, p.score, s.nom, s.domaine FROM popularite p "
            "JOIN skills s ON s.num = p.num ORDER BY p.score DESC LIMIT ?", (n,)).fetchall()
    except _sq.OperationalError:
        print("table popularite absente — aucune session enregistrée"); return 1
    for r in rows:
        print(f"{r['score']:6.1f}  #{r['num']}  {r['nom']}  [{r['domaine']}]")
    return 0


def cmd_vocab(limit: int = 30) -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    charger_vec(db)
    try:
        rows = db.execute(
            "SELECT term, doc, cnt FROM skills_fts_vocab ORDER BY cnt DESC, doc DESC LIMIT ?",
            (limit,)).fetchall()
    except sqlite3.OperationalError:
        print("fts5vocab indisponible")
        return 1
    print(f"Top {len(rows)} tokens du FTS (term · docs · occurrences) :")
    for term, doc, cnt in rows:
        print(f"  {term:<20} {doc:>4} docs  {cnt:>5} occ")
    db.close()
    return 0


def cmd_versions() -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    try:
        rows = db.execute(
            "SELECT id, date, nb_skills, ajouts, supprimes, modifies "
            "FROM versions ORDER BY id").fetchall()
    except sqlite3.OperationalError:
        print("table versions absente — rebuild nécessaire")
        return 1
    ver = db.execute("SELECT v FROM meta WHERE k='version'").fetchone()
    print(f"Version courante du catalogue : {ver[0] if ver else CATALOGUE_VERSION}")
    for vid, date, nb, aj, su, mo in rows:
        print(f"#{vid} {date} — {nb} skills · +{aj} -{su} ~{mo}")
    db.close()
    return 0


def cmd_analytics() -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    try:
        print("Par code de sortie :")
        for r in db.execute("SELECT code, COUNT(*) n FROM routes GROUP BY code ORDER BY code"):
            print(f"  exit {r['code']} : {r['n']}")
        print("Par voie (top) :")
        for r in db.execute("SELECT voie, COUNT(*) n FROM routes GROUP BY voie ORDER BY n DESC LIMIT 8"):
            print(f"  {r['voie']:<12} {r['n']}")
        print("Exit 2 par domaine :")
        for r in db.execute(
                "SELECT s.domaine, COUNT(*) n FROM routes r "
                "LEFT JOIN skills s ON s.num = r.num "
                "WHERE r.code = 2 GROUP BY s.domaine ORDER BY n DESC LIMIT 8"):
            print(f"  {r['domaine'] or '(sans skill)':<20} {r['n']}")
    except sqlite3.OperationalError:
        print("table routes absente — aucune session enregistrée")
    db.close()
    return 0


def cmd_count(canvas: Path, dossier: Path) -> int:
    """Compte les skills du catalogue et écrit totalSkillsCount.md."""
    texte = Path(canvas).read_text(encoding="utf-8")
    sommaire, signaux, mot_cles, branches, noms_courts, cartes = extraire(texte)

    domaines: dict[str, int] = {}
    for num, (_, dom) in sommaire.items():
        if num == 0:
            continue  # -1 : skill 0 = routeur, jamais comptée comme skill
        domaines[dom] = domaines.get(dom, 0) + 1
    total = len(sommaire)
    operationnelles = total - 1  # hors skill 0 (routeur)

    lignes = [
        "# Compteur de skills — skillAISlop",
        "",
        "> 🔎 **Index** : Total · Répartition par domaine · Génération",
        "",
        f"**Total : {total} sections (0-{max(sommaire)})** — "
        f"**{operationnelles} skills opérationnelles** + 1 routeur (skill 0).",
        "",
        "## Répartition par domaine",
        "",
        "| Domaine | Skills |",
        "|---|---|",
    ]
    for dom, n in sorted(domaines.items(), key=lambda x: (-x[1], x[0])):
        lignes.append(f"| {dom} | {n} |")
    lm = _langs_map(_skills_dir())
    trad = {}
    for ls in lm.values():
        for l in ls:
            if l != "fr":
                trad[l] = trad.get(l, 0) + 1
    if trad:
        lignes += [
            "",
            "## Traductions",
            "",
            "Sidecars `NNN-slug.<lang>.md` : "
            + ", ".join(f"{l} = {n} skills (`.{l}.md`, routage `route --lang {l}`)" for l, n in sorted(trad.items()))
            + ".",
        ]
    lignes += [
        "",
        "## Génération",
        "",
        f"Fichier `totalSkillsCount.md` généré par `routage.py count` "
        "(canvas « Routage SQL Skills ») le "
        f"{time.strftime('%Y-%m-%d')}. À régénérer après chaque évolution "
        "du catalogue (R8), puis recopier dans le canvas "
        "« totalSkillsCount — skillAISlop ».",
    ]

    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    fichier = dossier / "totalSkillsCount.md"
    fichier.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"✅ {total} sections ({operationnelles} skills + 1 routeur) — "
          f"{len(domaines)} domaines -> {fichier}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Routage SQL — skillAISlop")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_build = sub.add_parser("build", help="canvas -> skills.db (ou --from-skills pour lire skills/*.md)")
    p_build.add_argument("canvas", nargs="?", type=Path, default=CANVAS_PAR_DEFAUT)
    p_build.add_argument("--from-skills", action="store_true",
                         help="reconstruit depuis skills/*.md (frontmatter) au lieu du canvas")

    p_route = sub.add_parser("route", help="recherche rapide d'une skill")
    p_route.add_argument("query")
    p_route.add_argument("--tag", help="pré-filtre optionnel par tag (ex. --tag 2027)")

    p_route.add_argument("--top", type=int, default=5)
    p_route.add_argument("--json", action="store_true")
    p_route.add_argument("--lang", default=None, help="langue de la demande (fr/en/nl/... ; défaut : auto-détection par stopwords)")

    p_gen = sub.add_parser("generate", help="base -> sections de routage du canvas")
    p_gen.add_argument("canvas", nargs="?", type=Path, default=CANVAS_PAR_DEFAUT)
    p_gen.add_argument("--check", action="store_true")

    sub.add_parser("test", help="non-régression du routage")

    p_gold = sub.add_parser("golden", help="golden set de régression (P0-3) : rejoue outils/golden_queries.txt vs data/golden-routage.json")
    p_gold.add_argument("--update", action="store_true", help="réécrit le baseline avec les gagnants actuels")

    p_miss = sub.add_parser("misses", help="journal des demandes non routées")
    p_miss.add_argument("--clear", action="store_true")
    p_miss.add_argument("--suggest", action="store_true",
                        help="propose le synonyme à ajouter pour chaque entrée")

    p_stats = sub.add_parser("stats", help="observabilité du routage")
    p_stats.add_argument("--clear", action="store_true")

    p_sonde = sub.add_parser("sonde", help="batterie de sujets -> rapport couvert/partiel/gaps")
    p_sonde.add_argument("--fichier", type=Path, default=None)
    p_sonde.add_argument("--top", type=int, default=3)

    p_vocab = sub.add_parser("vocab", help="top tokens FTS5 (fts5vocab) — lint sémantique")
    p_vocab.add_argument("--limit", type=int, default=30)
    sub.add_parser("versions", help="historique des builds (ajouts/supprimes/modifies)")
    p_todo = sub.add_parser("todo", help="ajoute une tâche à TODO.md (R10)")
    p_todo.add_argument("texte")
    p_done = sub.add_parser("done", help="marque une tâche terminée : la retire de TODO.md et la met en tête de DONE.md (R10)")
    p_done.add_argument("texte")
    sub.add_parser("analytics", help="stats SQL des routages de session (exit, voie, domaine)")
    p_pack = sub.add_parser("pack", help="exporte un zip portable (skills/ + routage.py + manifeste + README) pour un autre projet")
    p_pack.add_argument("--sortie", type=Path, default=RACINE / "data" / "skillaislop-pack.zip")
    p_pack.add_argument("--check", action="store_true", help="vérifie le pack : extrait, rebuild --from-skills, compare les tables")
    p_sm = sub.add_parser("skillmd", help="génère un dossier de SKILL.md (standard Agent Skills) depuis skills/*.md")
    p_sm.add_argument("--sortie", type=Path, default=RACINE / "data" / "agent-skills")
    p_sm.add_argument("--lang", default=None, help="générer depuis les sidecars .<lang>.md (ex. --lang en -> data/agent-skills-en)")
    sub.add_parser("top", help="top-N des skills les plus utilisées (popularité)").add_argument("--n", type=int, default=20)
    p_ev = sub.add_parser("evals", help="exécute les tests de routage et score la couverture par skill (evals)")
    p_ev.add_argument("--num", type=int, help="une seule skill")
    p_srv = sub.add_parser("serve", help="mini API HTTP locale (127.0.0.1 uniquement) : /route?q= /skills /export.json /health")
    p_srv.add_argument("--port", type=int, default=8765)
    p_srv.add_argument("--host", default="127.0.0.1")

    p_bench = sub.add_parser("bench", help="mesure build/route et gain tokens")
    p_bench.add_argument("--tours", type=int, default=3)

    sub.add_parser("lint", help="contrôle qualité de SYNONYMES et TESTS_ROUTAGE")

    p_exp = sub.add_parser("export", help="catalogue -> JSON structuré (compact par défaut)")
    p_exp.add_argument("canvas", nargs="?", type=Path, default=CANVAS_PAR_DEFAUT)
    p_exp.add_argument("--fichier", type=Path, default=None,
                       help="écrire le JSON dans ce fichier (défaut : stdout)")
    p_exp.add_argument("--complet", action="store_true",
                       help="inclure le texte intégral des sections (sinon index compact)")
    p_exp.add_argument("--condensé", dest="condense", action="store_true",
                       help="index condensé machine (resume + méthode + garde-fous) -> data/catalogue-condensed.json")

    p_cnt = sub.add_parser("count", help="compte les skills -> totalSkillsCount.md")
    p_cnt.add_argument("canvas", nargs="?", type=Path, default=CANVAS_PAR_DEFAUT)
    p_cnt.add_argument("--dossier", type=Path, default=RACINE / "data")

    p_perso = sub.add_parser("perso", help="skills perso (mesSkillsPerso/) : liste / --add <fichier.md> / --convert")
    p_perso.add_argument("--add", default=None, help="copie un fichier .md dans mesSkillsPerso/")
    p_perso.add_argument("--convert", action="store_true", help="convertit tous les fichiers du dossier au template")

    args = ap.parse_args()
    if args.cmd == "build":
        cmd_build(args.canvas, from_skills=args.from_skills)
    elif args.cmd == "route":
        raise SystemExit(cmd_route(args.query, args.top, args.json, getattr(args, "tag", None), getattr(args, "lang", None)))
    elif args.cmd == "generate":
        raise SystemExit(cmd_generate(args.canvas, args.check))
    elif args.cmd == "test":
        raise SystemExit(cmd_test())
    elif args.cmd == "golden":
        raise SystemExit(cmd_golden(args.update))
    elif args.cmd == "misses":
        raise SystemExit(cmd_misses(args.clear, args.suggest))
    elif args.cmd == "stats":
        raise SystemExit(cmd_stats(args.clear))
    elif args.cmd == "sonde":
        raise SystemExit(cmd_sonde(args.fichier, args.top))
    elif args.cmd == "vocab":
        raise SystemExit(cmd_vocab(args.limit))
    elif args.cmd == "versions":
        raise SystemExit(cmd_versions())
    elif args.cmd == "todo":
        raise SystemExit(cmd_todo(args.texte))
    elif args.cmd == "done":
        raise SystemExit(cmd_done(args.texte))
    elif args.cmd == "analytics":
        raise SystemExit(cmd_analytics())
    elif args.cmd == "pack":
        raise SystemExit(cmd_pack(args.sortie, args.check))
    elif args.cmd == "skillmd":
        sortie = args.sortie
        if getattr(args, "lang", None) and sortie == RACINE / "data" / "agent-skills":
            sortie = RACINE / "data" / f"agent-skills-{args.lang}"
        raise SystemExit(cmd_skillmd(sortie, getattr(args, "lang", None)))
        raise SystemExit(cmd_skillmd(args.sortie))
    elif args.cmd == "evals":
        raise SystemExit(cmd_evals(getattr(args, "num", None)))
    elif args.cmd == "top":
        raise SystemExit(cmd_top(args.n))
    elif args.cmd == "serve":
        raise SystemExit(cmd_serve(args.host, args.port))
    elif args.cmd == "bench":
        raise SystemExit(cmd_bench(args.tours))
    elif args.cmd == "lint":
        raise SystemExit(cmd_lint())
    elif args.cmd == "export":
        raise SystemExit(cmd_export(args.canvas, args.fichier, args.complet, args.condense))
    elif args.cmd == "count":
        raise SystemExit(cmd_count(args.canvas, args.dossier))
    elif args.cmd == "perso":
        raise SystemExit(cmd_perso(args.add, args.convert))


if __name__ == "__main__":
    main()
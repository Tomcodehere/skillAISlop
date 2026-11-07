
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
    ("onboarder notre nouveau développeur lundi", 698),
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
    ("génère des packshots blancs pour mes 20 produits", 730),
    ("rédige tous les textes de notre page d'inscription", 731),
    ("par quoi commencer notre design system", 732),
    ("comment mener ce test a/b proprement", 733),
    ("prépare le guide de nos interviews utilisateurs", 734),
    ("70 % des inscrits partent après l'accueil, corrige l'onboarding", 735),
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
    ("quelles clauses ne pas oublier dans ce contrat", 750),
    ("quelles obligations rgpd pour notre pme", 751),
    ("faut-il déposer notre marque avant le lancement", 752),
    ("sommes-nous concernés par l'ai act pour le tri de cv", 753),
    ("notre serveur a été compromis, procédure d'incident", 754),
    ("mets en place la sauvegarde 3-2-1", 755),
    ("fais la routine de nettoyage de mes appareils", 756),
    ("forme mon équipe au phishing", 757),
    ("est-ce que ce site marchand est sûr pour payer", 758),
    ("quelles démarches pour embaucher mon premier salarié", 759),
    ("notre comité est hybride et les distants décrochent", 760),
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
    ("automatiser la revue de mes pr", 821),
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
    assert len(sommaire) == 1351, f"sommaire : {len(sommaire)} lignes"

    signaux = {}
    for sig, num, dom in RE_ROUTAGE.findall(canvas):
        n = int(num)
        assert n not in signaux, f"signal dupliqué pour {n}"
        signaux[n] = sig.strip()
        assert sommaire[n][1] == dom.strip(), f"domaine incohérent pour {n}"
    assert len(signaux) == 1350

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
    assert len(cartes) == 28, f"carte : {len(cartes)}"
    assert len(mot_cles) == 1350, f"index : {len(mot_cles)}"

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
    assert len(branches) == 1350, f"arbre : {len(branches)} skills couvertes"
    return sommaire, signaux, mot_cles, branches, noms_courts, cartes


def _json_dumps(x) -> str:
    import json
    return json.dumps(x, ensure_ascii=False)


VEC_DIM = 64  # dimension des embeddings locaux (hash bag-of-words normalisé) — 64 suffit à 1350 skills, 2x plus rapide
CATALOGUE_VERSION = "12.0.0"  # version sémantique du catalogue (vague 12 = 900 sections)
VEC_SEUIL = 0.88  # candidat vec (exit 0) : seuil strict, le contextual enrichment monte les cosinus  # cosinus min pour qu'une candidate vectorielle compte (secours sémantique)
VEC_PISTE = 0.80  # au-dessus, la meilleure candidate vec devient piste (exit 1) — même seuil que les candidats


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


def cmd_build(chemin: Path, db_path: Path = DB_PATH, from_skills: bool = False) -> None:
    if from_skills:
        sommaire, signaux, mot_cles, branches, noms_courts, _, syns_par_num, cartes_brutes = \
            extraire_frontmatter(Path(__file__).resolve().parent / "skills")
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
            nom_court TEXT NOT NULL DEFAULT ''
        );
        CREATE TABLE domaines (
            domaine   TEXT PRIMARY KEY,
            mots_cles TEXT NOT NULL
        );
        CREATE TABLE synonymes (
            synonyme      TEXT PRIMARY KEY,
            synonyme_norm TEXT NOT NULL DEFAULT '',
            num           INTEGER NOT NULL
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
            PRIMARY KEY (mot_cle_norm, num)
        ) WITHOUT ROWID;
        CREATE TABLE IF NOT EXISTS trigrammes (
            trigramme TEXT NOT NULL,
            num       INTEGER NOT NULL,
            PRIMARY KEY (trigramme, num)
        ) WITHOUT ROWID;
        CREATE TABLE IF NOT EXISTS versions (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            date      TEXT NOT NULL DEFAULT (datetime('now')),
            nb_skills INTEGER NOT NULL,
            ajouts    TEXT NOT NULL DEFAULT '[]',
            supprimes TEXT NOT NULL DEFAULT '[]',
            modifies  TEXT NOT NULL DEFAULT '[]'
        );
    """)
    if old_snapshot:
        db.execute("INSERT OR REPLACE INTO meta VALUES ('snapshot', ?)",
                   (old_snapshot[0],))
    db.executemany("INSERT INTO domaines VALUES (?, ?)", cartes)
    for num in sorted(sommaire):
        nom, dom = sommaire[num]
        sig = signaux.get(num, "")
        mc = mot_cles.get(num, "")
        br = branches.get(num, "")
        nc = noms_courts.get(num, "")
        db.execute("INSERT INTO skills VALUES (?,?,?,?,?,?,?)",
                   (num, nom, dom, sig, mc, br, nc))
        if vec_ok:
            # contextual enrichment : préfixer par domaine + branche avant l'embedding
            ctx = f"[{dom} | {br}] " if (dom or br) else ""
            db.execute("INSERT INTO skills_vec(num, embedding) VALUES (?,?)",
                       (num, embed_hash(ctx + " ".join(x for x in (nom, sig, mc, nc) if x))))
    connus = {n for (n,) in db.execute("SELECT num FROM skills")}
    if 0 not in connus:  # pack autonome : recréer la skill 0 (routeur)
        db.execute("INSERT INTO skills VALUES (0, '🧭 Routeur de skills', 'Routage', '', '', '', '')")
        db.execute("INSERT INTO skills_fts VALUES (0, 'Routeur de skills', '', '', 'Routeur', 'Routage')")
        db.commit()
        connus = {n for (n,) in db.execute("SELECT num FROM skills")}
    for num, syns in SYN_A_UTILISER.items():
        for syn in syns:
            assert num in connus, f"synonyme « {syn} » -> skill inexistante {num}"
            db.execute("INSERT OR IGNORE INTO synonymes VALUES (?,?,?)", (syn, norm(syn), num))
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
        mcs.append((norm(r[1]), r[0]))
    db.executemany("INSERT OR IGNORE INTO mots_cles VALUES (?,?)", mcs)
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
                    tg.append((tri, r[0]))
    db.executemany("INSERT OR IGNORE INTO trigrammes VALUES (?,?)", tg)
    db.commit()
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
               (n, _json_dumps(ajouts), _json_dumps(supprimes), _json_dumps(modifies)))
    db.execute("INSERT OR REPLACE INTO meta VALUES ('snapshot', ?)", (snapshot,))
    db.execute("INSERT OR REPLACE INTO meta VALUES ('version', ?)", (CATALOGUE_VERSION,))
    db.commit()
    db.execute("PRAGMA optimize")
    db.execute("VACUUM")
    db.close()
    if db_path == DB_PATH:
        print(f"skills.db reconstruit : {n} skills · {d} domaines · "
              f"{s} synonymes · {f} lignes FTS · {v} vecteurs")


# ---------------------------------------------------------------------------
# route : base -> candidates
# ---------------------------------------------------------------------------

def proches_trigrammes_sql(db: sqlite3.Connection, qt, ratio_mini=0.6,
                           vus=None):
    """Passe floue par trigrammes en SQL (table `trigrammes` indexée).
    Même contrat que proches_trigrammes : liste triée (ratio, nb, mot, row).
    Repli sur la version Python si la table est absente (base ancienne)."""
    req_tri = {t: {t[i:i + 3] for i in range(len(t) - 2)}
               for t in qt if len(t) >= 5}
    if not req_tri:
        return []
    if not db.execute("SELECT 1 FROM sqlite_master WHERE name='trigrammes'").fetchone():
        return proches_trigrammes(db, qt, ratio_mini, vus)
    best = {}
    for t, tri in req_tri.items():
        ph = ",".join("?" * len(tri))
        for num, c in db.execute(
                f"SELECT num, COUNT(*) FROM trigrammes WHERE trigramme IN ({ph}) "
                f"GROUP BY num", tuple(tri)):
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
    skills = {r["num"]: r for r in db.execute(
        f"SELECT num, nom, domaine, signal, mot_cle, nom_court FROM skills "
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


def chercher(db: sqlite3.Connection, query: str, top: int) -> dict:
    q = norm(query)
    qt = tokens(query)
    qn = q  # forme normalisée hoistée (évite de re-normaliser dans les boucles)
    qt_forts = [t for t in qt if len(t) >= 3]
    res = {"exact": [], "fts": [], "vec": [], "flou": [], "pistes": [],
           "domaines": [], "direct": None}
    vus = set()

    def cand(num, nom, domaine, signal, voie, cible, score=None):
        d = {"num": num, "nom": nom, "domaine": domaine, "signal": signal,
             "voie": voie, "cible": cible, "section": f"## {num}."}
        if score is not None:
            d["score"] = score
        return d

    # 0) renvoi direct « skill N » (n'importe où dans la demande)
    m = re.search(r"skill (\d+)", q)
    if m:
        r = db.execute("SELECT num, nom, domaine, signal FROM skills WHERE num=?",
                       (int(m.group(1)),)).fetchone()
        if r:
            res["direct"] = cand(r["num"], r["nom"], r["domaine"],
                                 r["signal"] or "(routeur)", "direct", None)

    # 1) mot-clé canonique : égalité puis inclusion, en SQL sur mots_cles (indexé)
    if qn:
        rows_mc = db.execute(
            "SELECT m.num, s.nom, s.domaine, s.signal, m.mot_cle_norm AS mot_cle FROM mots_cles m "
            "JOIN skills s ON s.num = m.num "
            "WHERE m.mot_cle_norm = ? OR (length(?) >= 5 AND instr(m.mot_cle_norm, ?) > 0) "
            "   OR (length(m.mot_cle_norm) >= 5 AND instr(?, m.mot_cle_norm) > 0)",
            (qn, qn, qn, qn)).fetchall()
        for r in rows_mc:
            res["exact"].append(cand(r["num"], r["nom"], r["domaine"],
                                     r["signal"], "mot-clé", r["mot_cle"]))
            vus.add(r["num"])
    for r in db.execute("SELECT m.num, s.nom, s.domaine, s.signal, m.mot_cle_norm AS mot_cle FROM mots_cles m "
                       "JOIN skills s ON s.num = m.num"):
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
            "SELECT s.synonyme, k.num, k.nom, k.domaine, k.signal FROM synonymes s "
            "JOIN skills k ON k.num = s.num "
            "WHERE instr(?, s.synonyme_norm) > 0 OR instr(s.synonyme_norm, ?) > 0",
            (qn, qn)).fetchall()
    else:
        rows_syn = []
    for r in rows_syn:
        sn = r["synonyme_norm"] if "synonyme_norm" in r.keys() else norm(r["synonyme"])
        if r["num"] in vus:
            continue
        touche = sn in qn or (len(sn) >= 6 and any(len(t) >= 7 and t[:7] == sn[:7] for t in qt))
        if touche:
            res["exact"].append(cand(r["num"], r["nom"], r["domaine"],
                                     r["signal"], "synonyme", r["synonyme"]))
            vus.add(r["num"])
    res["exact"] = res["exact"][:top]

    # 3) FTS5 : préfixes, ET puis OU, bm25 pondéré
    if qt_forts:
        poids = "bm25(skills_fts, 0.0, 2.0, 6.0, 10.0, 3.0, 1.0)"
        for op in ("AND", "OR"):
            match = (" ".join(f'"{t}"*' for t in qt_forts) if op == "AND"
                     else " OR ".join(f'"{t}"*' for t in qt_forts))
            try:
                hits = db.execute(
                    "SELECT num, nom, domaine, signal, mot_cle, nom_court, "
                    + poids + " AS score "
                    "FROM skills_fts WHERE skills_fts MATCH ? "
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
            "SELECT 1 FROM sqlite_master WHERE name='skills_vec'").fetchone()
    except sqlite3.Error:
        has_vec = None
    if has_vec and qt_forts:
        qvec = embed_hash(query)
        try:
            hits = db.execute(
                "SELECT v.num, s.nom, s.domaine, s.signal, 1 - distance AS cos "
                "FROM skills_vec v JOIN skills s ON s.num = v.num "
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
                    "FROM skills_vec v JOIN skills s ON s.num = v.num "
                    "WHERE v.embedding MATCH ? AND k = 1 ORDER BY distance",
                    (qvec,)).fetchone()
                if r0 and r0["cos"] >= VEC_PISTE and r0["num"] not in vus:
                    res["pistes"].append(cand(r0["num"], r0["nom"], r0["domaine"],
                                              r0["signal"], "piste-vec", None,
                                              round(r0["cos"], 3)))
            except sqlite3.OperationalError:
                pass

    # 3b) passe floue : trigrammes communs (fautes de frappe), si rien trouvé ;
    #     en dessous du seuil, les meilleurs recouvrements deviennent pistes
    if not res["exact"] and not res["fts"] and not res["vec"] and not res["pistes"]:
        pistes_vues = set()
        for ratio, nb, t, r in proches_trigrammes_sql(db, qt_forts, 0.65, vus):
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
                n = db.execute("SELECT COUNT(*) FROM skills WHERE domaine=?",
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

    # 6) fusion RRF (k=60) des voies en un classement hybride : rang plutôt que score brut
    K_RRF = 60
    fusion = {}
    for voie, liste in (("exact", res["exact"]), ("fts", res["fts"]),
                        ("vec", res["vec"]), ("flou", res["flou"])):
        for rang, c in enumerate(liste):
            fusion.setdefault(c["num"], {"c": c, "rrf": 0.0, "voies": []})
            fusion[c["num"]]["rrf"] += 1.0 / (K_RRF + rang)
            fusion[c["num"]]["voies"].append(voie)
    for v in fusion.values():
        v["c"]["rrf"] = round(v["rrf"], 4)
        v["c"]["voies"] = v["voies"]
    res["fusion"] = [v["c"] for v in sorted(fusion.values(), key=lambda v: -v["rrf"])][:top]
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


def cmd_route(query: str, top: int, as_json: bool, tag: str | None = None) -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA cache_size=-8000")
    charger_vec(db)
    res = chercher(db, query, top)
    if tag:
        # pré-filtre optionnel par tag : ne garder que les skills taguées
        try:
            tag_nums = {r["num"] for r in db.execute("SELECT num FROM tags WHERE tag=?", (norm(tag),))}
            for k in ("exact", "fts", "vec", "flou", "pistes"):
                res[k] = [c for c in res[k] if c["num"] in tag_nums]
        except sqlite3.OperationalError:
            pass
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
        print(f"⤳ Section : {candidats[0]['section']}")
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

def cmd_test() -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    echecs = []
    for demande, attendu in TESTS_ROUTAGE:
        res = chercher(db, demande, 5)
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
    db.close()
    if echecs:
        print(f"✖ {len(echecs)}/{len(TESTS_ROUTAGE)} tests en échec :")
        for demande, attendu, obtenu in echecs:
            print(f"  - « {demande} » : attendu {attendu}, obtenu {obtenu}")
        return 1
    print(f"✅ {len(TESTS_ROUTAGE)}/{len(TESTS_ROUTAGE)} tests de routage passés")
    return 0


def cmd_sonde(fichier, top):
    if not DB_PATH.exists():
        raise SystemExit('skills.db introuvable')
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    sujets = []
    for d in db.execute('SELECT domaine, mots_cles FROM domaines ORDER BY domaine'):
        for kw in re.findall('[a-z0-9-]+', norm(d['mots_cles'])):
            if len(kw) >= 4:  # sujets < 4 lettres = artefacts de sonde (ex. « ton »)
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


def cmd_export(canvas: Path, fichier: Path | None = None, complet: bool = False) -> int:
    """Exporte toutes les sections du catalogue en JSON (compact par défaut, --complet pour le texte intégral)."""
    texte = Path(canvas).read_text(encoding="utf-8")
    sommaire, signaux, mot_cles, branches, noms_courts, cartes = extraire(texte)

    sections = _sections_multi(canvas)
    assert sections, "aucune section « ## N. » trouvée"

    synonymes: dict[int, list[str]] = {}
    for syn, num in SYNONYMES:
        synonymes.setdefault(num, []).append(syn)

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

## Contenu
- `skills/` — {nb} fichiers `NNN-slug.md` (frontmatter YAML complet : num, nom, domaine, signal, mot_cle, synonymes, cross_refs)
- `routage.py` — routeur autonome (build, route, test, lint, export, sonde, vocab, versions, analytics)
- `manifeste.json` — version sémantique (meta), nombre de skills, domaines, hash sha256 des fichiers skills

## Commandes utiles
- `route "<demande>"` → skill 0/1/2 (0 = trouvée, 1 = piste, 2 = rien)
- `route "<demande>" --json` → candidats avec voie et score
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
        "skills": nb,
        "domaines": 28,
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
            import sqlite3 as _sq
            sys_path_backup = list(sys.path)
            sys.path.insert(0, str(td))
            try:
                spec = importlib.util.spec_from_file_location("rt_pack", td / "routage.py")
                rt = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(rt)
                rt.cmd_build(td / "routage.py", db_path=td / "skills.db", from_skills=True)
                db = _sq.connect(td / "skills.db")
                got = {t: db.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
                       for t in ("skills", "synonymes", "domaines", "skills_fts", "trigrammes")}
                gh = hashlib.sha256()
                for f in sorted((td / "skills").glob("*.md")):
                    gh.update(f.name.encode()); gh.update(f.read_bytes())
                hash_ok = gh.hexdigest() == h
            finally:
                sys.path[:] = sys_path_backup
            ref = sqlite3.connect(Path(__file__).resolve().with_name("skills.db"))  # DB du dépôt courant
            attendu = {t: ref.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
                       for t in ("skills", "synonymes", "domaines", "skills_fts", "trigrammes")}
            ref.close()
            # trigrammes : tolérance 1 % (source canvas vs fichiers peut différer marginalement)
            tri_ok = abs(got["trigrammes"] - attendu["trigrammes"]) <= max(1, attendu["trigrammes"] // 100)
            autres = {k: v for k, v in attendu.items() if k != "trigrammes"}
            ok = all(got[k] == v for k, v in autres.items()) and tri_ok and hash_ok
            print("pack check:", "✅ FIDÈLE" if ok else f"❌ écart {got} vs {attendu}, hash_ok={hash_ok}")
            return 0 if ok else 1
    sortie.parent.mkdir(parents=True, exist_ok=True)
    # deflate reste le meilleur sur du markdown (testé : LZMA 2,2 Mo vs deflate 1,93 Mo) ;
    # aucun impact runtime — la décompression ne se fait qu'à l'extraction du pack
    with zipfile.ZipFile(sortie, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in sorted((RACINE / "skills").glob("*.md")):
            # (skills.db est régénéré par build --from-skills : exclu du pack)
            z.write(f, f"skills/{f.name}")
        z.write(RACINE / "outils" / "routage.py", "routage.py")
        z.writestr("manifeste.json", json.dumps(manifeste, ensure_ascii=False, indent=2))
        z.writestr("README.md", README_PACK.format(nb=nb))
    print(f"✅ pack exporté : {sortie} ({sortie.stat().st_size/1e6:.2f} Mo, {nb} skills, hash {h[:12]}…)")
    print(f"   test de fidélité : python3 outils/routage.py pack --check")
    return 0


def cmd_skillmd(sortie: Path) -> int:
    """Génère un dossier de SKILL.md (standard ouvert Agent Skills : frontmatter
    name/description + corps) depuis skills/*.md — installable via `npx skills add`."""
    import re as _re, unicodedata
    def norm(s):
        s = unicodedata.normalize("NFKD", s)
        return "".join(c for c in s if not unicodedata.combining(c)).lower()
    sortie.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sorted((Path(__file__).resolve().parent.parent / "skills").glob("*.md")):
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
    for _, dom in sommaire.values():
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

    p_gen = sub.add_parser("generate", help="base -> sections de routage du canvas")
    p_gen.add_argument("canvas", nargs="?", type=Path, default=CANVAS_PAR_DEFAUT)
    p_gen.add_argument("--check", action="store_true")

    sub.add_parser("test", help="non-régression du routage")

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

    p_cnt = sub.add_parser("count", help="compte les skills -> totalSkillsCount.md")
    p_cnt.add_argument("canvas", nargs="?", type=Path, default=CANVAS_PAR_DEFAUT)
    p_cnt.add_argument("--dossier", type=Path, default=RACINE / "data")

    args = ap.parse_args()
    if args.cmd == "build":
        cmd_build(args.canvas, from_skills=args.from_skills)
    elif args.cmd == "route":
        raise SystemExit(cmd_route(args.query, args.top, args.json, getattr(args, "tag", None)))
    elif args.cmd == "generate":
        raise SystemExit(cmd_generate(args.canvas, args.check))
    elif args.cmd == "test":
        raise SystemExit(cmd_test())
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
        raise SystemExit(cmd_export(args.canvas, args.fichier, args.complet))
    elif args.cmd == "count":
        raise SystemExit(cmd_count(args.canvas, args.dossier))


if __name__ == "__main__":
    main()
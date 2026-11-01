
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""routage.py — outillage SQL du routage de la Bibliothèque de Skills AI.

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

Sous-commandes :
  build    (re)construit skills.db depuis le canvas : tables skills, domaines,
           synonymes + index full-text FTS5 (unicode61) avec triggers.
  route    cascade : renvoi direct -> mot-clé canonique -> synonyme ->
           full-text FTS5 (bm25 pondéré : mot-clé > signal > nom court > nom)
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
    ("declaration", 297),
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
    ("voisinage", 529),
    ("voisin", 529),
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
    ("préavis", 555),
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
    ("impots", 297),
    ("traduire un texte", 7),
    ("résumer un document", 5),
    ("publicité", 3),
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
]

# ---------------------------------------------------------------------------
# Outils communs
# ---------------------------------------------------------------------------

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


def extraire(canvas: str):
    sommaire = {}
    for num, nom, dom in RE_SOMMAIRE.findall(canvas):
        sommaire[int(num)] = [nom.strip(), dom.strip()]
    assert len(sommaire) == 617, f"sommaire : {len(sommaire)} lignes"

    signaux = {}
    for sig, num, dom in RE_ROUTAGE.findall(canvas):
        n = int(num)
        assert n not in signaux, f"signal dupliqué pour {n}"
        signaux[n] = sig.strip()
        assert sommaire[n][1] == dom.strip(), f"domaine incohérent pour {n}"
    assert len(signaux) == 616

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
    assert len(mot_cles) == 616, f"index : {len(mot_cles)}"

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
    assert len(branches) == 616, f"arbre : {len(branches)} skills couvertes"
    return sommaire, signaux, mot_cles, branches, noms_courts, cartes


def cmd_build(chemin: Path, db_path: Path = DB_PATH) -> None:
    sommaire, signaux, mot_cles, branches, noms_courts, cartes = extraire(
        chemin.read_text(encoding="utf-8"))
    if db_path.exists():
        db_path.unlink()
    db = sqlite3.connect(db_path)
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
            synonyme TEXT PRIMARY KEY,
            num      INTEGER NOT NULL
        );
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
    """)
    db.executemany("INSERT INTO domaines VALUES (?, ?)", cartes)
    for num in sorted(sommaire):
        nom, dom = sommaire[num]
        db.execute("INSERT INTO skills VALUES (?,?,?,?,?,?,?)",
                   (num, nom, dom, signaux.get(num, ""), mot_cles.get(num, ""),
                    branches.get(num, ""), noms_courts.get(num, "")))
    connus = {n for (n,) in db.execute("SELECT num FROM skills")}
    for syn, num in SYNONYMES:
        assert num in connus, f"synonyme « {syn} » -> skill inexistante {num}"
        db.execute("INSERT OR IGNORE INTO synonymes VALUES (?,?)", (syn, num))
    db.commit()
    n = db.execute("SELECT COUNT(*) FROM skills").fetchone()[0]
    d = db.execute("SELECT COUNT(*) FROM domaines").fetchone()[0]
    s = db.execute("SELECT COUNT(*) FROM synonymes").fetchone()[0]
    f = db.execute("SELECT COUNT(*) FROM skills_fts").fetchone()[0]
    db.close()
    if db_path == DB_PATH:
        print(f"skills.db reconstruit : {n} skills · {d} domaines · "
              f"{s} synonymes · {f} lignes FTS")


# ---------------------------------------------------------------------------
# route : base -> candidates
# ---------------------------------------------------------------------------

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
    qt_forts = [t for t in qt if len(t) >= 3]
    res = {"exact": [], "fts": [], "flou": [], "pistes": [], "domaines": [],
           "direct": None}
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

    # 1) mot-clé canonique : égalité puis inclusion
    for r in db.execute("SELECT num, nom, domaine, signal, mot_cle FROM skills "
                        "WHERE mot_cle != ''"):
        kw = norm(r["mot_cle"])
        if q and (q == kw or (len(q) >= 5 and q in kw)
                  or (len(kw) >= 5 and kw in q)):
            res["exact"].append(cand(r["num"], r["nom"], r["domaine"],
                                     r["signal"], "mot-clé", r["mot_cle"]))
            vus.add(r["num"])
    for r in db.execute("SELECT num, nom, domaine, signal, mot_cle FROM skills "
                       "WHERE mot_cle != ''"):
        if r["num"] in vus:
            continue
        kwt = set(tokens(r["mot_cle"]))
        if kwt and kwt <= set(qt):
            res["exact"].append(cand(r["num"], r["nom"], r["domaine"],
                                     r["signal"], "mot-clé", r["mot_cle"]))
            vus.add(r["num"])
    res["exact"] = res["exact"][:top]

    # 2) synonymes (mots simples par token, expressions par inclusion)
    for r in db.execute("SELECT s.synonyme, k.num, k.nom, k.domaine, k.signal "
                        "FROM synonymes s JOIN skills k ON k.num = s.num"):
        sn = norm(r["synonyme"])
        simple = sn.isalnum() and " " not in sn
        if simple:
            # tolérance aux conjugaisons : préfixe commun >= 7 caractères
            # (à 6, des faux amis passaient : persona/personnel)
            touche = (sn in qt or (len(sn) >= 6 and sn in q)
                      or any(len(t) >= 7 and len(sn) >= 7
                             and t[:7] == sn[:7] for t in qt))
        else:
            touche = sn in q
        if touche and r["num"] not in vus:
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

    # 3b) passe floue : trigrammes communs (fautes de frappe), si rien trouvé ;
    #     en dessous du seuil, les meilleurs recouvrements deviennent pistes
    if not res["exact"] and not res["fts"]:
        pistes_vues = set()
        for ratio, nb, t, r in proches_trigrammes(db, qt_forts, 0.35, vus):
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
    if not res["exact"] and not res["fts"] and not res["flou"]:
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


def cmd_route(query: str, top: int, as_json: bool) -> int:
    if not DB_PATH.exists():
        raise SystemExit("skills.db introuvable — lance d'abord : routage.py build")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    res = chercher(db, query, top)
    candidats = ([res["direct"]] if res["direct"] else []) + res["exact"] \
        + res["fts"] + res["flou"]
    code = 0 if candidats else (1 if res["domaines"] else 2)
    if code == 2:
        _journaliser(db, query)
    try:
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
    for r in res["exact"]:
        print(f"◆ Skill {r['num']} · {r['nom']} · [{r['domaine']}]")
        print(f"  ↳ {r['voie']} « {r['cible']} » — signal : {r['signal']}")
    for r in res["fts"]:
        print(f"◇ Skill {r['num']} · {r['nom']} · [{r['domaine']}]")
        print(f"  ↳ full-text (score {r['score']}) — signal : {r['signal']}")
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
            if len(kw) >= 3:
                sujets.append((kw, d['domaine']))
    for r in db.execute('SELECT num, signal, domaine FROM skills WHERE signal != "" ORDER BY num'):
        sujets.append((r['signal'], r['domaine']))
    couverts, partiels, gaps = [], [], []
    for sujet, domaine in sujets:
        res = chercher(db, sujet, top)
        nums = sorted({r['num'] for r in res['exact'] + res['fts'] + res['flou']}
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
        "catalogue": "Bibliothèque de Skills AI",
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
        "# Compteur de skills — Bibliothèque de Skills AI",
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
        "« totalSkillsCount — Bibliothèque de Skills AI ».",
    ]

    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    fichier = dossier / "totalSkillsCount.md"
    fichier.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"✅ {total} sections ({operationnelles} skills + 1 routeur) — "
          f"{len(domaines)} domaines -> {fichier}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Routage SQL — Bibliothèque de Skills AI")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_build = sub.add_parser("build", help="canvas -> skills.db")
    p_build.add_argument("canvas", nargs="?", type=Path, default=CANVAS_PAR_DEFAUT)

    p_route = sub.add_parser("route", help="recherche rapide d'une skill")
    p_route.add_argument("query")
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
        cmd_build(args.canvas)
    elif args.cmd == "route":
        raise SystemExit(cmd_route(args.query, args.top, args.json))
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
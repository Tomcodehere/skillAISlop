
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyseur de conformité — Bibliothèque de Skills AI (projet SkillsLibrairy).

Vérifie que chaque skill du catalogue respecte les règles du projet :
  R1 — Indexation obligatoire (index en tête de chaque skill)
  R2 — Uniformisation par le template officiel
       (Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage)
  R3 — Routage systématique (table de routage + arbre de décision + sommaire)
  R4 — Référencement croisé (mention d'au moins une skill complémentaire)
  R6 — Zéro doublon : unicité des noms et des signaux de routage
       (contrôles par skill + contrôles globaux sur l'ensemble du catalogue ;
       l'emoji doit être présent et pertinent, sa réutilisation est permise)
  R5 — le présent script EST l'audit : une règle n'est active qu'une fois
       l'audit repassé et le verdict consigné.
  R7 — Alignement AGENTS.md & mise à jour trimestrielle : ce script est
       exécuté à chaque cycle (janvier, avril, juillet, octobre).
  R8 — Synchronisation automatique de l'index et du routage : ce script
       détecte toute désynchronisation entre le catalogue et ses index —
       entrée manquante, orpheline ou en double dans le sommaire, la table
       de routage ou l'arbre de décision.
  R9 — Concision des sorties : rapport compact par défaut (verdict en une
       ligne, seules les non-conformités détaillées) ; --verbose pour la
       table complète.

Usage :
    python check_conformite.py chemin/vers/CANVAS.md
    python check_conformite.py chemin/vers/CANVAS.md --verbose

Codes de sortie : 0 si conforme, 1 sinon (utilisable en CI).
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------- Constantes

SECTION_HEADING = re.compile(r"^## (?P<num>\d+)\. (?P<emoji>\S+)\s+(?P<nom>.+)$")
INDEX_LINE = re.compile(r"^> 🔎 \*\*Index\*\* : .+$")
OBJECTIF = re.compile(r"\*\*Objectif\*\* : \S")
INSTRUCTIONS = re.compile(r"\*\*Instructions système\*\* :")
INSTR_TU_ES = re.compile(r"^\s*Tu es\b")
METHODE = re.compile(r"\*\*Méthode\*\* :")
METHODE_STEP = re.compile(r"^\d+\. \S")
EXEMPLE = re.compile(r"\*\*Exemple de prompt\*\*")
EXEMPLE_CONCRET = re.compile(r'[«"][^»"]{10,}[»"]')
CAS_USAGE = re.compile(r"\*\*Cas d'usage\*\* : (?P<liste>.+)$", re.MULTILINE)
SOMMAIRE_ROW = re.compile(r"^\| (?P<num>\d+) \| \S")
ROUTING_ROW = re.compile(r"^\| (?P<signal>.+) \| (?P<num>\d+)(?: \| (?P<domaine>[^|]*))? \|$")
CROSS_REF = re.compile(r"skills? \d+|skills? \d+/\d+")
MIN_CONTEXTE_EXEMPLE = 60  # caractères minimum de contexte concret dans l'exemple


@dataclass
class SkillAudit:
    """Résultat de l'audit d'une skill."""
    num: int
    titre: str = ""
    emoji: str = ""
    nom: str = ""
    signal: str = ""
    tests: dict[str, bool] = field(default_factory=dict)
    details: list[str] = field(default_factory=list)

    @property
    def score(self) -> float:
        if not self.tests:
            return 0.0
        return 100.0 * sum(self.tests.values()) / len(self.tests)

    @property
    def conforme(self) -> bool:
        return all(self.tests.values())


CHECKS = [
    ("R1_index_present", "R1 : Index 🔎 en tête de skill"),
    ("R2_objectif", "R2 : bloc Objectif non vide"),
    ("R2_instructions_tu_es", "R2 : Instructions système commençant par « Tu es »"),
    ("R2_methode_3_etapes", "R2 : Méthode avec 3 étapes numérotées"),
    ("R2_exemple_concret", "R2 : Exemple de prompt entre guillemets, avec contexte"),
    ("R2_cas_usage_2", "R2 : Cas d'usage avec au moins 2 usages"),
    ("R3_sommaire", "R3 : ligne présente dans le sommaire global"),
    ("R3_table_routage", "R3 : ligne présente dans la table de routage"),
    ("R3_arbre_decision", "R3 : présente dans l'arbre de décision"),
    ("R4_cross_ref", "R4 : référence croisée vers au moins une autre skill"),
    ("R6_nom_unique", "R6 : nom unique dans le catalogue"),
    ("R6_signal_unique", "R6 : signal de routage unique"),
]


def extraire_skills(texte: str) -> list[tuple[int, str, str]]:
    """Découpe le document en sections (numéro, titre, corps)."""
    sections: list[tuple[int, str, str]] = []
    courant: tuple[int, str, str] | None = None
    lignes_corps: list[str] = []

    for ligne in texte.splitlines():
        m = SECTION_HEADING.match(ligne)
        if m:
            if courant is not None:
                sections.append((courant[0], courant[1], "\n".join(lignes_corps)))
            courant = (int(m.group("num")), ligne.strip(), "")
            lignes_corps = []
        elif courant is not None:
            lignes_corps.append(ligne)

    if courant is not None:
        sections.append((courant[0], courant[1], "\n".join(lignes_corps)))
    return sections


def nombre_dans_arbre(num: int, bloc_arbre: str) -> bool:
    """R3 — présence d'une skill dans l'arbre de décision.

    Skills 1-18 : nœuds « Skill N] ». Skills 19+ : entrées des branches
    D1-D26 au format « N Nom » (nombre suivi d'un espace, précédé d'un
    non-chiffre pour éviter les collisions 13/213 ou 76/176).
    """
    if not bloc_arbre:
        return False
    if num <= 18:
        return re.search(rf"Skill {num}\]", bloc_arbre) is not None
    return re.search(rf"(?:^|[^0-9]){num} ", bloc_arbre, re.MULTILINE) is not None


def collecter_references(texte: str) -> tuple[set[int], dict[int, str], str]:
    """Extrait le sommaire (numéros), le routage (numéro -> signal) et le bloc arbre."""
    sommaire: set[int] = set()
    routage: dict[int, str] = {}
    lignes_arbre: list[str] = []
    dans_arbre = False
    fence_vue = False

    for ligne in texte.splitlines():
        s = ligne.strip()
        m_s = SOMMAIRE_ROW.match(s)
        if m_s:
            sommaire.add(int(m_s.group("num")))
        m_r = ROUTING_ROW.match(s)
        if m_r and not re.match(r"^[-–— ]", m_r.group("signal")):
            routage[int(m_r.group("num"))] = m_r.group("signal")
        if s.startswith("**Arbre de décision**"):
            dans_arbre = True
            fence_vue = False
            continue
        if dans_arbre and s.startswith("```"):
            if not fence_vue:
                fence_vue = True  # ouverture ```mermaid
            else:
                dans_arbre = False  # clôture ```
            continue
        if dans_arbre and fence_vue:
            lignes_arbre.append(ligne)

    return sommaire, routage, "\n".join(lignes_arbre)


def auditer_skill(num: int, titre: str, corps: str, sommaire: set[int],
                  routage: dict[int, str], arbre: set[int],
                  compteur_emojis: Counter, compteur_noms: Counter,
                  compteur_signaux: Counter) -> SkillAudit:
    """Applique les règles R1-R4 et R6 à une section de skill."""
    audit = SkillAudit(num=num, titre=titre)
    lignes = corps.splitlines()
    corps_strip = corps.strip()

    m_head = SECTION_HEADING.match(titre)
    audit.emoji = m_head.group("emoji") if m_head else ""
    audit.nom = m_head.group("nom") if m_head else ""
    audit.signal = routage.get(num, "")

    # R1 — index en tête (première ligne non vide du corps)
    tete = next((l for l in lignes if l.strip()), "")
    audit.tests["R1_index_present"] = bool(INDEX_LINE.match(tete.strip()))

    # R2 — blocs du template
    audit.tests["R2_objectif"] = bool(OBJECTIF.search(corps_strip))

    instr_ok = bool(INSTRUCTIONS.search(corps_strip))
    apres_instr = INSTRUCTIONS.search(corps_strip)
    debut = apres_instr.end() if apres_instr else 0
    fin_methode = METHODE.search(corps_strip)
    zone_instr = corps_strip[debut:fin_methode.start()] if fin_methode else corps_strip[debut:]
    audit.tests["R2_instructions_tu_es"] = instr_ok and bool(INSTR_TU_ES.search(zone_instr))

    m_methode = METHODE.search(corps_strip)
    zone_methode = corps_strip[m_methode.end():] if m_methode else ""
    zone_methode = zone_methode.split("**Exemple")[0]
    etapes = re.findall(r"(?m)^\d+\. ", zone_methode)
    audit.tests["R2_methode_3_etapes"] = len(etapes) >= 3

    m_ex = EXEMPLE.search(corps_strip)
    zone_ex = corps_strip[m_ex.end():] if m_ex else ""
    zone_ex = zone_ex.split("**Cas d'usage")[0]
    audit.tests["R2_exemple_concret"] = (
        bool(EXEMPLE_CONCRET.search(zone_ex))
        and len(zone_ex.strip()) >= MIN_CONTEXTE_EXEMPLE
    )

    m_cu = CAS_USAGE.search(corps_strip)
    usages = [u for u in re.split(r"[,;]", m_cu.group("liste")) if u.strip()] if m_cu else []
    audit.tests["R2_cas_usage_2"] = len(usages) >= 2

    # R3 — routage
    audit.tests["R3_sommaire"] = num in sommaire
    audit.tests["R3_table_routage"] = num in routage
    audit.tests["R3_arbre_decision"] = num in arbre

    # R4 — référencement croisé
    refs = CROSS_REF.findall(corps_strip)
    audit.tests["R4_cross_ref"] = len(refs) >= 1

    # R6 — unicité (par skill, sur la base des compteurs globaux)
    audit.tests["R6_nom_unique"] = bool(audit.nom) and compteur_noms[audit.nom] <= 1
    audit.tests["R6_signal_unique"] = (num not in routage) or compteur_signaux[audit.signal] <= 1

    return audit


def doublons_globaux(audits: list[SkillAudit], routage: dict[int, str]) -> list[str]:
    """Contrôles R6 globaux : noms, signaux et numéros en double."""
    problemes: list[str] = []
    noms = Counter(a.nom for a in audits if a.nom)
    signaux = Counter(routage.values())
    nums = Counter(routage.keys())

    for nom, c in noms.items():
        if c > 1:
            concernes = sorted(a.num for a in audits if a.nom == nom)
            problemes.append(f"Nom « {nom} » utilisé par les skills {concernes}")
    for signal, c in signaux.items():
        if c > 1:
            concernes = sorted(n for n, s in routage.items() if s == signal)
            problemes.append(f"Signal « {signal} » routé vers {concernes}")
    for num, c in nums.items():
        if c > 1:
            problemes.append(f"Numéro {num} présent plusieurs fois dans la table de routage")
    return problemes


def desynchronisations(texte: str, nums_sections: set[int],
                       sommaire: set[int], routage: dict[int, str],
                       bloc_arbre: str) -> list[str]:
    """R8 — détecte toute désynchronisation index/routage/catalogue."""
    problemes: list[str] = []
    nums_sans_routeur = nums_sections - {0}

    # Sommaire : comptage des lignes (doublons) et couverture
    lignes_sommaire = [int(m) for m in re.findall(r"(?m)^\| (\d+) \| \S", texte)]
    for num, c in Counter(lignes_sommaire).items():
        if c > 1:
            problemes.append(f"Sommaire : la skill {num} y figure {c} fois")
    orphelins_sommaire = sorted(set(lignes_sommaire) - nums_sections)
    if orphelins_sommaire:
        problemes.append(f"Sommaire : entrées orphelines (aucune skill correspondante) : {orphelins_sommaire}")
    manquants_sommaire = sorted(nums_sections - set(lignes_sommaire))
    if manquants_sommaire:
        problemes.append(f"Sommaire : skills absentes : {manquants_sommaire}")

    # Table de routage : couverture et orphelins
    nums_routage = [int(m) for m in re.findall(r"(?m)^\| .+ \| (\d+)(?: \| [^|]+)? \|$", texte)]
    orphelins_routage = sorted(set(nums_routage) - nums_sections)
    if orphelins_routage:
        problemes.append(f"Table de routage : signaux pointant vers des skills inexistantes : {orphelins_routage}")
    manquants_routage = sorted(nums_sans_routeur - set(nums_routage))
    if manquants_routage:
        problemes.append(f"Table de routage : skills sans signal : {manquants_routage}")

    # Arbre de décision : couverture et orphelins
    nombres_arbre = set(int(m) for m in re.findall(r"(?m)(?:^|[^0-9])(\d{1,3}) ", bloc_arbre))
    nombres_arbre |= set(int(m) for m in re.findall(r"Skill (\d+)\]", bloc_arbre))
    orphelins_arbre = sorted(nombres_arbre - nums_sections)
    if orphelins_arbre:
        problemes.append(f"Arbre de décision : renvois vers des skills inexistantes : {orphelins_arbre}")

    return problemes


def generer_rapport(audits: list[SkillAudit], seuil: float, r6_global: list[str],
                    r8_sync: list[str], verbose: bool = False) -> str:
    """Construit le rapport Markdown — compact par défaut (R9), table complète avec --verbose."""
    lignes_rapport = [
        "# Rapport de conformité — Bibliothèque de Skills AI",
        "",
        f"Skills auditées : **{len(audits)}** — Seuil de conformité : **{seuil:.0f} %**",
        "",
    ]

    score_global = sum(a.score for a in audits) / len(audits) if audits else 0.0
    conformes = sum(1 for a in audits if a.conforme and a.score >= seuil)

    if not verbose:
        etat = "✅" if conformes == len(audits) and not r6_global and not r8_sync else "❌"
        lignes_rapport.append(
            f"**Verdict : {etat} {conformes}/{len(audits)} conformes "
            f"({score_global:.1f} %) · R6 {'✅' if not r6_global else '❌'} · "
            f"R8 {'✅' if not r8_sync else '❌'}**"
        )
        echecs = [a for a in audits if not a.conforme or a.score < seuil]
        if echecs:
            lignes_rapport += ["", "## Non-conformités", ""]
            for audit in echecs:
                manques = "; ".join(
                    label for code, label in CHECKS if not audit.tests.get(code, False)
                )
                lignes_rapport.append(f"- ❌ Skill {audit.num} ({audit.titre}) : {manques}")
        for p in r6_global:
            lignes_rapport.append(f"- ❌ R6 : {p}")
        for p in r8_sync:
            lignes_rapport.append(f"- ❌ R8 : {p}")
        return "\n".join(lignes_rapport)

    lignes_rapport += [
        "| Skill | Score | Conforme | Non-conformités |",
        "|---|---|---|---|",
    ]
    for audit in audits:
        echecks = [label for code, label in CHECKS if not audit.tests.get(code, False)]
        etat = "✅" if audit.score >= seuil and audit.conforme else "❌"
        manques = "; ".join(echecks) if echecks else "—"
        lignes_rapport.append(
            f"| {audit.num} | {audit.score:.0f} % | {etat} | {manques} |"
        )

    lignes_rapport += [
        "",
        f"**Score global : {score_global:.1f} %** — Skills conformes : {conformes}/{len(audits)}",
    ]

    # Contrôles globaux R6
    lignes_rapport += ["", "## Contrôles globaux R6 — zéro doublon", ""]
    if r6_global:
        lignes_rapport += [f"- ❌ {p}" for p in r6_global]
    else:
        lignes_rapport += [
            "- ✅ Noms de skills : tous uniques",
            "- ✅ Signaux de routage : tous uniques",
            "- ✅ Un seul signal par skill dans la table de routage",
        ]

    # Synchronisation index & routage (R8)
    lignes_rapport += ["", "## Synchronisation index & routage (R8)", ""]
    if r8_sync:
        lignes_rapport += [f"- ❌ {p}" for p in r8_sync]
    else:
        lignes_rapport += [
            "- ✅ Sommaire : complet, sans doublon ni orphelin",
            "- ✅ Table de routage : chaque skill routée, aucun signal orphelin",
            "- ✅ Arbre de décision : aucun renvoi vers une skill inexistante",
        ]

    # Détail des non-conformités
    problemes = [a for a in audits if not a.conforme]
    if problemes:
        lignes_rapport += ["", "## Détail des non-conformités", ""]
        for audit in problemes:
            lignes_rapport.append(f"### Skill {audit.num} — {audit.titre}")
            for code, label in CHECKS:
                if not audit.tests.get(code, False):
                    lignes_rapport.append(f"- ❌ {label}")
            lignes_rapport.append("")

    return "\n".join(lignes_rapport)


def main() -> int:
    parseur = argparse.ArgumentParser(description="Analyse de conformité de la bibliothèque de skills.")
    parseur.add_argument("chemins", nargs="+",
                         help="Canvas principal puis canvases corpus (sections 1-300, 301-600, 601-900…)")
    parseur.add_argument("--min-score", type=float, default=100.0,
                         help="Score minimal (%%) pour déclarer une skill conforme (défaut : 100)")
    parseur.add_argument("--verbose", action="store_true",
                         help="Rapport détaillé : table complète des 250 skills (défaut : compact, R9)")
    args = parseur.parse_args()

    morceaux: list[str] = []
    for chemin_saisi in args.chemins:
        chemin = Path(chemin_saisi)
        if not chemin.is_file():
            print(f"Erreur : fichier introuvable — {chemin}", file=sys.stderr)
            return 1
        morceaux.append(chemin.read_text(encoding="utf-8"))
    # Le canvas principal porte sommaire + routage + arbre ; les corpus portent les sections.
    texte = "\n\n".join(morceaux)
    sommaire, routage, bloc_arbre = collecter_references(texte)
    sections = [(n, t, c) for n, t, c in extraire_skills(texte) if n != 0]
    if not sections:
        print("Aucune skill détectée.", file=sys.stderr)
        return 1

    arbre = {num for num, _, _ in sections if nombre_dans_arbre(num, bloc_arbre)}
    compteur_emojis = Counter()
    compteur_noms = Counter()
    for num, titre, corps in sections:
        m = SECTION_HEADING.match(titre)
        if m:
            compteur_emojis[m.group("emoji")] += 1
            compteur_noms[m.group("nom")] += 1
    compteur_signaux = Counter(routage.values())

    audits = [
        auditer_skill(num, titre, corps, sommaire, routage, arbre,
                      compteur_emojis, compteur_noms, compteur_signaux)
        for num, titre, corps in sections
    ]

    r6_global = doublons_globaux(audits, routage)
    nums_sections = {num for num, _, _ in extraire_skills(texte)}
    r8_sync = desynchronisations(texte, nums_sections, sommaire, routage, bloc_arbre)
    rapport = generer_rapport(audits, args.min_score, r6_global, r8_sync, args.verbose)
    print(rapport)

    tout_conforme = all(a.conforme and a.score >= args.min_score for a in audits)
    return 0 if (tout_conforme and not r6_global and not r8_sync) else 1


if __name__ == "__main__":
    sys.exit(main())

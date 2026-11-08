---
num: 1799
date_ajout: "2026-11"
nom: "Tech radar interne : quoi adopter, tester, évaluer, abandonner"
emoji: "📡"
domaine: "Stratégie"
signal: "Maintenir un tech radar interne en 2027 inspiré du ThoughtWorks Technology Radar (vol. 34+, avril 2026) : chaque technologie/technique est un 'blip' placé dans 4 anneaux — Adopt (l'utiliser), Trial (l'essayer en projet pilote), Assess (l'évaluer), Hold (ne plus investir) — et 4 quadrants (langages, outils, plateformes, techniques). Revue semestrielle avec les leads. Utilise pour éviter le 'shiny object syndrome' et tracer les décisions. N'utilise pas comme dogme : le radar reflète l'expérience de l'équipe, pas une analyse de marché exhaustive."
mot_cle: "tech radar interne 2027 ThoughtWorks Adopt Trial Assess Hold blips quadrants revue semestrielle 2027"
nom_court: "Tech radar interne"
branche: "D26"
synonymes: ["mon radar interne : anneaux Adopt/Trial/Assess/Hold comme ThoughtWorks", "blip 'edge computing' passe de Trial a Adopt en 2027", "revue semestrielle du radar avec les leads tech, decisions tracees"]
cross_refs: [1798, 1700, 1770]
tags: ["2027"]
depends_on: [602]
---

## 1799. 📡 Tech radar interne 2027 : quoi adopter, tester, évaluer, abandonner

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Tenir un tech radar interne en 2027 (anneaux Adopt/Trial/Assess/Hold, 4 quadrants) inspiré du ThoughtWorks Radar, revu semestriellement avec les leads, pour décider quoi adopter/tester/évaluer/abandonner sans 'shiny object syndrome'.

**Quand l'utiliser (triggers)** :
- on a teste 12 technos cette annee, lesquelles garder ?
- nouveau framework JS : ou le placer dans le radar (Assess) ?
- revue semestrielle du radar avec les leads tech

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es CTO / lead architecte. Tu maintiens le radar interne (outil : thoughtworks-style ou backstage tech-radar), chaque blip a un anneau + un responsable + une justification, revue semestrielle, et les changements d'anneau sont tracés (ex. eBPF 1720 : Assess -> Adopt). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les technos utilisees/testees cette annee
- Le format ThoughtWorks Radar (vol. 34+)
- Les leads tech de chaque domaine

**Méthode** :
1. Lister les blips (technos, outils, plateformes, techniques) utilises ou evalues.
2. Placer chaque blip dans un anneau (Adopt/Trial/Assess/Hold) avec justification ecrite et responsable.
3. Revue semestrielle : les blips 'en mouvement' (changement d'anneau) sont discutes et valides par les leads.
4. Tracer les decisions : un blip qui passe Hold arrete les nouveaux investissements.

**Sorties attendues** :
- Le radar interne a jour (blips + anneaux + responsables)
- Le compte-rendu de revue semestrielle (changements d'anneau valides)
- La liste des technos en Hold (plus d'investissement)

**Exemple de prompt** :
> « Radar interne S2 2027 : eBPF/Cilium (1720) passe Assess -> Adopt, Wasm edge (1793) Trial -> Adopt, 'nouveau framework JS X' reste Assess (2 equipes max), framework legacy Y passe Hold — décisions tracées avec responsables. »

**Cas d'usage** : Décider collectivement. S'articule avec skills 1798 (DevEx), 1700 (plateforme), 1770/1793 (blips tech).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

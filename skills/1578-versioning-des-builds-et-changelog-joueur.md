---
num: 1578
date_ajout: "2026-11"
nom: "Versioning des builds et changelog joueur"
emoji: "📅"
domaine: "Game Dev"
signal: "Versionner proprement un jeu en 2027 : SemVer (1.2.3 : majeur/mineur/patch), build number auto (CI 1593), changelog public (patch notes joueur lisibles, 1579), branches Steam (beta/par défaut 1581), downgrade possible (branche 'previous'), compatibilité des saves (migration 1503). Utilise pour tout jeu en live ops (1542). N'utilise pas pour un prototype."
mot_cle: "versioning builds SemVer 1.2.3 changelog patch notes branches Steam beta"
nom_court: "Versioning"
branche: "D21"
synonymes: ["SemVer 1.2.3 : quoi en majeur mineur patch ?", "patch notes publiques lisibles par les joueurs", "branche beta Steam pour tester avant prod (1581)"]
cross_refs: [303, 1581, 1503]
tags: ["2027"]
depends_on: [303]
---

## 1578. 📅 Versioning des builds et changelog joueur (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Versionner un jeu en 2027 : SemVer (majeur = rupture save/compat, mineur = contenu, patch = bug), build auto en CI (1593), changelog public (patch notes lisibles), branches Steam (beta 1581), migration des saves (1503), branche 'previous' pour downgrade.

**Quand l'utiliser (triggers)** :
- C'est la v1.2 ou v2.0 si on casse les saves ?
- Patch notes publiques : 3-5 lignes lisibles
- Branche beta Steam avant de pousser en prod

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es release manager jeu. Tu appliques SemVer + build number CI, tu rédiges le changelog public (CHANGELOG.md + in-game 'Nouveautés' 1542), branches Steam (default/beta/previous 1581), et la règle : une version majeure = migration de save testée (1503). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La version actuelle (ex. 1.2.3)
- Le type de changement (bug/contenu/rupture)
- Les branches Steam (1581) et le changelog

**Méthode** :
1. SemVer : MAJEUR si rupture (save incompatible, moteur changé), MINEUR si nouveau contenu (niveau, perso), PATCH si bugfix. Build auto = numéro de commit CI (1593).
2. CHANGELOG.md (Keep a Changelog) + patch notes in-game (1542) : 3-5 puces lisibles ('Nouveau donjon', 'Fix crash boss').
3. Steam (1581) : branches 'default' (prod), 'beta' (testeurs), 'previous' (downgrade si la maj casse).
4. Saves : chaque version majeure migre les saves (1503) et est testée (rollback possible via branche previous).
5. Communication : annonce Discord/mail 48 h avant une maj majeure.

**Sorties attendues** :
- Le versioning SemVer + build CI appliqué
- Le changelog public + notes in-game
- Les branches Steam beta/previous configurées

**Exemple de prompt** :
> « On sort la v1.3 : applique SemVer (patch notes 5 lignes lisibles in-game, CHANGELOG.md, branche beta Steam testée 1 semaine avant prod, branche previous pour rollback, migration save 1503 si besoin). »

**Cas d'usage** : Live ops (1542), communication joueurs. S'articule avec skills 303 (SemVer code), 1581 (Steam) et 1503 (saves).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

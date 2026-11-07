---
num: 1591
date_ajout: "2026-11"
nom: "Tests automatises de gameplay (playmode tests)"
emoji: "🧪"
domaine: "Game Dev"
signal: "Automatiser les tests d'un jeu en 2027 : playmode tests (Unity Test Framework / Godot GUT) qui lancent une scène, simulent des inputs (1504), vérifient (PV après dégâts 1508, save/load 1503, quête 1531), en CI (1593) à chaque PR; tests unitaires sur la logique pure (économie 1529, formules dégâts). Utilise pour éviter les régressions. N'utilise pas pour le game feel (test humain)."
mot_cle: "tests automatisés gameplay playmode Unity Test Framework CI régressions"
nom_court: "Tests auto"
branche: "D1"
synonymes: ["playmode test : simuler un tir et vérifier les PV (1508)", "test save/load (1503) : round-trip identique", "CI qui fait tourner les tests à chaque PR (1593)"]
cross_refs: [67, 302, 1593]
tags: ["2027"]
depends_on: [302]
---

## 1591. 🧪 Tests automatises de gameplay (playmode tests, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser les tests d'un jeu en 2027 : tests unitaires sur la logique pure (formules dégâts 1535, économie 1529) + playmode tests (scène lancée, inputs simulés 1504, assertions sur PV/save/quêtes), exécutés en CI (1593) à chaque PR.

**Quand l'utiliser (triggers)** :
- Un patch casse la sauvegarde (1503), personne ne teste
- Playmode test : tirer sur une cible, vérifier -20 PV (1508)
- CI verte = tous les tests passent (1593)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es QA engineer jeu. Tu sépare : tests unitaires (logique pure, rapides, 1000+/s) et playmode (scènes réelles, lent, mais couvre l'intégration : input 1504 → physique 1509 → hitbox 1508 → PV). CI (1593) : tests unitaires à chaque commit, playmode nightly. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La logique à tester (dégâts, économie 1529, saves 1503, quêtes 1531)
- Unity Test Framework / GUT / custom
- La CI (1593)

**Méthode** :
1. Tests unitaires : formules pures (dégâts arme 1535 * rareté 1528, courbe XP 1530, loot 1528) → assert égalité exacte.
2. Playmode : [UnityTest] charge une scène test, simule input (InputSystem actions 1504), avance le temps (yield WaitForFixedUpdate 1501), assert (PV cible == 80 après 1 tir, save round-trip 1503 identique).
3. CI (1593) : tests unitaires à chaque commit (rapide), playmode nightly + avant release (branche 1578).
4. Couverture : viser 80 % sur la logique métier (pas le rendu).
5. Flake : un test qui échoue aléatoirement est supprimé ou fiabilisé (timeout, seed fixe 1513).

**Sorties attendues** :
- La suite de tests (unitaires + playmode) fonctionnelle
- La CI qui bloque la PR si test rouge (1593)
- La couverture de la logique métier mesurée

**Exemple de prompt** :
> « Ajoute des tests auto au jeu : unitaires (dégâts 1535, XP 1530, loot 1528) + playmode (tir → PV -20 via 1508, save/load round-trip 1503), CI bloque la PR si rouge (1593). »

**Cas d'usage** : Qualité continue, release sereine. S'articule avec skills 67 (tests unitaires), 302 (TDD) et 1593 (CI).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

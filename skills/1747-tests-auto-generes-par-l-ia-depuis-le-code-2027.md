---
num: 1747
date_ajout: "2026-11"
nom: "Tests auto generes par l'IA depuis le code (2027)"
emoji: "🧪"
domaine: "Développement"
signal: "Générer les tests unitaires/intégration en 2027 avec l'IA depuis le code (doc-to-test 822 existe — angle 2027 : couverture ciblée) : viser les chemins critiques (happy path + erreurs + limites 310), mocker les dépendances externes (BDD/API 254), atteindre 80 % de couverture sur le nouveau code, revue humaine (1401) + mutation testing (mutmut/stryker) pour vérifier que les tests testent vraiment. N'utilise pas sans revue (tests IA peuvent être creux)."
mot_cle: "tests auto IA 2027 couverture 80% chemins critiques mock dépendances mutation testing mutmut stryker revue 1401"
nom_court: "Tests auto IA"
branche: "D12"
synonymes: ["générer les tests d'un module (IA) puis mutation testing pour vérifier qu'ils testent vraiment", "couverture 80% sur le nouveau code (CI 1658 bloque sinon)", "mocker la BDD et l'API externe (254) dans les tests générés"]
cross_refs: [67, 822, 310]
tags: ["2027"]
depends_on: [822]
---

## 1747. 🧪 Tests auto generes par l'IA depuis le code (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Générer des tests utiles en 2027 avec l'IA : couvrir les chemins critiques (happy + erreurs + limites 310) à 80 % sur le nouveau code, mocker les dépendances (254), vérifier par mutation testing (mutmut/Stryker) + revue humaine (1401).

**Quand l'utiliser (triggers)** :
- ce nouveau module n'a aucun test, l'IA en génère (puis mutation testing)
- couverture 80% sur le diff en CI (1658 bloque sinon)
- les tests générés passent mais testent rien (mutation testing le montre)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev / QA. Tu fais générer les tests par l'agent (Cursor 1740 / Copilot 1741) sur le module, tu demandes explicitement : happy path, erreurs, cas limites (310), mocks (254), assertions précises ; puis mutation testing + revue (1401). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le code à tester (module/fonction)
- L'agent IA (1735)
- La CI (1658) + mutation testing

**Méthode** :
1. Prompt : 'génère les tests unitaires de ce module : happy path, chaque erreur, cas limites (null, vide, max 310), mocks des dépendances externes (BDD/API 254), assertions fortes' (pas juste 'ça marche').
2. Appliquer, lancer les tests (67) — doivent passer.
3. Mutation testing (mutmut Python / Stryker JS) : tue les mutants ; si un mutant survit, le test est creux → le renforcer.
4. Couverture : viser 80 % sur le nouveau code (pas l'ancien), check CI (1658) bloque la PR sinon.
5. Revue humaine (1401) : les tests couvrent-ils VRAIMENT la logique métier ? (l'IA fait parfois des tests qui passent toujours).
6. Intégration : tests E2E (252) sur les parcours critiques, pas que des unitaires.

**Sorties attendues** :
- Les tests générés + passés (67), couverture 80% sur le nouveau code (CI 1658)
- Le rapport de mutation testing (mutants tués vs survivants → tests renforcés)
- La revue humaine (1401) documentée

**Exemple de prompt** :
> « Module de paiement sans tests : l'IA (Cursor 1740) génère les tests (happy + CB refusée + timeout + cas limites 310, mock PSP 254), coverage 80% check CI (1658), mutation testing (Stryker) tue les mutants → tests solides, relus (1401). »

**Cas d'usage** : Qualité du code nouveau. S'articule avec skills 67 (tests), 822 (doc-to-test), 310 (cas limites), 254 (mocks), 1658 (CI), 1401 (revue).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

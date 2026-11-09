---
num: 252
resume: "écrire des scénarios de tests end-to-end pilotant une application web dans un vrai navigateur (Playwright), reproductibles en CI. Étape 1 : Identifier les parcours critiques de l'application et leurs critères de succès."
lang: "fr"
date_ajout: "2026-11"
nom: "Testeur E2E navigateur"
emoji: "🖱️"
domaine: "Développement"
signal: "Test E2E navigateur, scénario Playwright"
mot_cle: "testeur e2e navigateur"
nom_court: "E2E"
branche: "D16"
synonymes: []
cross_refs: [82, 178, 803]
depends_on: [803]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : écrire des scénarios de tests end-to-end pilotant une application web dans un vrai navigateur (Playwright), reproductibles en CI.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « testeur e2e navigateur ».
- Mots-clés du signal : Test E2E navigateur, scénario Playwright
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es ingénieur tests E2E. Tu traduis des parcours utilisateurs en scénarios Playwright : sélecteurs stables (data-testid plutôt que classes générées), assertions explicites, attentes conditionnelles plutôt que timeouts figés. Tu couvres d'abord les parcours critiques puis les cas limites, et chaque test reste indépendant des autres.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Identifier les parcours critiques de l'application et leurs critères de succès.
2. Écrire les scénarios Playwright avec sélecteurs robustes et assertions métier.
3. Exécuter, corriger la flakiness et documenter la commande de lancement en CI.

**Sorties attendues** :
- Le livrable attendu pour « Testeur E2E navigateur », structuré et vérifié.

**Exemple de prompt** :
> « Écris un scénario Playwright pour ma boutique : recherche de "lampe de bureau", ajout au panier, checkout avec l'email test@example.com, vérification de la page de confirmation. »

**Cas d'usage** : sécuriser un flux de paiement, tester une refonte avant mise en production, non-régression en CI. S'articule avec les skills 178 (plan de tests fonctionnels) et 82 (déploiement CI/CD).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---


---
num: 1414
nom: "Tests de contrat consommateur (Pact, 2027)"
emoji: "🤝"
domaine: "Développement"
signal: "Écrire des tests de contrat (consumer-driven contracts) avec Pact en 2027 : le consommateur décrit ses attentes, le provider les valide en CI, évitant les ruptures d'API entre microservices. Utilise quand plusieurs services communiquent par API. N'utilise pas pour les tests internes."
mot_cle: "tests de contrat pact consumer driven API"
nom_court: "Tests Pact"
branche: "D12"
synonymes: ["consumer contract testing", "pact tests API microservices", "éviter rupture API entre services"]
cross_refs: [604, 526, 87]
tags: ["2027"]
depends_on: [604]
---

## 1414. 🤝 Tests de contrat consommateur (Pact, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en place des tests de contrat Pact en 2027 entre consommateur et provider d'API : le consumer publie ses attentes, le provider les vérifie en CI avant chaque déploiement.

**Quand l'utiliser (triggers)** :
- Nos microservices cassent l'API sans prévenir
- Mettre en place Pact consumer/provider
- Vérifier un contrat d'API en CI (can-i-deploy)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de contrats d'API. Tu décris le flow Pact (consumer écrit le pact → broker → provider vérifie en CI), et tu précises : ça complète les tests d'intégration, ne les remplace pas. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les services consumer et provider
- Le broker Pact (self-hosted ou PactFlow)
- L'API concernée (endpoints, formats)

**Méthode** :
1. Côté consumer : écrire le test Pact (interaction attendue, réponse 200 + schéma).
2. Publier le pact au broker (CI du consumer).
3. Côté provider : vérifier tous les pacts en CI (can-i-deploy).
4. En cas d'échec : corriger l'API ou notifier le consumer (versioning).
5. Garder le broker à jour (versions, tag prod).

**Sorties attendues** :
- Les pacts écrits et publiés
- La vérification provider en CI
- Le contrat d'API versionné

**Exemple de prompt** :
> « Notre front casse l'API paiement sans prévenir : mets en place des tests de contrat Pact (consumer publie, provider vérifie en CI). »

**Cas d'usage** : Microservices, équipes indépendantes, déploiements fréquents. S'articule avec skills 604 (contrats d'API), 526 (design API) et 87 (OpenAPI).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

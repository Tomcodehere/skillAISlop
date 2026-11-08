---
num: 1886
date_ajout: "2026-11"
nom: "OpenAPI 3.2 / AsyncAPI : spec-first pour les API"
emoji: "📄"
domaine: "Développement"
signal: "Définir les API en spec-first avec OpenAPI 3.2 (HTTP sync) / AsyncAPI (event-driven, Kafka 1866) : un fichier YAML/JSON = contrat (1840), génération de clients/serveurs (openapi-generator), doc interactive (Swagger UI/Redoc), tests de contrat (Pact 1414 côté consommateur), validation en CI (1413). Breaking changes détectés par diff de spec (comme 1840). N'utilise pas de doc écrite à la main (drift garanti)."
mot_cle: "OpenAPI 3.2 AsyncAPI spec-first contrat API génération client serveur Swagger Redoc tests contrat Pact 1414 CI 1413 breaking change diff"
nom_court: "OpenAPI/AsyncAPI"
branche: "D1"
synonymes: ["définir l'API en OpenAPI 3.2 d'abord, générer le code ensuite (spec-first)", "AsyncAPI pour les événements Kafka (1866) : contrat des messages aussi", "breaking change d'API détecté en CI par diff de la spec OpenAPI (1840)"]
cross_refs: [1414, 1413, 1840]
tags: ["2027"]
depends_on: [1414]
---

## 1886. 📄 OpenAPI 3.2 / AsyncAPI : spec-first pour les API

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir les API en spec-first (OpenAPI 3.2 sync, AsyncAPI events) : contrat unique (1840) -> génération de clients/serveurs, doc interactive, tests de contrat (Pact 1414), détection des breaking changes en CI.

**Quand l'utiliser (triggers)** :
- le front et le back divergent sur l'API : écrire la spec OpenAPI d'abord
- générer le client TypeScript depuis l'OpenAPI (openapi-generator)
- AsyncAPI pour documenter les événements Kafka (1866) comme contrat

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur API / architecte. Tu écris la spec (openapi.yaml / asyncapi.yaml) dans le repo, tu génères code + doc, tu valides en CI (lint + diff breaking 1840 + tests Pact 1414). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le contrat API (spec)
- openapi-generator / asyncapi tooling
- La CI (1413) + Pact (1414)

**Méthode** :
1. Rédiger openapi.yaml (paths, schémas, sécurité) — source de vérité unique (1840).
2. Générer : serveur (stubs) + client (TS/Python) + doc (Redoc) depuis la spec.
3. CI 1413 : lint de la spec (spectral), diff vs main (breaking = fail 1840), tests Pact consommateur (1414).
4. AsyncAPI pour les events Kafka (1866) : schéma des messages versionné aussi.

**Sorties attendues** :
- La spec OpenAPI/AsyncAPI versionnée (source de vérité)
- Le code client/serveur + doc générés
- Le CI qui bloque les breaking changes (1840) + tests Pact 1414

**Exemple de prompt** :
> « API orders : openapi.yaml v2.1.0 ajoute champ optionnel (compatible) -> CI vert ; v3.0.0 supprime un champ -> diff breaking détecté (1840) -> CI rouge, revue obligatoire avant merge. »

**Cas d'usage** : API fiables. S'articule avec skills 1414, 1413, 1840, 1406, 1866.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

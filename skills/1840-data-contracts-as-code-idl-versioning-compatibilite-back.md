---
num: 1840
resume: "Gérer les data contracts as code : IDL (Protobuf/Avro/Smithy/dbt schema.yml), versioning sémantique, compatibilité backward validée en CI (breaking change = v3 majeur). Étape 1 : Choisir l'IDL : Protobuf (perf, binaire), Avro (schema evolutif natif), Smithy/OpenDataMesh (data contracts), dbt schema.yml (tables)."
lang: "fr"
date_ajout: "2026-11"
nom: "Data contracts as code : IDL, versioning, compatibilité backward"
emoji: "🧬"
domaine: "Développement"
signal: "Gérer les data contracts comme du code : définis dans un IDL (Protobuf, Avro, Smithy, OpenDataMesh, ou schema.yml dbt 1834), versionnés (v1, v2), avec règle de compatibilité backward (ajout de champ optionnel OK, suppression/changement de type = v3 majeur + migration). CI valide la compatibilité à chaque PR (1413). N'utilise pas de contrat non versionné ou de breaking change sans major."
mot_cle: "data contracts as code IDL Protobuf Avro Smithy OpenDataMesh versioning sémantique compatibilité backward breaking change CI"
nom_court: "Contracts as code"
branche: "D12"
synonymes: ["définir les data contracts dans un IDL (Protobuf/Avro/Smithy/dbt schema.yml) versionné", "compatibilité backward : ajout optionnel OK, suppression = v3 majeur", "CI valide la compatibilité du contrat à chaque PR (breaking change détecté)"]
cross_refs: [1831, 1834, 1413]
tags: ["2027"]
depends_on: [1831]
---

## 1840. 🧬 Data contracts as code : IDL, versioning, compatibilité backward

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gérer les data contracts as code : IDL (Protobuf/Avro/Smithy/dbt schema.yml), versioning sémantique, compatibilité backward validée en CI (breaking change = v3 majeur).

**Quand l'utiliser (triggers)** :
- changer un champ de type : c'est un breaking change -> v3 majeur
- valider en CI que le contrat v2 reste compatible avec v1
- IDL : Protobuf vs Avro vs Smithy pour nos contrats data

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte data / dev. Tu mets les contrats dans un repo dédié (IDL), tu versionnes (semver), et tu ajoutes un check CI (1413) qui compare v1 vs v2 et bloque si breaking sans bump majeur. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo de contrats (IDL)
- La CI (1413)
- Les consommateurs (1831)

**Méthode** :
1. Choisir l'IDL : Protobuf (perf, binaire), Avro (schema evolutif natif), Smithy/OpenDataMesh (data contracts), dbt schema.yml (tables).
2. Versionner : v1.0.0 -> ajout champ optionnel = v1.1.0 ; suppression/changement type = breaking -> v2.0.0 majeur.
3. CI : comparer les deux versions (buf breaking pour Protobuf, outil custom sinon), bloquer le merge si breaking sans bump majeur.
4. Publier le contrat (catalog 1095/1836) + notifier les consommateurs (1831).

**Sorties attendues** :
- Les contrats IDL versionnés (semver) dans un repo dédié
- Le check CI de compatibilité backward actif
- Les consommateurs notifiés des changements

**Exemple de prompt** :
> « Contrat orders.proto v1.2.0 ajoute champ optionnel discount_code (compatible, v1.3.0) ; v2.0.0 renomme amount en total_amount (breaking, notifié) — CI bloque le merge v2 sans bump majeur. »

**Cas d'usage** : Contrats data fiables. S'articule avec skills 1831, 1834, 1413, 1884.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

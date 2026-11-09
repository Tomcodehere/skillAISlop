---
num: 1836
resume: "Choisir son métacatalog : Marquez (lineage OpenLineage, léger) pour la technique ; OpenMetadata ou DataHub pour la gouvernance métier (glossaire, owners, PII) — Amundsen étant archivé. Étape 1 : Lineage technique : Marquez + OpenLineage (1832/1833) — standard, léger."
date_ajout: "2026-11"
nom: "Choisir son métacatalog : DataHub vs OpenMetadata vs Marquez"
emoji: "🗺️"
domaine: "Data"
signal: "Choisir l'outil de catalogage/lineage en 2027 : Marquez (1833) = backend OpenLineage pur (léger, standard ouvert) ; DataHub (LinkedIn, acq. 2023) = riche (glossaire, ownership, qualité, recherche) mais modèle propriétaire ; OpenMetadata = riche aussi (open source, lineage + qualité + gouvernance, Rembrandt UI), Amundsen archivé (sept. 2026). Règle : lineage technique = OpenLineage+Marquez ; gouvernance métier (glossaire, owners, PII) = OpenMetadata ou DataHub."
mot_cle: "choisir métacatalog DataHub OpenMetadata Marquez Amundsen archivé glossaire ownership gouvernance PII lineage"
nom_court: "Métacatalog"
branche: "D17"
synonymes: ["DataHub vs OpenMetadata vs Marquez : lequel pour le catalogage data", "Amundsen archivé sept 2026 : migrer vers quoi", "lineage technique (Marquez/OpenLineage) vs gouvernance métier (OpenMetadata/DataHub)"]
cross_refs: [1832, 1833, 1095]
tags: ["2027"]
depends_on: [1833]
---

## 1836. 🗺️ Choisir son métacatalog : DataHub vs OpenMetadata vs Marquez

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir son métacatalog : Marquez (lineage OpenLineage, léger) pour la technique ; OpenMetadata ou DataHub pour la gouvernance métier (glossaire, owners, PII) — Amundsen étant archivé.

**Quand l'utiliser (triggers)** :
- on a Amundsen (archivé) : migrer vers OpenMetadata ou DataHub
- catalog avec glossaire métier + owners + tags PII
- lineage pur sans gouvernance : Marquez suffit

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte data / plateforme. Tu sépares les deux besoins : lineage technique (OpenLineage+Marquez 1832/1833, standard) et gouvernance métier (OpenMetadata : glossaire, owners, classification PII 1839, qualité 1835). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les besoins (lineage vs gouvernance)
- L'existant (Amundsen à migrer ?)
- Les consommateurs (métier vs tech)

**Méthode** :
1. Lineage technique : Marquez + OpenLineage (1832/1833) — standard, léger.
2. Gouvernance : OpenMetadata (open source, glossaire + owners + tags PII + qualité + profilage) ou DataHub (si écosystème LinkedIn/DataHub déjà là).
3. Migration Amundsen (archivé) : exporter les métadonnées, réimporter dans OpenMetadata.
4. Compléter par le catalogue existant 1095 (Data Catalog & Lineage).

**Sorties attendues** :
- L'architecture cible documentée (lineage + gouvernance)
- La migration Amundsen faite si besoin
- Les deux outils déployés et connectés

**Exemple de prompt** :
> « Architecture data 2027 : Marquez pour le lineage colonne (1833) + OpenMetadata pour le glossaire métier (définition 'revenu net', owner, PII sur email) + qualité (1835) — les deux alimentés par OpenLineage. »

**Cas d'usage** : Choisir les bons outils data. S'articule avec skills 1832, 1833, 1095, 1839.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

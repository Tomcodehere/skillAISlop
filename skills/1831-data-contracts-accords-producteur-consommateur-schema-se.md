---
num: 1831
resume: "Rédiger et versionner des data contracts (schéma, sémantique métier, SLA de fraîcheur/volume, gouvernance) entre producteurs et consommateurs, avec enforcement au pipeline (dbt/GX/Soda). Étape 1 : Définir le contrat : schéma (colonnes, types, nullabilité, clés), sémantique (définition métier de chaque champ), SLA (fraîcheur, complétude, dispo), gouvernance (owner, rétention, PII)."
lang: "fr"
date_ajout: "2026-11"
nom: "Data contracts : accords producteur-consommateur (schéma, sémantique, SLA)"
emoji: "📝"
domaine: "Data"
signal: "Rédiger des data contracts entre producteurs et consommateurs de données : schéma (types, nullabilité), sémantique (définitions métier), SLA (fraîcheur, volume, disponibilité), gouvernance (propriétaire, rétention, PII). Enforcement au pipeline (dbt tests, Great Expectations, Soda) + lisible par les agents IA (MCP dbt 1765). 70 % des orgs adoptent la data quality moderne d'ici là (Gartner). N'utilise pas un contrat non versionné (il casse les consommateurs silencieusement)."
mot_cle: "data contract producteur consommateur schéma sémantique SLA fraîcheur enforcement dbt Great Expectations Soda versionné"
nom_court: "Data contracts"
branche: "D15"
synonymes: ["rédiger un data contract : schéma + sémantique + SLA entre producteur et consommateur", "enforcement du contrat au pipeline (dbt tests, GX, Soda) : violation = blocage", "contrat lisible par les agents IA (MCP dbt) pour éviter les hallucinations de sens"]
cross_refs: [1095, 1834, 1835]
tags: ["2027"]
depends_on: [1095]
---

## 1831. 📝 Data contracts : accords producteur-consommateur (schéma, sémantique, SLA)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rédiger et versionner des data contracts (schéma, sémantique métier, SLA de fraîcheur/volume, gouvernance) entre producteurs et consommateurs, avec enforcement au pipeline (dbt/GX/Soda).

**Quand l'utiliser (triggers)** :
- le dashboard revenue a chuté de 11 % : un producteur a changé le schéma sans prévenir
- définir le SLA de fraîcheur d'une table critique (alert si retard > 1 h)
- contrat exposé aux agents IA via MCP pour éviter les mauvaises interprétations

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data product owner / architecte data. Tu écris le contrat en YAML (schema.yml dbt ou format ouvert), tu versionnes (v1, v2 avec compatibilité backward 1840), et tu branches l'enforcement (violation = pipeline fail + alerte propriétaire). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le producteur et le consommateur
- Le schéma actuel
- Les SLA métier (fraîcheur, volume)

**Méthode** :
1. Définir le contrat : schéma (colonnes, types, nullabilité, clés), sémantique (définition métier de chaque champ), SLA (fraîcheur, complétude, dispo), gouvernance (owner, rétention, PII).
2. Versionner : contrat v1 -> v2 avec règle de compatibilité backward (1840).
3. Enforcer : dbt tests/GX/Soda à chaque run (1834/1835) — violation = fail + alerte (1761).
4. Exposer aux agents IA via MCP (1765) pour le grounding sémantique.

**Sorties attendues** :
- Le contrat versionné (YAML) publié
- L'enforcement actif (violation = blocage + alerte)
- Le contrat exposé aux agents (MCP)

**Exemple de prompt** :
> « Table f_orders : contrat v2 ajoute colonne discount_code (nullable, sémantique 'code promo appliqué, % du total') + SLA fraîcheur 1 h — dbt test échoue si colonne manquante ou fraîcheur > 1 h, alerte owner data. »

**Cas d'usage** : Fiabiliser les pipelines. S'articule avec skills 1095 (catalog), 1834 (dbt), 1835 (SLA), 1765 (MCP), 1840 (as code).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

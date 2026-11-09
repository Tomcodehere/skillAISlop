---
num: 1837
resume: "Organiser le data en mesh : chaque domaine métier possède ses data products (contrat 1831, SLA 1835, catalogués 1836, self-serve via la plateforme 1700), avec gouvernance fédérée (PII, standards). Étape 1 : Identifier les domaines (marketing, ventes, produit...) et leurs data products (ex. 'clients segmentés')."
date_ajout: "2026-11"
nom: "Data mesh : domaines propriétaires et data products"
emoji: "🕵️"
domaine: "Stratégie"
signal: "Passer au data mesh (Zhamak Dehghani) quand le modèle centralisé data team bottleneck : domaines métier propriétaires de leurs données, exposées comme des data products (contrat 1831, SLA 1835, discoverable via catalog 1836, self-serve infra platform), fédération de gouvernance (PII, standards). Pas pour inférieur à 20 personnes data ou un seul domaine. N'utilise pas sans plateforme self-serve (sinon ça crée du chaos, pas de la fédération)."
mot_cle: "data mesh domaines propriétaires data products self-serve fédération gouvernance Zhamak Dehghani plateforme"
nom_court: "Data mesh"
branche: "D26"
synonymes: ["passer au data mesh : domaines métier propriétaires de leurs data products", "data product : contrat 1831 + SLA 1835 + discoverable (catalog 1836) + self-serve", "ne pas faire de data mesh sans plateforme self-serve (risque de chaos)"]
cross_refs: [1831, 1835, 1836]
tags: ["2027"]
depends_on: [1831]
---

## 1837. 🕵️ Data mesh : domaines propriétaires et data products

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Organiser le data en mesh : chaque domaine métier possède ses data products (contrat 1831, SLA 1835, catalogués 1836, self-serve via la plateforme 1700), avec gouvernance fédérée (PII, standards).

**Quand l'utiliser (triggers)** :
- la data team centrale est un bottleneck (toutes les demandes passent par elle)
- domaine marketing veut exposer ses données en self-serve
- définir un data product : contrat + SLA + doc + owner

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte data / DSI. Tu découpes par domaines métier (bounded contexts), chaque domaine publie ses data products avec contrat/SLA/catalog, et la plateforme (1700) fournit le self-serve (infra, qualité 1835, catalog 1836). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les domaines métier (bounded contexts)
- La plateforme self-serve (1700)
- Les standards fédérés (PII 1839, contrats 1831)

**Méthode** :
1. Identifier les domaines (marketing, ventes, produit...) et leurs data products (ex. 'clients segmentés').
2. Chaque data product : contrat (1831), SLA (1835), doc, owner, publié dans le catalog (1836).
3. Plateforme self-serve : ingestion, stockage, qualité (1835), accès (1839) en 1 commande (golden path 1701).
4. Gouvernance fédérée : standards communs (PII, formats), pas de centralisation des données.

**Sorties attendues** :
- Les domaines et leurs data products documentés
- La plateforme self-serve opérationnelle
- La gouvernance fédérée (standards PII) en place

**Exemple de prompt** :
> « Domaine marketing publie le data product 'audiences_qualifiées' : contrat v1 (schéma+sémantique), SLA fraîcheur 1 h, catalogué (1836), consommable en self-serve par le domaine ventes — la data team centrale n'est plus dans le loop. »

**Cas d'usage** : Scale data > 20 personnes. S'articule avec skills 1831, 1835, 1836, 1700, 1095.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

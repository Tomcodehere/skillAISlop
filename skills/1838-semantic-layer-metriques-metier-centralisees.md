---
num: 1838
resume: "Centraliser les définitions des métriques métier dans une semantic layer (dbt Semantic Layer/LookML/Cube) : une seule définition par métrique, consommée par la BI, les notebooks et les agents IA (MCP 1765). Étape 1 : Lister les métriques critiques (revenu, marge, churn...) et UNE définition validée par le métier."
lang: "fr"
date_ajout: "2026-11"
nom: "Semantic layer : métriques métier centralisées"
emoji: "📐"
domaine: "Data"
signal: "Centraliser les définitions métier des métriques dans une semantic layer (dbt Semantic Layer, LookML, Cube, Metabase models) pour que 'revenu net' ait UNE définition partout (BI, notebooks, agents IA) — fini les 5 chiffres différents selon l'outil. La couche sémantique traduit la métrique en SQL sur le warehouse. Les agents IA la consomment via MCP (1765) pour répondre juste. N'utilise pas si les définitions métier ne sont pas validées (garbage in)."
mot_cle: "semantic layer métriques métier définition unique dbt Semantic Layer LookML Cube Metabase agents IA MCP SQL warehouse"
nom_court: "Semantic layer"
branche: "D15"
synonymes: ["une seule définition de 'revenu net' partout (semantic layer dbt/LookML/Cube)", "les agents IA consomment les métriques via MCP (1765) : définition sémantique fiable", "éviter 5 chiffres différents pour la même métrique selon l'outil BI"]
cross_refs: [1834, 1765, 1831]
tags: ["2027"]
depends_on: [1834]
---

## 1838. 📐 Semantic layer : métriques métier centralisées

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Centraliser les définitions des métriques métier dans une semantic layer (dbt Semantic Layer/LookML/Cube) : une seule définition par métrique, consommée par la BI, les notebooks et les agents IA (MCP 1765).

**Quand l'utiliser (triggers)** :
- le CFO et le CEO ont des chiffres de revenu différents : définir 'revenu net' une fois
- exposer les métriques aux agents IA via MCP (1765)
- dbt Semantic Layer vs LookML vs Cube : lequel

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analytics engineer / data product. Tu définis chaque métrique métier (nom, définition, formule SQL, dimensions, filtres) dans la semantic layer, tu la testes (1834), et tu l'exposes via MCP pour les agents (1765). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les définitions métier validées
- La semantic layer choisie
- Les consommateurs (BI, IA)

**Méthode** :
1. Lister les métriques critiques (revenu, marge, churn...) et UNE définition validée par le métier.
2. Les modéliser dans la semantic layer (dbt metrics/semantic models, LookML, ou Cube).
3. Tester : la métrique = somme des faits (réconciliation 1834).
4. Exposer : API sémantique + MCP (1765) pour les agents IA ; dashboards 1766 branchés dessus.

**Sorties attendues** :
- Les métriques métier centralisées et testées
- L'API/MCP sémantique pour BI + agents IA
- Le dashboard 1766 sur la même définition

**Exemple de prompt** :
> « 'Revenu net' défini dans dbt Semantic Layer (CA - remises - taxes, filtre statut=payé) : le dashboard CFO (1766), le notebook data et l'agent IA (MCP 1765) retournent tous 4,2 M€ — un seul chiffre. »

**Cas d'usage** : Une vérité métier unique. S'articule avec skills 1834, 1765, 1831, 1766.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

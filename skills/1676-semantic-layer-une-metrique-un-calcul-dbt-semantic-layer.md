---
num: 1676
resume: "Construire une semantic layer en 2027 (dbt Semantic Layer 350 ou Cube) : chaque métrique métier (CA, marge, churn 344) définie UNE fois en YAML/SQL versionné Git, consommée identiquement par tous les BI (Superset 1666, Excel 264, dashboards 107). Étape 1 : Lister les métriques contestées (CA, marge, churn, NPS 797) et leur définition 'officielle' (avec le métier 344)."
date_ajout: "2026-11"
nom: "Semantic layer : une metrique, un calcul (dbt Semantic Layer, Cube)"
emoji: "📐"
domaine: "Data"
signal: "Construire une semantic layer en 2027 (dbt Semantic Layer ou Cube) : définir UNE fois chaque métrique métier (CA, marge, churn 344) avec sa logique, et tous les outils BI (Superset 1666, Excel 264, dashboards 107) la consomment identiquement — fini les 3 définitions du CA. Utilise quand plusieurs équipes/BI divergent sur les métriques. N'utilise pas pour une seule équipe."
mot_cle: "semantic layer 2027 dbt semantic layer cube une métrique un calcul BI cohérent"
nom_court: "Semantic layer"
branche: "D17"
synonymes: ["3 définitions du CA selon l'équipe, semantic layer pour unifier", "dbt Semantic Layer : métriques versionnées Git (350)", "Cube : semantic layer open source avec API metrics"]
cross_refs: [344, 36, 350]
tags: ["2027"]
depends_on: [344]
---

## 1676. 📐 Semantic layer 2027 : une metrique, un calcul (dbt Semantic Layer, Cube) (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire une semantic layer en 2027 (dbt Semantic Layer 350 ou Cube) : chaque métrique métier (CA, marge, churn 344) définie UNE fois en YAML/SQL versionné Git, consommée identiquement par tous les BI (Superset 1666, Excel 264, dashboards 107).

**Quand l'utiliser (triggers)** :
- le CA du marketing et celui de la finance diffèrent de 10 %
- une seule définition du churn (344) pour tout le monde
- dbt Semantic Layer vs Cube choisir 2027

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analytics engineer. Tu définis les métriques dans le semantic layer (dimensions, mesures, filtres, calculs dérivés), versionné Git, exposé via API metrics, consommé par les BI — et tu interdis les définitions locales. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les métriques métier qui divergent (CA, churn, panier moyen)
- Les outils BI consommateurs (Superset 1666, Excel, Looker)
- Le modèle de données (dbt 350)

**Méthode** :
1. Lister les métriques contestées (CA, marge, churn, NPS 797) et leur définition 'officielle' (avec le métier 344).
2. dbt Semantic Layer : metrics YAML (type: simple/ratio/derived, sql, dimensions, filtres), versionné Git, servi via API.
3. Cube : modèle YAML similaire, API metrics + dashboards intégrés.
4. Connecter les BI (Superset 1666, Excel 264 via connecteur, Looker) à la semantic layer — plus de calcul local.
5. Gouvernance : revue des métriques chaque trimestre avec les métiers (qui peut modifier).

**Sorties attendues** :
- La semantic layer avec les métriques officielles versionnées
- Tous les BI connectés à la même définition (plus de divergence CA)
- La gouvernance des métriques (revue trimestrielle)

**Exemple de prompt** :
> « Marketing et finance ont deux CA différents (10 % d'écart) : semantic layer (dbt 350 ou Cube) — une définition du CA en YAML versionné Git, Superset (1666) + Excel (264) + dashboards (107) la consomment tous pareil. »

**Cas d'usage** : Plusieurs équipes/BI sur les mêmes données. S'articule avec skills 344 (définitions métriques), 36 (KPI), 350 (dbt) et 107 (dashboards).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1420
resume: "Réaliser des analytics avancés directement en SQL en 2027 avec les fonctions fenêtres (ROW_NUMBER, RANK, LAG, SUM OVER, PARTITION BY) : cumuls, classements, deltas sans exporter les données. Étape 1 : Formuler le besoin ligne à ligne (cumul, rang, delta)."
date_ajout: "2026-11"
nom: "SQL avance : fonctions fenetres (window functions)"
emoji: "🪟"
domaine: "Développement"
signal: "Utiliser les fonctions fenêtres SQL en 2027 (ROW_NUMBER, RANK, LAG, SUM OVER, PARTITION BY) pour des analytics directement en SQL, sans exporter les données. Utilise pour cumuls, classements, deltas ligne à ligne. N'utilise pas pour un simple GROUP BY."
mot_cle: "sql window functions partition by row_number lag"
nom_court: "Window functions"
branche: "D15"
synonymes: ["partition by sql", "row_number rank sql", "lag lead sql"]
cross_refs: [318, 69, 1277]
tags: ["2027"]
depends_on: [318]
---

## 1420. 🪟 SQL avance : fonctions fenetres (window functions, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Réaliser des analytics avancés directement en SQL en 2027 avec les fonctions fenêtres (ROW_NUMBER, RANK, LAG, SUM OVER, PARTITION BY) : cumuls, classements, deltas sans exporter les données.

**Quand l'utiliser (triggers)** :
- Calculer un cumul par mois en SQL
- Rang des commerciaux par CA
- Delta vs mois précédent avec LAG

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es analyste SQL avancé. Tu expliques OVER (PARTITION BY + ORDER BY + frame), tu donnes 4 exemples concrets (cumul, rank, lag, moyenne mobile) et tu compares au GROUP BY. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La requête métier à calculer
- Le schéma (table de faits)
- Le SGBD (PostgreSQL, BigQuery, MySQL 8+)

**Méthode** :
1. Formuler le besoin ligne à ligne (cumul, rang, delta).
2. Choisir la fonction : ROW_NUMBER/RANK, LAG/LEAD, SUM/AVG OVER.
3. Écrire OVER (PARTITION BY categorie ORDER BY date).
4. Vérifier sur un échantillon.
5. Comparer les perfs vs deux requêtes séparées.

**Sorties attendues** :
- Les requêtes window validées
- L'explication PARTITION BY vs GROUP BY
- Le rapport SQL autonome

**Exemple de prompt** :
> « Donne-moi le CA cumulé par mois et le rang de chaque commercial en SQL (PARTITION BY, ROW_NUMBER, SUM OVER). »

**Cas d'usage** : Dashboards, rapports financiers, analytics produit. S'articule avec skills 318 (SQL lentes), 69 (SQL) et 1277 (SQL analytics).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

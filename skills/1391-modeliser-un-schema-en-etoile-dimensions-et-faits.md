---
num: 1391
date_ajout: "2026-11"
nom: "Modeliser un schema en etoile (dimensions et faits)"
emoji: "⭐"
domaine: "Data"
signal: "Modeliser un entrepot de donnees en schema en etoile en 2027 : une table de faits (mesures numeriques : ventes, clics) entouree de tables de dimensions (date, produit, client, magasin). Alternative au schema en flocon. Utilise quand on construit un data warehouse ou un modele BI. N'utilise pas pour une base operationnelle (OLTP, voir skill 321)."
mot_cle: "schéma en étoile table de faits dimensions"
nom_court: "Schéma en étoile"
branche: "D15"
synonymes: ["modèle en étoile data warehouse", "table de faits et dimensions", "star schema 2027"]
cross_refs: [350, 95, 94]
tags: ["2027"]
depends_on: [350]
---

## 1391. ⭐ Modeliser un schema en etoile (dimensions et faits, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un schéma en étoile pour un data warehouse 2027 : identifier la table de faits (mesures agrégables) et les 4-6 dimensions pertinentes, avec les cles et la granularité.

**Quand l'utiliser (triggers)** :
- Modéliser mon entrepôt de données en schéma en étoile
- Table de faits vs tables de dimensions : c'est quoi la différence ?
- Passer d'une base opérationnelle à un modèle BI en étoile

**Hors périmètre** :
- La base de données opérationnelle OLTP (skill 321)
- Les pipelines ETL eux-mêmes (skill 94)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (les principes de Kimball sont documentés).
- GF-02 : une seule table de faits par processus métier (ventes, livraisons...).
- GF-03 : la granularité de la table de faits doit être declaree (ex. une ligne = une ligne de commande).

**Instructions système** :
Tu es architecte de données specialise modélisation dimensionnelle. Tu identifies le processus métier, la granularité, la table de faits (mesures additives) et les dimensions (qui/quoi/quand/où), tu proposes le schéma et tu restes factuel sur étoile vs flocon. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le processus métier à modéliser (ventes, support, RH...)
- Les besoins des utilisateurs (rapports, filtres)
- Les sources de données existantes

**Méthode** :
1. Choisir le processus métier et la granularité de la table de faits.
2. Lister les mesures numeriques de la table de faits (additives : CA, quantité).
3. Identifier les dimensions (date, produit, client, magasin, canal...).
4. Dessiner le schéma : faits au centre, dimensions autour, cles etrangeres.
5. Valider avec les utilisateurs : le schéma repond-il aux questions fréquentes (ex. CA par produit et par mois) ?

**Sorties attendues** :
- Le schéma en étoile dessiné (faits + dimensions)
- Le dictionnaire des mesures et attributs
- La granularité déclarée et validée

**Exemple de prompt** :
> « Je veux un entrepôt pour analyser mes ventes e-commerce : conçois le schéma en étoile (table de faits vente, dimensions date/produit/client/canal). »

**Cas d'usage** : Construction d'un data warehouse, migration vers un outil BI, rapports direction. S'articule avec skills 350 (dbt), 95 (cartographie de données), 94 (pipelines) et 321 (schémas BDD).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

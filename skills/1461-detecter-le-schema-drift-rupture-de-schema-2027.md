---
num: 1461
date_ajout: "2026-11"
nom: "Detecter le schema drift (rupture de schema, 2027)"
emoji: "💥"
domaine: "Data"
signal: "Détecter automatiquement un schema drift en 2027 (une colonne supprimée/renommée en amont casse le pipeline) : contrats de données (data contracts), monitoring des schémas (Soda, Great Expectations, dbt tests), alertes avant casse en prod. Utilise quand des producteurs changent le schéma sans prévenir. N'utilise pas pour la qualité des valeurs (voir 343)."
mot_cle: "schema drift détection contrat données soda dbt tests"
nom_court: "Schema drift"
branche: "D15"
synonymes: ["colonne supprimée en amont casse mon ETL", "data contracts entre producteurs et consommateurs", "monitoring schéma Soda 2027"]
cross_refs: [1234, 343, 349]
tags: ["2027"]
depends_on: [1234]
---

## 1461. 💥 Detecter le schema drift (rupture de schema, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Détecter le schema drift en 2027 avant qu'il ne casse la prod : data contracts (schéma attendu signé), monitoring automatisé (Soda/dbt tests) avec alerte au producteur et au consommateur.

**Quand l'utiliser (triggers)** :
- Un producteur a supprimé une colonne, tout a cassé
- Mettre des data contracts sur les tables critiques
- Monitorer le schéma avec Soda ou dbt tests

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data steward contrats. Tu définis le data contract (schéma JSON : colonnes, types, nullabilité, sémantique) versionné, le check auto en CI et en prod (Soda/dbt), et l'alerte des deux côtés (producteur et consommateur) avec SLA de correction. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les tables/flux critiques (contrats à protéger)
- Les producteurs et consommateurs
- L'outil (Soda, Great Expectations, dbt tests)

**Méthode** :
1. Rédiger le data contract par source critique (schéma + sémantique + propriétaire).
2. Versionner le contrat dans Git, check auto à chaque livraison du producteur.
3. Monitorer en prod (Soda scan horaire) : alerte si écart (colonne manquante, type changé).
4. Bloquer ou dégrader gracieusement côté consommateur + notifier les 2 côtés.
5. Revoir les contrats à chaque changement majeur (versionning v1 → v2).

**Sorties attendues** :
- Les data contracts des sources critiques
- Le monitoring de schéma actif avec alertes
- La procédure de gestion de changement (v1→v2)

**Exemple de prompt** :
> « Le CRM a renommé un champ et notre BI est cassée depuis 3 jours : mets des data contracts + monitoring schema drift (Soda) avec alerte producteur. »

**Cas d'usage** : Fiabilité data, confiance producteur/consommateur. S'articule avec skills 1234 (contrats producteur-consommateur), 343 (qualité données) et 349 (tests données).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

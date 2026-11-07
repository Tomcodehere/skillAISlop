---
num: 1467
nom: "Reduire sa facture cloud data (BigQuery, Snowflake, 2027)"
emoji: "💸"
domaine: "Data"
signal: "Réduire la facture cloud data en 2027 (BigQuery, Snowflake, Redshift) : partitionnement + clustering des grosses tables, requêtes qui ne scannent que les partitions utiles, cache des résultats, réservation vs on-demand, archivage froid (S3 Glacier), quotas par équipe. Utilise quand la facture data dépasse le budget. N'utilise pas pour l'optimisation applicative (voir 318)."
mot_cle: "réduire facture BigQuery Snowflake partitionnement clustering coût"
nom_court: "FinOps data"
branche: "D17"
synonymes: ["baisser coût requêtes BigQuery", "partitionnement clustering Snowflake", "archivage froid Glacier"]
cross_refs: [1092, 1463, 318]
tags: ["2027"]
depends_on: [1092]
---

## 1467. 💸 Reduire sa facture cloud data (BigQuery, Snowflake, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Réduire la facture cloud data en 2027 (BigQuery/Snowflake) : partitionner + clusteriser les grosses tables, requêtes ciblées (moins de scan), cache, réservations ou on-demand selon le profil, archivage froid, quotas par équipe.

**Quand l'utiliser (triggers)** :
- Notre facture BigQuery a doublé, pourquoi ?
- Partitionner une table de 5 To par date
- Réservation vs on-demand Snowflake

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es FinOps data. Tu analyses la facture (query log : quelles requêtes scannent le plus), tu proposes partitionnement (date) + clustering (user_id), le cache, le choix réservation vs on-demand, et des quotas/budgets par équipe avec alertes. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'historique des requêtes et coûts (query log)
- Les grosses tables et leurs patterns d'accès
- Les besoins de fraîcheur (streaming vs batch)

**Méthode** :
1. Analyser le query log : top 10 requêtes en coût (scan complet de grosses tables ?).
2. Partitionner par date + clusteriser par colonne fréquente (user_id, event_type).
3. Forcer les requêtes à filtrer sur la partition (WHERE date = ...).
4. Activer le cache de résultats (24 h BigQuery) et les réservations/credits selon profil.
5. Archiver le froid (S3 Glacier) et poser des quotas par équipe avec alerte à 80 %.

**Sorties attendues** :
- Le top 10 des requêtes coûteuses et les correctifs
- Les tables partitionnées/clusterisées
- L'économie estimée + quotas par équipe

**Exemple de prompt** :
> « La facture Snowflake a explosé (dashboard qui scanne 5 To/jour) : analyse le query log, partitionne/clusterise, cache, et pose des quotas par équipe. »

**Cas d'usage** : FinOps data, budget, gouvernance des coûts. S'articule avec skills 1092 (FinOps), 1463 (archi) et 318 (SQL).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

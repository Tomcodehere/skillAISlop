---
num: 1787
resume: "Réaliser une montée de version majeure PG (ex. 16→18) avec pg_upgrade --swap (échange atomique des répertoires, downtime de quelques secondes) en conservant les statistiques, sans ANALYZE massif. Étape 1 : Installer les deux versions, lancer pg_upgrade --check (compatibilite)."
date_ajout: "2026-11"
nom: "pg_upgrade --swap : montée majeure sans downtime (PG18)"
emoji: "🔄"
domaine: "Data"
signal: "PG18 améliore pg_upgrade avec --swap : echange atomique des repertoires de données entre l'ancienne et la nouvelle instance (plus de lien dur copie longue), et les statistiques (pg_statistic) sont conservees/transferees automatiquement (plus de ANALYZE massif post-upgrade). Résultat : montée majeure (ex. PG16 vers PG18) en quelques secondes de downtime. N'utilise pas sans le plan de test et rollback (1789)."
mot_cle: "pg_upgrade --swap PG18 echange atomique repertoires statistiques conservees downtime secondes 2027"
nom_court: "pg_upgrade --swap"
branche: "D17"
synonymes: ["montee PG16 vers PG18 en quelques secondes avec pg_upgrade --swap", "les stats pg_statistic sont conservees apres upgrade (plus d'ANALYZE massif)", "--swap echange atomique des repertoires de donnees"]
cross_refs: [1780, 1789, 1758]
tags: ["2027"]
depends_on: [1780]
---

## 1787. 🔄 pg_upgrade --swap : montée majeure sans downtime (PG18)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Réaliser une montée de version majeure PG (ex. 16→18) avec pg_upgrade --swap (échange atomique des répertoires, downtime de quelques secondes) en conservant les statistiques, sans ANALYZE massif.

**Quand l'utiliser (triggers)** :
- montee PG16 vers PG18 : combien de downtime ?
- pg_upgrade --swap + stats conservees, fini l'ANALYZE de 3 h
- rollback prevu si l'upgrade echoue (1789)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DBA. Tu prepares les deux binaires (ancien/nouveau), tu lances pg_upgrade --check puis --swap, tu verifies les stats conservees (pg_statistic) et le downtime mesure, et tu gardes le rollback (ancien cluster intact) selon 1789. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les binaires PG ancien et nouveau installes
- L'ancien cluster (ne pas toucher)
- Le plan de rollback (1789)

**Méthode** :
1. Installer les deux versions, lancer pg_upgrade --check (compatibilite).
2. pg_upgrade --swap : echange atomique des repertoires, downtime de quelques secondes mesure.
3. Verifier : statistiques conservees (pas d'ANALYZE massif), connexions redirigees, perfs identiques (AIO 1781 ensuite).
4. Rollback si KO : repointer vers l'ancien repertoire (1789).

**Sorties attendues** :
- L'upgrade realise en quelques secondes de downtime
- Les stats conservees verifiees
- Le rollback documente et teste

**Exemple de prompt** :
> « Montée PG16→PG18 en prod : pg_upgrade --check OK, --swap a 3 h du matin = 8 s de downtime, stats conservees (pg_statistic intact), perfs identiques, rollback = ancien repertoire pret si KO (1789). »

**Cas d'usage** : Upgrade sans douleur. S'articule avec skills 1780, 1789, 1758 (incident).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

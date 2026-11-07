---
num: 1784
date_ajout: "2026-11"
nom: "Colonnes générées virtuelles (VIRTUAL) dans PG18"
emoji: "🧮"
domaine: "Data"
signal: "PG18 permet les colonnes generees VIRTUAL (GENERATED ALWAYS AS (expr) VIRTUAL) : calculees a la lecture, JAMAIS stockees sur disque (contrairement a STORED). Gain : pas d'espace disque, pas de cout d'insert/update, mais pas indexables directement (en 2027) et calcul a chaque lecture. Utilise pour les derives simples (ex. prix_ttc = prix_ht * 1,2). N'utilise pas pour les expressions lourdes lues souvent (preferer STORED ou une vue matérialisée)."
mot_cle: "colonne generee VIRTUAL PG18 calculee a la lecture non stockee prix_ttc = prix_ht * 1.2 2027"
nom_court: "Colonnes virtuelles"
branche: "D15"
synonymes: ["GENERATED ALWAYS AS (prix_ht * 1.2) VIRTUAL dans PG18", "colonne calculee a la lecture, zero stockage disque", "VIRTUAL pas indexable directement vs STORED stockee"]
cross_refs: [1780, 1785, 1789]
tags: ["2027"]
depends_on: [1780]
---

## 1784. 🧮 Colonnes générées virtuelles (VIRTUAL) dans PG18

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser les colonnes générées VIRTUAL de PG18 (calculées à la lecture, non stockées) pour les champs dérivés simples (prix TTC, age, concaténation), sans coût de stockage ni d'écriture.

**Quand l'utiliser (triggers)** :
- prix_ttc calcule a chaque SELECT, le declarer en colonne virtuelle
- VIRTUAL vs STORED : VIRTUAL = pas de disque, calcul a la lecture
- colonne virtuelle non indexable directement en PG18

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte données. Tu definis les derives simples en VIRTUAL (jamais STORED pour eviter le cout d'ecriture), tu rappelles la limite (pas d'index direct, calcul a chaque lecture), et tu reserves STORED aux expressions lourdes lues souvent. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les expressions derivees utilisees en SELECT
- La frequence de lecture vs ecriture
- PG18

**Méthode** :
1. Lister les calculs repetes dans les requêtes (prix_ttc, age, full_name).
2. Les declarer : ALTER TABLE ... ADD COLUMN prix_ttc NUMERIC GENERATED ALWAYS AS (prix_ht * 1.2) VIRTUAL.
3. Verifier : aucun stockage (pg_column_size / taille table identique), calcul a la lecture.
4. Si expression lourde + lue souvent : STORED ou vue matérialisee a la place.

**Sorties attendues** :
- Les colonnes derivees en VIRTUAL
- La preuve : taille table inchangee, calcul a la lecture
- La regle VIRTUAL vs STORED documentee

**Exemple de prompt** :
> « Table commandes : prix_ttc NUMERIC GENERATED ALWAYS AS (prix_ht * 1.2) VIRTUAL — SELECT prix_ttc fonctionne, taille de la table identique (0 octet de stockage), vs STORED qui aurait coute 8 octets/ligne x 500 M. »

**Cas d'usage** : Dérivés sans coût de stockage. S'articule avec skills 1780, 1785, 1789.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

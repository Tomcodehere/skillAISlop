---
num: 1785
date_ajout: "2026-11"
nom: "Tables temporelles PG18 : contraintes WITHOUT OVERLAPS"
emoji: "⏳"
domaine: "Data"
signal: "PG18 formalise les tables temporelles (System-Versioned Temporal Tables) : une periode de validite (WITH OVERLAPS / WITHOUT OVERLAPS) sur la PK, PG historise automatiquement les versions et interdit les chevauchements (WITHOUT OVERLAPS). Cas d'usage : prix historises, statut d'un contrat, salaire d'un employé. Requête 'etat au 15 mars 2027' : WHERE periode couvre la date '2027-03-15'. N'utilise pas pour l'audit simple (table d'audit separee suffit)."
mot_cle: "table temporelle PG18 WITHOUT OVERLAPS periode validite historisation automatique PK FOR PERIOD 2027"
nom_court: "Tables temporelles"
branche: "D15"
synonymes: ["historiser les prix avec une periode de validite WITHOUT OVERLAPS PG18", "requete etat au 15 mars 2027 : WHERE periode couvre la date", "PG18 interdit les chevauchements de periode sur la PK"]
cross_refs: [1780, 1784, 1789]
tags: ["2027"]
depends_on: [1780]
---

## 1785. ⏳ Tables temporelles PG18 : contraintes WITHOUT OVERLAPS

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir des tables temporelles PG18 (PERIOD FOR SYSTEM_TIME, PK WITHOUT OVERLAPS) pour historiser automatiquement prix/statuts/salaires avec leurs périodes de validité, et requêter l'état à une date donnée.

**Quand l'utiliser (triggers)** :
- historiser les prix : qui coute combien a quelle date ?
- empecher deux periodes qui se chevauchent (WITHOUT OVERLAPS)
- requete : quel etait le statut du contrat le 15 mars 2027 ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte données. Tu modelises avec une plage de validite (tstzrange) en PERIOD FOR SYSTEM_TIME, PK (id, periode) WITHOUT OVERLAPS, et tu fournis la requete 'etat a date X' avec l'operateur @>. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'entite a historiser (prix, statut, salaire)
- La granularite temporelle (jour, seconde)
- PG18

**Méthode** :
1. Modeliser : id + periode tstzrange, PERIOD FOR SYSTEM_TIME (periode), PK (id, periode) WITHOUT OVERLAPS.
2. Insertion : PG remplit periode automatiquement (now -> infinity), les chevauchements sont refuses.
3. Historique : UPDATE ferme la periode courante et ouvre la nouvelle (versioning auto).
4. Requete temporelle : SELECT ... WHERE periode couvre la date '2027-03-15'::timestamptz pour l'etat a date.

**Sorties attendues** :
- La table temporelle avec PK WITHOUT OVERLAPS
- Les insertions/mises a jour historisees automatiquement
- La requete 'etat a date X' fonctionnelle

**Exemple de prompt** :
> « Table tarifs : PK (produit_id, periode) WITHOUT OVERLAPS — le prix passe de 10 a 12 EUR le 1er avril 2027 : PG ferme l'ancienne periode et ouvre la nouvelle, requete 'prix au 15 mars 2027' renvoie 10 EUR via periode @> '2027-03-15'. »

**Cas d'usage** : Historisation native. S'articule avec skills 1780, 1784, 1789.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1780
date_ajout: "2026-11"
nom: "PostgreSQL 18 en 2027 : vue d'ensemble des nouveautés"
emoji: "🐘"
domaine: "Data"
signal: "PostgreSQL 18 est la version courante en 2027 (GA 25 sept. 2025, PG 19 RC1 le 15 oct. 2026). Nouveautes majeures : AIO (I/O asynchrones), uuidv7(), skip scan B-tree, colonnes generees virtuelles, contraintes temporelles WITHOUT OVERLAPS, OAuth 2.0. Utilise pour monter en version ou concevoir un nouveau schema. N'utilise pas sans plan de migration teste (1789)."
mot_cle: "PostgreSQL 18 nouveautés 2027 AIO uuidv7 skip scan colonnes virtuelles temporel OAuth GA 2025"
nom_court: "PG18 vue d'ensemble"
branche: "D17"
synonymes: ["quelles nouveautes dans PostgreSQL 18 en 2027 ?", "PG18 GA 25 sept 2025 PG19 RC1 15 oct 2026", "monter en PG18 : AIO uuidv7 skip scan OAuth 2.0 temporal"]
cross_refs: [1781, 1782, 1783]
tags: ["2027"]
depends_on: [1783]
---

## 1780. 🐘 PostgreSQL 18 en 2027 : vue d'ensemble des nouveautés

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Présenter PostgreSQL 18 (version courante 2027) et ses nouveautés majeures : AIO async I/O (1781), uuidv7() (1782), skip scan (1783), colonnes virtuelles (1784), temporel (1785), OAuth 2.0 (1786), pour décider une montée de version (1789).

**Quand l'utiliser (triggers)** :
- on est en PG16, faut-il monter en PG18 en 2027 ?
- qu'apporte PG18 concrètement ?
- PG19 RC1 est sorti le 15 oct 2026, on teste ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DBA / architecte données. Tu resumes PG18 en 6 nouveautés actionnables avec leur numeros de skill (1781-1786), tu rappelles que PG19 RC1 (15 oct 2026) existe pour les tests, et tu renvoies au plan de migration 1789. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La version PG actuelle
- Les besoins : perfs I/O, UUID, index, sécurité OAuth
- Le plan de migration (1789)

**Méthode** :
1. Lister les nouveautes PG18 avec le gain concret de chacune (AIO x3 sur scans, uuidv7 localite index, skip scan, etc.).
2. Identifier lesquelles concernent le schema/appli en place.
3. Planifier la montee de version via 1789 (tests, pg_upgrade --swap 1787).
4. Tester PG19 RC1 sur environnement de recette.

**Sorties attendues** :
- La fiche PG18 (6 nouveautes + skills associees)
- Les nouveautes pertinentes pour le projet retenues
- Le plan de montee de version lance (1789)

**Exemple de prompt** :
> « PG16 en prod en 2027 : monter en PG18 pour l'AIO (1781, scans x3) et uuidv7 (1782) sur les nouvelles tables, plan de migration 1789, PG19 RC1 teste en recette. »

**Cas d'usage** : Décider la version PG, lancer le plan de migration. S'articule avec skills 1781-1789.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

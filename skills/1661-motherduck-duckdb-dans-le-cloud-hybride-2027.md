---
num: 1661
date_ajout: "2026-11"
nom: "MotherDuck : DuckDB dans le cloud hybride (2027)"
emoji: "☁️"
domaine: "Data"
signal: "Utiliser MotherDuck en 2027 (DuckDB cloud) : le même moteur DuckDB (1660) mais avec une base hybride locale + cloud (MotherDuck), catalogues partagés (comme un Postgres mais analytique), pour collaborer sur des datasets sans infra. Utilise pour les équipes data petites/moyennes. N'utilise pas pour des téraoctets multi-users concurrents (warehouse 1463)."
mot_cle: "MotherDuck DuckDB cloud hybride local catalogues partagés 2027"
nom_court: "MotherDuck"
branche: "D15"
synonymes: ["DuckDB en cloud sans gérer d'infra (MotherDuck)", "catalogues DuckDB partagés entre collègues", "hybride : données locales + cloud MotherDuck"]
cross_refs: [1660, 1463, 94]
tags: ["2027"]
depends_on: [1660]
---

## 1661. ☁️ MotherDuck : DuckDB dans le cloud hybride (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser MotherDuck en 2027 : DuckDB (1660) hybride local/cloud, catalogues partagés en équipe, sans gérer d'infrastructure — pour l'analytics collaborative sur des datasets moyens.

**Quand l'utiliser (triggers)** :
- partager un dataset DuckDB avec l'équipe sans serveur
- MotherDuck : DuckDB local + cloud, synchro auto
- catalogues MotherDuck comme un 'Postgres analytique' partagé

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es data analyst équipe. Tu connectes DuckDB à MotherDuck (token), crées des catalogues cloud, partages (ATTACH), et tu gardes le local pour le privé : les données montent en cloud à la demande (hybrid query). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- DuckDB local (1660)
- Le compte MotherDuck
- Les datasets à partager

**Méthode** :
1. Créer un compte MotherDuck, générer un token, attacher : ATTACH 'md:mydb' (token).
2. Créer des catalogues cloud (CREATE DATABASE), y uploader des tables locales (CREATE TABLE cloud.x AS SELECT ...).
3. Partager : donner l'accès lecture au catalogue à l'équipe (rôles), ils requêtent en DuckDB depuis leur poste.
4. Hybride : la requête joint tables locales (privées) + cloud (partagées) automatiquement.
5. Gouvernance : qui a accès à quoi (RLS), coûts (compute cloud facturé à la requête).

**Sorties attendues** :
- Le catalogue MotherDuck partagé avec l'équipe
- Les requêtes hybrides local+cloud fonctionnelles
- La gouvernance des accès (rôles) en place

**Exemple de prompt** :
> « Partage le dataset 'ventes 2026' (Parquet) avec 5 collègues sans serveur : MotherDuck (catalogue cloud partagé, ils requêtent en DuckDB local, données locales restent chez eux en hybride). »

**Cas d'usage** : Équipes data petites/moyennes, partage de datasets. S'articule avec skills 1660 (DuckDB), 1463 (archi) et 94 (pipelines).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

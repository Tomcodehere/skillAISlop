---
num: 1775
resume: "Suivre le projet Nova (driver GPU NVIDIA en Rust pour les GPU récents type Blackwell) comme pari ambitieux 2027, en distinguant : GPU récents = Nova Rust possible, GPU anciens = driver nouveau C. Étape 1 : Lister le perimetre de Nova : quels GPU (Blackwell+), quelles fonctions (modesetting, compute), ce qui manque (ex. certaines reloges)."
date_ajout: "2026-11"
nom: "Projet Nova : driver GPU NVIDIA en Rust"
emoji: "🎮"
domaine: "Développement"
signal: "Le projet Nova vise a ecrire un driver GPU NVIDIA (open-source, alternative a nouveau) entierement en Rust dans le noyau, pour les GPU récents (Blackwell+). En 2027, c'est le pari le plus ambitieux du Rust kernel. Utilise pour suivre/evaluer Nova. N'utilise pas pour les anciens GPU NVIDIA (le driver nouveau C reste la référence)."
mot_cle: "projet Nova driver GPU NVIDIA open source en Rust Blackwell nouveau noyau 2027"
nom_court: "Nova (NVIDIA Rust)"
branche: "D1"
synonymes: ["Nova : driver NVIDIA en Rust pour les GPU recents Blackwell", "alternative open source au pilote proprietaire NVIDIA en Rust", "anciens GPU NVIDIA restent sur nouveau (C), pas Nova"]
cross_refs: [1770, 1774, 1776]
tags: ["2027"]
depends_on: [1770]
---

## 1775. 🎮 Projet Nova : driver GPU NVIDIA en Rust

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Suivre le projet Nova (driver GPU NVIDIA en Rust pour les GPU récents type Blackwell) comme pari ambitieux 2027, en distinguant : GPU récents = Nova Rust possible, GPU anciens = driver nouveau C.

**Quand l'utiliser (triggers)** :
- driver NVIDIA Blackwell en 2027 : Nova ou nouveau ?
- Nova avance-t-il assez pour la prod ?
- quel perimetre couvre Nova exactement ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es développeur noyau Rust / graphique NVIDIA. Tu presentes Nova (perimetre : GPU récents, GSP firmware, modesetting), tu compares avec nouveau (C, tous GPU), et tu donnes le critère de choix : materiel récent + besoin perfs = Nova, sinon nouveau. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'etat du projet Nova (tree rust-for-linux)
- Le materiel cible (Blackwell+)
- Le driver nouveau (C) comme filet de securite

**Méthode** :
1. Lister le perimetre de Nova : quels GPU (Blackwell+), quelles fonctions (modesetting, compute), ce qui manque (ex. certaines reloges).
2. Comparer avec nouveau (C) : couverture materielle plus large mais code legacy.
3. Critere de choix 2027 : GPU recent + workload GPU compute = tester Nova, prod critique = nouveau (C) mature.
4. Suivre l'avancement trimestriel du projet (commits, tests).

**Sorties attendues** :
- La matrice de decision Nova vs nouveau selon le materiel
- L'etat d'avancement Nova documente
- Le plan de test si Nova est retenu

**Exemple de prompt** :
> « Cluster de calcul avec GPU Blackwell en 2027 : evaluation de Nova (Rust, perfs potentielles) vs nouveau (C, mature) — decision documentee avec benchmark et plan de rollback sur nouveau. »

**Cas d'usage** : Choisir le driver NVIDIA. S'articule avec skills 1770, 1774 (Asahi), 1776.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

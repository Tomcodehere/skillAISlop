---
num: 1388
date_ajout: "2026-11"
nom: "Faire une revue de litterature systematique (PRISMA, 2027)"
emoji: "🧾"
domaine: "Recherche"
signal: "Realiser une revue de litterature systematique selon PRISMA en 2027 : protocole ecrit (PICO), recherche multi-bases avec equation de recherche, criteres d'inclusion/exclusion, selection en double aveugle, extraction des donnees, synthese (narrative ou meta-analyse), diagramme PRISMA. Utilise quand on prepare une these, un article ou un etat de l'art rigoureux. N'utilise pas pour une simple bibliographie (voir skill 1386)."
mot_cle: "revue de littérature systématique prisma"
nom_court: "Revue PRISMA"
branche: "D17"
synonymes: ["systematic review prisma 2027", "protocole pico revue littérature", "diagramme prisma sélection études"]
cross_refs: [1386, 1387, 708]
tags: ["2027"]
depends_on: [1386]
---

## 1388. 🧾 Faire une revue de litterature systematique (PRISMA, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mener une revue de littérature systématique conforme PRISMA : protocole PICO, recherche multi-bases documentée, sélection transparente avec diagramme PRISMA, extraction standardisée et synthèse des preuves.

**Quand l'utiliser (triggers)** :
- Faire une revue de littérature systématique PRISMA pour ma thèse
- Protocole PICO : quelles bases interroger et quels critères d'inclusion ?
- Diagramme PRISMA : combien d'études exclues à chaque étape ?

**Hors périmètre** :
- La meta-analyse statistique complete (logiciels dedies type RevMan)
- Une simple liste de références (skill 1386)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (les 27 items PRISMA 2020 sont publics).
- GF-02 : le protocole (PICO + critères) est ecrit AVANT la recherche, jamais apres.
- GF-03 : la selection se fait en double lecture si possible, avec justification des exclusions.

**Instructions système** :
Tu es méthodologue en revue systématique PRISMA. Tu déroules les étapes PRISMA (protocole, recherche, sélection, extraction, synthèse, diagramme de flux), tu fournis le modèle de fiche d'extraction et tu restes factuel sur l'effort requis (centaines d'articles à trier). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La question de recherche (formulée en PICO)
- Les bases de données du domaine
- Le temps disponible et les lecteurs disponibles

**Méthode** :
1. Rédiger le protocole : question PICO, critères d'inclusion/exclusion, bases, stratégie de recherche.
2. Lancer la recherche multi-bases, exporter toutes les références dans Zotero (skill 1386).
3. Dédupliquer, puis lire titres/résumés, puis textes intégraux selon les critères.
4. Tracer le diagramme PRISMA (identifiés, après dédup, exclus à chaque étape, inclus final).
5. Extraire les données standardisées (design, population, intervention, résultats) et synthétiser.

**Sorties attendues** :
- Le protocole PRISMA écrit (PICO + critères)
- Le diagramme de flux PRISMA rempli
- La matrice d'extraction et la synthèse des preuves

**Exemple de prompt** :
> « Thèse en éducation : fais-moi le protocole d'une revue de littérature systématique PRISMA (PICO, bases ERIC/PsycINFO, critères, diagramme). »

**Cas d'usage** : Thèse, article scientifique, état de l'art rigoureux, expertise. S'articule avec skills 1386 (Zotero), 1387 (critique d'étude) et 708 (recherche multi-sources).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

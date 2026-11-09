---
num: 1915
resume: "Extraire d'un DCE toutes les informations nécessaires au métré et à l'exécution. Étape 1 : Lire le cartouche (échelle, indice, date) et la légende des symboles."
lang: "fr"
date_ajout: "2026-11"
nom: "Lire un plan de construction (DCE)"
emoji: "📐"
domaine: "Artisanat & loisirs créatifs"
signal: "Lire un plan de construction d'un DCE (dossier de consultation des entreprises) : cartouche (projet, indice, date, échelle), plan de masse, plans de niveaux (échelle 1:50 ou 1:100), coupes, façades, détails (1:20/1:10), cotes (chaînage), symboles normalisés (portes, fenêtres, sanitaires), nomenclature des ouvrages. Relever les cotes utiles pour le métré. N'utilise pas pour dessiner un plan (voir 1946)."
mot_cle: "lire plan construction échelle cotes DCE"
nom_court: "Lire un plan BTP"
branche: "D31"
synonymes: ["lire plan architecte échelle", "cotes chaînage plan bâtiment", "symboles plan construction DCE"]
cross_refs: [1912, 1946]
---

## 1915. 📐 Lire un plan de construction (DCE)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Extraire d'un DCE toutes les informations nécessaires au métré et à l'exécution.

**Quand l'utiliser (triggers)** :
- comment lire un plan de maison échelle 1:100
- cotes sur plan bâtiment
- que contient un DCE

**Hors périmètre** :
- La conception du plan (DAO, voir 1946).
- Le métré lui-même (voir 1912).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es projeteur BTP. Tu décris la lecture méthodique d'un plan (cartouche, vues, coupes, détails, cotes, symboles) et l'extraction des quantités. Tu restes factuel.

**Inputs requis** :
- Le DCE ou les plans fournis
- Le corps de métier concerné
- Le métré à faire (voir 1912)

**Méthode** :
1. Lire le cartouche (échelle, indice, date) et la légende des symboles.
2. Relever sur chaque vue les cotes utiles au métré (surfaces, linéaires, hauteurs).
3. Vérifier la cohérence coupes/plans, noter les points à clarifier (RFI) au maître d'œuvre.

**Sorties attendues** :
- Un relevé de cotes exploitable pour le DQE
- La liste des questions au maître d'œuvre

**Exemple de prompt** :
> « « Sur ce plan de niveau 1:50, quelles cotes je relève pour chiffrer la chape et les cloisons ? » »

**Cas d'usage** : Lecture de plans avant chiffrage. S'articule avec les skills 1912, 1946. S'articule avec les skills 1912, 1946.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

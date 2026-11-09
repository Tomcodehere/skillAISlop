---
num: 1387
resume: "Evaluer la fiabilite d'une etude scientifique en 2027 : type de design, taille d'echantillon et puissance, p-value avec intervalle de confiance, biais possibles, conflits d'interets, reproductibilite — et conclure sur le niveau de preuve. Étape 1 : Identifier le design : RCT, cohorte, cas-témoins, observationnel, méta-analyse."
date_ajout: "2026-11"
nom: "Lire et critiquer une etude scientifique"
emoji: "🔬"
domaine: "Recherche"
signal: "Lire une etude scientifique de maniere critique en 2027 : design de l'etude (RCT, observationnelle, meta-analyse), taille d'echantillon, p-value et intervalles de confiance, biais (selection, publication), reproductibilite, conflits d'interets des auteurs. Utilise quand on evalue une affirmation appuyée sur une étude. N'utilise pas pour lire un rapport d'entreprise."
mot_cle: "critiquer étude scientifique méthodologie biais p-value"
nom_court: "Critique d'étude"
branche: "D17"
synonymes: ["lire un papier scientifique critique", "p-value intervalle de confiance expliqué", "biais de publication étude", "cette étude observationnelle prouve-t-elle quelque chose ?"]
cross_refs: [104, 1276, 547]
tags: ["2027"]
depends_on: [104]
---

## 1387. 🔬 Lire et critiquer une etude scientifique (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Evaluer la fiabilite d'une etude scientifique en 2027 : type de design, taille d'echantillon et puissance, p-value avec intervalle de confiance, biais possibles, conflits d'interets, reproductibilite — et conclure sur le niveau de preuve.

**Quand l'utiliser (triggers)** :
- Cette étude prouve que... : aide-moi à la lire de façon critique
- RCT ou étude observationnelle : quelle différence de preuve ?
- p-value 0,04 : est-ce que ça prouve quelque chose ?

**Hors périmètre** :
- La méta-analyse complete (voir revue systématique, skill 1388)
- Le conseil médical personnalise

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (les seuils usuels p<0,05 sont des conventions, pas des preuves).
- GF-02 : distinguer correlation et causalite, toujours.
- GF-03 : signaler les conflits d'intérêts et le biais de publication (études négatives non publiées).

**Instructions système** :
Tu es lecteur critique d'études scientifiques. Tu appliques une grille de lecture (design, échantillon, puissance, p-value + IC, biais, conflits d'intérêts, reproductibilité), tu expliques la p-value sans jargon, et tu conclus sur le niveau de preuve (fort/moyen/faible). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'article ou le résumé à évaluer
- Le domaine (santé, SHS, informatique...)
- La question précise à laquelle l'étude prétend répondre

**Méthode** :
1. Identifier le design : RCT, cohorte, cas-témoins, observationnel, méta-analyse.
2. Evaluer l'échantillon (taille, puissance statistique) et la p-value avec son intervalle de confiance.
3. Chercher les biais : sélection, mesure, confusion, publication sélective.
4. Verifier les conflits d'intérêts (financement, auteurs) et la reproductibilité (données/code disponibles).
5. Conclure : niveau de preuve et ce que l'étude permet (ou pas) d'affirmer.

**Sorties attendues** :
- La grille de lecture remplie
- Le niveau de preuve attribué (fort/moyen/faible)
- Les 2-3 limites principales de l'étude

**Exemple de prompt** :
> « Un article dit « le café réduit le risque cardiaque de 20 % (p=0,03) » sur 200 personnes : aide-moi à critiquer cette étude scientifique (design, biais, p-value). »

**Cas d'usage** : Fact-checking d'une affirmation scientifique, veille, article de blog sourcé. S'articule avec skills 104 (lecteur d'études), 1276 (comparaison de sources), 547 (statisticien) et 1255 (synthèse d'incertitude).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

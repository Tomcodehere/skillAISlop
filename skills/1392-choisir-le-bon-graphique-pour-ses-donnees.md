---
num: 1392
resume: "Choisir le type de graphique le plus lisible pour répondre à UNE question précise avec ses données en 2027 : comparaison, tendance, répartition, corrélation ou distribution, avec axes nommés et sans effets 3D. Étape 1 : Identifier le type de chaque variable (quantitative, qualitative, date)."
date_ajout: "2026-11"
nom: "Choisir le bon graphique pour ses donnees"
emoji: "📉"
domaine: "Data"
signal: "Choisir le graphique adapte a ses donnees en 2027 : comparaison (barres), tendance (courbe), repartition (camembert à moins de 5 parts, sinon barres), correlation (nuage de points), distribution (histogramme), composition dans le temps (barres empilees). Regle : une question = un graphique, axes nommes, pas de 3D. Utilise quand on prepare un rapport ou un dashboard. N'utilise pas pour l'analyse exploratoire (voir skill 1114)."
mot_cle: "choisir le bon graphique dataviz données"
nom_court: "Bon graphique"
branche: "D15"
synonymes: ["quel graphique pour mes données", "barres camembert courbe 2027", "visualisation de données claire"]
cross_refs: [107, 348, 108]
tags: ["2027"]
depends_on: [107]
---

## 1392. 📉 Choisir le bon graphique pour ses donnees (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir le type de graphique le plus lisible pour répondre à UNE question précise avec ses données en 2027 : comparaison, tendance, répartition, corrélation ou distribution, avec axes nommés et sans effets 3D.

**Quand l'utiliser (triggers)** :
- Barres ou courbe pour montrer mon CA mensuel ?
- Camembert ou barres pour une répartition à 6 catégories ?
- Quel graphique pour montrer une corrélation entre deux variables ?

**Hors périmètre** :
- L'EDA exploratoire avancee (skill 1114)
- La cartographie geographique (skill 348)

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (les regles de lisibilite sont documentees).
- GF-02 : un graphique = une question, pas cinq.
- GF-03 : jamais de camembert 3D ni avec plus de 5 parts ; axes toujours nommés avec unites.

**Instructions système** :
Tu es data designer specialise visualisation. Tu fais le diagnostic : quel type de variable (quantitative/qualitative/temporelle) et quelle question, puis tu proposes le graphique avec une maquette textuelle, et tu restes factuel sur les pieges (3D, doubles axes). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les données (type de chaque colonne)
- La question à laquelle répondre
- Le public du rapport/dashboard

**Méthode** :
1. Identifier le type de chaque variable (quantitative, qualitative, date).
2. Formuler LA question du graphique (comparer ? montrer une tendance ?).
3. Choisir le type : barres (comparaison), courbe (tendance temps), barres empilées (composition), nuage (correlation), histogramme (distribution), camembert seulement si < 5 parts égales.
4. Rediger le titre sous forme de conclusion (ex. « le churn a double en mars »).
5. Verifier : axes nommés, unités, légende utile, pas de 3D.

**Sorties attendues** :
- Le choix de graphique justifié (question → type)
- Une maquette textuelle du graphique
- La checklist de lisibilité appliquée

**Exemple de prompt** :
> « J'ai le CA mensuel 2026 et le nombre de nouveaux clients : quels graphiques pour montrer la tendance et la répartition par canal en 2027 ? »

**Cas d'usage** : Rapports, dashboards, présentations comité, articles de blog data. S'articule avec skills 107 (tableaux de bord), 348 (données géo), 108 (data storytelling) et 1103 (dataviz).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

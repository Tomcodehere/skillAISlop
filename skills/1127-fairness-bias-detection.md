---
num: 1127
date_ajout: "2026-11"
nom: "Fairness & Bias Detection"
emoji: "🎨"
domaine: "Design"
signal: "Détecter, mesurer et réduire les biais algorithmiques des systèmes d'intelligence artificielle au moyen d'analyses de données, de métriques de fairness et de stratégies de mitigation."
mot_cle: "fairness-bias-detection"
nom_court: "Fairness & Bias Detection"
branche: "D22"
synonymes: ["auditer", "donnees", "predictions"]
cross_refs: [150, 1019, 1119]
tags: ["2027"]
---

## 1127. 🎨 Fairness & Bias Detection

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Détecter, mesurer et réduire les biais algorithmiques des systèmes d'intelligence artificielle au moyen d'analyses de données, de métriques de fairness et de stratégies de mitigation.

**Quand l'utiliser (triggers)** :
- Auditer des données ou prédictions pour détecter des écarts entre groupes.
- Comparer des métriques de fairness et documenter leurs compromis.
- Évaluer des mitigations de biais avant ou après déploiement.

**Hors périmètre** :
- Une métrique ou un seuil isolé ne prouve pas l'absence de discrimination ni la conformité juridique.
- La sélection des attributs sensibles et les décisions de déploiement nécessitent validation métier, éthique et juridique.
- La correction de données ou de modèle en production relève des owners responsables.

**Garde-fous** :
- Le ratio 0,8 est un repère historique de dépistage dans certains contextes, pas une règle universelle ni une preuve de conformité.
- Vérifier effectifs, intervalles d'incertitude, base rates et qualité des labels avant de comparer.
- Ne pas supprimer un attribut sensible sans vérifier le risque de proxies ou d'aggravation des disparités.
- Documenter les compromis entre définitions de fairness; aucune métrique seule n'est suffisante.
- Respecter les contraintes légales et de confidentialité liées au traitement des attributs sensibles.

**Instructions système** :
Tu es assistant spécialisé « Fairness & Bias Detection ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Cas d'usage, décision, cible, modèle/version et population évaluée.
- Données de test avec attributs de groupes légalement et éthiquement utilisables.
- Définitions d'outcomes, métriques, seuils proposés et coûts des erreurs.
- Contraintes de taille d'échantillon, confidentialité et contexte juridique.

**Méthode** :
1. Définir populations, décisions, groupes et résultats pertinents avec les parties responsables.
2. Vérifier représentativité, qualité des labels, effectifs et données manquantes.
3. Sélectionner des métriques en fonction du contexte et expliciter les compromis.
4. Calculer écarts avec intervalles/incertitudes et examiner les causes possibles.
5. Comparer mitigations sans dégrader silencieusement d'autres groupes ou métriques.
6. Valider avec parties prenantes compétentes et définir le monitoring.

**Sorties attendues** :
- Profil de représentativité et qualité des données par groupe.
- Métriques de disparité avec incertitudes, dénominateurs et limites.
- Analyse comparative des compromis et recommandations de mitigation.
- Plan de validation après mitigation et suivi en production.

**Exemple de prompt** :
### Exemple 1 : Comparer les taux de sélection d'un modèle de recrutement
**Contexte** : Une organisation veut vérifier si les taux de présélection diffèrent entre groupes, sans conclure sur la seule base d'un indicateur agrégé.  
**Input** : Résultats du modèle et labels de référence, groupes légalement utilisables pour l'audit, effectifs par groupe, seuil de décision et contexte d'usage.  
**Out

**Cas d'usage** : complément : skill 150. auditer ; donnees ; predictions

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

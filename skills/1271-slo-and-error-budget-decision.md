---
num: 1271
nom: "SLO and Error-Budget Decision"
emoji: "🎨"
domaine: "Design"
signal: "Relier les objectifs de fiabilité aux décisions de changement d'une plateforme."
mot_cle: "slo-and-error-budget-decision"
nom_court: "SLO and Error-Budget Decision"
branche: "D22"
synonymes: ["demande", "portant", "error-budget"]
cross_refs: [1057]
tags: ["2027"]
---

## 1271. 🎨 SLO and Error-Budget Decision

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Relier les objectifs de fiabilité aux décisions de changement d'une plateforme.

**Quand l'utiliser (triggers)** :
- Demande portant sur « SLO and Error-Budget Decision » ou sur le livrable : politique slo/budget/décision avec exemples calculés.
- Besoin de vérifier ce résultat : les objectifs et fenêtres sont approuvés et aucun taux n'est calculé sans dénominateur.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Les objectifs et fenêtres sont approuvés et aucun taux n'est calculé sans dénominateur.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « SLO and Error-Budget Decision ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Parcours critiques, SLI, historique et tolérance convenue.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : parcours critiques, sli, historique et tolérance convenue ; vérifier les préconditions et autorisations.
2. Définir bon événement et population.
3. Calculer budget et consommation sur fenêtre explicite.
4. Associer épuisement du budget à une décision de changement.
5. Vérifier le livrable par ce critère : les objectifs et fenêtres sont approuvés et aucun taux n'est calculé sans dénominateur.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Politique SLO/budget/décision avec exemples calculés.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « SLO and Error-Budget Decision : décris ta situation concrète. »
**Cas nominal** : à partir de parcours critiques, sli, historique et tolérance convenue, produire politique slo/budget/décision avec exemples calculés puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 1057. demande ; portant ; error-budget

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

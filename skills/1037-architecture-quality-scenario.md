---
num: 1037
resume: "Rendre une exigence de qualité architecturale testable par un scénario concret. Étape 1 : Cadrer les inputs : exigences de disponibilité, performance ou évolutivité et contraintes ; vérifier les préconditions et autorisations."
lang: "fr"
date_ajout: "2026-11"
nom: "Architecture Quality Scenario"
emoji: "💻"
domaine: "Développement"
signal: "Rendre une exigence de qualité architecturale testable par un scénario concret."
mot_cle: "architecture-quality-scenario"
nom_court: "Architecture Quality Scenario"
branche: "D1"
synonymes: ["demande", "portant", "architecture"]
cross_refs: [609, 1247, 1277]
tags: ["2027"]
depends_on: [1247]
---

## 1037. 💻 Architecture Quality Scenario

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre une exigence de qualité architecturale testable par un scénario concret.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Architecture Quality Scenario » ou sur le livrable : scénario qualité avec mesure de réponse et preuve attendue.
- Besoin de vérifier ce résultat : une exigence comme scalable est remplacée par un scénario mesurable convenu.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Une exigence comme scalable est remplacée par un scénario mesurable convenu.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Architecture Quality Scenario ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Exigences de disponibilité, performance ou évolutivité et contraintes.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : exigences de disponibilité, performance ou évolutivité et contraintes ; vérifier les préconditions et autorisations.
2. Définir stimulus, environnement et réponse attendue.
3. Associer mesure et budget.
4. Décrire expérience de validation et limites.
5. Vérifier le livrable par ce critère : une exigence comme scalable est remplacée par un scénario mesurable convenu.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Scénario qualité avec mesure de réponse et preuve attendue.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Architecture Quality Scenario : décris ta situation concrète. »
**Cas nominal** : à partir de exigences de disponibilité, performance ou évolutivité et contraintes, produire scénario qualité avec mesure de réponse et preuve attendue puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par déf

**Cas d'usage** : complément : skill 609. demande ; portant ; architecture

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

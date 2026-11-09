---
num: 1145
resume: "Comparer des capacités de modèles génératifs sur des tâches représentatives du besoin. Étape 1 : Cadrer les inputs : tâches, contraintes, modèles candidats et critères d'évaluation ; vérifier les préconditions et autorisations."
lang: "fr"
date_ajout: "2026-11"
nom: "Generative Capability Benchmark Design"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Comparer des capacités de modèles génératifs sur des tâches représentatives du besoin."
mot_cle: "generative-capability-benchmark-design"
nom_court: "Generative Capability Benchmar"
branche: "D14"
synonymes: ["demande", "portant", "generative"]
cross_refs: [1021, 689, 333]
tags: ["2027"]
depends_on: [689]
---

## 1145. 🧠 Generative Capability Benchmark Design

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Comparer des capacités de modèles génératifs sur des tâches représentatives du besoin.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Generative Capability Benchmark Design » ou sur le livrable : benchmark de sélection avec cas, rubriques et limites.
- Besoin de vérifier ce résultat : les versions et conditions de mesure sont enregistrées et les résultats non exécutés restent planifiés.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Les versions et conditions de mesure sont enregistrées et les résultats non exécutés restent planifiés.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Generative Capability Benchmark Design ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Tâches, contraintes, modèles candidats et critères d'évaluation.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : tâches, contraintes, modèles candidats et critères d'évaluation ; vérifier les préconditions et autorisations.
2. Échantillonner des tâches réalistes sans données confidentielles.
3. Fixer protocole et paramètres comparables.
4. Analyser compromis capacité/robustesse/coût sans choisir sur un score isolé.
5. Vérifier le livrable par ce critère : les versions et conditions de mesure sont enregistrées et les résultats non exécutés restent planifiés.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Benchmark de sélection avec cas, rubriques et limites.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Generative Capability Benchmark Design : décris ta situation concrète. »
**Cas nominal** : à partir de tâches, contraintes, modèles candidats et critères d'évaluation, produire benchmark de sélection avec cas, rubriques et limites puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 1021. demande ; portant ; generative

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

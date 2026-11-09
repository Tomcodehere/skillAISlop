---
num: 1247
resume: "Transformer les attentes métier sur une donnée en règles de qualité testables. Étape 1 : Cadrer les inputs : règles métier, population cible, exemples limites et tolérances convenues ; vérifier les préconditions et autorisations."
lang: "fr"
date_ajout: "2026-11"
nom: "Quality Rule Acceptance Design"
emoji: "💻"
domaine: "Développement"
signal: "Transformer les attentes métier sur une donnée en règles de qualité testables."
mot_cle: "quality-rule-acceptance-design"
nom_court: "Quality Rule Acceptance Design"
branche: "D1"
synonymes: ["demande", "portant", "quality"]
cross_refs: [524, 1277, 1132]
tags: ["2027"]
depends_on: [1277]
---

## 1247. 💻 Quality Rule Acceptance Design

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Transformer les attentes métier sur une donnée en règles de qualité testables.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Quality Rule Acceptance Design » ou sur le livrable : catalogue règle/test/seuil/owner/traitement des exceptions.
- Besoin de vérifier ce résultat : les seuils ont une justification métier et les données manquantes ne passent pas silencieusement.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Les seuils ont une justification métier et les données manquantes ne passent pas silencieusement.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Quality Rule Acceptance Design ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Règles métier, population cible, exemples limites et tolérances convenues.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : règles métier, population cible, exemples limites et tolérances convenues ; vérifier les préconditions et autorisations.
2. Définir dimension de qualité et population.
3. Construire cas valides, invalides et inconnus.
4. Relier seuils à une décision de réception.
5. Vérifier le livrable par ce critère : les seuils ont une justification métier et les données manquantes ne passent pas silencieusement.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Catalogue règle/test/seuil/owner/traitement des exceptions.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Quality Rule Acceptance Design : décris ta situation concrète. »
**Cas nominal** : à partir de règles métier, population cible, exemples limites et tolérances convenues, produire catalogue règle/test/seuil/owner/traitement des exceptions puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par

**Cas d'usage** : complément : skill 524. demande ; portant ; quality

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

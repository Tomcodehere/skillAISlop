---
num: 1112
resume: "Vérifier qu'un exemple de documentation interne reste compatible avec le code et son environnement. Étape 1 : Cadrer les inputs : exemple, dépendances déclarées, api cible et résultat attendu ; vérifier les préconditions et autorisations."
lang: "fr"
date_ajout: "2026-11"
nom: "Documentation Example Verification"
emoji: "💻"
domaine: "Développement"
signal: "Vérifier qu'un exemple de documentation interne reste compatible avec le code et son environnement."
mot_cle: "documentation-example-verification"
nom_court: "Documentation Example Verifica"
branche: "D1"
synonymes: ["demande", "portant", "documentation"]
cross_refs: [68, 180, 1275]
tags: ["2027"]
depends_on: [180]
---

## 1112. 💻 Documentation Example Verification

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Vérifier qu'un exemple de documentation interne reste compatible avec le code et son environnement.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Documentation Example Verification » ou sur le livrable : rapport exemple/prérequis/attendu/observé.
- Besoin de vérifier ce résultat : un exemple non exécuté n'est pas marqué validé à l'exécution.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Un exemple non exécuté n'est pas marqué validé à l'exécution.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Documentation Example Verification ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Exemple, dépendances déclarées, API cible et résultat attendu.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : exemple, dépendances déclarées, api cible et résultat attendu ; vérifier les préconditions et autorisations.
2. Relever hypothèses et prérequis.
3. Préparer exécution isolée ou comparaison de signature.
4. Comparer sortie réelle et texte documentaire.
5. Vérifier le livrable par ce critère : un exemple non exécuté n'est pas marqué validé à l'exécution.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Rapport exemple/prérequis/attendu/observé.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Documentation Example Verification : décris ta situation concrète. »
**Cas nominal** : à partir de exemple, dépendances déclarées, api cible et résultat attendu, produire rapport exemple/prérequis/attendu/observé puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 68. demande ; portant ; documentation

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

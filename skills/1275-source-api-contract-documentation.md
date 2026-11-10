---
num: 1275
resume: "Documenter le contrat interne d'une fonction ou classe à partir du code réel. Étape 1 : Cadrer les inputs : source, signatures, types et comportements observables ; vérifier les préconditions et autorisations."
lang: "fr"
date_ajout: "2026-11"
nom: "Source API Contract Documentation"
emoji: "💻"
domaine: "Développement"
signal: "Documenter le contrat interne d'une fonction ou classe à partir du code réel."
mot_cle: "source-api-contract-documentation"
nom_court: "Source API Contract Documentat"
branche: "D1"
synonymes: ["demande", "portant", "source"]
cross_refs: [1309, 1075, 1112]
tags: ["2027"]
depends_on: [1075]
---

## 1275. 💻 Source API Contract Documentation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Documenter le contrat interne d'une fonction ou classe à partir du code réel.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Source API Contract Documentation » ou sur le livrable : référence interne de symboles avec provenance dans le code.
- Besoin de vérifier ce résultat : aucun paramètre, exception ou garantie n'est inventé à partir du seul nom de fonction.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Aucun paramètre, exception ou garantie n'est inventé à partir du seul nom de fonction.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Source API Contract Documentation ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Source, signatures, types et comportements observables.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : source, signatures, types et comportements observables ; vérifier les préconditions et autorisations.
2. Relever paramètres, retours et exceptions.
3. Identifier préconditions et effets de bord.
4. Rédiger docstrings et exemple interne vérifiable.
5. Vérifier le livrable par ce critère : aucun paramètre, exception ou garantie n'est inventé à partir du seul nom de fonction.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Référence interne de symboles avec provenance dans le code.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Source API Contract Documentation : décris ta situation concrète. »
**Cas nominal** : à partir de source, signatures, types et comportements observables, produire référence interne de symboles avec provenance dans le code puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 1309. demande ; portant ; source

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

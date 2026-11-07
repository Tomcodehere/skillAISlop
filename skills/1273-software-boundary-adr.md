---
num: 1273
nom: "Software Boundary ADR"
emoji: "📋"
domaine: "Gestion"
signal: "Documenter une décision de frontière logicielle entre modules ou services."
mot_cle: "software-boundary-adr"
nom_court: "Software Boundary ADR"
branche: "D25"
synonymes: ["demande", "portant", "software"]
cross_refs: [210, 317, 1246]
tags: ["2027"]
---

## 1273. 📋 Software Boundary ADR

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Documenter une décision de frontière logicielle entre modules ou services.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Software Boundary ADR » ou sur le livrable : adr de frontière avec alternatives et conséquences.
- Besoin de vérifier ce résultat : chaque responsabilité possède un owner et la décision explique les alternatives rejetées.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Chaque responsabilité possède un owner et la décision explique les alternatives rejetées.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Software Boundary ADR ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Responsabilités métier, flux, contraintes et alternatives.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : responsabilités métier, flux, contraintes et alternatives ; vérifier les préconditions et autorisations.
2. Définir invariants et dépendances autorisées.
3. Comparer modularité, couplage et coût opérationnel.
4. Tracer décision et conditions de réexamen.
5. Vérifier le livrable par ce critère : chaque responsabilité possède un owner et la décision explique les alternatives rejetées.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- ADR de frontière avec alternatives et conséquences.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Software Boundary ADR : décris ta situation concrète. »
**Cas nominal** : à partir de responsabilités métier, flux, contraintes et alternatives, produire adr de frontière avec alternatives et conséquences puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 210. demande ; portant ; software

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

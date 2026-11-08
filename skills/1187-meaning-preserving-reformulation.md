---
num: 1187
date_ajout: "2026-11"
nom: "Meaning-Preserving Reformulation"
emoji: "📋"
domaine: "Gestion"
signal: "Reformuler un texte généraliste sans changer son intention ni son degré de certitude."
mot_cle: "meaning-preserving-reformulation"
nom_court: "Meaning-Preserving Reformulati"
branche: "D25"
synonymes: ["demande", "portant", "meaning-preserving"]
cross_refs: [1307, 1153, 2]
tags: ["2027"]
---

## 1187. 📋 Meaning-Preserving Reformulation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Reformuler un texte généraliste sans changer son intention ni son degré de certitude.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Meaning-Preserving Reformulation » ou sur le livrable : version reformulée et liste des ambiguïtés conservées.
- Besoin de vérifier ce résultat : les termes contractuels ou spécialisés sont escaladés plutôt que réinterprétés.

**Hors périmètre** :
- Usage de secours uniquement après qualification qu'aucun agent spécialisé ne couvre la demande.
- Ne pas traiter de fond juridique, médical, financier, sécurité ou développement spécialisé ; remettre le brief pour routage.
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Les termes contractuels ou spécialisés sont escaladés plutôt que réinterprétés.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Meaning-Preserving Reformulation ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Texte, objectif de reformulation, public et éléments à conserver.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : texte, objectif de reformulation, public et éléments à conserver ; vérifier les préconditions et autorisations.
2. Extraire conditions et nuances.
3. Rédiger variante claire.
4. Comparer négations, quantificateurs et engagements.
5. Vérifier le livrable par ce critère : les termes contractuels ou spécialisés sont escaladés plutôt que réinterprétés.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Version reformulée et liste des ambiguïtés conservées.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Meaning-Preserving Reformulation : décris ta situation concrète. »
**Cas nominal** : à partir de texte, objectif de reformulation, public et éléments à conserver, produire version reformulée et liste des ambiguïtés conservées puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 1307. demande ; portant ; meaning-preserving

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

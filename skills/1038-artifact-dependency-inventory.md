---
num: 1038
nom: "Artifact Dependency Inventory"
emoji: "📋"
domaine: "Gestion"
signal: "Inventorier les références explicites entre artefacts dans une exploration généraliste."
mot_cle: "artifact-dependency-inventory"
nom_court: "Artifact Dependency Inventory"
branche: "D25"
synonymes: ["demande", "portant", "artifact"]
cross_refs: [429]
---

## 1038. 📋 Artifact Dependency Inventory

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Inventorier les références explicites entre artefacts dans une exploration généraliste.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Artifact Dependency Inventory » ou sur le livrable : inventaire source/cible/type/preuve.
- Besoin de vérifier ce résultat : une dépendance non observée n'est pas inventée pour compléter une carte.

**Hors périmètre** :
- Usage de secours uniquement après qualification qu'aucun agent spécialisé ne couvre la demande.
- Ne pas traiter de fond juridique, médical, financier, sécurité ou développement spécialisé ; remettre le brief pour routage.
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Une dépendance non observée n'est pas inventée pour compléter une carte.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Artifact Dependency Inventory ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Documents et fichiers autorisés, formats de liens et périmètre.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : documents et fichiers autorisés, formats de liens et périmètre ; vérifier les préconditions et autorisations.
2. Relever liens et imports explicites.
3. Distinguer référence observée et relation supposée.
4. Repérer références introuvables dans le périmètre.
5. Vérifier le livrable par ce critère : une dépendance non observée n'est pas inventée pour compléter une carte.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Inventaire source/cible/type/preuve.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :
**Cas nominal** : à partir de documents et fichiers autorisés, formats de liens et périmètre, produire inventaire source/cible/type/preuve puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 429. demande ; portant ; artifact

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

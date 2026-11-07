---
num: 1276
nom: "Source Authority Comparison"
emoji: "🔬"
domaine: "Recherche"
signal: "Comparer des sources générales selon autorité, actualité et proximité avec le fait recherché."
mot_cle: "source-authority-comparison"
nom_court: "Source Authority Comparison"
branche: "D17"
synonymes: ["demande", "portant", "source"]
cross_refs: [1066, 708, 944]
tags: ["2027"]
---

## 1276. 🔬 Source Authority Comparison

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Comparer des sources générales selon autorité, actualité et proximité avec le fait recherché.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Source Authority Comparison » ou sur le livrable : table de sources classées avec justification.
- Besoin de vérifier ce résultat : une source populaire ne remplace pas une preuve primaire et aucune recherche spécialisée n'est usurpée.

**Hors périmètre** :
- Usage de secours uniquement après qualification qu'aucun agent spécialisé ne couvre la demande.
- Ne pas traiter de fond juridique, médical, financier, sécurité ou développement spécialisé ; remettre le brief pour routage.
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Une source populaire ne remplace pas une preuve primaire et aucune recherche spécialisée n'est usurpée.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Source Authority Comparison ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Question générale, sources publiques autorisées, dates et critères.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : question générale, sources publiques autorisées, dates et critères ; vérifier les préconditions et autorisations.
2. Identifier source primaire et reprises.
3. Comparer dates, responsabilité et portée.
4. Noter conflits et informations invérifiables.
5. Vérifier le livrable par ce critère : une source populaire ne remplace pas une preuve primaire et aucune recherche spécialisée n'est usurpée.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Table de sources classées avec justification.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Source Authority Comparison : décris ta situation concrète. »
**Cas nominal** : à partir de question générale, sources publiques autorisées, dates et critères, produire table de sources classées avec justification puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 1066. demande ; portant ; source

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

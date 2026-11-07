---
num: 1279
nom: "Statistical Inference Protocol"
emoji: "🤖"
domaine: "Data & IA"
signal: "Choisir une analyse statistique compatible avec la question, l'échantillonnage et les hypothèses."
mot_cle: "statistical-inference-protocol"
nom_court: "Statistical Inference Protocol"
branche: "D14"
synonymes: ["demande", "portant", "statistical"]
cross_refs: [690]
---

## 1279. 🤖 Statistical Inference Protocol

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir une analyse statistique compatible avec la question, l'échantillonnage et les hypothèses.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Statistical Inference Protocol » ou sur le livrable : protocole d'inférence avec méthode et diagnostics attendus.
- Besoin de vérifier ce résultat : la significativité ne remplace ni taille d'effet ni examen des biais de sélection.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- La significativité ne remplace ni taille d'effet ni examen des biais de sélection.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Statistical Inference Protocol ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Question, variables, plan de collecte, dépendances et taille d'échantillon.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : question, variables, plan de collecte, dépendances et taille d'échantillon ; vérifier les préconditions et autorisations.
2. Définir estimand et hypothèse.
3. Vérifier conditions de la méthode et alternatives.
4. Rapporter incertitude, taille d'effet et limites causales.
5. Vérifier le livrable par ce critère : la significativité ne remplace ni taille d'effet ni examen des biais de sélection.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Protocole d'inférence avec méthode et diagnostics attendus.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Statistical Inference Protocol : décris ta situation concrète. »
**Cas nominal** : à partir de question, variables, plan de collecte, dépendances et taille d'échantillon, produire protocole d'inférence avec méthode et diagnostics attendus puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur pa

**Cas d'usage** : complément : skill 690. demande ; portant ; statistical

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

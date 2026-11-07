---
num: 1176
nom: "Language Correction Regression Suite"
emoji: "🎨"
domaine: "Design"
signal: "Empêcher qu'une nouvelle révision réintroduise des fautes déjà corrigées."
mot_cle: "language-correction-regression-suite"
nom_court: "Language Correction Regression"
branche: "D22"
synonymes: ["demande", "portant", "language"]
cross_refs: [1153]
tags: ["2027"]
---

## 1176. 🎨 Language Correction Regression Suite

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Empêcher qu'une nouvelle révision réintroduise des fautes déjà corrigées.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Language Correction Regression Suite » ou sur le livrable : jeu de cas phrase/règle/attendu avec rapport de régression.
- Besoin de vérifier ce résultat : chaque échec renvoie à une règle linguistique et une occurrence vérifiable.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Chaque échec renvoie à une règle linguistique et une occurrence vérifiable.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Language Correction Regression Suite ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Texte de référence, corrections validées, version nouvelle.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : texte de référence, corrections validées, version nouvelle ; vérifier les préconditions et autorisations.
2. Créer des cas minimaux pour les fautes récurrentes.
3. Comparer les occurrences nouvelles aux corrections validées.
4. Isoler faux positifs et exceptions linguistiques.
5. Vérifier le livrable par ce critère : chaque échec renvoie à une règle linguistique et une occurrence vérifiable.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Jeu de cas phrase/règle/attendu avec rapport de régression.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Language Correction Regression Suite : décris ta situation concrète. »
**Cas nominal** : à partir de texte de référence, corrections validées, version nouvelle, produire jeu de cas phrase/règle/attendu avec rapport de régression puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 1153. demande ; portant ; language

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

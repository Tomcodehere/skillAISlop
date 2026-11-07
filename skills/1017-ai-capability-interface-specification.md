---
num: 1017
nom: "AI Capability Interface Specification"
emoji: "🎨"
domaine: "Design"
signal: "Spécifier le contrat d'une capacité IA exposée au reste du système."
mot_cle: "ai-capability-interface-specification"
nom_court: "AI Capability Interface Specif"
branche: "D22"
synonymes: ["demande", "portant", "capability"]
cross_refs: [1028]
---

## 1017. 🎨 AI Capability Interface Specification

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Spécifier le contrat d'une capacité IA exposée au reste du système.

**Quand l'utiliser (triggers)** :
- Demande portant sur « AI Capability Interface Specification » ou sur le livrable : contrat de capacité ia avec exemples et cas d'échec.
- Besoin de vérifier ce résultat : une sortie invalide ou incertaine ne peut pas être interprétée comme une réussite normale.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Une sortie invalide ou incertaine ne peut pas être interprétée comme une réussite normale.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « AI Capability Interface Specification ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Entrées, sorties, contraintes, erreurs et exigences de supervision.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : entrées, sorties, contraintes, erreurs et exigences de supervision ; vérifier les préconditions et autorisations.
2. Définir schémas et garanties limitées.
3. Expliciter abstention, erreurs et états intermédiaires.
4. Décrire validation des sorties avant consommation.
5. Vérifier le livrable par ce critère : une sortie invalide ou incertaine ne peut pas être interprétée comme une réussite normale.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Contrat de capacité IA avec exemples et cas d'échec.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « AI Capability Interface Specification : décris ta situation concrète. »
**Cas nominal** : à partir de entrées, sorties, contraintes, erreurs et exigences de supervision, produire contrat de capacité ia avec exemples et cas d'échec puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 1028. demande ; portant ; capability

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

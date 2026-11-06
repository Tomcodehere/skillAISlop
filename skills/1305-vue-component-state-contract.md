---
num: 1305
nom: "Vue Component State Contract"
emoji: "💻"
domaine: "Développement"
signal: "Définir l'interface et le cycle de vie d'un composant Vue sans état implicite incontrôlé."
mot_cle: "vue-component-state-contract"
nom_court: "Vue Component State Contract"
branche: "D1"
synonymes: ["demande", "portant", "component"]
cross_refs: [809]
---

## 1305. 💻 Vue Component State Contract

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir l'interface et le cycle de vie d'un composant Vue sans état implicite incontrôlé.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Vue Component State Contract » ou sur le livrable : composant ou contrat props/events avec scénarios de transition.
- Besoin de vérifier ce résultat : les props ne sont pas mutées et chaque transition observable possède un résultat attendu.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Les props ne sont pas mutées et chaque transition observable possède un résultat attendu.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Vue Component State Contract ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Props, événements, états UI, contraintes d'accessibilité et composition.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : props, événements, états ui, contraintes d'accessibilité et composition ; vérifier les préconditions et autorisations.
2. Distinguer état possédé et dérivé.
3. Définir mutations et émissions.
4. Prévoir chargement, erreur, destruction et réutilisation.
5. Vérifier le livrable par ce critère : les props ne sont pas mutées et chaque transition observable possède un résultat attendu.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Composant ou contrat props/events avec scénarios de transition.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :
**Cas nominal** : à partir de props, événements, états ui, contraintes d'accessibilité et composition, produire composant ou contrat props/events avec scénarios de transition puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur p

**Cas d'usage** : complément : skill 809. demande ; portant ; component

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

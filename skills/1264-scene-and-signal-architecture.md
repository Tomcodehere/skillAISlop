---
num: 1264
nom: "Scene and Signal Architecture"
emoji: "💻"
domaine: "Développement"
signal: "Structurer les responsabilités de scènes Godot et leurs communications par signaux."
mot_cle: "scene-and-signal-architecture"
nom_court: "Scene and Signal Architecture"
branche: "D1"
synonymes: ["demande", "portant", "scene"]
cross_refs: [10]
---

## 1264. 💻 Scene and Signal Architecture

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Structurer les responsabilités de scènes Godot et leurs communications par signaux.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Scene and Signal Architecture » ou sur le livrable : schéma scènes/signaux avec scripts et scénarios de cycle de vie.
- Besoin de vérifier ce résultat : une scène supprimée ne laisse pas une interaction attendue avec un nœud invalide.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Une scène supprimée ne laisse pas une interaction attendue avec un nœud invalide.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Scene and Signal Architecture ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Arbre de scènes, interactions gameplay et cycle de vie des nœuds.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : arbre de scènes, interactions gameplay et cycle de vie des nœuds ; vérifier les préconditions et autorisations.
2. Définir émetteurs, récepteurs et responsabilités.
3. Vérifier connexions et désabonnements.
4. Prévoir instanciation répétée et libération des nœuds.
5. Vérifier le livrable par ce critère : une scène supprimée ne laisse pas une interaction attendue avec un nœud invalide.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Schéma scènes/signaux avec scripts et scénarios de cycle de vie.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :
**Cas nominal** : à partir de arbre de scènes, interactions gameplay et cycle de vie des nœuds, produire schéma scènes/signaux avec scripts et scénarios de cycle de vie puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par déf

**Cas d'usage** : complément : skill 10. demande ; portant ; scene

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

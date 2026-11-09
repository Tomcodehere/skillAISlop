---
num: 1050
resume: "Produire un livrable maîtrisé : export glTF 2.0 (ou FBX si justifié) avec paramètres, checklist et test d'import. Étape 1 : Cadrer les inputs : scène Blender, moteur cible et version, conventions de nommage, besoins d'animation ; vérifier les préconditions et autorisations."
date_ajout: "2026-11"
nom: "Blender Game-Ready Export Pipeline"
emoji: "💻"
domaine: "Développement"
signal: "Produire un livrable maîtrisé : export glTF 2.0 (ou FBX si justifié) avec paramètres, checklist et test d'import."
mot_cle: "blender-game-ready-export-pipeline"
nom_court: "Blender Game-Ready Export Pipe"
branche: "D1"
synonymes: ["demande", "portant", "blender"]
cross_refs: [1202, 1167, 1224]
tags: ["2027"]
depends_on: [1167]
---

## 1050. 💻 Blender Game-Ready Export Pipeline

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Produire un livrable maîtrisé : export glTF 2.0 (ou FBX si justifié) avec paramètres, checklist et test d'import.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Blender Game-Ready Export Pipeline » ou sur le livrable : export glTF 2.0 (ou FBX si justifié) avec paramètres, checklist et test d'import.
- Besoin de vérifier ce résultat : l'asset exporté s'importe dans le moteur cible avec échelle, orientation et matériaux conformes.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle dans le logiciel.

**Garde-fous** :
- L'asset exporté s'importe dans le moteur cible avec échelle, orientation et matériaux conformes.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Utiliser uniquement des ressources originales, du Domaine Public ou CC0 ; tracer chaque source externe dans `docs/imageLicencesSources.md` (format `Nomdefichier | licence | url source`).
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Blender Game-Ready Export Pipeline ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Scène Blender, moteur cible et version, conventions de nommage, besoins d'animation.
- Périmètre autorisé, version des logiciels et des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : scène Blender, moteur cible et version, conventions de nommage, besoins d'animation ; vérifier les préconditions et autorisations.
2. Nettoyer la scène (hiérarchie, pivots, échelle, noms).
3. Régler les options d'export glTF et les matériaux.
4. Tester l'import dans le moteur cible et corriger les écarts.
5. Vérifier le livrable par ce critère : l'asset exporté s'importe dans le moteur cible avec échelle, orientation et matériaux conformes.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Export glTF 2.0 (ou FBX si justifié) avec paramètres, checklist et test d'import.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Blender Game-Ready Export Pipeline : décris ta situation concrète. »
**Cas nominal** : à partir de scène Blender, moteur cible et version, conventions de nommage, besoins d'animation, produire export glTF 2.0 (ou FBX si justifié) avec paramètres, checklist et test d'import puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation

**Cas d'usage** : complément : skill 1202. demande ; portant ; blender

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

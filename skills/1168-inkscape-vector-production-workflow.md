---
num: 1168
resume: "Produire un livrable maîtrisé : fichier SVG structuré (calques, groupes, identifiants) avec guide de manipulation Inkscape. Étape 1 : Cadrer les inputs : brief visuel, formats cibles, palette, contraintes de taille et références libres de droits ; vérifier les préconditions et autorisations."
lang: "fr"
date_ajout: "2026-11"
nom: "Inkscape Vector Production Workflow"
emoji: "🎨"
domaine: "Design"
signal: "Produire un livrable maîtrisé : fichier SVG structuré (calques, groupes, identifiants) avec guide de manipulation Inkscape."
mot_cle: "inkscape-vector-production-workflow"
nom_court: "Inkscape Vector Production Wor"
branche: "D22"
synonymes: ["demande", "portant", "inkscape"]
cross_refs: [454, 1148, 1174]
tags: ["2027"]
depends_on: [1148]
---

## 1168. 🎨 Inkscape Vector Production Workflow

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Produire un livrable maîtrisé : fichier SVG structuré (calques, groupes, identifiants) avec guide de manipulation Inkscape.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Inkscape Vector Production Workflow » ou sur le livrable : fichier SVG structuré (calques, groupes, identifiants) avec guide de manipulation Inkscape.
- Besoin de vérifier ce résultat : le SVG s'ouvre dans Inkscape stable avec des calques nommés et sans objet caché non documenté.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle dans le logiciel.

**Garde-fous** :
- Le SVG s'ouvre dans Inkscape stable avec des calques nommés et sans objet caché non documenté.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Utiliser uniquement des ressources originales, du Domaine Public ou CC0 ; tracer chaque source externe dans `docs/imageLicencesSources.md` (format `Nomdefichier | licence | url source`).
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Inkscape Vector Production Workflow ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Brief visuel, formats cibles, palette, contraintes de taille et références libres de droits.
- Périmètre autorisé, version des logiciels et des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : brief visuel, formats cibles, palette, contraintes de taille et références libres de droits ; vérifier les préconditions et autorisations.
2. Construire la structure calques/groupes et nommer les objets.
3. Tracer et combiner les chemins (opérations booléennes, nœuds, vectorisation d'un bitmap si nécessaire).
4. Appliquer couleurs, dégradés et traits en conservant l'éditabilité.
5. Vérifier le livrable par ce critère : le SVG s'ouvre dans Inkscape stable avec des calques nommés et sans objet caché non documenté.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Fichier SVG structuré (calques, groupes, identifiants) avec guide de manipulation Inkscape.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Inkscape Vector Production Workflow : décris ta situation concrète. »
**Cas nominal** : à partir de brief visuel, formats cibles, palette, contraintes de taille et références libres de droits, produire fichier SVG structuré (calques, groupes, identifiants) avec guide de manipulation Inkscape puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui emp

**Cas d'usage** : complément : skill 454. demande ; portant ; inkscape

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

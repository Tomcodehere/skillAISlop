---
num: 1166
nom: "Inkscape Icon & Logo System Design"
emoji: "💻"
domaine: "Développement"
signal: "Produire un livrable maîtrisé : système d'icônes ou de logo (grille, déclinaisons, variantes de taille et de couleur)."
mot_cle: "inkscape-icon-logo-system-design"
nom_court: "Inkscape Icon & Logo System De"
branche: "D1"
synonymes: ["demande", "portant", "inkscape"]
cross_refs: [783, 1167, 1149]
tags: ["2027"]
depends_on: [1167]
---

## 1166. 💻 Inkscape Icon & Logo System Design

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Produire un livrable maîtrisé : système d'icônes ou de logo (grille, déclinaisons, variantes de taille et de couleur).

**Quand l'utiliser (triggers)** :
- Demande portant sur « Inkscape Icon & Logo System Design » ou sur le livrable : système d'icônes ou de logo (grille, déclinaisons, variantes de taille et de couleur).
- Besoin de vérifier ce résultat : chaque icône respecte la grille déclarée et reste lisible à la taille minimale annoncée.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle dans le logiciel.

**Garde-fous** :
- Chaque icône respecte la grille déclarée et reste lisible à la taille minimale annoncée.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Utiliser uniquement des ressources originales, du Domaine Public ou CC0 ; tracer chaque source externe dans `docs/imageLicencesSources.md` (format `Nomdefichier | licence | url source`).
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Inkscape Icon & Logo System Design ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Identité visuelle, usages, tailles minimales, contraintes d'accessibilité et de contraste.
- Périmètre autorisé, version des logiciels et des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : identité visuelle, usages, tailles minimales, contraintes d'accessibilité et de contraste ; vérifier les préconditions et autorisations.
2. Définir la grille, l'épaisseur de trait et les règles de construction.
3. Décliner les variantes (monochrome, couleur, fond clair/sombre).
4. Vérifier la lisibilité aux tailles minimales.
5. Vérifier le livrable par ce critère : chaque icône respecte la grille déclarée et reste lisible à la taille minimale annoncée.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Système d'icônes ou de logo (grille, déclinaisons, variantes de taille et de couleur).
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Inkscape Icon & Logo System Design : décris ta situation concrète. »
**Cas nominal** : à partir de identité visuelle, usages, tailles minimales, contraintes d'accessibilité et de contraste, produire système d'icônes ou de logo (grille, déclinaisons, variantes de taille et de couleur) puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la

**Cas d'usage** : complément : skill 783. demande ; portant ; inkscape

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

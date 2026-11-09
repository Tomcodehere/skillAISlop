---
num: 1190
resume: "Définir un standard de métadonnées et de classification exploitable par les responsables de domaine. Étape 1 : Cadrer les inputs : jeux de données, catégories de sensibilité, usages et vocabulaire ; vérifier les préconditions et autorisations."
lang: "fr"
date_ajout: "2026-11"
nom: "Metadata Classification Policy"
emoji: "🤖"
domaine: "Data & IA"
signal: "Définir un standard de métadonnées et de classification exploitable par les responsables de domaine."
mot_cle: "metadata-classification-policy"
nom_court: "Metadata Classification Policy"
branche: "D14"
synonymes: ["demande", "portant", "metadata"]
cross_refs: [1234, 1100, 1101]
tags: ["2027"]
depends_on: [1100]
---

## 1190. 🤖 Metadata Classification Policy

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir un standard de métadonnées et de classification exploitable par les responsables de domaine.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Metadata Classification Policy » ou sur le livrable : politique de classification avec dictionnaire de métadonnées.
- Besoin de vérifier ce résultat : les catégories ambiguës sont escaladées plutôt que devinées à partir d'un nom de colonne.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Les catégories ambiguës sont escaladées plutôt que devinées à partir d'un nom de colonne.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Metadata Classification Policy ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Jeux de données, catégories de sensibilité, usages et vocabulaire.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : jeux de données, catégories de sensibilité, usages et vocabulaire ; vérifier les préconditions et autorisations.
2. Choisir champs obligatoires et valeurs autorisées.
3. Relier sensibilité, finalité et règles d'accès.
4. Définir contrôle de complétude et cycle de révision.
5. Vérifier le livrable par ce critère : les catégories ambiguës sont escaladées plutôt que devinées à partir d'un nom de colonne.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Politique de classification avec dictionnaire de métadonnées.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Metadata Classification Policy : décris ta situation concrète. »
**Cas nominal** : à partir de jeux de données, catégories de sensibilité, usages et vocabulaire, produire politique de classification avec dictionnaire de métadonnées puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défau

**Cas d'usage** : complément : skill 1234. demande ; portant ; metadata

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

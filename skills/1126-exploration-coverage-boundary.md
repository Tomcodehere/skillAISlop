---
num: 1126
nom: "Exploration Coverage Boundary"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Rendre visible ce qui a été et n'a pas été examiné lors d'une cartographie."
mot_cle: "exploration-coverage-boundary"
nom_court: "Exploration Coverage Boundary"
branche: "D14"
synonymes: ["demande", "portant", "exploration"]
cross_refs: [601]
---

## 1126. 🧠 Exploration Coverage Boundary

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre visible ce qui a été et n'a pas été examiné lors d'une cartographie.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Exploration Coverage Boundary » ou sur le livrable : matrice périmètre/méthode/couverture/limites.
- Besoin de vérifier ce résultat : aucune exploration partielle n'est présentée comme audit exhaustif.

**Hors périmètre** :
- Usage de secours uniquement après qualification qu'aucun agent spécialisé ne couvre la demande.
- Ne pas traiter de fond juridique, médical, financier, sécurité ou développement spécialisé ; remettre le brief pour routage.
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Aucune exploration partielle n'est présentée comme audit exhaustif.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Exploration Coverage Boundary ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Question, fichiers autorisés, exclusions et observations.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : question, fichiers autorisés, exclusions et observations ; vérifier les préconditions et autorisations.
2. Définir critères de sélection.
3. Tracer zones lues, échantillonnées et non lues.
4. Limiter les conclusions à l'évidence disponible.
5. Vérifier le livrable par ce critère : aucune exploration partielle n'est présentée comme audit exhaustif.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Matrice périmètre/méthode/couverture/limites.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :
**Cas nominal** : à partir de question, fichiers autorisés, exclusions et observations, produire matrice périmètre/méthode/couverture/limites puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 601. demande ; portant ; exploration

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

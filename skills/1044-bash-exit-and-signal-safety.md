---
num: 1044
resume: "Fiabiliser propagation des erreurs, nettoyage et arrêt d'un script Bash. Étape 1 : Cadrer les inputs : script, effets de bord, codes de sortie et signaux attendus ; vérifier les préconditions et autorisations."
lang: "fr"
date_ajout: "2026-11"
nom: "Bash Exit and Signal Safety"
emoji: "💻"
domaine: "Développement"
signal: "Fiabiliser propagation des erreurs, nettoyage et arrêt d'un script Bash."
mot_cle: "bash-exit-and-signal-safety"
nom_court: "Bash Exit and Signal Safety"
branche: "D1"
synonymes: ["demande", "portant", "signal"]
cross_refs: [1183, 9, 1264]
tags: ["2027"]
---

## 1044. 💻 Bash Exit and Signal Safety

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Fiabiliser propagation des erreurs, nettoyage et arrêt d'un script Bash.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Bash Exit and Signal Safety » ou sur le livrable : script ou revue avec contrat des codes de sortie et matrice de signaux.
- Besoin de vérifier ce résultat : une erreur d'étape ne se transforme pas en code de succès final.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Une erreur d'étape ne se transforme pas en code de succès final.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Bash Exit and Signal Safety ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Script, effets de bord, codes de sortie et signaux attendus.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : script, effets de bord, codes de sortie et signaux attendus ; vérifier les préconditions et autorisations.
2. Examiner pipelines et substitutions.
3. Définir traps et nettoyage idempotent.
4. Préparer tests d'échec, d'interruption et d'expansion des chemins.
5. Vérifier le livrable par ce critère : une erreur d'étape ne se transforme pas en code de succès final.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Script ou revue avec contrat des codes de sortie et matrice de signaux.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Bash Exit and Signal Safety : décris ta situation concrète. »
**Cas nominal** : à partir de script, effets de bord, codes de sortie et signaux attendus, produire script ou revue avec contrat des codes de sortie et matrice de signaux puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par d

**Cas d'usage** : complément : skill 1183. demande ; portant ; signal

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

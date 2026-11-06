---
num: 1298
nom: "Utility Execution Evidence"
emoji: "🔬"
domaine: "Recherche"
signal: "Préparer les preuves minimales de réussite d'un utilitaire ponctuel exécuté par l'agent de coordination."
mot_cle: "utility-execution-evidence"
nom_court: "Utility Execution Evidence"
branche: "D17"
synonymes: ["demande", "portant", "utility"]
cross_refs: [1185]
---

## 1298. 🔬 Utility Execution Evidence

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Préparer les preuves minimales de réussite d'un utilitaire ponctuel exécuté par l'agent de coordination.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Utility Execution Evidence » ou sur le livrable : checklist de vérification et rapport d'écarts.
- Besoin de vérifier ce résultat : un code zéro sans sortie conforme ne suffit pas à déclarer la tâche réussie.

**Hors périmètre** :
- Usage de secours uniquement après qualification qu'aucun agent spécialisé ne couvre la demande.
- Ne pas traiter de fond juridique, médical, financier, sécurité ou développement spécialisé ; remettre le brief pour routage.
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Un code zéro sans sortie conforme ne suffit pas à déclarer la tâche réussie.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Utility Execution Evidence ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Commande proposée, entrées connues, sortie attendue et critères.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : commande proposée, entrées connues, sortie attendue et critères ; vérifier les préconditions et autorisations.
2. Définir vérifications indépendantes du code retour.
3. Prévoir échec et artefacts temporaires.
4. Relier rapport reçu aux critères de succès.
5. Vérifier le livrable par ce critère : un code zéro sans sortie conforme ne suffit pas à déclarer la tâche réussie.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Checklist de vérification et rapport d'écarts.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :
**Cas nominal** : à partir de commande proposée, entrées connues, sortie attendue et critères, produire checklist de vérification et rapport d'écarts puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 1185. demande ; portant ; utility

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

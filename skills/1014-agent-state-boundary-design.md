---
num: 1014
resume: "Définir quelles données d'état un agent peut lire, modifier et transmettre dans un système multi-agents. Étape 1 : Cadrer les inputs : rôles, états, messages, permissions et exigences d'isolation ; vérifier les préconditions et autorisations."
lang: "fr"
date_ajout: "2026-11"
nom: "Agent State Boundary Design"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Définir quelles données d'état un agent peut lire, modifier et transmettre dans un système multi-agents."
mot_cle: "agent-state-boundary-design"
nom_court: "Agent State Boundary Design"
branche: "D14"
synonymes: ["demande", "portant", "state"]
cross_refs: [338, 335, 330]
tags: ["2027"]
depends_on: [335]
---

## 1014. 🧠 Agent State Boundary Design

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Définir quelles données d'état un agent peut lire, modifier et transmettre dans un système multi-agents.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Agent State Boundary Design » ou sur le livrable : modèle d'état et matrice de droits par agent.
- Besoin de vérifier ce résultat : aucune transition ne dépend d'une instruction non fiable comme autorisation.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Aucune transition ne dépend d'une instruction non fiable comme autorisation.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Agent State Boundary Design ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Rôles, états, messages, permissions et exigences d'isolation.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : rôles, états, messages, permissions et exigences d'isolation ; vérifier les préconditions et autorisations.
2. Distinguer mémoire locale, état partagé et données externes.
3. Définir transitions autorisées et propriétaire.
4. Décrire contrôle des entrées et reprise après interruption.
5. Vérifier le livrable par ce critère : aucune transition ne dépend d'une instruction non fiable comme autorisation.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Modèle d'état et matrice de droits par agent.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Agent State Boundary Design : décris ta situation concrète. »
**Cas nominal** : à partir de rôles, états, messages, permissions et exigences d'isolation, produire modèle d'état et matrice de droits par agent puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 338. demande ; portant ; state

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

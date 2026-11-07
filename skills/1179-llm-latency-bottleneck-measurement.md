---
num: 1179
nom: "LLM Latency Bottleneck Measurement"
emoji: "🧠"
domaine: "IA / Prompting"
signal: "Localiser les causes d'une latence IA excessive avant de recommander une optimisation."
mot_cle: "llm-latency-bottleneck-measurement"
nom_court: "LLM Latency Bottleneck Measure"
branche: "D14"
synonymes: ["demande", "portant", "latency"]
cross_refs: [737, 309, 1241]
tags: ["2027"]
---

## 1179. 🧠 LLM Latency Bottleneck Measurement

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Localiser les causes d'une latence IA excessive avant de recommander une optimisation.

**Quand l'utiliser (triggers)** :
- Demande portant sur « LLM Latency Bottleneck Measurement » ou sur le livrable : profil de latence avec goulet et protocole de comparaison.
- Besoin de vérifier ce résultat : les chiffres de gain utilisent la même charge et des fenêtres comparables.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Les chiffres de gain utilisent la même charge et des fenêtres comparables.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « LLM Latency Bottleneck Measurement ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Traces horodatées, volumes, concurrence et objectifs de latence.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : traces horodatées, volumes, concurrence et objectifs de latence ; vérifier les préconditions et autorisations.
2. Séparer attente, prétraitement, premier token et génération.
3. Comparer distributions plutôt que seule moyenne.
4. Mesurer le gain sous charge comparable.
5. Vérifier le livrable par ce critère : les chiffres de gain utilisent la même charge et des fenêtres comparables.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Profil de latence avec goulet et protocole de comparaison.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « LLM Latency Bottleneck Measurement : décris ta situation concrète. »
**Cas nominal** : à partir de traces horodatées, volumes, concurrence et objectifs de latence, produire profil de latence avec goulet et protocole de comparaison puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 737. demande ; portant ; latency

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

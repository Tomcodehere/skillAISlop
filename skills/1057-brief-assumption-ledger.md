---
num: 1057
date_ajout: "2026-11"
nom: "Brief Assumption Ledger"
emoji: "🎨"
domaine: "Design"
signal: "Rendre explicites les hypothèses qui conditionnent un brief avant la décision de routage de l'agent de coordination."
mot_cle: "brief-assumption-ledger"
nom_court: "Brief Assumption Ledger"
branche: "D22"
synonymes: ["demande", "portant", "brief"]
cross_refs: [454, 1252, 1302]
tags: ["2027"]
depends_on: [1252]
---

## 1057. 🎨 Brief Assumption Ledger

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre explicites les hypothèses qui conditionnent un brief avant la décision de routage de l'agent de coordination.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Brief Assumption Ledger » ou sur le livrable : registre hypothèse/preuve/impact/décision attendue.
- Besoin de vérifier ce résultat : aucune hypothèse bloquante ne figure comme fait acquis.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Aucune hypothèse bloquante ne figure comme fait acquis.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Brief Assumption Ledger ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Brief, décisions attendues, faits établis, inconnues.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : brief, décisions attendues, faits établis, inconnues ; vérifier les préconditions et autorisations.
2. Extraire les prémisses non prouvées.
3. Relier chaque prémisse à la décision affectée.
4. Proposer la preuve ou clarification minimale nécessaire.
5. Vérifier le livrable par ce critère : aucune hypothèse bloquante ne figure comme fait acquis.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Registre hypothèse/preuve/impact/décision attendue.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Brief Assumption Ledger : décris ta situation concrète. »
**Cas nominal** : à partir de brief, décisions attendues, faits établis, inconnues, produire registre hypothèse/preuve/impact/décision attendue puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une valeur par défaut.

**Cas d'usage** : complément : skill 454. demande ; portant ; brief

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

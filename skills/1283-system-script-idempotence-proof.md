---
num: 1283
nom: "System Script Idempotence Proof"
emoji: "💻"
domaine: "Développement"
signal: "Démontrer qu'un script système peut être rejoué sans appliquer deux fois un changement."
mot_cle: "system-script-idempotence-proof"
nom_court: "System Script Idempotence Proo"
branche: "D1"
synonymes: ["demande", "portant", "script"]
cross_refs: [256]
---

## 1283. 💻 System Script Idempotence Proof

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Démontrer qu'un script système peut être rejoué sans appliquer deux fois un changement.

**Quand l'utiliser (triggers)** :
- Demande portant sur « System Script Idempotence Proof » ou sur le livrable : matrice avant/après/rejeu avec preuves d'absence d'effet supplémentaire.
- Besoin de vérifier ce résultat : le deuxième passage ne duplique ni ressources ni lignes de configuration.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas confondre préparation d'un protocole, revue statique et résultat d'une exécution réelle.

**Garde-fous** :
- Le deuxième passage ne duplique ni ressources ni lignes de configuration.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles.
- Privilégier les outils libres maintenus et vérifier les versions applicables sans introduire de dépendance EOL.
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « System Script Idempotence Proof ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- État initial, état cible, effets externes et interruptions possibles.
- Périmètre autorisé, version des artefacts, sources accessibles et décisions déjà validées.
- Critères d'acceptation et limites d'action ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les inputs : état initial, état cible, effets externes et interruptions possibles ; vérifier les préconditions et autorisations.
2. Définir observation de l'état courant.
3. Séparer création, mise à jour et absence de changement.
4. Préparer premier passage, rejeu et reprise partielle.
5. Vérifier le livrable par ce critère : le deuxième passage ne duplique ni ressources ni lignes de configuration.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages.

**Sorties attendues** :
- Matrice avant/après/rejeu avec preuves d'absence d'effet supplémentaire.
- Preuves ou références par constat ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « System Script Idempotence Proof : décris ta situation concrète. »
**Cas nominal** : à partir de état initial, état cible, effets externes et interruptions possibles, produire matrice avant/après/rejeu avec preuves d'absence d'effet supplémentaire puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une preuve ou autorisation nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans substituer une va

**Cas d'usage** : complément : skill 256. demande ; portant ; script

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

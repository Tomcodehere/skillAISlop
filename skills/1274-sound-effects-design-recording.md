---
num: 1274
date_ajout: "2026-11"
nom: "Sound Effects Design & Recording"
emoji: "🎨"
domaine: "Design"
signal: "Produire un livrable maîtrisé : bibliothèque d'effets sonores (SFX et foley) originaux, enregistrés, synthétisés ou issus du Domaine Public/CC0, nettoyés, nommés et prêts à être mixés."
mot_cle: "sound-effects-design-recording"
nom_court: "Sound Effects Design & Recordi"
branche: "D22"
synonymes: ["demande", "portant", "sound"]
cross_refs: [1070, 1137, 1135]
tags: ["2027"]
depends_on: [1137]
---

## 1274. 🎨 Sound Effects Design & Recording

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Produire un livrable maîtrisé : bibliothèque d'effets sonores (SFX et foley) originaux, enregistrés, synthétisés ou issus du Domaine Public/CC0, nettoyés, nommés et prêts à être mixés.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Sound Effects Design & Recording » ou sur le livrable : bibliothèque d'effets sonores (SFX et foley) originaux, enregistrés, synthétisés ou issus du Domaine Public/CC0, nettoyés, nommés et prêts à être mixés.
- Besoin de vérifier ce résultat : chaque son de la liste de besoins est livré en WAV propre (sans clic ni écrêtage), nommé selon la convention et associé à une source tracée.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas composer de musique (→ l'agent de composition musicale) ni écrire le code audio du moteur (→ l'agent de développement Godot).
- Ne pas confondre préparation d'un protocole d'enregistrement, revue statique et résultat d'une écoute ou d'une exécution réelle dans le logiciel.

**Garde-fous** :
- Chaque son de la liste est livré en WAV propre (sans clic ni écrêtage), nommé selon la convention et associé à une source tracée.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; minimiser les données sensibles (voix enregistrées comprises).
- Privilégier les outils libres maintenus (Audacity, Ardour, Sox/FFmpeg) et vérifier les versions applicables sans introduire de dépendance EOL.
- Utiliser uniquement des sons originaux, du Domaine Public ou CC0 ; tracer chaque source externe dans `docs/imageLicencesSources.md` (format `Nomdefichier | licence | url source`).
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Sound Effects Design & Recording ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Liste des événements sonores (action, matériau, durée indicative), ambiance visuelle ou narrative, plateforme cible.
- Matériel et logiciels disponibles (micro, interface, Audacity, Ardour, Sox/FFmpeg), format et fréquence d'échantillonnage attendus.
- Périmètre autorisé, sources externes envisagées et leur licence, décisions déjà validées ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer la liste de besoins : événements, matériaux, durée, intensité, nombre de variations, format cible ; vérifier préconditions et autorisations.
2. Choisir la source de chaque son : enregistrement (foley, terrain), synthèse, ou ressource Domaine Public/CC0 ; tracer toute source externe.
3. Capturer ou synthétiser avec marge de gain suffisante (pas d'écrêtage), plusieurs prises par événement.
4. Éditer : découpe, fondus courts aux bords, réduction de bruit mesurée, égalisation, superposition de couches (attaque, corps, queue).
5. Normaliser le nommage, exporter en WAV et vérifier le critère : chaque son est propre (sans clic ni écrêtage), nommé selon la convention et associé à une source tracée.
6. Restituer résultat, hypothèses, risques et prochaines actions ; signaler explicitement les blocages et ce qui n'a pas pu être écouté.

**Sorties attendues** :
- Bibliothèque de SFX (WAV non compressé, plusieurs variations par événement) avec convention de nommage et fiche de métadonnées.
- Journal des sources : origine de chaque son (enregistré, synthétisé, externe) avec licence et URL ; hypothèses, exceptions et vérifications non réalisées séparées.
- Brief des décisions ou actions nécessaires pour l'agent rattaché, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Sound Effects Design & Recording : décris ta situation concrète. »
**Cas nominal** : à partir d'une liste de 12 événements (pas sur gravier, porte, coffre, etc.), produire 3 variations WAV par événement, nommées `sfxFootstepGravel01`, avec journal des sources, puis vérifier le critère d'acceptation ci-dessus.

**Cas limite** : une licence ou une source nécessaire manque ; livrer les éléments établis et indiquer précisément ce qui empêche la validation, sans subst

**Cas d'usage** : complément : skill 1070. demande ; portant ; sound

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

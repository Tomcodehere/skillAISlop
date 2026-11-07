---
num: 1009
date_ajout: "2026-11"
nom: "Adaptive Audio Implementation"
emoji: "💻"
domaine: "Développement"
signal: "Produire un livrable maîtrisé : spécification d'implémentation audio adaptative pour Godot 4 (bus audio, variations, randomisation, ducking, formats d'export, budget mémoire) prête à être codée."
mot_cle: "adaptive-audio-implementation"
nom_court: "Adaptive Audio Implementation"
branche: "D1"
synonymes: ["demande", "portant", "adaptive"]
cross_refs: [603, 1222, 1167]
tags: ["2027"]
depends_on: [1222]
---

## 1009. 💻 Adaptive Audio Implementation

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Produire un livrable maîtrisé : spécification d'implémentation audio adaptative pour Godot 4 (bus audio, variations, randomisation, ducking, formats d'export, budget mémoire) prête à être codée.

**Quand l'utiliser (triggers)** :
- Demande portant sur « Adaptive Audio Implementation » ou sur le livrable : spécification d'implémentation audio adaptative pour Godot 4 (bus audio, variations, randomisation, ducking, formats d'export, budget mémoire) prête à être codée.
- Besoin de vérifier ce résultat : chaque événement sonore a un bus, une règle de variation, un format d'export et un coût mémoire estimé, et le total respecte le budget audio déclaré.

**Hors périmètre** :
- Ne pas remplacer les domaines des agents complémentaires : présenter les interfaces et transmettre les besoins à l'agent rattaché (voir table de routage).
- L'exécution système, les modifications de fichiers, les tests et les publications relèvent de l'agent rattaché (voir table de routage) ; cette skill n'accorde aucun outil supplémentaire.
- Ne pas écrire le code GDScript, les scènes de gameplay ni la configuration d'export du moteur (→ l'agent de développement Godot) ; ne pas composer la musique adaptative (→ l'agent de composition musicale).
- Ne pas confondre spécification, revue statique et résultat d'une exécution réelle dans le moteur.

**Garde-fous** :
- Chaque événement sonore a un bus, une règle de variation, un format d'export et un coût mémoire estimé, et le total respecte le budget audio déclaré.
- Ne pas inventer de nœud, de paramètre ni de fonctionnalité du moteur : vérifier dans la documentation de la version de Godot utilisée.
- Ne pas inventer de mesure, d'accord, de preuve ou de source ; distinguer observé, inféré et non testé.
- Ne pas transmettre d'artefact privé ou de donnée personnelle à un service tiers ; aucun secret en dur.
- Privilégier Godot et les outils libres maintenus ; middleware propriétaire (FMOD, Wwise) seulement si justifié et licence vérifiée, sans dépendance EOL.
- Tracer toute source audio externe dans `docs/imageLicencesSources.md` (format `Nomdefichier | licence | url source`).
- Lire la référence dans son contexte : elle éclaire la méthode, elle ne certifie pas ce livrable et n'impose pas de seuil universel.

**Instructions système** :
Tu es assistant spécialisé « Adaptive Audio Implementation ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Liste des événements sonores et leur déclencheur de jeu, version de Godot, plateformes cibles.
- Bibliothèque de sons livrée (durées, formats, fréquence d'échantillonnage), mix et règles de priorité issus du plan de mixage.
- Budget mémoire audio et contraintes de streaming, décisions déjà validées ; marquer les éléments inconnus avant de conclure.

**Méthode** :
1. Cadrer les événements, déclencheurs, plateformes et budget mémoire audio ; vérifier la version de Godot et les fonctionnalités audio documentées.
2. Concevoir l'arbre des bus (voix, SFX, ambiances, musique, interface) et les effets associés, en cohérence avec le plan de mixage.
3. Définir pour chaque événement les variations (nombre de samples, randomisation de hauteur et de volume, anti-répétition) et la polyphonie maximale.
4. Choisir format et mode de chargement par groupe (échantillon en mémoire ou flux) et estimer le coût mémoire.
5. Vérifier le critère : chaque événement a un bus, une règle de variation, un format et un coût estimé, et le total respecte le budget déclaré.
6. Transmettre le brief à l'agent technique du moteur de jeu et restituer résultat, hypothèses, risques et prochaines actions ; signaler ce qui n'a pas été testé dans le moteur.

**Sorties attendues** :
- Spécification d'implémentation : arbre des bus audio, effets par bus, règles de variation (choix aléatoire, hauteur, volume), règles de ducking, polyphonie maximale par événement.
- Table des formats d'export (WAV pour les sons courts, OGG Vorbis pour les sons longs ou la musique, à vérifier selon la version du moteur) et estimation du poids mémoire par groupe.
- Brief de code pour l'agent de développement Godot, via flux à sens unique ; décisions ou actions pour l'agent de coordination, sans les annoncer déjà exécutées.

**Exemple de prompt** :

> « Adaptive Audio Implementation : décris ta situation concrète. »
**Cas nominal** : à partir de 30 événements sonores d'un niveau, des plans de bus et d'un budget de 20 Mo, produire la table bus/variation/format/coût, vérifier le critère d'acceptation ci-dessus et transmettre le brief à l'agent technique du moteur de jeu.

**Cas limite** : le budget mémoire n'est pas fourni ; livrer la spécification avec les coûts estimés par groupe et indiquer que la conformité

**Cas d'usage** : complément : skill 603. demande ; portant ; adaptive

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

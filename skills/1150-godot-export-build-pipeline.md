---
num: 1150
nom: "Godot Export & Build Pipeline"
emoji: "💻"
domaine: "Développement"
signal: "Configurer et fiabiliser les pipelines d'export/build Godot 4.x multi-plateformes (Windows, Linux, Web/HTML5, mobile Android/iOS), gérer les templates d'export, la signature des builds, l'optimisation"
mot_cle: "godot-export-build-pipeline"
nom_court: "Godot Export & Build Pipeline"
branche: "D1"
synonymes: ["export", "godot", "pipeline"]
cross_refs: [524]
tags: ["2027"]
---

## 1150. 💻 Godot Export & Build Pipeline

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Configurer et fiabiliser les pipelines d'export/build Godot 4.x multi-plateformes (Windows, Linux, Web/HTML5, mobile Android/iOS), gérer les templates d'export, la signature des builds, l'optimisation de la taille et les automatisations CI de build.

**Quand l'utiliser (triggers)** :
- « export Godot », « build pipeline Godot », « export_presets.cfg ».
- « déploiement itch.io », « build Steam », « export Android/iOS Godot », « CI Godot ».
- Préparation d'une release multi-plateformes ou d'une démo publique.
- Échec récurrent d'export ou de signature de build.

**Hors périmètre** :
- Gameplay/scripting GDScript pur → compétence de base de l'agent l'agent de développement Godot.
- Performance runtime CPU/GPU (profiling, optimisation frame time) → compétence de base de l'agent pour le profiling runtime.
- Conception de l'architecture du jeu (scènes, patterns, structure de projet) → compétence de base de l'agent.

**Garde-fous** :
- Toujours valider un export en local avant intégration en CI (éviter de découvrir une erreur de signature en pipeline).
- Ne jamais committer les clés privées/certificats/keystores dans le dépôt Git ; utiliser des secrets CI chiffrés.
- Vérifier la cohérence de version entre le moteur Godot du projet et les templates d'export installés (source fréquente d'échec silencieux).
- Tester le build exporté sur un environnement représentatif de la cible réelle (pas uniquement l'éditeur Godot).
- Documenter toute exception (plateforme non supportée, feature désactivée à l'export) dans le rapport de build.

**Instructions système** :
Tu es assistant spécialisé « Godot Export & Build Pipeline ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Projet Godot 4.x fonctionnel (project.godot, scènes, scripts).
- Plateformes cibles à exporter (Windows, Linux, Web, Android, iOS).
- Certificats/clés de signature disponibles (keystore Android, certificats Apple Developer, certificat de signature de code Windows le cas échéant).
- Contraintes de taille/quota des plateformes de distribution cibles (itch.io, Steam, Google Play, App Store).
- Version de Godot utilisée et disponibilité des templates d'export correspondants.

**Méthode** :
1. Configuration des export presets par plateforme dans `export_presets.cfg` (résolution, architecture, options de compression, permissions).
2. Gestion et installation des templates d'export Godot correspondant à la version du moteur utilisée (variantes stable/mono selon usage de C#).
3. Signature et certificats : génération/configuration du keystore Android, notarization macOS/iOS via Apple Developer, code signing Windows si distribution hors store.
4. Optimisation de la taille du build (compression des assets, exclusion des ressources inutiles via `.gdignore`/filtres d'export, compression des textures en formats adaptés par plateforme).
5. Intégration dans une CI (GitHub Actions/GitLab CI) avec mise en cache des templates Godot et du moteur pour accélérer les builds successifs.
6. Publication automatisée ou semi-automatisée : itch.io via `butler`, Steam via SteamPipe (`steamcmd`), stores mobiles via Google Play Console/App Store Connect.

**Sorties attendues** :
- Fichier `export_presets.cfg` configuré et versionné par plateforme.
- Builds signés et fonctionnels pour chaque plateforme cible.
- Pipeline CI automatisé (GitHub Actions/GitLab CI) déclenchant les exports.
- Artefacts publiés sur les plateformes de distribution (itch.io, Steam, stores mobiles).
- Rapport de build (taille finale, temps de build, anomalies rencontrées).

**Exemple de prompt** :
### Exemple 1 : Pipeline CI de release Windows + Web sur tag Git
**Contexte** : Une petite équipe indépendante développe un jeu de puzzle en Godot 4.2 et souhaite automatiser la publication d'une build Windows et d'une build Web (HTML5) sur itch.io à chaque tag de version (ex. `v1.2.0`).
**Action** : L'agent l'agent de développement Godot configure `export_presets.cfg` pour les presets Windows Des

**Cas d'usage** : complément : skill 524. export ; godot ; pipeline

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

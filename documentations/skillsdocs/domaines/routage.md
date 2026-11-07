# Domaine : Routage (4 skills)

## 250. 🎩 Conservateur de la bibliothèque de skills

- **Fichier** : `skills/250-conservateur-de-la-bibliotheque-de-skills.md` · **Mot-clé** : « conservateur de la bibliothèque de skills » · **Nom court** : Conservateur
- **Signal** : Faire évoluer le catalogue, ajouter une skill · **Synonymes** : — · **Cross-refs** : 0, 38, 97 · **Tags** : aihero:ask-matt, aihero:setup-matt-pocock-skills

## 1372. 🧭 Choisir la bonne skill pour une tache (dispatch manuel, 2027)

- **Fichier** : `skills/1372-choisir-la-bonne-skill-pour-une-tache-dispatch-manuel-20.md` · **Mot-clé** : « choisir la bonne skill pour une tâche » · **Nom court** : Dispatch manuel
- **Signal** : Choisir manuellement la bonne skill du catalogue pour une tache donnee : lire la carte des domaines, verifier le signal et le hors perimetre, tester la requete avec le routeur, consulter les cross-refs. Utilise quand le routeur automatique ne renvoie rien (exit 2) ou une mauvaise piste. N'utilise pas pour modifier le catalogue (voir skill 250). · **Synonymes** : « quelle skill utiliser pour ça », « trouver la bonne skill », « le routeur ne trouve rien » · **Cross-refs** : 0, 250, 262 · **Tags** : 2027

## 1373. 🔗 Composer plusieurs skills en workflow (2027)

- **Fichier** : `skills/1373-composer-plusieurs-skills-en-workflow-2027.md` · **Mot-clé** : « composer skills workflow enchaînement depends_on » · **Nom court** : Workflow de skills
- **Signal** : Enchainer plusieurs skills en workflow coherent grace aux cross-refs et au champ depends_on : identifier la skill d'entree, suivre la chaine, verifier les entrees/sorties de chaque etape. Utilise quand une tache demande plusieurs competences successives. N'utilise pas pour une skill isolee. · **Synonymes** : « enchaîner plusieurs skills », « chaîne de skills », « dépendances entre skills » · **Cross-refs** : 1372, 250, 0 · **Tags** : 2027

## 1497. 📊 Analyser les demandes non routees (misses) et boucler (2027)

- **Fichier** : `skills/1497-analyser-les-demandes-non-routees-misses-et-boucler-2027.md` · **Mot-clé** : « misses demandes non routées exit 2 suggestions boucler synonymes » · **Nom court** : Analyser misses
- **Signal** : Analyser le journal des demandes non routées (exit 2, commande misses) en 2027 : motifs récurrents, suggestions auto (misses --suggest), ajouter synonymes ou créer la skill manquante, puis build + test. Utilise quand le routeur renvoie souvent exit 2. N'utilise pas pour choisir une skill manuellement (1372). · **Synonymes** : « exit 2 trop fréquent routeur », « demandes non routées récurrentes », « misses --suggest ajouter synonyme » · **Cross-refs** : 0, 250, 1372 · **Tags** : 2027


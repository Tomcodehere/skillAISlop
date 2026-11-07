# Domaine : Game Dev (100 skills)

## 1500. 🎮 Choisir son moteur de jeu : Unity, Godot ou Unreal

- **Fichier** : `skills/1500-choisir-son-moteur-de-jeu-unity-godot-ou-unreal.md` · **Mot-clé** : « choisir moteur de jeu unity godot unreal 2027 » · **Nom court** : Choisir moteur
- **Signal** : Choisir un moteur de jeu en 2027 selon le projet : Unity (C#, écosystème immense, mobile/2D), Godot 4 (GDScript, léger, open source, 2D excellent), Unreal 5 (C++/Blueprints, 3D haut de gamme, exigeant). Utilise quand on démarre un jeu. N'utilise pas pour un jeu web (voir 545). · **Synonymes** : « unity ou godot ou unreal », « quel moteur pour mon jeu 2027 », « godot 4 vs unity 2027 » · **Cross-refs** : 524, 1140, 545 · **Tags** : 2027

## 1501. ⏱️ Boucle de jeu fixe : fixed timestep et interpolation

- **Fichier** : `skills/1501-boucle-de-jeu-fixe-fixed-timestep-et-interpolation.md` · **Mot-clé** : « fixed timestep boucle de jeu interpolation physique 60 Hz » · **Nom court** : Fixed timestep
- **Signal** : Implémenter une boucle de jeu robuste en 2027 : fixed timestep pour la physique/logique (ex. 60 Hz fixe), variable render, interpolation entre les 2 derniers états pour un rendu fluide. Utilise pour tout jeu temps réel. N'utilise pas pour un jeu au tour par tour. · **Synonymes** : « boucle de jeu fixe 60 hz », « interpolation render entre deux états », « delta time vs fixed dt » · **Cross-refs** : 1140, 308, 309 · **Tags** : 2027

## 1502. 🎬 Gestion des scenes et transitions

- **Fichier** : `skills/1502-gestion-des-scenes-et-transitions.md` · **Mot-clé** : « gestion des scènes chargement asynchrone additif transitions » · **Nom court** : Scènes
- **Signal** : Organiser un jeu en scènes/niveaux en 2027 (existe 1264 sur les scènes Godot) : scène de chargement dédiée, chargement asynchrone (LoadSceneAsync), additifs (menu + HUD + niveau), transitions fondues, persistance entre scènes (singleton/DontDestroyOnLoad). Utilise pour structurer un jeu. N'utilise pas pour un écran unique. · **Synonymes** : « charger un niveau sans freeze », « scènes additives menu + hud + niveau », « transition fondu entre niveaux » · **Cross-refs** : 1264, 1140, 1573 · **Tags** : 2027

## 1503. 💾 Sauvegarde et chargement de partie

- **Fichier** : `skills/1503-sauvegarde-et-chargement-de-partie.md` · **Mot-clé** : « sauvegarde partie sérialisation JSON slots auto-save versionning » · **Nom court** : Save/Load
- **Signal** : Implémenter la sauvegarde d'une partie en 2027 : sérialisation JSON/binaire des données de jeu (position, inventaire, quêtes, temps de jeu), 3 slots + auto-save, versionning des saves (migration si format change), sauvegarde cloud (1576). Utilise dans tout jeu avec progression. N'utilise pas pour un jeu en ligne compétitif (anti-triche 1543). · **Synonymes** : « 3 slots de sauvegarde », « sérialiser l'état du jeu en JSON », « migration de save entre versions » · **Cross-refs** : 1576, 1539, 601 · **Tags** : 2027

## 1504. 🎮 Systeme d'input moderne : actions, gamepad, remappable

- **Fichier** : `skills/1504-systeme-d-input-moderne-actions-gamepad-remappable.md` · **Mot-clé** : « input actions remappable gamepad clavier remap contrôles » · **Nom court** : Input moderne
- **Signal** : Concevoir un système d'input en 2027 : actions nommées (saut, tir, inventaire) mappées à plusieurs entrées (clavier AZERTY/QWERTY, manette, tactile), Input Actions (Unity) ou InputMap (Godot), remapping par le joueur + sauvegarde des contrôles, coyote via l'input buffer. Utilise pour tout jeu jouable. N'utilise pas pour un jeu piloté à la souris seule. · **Synonymes** : « remapper les contrôles par le joueur », « input actions unity ou inputmap godot », « AZERTY et QWERTY supportés » · **Cross-refs** : 1511, 1571, 1575 · **Tags** : 2027

## 1505. 📷 Camera 2D : follow, deadzone et lookahead

- **Fichier** : `skills/1505-camera-2d-follow-deadzone-et-lookahead.md` · **Mot-clé** : « caméra 2D follow deadzone lookahead limites niveau » · **Nom court** : Caméra 2D
- **Signal** : Concevoir une caméra 2D confortable en 2027 : follow du joueur avec deadzone (zone morte), lookahead dans la direction du mouvement, limites de niveau (clamp), lerp doux, et zoom sur événements. Utilise pour tout jeu 2D à défilement. N'utilise pas pour la 3D (voir 1506). · **Synonymes** : « caméra qui suit le joueur en 2D », « deadzone caméra zone morte », « lookahead caméra selon direction » · **Cross-refs** : 1506, 1511, 1140 · **Tags** : 2027

## 1506. 🎥 Camera 3D third-person : collision et lock-on

- **Fichier** : `skills/1506-camera-3d-third-person-collision-et-lock-on.md` · **Mot-clé** : « caméra 3D third-person collision raycast lock-on FOV sprint » · **Nom court** : Caméra 3D
- **Signal** : Concevoir une caméra 3D en vue third-person en 2027 : orbite autour du joueur (souris/stick), collision caméra (raycast : la caméra ne traverse pas les murs), lock-on sur les ennemis proches, FOV dynamique (sprint). Utilise pour tout jeu 3D action/aventure. N'utilise pas pour la 2D (voir 1505). · **Synonymes** : « caméra qui ne traverse pas les murs », « lock-on ennemi caméra 3D », « FOV qui augmente en sprint » · **Cross-refs** : 1505, 1574, 1526 · **Tags** : 2027

## 1507. 💥 Detection de collision 2D : AABB, cercles, SAT

- **Fichier** : `skills/1507-detection-de-collision-2d-aabb-cercles-sat.md` · **Mot-clé** : « collision 2D AABB cercles SAT résolution séparation » · **Nom court** : Collision 2D
- **Signal** : Implémenter la détection de collision 2D en 2027 : AABB (rectangles alignés) pour la plupart, cercles pour les projectiles/ennemis ronds, SAT (Separating Axis Theorem) pour les rectangles orientés, avec résolution (pousser hors) et événements (on_enter/on_stay/on_exit). Utilise pour tout jeu 2D physique. N'utilise pas pour la 3D (moteur physique). · **Synonymes** : « AABB rectangle aligné collision », « cercle vs cercle collision », « SAT rectangles orientés » · **Cross-refs** : 1508, 1510, 1140 · **Tags** : 2027

## 1508. ⚔️ Hitbox, hurtbox et i-frames

- **Fichier** : `skills/1508-hitbox-hurtbox-et-i-frames.md` · **Mot-clé** : « hitbox hurtbox i-frames invincibilité knockback combat » · **Nom court** : Hitbox
- **Signal** : Concevoir les hitboxes d'un jeu d'action en 2027 : hitbox (dégâts de l'attaque) vs hurtbox (réception), priorité des attaques, i-frames (invincibilité 0,3 s après un coup reçu), knockback. Utilise pour tout jeu de combat/action. N'utilise pas pour un RPG au tour par tour. · **Synonymes** : « séparer hitbox et hurtbox », « i-frames après un coup », « knockback directionnel » · **Cross-refs** : 1507, 1559, 1526 · **Tags** : 2027

## 1509. 🏃 Physique 2D custom : gravité et saut variable

- **Fichier** : `skills/1509-physique-2d-custom-gravite-et-saut-variable.md` · **Mot-clé** : « physique 2D custom gravité saut variable couper vélocité » · **Nom court** : Physique 2D
- **Signal** : Coder une physique 2D custom en 2027 (sans moteur physique lourd) : gravité constante, saut variable (relâcher la touche = couper la vélocité verticale, saut plus court), vitesse max, friction au sol. Utilise pour un plateformer exigeant (game feel). N'utilise pas si le moteur physique suffit. · **Synonymes** : « saut variable selon appui long court », « gravité custom plateformer », « friction au sol glisser » · **Cross-refs** : 1510, 1511, 1559 · **Tags** : 2027

## 1510. 🎯 Plateformer : coyote time et jump buffering

- **Fichier** : `skills/1510-plateformer-coyote-time-et-jump-buffering.md` · **Mot-clé** : « coyote time jump buffering plateformer 0,1 s » · **Nom court** : Coyote+buffer
- **Signal** : Implémenter le coyote time et le jump buffering en 2027, indispensables à un bon plateformer : coyote time (0,1 s pour sauter après avoir quitté le sol), jump buffer (0,1 s : appuyer juste avant d'atterrir saute dès l'atterrissage). Utilise dans tout plateformer 2D. N'utilise pas pour un jeu sans saut. · **Synonymes** : « sauter 0 », « 1 s après avoir quitté le sol », « jump buffer appuyer avant d'atterrir », « tolérance de saut plateformer » · **Cross-refs** : 1509, 1504, 1559 · **Tags** : 2027

## 1511. 💨 Mouvement 8 directions et dash

- **Fichier** : `skills/1511-mouvement-8-directions-et-dash.md` · **Mot-clé** : « mouvement 8 directions normalisé dash cooldown trail » · **Nom court** : Déplacement 8 dir
- **Signal** : Coder un déplacement 8 directions fluide en 2027 : normalisation du vecteur d'input (diagonale pas plus rapide), accélération/décélération, dash avec cooldown et i-frames, trail visuel. Utilise pour top-down 2D et twin-stick. N'utilise pas pour un plateformer (voir 1510). · **Synonymes** : « diagonale pas plus rapide normaliser », « dash avec cooldown et i-frames », « top-down 2D déplacement fluide » · **Cross-refs** : 1509, 1504, 1559 · **Tags** : 2027

## 1512. 🧱 Tilemap et autotiling par regles de bits

- **Fichier** : `skills/1512-tilemap-et-autotiling-par-regles-de-bits.md` · **Mot-clé** : « tilemap autotiling règles de bits 47 tuiles collision auto » · **Nom court** : Tilemap
- **Signal** : Construire des niveaux 2D avec une tilemap en 2027 : grille de tuiles (16/32 px), autotiling par règles de bits (47 tuiles selon les voisins N/S/E/O), peinture dans l'éditeur, collision automatique par tuile, couches (sol/décor/avant-plan). Utilise pour tout jeu 2D tile-based. N'utilise pas pour la 3D (voxels). · **Synonymes** : « peindre un niveau avec des tuiles », « autotiling 47 tuiles selon voisins », « collision auto par tuile tilemap » · **Cross-refs** : 1513, 1140, 1554 · **Tags** : 2027

## 1513. 🏰 Generation procédurale de donjons : rooms et corridors

- **Fichier** : `skills/1513-generation-procedurale-de-donjons-rooms-et-corridors.md` · **Mot-clé** : « génération procédurale donjon salles corridors roguelike » · **Nom court** : Procgen donjon
- **Signal** : Générer un donjon procédural en 2027 par placement de salles + corridors : placer N salles aléatoires sans chevauchement (rejet ou poussée), connecter les centres (MST ou plus proche voisin), instancier les tuiles (1512), placer ennemis/loot (1528). Utilise pour les roguelikes. N'utilise pas pour un niveau hand-crafted. · **Synonymes** : « générer un donjon aléatoire rooms corridors », « roguelike niveau procédural 2027 », « salles sans chevauchement + MST » · **Cross-refs** : 1512, 1514, 1528 · **Tags** : 2027

## 1514. 🏔️ Cavernes par cellular automata

- **Fichier** : `skills/1514-cavernes-par-cellular-automata.md` · **Mot-clé** : « cellular automata cavernes génération procédurale lissage 45% » · **Nom court** : Cavernes CA
- **Signal** : Générer des cavernes naturelles en 2027 avec un automate cellulaire : grille remplie à 45 % aléatoirement, 4-5 itérations de lissage (une cellule devient mur si 4+ voisins sont murs), garder la plus grande zone connexe, placer joueur/ennemis dedans. Utilise pour grottes, forêts, donjons organiques. N'utilise pas pour des salles structurées (voir 1513). · **Synonymes** : « générer une grotte naturelle automate cellulaire », « lissage 4-5 itérations 45% remplissage », « garder la plus grande zone connexe » · **Cross-refs** : 1513, 1517, 1512 · **Tags** : 2027

## 1515. 🌊 Bruit de Perlin pour terrain et heightmap

- **Fichier** : `skills/1515-bruit-de-perlin-pour-terrain-et-heightmap.md` · **Mot-clé** : « bruit de Perlin terrain heightmap octaves fractal seed seuils biomes » · **Nom court** : Perlin
- **Signal** : Générer du terrain 2D/3D avec le bruit de Perlin en 2027 : octaves (fréquences multiples + amplitudes décroissantes = fractal), seuils (eau sous 0,3 inf. à  sable sous 0,5 inf. à  herbe sous 0,8 inf. à  roche inf. à  neige), seed pour reproductibilité. Utilise pour maps ouvertes, îles, reliefs. N'utilise pas pour des donjons (voir 1513/1514). · **Synonymes** : « générer une île avec Perlin noise », « heightmap terrain 3D procédural », « octaves fractal bruit Perlin 2027 » · **Cross-refs** : 1514, 1516, 1512 · **Tags** : 2027

## 1516. 🧩 Wave Function Collapse (WFC) simplifié

- **Fichier** : `skills/1516-wave-function-collapse-wfc-simplifie.md` · **Mot-clé** : « wave function collapse WFC entropie propagation contraintes backtrack » · **Nom court** : WFC
- **Signal** : Générer un niveau avec Wave Function Collapse en 2027 (version simplifiée) : chaque cellule a un ensemble de tuiles possibles, on choisit la cellule à plus basse entropie, on propage les contraintes aux voisins (règles de compatibilité), backtrack si contradiction. Utilise pour des niveaux cohérents procéduraux (ville, donjon). N'utilise pas si rooms+corridors (1513) suffit. · **Synonymes** : « générer niveau WFC wave function collapse », « propagation des contraintes tuiles voisines », « entropie choisir cellule la plus contrainte » · **Cross-refs** : 1513, 1515, 1512 · **Tags** : 2027

## 1517. 🧭 Pathfinding A* avec poids et flow field

- **Fichier** : `skills/1517-pathfinding-a-avec-poids-et-flow-field.md` · **Mot-clé** : « pathfinding A* grille heap g h f poids terrain flow field » · **Nom court** : A* + flow field
- **Signal** : Implémenter le pathfinding A* en 2027 sur une grille : open set (heap), coûts g/h/f, voisins 4 ou 8 directions (diagonales sans couper les coins), poids par terrain (route x1, herbe x1,5, eau infranchissable), puis flow field (champ de directions) pour 100+ unités qui suivent le même chemin. Utilise pour les RTS et foules. N'utilise pas pour un seul PNJ (voir 1224 navmesh 3D). · **Synonymes** : « A* sur grille open set heap », « flow field pour 100 unités même chemin », « poids terrain route herbe eau » · **Cross-refs** : 1224, 1512, 1525 · **Tags** : 2027

## 1518. 🧭 Navmesh 3D : baking et navigation

- **Fichier** : `skills/1518-navmesh-3d-baking-et-navigation.md` · **Mot-clé** : « navmesh 3D baking navigation agent recast obstacles dynamiques » · **Nom court** : Navmesh 3D
- **Signal** : Utiliser un navmesh 3D en 2027 (existe 1224 sur pathfinding général) : bake de la navigation sur la géométrie walkable (Unreal NavMesh, Unity AI Navigation, Godot NavigationServer), agents qui suivent (NavigationAgent), recast local pour obstacles dynamiques. Utilise pour PNJ en 3D. N'utilise pas en 2D (voir A* 1517). · **Synonymes** : « baker la navigation 3D sur le niveau », « NavigationAgent suit le navmesh », « obstacles dynamiques navmesh local » · **Cross-refs** : 1224, 1517, 1520 · **Tags** : 2027

## 1519. 🧠 IA ennemie : state machine (FSM) simple

- **Fichier** : `skills/1519-ia-ennemie-state-machine-fsm-simple.md` · **Mot-clé** : « IA ennemie state machine FSM patrouille poursuite attaque fuite » · **Nom court** : FSM ennemi
- **Signal** : Construire une IA ennemie par machine à états finis (FSM) en 2027 : états (Patrouille, Poursuite, Attaque, Fuite, Mort), transitions par conditions (distance joueur, PV, ligne de vue 1524), une seule update par état. Alternative plus simple que les behavior trees (1208). Utilise pour un ennemi simple et lisible. N'utilise pas pour 10+ comportements (voir utility AI 1521). · **Synonymes** : « machine à états ennemi patrouille attaque », « FSM simple lisible debuggable », « transition si joueur à moins de 8 m » · **Cross-refs** : 1208, 1524, 1520 · **Tags** : 2027

## 1520. 👁️ Perception ennemie : vue, ouïe et memoire

- **Fichier** : `skills/1520-perception-ennemie-vue-ouie-et-memoire.md` · **Mot-clé** : « perception IA cône de vision ouïe mémoire dernier point vu » · **Nom court** : Perception
- **Signal** : Donner une perception crédible à un ennemi en 2027 : cône de vision (angle + portée + obstacles via raycast 1524), ouïe (bruits avec intensité/distance, le joueur qui court alerte), mémoire (dernier point vu, l'ennemi y va puis cherche 5 s). Utilise pour du stealth/action. N'utilise pas pour un ennemi aveugle. · **Synonymes** : « ennemi qui voit dans un cône 90° », « l'ennemi entend le joueur courir », « mémoire : dernier point vu puis chercher » · **Cross-refs** : 1524, 1519, 1525 · **Tags** : 2027

## 1521. ⚖️ Utility AI : choisir l'action par score

- **Fichier** : `skills/1521-utility-ai-choisir-l-action-par-score.md` · **Mot-clé** : « utility AI score actions besoins faim PV ennemi choisir meilleure » · **Nom court** : Utility AI
- **Signal** : Construire une Utility AI en 2027 (alternative aux behavior trees 1208) : chaque action possible a un score 0-1 selon le contexte (faim, PV, ennemi proche), l'IA choisit la meilleure toutes les 0,5 s. Utilise pour des PNJ avec 5-10 besoins concurrents. N'utilise pas pour un ennemi scripté (FSM 1519). · **Synonymes** : « IA par utilité score 0-1 choisir action », « PNJ avec besoins faim sommeil social », « évaluer chaque action toutes les 0 », « 5 s » · **Cross-refs** : 1208, 1519, 1136 · **Tags** : 2027

## 1522. 🎯 GOAP : planification d'actions par objectif

- **Fichier** : `skills/1522-goap-planification-d-actions-par-objectif.md` · **Mot-clé** : « GOAP goal oriented action planning préconditions effets plan A* » · **Nom court** : GOAP
- **Signal** : Implémenter un GOAP (Goal-Oriented Action Planning) en 2027 : un objectif (ex. 'avoir une épée'), des actions avec préconditions et effets (forger épée nécessite forge + 50 minerais), l'algo A* sur l'espace des états choisit le plan le moins cher. Utilise pour des PNJ autonomes complexes. N'utilise pas pour un ennemi simple (FSM 1519 suffit). · **Synonymes** : « PNJ autonome qui planifie pour atteindre un objectif », « actions avec préconditions et effets », « plan le moins cher avec A* sur les états » · **Cross-refs** : 1521, 1519, 1517 · **Tags** : 2027

## 1523. 🕶️ Stealth : ligne de vue et cone de vision avances

- **Fichier** : `skills/1523-stealth-ligne-de-vue-et-cone-de-vision-avances.md` · **Mot-clé** : « stealth ligne de vue raycasts cone détection 0-100% ombre » · **Nom court** : Stealth LOS
- **Signal** : Construire un système de stealth en 2027 : cône de vision de garde (mesh visuel translucide), ligne de vue par raycasts multiples (tête/corps/pieds du joueur), niveau de détection 0-100 % (remplit si visible, décroit sinon), états Alerte/Inquiet/Suspect, ombre = bonus de dissimulation. Utilise pour les jeux d'infiltration. N'utilise pas sans garde (voir perception 1520). · **Synonymes** : « garde avec cône de vision mesh translucide », « 3 raycasts tête corps pieds visibilité », « jauge de détection qui monte descend » · **Cross-refs** : 1520, 1524, 1519 · **Tags** : 2027

## 1524. 💡 Raycast et ligne de vue (LOS) en 2D/3D

- **Fichier** : `skills/1524-raycast-et-ligne-de-vue-los-en-2d-3d.md` · **Mot-clé** : « raycast lancer de rayon ligne de vue hit point normal distance » · **Nom court** : Raycast
- **Signal** : Implémenter le raycast (lancer de rayon) en 2027 : Physics.Raycast (Unity), space.intersect_ray (Godot), pour la ligne de vue (joueur visible ?), les tirs hitscan, les clics souris → monde, les ombres. Retourne le premier hit (point, normal, distance, objet). Utilise partout. N'utilise pas pour la détection de zone (overlap). · **Synonymes** : « joueur visible si aucun mur entre (raycast) », « tir hitscan raycast premier hit », « clic souris vers position monde 3D » · **Cross-refs** : 1523, 1520, 1507 · **Tags** : 2027

## 1525. 👥 Coordination d'ennemis : flanquement et focus

- **Fichier** : `skills/1525-coordination-d-ennemis-flanquement-et-focus.md` · **Mot-clé** : « coordination ennemis flanquement focus fire rôles tank dps soigneur » · **Nom court** : Coordination
- **Signal** : Faire coopérer des ennemis en groupe en 2027 : rôles (tank qui attire l'attention, DPS qui tirent, soigneur), flanquement (un ennemi contourne pendant que l'autre attaque de front), focus fire (tous sur la même cible), communication par 'last seen' partagé (1520). Utilise pour des combats de groupe mémorables. N'utilise pas pour un ennemi seul. · **Synonymes** : « ennemis qui flanquent le joueur », « tous attaquent la même cible (focus) », « tank + dps + soigneur rôles » · **Cross-refs** : 1520, 1526, 1519 · **Tags** : 2027

## 1526. 🐉 Boss : phases et patterns telegraphes

- **Fichier** : `skills/1526-boss-phases-et-patterns-telegraphes.md` · **Mot-clé** : « boss phases PV patterns telegraphes marque au sol barre de cast fenêtre dégâts » · **Nom court** : Boss design
- **Signal** : Concevoir un boss en 2027 : plusieurs phases selon les PV (100-66 %, 66-33 %, sous 33 %) avec transition (invincible + cinématique courte), attaques télégraphiées (marque au sol 1 s avant = zone de dégâts, barre de cast), patterns rotatifs, fenêtres de dégâts après certaines attaques. Utilise pour un boss mémorable. N'utilise pas pour un ennemi normal (1519). · **Synonymes** : « boss 3 phases selon PV transition cinématique », « attaque télégraphiée marque au sol 1 s avant », « fenêtre de dégâts après l'attaque du boss » · **Cross-refs** : 1519, 1525, 1508 · **Tags** : 2027

## 1527. 🌊 Spawner de vagues a difficulté progressive

- **Fichier** : `skills/1527-spawner-de-vagues-a-difficulte-progressive.md` · **Mot-clé** : « spawner vagues difficulté progressive budget points délais entre spawns » · **Nom court** : Spawner vagues
- **Signal** : Concevoir un spawner de vagues en 2027 : N vagues avec composition qui durcit (vague 1 = 3 slimes, vague 5 = 2 brutes + 5 archers), points de spawn budget (coût par ennemi), délais entre spawns, événement 'vague suivante dans 10 s', bonus si vague nettoyée sans dégâts. Utilise pour survival/arena. N'utilise pas pour un donjon fixe (1513). · **Synonymes** : « vagues d'ennemis qui durcissent », « budget de points par vague (slime 1 », « brute 5) », « delai 10 s entre deux vagues » · **Cross-refs** : 1513, 1528, 1136 · **Tags** : 2027

## 1528. 🎰 Loot table ponderee et pity timer

- **Fichier** : `skills/1528-loot-table-ponderee-et-pity-timer.md` · **Mot-clé** : « loot table pondérée poids pity timer drop garanti boss » · **Nom court** : Loot table
- **Signal** : Concevoir une table de loot en 2027 : objets avec poids (commun 60, rare 30, épique 9, légendaire 1), tirage pondéré, pity timer (après 20 monstres sans rare, le taux rare x2, reset au drop), drop garanti tous les 50 (boss 1526). Utilise pour tout système de récompense aléatoire. N'utilise pas pour les récompenses fixes (quêtes 1531). · **Synonymes** : « tirage pondéré commun 60 rare 30 épique 9 légendaire 1 », « pity timer après 20 monstres sans rare », « drop garanti tous les 50 monstres » · **Cross-refs** : 1527, 1529, 1526 · **Tags** : 2027

## 1529. ⚖️ Equilibrage d'economie interne : inflation et sinks

- **Fichier** : `skills/1529-equilibrage-d-economie-interne-inflation-et-sinks.md` · **Mot-clé** : « équilibrage économie jeu sources sinks inflation courbe farm prix paliers » · **Nom court** : Équilibrage éco
- **Signal** : Équilibrer l'économie d'un jeu en 2027 (complète 1138 sur la modélisation) : sources (monstres, quêtes, farm) vs sinks (réparation, reroll, fast-travel) pour que la monnaie ne s'inflate pas; courbe de farm (combien de gold/heure à chaque niveau); prix des objets scalés par palier. Utilise quand l'économie d'un jeu dérive. N'utilise pas pour la monétisation réelle (1585). · **Synonymes** : « l'or s'inflate dans mon jeu », « sources vs sinks de gold équilibrés », « prix objets scalés par niveau joueur » · **Cross-refs** : 1138, 1528, 1530 · **Tags** : 2027

## 1530. 📈 Progression joueur : XP, courbes de niveau et paliers

- **Fichier** : `skills/1530-progression-joueur-xp-courbes-de-niveau-et-paliers.md` · **Mot-clé** : « courbe XP exponentielle paliers déblocage respec prestige niveaux » · **Nom court** : Progression XP
- **Signal** : Concevoir la progression d'un joueur en 2027 : courbe d'XP par niveau (exponentielle douce : xp(n) = 100 * 1,15^n), paliers de déblocage (niveau 5 = donjon 2, niveau 10 = monture), respec payant, prestige optionnel. Utilise pour tout RPG/action avec niveaux. N'utilise pas pour un jeu sans progression (puzzle). · **Synonymes** : « xp niveau = 100 * 1 », « 15^n exponentiel », « déblocage donjon niveau 5 monture niveau 10 », « respec payant des compétences » · **Cross-refs** : 1537, 1529, 1481 · **Tags** : 2027

## 1531. 📜 Systeme de quetes : journal, objectifs, recompenses

- **Fichier** : `skills/1531-systeme-de-quetes-journal-objectifs-recompenses.md` · **Mot-clé** : « système de quêtes journal objectifs compteur récompenses chaînées » · **Nom court** : Quêtes
- **Signal** : Concevoir un système de quêtes en 2027 : journal de quêtes (en cours/terminées), objectifs traçables (tuer 5 rats → compteur 3/5), quêtes principales (chaînées) et secondaires, récompenses (XP 1530, gold 1529, objet 1528), échec si timer. Utilise pour tout RPG/aventure. N'utilise pas pour un jeu bac à sable pur. · **Synonymes** : « journal de quêtes avec compteur 3/5 », « quête principale chaînée quêtes secondaires », « récompense XP gold objet à la validation » · **Cross-refs** : 1530, 1532, 1528 · **Tags** : 2027

## 1532. 💬 Arbre de dialogue avec conditions et consequences

- **Fichier** : `skills/1532-arbre-de-dialogue-avec-conditions-et-consequences.md` · **Mot-clé** : « arbre de dialogue nœuds choix conditions conséquences réputation » · **Nom court** : Dialogues
- **Signal** : Construire un arbre de dialogue en 2027 : nœuds (PNJ parle, choix du joueur), conditions sur les choix (si quête 1531 faite, si or supérieur ou égal à 50), conséquences (donne objet, démarre quête, change réputation), sauvegarde de l'état. Utilise pour tout RPG avec PNJ. N'utilise pas pour des dialogues linéaires simples (texte fixe). · **Synonymes** : « choix de dialogue avec condition (si quête faite) », « PNJ qui se souvient de ce qu'on a dit », « réputation qui change selon les réponses » · **Cross-refs** : 1531, 1529, 1533 · **Tags** : 2027

## 1533. 🌐 Localisation in-game des textes (i18n des dialogues)

- **Fichier** : `skills/1533-localisation-in-game-des-textes-i18n-des-dialogues.md` · **Mot-clé** : « localisation jeu i18n clés traduction pluriels ICU pseudo-localisation » · **Nom court** : Loca in-game
- **Signal** : Localiser les textes d'un jeu en 2027 : clés de traduction (ui.title, quest.rats.desc) dans des fichiers par langue (JSON/CSV/PO), pluriels et genre (ICU), noms propres inchangés, longueur max par UI, test de pseudo-localisation (accents allongés) pour détecter les débordements. Utilise quand on sort un jeu à l'international. N'utilise pas pour la traduction de docs (skill 7). · **Synonymes** : « traduire les textes du jeu en 5 langues », « clés ui.title quest.desc par langue JSON », « pseudo-localisation détecter débordements UI » · **Cross-refs** : 1485, 1094, 1532 · **Tags** : 2027

## 1534. 🎁 Inventaire : grille, drag and drop, stacking

- **Fichier** : `skills/1534-inventaire-grille-drag-and-drop-stacking.md` · **Mot-clé** : « inventaire grille drag and drop stack x99 tri auto tooltip » · **Nom court** : Inventaire
- **Signal** : Concevoir un inventaire en grille en 2027 : N slots (ex. 5x4), objets avec taille 1x1 à 2x3, drag & drop (souris + manette 1571), stacking (potion x99 dans 1 slot), tri auto, survol avec tooltip (stats 1535), équipement séparé. Utilise pour tout RPG/loot. N'utilise pas pour un inventaire liste simple (UI texte). · **Synonymes** : « inventaire 5x4 slots drag drop souris manette », « potions stackées x99 dans un slot », « tri auto et tooltip au survol » · **Cross-refs** : 1535, 1571, 1532 · **Tags** : 2027

## 1535. ⚔️ Equipement et stats : armes, armures, rarete

- **Fichier** : `skills/1535-equipement-et-stats-armes-armures-rarete.md` · **Mot-clé** : « équipement slots arme armure stats rareté comparaison équipement actuel » · **Nom court** : Équipement
- **Signal** : Concevoir l'équipement en 2027 : slots (arme, armure, casque, bottes, 2 anneaux), chaque objet a des stats (dégâts, défense, PV, crit...) selon sa rareté (commun x1 → légendaire x2,5, 1528), comparaison avec l équipé (tooltip + flèche verte/rouge), niveaux d'objet (upgrade forgeron 1536). Utilise pour tout RPG. N'utilise pas pour un jeu sans équipement. · **Synonymes** : « slots arme armure anneaux », « stats selon rareté x1 à x2 », « 5 », « comparer avec l'objet équipé (flèche verte rouge) » · **Cross-refs** : 1534, 1528, 1536 · **Tags** : 2027

## 1536. 🔨 Crafting : recettes, materiaux et forge

- **Fichier** : `skills/1536-crafting-recettes-materiaux-et-forge.md` · **Mot-clé** : « crafting recettes matériaux forge maîtrise chance bonus démontage » · **Nom court** : Crafting
- **Signal** : Concevoir un système de craft en 2027 : recettes (liste de matériaux + résultat, ex. épée fer = 3 minerais fer + 1 bois), stations (forge, alchimie), qualité de craft (maîtrise du joueur → chance de bonus de stats), démontage d'objets (récupère 50 % matériaux). Utilise pour les jeux avec gathering. N'utilise pas pour un craft instantané sans ressources (voir 1534). · **Synonymes** : « recette épée = 3 fer + 1 bois à la forge », « maîtrise craft : chance de +10% stats », « démonter un objet récupère 50% matériaux » · **Cross-refs** : 1534, 1535, 1529 · **Tags** : 2027

## 1537. 🌳 Arbre de competences (skill tree) et respec

- **Fichier** : `skills/1537-arbre-de-competences-skill-tree-et-respec.md` · **Mot-clé** : « skill tree arbre compétences points de talent prérequis respec payant » · **Nom court** : Skill tree
- **Signal** : Concevoir un arbre de compétences en 2027 : 3 branches (ex. guerrier/mage/voleur), nœuds avec coût en points de talent (gagnés par niveau 1530), prérequis (nœud parent), effets passifs (dégâts +10 %), respec payant (1530). Utilise pour la customisation du build. N'utilise pas pour un personnage sans choix (tout fixe). · **Synonymes** : « arbre de talents 3 branches guerrier mage voleur », « points de talent gagnés par niveau », « respec payant reset des talents » · **Cross-refs** : 1530, 1535, 1531 · **Tags** : 2027

## 1538. 🏆 Succes (achievements) et deblocages

- **Fichier** : `skills/1538-succes-achievements-et-deblocages.md` · **Mot-clé** : « achievements succès cachés conditions toast progression Steam » · **Nom court** : Achievements
- **Signal** : Concevoir les succès (achievements) d'un jeu en 2027 : 40-60 succès cachés/visibles, conditions variées (tuer 100 monstres, finir sans dégâts, trouver un easter egg), récompense (cosmétique, titre, 1529), notification toast, progression %, intégration Steam (1581). Utilise pour la rétention et la fierté. N'utilise pas pour les objectifs de quêtes (1531). · **Synonymes** : « succès 'tuer 100 monstres' avec toast », « succès caché easter egg », « progression 12/50 succès et intégration Steam » · **Cross-refs** : 1581, 1531, 1530 · **Tags** : 2027

## 1539. ☁️ Sauvegarde cloud et sync multi-appareils

- **Fichier** : `skills/1539-sauvegarde-cloud-et-sync-multi-appareils.md` · **Mot-clé** : « sauvegarde cloud sync Steam Cloud multi-appareils conflit plus récent » · **Nom court** : Save cloud
- **Signal** : Synchroniser les sauvegardes d'un jeu dans le cloud en 2027 : Steam Cloud (1581), Google Play Games, iCloud, ou API maison (S3 + API); upload auto à la fermeture, download au lancement, gestion de conflit (plus récent gagne, ou choix du joueur), quota (1 Mo), offline d'abord. Utilise pour les jeux multi-plateformes. N'utilise pas pour les jeux compétitifs (anti-triche 1543). · **Synonymes** : « sauvegarder dans le cloud automatiquement », « jouer sur PC puis téléphone même progression », « conflit de save : garder le plus récent » · **Cross-refs** : 1503, 1581, 1576 · **Tags** : 2027

## 1540. 📊 Analytics de jeu : funnels, rétention D1/D7, telemetry

- **Fichier** : `skills/1540-analytics-de-jeu-funnels-retention-d1-d7-telemetry.md` · **Mot-clé** : « analytics jeu télémétrie funnels rétention D1 D7 D30 événements custom » · **Nom court** : Analytics jeu
- **Signal** : Mettre en place la télémétrie d'un jeu en 2027 (RGPD-compliant 1587) : événements custom (level_start, boss_kill, purchase) envoyés à Unity Analytics/GameAnalytics/custom, funnels (tutoriel étape 3 → 4), rétention D1/D7/D30, dashboards, décisions data-driven. Utilise dès le soft launch. N'utilise pas pour espionner (consentement requis). · **Synonymes** : « funnel tutoriel étape par étape », « rétention D1 D7 D30 dashboard », « envoyer événements custom à Unity Analytics », « mesurer ARPU rétention D7 p-value ship kill » · **Cross-refs** : 1541, 110, 1587 · **Tags** : 2027

## 1541. ⚖️ A/B testing in-game : evenements saisonniers

- **Fichier** : `skills/1541-a-b-testing-in-game-evenements-saisonniers.md` · **Mot-clé** : « A/B testing in-game cohortes remote config impact rétention revenus » · **Nom court** : A/B in-game
- **Signal** : Faire de l'A/B testing in-game en 2027 : répartir les joueurs en cohortes (A/B/C) à distance (remote config Firebase/Unity), mesurer l'impact d'un changement (prix d'un skin, difficulté niveau 3) sur la rétention/revenus (1540), significativité (1482), décision ship/kill. Utilise en live ops (1542). N'utilise pas pour les bugs (hotfix direct). · **Synonymes** : « cohorte A prix 2 », « 99 € vs B 4 », « 99 € mesurer revenus », « remote config changer difficulté sans mise à jour », « significativité statistique décision ship » · **Cross-refs** : 1540, 1482, 110 · **Tags** : 2027

## 1542. 🌟 Live ops : evenements saisonniers et battle pass simple

- **Fichier** : `skills/1542-live-ops-evenements-saisonniers-et-battle-pass-simple.md` · **Mot-clé** : « live ops événement saisonnier Halloween battle pass 30 paliers rotation » · **Nom court** : Live ops
- **Signal** : Organiser des événements saisonniers en 2027 : event temporaire (Halloween 2 semaines) avec contenu dédié (skins, niveau, quêtes 1531), battle pass simple (30 paliers, récompenses gratuites/payantes 1585), annonce in-game + mail, analytics de l'event (1540), rotation mensuelle. Utilise pour la rétention long terme. N'utilise pas pour le contenu permanent. · **Synonymes** : « organiser un event Halloween 2 semaines skins niveau temporaire », « battle pass 30 paliers gratuit payant », « rotation mensuelle des events avec analytics » · **Cross-refs** : 1541, 1540, 1531 · **Tags** : 2027

## 1543. 🛡 Anti-triche : validation cote serveur

- **Fichier** : `skills/1543-anti-triche-validation-cote-serveur.md` · **Mot-clé** : « anti-triche serveur fait autorité détection anomalies shadowban chiffrement » · **Nom court** : Anti-triche
- **Signal** : Protéger un jeu multijoueur de la triche en 2027 : le serveur fait autorité (positions, dégâts, scores calculés côté serveur, jamais confiance au client), détection d'anomalies (vitesse impossible, dégâts x10, wallhack = LOS impossible), ban progressif (shadowban), chiffrement des paquets. Utilise pour tout jeu compétitif (1549). N'utilise pas pour un jeu solo (inutile). · **Synonymes** : « ne jamais faire confiance au client (serveur autorité) », « détecter un aimbot (tirs trop précis trop vite) », « shadowban : banir sans prévenir le tricheur » · **Cross-refs** : 1544, 1549, 1451 · **Tags** : 2027

## 1544. 🖧️ Architecture multijoueur : client-serveur vs P2P

- **Fichier** : `skills/1544-architecture-multijoueur-client-serveur-vs-p2p.md` · **Mot-clé** : « architecture multijoueur client-serveur dédié P2P relais compromis » · **Nom court** : Archi multi
- **Signal** : Choisir l'architecture réseau d'un jeu multi en 2027 : client-serveur dédié (autoritaire, anti-triche 1543, coûteux en serveurs) vs P2P/host (pas cher, triche facile, latence variable) vs relais (Steam relay, compromis). Critères : compétitif ou coop, budget serveurs, régions. Utilise quand on ajoute le multi (1549). N'utilise pas pour un jeu solo. · **Synonymes** : « serveur dédié vs P2P pour mon jeu coop », « relais Steam Network (pas cher », « pas d'anti-triche) », « client-serveur autoritaire pour un compétitif » · **Cross-refs** : 1543, 1545, 1549 · **Tags** : 2027

## 1545. ⏳ Lag compensation : rewind et reconciliation

- **Fichier** : `skills/1545-lag-compensation-rewind-et-reconciliation.md` · **Mot-clé** : « lag compensation rewind 200 ms serveur état monde en arrière réconciliation » · **Nom court** : Lag comp
- **Signal** : Implémenter la lag compensation en 2027 pour un jeu de tir : quand un joueur tire, le serveur rejoue l'état du monde 200 ms en arrière (à la latence du tireur) pour voir si le tir touche, puis réconcilie. Utilise pour les hitscan compétitifs. N'utilise pas pour un jeu au tour par tour. · **Synonymes** : « le serveur rejoue le monde 200 ms en arrière au tir », « toucher quelqu'un qui a déjà bougé (lag) », « réconciliation serveur après coup » · **Cross-refs** : 1544, 1547, 1543 · **Tags** : 2027

## 1546. 🔁 Lockstep vs snapshot interpolation

- **Fichier** : `skills/1546-lockstep-vs-snapshot-interpolation.md` · **Mot-clé** : « lockstep RTS déterministe vs snapshot interpolation 20 Hz action » · **Nom court** : Lockstep/snapshot
- **Signal** : Choisir le modèle de synchro réseau en 2027 : lockstep (RTS : tous les joueurs envoient leurs inputs au même tick, déterministe, mais un joueur lent bloque tous) vs snapshot interpolation (action : le serveur envoie des snapshots d'état à 20 Hz, le client interpole entre les 2 derniers pour rendre à 60+ fps). Utilise selon le genre. N'utilise pas pour le solo. · **Synonymes** : « RTS en lockstep : inputs au même tick déterministe », « action : snapshots serveur 20 Hz interpolés client », « un joueur lent bloque tout en lockstep » · **Cross-refs** : 1544, 1547, 1501 · **Tags** : 2027

## 1547. 🔮 Prediction client et reconciliation serveur

- **Fichier** : `skills/1547-prediction-client-et-reconciliation-serveur.md` · **Mot-clé** : « prédiction client input immédiat reconciliation rejouer inputs non ack » · **Nom court** : Prédiction
- **Signal** : Implémenter la prédiction côté client en 2027 : le client simule localement son personnage dès l'input (réponse instantanée), envoie l'input au serveur; à la réception de l'état serveur (ack), si divergence → réconcilier (rejouer les inputs non acquittés par-dessus l'état serveur). Utilise pour tout jeu d'action en ligne. N'utilise pas pour un tour par tour. · **Synonymes** : « mon perso répond instantanément malgré 100 ms de ping », « réconciliation : état serveur + rejouer mes inputs non ack », « input sequence number et acquittement serveur » · **Cross-refs** : 1546, 1545, 1544 · **Tags** : 2027

## 1548. 💬 Chat in-game et moderation automatique

- **Fichier** : `skills/1548-chat-in-game-et-moderation-automatique.md` · **Mot-clé** : « chat in-game filtre vulgarité anti-spam signalement mute ban vote » · **Nom court** : Chat in-game
- **Signal** : Ajouter un chat in-game en 2027 : chat texte (général/équipe/privé), filtre de vulgarité (liste + LLM léger 1490), anti-spam (rate limit 1 msg/2 s), signalement + mute/ban par les joueurs (vote), modération auto des insultes, conformité mineurs (1587). Utilise pour tout jeu multi. N'utilise pas pour un chat vocal (1569). · **Synonymes** : « filtrer les insultes automatiquement », « rate limit 1 message 2 secondes anti-spam », « signaler un joueur toxique → mute/ban vote » · **Cross-refs** : 1490, 1543, 1587 · **Tags** : 2027

## 1549. 🎯 Matchmaking : ELO/MMR simple et files d'attente

- **Fichier** : `skills/1549-matchmaking-elo-mmr-simple-et-files-d-attente.md` · **Mot-clé** : « matchmaking MMR ELO file d'attente plage élargie avec attente ±100 ±400 » · **Nom court** : Matchmaking
- **Signal** : Implémenter un matchmaking en 2027 : chaque joueur a un MMR (ELO) qui monte/gagne (+25) ou descend (-25) selon victoire/défaite et écart de niveau; file d'attente qui élargit la plage de MMR acceptée avec le temps d'attente (30 s → ±100, 2 min → ±400); évite les smurfs (1543). Utilise pour tout jeu compétitif classé. N'utilise pas pour du coop casual (1544). · **Synonymes** : « MMR qui monte de 25 si victoire », « file qui accepte ±100 après 30 s ±400 après 2 min », « match trouvé en moins de 2 min » · **Cross-refs** : 1544, 1543, 1540 · **Tags** : 2027

## 1550. 🧩 ECS : composition vs heritage pour le gameplay

- **Fichier** : `skills/1550-ecs-composition-vs-heritage-pour-le-gameplay.md` · **Mot-clé** : « ECS entity component system composants données pures systèmes logique composition » · **Nom court** : ECS gameplay
- **Signal** : Organiser le code gameplay en ECS (Entity Component System) en 2027 (complète 1140) : entités = identifiants, composants = données pures (Position, Health, Velocity), systèmes = logique (MovementSystem itère sur les entités avec Position+Velocity). Avantage : composition flexible (un ennemi = Position+Health+AI, pas d'héritage), cache-friendly. Utilise pour les jeux à beaucoup d'entités. N'utilise pas pour un petit jeu (classes suffisent). · **Synonymes** : « composants = données pures », « systèmes = logique », « pas d'héritage : un ennemi = Position + Health + AI », « Unity DOTS / Flecs / Bevy ECS 2027 » · **Cross-refs** : 1140, 1551, 84 · **Tags** : 2027

## 1551. ♻️ Object pooling : reutiliser les objets

- **Fichier** : `skills/1551-object-pooling-reutiliser-les-objets.md` · **Mot-clé** : « object pooling pré-allouer réutiliser éviter GC Instantiate Destroy » · **Nom court** : Object pool
- **Signal** : Implémenter un object pool en 2027 : au lieu de Instantiate/Destroy (allocations GC, pics de lag), un pool pré-alloue N objets (balles, ennemis, particules), les 'désactive' (inactif) et les réutilise. Utilise pour tout ce qui spawn/despawn souvent. N'utilise pas pour des objets uniques rares. · **Synonymes** : « ne plus Instantiate/Destroy à chaque tir (GC lag) », « pool de 50 balles pré-allouées réutilisées », « Get() depuis le pool », « Release() retour au pool » · **Cross-refs** : 1550, 308, 1552 · **Tags** : 2027

## 1552. 📊 Profilage memoire et CPU du jeu

- **Fichier** : `skills/1552-profilage-memoire-et-cpu-du-jeu.md` · **Mot-clé** : « profiler jeu Unity Profiler Memory Profiler fuites draw calls CPU render » · **Nom court** : Profilage
- **Signal** : Profiler un jeu en 2027 pour trouver les fuites et goulots : Unity Profiler / Godot debugger, Memory Profiler (fuites, allocations/frame), CPU (quel système prend 8 ms ?), render (draw calls, overdraw), captures comparatives avant/après. Utilise quand le jeu rame ou fuite. N'utilise pas sans symptôme (ne pas over-optimiser). · **Synonymes** : « fuite mémoire : +50 Mo par niveau chargé », « quel système prend 8 ms de CPU ? », « draw calls 2000 → batching pour passer à 200 » · **Cross-refs** : 308, 309, 1551 · **Tags** : 2027

## 1553. 🖼️ Draw calls : batching, atlas et occlusion culling

- **Fichier** : `skills/1553-draw-calls-batching-atlas-et-occlusion-culling.md` · **Mot-clé** : « draw calls sprite atlas batching statique SRP Batcher occlusion culling LOD » · **Nom court** : Draw calls
- **Signal** : Réduire les draw calls en 2027 : chaque objet affiché = 1 draw call (2000 objets = 2000 appels GPU lents). Solutions : sprite atlas (1554, tout dans 1 texture = 1 draw call), batching statique (objets immobiles fusionnés), SRP Batcher (Unity), occlusion culling (ne pas rendre ce qui est caché), LOD (loin = modèle simple). Utilise quand le render rame. N'utilise pas avant d'avoir profilé (1552). · **Synonymes** : « 2000 objets = 2000 draw calls trop lent », « sprite atlas tout en 1 texture = 1 draw call », « occlusion culling ne pas rendre caché + LOD loin » · **Cross-refs** : 1552, 1554, 309 · **Tags** : 2027

## 1554. 🖼️ Sprite atlas : packer les sprites en 1 texture

- **Fichier** : `skills/1554-sprite-atlas-packer-les-sprites-en-1-texture.md` · **Mot-clé** : « sprite atlas packer sprites 1 texture 2048 padding bleed réduire draw calls » · **Nom court** : Sprite atlas
- **Signal** : Créer un sprite atlas en 2027 : packer des centaines de sprites (personnages, tuiles, UI) dans 1-4 grosses textures (2048x2048 ou 4096) avec marges (bleed 2 px) et padding (éviter le bleeding), via l'éditeur (Unity Sprite Atlas, Godot atlas) ou TexturePacker. Réduit les draw calls (1553) et la mémoire. Utilise pour tout jeu 2D/UI. N'utilise pas pour la 3D (textures de modèles). · **Synonymes** : « packer 500 sprites dans 2 textures 2048x2048 », « padding 2 px éviter le bleeding entre sprites », « TexturePacker ou atlas intégré au moteur » · **Cross-refs** : 1553, 1048, 1512 · **Tags** : 2027

## 1555. 🌟 Post-processing : vignette, grain, bloom legers

- **Fichier** : `skills/1555-post-processing-vignette-grain-bloom-legers.md` · **Mot-clé** : « post-processing vignette grain bloom chromatic aberration 1 passe mobile » · **Nom court** : Post-FX
- **Signal** : Ajouter du post-processing en 2027 sans tuer les perfs (complète les shaders 1270) : vignette (assombrir les bords), grain (bruit film), bloom léger (lumières qui débordent), chromatic aberration (impact), en un seul passe GPU sur mobile (URP/HDRP), profilé (1552). Utilise pour le look final. N'utilise pas si ça fait passer sous 60 fps. · **Synonymes** : « vignette + grain pour le look film », « bloom léger sur les lumières sans lag », « 1 seul passe post-FX sur mobile (URP) » · **Cross-refs** : 1270, 1552, 1553 · **Tags** : 2027

## 1556. 💡 Eclairage 2D : lights, ombres et normal maps

- **Fichier** : `skills/1556-eclairage-2d-lights-ombres-et-normal-maps.md` · **Mot-clé** : « éclairage 2D lights occluders ombres normal map 2D torches » · **Nom court** : Lumière 2D
- **Signal** : Ajouter de l'éclairage 2D en 2027 (Godot 2D lights, Unity URP 2D lights) : sources de lumière (ponctuelles, directionnelles), occlusion des ombres (les murs bloquent la lumière via raycast 1524 ou light occluders), normal maps 2D (texture de normales pour l'effet de relief), blend additif. Utilise pour l'ambiance (donjon sombre, torches). N'utilise pas pour un jeu 2D plat sans ambiance. · **Synonymes** : « torches qui éclairent et les murs font ombre », « normal map 2D pour le relief des sprites », « light occluders bloquent la lumière 2D » · **Cross-refs** : 1524, 1512, 1555 · **Tags** : 2027

## 1557. ✨ Particules GPU : instancing pour milliers de particules

- **Fichier** : `skills/1557-particules-gpu-instancing-pour-milliers-de-particules.md` · **Mot-clé** : « particules GPU instancing VFX Graph compute buffer 5000 particules 1 draw call » · **Nom court** : Particules GPU
- **Signal** : Faire des milliers de particules sans lag en 2027 (complète 1222) : GPU instancing (le GPU dessine N particules en 1 draw call au lieu de N), système de particules custom (spawn, vélocité, gravité, fade, mort) dans un compute buffer ou VFX Graph, cap à 5000 particules. Utilise pour explosions, pluie, foule. N'utilise pas le CPU pour 10k particules. · **Synonymes** : « 10 000 particules en 1 draw call (GPU instancing) », « VFX Graph Unity ou shaders de particules custom », « pluie/neige/explosions sans lag » · **Cross-refs** : 1222, 1553, 1551 · **Tags** : 2027

## 1558. 💥 Screen shake et hit feedback visuel

- **Fichier** : `skills/1558-screen-shake-et-hit-feedback-visuel.md` · **Mot-clé** : « screen shake caméra tremble decay exponentiel intensité explosion dégâts » · **Nom court** : Screen shake
- **Signal** : Ajouter du screen shake en 2027 : la caméra tremble brièvement (0,2 s, amplitude selon l'intensité : explosion forte = 0,5, dégâts reçus = 0,2) avec decay exponentiel, sans nausée (jamais en continu), désactivable (1575). Utilise pour les impacts. N'utilise pas pour la caméra de visée précise (sniper). · **Synonymes** : « caméra qui tremble 0 », « 2 s à l'explosion », « shake fort 0 », « 5 faible 0 », « 2 decay rapide », « désactivable dans l'accessibilité (1575) » · **Cross-refs** : 1506, 1559, 1575 · **Tags** : 2027

## 1559. 🧃 Juice : game feel (squash & stretch, hitstop, particules)

- **Fichier** : `skills/1559-juice-game-feel-squash-stretch-hitstop-particules.md` · **Mot-clé** : « juice game feel squash stretch hitstop 50 ms flash blanc particules » · **Nom court** : Juice
- **Signal** : Ajouter du 'juice' (game feel) en 2027 pour rendre le jeu satisfaisant : squash & stretch (le perso s'écrase à l'atterrissage et s'étire au saut), hitstop (freeze 50 ms à l'impact, 1508), particules à chaque action, flash blanc au hit, son impact, caméra (1558). Règle : le juice ne change pas le gameplay, que la perception. Utilise partout. N'utilise pas pour un jeu sérieux (simulation). · **Synonymes** : « squash & stretch au saut et atterrissage », « hitstop freeze 50 ms à l'impact », « flash blanc + particules + son à chaque hit » · **Cross-refs** : 1558, 1508, 1557 · **Tags** : 2027

## 1560. 🎭 State machine d'animation (Animator)

- **Fichier** : `skills/1560-state-machine-d-animation-animator.md` · **Mot-clé** : « state machine animation Animator états transitions conditions crossfade » · **Nom court** : Anim FSM
- **Signal** : Organiser les animations d'un personnage en 2027 avec une state machine : états (Idle, Run, Jump, Attack, Hit, Death), transitions avec conditions (vitesse supérieur à 0,1 → Run; grounded false → Jump), blend (crossfade 0,1 s), paramètres (float speed, bool grounded, trigger attack). Utilise pour tout personnage animé. N'utilise pas pour une anim linéaire unique. · **Synonymes** : « états Idle Run Jump Attack avec transitions », « condition vitesse superieure a 0 », « 1 passe en Run », « crossfade 0 », « 1 s entre deux animations » · **Cross-refs** : 1561, 1519, 1509 · **Tags** : 2027

## 1561. 🌿 Blend trees : mouvement multidirectionnel fluide

- **Fichier** : `skills/1561-blend-trees-mouvement-multidirectionnel-fluide.md` · **Mot-clé** : « blend tree 2D X Y 9 clips interpoler déplacement 8 directions » · **Nom court** : Blend tree
- **Signal** : Utiliser un blend tree en 2027 pour un déplacement 8 directions fluide : 1 paramètre X (gauche/droite), 1 Y (haut/bas), le blend tree interpole entre 9 clips (idle + 8 directions) selon (X,Y) — plus fluide que des transitions conditionnelles (1560). Utilise pour le déplacement d'un perso 2D/3D. N'utilise pas pour des anims discrètes (attaque). · **Synonymes** : « 9 clips (idle + 8 directions) interpolés selon X Y », « déplacement 3D fluide selon la direction de la caméra », « blend tree 2D vs transitions conditionnelles » · **Cross-refs** : 1560, 1511, 1506 · **Tags** : 2027

## 1562. 🦴 Rigging procédural et IK deux os

- **Fichier** : `skills/1562-rigging-procedural-et-ik-deux-os.md` · **Mot-clé** : « IK inverse kinematics two bone FABRIK pied sol main arme cible » · **Nom court** : IK 2 os
- **Signal** : Faire du rigging procédural en 2027 : IK (Inverse Kinematics) à 2 os (Two Bone IK Unity, FABRIK) pour que le pied/main touche une cible (sol, arme, poignée), sans coder la rotation à la main. Utilise pour les pieds qui suivent le terrain, les mains sur une arme. N'utilise pas pour un humanoïde simple sans IK (1560 suffit). · **Synonymes** : « pieds qui suivent le terrain (IK) », « main qui tient l'arme (IK deux os) », « FABRIK ou Two Bone IK sans coder la rotation » · **Cross-refs** : 1560, 1563, 1564 · **Tags** : 2027

## 1563. 👀 IK avancé : full body et look-at

- **Fichier** : `skills/1563-ik-avance-full-body-et-look-at.md` · **Mot-clé** : « full body IK look-at spine tête regarde ennemi poids IK Unity Final IK » · **Nom court** : Full-body IK
- **Signal** : Aller plus loin que l'IK 2 os en 2027 : Full Body IK (Unity Animator IK, Final IK) pour tout le corps (ajuste hanche/épaule/tête), look-at (la tête regarde un objet/ennemi avec poids), spine IK (torse se penche). Utilise pour des PNJ crédibles. N'utilise pas si 2 os suffisent (1562). · **Synonymes** : « la tête du PNJ regarde le joueur (look-at) », « le torse se penche vers l'objet (spine IK) », « Full Body IK Unity Animator.SetIKPosition » · **Cross-refs** : 1562, 1520, 1560 · **Tags** : 2027

## 1564. 🧸 Ragdoll physique sur un personnage

- **Fichier** : `skills/1564-ragdoll-physique-sur-un-personnage.md` · **Mot-clé** : « ragdoll rigidbody joints charnières mort explosion personnage physique » · **Nom court** : Ragdoll
- **Signal** : Transformer un personnage en ragdoll en 2027 (mort, assommé, explosion) : chaque partie du corps (tête, torse, bras, jambes) devient un rigidbody avec joint (charnière), on applique la force de l'explosion, le perso s'effondre de façon crédible. Utilise à la mort/assommage. N'utilise pas en gameplay normal (anim 1560). · **Synonymes** : « le perso s'effondre crédiblement à la mort », « chaque membre = rigidbody + joint charnière », « explosion projette le ragdoll (AddForce) » · **Cross-refs** : 1562, 1560, 1508 · **Tags** : 2027

## 1565. 💥 Destruction procédurale simple (fracture de mesh)

- **Fichier** : `skills/1565-destruction-procedurale-simple-fracture-de-mesh.md` · **Mot-clé** : « destruction procédurale voronoi fracture mesh morceaux rigidbody » · **Nom court** : Fracture
- **Signal** : Détruire un objet procéduralement en 2027 : couper un mesh en morceaux (Voronoi fracture : N cellules autour de points aléatoires, chaque cellule = 1 mesh avec rigidbody), au lieu de swapper avec un modèle cassé préfait. Utilise pour murs destructibles, glace. N'utilise pas pour la destruction massive (perf, cap 20 morceaux, pool 1551). · **Synonymes** : « mur qui se casse en morceaux Voronoi », « couper un mesh en N morceaux procéduralement », « cap 20 morceaux + pool pour les perfs » · **Cross-refs** : 1564, 1551, 1552 · **Tags** : 2027

## 1566. 🔊 Middleware audio : intégrer FMOD ou Wwise

- **Fichier** : `skills/1566-middleware-audio-integrer-fmod-ou-wwise.md` · **Mot-clé** : « middleware audio FMOD Wwise banques événements bus ducking intégration » · **Nom court** : FMOD/Wwise
- **Signal** : Intégrer un middleware audio en 2027 (complète le mixage 1137) : FMOD Studio ou Wwise (authoring pro : banques, événements, bus, ducking), intégration moteur (Unity/Unreal), événements déclenchés par le gameplay (tir, pas, UI), pas de son direct dans le code. Utilise pour un jeu avec beaucoup de sons. N'utilise pas pour 5 sons simples (AudioSource suffit). · **Synonymes** : « intégrer FMOD Studio dans Unity 2027 », « Wwise authoring banques sons événements », « bus audio ducking (musique baisse quand dialogue) » · **Cross-refs** : 1137, 1568, 1567 · **Tags** : 2027

## 1567. 🎵 Musique adaptative : layers selon l'intensite

- **Fichier** : `skills/1567-musique-adaptative-layers-selon-l-intensite.md` · **Mot-clé** : « musique adaptative layers intensité calme combat boss transitions FMOD » · **Nom court** : Musique adaptative
- **Signal** : Faire une musique adaptative en 2027 (complète la composition 1141) : découper la musique en couches (calme, exploration, combat, boss 1526) + transitions musicales, déclenchées par l'état du jeu (intensité = distance ennemi, PV, phase de boss), via FMOD/Wwise (1566) ou markers + crossfade. Utilise pour l'immersion. N'utilise pas pour un menu statique. · **Synonymes** : « la musique passe en combat quand un ennemi approche », « layers : calm → explore → combat → boss (1526) », « transition musicale douce entre les couches » · **Cross-refs** : 1141, 1566, 1526 · **Tags** : 2027

## 1568. 📢 SFX réactifs : variation de pitch/volume et pooling

- **Fichier** : `skills/1568-sfx-reactifs-variation-de-pitch-volume-et-pooling.md` · **Mot-clé** : « SFX variation pitch volume aléatoire pool voix priorité cooldown anti-spam » · **Nom court** : SFX réactifs
- **Signal** : Rendre les effets sonores réactifs et non répétitifs en 2027 : variation aléatoire de pitch (0,9-1,1) et volume (±3 dB) à chaque joue (sinon effet 'cassette'), pool de 8-16 voix par catégorie (pas d'alloc, 1551), priorité (sons proches de la caméra), cooldown pour éviter le spam (tir = max 10/s). Utilise pour tous les SFX. N'utilise pas pour la musique (1567) ni la VO (1569). · **Synonymes** : « chaque tir a un pitch légèrement différent (0 », « 9-1 », « 1) », « pool de 16 voix pour les tirs (pas d'alloc) », « cooldown : max 10 sons de tir par seconde » · **Cross-refs** : 1566, 1551, 1559 · **Tags** : 2027

## 1569. 🎤 Voix off (VO) : pipeline de doublage

- **Fichier** : `skills/1569-voix-off-vo-pipeline-de-doublage.md` · **Mot-clé** : « VO voix off doublage pipeline IDs lignes sous-titres synchronisés FMOD » · **Nom court** : VO doublage
- **Signal** : Organiser le doublage (VO) d'un jeu en 2027 : script avec IDs de lignes (vo_quest01_03), enregistrement studio (ou TTS IA de secours marqué), fichiers nommés par ID, intégration moteur (FMOD 1566) avec sous-titres synchronisés (1533), priorité VO sur tout, durée max par bulle. Utilise pour tout jeu narratif. N'utilise pas pour les SFX (1568). · **Synonymes** : « enregistrer les voix du jeu en studio (fichiers vo_quest01_03) », « sous-titres synchronisés avec la VO », « TTS IA de secours marqué comme tel » · **Cross-refs** : 1566, 1532, 1533 · **Tags** : 2027

## 1570. 🎯 HUD et minimap : barre de vie, jauge, objectifs

- **Fichier** : `skills/1570-hud-et-minimap-barre-de-vie-jauge-objectifs.md` · **Mot-clé** : « HUD barre de vie minimap réticule notifications désactivable accessibilité » · **Nom court** : HUD
- **Signal** : Concevoir le HUD d'un jeu en 2027 : barre de vie/PV (couleur qui change sous 30 %, 1535), jauge de dash (cooldown 1511), munitions, minimap (1506 caméra, points quête 1531, ennemis 1520 si compétence), réticule contextuel, notifications (loot 1528, succès 1538), tout désactivable (1575). Utilise pour tout jeu avec un personnage. N'utilise pas pour un jeu d'interface pure. · **Synonymes** : « barre de PV rouge qui clignote sous 30 % », « minimap avec marqueurs de quêtes (1531) », « HUD désactivable (mode minimaliste 1575) » · **Cross-refs** : 1531, 1535, 1538 · **Tags** : 2027

## 1571. 🎛️ Menus accessibles : navigation clavier et manette

- **Fichier** : `skills/1571-menus-accessibles-navigation-clavier-et-manette.md` · **Mot-clé** : « menus accessibles clavier manette focus visible navigation directionnelle remap » · **Nom court** : Menus a11y
- **Signal** : Rendre les menus d'un jeu navigables en 2027 au clavier ET à la manette (pas souris seule) : focus visible, ordre de tabulation logique, navigation directionnelle (haut/bas/gauche/droite), valider (Entrée/A), retour (Echap/B), remap des contrôles de menu (1504), test au clavier sans souris. Utilise pour tous les menus. N'utilise pas pour le HUD in-game (1570). · **Synonymes** : « naviguer au clavier dans les menus (tab + entrée) », « focus visible sur le bouton sélectionné », « manette : A valider », « B retour », « croix directionnelle » · **Cross-refs** : 1504, 1575, 1484 · **Tags** : 2027

## 1572. 📖 Tutoriel in-game contextuel et skippable

- **Fichier** : `skills/1572-tutoriel-in-game-contextuel-et-skippable.md` · **Mot-clé** : « tutoriel in-game contextuel skippable rejouable funnel analytics onboarding » · **Nom court** : Tutoriel
- **Signal** : Concevoir un tutoriel in-game en 2027 : astuces contextuelles (pas un texte mural), déclenchées au bon moment (premier saut → astuce coyote 1510), skippable (bouton 'Passer le tutoriel'), rejouable (dans les settings 1574), progression trackée (analytics funnel 1540), pas bloquant (jamais de modale qui bloque le jeu). Utilise pour l'onboarding. N'utilise pas pour un jeu évident (puzzle simple). · **Synonymes** : « astuce qui apparaît au bon moment (premier saut) », « bouton 'Passer le tutoriel' toujours visible », « tutoriel rejouable depuis les settings » · **Cross-refs** : 1540, 1574, 1510 · **Tags** : 2027

## 1573. ⏳ Ecran de chargement et streaming de niveaux

- **Fichier** : `skills/1573-ecran-de-chargement-et-streaming-de-niveaux.md` · **Mot-clé** : « écran de chargement streaming de niveaux zones asynchrone addressables » · **Nom court** : Streaming
- **Signal** : Gérer le chargement de gros niveaux en 2027 sans freeze : écran de chargement dédié (1502) avec barre de progression, chargement asynchrone (LoadSceneAsync / Addressables 1590), streaming par zones (charger la zone autour du joueur, décharger le loin, 100 m), loading prioritaire (visuels d'abord, son après). Utilise pour les mondes ouverts. N'utilise pas pour un petit niveau fixe. · **Synonymes** : « barre de progression au chargement du niveau », « charger la zone autour du joueur », « décharger le loin (100 m) », « monde ouvert sans écran de chargement entre les zones » · **Cross-refs** : 1502, 1590, 1552 · **Tags** : 2027

## 1574. ⚙️ Ecran des reglages : qualité graphique, audio, contrôles

- **Fichier** : `skills/1574-ecran-des-reglages-qualite-graphique-audio-controles.md` · **Mot-clé** : « écran réglages qualité graphique VSync FOV volumes audio remap sensibilité accessibilité » · **Nom court** : Settings
- **Signal** : Concevoir l'écran des réglages d'un jeu en 2027 : qualité graphique (preset Bas/Moyen/Haut + custom : résolution, VSync 1506 FOV, qualité ombres/particules 1557), audio (volumes Master/Music/SFX/VO par slider, 1566), contrôles (remap 1504, sensibilité, invert Y), accessibilité (1575), sauvegarde auto (1503), test des changements en live. Utilise pour tout jeu publiable. N'utilise pas pour un prototype jetable. · **Synonymes** : « preset qualité Bas Moyen Haut + résolution VSync FOV », « sliders de volume Master/Music/SFX/VO séparés », « remap des contrôles + sensibilité + invert Y » · **Cross-refs** : 1504, 1575, 1503 · **Tags** : 2027

## 1575. ♿ Accessibilite d'un jeu : daltonisme, tailles, secousses, sous-titres

- **Fichier** : `skills/1575-accessibilite-d-un-jeu-daltonisme-tailles-secousses-sous.md` · **Mot-clé** : « accessibilité jeu daltonisme filtres tailles textes secousses sous-titres remap couleur seule » · **Nom court** : Accessibilité jeu
- **Signal** : Rendre un jeu accessible en 2027 (WCAG + bonnes pratiques jeu, complément 1484/1495) : filtres daltonisme (protanopie/deutéranopie/tritanopie sur les couleurs critiques PV/ennemis), taille des textes/UI (100-200 %), réduction des secousses (1558) et flashs (1495), sous-titres VO + effets sonores (1533/1569), remap total (1504), pas d'info par couleur seule (formes aussi). Utilise pour tout jeu publiable. N'utilise pas pour un prototype. · **Synonymes** : « filtre daltonisme deutéranopie sur les barres PV/ennemis », « taille de l'UI 100 à 200 % », « réduire les secousses (1558) et les flashs (1495) », « sous-titres des dialogues et des SFX importants » · **Cross-refs** : 1484, 1495, 1558 · **Tags** : 2027

## 1576. 🦩 Support des mods : architecture modable (JSON, scripts)

- **Fichier** : `skills/1576-support-des-mods-architecture-modable-json-scripts.md` · **Mot-clé** : « mods jeu JSON externes API modding Lua dossier /mods sandbox versionning » · **Nom court** : Support mods
- **Signal** : Rendre un jeu modable en 2027 : données de jeu (objets 1535, quêtes 1531, équilibrage 1529) en JSON externes (pas hardcodés), API de modding (Lua/Python embarqué ou événements exposés), dossier /mods chargé au boot, versionning des mods (compatible v1.2), sandbox (pas d'accès disque/réseau), liste des mods dans les settings (1574) avec on/off. Utilise pour la longévité (Skyrim, Minecraft). N'utilise pas si le code est fermé volontairement. · **Synonymes** : « données du jeu en JSON modifiables (armes », « quêtes) », « dossier /mods chargé au boot avec liste on/off », « API Lua pour les mods + sandbox sécurité » · **Cross-refs** : 1531, 1535, 1574 · **Tags** : 2027

## 1577. 💻 Console de commandes et cheats de dev

- **Fichier** : `skills/1577-console-de-commandes-et-cheats-de-dev.md` · **Mot-clé** : « console de commandes dev god give tp killall timescale autocomplétion » · **Nom court** : Dev console
- **Signal** : Ajouter une console de commandes en 2027 (touche² ou /) pour le dev : commandes utiles (god, noclip, give gold 1529, tp x y, killall ennemis 1519, setlevel 1530, timescale 0,5 pour debug slow-mo, screenshot), autocomplétion, historique (flèches), log. Cachée en prod (flag build) ou réservée (1543 anti-triche). Utilise pendant le développement et les tests. N'utilise pas en prod compétitif. · **Synonymes** : « console / avec god noclip give tp killall », « timescale 0 », « 5 pour déboguer au ralenti », « cachée en build release (anti-triche 1543) » · **Cross-refs** : 1543, 1552, 1530 · **Tags** : 2027

## 1578. 📅 Versioning des builds et changelog joueur

- **Fichier** : `skills/1578-versioning-des-builds-et-changelog-joueur.md` · **Mot-clé** : « versioning builds SemVer 1.2.3 changelog patch notes branches Steam beta » · **Nom court** : Versioning
- **Signal** : Versionner proprement un jeu en 2027 : SemVer (1.2.3 : majeur/mineur/patch), build number auto (CI 1593), changelog public (patch notes joueur lisibles, 1579), branches Steam (beta/par défaut 1581), downgrade possible (branche 'previous'), compatibilité des saves (migration 1503). Utilise pour tout jeu en live ops (1542). N'utilise pas pour un prototype. · **Synonymes** : « SemVer 1.2.3 : quoi en majeur mineur patch ? », « patch notes publiques lisibles par les joueurs », « branche beta Steam pour tester avant prod (1581) » · **Cross-refs** : 303, 1581, 1503 · **Tags** : 2027

## 1579. 🎮 Publication sur Steam : builds, depots et mise en ligne

- **Fichier** : `skills/1579-publication-sur-steam-builds-depots-et-mise-en-ligne.md` · **Mot-clé** : « publier sur Steam SteamPipe builds dépôts page store CI Steamworks » · **Nom court** : Steam publish
- **Signal** : Publier un jeu sur Steam en 2027 : Steamworks SDK (1581), SteamPipe pour uploader les builds (branches 1578), configurer les dépôts (fichiers par OS), la page store (1582), les builds automatiques CI (1593), validation Steam (checklist), prix et régions, sortie en accès anticipé ou 1.0. Utilise quand le jeu est prêt. N'utilise pas pour itch.io (1584) ou mobile. · **Synonymes** : « uploader un build Steam avec SteamPipe (branches 1578) », « configurer les dépôts (fichiers Windows/Mac/Linux) », « checklist de validation Steam avant mise en ligne » · **Cross-refs** : 1581, 1582, 1593 · **Tags** : 2027

## 1580. 🏆 Steamworks : succes, leaderboards, cloud saves, lobby

- **Fichier** : `skills/1580-steamworks-succes-leaderboards-cloud-saves-lobby.md` · **Mot-clé** : « Steamworks API succès leaderboards cloud lobby matchmaking invitations overlay DLC » · **Nom court** : Steamworks
- **Signal** : Exploiter l'API Steamworks en 2027 (complète 1579) : succès (1538) avec stats, leaderboards (scores globaux/amis, upload/download), cloud saves (1539), lobby + matchmaking Steam (1549), invitations amis, overlay (Shift+Tab), DLC. Utilise pour un jeu Steam. N'utilise pas pour d'autres plateformes (1584/1590). · **Synonymes** : « leaderboard Steam (top 100 mondial + amis) », « cloud saves Steam (1539) + succès (1538) », « lobby Steam + invitation ami + matchmaking 1549 » · **Cross-refs** : 1579, 1538, 1539 · **Tags** : 2027

## 1581. 🎪 Page store et marketing d'un jeu (Steam, itch)

- **Fichier** : `skills/1581-page-store-et-marketing-d-un-jeu-steam-itch.md` · **Mot-clé** : « page store Steam captures GIF vidéo tags prix wishlist démo marketing jeu » · **Nom court** : Store page
- **Signal** : Concevoir la page store d'un jeu en 2027 (Steam 1579, itch 1584, Epic) : accroche en 1 phrase, GIF/vidéo de gameplay (10-15 s) en 1er, 8-10 captures ordonnées (loop → combat → récompense 1528), description courte (3-5 lignes) + longue, tags pertinents (max 20), prix psychologique (9,99/14,99/19,99 €), régions, démo gratuite, wishlist (objectif 20k avant launch). Utilise avant la mise en ligne. N'utilise pas pour le marketing post-launch (1596). · **Synonymes** : « 10 captures d'écran ordonnées (loop → combat) », « prix psychologique 9 », « 99 14 », « 99 19 », « 99 € », « objectif 20 000 wishlists avant le lancement » · **Cross-refs** : 1579, 1584, 1597 · **Tags** : 2027

## 1582. 📱 Monetisation mobile éthique : pub rewarded et IAP

- **Fichier** : `skills/1582-monetisation-mobile-ethique-pub-rewarded-et-iap.md` · **Mot-clé** : « monétisation mobile éthique rewarded IAP cosmétique pas pay-to-win dark patterns » · **Nom court** : Monétisation éthique
- **Signal** : Monétiser un jeu mobile en 2027 sans dark patterns (régulé UE 2027) : publicité rewarded (choisie par le joueur, jamais forcée, max 3/jour), IAP cosmétiques uniquement (jamais pay-to-win, 1585), pas de pop-up agressive, prix transparents, remboursement facile, mineurs protégés (1587). Utilise pour un F2P mobile. N'utilise pas pour un jeu premium payant (prix fixe 1581). · **Synonymes** : « pub rewarded choisie par le joueur max 3/jour », « IAP cosmétiques uniquement jamais pay-to-win », « pas de pop-up forcée (dark patterns interdits UE 2027) » · **Cross-refs** : 1585, 1586, 1587 · **Tags** : 2027

## 1583. 📦 Gacha et loot boxes : conformite legale en

- **Fichier** : `skills/1583-gacha-et-loot-boxes-conformite-legale-en.md` · **Mot-clé** : « gacha loot box conformité légale 2027 taux affichés pity Belgique interdit mineurs » · **Nom court** : Gacha légal
- **Signal** : Concevoir des loot boxes/gacha conformes en 2027 : en Belgique/Pays-Bas interdits sans licence; ailleurs : taux affichés obligatoires (probabilités exactes des raretés 1528), pas de 'presque gagné' trompeur, pas de ciblage des mineurs (1587), achats via monnaie virtuelle interdits d'être opaque (prix en € clair), pity (1528) obligatoire. Utilise quand le jeu a du gacha. N'utilise pas pour des IAP directs sans hasard (1585). · **Synonymes** : « taux de drop affichés obligatoires (1528) dans le gacha », « Belgique/Pays-Bas : loot box interdite sans licence 2027 », « pas de ciblage des mineurs (1587) par le gacha » · **Cross-refs** : 1528, 1587, 1582 · **Tags** : 2027

## 1584. ⚖️ RGPD et protection des mineurs dans un jeu video

- **Fichier** : `skills/1584-rgpd-et-protection-des-mineurs-dans-un-jeu-video.md` · **Mot-clé** : « RGPD jeu vidéo mineurs consentement parental moins de 16 ans pas de pub ciblée droit effacement » · **Nom court** : RGPD mineurs
- **Signal** : Appliquer le RGPD et la protection des mineurs à un jeu en 2027 : consentement parental vérifiable moins de 16 ans (13 ans FR) pour compte/chat/multi (1548), minimisation des données (analytics 1540 anonymisés), pas de pub ciblée sur les mineurs (1582), DPO si gros studio, registre des traitements, droit à l'effacement (1503 saves cloud 1539), modération renforcée (1548). Utilise pour tout jeu en ligne. N'utilise pas pour un jeu 100 % offline solo. · **Synonymes** : « consentement parental vérifiable pour les moins de 16 ans (13 en France) », « analytics anonymisés pas de tracking des mineurs (1540) », « droit à l'effacement des données d'un compte mineur » · **Cross-refs** : 1455, 1226, 1540 · **Tags** : 2027

## 1585. 🔋 Performance mobile : 60 fps, batterie et thermique

- **Fichier** : `skills/1585-performance-mobile-60-fps-batterie-et-thermique.md` · **Mot-clé** : « performance mobile 60 fps batterie thermique ASTC draw calls LOD throttling » · **Nom court** : Perf mobile
- **Signal** : Optimiser un jeu mobile pour 60 fps stables en 2027 : profiler (1552) sur appareil réel (pas émulateur), réduire draw calls (1553), particules GPU cap (1557), pas d'alloc par frame (pooling 1551), textures compressées (ASTC/ETC2), modèle LOD (1553), limiter la fréquence CPU/GPU (QualitySettings), surveiller batterie/thermique (throttling après 10 min). Utilise avant sortie mobile. N'utilise pas pour PC/console. · **Synonymes** : « 60 fps stables sur téléphone milieu de gamme », « textures ASTC compressées (mémoire GPU divisée) », « throttling thermique après 10 min de jeu » · **Cross-refs** : 1552, 1553, 1590 · **Tags** : 2027

## 1586. 📦 Build mobile : IL2CPP, Addressables, taille de l'app

- **Fichier** : `skills/1586-build-mobile-il2cpp-addressables-taille-de-l-app.md` · **Mot-clé** : « build mobile IL2CPP Addressables ASTC taille APK sous 150 Mo stripping crashlytics » · **Nom court** : Build mobile
- **Signal** : Préparer un build mobile propre en 2027 : IL2CPP (au lieu de Mono, + rapide, + petit, mais build long), Addressables (chargement à la demande, patchs petits, streaming 1573), compression des assets (ASTC 1585, audio OGG/Vorbis), taille cible sous 150 Mo (store), stripping du code (managed stripping), symboles de crash (Crashlytics/Firebase). Utilise avant chaque release mobile. N'utilise pas pour PC (1579). · **Synonymes** : « IL2CPP au lieu de Mono (build plus lent mais app plus rapide) », « Addressables pour des patchs de 5 Mo au lieu de 200 Mo », « taille de l'app inferieure a 150 Mo (ASTC + OGG + stripping) » · **Cross-refs** : 1585, 1573, 1590 · **Tags** : 2027

## 1587. 🎮 Portage console : Switch, PS5, Xbox et certification

- **Fichier** : `skills/1587-portage-console-switch-ps5-xbox-et-certification.md` · **Mot-clé** : « portage console Switch PS5 Xbox certification TRC XR kit de dev éditeur » · **Nom court** : Portage console
- **Signal** : Porter un jeu sur console en 2027 (Switch/PS5/Xbox) : kit de dev éditeur (demandeEarly), adapté l'UI à la manette (1571) et à la TV (distance 3 m, textes gros), perfs cibles (Switch 30/60 fps, PS5/Xbox 60), gestion mémoire (Switch 4 Go partagés), certification TRC/XR (checklist éditeur : pas de crash, sauvegardes OK 1539, succès console), délai 2-4 semaines. Utilise quand un éditeur est intéressé (1594). N'utilise pas pour PC/mobile. · **Synonymes** : « demander le kit de dev Nintendo/Sony/Microsoft », « certification TRC (Nintendo) / XR (Xbox) : checklist 2 semaines », « Switch : 30 fps et 4 Go de RAM partagés », « UI manette TV » · **Cross-refs** : 1585, 1571, 1594 · **Tags** : 2027

## 1588. 💷 Soldes Steam et prix regionaux

- **Fichier** : `skills/1588-soldes-steam-et-prix-regionaux.md` · **Mot-clé** : « soldes Steam saisonniers prix régionaux localisés -50 % Inde Brésil Turquie » · **Nom court** : Soldes/prix
- **Signal** : Gérer les soldes et le prix régional d'un jeu PC en 2027 : soldes Steam saisonniers (Spring/Summer/Autumn/Winter, -30 à -50 % sur un jeu bien noté 1589), règles (pas de solde sous 30 jours après sortie, cooldown 30 j entre soldes), prix localisés par région (Steam recommande -30 à -70 % selon pouvoir d'achat : Inde, Brésil, Turquie...), personnages regional pricing. Utilise pour la stratégie de revenus. N'utilise pas pour le mobile (1582). · **Synonymes** : « soldes Steam printemps été automne hiver -50% », « prix régional Steam : -70% en Inde Turquie Brésil », « pas de solde dans les 30 jours après la sortie » · **Cross-refs** : 1581, 1589, 1582 · **Tags** : 2027

## 1589. 💬 Gerer les avis negatifs et une crise post-lancement

- **Fichier** : `skills/1589-gerer-les-avis-negatifs-et-une-crise-post-lancement.md` · **Mot-clé** : « avis négatifs Steam répondre hotfix 48 h crise post-lancement communication » · **Nom court** : Avis/crise
- **Signal** : Gérer les avis Steam négatifs et une mini-crise post-lancement en 2027 : ne pas supprimer (interdit), répondre publiquement et calmement aux avis techniques (en moins de 24 h), prioriser les bugs bloquants (hotfix 1578 sous 48 h), communiquer (devlog 1596 + patch notes claires), ne pas acheter d'avis. Utilise quand le lancement se passe mal. N'utilise pas pour la communication marketing normale (1596). · **Synonymes** : « répondre aux avis Steam négatifs en 24 h calmement », « hotfix sous 48 h si bug bloquant au lancement », « devlog transparent (1596) + patch notes claires (1578) » · **Cross-refs** : 1578, 1596, 1540 · **Tags** : 2027

## 1590. 📥 Addressables et DLC : contenu telechargeable et patchs

- **Fichier** : `skills/1590-addressables-et-dlc-contenu-telechargeable-et-patchs.md` · **Mot-clé** : « Addressables DLC contenu téléchargeable patchs remote bundle cache versioning » · **Nom court** : Addressables/DLC
- **Signal** : Gérer le contenu téléchargeable d'un jeu en 2027 avec Addressables (Unity) : assets adressables (groupés local vs remote), chargement à la demande (streaming 1573, VO 1569), patchs de contenu sans re-télécharger l'app (1586), DLC (vérification Steam 1580 possédé, contenu débloqué), versioning des bundles (cache invalidé proprement). Utilise pour un jeu avec mises à jour/DLC. N'utilise pas pour un petit jeu statique. · **Synonymes** : « patch de 5 Mo sans re-télécharger les 150 Mo (Addressables) », « DLC vérifié via Steam (1580) puis contenu débloqué », « groupes remote : VO (1569) », « textures HD », « niveaux (1573) » · **Cross-refs** : 1586, 1573, 1580 · **Tags** : 2027

## 1591. 🧪 Tests automatises de gameplay (playmode tests)

- **Fichier** : `skills/1591-tests-automatises-de-gameplay-playmode-tests.md` · **Mot-clé** : « tests automatisés gameplay playmode Unity Test Framework CI régressions » · **Nom court** : Tests auto
- **Signal** : Automatiser les tests d'un jeu en 2027 : playmode tests (Unity Test Framework / Godot GUT) qui lancent une scène, simulent des inputs (1504), vérifient (PV après dégâts 1508, save/load 1503, quête 1531), en CI (1593) à chaque PR; tests unitaires sur la logique pure (économie 1529, formules dégâts). Utilise pour éviter les régressions. N'utilise pas pour le game feel (test humain). · **Synonymes** : « playmode test : simuler un tir et vérifier les PV (1508) », « test save/load (1503) : round-trip identique », « CI qui fait tourner les tests à chaque PR (1593) » · **Cross-refs** : 67, 302, 1593 · **Tags** : 2027

## 1592. 🔄 CI/CD pour un jeu : builds auto multi-plateformes

- **Fichier** : `skills/1592-ci-cd-pour-un-jeu-builds-auto-multi-plateformes.md` · **Mot-clé** : « CI/CD jeu builds auto multi-plateformes GitHub Actions branche beta Steam tests » · **Nom court** : CI/CD jeu
- **Signal** : Automatiser les builds d'un jeu en 2027 : CI (GitHub Actions 1413, GitLab CI) qui build Windows/Linux/Mac (1579) + Android/iOS (1586) à chaque commit sur main, upload branche beta Steam (1578/1580), tests auto (1591), taille du build checkée (sous 150 Mo 1586), symboles de crash uploadés (1586), notif Discord (1596) en cas d'échec. Utilise dès le début du projet. N'utilise pas pour un prototype jetable. · **Synonymes** : « build auto Windows Linux Mac Android à chaque commit », « upload auto sur la branche beta Steam (1580) », « notif Discord si le build échoue (1596) » · **Cross-refs** : 1413, 1591, 1579 · **Tags** : 2027

## 1593. 🥧 Vertical slice : la tranche verticale de démonstration

- **Fichier** : `skills/1593-vertical-slice-la-tranche-verticale-de-demonstration.md` · **Mot-clé** : « vertical slice 1 niveau poli complet loop final démo éditeur pitch » · **Nom court** : Vertical slice
- **Signal** : Construire un vertical slice en 2027 : 1 niveau complet et poli (pas tout le jeu) montrant le gameplay loop final (exploration → combat 1526 → récompense 1528 → progression 1530), avec graphismes/audio/UI finaux (1570), pour convaincre un éditeur (1594) ou financer (1595). Durée : 2-4 mois. N'utilise pas pour le jeu complet (scope). · **Synonymes** : « 1 niveau final poli pour montrer le jeu (pas un prototype gris) », « le loop complet : exploration → combat → loot → progression », « convaincre un éditeur (1594) avec le vertical slice » · **Cross-refs** : 1594, 1595, 1526 · **Tags** : 2027

## 1594. 📊 Pitch deck pour un editeur de jeux video

- **Fichier** : `skills/1594-pitch-deck-pour-un-editeur-de-jeux-video.md` · **Mot-clé** : « pitch deck éditeur jeu vidéo 10-12 slides démo jouable vertical slice budget équipe » · **Nom court** : Pitch éditeur
- **Signal** : Préparer un pitch deck en 2027 pour un éditeur (EA, Ubisoft, Devolver, Annapurna...) : 10-12 slides (accroche, concept en 1 phrase, pourquoi maintenant, gameplay loop vidéo 1593, marché cible + jeux comparables, équipe, budget demandé 1595, planning, pourquoi VOUS), démo jouable du vertical slice (1593), 15 min de présentation + 15 min de Q/R. Utilise pour obtenir un contrat d'édition. N'utilise pas pour du crowdfunding (1595). · **Synonymes** : « 10-12 slides : accroche concept marché équipe budget planning », « démo jouable du vertical slice (1593) pendant le pitch », « combien demander à l'éditeur (1595) : 200k-2M € selon le scope » · **Cross-refs** : 1593, 1595, 776 · **Tags** : 2027

## 1595. 💰 Budget et planning d'un jeu independant

- **Fichier** : `skills/1595-budget-et-planning-d-un-jeu-independant.md` · **Mot-clé** : « budget planning jeu indé postes équipe mois MVP milestones crowdfunding éditeur » · **Nom court** : Budget indé
- **Signal** : Budgéter et planifier un jeu indé en 2027 : postes (code, art, son, prod, marketing 10-20 %, imprévus 15 %), durée (mois × coût mensuel équipe), paliers de financement (éditeur 1594, crowdfunding, fonds régionaux), scope ajusté au budget (MVP 1593), rythme (milestones mensuels, démo à 6 mois). Utilise avant de signer. N'utilise pas pour un gros studio (budget AAA différent). · **Synonymes** : « combien coûte un jeu indé en 2027 (équipe x mois + marketing + imprévus) », « scope ajusté au budget : MVP (1593) d'abord », « crowdfunding Kickstarter + aides régionales (CNC France) » · **Cross-refs** : 1594, 1593, 775 · **Tags** : 2027

## 1596. 📣 Communaute et devlog : Discord, reseaux, transparence

- **Fichier** : `skills/1596-communaute-et-devlog-discord-reseaux-transparence.md` · **Mot-clé** : « communauté jeu Discord devlog hebdo TikTok GIF transparence playtest 1598 » · **Nom court** : Communauté
- **Signal** : Construire une communauté autour d'un jeu en 2027 : Discord (salons devlog, feedback, bug, rôles), devlog hebdo (ce qui avance, ce qui bloque — transparence), réseaux (TikTok/Bluesky/X : GIF de gameplay 1559 juice, pas que des annonces), newsletter, playtest régulier avec la communauté (1598), modération bienveillante (1548). Utilise dès l'annonce. N'utilise pas pour un jeu secret (NDA). · **Synonymes** : « devlog hebdo honnête (avancées + blocages) », « Discord avec salon #feedback et #bugs », « TikTok : 3 GIF de gameplay par semaine (juice 1559) » · **Cross-refs** : 1598, 1542, 1548 · **Tags** : 2027

## 1597. 🎪 Demo Steam Next Fest et salons de jeu

- **Fichier** : `skills/1597-demo-steam-next-fest-et-salons-de-jeu.md` · **Mot-clé** : « démo Steam Next Fest salon jeu PAX démo gratuite wishlist presse éditeur » · **Nom court** : Démo Next Fest
- **Signal** : Profiter des démos gratuites en 2027 : Steam Next Fest (février/juin/octobre) : soumettre la démo (build 1579 branche démo, 30 min de jeu, pas de NDA), objectif wishlist (1581) + retours joueurs (1598); salons (Pégases, Indie World, PAX) : stand, démo jouable, presse, rendez-vous éditeurs (1594). Utilise pour la visibilité avant la sortie. N'utilise pas après la sortie. · **Synonymes** : « soumettre ma démo au Steam Next Fest (février/juin/oct 2027) », « stand à un salon (PGW », « PAX) : démo jouable + presse », « objectif : 10k wishlists + 500 retours (1598) via la démo » · **Cross-refs** : 1581, 1598, 1594 · **Tags** : 2027

## 1598. 🧪 Playtest organise : recruter, questionnaire, synthèse

- **Fichier** : `skills/1598-playtest-organise-recruter-questionnaire-synthese.md` · **Mot-clé** : « playtest organisé recrutement 8-12 joueurs questionnaire SUS synthèse priorités » · **Nom court** : Playtest
- **Signal** : Organiser un playtest en 2027 : recruter 8-12 joueurs du profil cible (Discord 1596, panel Prolific/UserTesting, itch 1584), session 60 min (30 min jeu libre + 30 min interview), questionnaire (SUS 1483, NPS, questions ouvertes 'qu'est-ce qui t'a frustré ?'), enregistrement (écran + visage consentis, RGPD 1584), synthèse en 1 page avec priorités (bugs 1591, fun, difficulté 1529). Utilise à chaque milestone. N'utilise pas pour le game feel micro (juice 1559 = test interne). · **Synonymes** : « 8-12 testeurs du profil cible (Discord 1596 ou Prolific) », « session 60 min : 30 jeu + 30 interview + questionnaire SUS 1483 », « enregistrement écran+visage avec consentement RGPD (1584) » · **Cross-refs** : 1483, 1596, 1540 · **Tags** : 2027

## 1599. ⚖️ Accessibilite legale des jeux video en Europe

- **Fichier** : `skills/1599-accessibilite-legale-des-jeux-video-en-europe.md` · **Mot-clé** : « European Accessibility Act 2027 jeux vidéo conformité accessibilité rapport CVAA » · **Nom court** : A11y légale UE
- **Signal** : Se mettre en conformité accessibilité des jeux en Europe en 2027 (European Accessibility Act, en vigueur juin 2025, jeux concernés) : jeux utilisables par des personnes handicapées (visuel 1575 filtres daltonisme, moteur 1571 clavier/manette complet, cognitif : tutoriel skippable 1572, temps ajustable, pas d'info par couleur seule), rapport d'accessibilité publié, CVAA-like. Utilise pour tout jeu vendu en UE. N'utilise pas pour un prototype interne. · **Synonymes** : « European Accessibility Act en vigueur juin 2025 pour les jeux (UE) », « rapport d'accessibilité publié avec le jeu », « jeu jouable au clavier seul (1571) et avec lecteur d'écran » · **Cross-refs** : 1575, 1571, 1484 · **Tags** : 2027


---
num: 1546
date_ajout: "2026-11"
nom: "Lockstep vs snapshot interpolation"
emoji: "🔁"
domaine: "Game Dev"
signal: "Choisir le modèle de synchro réseau en 2027 : lockstep (RTS : tous les joueurs envoient leurs inputs au même tick, déterministe, mais un joueur lent bloque tous) vs snapshot interpolation (action : le serveur envoie des snapshots d'état à 20 Hz, le client interpole entre les 2 derniers pour rendre à 60+ fps). Utilise selon le genre. N'utilise pas pour le solo."
mot_cle: "lockstep RTS déterministe vs snapshot interpolation 20 Hz action"
nom_court: "Lockstep/snapshot"
branche: "D1"
synonymes: ["RTS en lockstep : inputs au même tick déterministe", "action : snapshots serveur 20 Hz interpolés client", "un joueur lent bloque tout en lockstep"]
cross_refs: [1544, 1547, 1501]
tags: ["2027"]
depends_on: [1544]
---

## 1546. 🔁 Lockstep vs snapshot interpolation (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir le modèle de synchro en 2027 : lockstep (RTS déterministe : tous les clients envoient leurs inputs au tick N, la sim avance quand tous reçus) vs snapshots (action : serveur 20 Hz, client interpole entre snapshots pour rendre fluide).

**Quand l'utiliser (triggers)** :
- Mon RTS doit être déterministe (replay identique)
- Mon action à 60 fps malgré un serveur à 20 Hz
- Lockstep : si un joueur a 300 ms de ping, le jeu bloque

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur réseau synchro. Tu expliques lockstep (inputs datés par tick, sim déterministe fixed timestep 1501, attente du tick de tous, rubber-banding si retard) vs snapshots (serveur envoie état à 20 Hz, client buffer 100 ms + interpolation entre 2 snapshots, entités prédites localement 1547). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le genre (RTS déterministe vs action temps réel)
- Le tick rate (lockstep 10-20 Hz, snapshots 20-30 Hz)
- La tolérance au lag (RTS 0, action 100-200 ms buffer)

**Méthode** :
1. RTS → lockstep : chaque joueur envoie input(tick); le serveur (ou tous en P2P) attend tous les inputs du tick N pour simuler N (déterminisme = replay).
2. Action → snapshots : serveur simule à 30 Hz, envoie snapshot toutes les 50 ms; client garde les 2 derniers, rend à t-100 ms en interpolant (lerp positions).
3. Lockstep : si un joueur est en retard de 3 ticks, tout le monde attend (ou on avance quand même avec input neutre = rubber band).
4. Snapshots : client prédit son propre perso localement (1547), réconcilie à la réception.
5. Choisir selon le genre et mesurer (ping max acceptable).

**Sorties attendues** :
- Le modèle de synchro choisi et implémenté
- L'interpolation côté client (snapshots) ou le lockstep (RTS)
- Le test avec ping simulé (100/300 ms)

**Exemple de prompt** :
> « Mon RTS doit avoir des replays identiques : passe en lockstep (inputs au tick N, sim déterministe 1501, attente de tous). Mon action à 60 fps avec serveur 20 Hz : snapshots + interpolation client. »

**Cas d'usage** : RTS (lockstep), action/FPS (snapshots). S'articule avec skills 1544 (archi), 1547 (prédiction) et 1501 (fixed timestep).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

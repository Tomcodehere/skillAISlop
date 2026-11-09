---
num: 1545
resume: "Implémenter la lag compensation en 2027 : le serveur garde un historique des états (positions) toutes les 50 ms; au tir d'un joueur à latence L, il rejoue le monde à t-L, teste le hit, applique les dégâts, puis réconcilie les autres joueurs. Étape 1 : Serveur : à chaque tick (20 Hz sim, 50 ms snapshots), stocker snapshot {t, positions, hitboxes} (ring buffer 2 s)."
date_ajout: "2026-11"
nom: "Lag compensation : rewind et reconciliation"
emoji: "⏳"
domaine: "Game Dev"
signal: "Implémenter la lag compensation en 2027 pour un jeu de tir : quand un joueur tire, le serveur rejoue l'état du monde 200 ms en arrière (à la latence du tireur) pour voir si le tir touche, puis réconcilie. Utilise pour les hitscan compétitifs. N'utilise pas pour un jeu au tour par tour."
mot_cle: "lag compensation rewind 200 ms serveur état monde en arrière réconciliation"
nom_court: "Lag comp"
branche: "D1"
synonymes: ["le serveur rejoue le monde 200 ms en arrière au tir", "toucher quelqu'un qui a déjà bougé (lag)", "réconciliation serveur après coup"]
cross_refs: [1544, 1547, 1543]
tags: ["2027"]
depends_on: [1544]
---

## 1545. ⏳ Lag compensation : rewind et reconciliation (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter la lag compensation en 2027 : le serveur garde un historique des états (positions) toutes les 50 ms; au tir d'un joueur à latence L, il rejoue le monde à t-L, teste le hit, applique les dégâts, puis réconcilie les autres joueurs.

**Quand l'utiliser (triggers)** :
- Je tire sur un joueur qui a déjà bougé, ça touche quand même
- Historique des positions toutes les 50 ms côté serveur
- Rejouer le monde à t - latence du tireur

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur réseau tir. Tu stockes un ring buffer d'états (positions de tous les joueurs, timestamp), au tir : t_server - RTT/2 → rewind → raycast (1524) sur cet état → hit ? dégâts → notifier tous (avec réconciliation 1547). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La latence (RTT) de chaque joueur (ping mesuré)
- L'historique des états (ring buffer 2 s, tick 50 ms)
- Les hitboxes des joueurs à chaque état

**Méthode** :
1. Serveur : à chaque tick (20 Hz sim, 50 ms snapshots), stocker snapshot {t, positions, hitboxes} (ring buffer 2 s).
2. Reçu un tir de joueur P à t_recv : latence L = RTT_P/2; état cible = snapshot à t_recv - L.
3. Rejouer : raycast(1524) depuis P dans cet état ancien → touche un joueur Q ? → dégâts à Q (1508).
4. Réponse : envoyer à tous 'P a tiré, Q -30 PV' + à P la confirmation de hit (crosshair rouge).
5. Anti-abus : clamp L à 250 ms max (anti lag switch), vérifier LOS serveur (1543).

**Sorties attendues** :
- La lag compensation fonctionnelle (rewind serveur)
- La réconciliation et le feedback de hit
- Le clamp anti-lag-switch (250 ms)

**Exemple de prompt** :
> « Dans mon FPS, tirer sur un joueur qui court ne touche jamais : ajoute la lag compensation (ring buffer d'états 2 s, rewind à t-RTT/2 au tir, raycast sur l'état ancien). »

**Cas d'usage** : FPS compétitifs, jeux de tir. S'articule avec skills 1544 (archi), 1547 (prédiction) et 1543 (anti-triche).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

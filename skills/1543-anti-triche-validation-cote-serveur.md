---
num: 1543
date_ajout: "2026-11"
nom: "Anti-triche : validation cote serveur"
emoji: "🛡"
domaine: "Game Dev"
signal: "Protéger un jeu multijoueur de la triche en 2027 : le serveur fait autorité (positions, dégâts, scores calculés côté serveur, jamais confiance au client), détection d'anomalies (vitesse impossible, dégâts x10, wallhack = LOS impossible), ban progressif (shadowban), chiffrement des paquets. Utilise pour tout jeu compétitif (1549). N'utilise pas pour un jeu solo (inutile)."
mot_cle: "anti-triche serveur fait autorité détection anomalies shadowban chiffrement"
nom_court: "Anti-triche"
branche: "D23"
synonymes: ["ne jamais faire confiance au client (serveur autorité)", "détecter un aimbot (tirs trop précis trop vite)", "shadowban : banir sans prévenir le tricheur"]
cross_refs: [1544, 1549, 1451]
tags: ["2027"]
depends_on: [1544]
---

## 1543. 🛡 Anti-triche : validation cote serveur (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Protéger un jeu multijoueur en 2027 : serveur autorité (le client envoie des inputs, le serveur calcule positions/dégâts/scores), détection d'anomalies (vitesse/dégâts impossibles, wallhack), ban progressif (warn → shadowban → ban), logs pour revue.

**Quand l'utiliser (triggers)** :
- Des joueurs volent à travers les murs (speedhack)
- Le serveur doit valider tous les dégâts (jamais le client)
- Détecter un aimbot (précision inhumaine)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur sécurité multiplayer. Tu appliques : client = input only (touches), serveur = simulation autoritaire (positions, collisions, dégâts), sanity checks (vitesse max, cadence de tir, LOS pour les dégâts), détection statistique (précision > 95 % sur 100 tirs = suspect). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'architecture réseau (1544)
- Les valeurs limites (vitesse max, dégâts max/s)
- Le système de ban (warn/shadowban/ban)

**Méthode** :
1. Autorité serveur : le client envoie ses inputs (avancer, tirer), le serveur simule et renvoie l'état; le client n'envoie jamais sa position.
2. Sanity checks : vitesse > max*1,5 → ignorer + flag; dégâts > max → clamp; tir sans LOS (1524) → ignorer.
3. Détection : stats (précision, réaction moyenne, mouvement) → score de suspicion; seuils → warn, puis shadowban (joue contre d'autres tricheurs), puis ban.
4. Logs : toutes les anomalies avec replay (enregistrer les 30 dernières secondes).
5. Chiffrement + signature des paquets (pas de MITM).

**Sorties attendues** :
- L'architecture serveur-autorité en place
- Le système de détection + shadowban/ban
- Les logs d'anomalies avec replays

**Exemple de prompt** :
> « Des tricheurs volent dans mon FPS : passe en autorité serveur (client = inputs seuls), sanity checks (vitesse/LOS/dégâts), détection aimbot (précision > 95 %), shadowban puis ban. »

**Cas d'usage** : Jeux compétitifs (FPS, MOBA, MMO PvP). S'articule avec skills 1544 (archi multi), 1549 (matchmaking) et 1451 (DDoS).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1580
nom: "Steamworks : succes, leaderboards, cloud saves, lobby (2027)"
emoji: "🏆"
domaine: "Game Dev"
signal: "Exploiter l'API Steamworks en 2027 (complète 1579) : succès (1538) avec stats, leaderboards (scores globaux/amis, upload/download), cloud saves (1539), lobby + matchmaking Steam (1549), invitations amis, overlay (Shift+Tab), DLC. Utilise pour un jeu Steam. N'utilise pas pour d'autres plateformes (1584/1590)."
mot_cle: "Steamworks API succès leaderboards cloud lobby matchmaking invitations overlay DLC"
nom_court: "Steamworks"
branche: "D21"
synonymes: ["leaderboard Steam (top 100 mondial + amis)", "cloud saves Steam (1539) + succès (1538)", "lobby Steam + invitation ami + matchmaking 1549"]
cross_refs: [1579, 1538, 1539]
tags: ["2027"]
depends_on: [1579]
---

## 1580. 🏆 Steamworks : succes, leaderboards, cloud saves, lobby (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Exploiter Steamworks en 2027 : succès avec stats (1538), leaderboards (upload score, top mondial + amis), cloud saves (1539), lobby/invitations (1544), matchmaking Steam (1549), overlay, et DLC si extension prévue.

**Quand l'utiliser (triggers)** :
- Ajouter un leaderboard 'temps speedrun' (top 100 + amis)
- Cloud saves Steam (1539) et succès (1538) à synchroniser
- Lobby Steam pour inviter un ami (1544)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur intégration Steam. Tu branches le SDK : SteamUserStats (succès 1538, leaderboards FindOrCreate + UploadScore), SteamRemoteStorage (cloud 1539), SteamMatchmaking (lobby create/join, invitations), SteamFriends (liste amis, overlay), DLC via SteamApps. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le SDK Steamworks intégré (1579)
- Les leaderboards à créer (nom, tri, affichage)
- Les succès (1538) et les saves cloud (1539)

**Méthode** :
1. Succès : SteamUserStats.SetAchievement + StoreStats, icônes 64x64, cachés ou non (1538).
2. Leaderboards : FindOrCreateLeaderboard('speedrun', Ascending), UploadScore, Download (global top 100 + amis), afficher UI.
3. Cloud : SteamRemoteStorage FileWrite/FileRead (1539), synchro auto au lancement/fermeture.
4. Lobby : CreateLobby (public/amis), join, liste des membres, host migration (1544), invitation overlay (SteamFriends).
5. DLC : SteamApps.GetDLCCount, possédé → contenu débloqué (cosmétiques).
6. Test : 2 comptes Steam test, vérifier succès/cloud/leaderboard/lobby entre les deux.

**Sorties attendues** :
- Succès + leaderboards + cloud + lobby fonctionnels sur Steam
- L'overlay et les invitations amis
- Le test à 2 comptes validé

**Exemple de prompt** :
> « Ajoute Steamworks au jeu : succès (1538), leaderboard speedrun (top 100 mondial + amis), cloud saves (1539), lobby pour inviter un ami (1544) — teste avec 2 comptes Steam. »

**Cas d'usage** : Jeu Steam PC. S'articule avec skills 1579 (publication), 1538 (succès) et 1539 (cloud).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

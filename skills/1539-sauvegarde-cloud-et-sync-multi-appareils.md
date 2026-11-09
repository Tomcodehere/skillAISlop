---
num: 1539
resume: "Synchroniser les saves dans le cloud en 2027 (Steam Cloud / Play Games / iCloud ou S3 maison) : upload auto à la fermeture, download au lancement, conflit résolu par date (plus récent gagne, notif au joueur), quota 1 Mo, mode offline d'abord. Étape 1 : Offline-first : la save locale (1503) est la source de vérité, le cloud est un miroir."
date_ajout: "2026-11"
nom: "Sauvegarde cloud et sync multi-appareils"
emoji: "☁️"
domaine: "Game Dev"
signal: "Synchroniser les sauvegardes d'un jeu dans le cloud en 2027 : Steam Cloud (1581), Google Play Games, iCloud, ou API maison (S3 + API); upload auto à la fermeture, download au lancement, gestion de conflit (plus récent gagne, ou choix du joueur), quota (1 Mo), offline d'abord. Utilise pour les jeux multi-plateformes. N'utilise pas pour les jeux compétitifs (anti-triche 1543)."
mot_cle: "sauvegarde cloud sync Steam Cloud multi-appareils conflit plus récent"
nom_court: "Save cloud"
branche: "D1"
synonymes: ["sauvegarder dans le cloud automatiquement", "jouer sur PC puis téléphone même progression", "conflit de save : garder le plus récent"]
cross_refs: [1503, 1581, 1576]
tags: ["2027"]
depends_on: [1503]
---

## 1539. ☁️ Sauvegarde cloud et sync multi-appareils (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Synchroniser les saves dans le cloud en 2027 (Steam Cloud / Play Games / iCloud ou S3 maison) : upload auto à la fermeture, download au lancement, conflit résolu par date (plus récent gagne, notif au joueur), quota 1 Mo, mode offline d'abord.

**Quand l'utiliser (triggers)** :
- Ma progression PC se retrouve sur mobile
- Upload auto de la save à la fermeture
- Deux appareils ont joué : garder la save la plus récente

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur backend save. Tu choisis le backend (Steam Cloud si Steam 1581, Play Games/iCloud mobile, ou S3+API maison), tu fais offline-first (save locale 1503 toujours), upload auto, download au boot, et la résolution de conflit par timestamp. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La save locale (1503) et son format
- Le backend cloud choisi
- Le quota (1 Mo) et la politique de conflit

**Méthode** :
1. Offline-first : la save locale (1503) est la source de vérité, le cloud est un miroir.
2. Au lancement : download cloud, comparer timestamps (local vs cloud) → garder le plus récent, notifier si conflit ('save du 12/11 plus récente').
3. À la fermeture/auto : upload la save locale (compressée, < 1 Mo quota), avec retry si offline.
4. Multi-appareils : PC + mobile lisent la même save cloud (même compte plateforme).
5. Chiffrement : TLS en transit, au repos si données sensibles (RGPD 1587).

**Sorties attendues** :
- La sync cloud opérationnelle (upload/download auto)
- La résolution de conflit par timestamp + notif
- Le mode offline-first garanti

**Exemple de prompt** :
> « Synchronise les saves de mon jeu mobile+PC : Steam Cloud (PC) et Play Games (Android), offline-first, upload auto à la fermeture, conflit = save la plus récente gagne avec notif. »

**Cas d'usage** : Jeux multi-plateformes, persistance cross-device. S'articule avec skills 1503 (save locale), 1581 (Steam) et 1576.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

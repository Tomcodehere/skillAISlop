---
num: 1576
date_ajout: "2026-11"
nom: "Support des mods : architecture modable (JSON, scripts)"
emoji: "🦩"
domaine: "Game Dev"
signal: "Rendre un jeu modable en 2027 : données de jeu (objets 1535, quêtes 1531, équilibrage 1529) en JSON externes (pas hardcodés), API de modding (Lua/Python embarqué ou événements exposés), dossier /mods chargé au boot, versionning des mods (compatible v1.2), sandbox (pas d'accès disque/réseau), liste des mods dans les settings (1574) avec on/off. Utilise pour la longévité (Skyrim, Minecraft). N'utilise pas si le code est fermé volontairement."
mot_cle: "mods jeu JSON externes API modding Lua dossier /mods sandbox versionning"
nom_court: "Support mods"
branche: "D1"
synonymes: ["données du jeu en JSON modifiables (armes, quêtes)", "dossier /mods chargé au boot avec liste on/off", "API Lua pour les mods + sandbox sécurité"]
cross_refs: [1531, 1535, 1574]
tags: ["2027"]
depends_on: [1531]
---

## 1576. 🦩 Support des mods : architecture modable (JSON, scripts, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre un jeu modable en 2027 : données (objets 1535, quêtes 1531, équilibres 1529) en JSON externes, API de modding (Lua embarqué ou events exposés), dossier /mods au boot avec liste on/off (1574), sandbox (pas d'accès système), version de compatibilité par mod.

**Quand l'utiliser (triggers)** :
- Les joueurs veulent modifier les dégâts des armes
- Tout en JSON externe (armes/quêtes/prix), pas hardcodé
- Dossier /mods avec mods.json (nom, version, compatible v1.2)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur plateforme mods. Tu externalises les données en JSON (data/items.json...), tu exposes une API (events onKill etc. ou Lua via MoonSharp), tu charges /mods au boot (scan, validation version, sandbox Lua sans io/os), et liste les mods actifs dans les settings (1574). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les données à externaliser (items, quêtes, dialogues, équilibres)
- Le langage de script (Lua MoonSharp, Python)
- La politique de sandbox (pas d'accès disque/réseau)

**Méthode** :
1. Externaliser : items.json, quests.json, balance.json (dégâts, prix 1529) chargés au boot, modifiables par les mods (merge).
2. API : exposer des events (onKill, onQuestComplete) + fonctions safe (dégâts, spawn) via Lua sandbox (whitelist, pas io/os/socket).
3. Dossier /mods : chaque mod = dossier avec mod.json {nom, auteur, version, compatible: '1.2.x'} + fichiers (JSON data + script.lua).
4. Boot : scanner /mods, vérifier compatibilité version, charger data (merge) puis scripts (sandbox), log erreurs sans crash.
5. Settings (1574) : liste des mods avec checkbox on/off, ordre de chargement, 'Ouvrir le dossier mods'.

**Sorties attendues** :
- Le jeu modable (data JSON + API Lua sandbox)
- Le dossier /mods fonctionnel (mod.json, compatibilité)
- La liste des mods on/off dans les settings

**Exemple de prompt** :
> « Rends le jeu modable : sors armes/quêtes/équilibres en JSON (/data), expose une API Lua sandbox (events onKill, fonctions spawn/dégâts, pas d'accès disque), dossier /mods avec mod.json, liste on/off dans les réglages (1574). »

**Cas d'usage** : Longévité du jeu, communauté. S'articule avec skills 1531 (quêtes data), 1535 (items) et 1574 (settings).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

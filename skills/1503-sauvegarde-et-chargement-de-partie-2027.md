---
num: 1503
date_ajout: "2026-11"
nom: "Sauvegarde et chargement de partie (2027)"
emoji: "💾"
domaine: "Game Dev"
signal: "Implémenter la sauvegarde d'une partie en 2027 : sérialisation JSON/binaire des données de jeu (position, inventaire, quêtes, temps de jeu), 3 slots + auto-save, versionning des saves (migration si format change), sauvegarde cloud (1576). Utilise dans tout jeu avec progression. N'utilise pas pour un jeu en ligne compétitif (anti-triche 1543)."
mot_cle: "sauvegarde partie sérialisation JSON slots auto-save versionning"
nom_court: "Save/Load"
branche: "D1"
synonymes: ["3 slots de sauvegarde", "sérialiser l'état du jeu en JSON", "migration de save entre versions"]
cross_refs: [1576, 1539, 601]
tags: ["2027"]
depends_on: [1539]
---

## 1503. 💾 Sauvegarde et chargement de partie (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter un système de sauvegarde en 2027 : sérialisation de l'état complet (position, inventaire, quêtes, stats, temps), 3 slots manuels + auto-save, champ 'version' dans chaque save pour migrer les anciennes sauvegardes.

**Quand l'utiliser (triggers)** :
- Sauvegarder la partie en JSON lisible
- 3 slots + auto-save à chaque checkpoint
- Une vieille save plante après mise à jour : migration

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur systèmes de jeu. Tu définis le schéma de save (version, date, données), la sérialisation (JSON lisible en dev, binaire en prod si gros), les slots, et la migration (charger v1 → convertir → sauver v2). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les données à sauvegarder (inventaire, quêtes, position...)
- Le format (JSON/binaire)
- Les slots (3 manuels + auto) et le cloud (1576)

**Méthode** :
1. Définir le schéma SaveData {version, date, player, monde, quêtes...}.
2. Sérialiser (JSON dev / binaire prod), écrire dans 3 slots + auto-save checkpoint.
3. Charger : lire, vérifier version, migrer si ancien (v1→v2), appliquer.
4. Gérer les erreurs (fichier corrompu → slot vide + log, jamais de crash).
5. Tester : save, quitter, recharger → état identique (checksum).

**Sorties attendues** :
- Le système de save/load fonctionnel (3 slots + auto)
- Le schéma versionné + migration v1→v2
- Le test de round-trip (save→load identique)

**Exemple de prompt** :
> « Ajoute la sauvegarde à mon RPG : sérialise l'état complet en JSON (versionné), 3 slots + auto-save, migration des vieilles saves, test round-trip. »

**Cas d'usage** : Tout jeu avec progression. S'articule avec skills 1576 (save cloud), 1539 (sync multi-appareils) et 601 (session).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

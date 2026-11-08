---
num: 1573
date_ajout: "2026-11"
nom: "Ecran de chargement et streaming de niveaux"
emoji: "⏳"
domaine: "Game Dev"
signal: "Gérer le chargement de gros niveaux en 2027 sans freeze : écran de chargement dédié (1502) avec barre de progression, chargement asynchrone (LoadSceneAsync / Addressables 1590), streaming par zones (charger la zone autour du joueur, décharger le loin, 100 m), loading prioritaire (visuels d'abord, son après). Utilise pour les mondes ouverts. N'utilise pas pour un petit niveau fixe."
mot_cle: "écran de chargement streaming de niveaux zones asynchrone addressables"
nom_court: "Streaming"
branche: "D1"
synonymes: ["barre de progression au chargement du niveau", "charger la zone autour du joueur, décharger le loin (100 m)", "monde ouvert sans écran de chargement entre les zones"]
cross_refs: [1502, 1590, 1552]
tags: ["2027"]
depends_on: [1502]
---

## 1573. ⏳ Ecran de chargement et streaming de niveaux (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Gérer le chargement/streaming en 2027 : écran de chargement avec barre (1502), chargement asynchrone par zones (charger autour du joueur, décharger au-delà de 100 m), priorité visuels > sons > gameplay, monde ouvert sans coupure.

**Quand l'utiliser (triggers)** :
- Mon monde ouvert freeze 3 s entre les zones
- Barre de progression qui avance vraiment (pas bloquée à 90 %)
- Charger/décharger les zones selon la distance au joueur

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur chargement. Tu découpes le monde en zones (grille), au déplacement du joueur : charger (Addressables 1590 / LoadSceneAsync additif 1502) les zones dans un rayon R, décharger celles hors 2R, avec une file prioritaire (la zone du joueur d'abord). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le monde découpé en zones (grille 100 m)
- L'Addressables ou le chargement de scènes additives
- Le rayon de chargement (R=100 m) et déchargement (2R)

**Méthode** :
1. Découper le monde en zones (chunks) avec leur contenu (ennemis 1519, objets, PNJ).
2. Au mouvement du joueur : zone courante + voisines dans R → charger (async, priorité à la zone courante); zones hors 2R → décharger (UnloadSceneAsync).
3. Écran de chargement (1502) au début avec vraie progression (ne bloque pas à 90 % : compter les opérations).
4. Priorité : meshs/colliders d'abord (gameplay jouable vite), puis textures HD, puis sons (1566).
5. Streaming continu : pendant le jeu, précharger en arrière-plan la zone suivante selon la vélocité du joueur (1511).

**Sorties attendues** :
- Le monde ouvert streamé par zones (pas de freeze)
- L'écran de chargement avec progression réelle
- Le préchargement directionnel (vélocité)

**Exemple de prompt** :
> « Mon monde ouvert freeze 3 s à chaque zone : découpe en chunks 100 m, charge async la zone du joueur + voisines (Addressables), décharge hors 200 m, écran de chargement avec vraie barre (1502). »

**Cas d'usage** : Mondes ouverts, gros niveaux. S'articule avec skills 1502 (scènes), 1590 (Addressables) et 1552 (perf mémoire).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

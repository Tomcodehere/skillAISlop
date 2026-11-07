---
num: 1502
date_ajout: "2026-11"
nom: "Gestion des scenes et transitions (2027)"
emoji: "🎬"
domaine: "Game Dev"
signal: "Organiser un jeu en scènes/niveaux en 2027 (existe 1264 sur les scènes Godot) : scène de chargement dédiée, chargement asynchrone (LoadSceneAsync), additifs (menu + HUD + niveau), transitions fondues, persistance entre scènes (singleton/DontDestroyOnLoad). Utilise pour structurer un jeu. N'utilise pas pour un écran unique."
mot_cle: "gestion des scènes chargement asynchrone additif transitions"
nom_court: "Scènes"
branche: "D1"
synonymes: ["charger un niveau sans freeze", "scènes additives menu + hud + niveau", "transition fondu entre niveaux"]
cross_refs: [1264, 1140, 1573]
tags: ["2027"]
depends_on: [1264]
---

## 1502. 🎬 Gestion des scenes et transitions (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Structurer un jeu en scènes en 2027 : scène bootstrap + chargement asynchrone (barre de progression), niveaux chargés en additif (menu/HUD persistants), transitions fondues, données persistantes entre scènes (profil joueur, settings).

**Quand l'utiliser (triggers)** :
- Charger un gros niveau sans freeze (barre de chargement)
- Scènes additives : menu + jeu + HUD en même temps
- Données qui persistent entre les scènes

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur architecture jeu. Tu donnes l'architecture (scène bootstrap légère, scène de loading avec LoadSceneAsync + progress, scènes additives, GameManager en DontDestroyOnLoad avec les données persistantes), et les transitions fondues. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le moteur et sa gestion de scènes
- Les écrans (menu, jeu, pause, game over)
- Les données à persister (profil, settings, progression)

**Méthode** :
1. Scène bootstrap (vide, charge le menu + manager persistant).
2. Écran de chargement avec chargement asynchrone et barre de progression.
3. Niveaux en additif : menu/HUD restent chargés, le niveau se superpose.
4. Transitions : fondu noir 0,3 s entre scènes (pas de coupure).
5. GameManager persistant : profil, settings, sauvegarde, audio.

**Sorties attendues** :
- L'architecture de scènes en place
- Le chargement asynchrone avec barre de progression
- Les transitions et le manager persistant

**Exemple de prompt** :
> « Mon niveau 3 freeze 2 s au chargement : mets en place scènes additives + chargement asynchrone avec barre de progression + transition fondu. »

**Cas d'usage** : Tout jeu multi-écrans. S'articule avec skills 1264 (scènes Godot), 1140 (game loop) et 1573 (écran de chargement/streaming).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

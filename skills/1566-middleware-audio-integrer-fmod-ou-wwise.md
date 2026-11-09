---
num: 1566
resume: "Intégrer FMOD Studio ou Wwise en 2027 : banques de sons, événements audio déclenchés par le gameplay (pas d'AudioSource en dur), bus (Master/Music/SFX/Voix) avec ducking, occlusion (son étouffé derrière un mur, 1524), perfs (limite de voix simultanées). Étape 1 : Créer les banques (armes, pas selon matériau, UI, VO) et les bus (Master/Music/SFX/Voix/Ambiance)."
date_ajout: "2026-11"
nom: "Middleware audio : intégrer FMOD ou Wwise"
emoji: "🔊"
domaine: "Game Dev"
signal: "Intégrer un middleware audio en 2027 (complète le mixage 1137) : FMOD Studio ou Wwise (authoring pro : banques, événements, bus, ducking), intégration moteur (Unity/Unreal), événements déclenchés par le gameplay (tir, pas, UI), pas de son direct dans le code. Utilise pour un jeu avec beaucoup de sons. N'utilise pas pour 5 sons simples (AudioSource suffit)."
mot_cle: "middleware audio FMOD Wwise banques événements bus ducking intégration"
nom_court: "FMOD/Wwise"
branche: "D19"
synonymes: ["intégrer FMOD Studio dans Unity 2027", "Wwise authoring banques sons événements", "bus audio ducking (musique baisse quand dialogue)"]
cross_refs: [1137, 1568, 1567]
tags: ["2027"]
depends_on: [1137]
---

## 1566. 🔊 Middleware audio : intégrer FMOD ou Wwise (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Intégrer FMOD Studio ou Wwise en 2027 : banques de sons, événements audio déclenchés par le gameplay (pas d'AudioSource en dur), bus (Master/Music/SFX/Voix) avec ducking, occlusion (son étouffé derrière un mur, 1524), perfs (limite de voix simultanées).

**Quand l'utiliser (triggers)** :
- Plus de 50 sons gérés à la main (AudioSource partout)
- FMOD Studio : banques + événements + bus
- Le son derrière un mur est étouffé (occlusion)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es sound designer intégration. Tu structures dans FMOD/Wwise : banques par catégorie (armes, UI, VO), bus hiérarchiques (Master → Music/SFX/Voix) avec ducking (musique -6 dB pendant la VO), événements nommés (play_one_shot), occlusion par raycast (1524). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les sons (banques FMOD/Wwise)
- Les événements de gameplay à sonoriser
- Les bus et le ducking souhaités

**Méthode** :
1. Créer les banques (armes, pas selon matériau, UI, VO) et les bus (Master/Music/SFX/Voix/Ambiance).
2. Dans le moteur : FMOD Runtime / Wwise SDK, initialiser, charger les banques au boot.
3. Gameplay : appeler RuntimeManager.PlayOneShot('event:/tir') — jamais d'AudioSource en dur.
4. Ducking : bus Music baisse quand un event VO joue (sidechain).
5. Occlusion : raycast (1524) entre caméra et source → lowpass filter selon obstacles.
6. Limite : max 32 voix simultanées (virtual voice), priorité aux sons proches de la caméra.

**Sorties attendues** :
- FMOD/Wwise intégré (banques + bus + ducking)
- Les événements déclenchés par le gameplay
- L'occlusion sonore et la limite de voix

**Exemple de prompt** :
> « Mon jeu a 200 AudioSource en dur dans le code : migre vers FMOD Studio (banques armes/UI/VO, bus avec ducking musique/VO, events play_one_shot, occlusion par raycast). »

**Cas d'usage** : Jeux avec beaucoup de sons (FPS, action, RPG). S'articule avec skills 1137 (mix), 1568 (SFX) et 1567 (musique adaptative).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

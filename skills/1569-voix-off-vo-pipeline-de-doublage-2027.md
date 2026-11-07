---
num: 1569
date_ajout: "2026-11"
nom: "Voix off (VO) : pipeline de doublage (2027)"
emoji: "🎤"
domaine: "Game Dev"
signal: "Organiser le doublage (VO) d'un jeu en 2027 : script avec IDs de lignes (vo_quest01_03), enregistrement studio (ou TTS IA de secours marqué), fichiers nommés par ID, intégration moteur (FMOD 1566) avec sous-titres synchronisés (1533), priorité VO sur tout, durée max par bulle. Utilise pour tout jeu narratif. N'utilise pas pour les SFX (1568)."
mot_cle: "VO voix off doublage pipeline IDs lignes sous-titres synchronisés FMOD"
nom_court: "VO doublage"
branche: "D19"
synonymes: ["enregistrer les voix du jeu en studio (fichiers vo_quest01_03)", "sous-titres synchronisés avec la VO", "TTS IA de secours marqué comme tel"]
cross_refs: [1566, 1532, 1533]
tags: ["2027"]
depends_on: [1566]
---

## 1569. 🎤 Voix off (VO) : pipeline de doublage (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Organiser la VO d'un jeu en 2027 : lignes scriptées avec IDs (vo_quest01_03) + texte pour les sous-titres (1533), fichiers studio (ou TTS IA de secours marqué), intégration FMOD (1566) avec ducking musique, sous-titres synchronisés, durée max par bulle.

**Quand l'utiliser (triggers)** :
- 500 lignes de dialogue à enregistrer et intégrer
- Sous-titres synchronisés automatiquement avec la VO
- Remplacer une voix manquante par du TTS (marqué)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es sound designer VO. Tu structures : script CSV (id, perso, texte FR, contexte) → studio enregistre → fichiers vo_id.wav + .txt (durées pour sous-titres); intégration FMOD event par id; TTS de secours (ElevenLabs etc.) clairement marqué '[TTS temporaire]'. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le script finalisé (dialogues 1532)
- Le studio (ou TTS de secours)
- Les langues (VO FR + sous-titres 5 langues, 1533)

**Méthode** :
1. Exporter le script en CSV (id, personnage, texte, contexte, durée max) pour le studio.
2. Réception : fichiers vo_id.wav + durée; TTS IA en secours pour les lignes manquantes (marquées).
3. Intégration : FMOD event 'vo_id', ducking musique auto (1566), priorité haute (VO non interruptible).
4. Sous-titres : fichier .srt/.json avec (id, début, fin, texte) → affiché synchro (1533).
5. Contraintes : bulle max 6 s (sinon couper en 2), pas de VO en combat rapide (SFX prioritaires).

**Sorties attendues** :
- Le pipeline VO (script → studio → fichiers → FMOD)
- Les sous-titres synchronisés (5 langues)
- Le TTS de secours marqué pour les lignes manquantes

**Exemple de prompt** :
> « 500 lignes de PNJ à doubler : pipeline VO (CSV id/texte → studio → vo_id.wav, intégration FMOD avec ducking, sous-titres .srt synchronisés en 5 langues, TTS marqué en secours). »

**Cas d'usage** : Jeux narratifs (RPG, aventure). S'articule avec skills 1566 (FMOD), 1532 (dialogues) et 1533 (sous-titres i18n).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

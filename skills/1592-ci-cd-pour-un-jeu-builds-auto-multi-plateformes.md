---
num: 1592
resume: "Automatiser les builds en 2027 : CI (GitHub Actions 1413) buildant Windows/Linux/Mac (1579) + Android/iOS (1586) à chaque commit, tests auto (1591), upload branche beta Steam (1580), check taille, symboles crash (1586), notif Discord (1596) si échec. Étape 1 : CI (GitHub Actions 1413) : job matrix (windows-latest, macos, ubuntu, + android/ios avec actions unity)."
lang: "fr"
date_ajout: "2026-11"
nom: "CI/CD pour un jeu : builds auto multi-plateformes"
emoji: "🔄"
domaine: "Game Dev"
signal: "Automatiser les builds d'un jeu en 2027 : CI (GitHub Actions 1413, GitLab CI) qui build Windows/Linux/Mac (1579) + Android/iOS (1586) à chaque commit sur main, upload branche beta Steam (1578/1580), tests auto (1591), taille du build checkée (sous 150 Mo 1586), symboles de crash uploadés (1586), notif Discord (1596) en cas d'échec. Utilise dès le début du projet. N'utilise pas pour un prototype jetable."
mot_cle: "CI/CD jeu builds auto multi-plateformes GitHub Actions branche beta Steam tests"
nom_court: "CI/CD jeu"
branche: "D1"
synonymes: ["build auto Windows Linux Mac Android à chaque commit", "upload auto sur la branche beta Steam (1580)", "notif Discord si le build échoue (1596)"]
cross_refs: [1413, 1591, 1579]
tags: ["2027"]
depends_on: [1413]
---

## 1592. 🔄 CI/CD pour un jeu : builds auto multi-plateformes (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Automatiser les builds en 2027 : CI (GitHub Actions 1413) buildant Windows/Linux/Mac (1579) + Android/iOS (1586) à chaque commit, tests auto (1591), upload branche beta Steam (1580), check taille, symboles crash (1586), notif Discord (1596) si échec.

**Quand l'utiliser (triggers)** :
- Plus de 'ça marche sur ma machine' : build CI à chaque commit
- Build auto uploadé sur la branche beta Steam (1580)
- Taille du build > 150 Mo = build rouge (1586)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es DevOps jeu. Tu écris le workflow CI : matrix OS (windows/macos/ubuntu + android/ios), Unity -batchmode -quit -executeMethod Build (ou Godot --headless --export), tests (1591) avant build, artefact upload, SteamPipe upload branche beta (1580), check taille (1586), notif (1596). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le moteur (Unity/Godot) et la scène d'entrée
- Les plateformes cibles (PC 1579, mobile 1586, console 1587)
- SteamPipe (1580) et le bot Discord (1596)

**Méthode** :
1. CI (GitHub Actions 1413) : job matrix (windows-latest, macos, ubuntu, + android/ios avec actions unity).
2. Étapes : checkout → cache Library → run tests (1591) → build par plateforme (batchmode) → check taille (< 150 Mo mobile 1586) → upload artefact.
3. Steam : si branche main/release, SteamPipe upload branche beta (1580) + default si tag vX.Y.Z (1578).
4. Échec : notif Discord (1596) avec le log, la PR est bloquée si tests rouges.
5. Cache : Library/ et ~/.cache pour diviser le temps de build par 3.

**Sorties attendues** :
- La CI/CD fonctionnelle (builds auto multi-OS + tests + upload beta)
- Le check taille et les symboles de crash
- La notif Discord en cas d'échec

**Exemple de prompt** :
> « Automatise les builds du jeu Unity : GitHub Actions (1413) matrix Windows/Mac/Linux/Android, tests (1591) avant build, build batchmode, check < 150 Mo (1586), upload branche beta Steam (1580) sur main, notif Discord (1596) si rouge. »

**Cas d'usage** : Toute équipe jeu sérieuse. S'articule avec skills 1413 (CI rapide), 1591 (tests) et 1579 (Steam).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

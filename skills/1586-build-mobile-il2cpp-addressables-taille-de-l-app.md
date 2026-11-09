---
num: 1586
resume: "Préparer un build mobile en 2027 : IL2CPP (perf/taille), Addressables (patchs petits, streaming 1573), ASTC textures (1585), audio OGG, stripping, symboles Crashlytics, taille cible inférieur à 150 Mo, testé sur device (1585). Étape 1 : IL2CPP : backend IL2CPP, ARM64 only, stripping 'Medium/High', build natif (build long OK en CI 1593)."
date_ajout: "2026-11"
nom: "Build mobile : IL2CPP, Addressables, taille de l'app"
emoji: "📦"
domaine: "Game Dev"
signal: "Préparer un build mobile propre en 2027 : IL2CPP (au lieu de Mono, + rapide, + petit, mais build long), Addressables (chargement à la demande, patchs petits, streaming 1573), compression des assets (ASTC 1585, audio OGG/Vorbis), taille cible sous 150 Mo (store), stripping du code (managed stripping), symboles de crash (Crashlytics/Firebase). Utilise avant chaque release mobile. N'utilise pas pour PC (1579)."
mot_cle: "build mobile IL2CPP Addressables ASTC taille APK sous 150 Mo stripping crashlytics"
nom_court: "Build mobile"
branche: "D1"
synonymes: ["IL2CPP au lieu de Mono (build plus lent mais app plus rapide)", "Addressables pour des patchs de 5 Mo au lieu de 200 Mo", "taille de l'app inferieure a 150 Mo (ASTC + OGG + stripping)"]
cross_refs: [1585, 1573, 1590]
tags: ["2027"]
depends_on: [1585]
---

## 1586. 📦 Build mobile : IL2CPP, Addressables, taille de l'app (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Préparer un build mobile en 2027 : IL2CPP (perf/taille), Addressables (patchs petits, streaming 1573), ASTC textures (1585), audio OGG, stripping, symboles Crashlytics, taille cible < 150 Mo, testé sur device (1585).

**Quand l'utiliser (triggers)** :
- L'APK fait 400 Mo, le store limite à 150 Mo
- IL2CPP : build 30 min mais jeu +30 % plus rapide
- Addressables : patch de contenu de 5 Mo sans re-télécharger tout

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur build mobile. Tu configures : Player Settings (IL2CPP, ARM64, stripping level, ASTC), Addressables groups (local vs remote), compression, symboles de crash (dSYM/symbols uploadés), et la taille cible < 150 Mo vérifiée en CI (1593). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le projet Unity (ou autre) et ses assets
- Addressables (groupes local/remote)
- La cible taille (< 150 Mo) et les symboles de crash

**Méthode** :
1. IL2CPP : backend IL2CPP, ARM64 only, stripping 'Medium/High', build natif (build long OK en CI 1593).
2. Addressables : assets adressables (textures HD, niveaux 1573, sons VO 1569 en remote), le reste en local (moteur, UI base).
3. Taille : textures ASTC 6x6 (1585), audio OGG Vorbis, modèles LOD, vidéos en streaming (pas dans l'app).
4. CI (1593) : build auto, upload symboles (Crashlytics), check taille < 150 Mo, test smoke sur device (1585).
5. Store : fiche (1581 mobile), classification d'âge (1584), IAP (1585).

**Sorties attendues** :
- Le build mobile propre (IL2CPP, Addressables, < 150 Mo)
- La CI de build + symboles de crash + check taille
- Le smoke test sur device (1585)

**Exemple de prompt** :
> « Prépare la release Android : passe en IL2CPP ARM64 (stripping), Addressables (niveaux 1573 et VO 1569 en remote), textures ASTC, audio OGG → APK < 150 Mo, CI build + Crashlytics + smoke test device. »

**Cas d'usage** : Release mobile. S'articule avec skills 1585 (perf), 1573 (streaming) et 1593 (CI).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

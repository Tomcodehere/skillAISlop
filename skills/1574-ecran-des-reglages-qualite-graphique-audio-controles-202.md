---
num: 1574
date_ajout: "2026-11"
nom: "Ecran des reglages : qualité graphique, audio, contrôles (2027)"
emoji: "⚙️"
domaine: "Game Dev"
signal: "Concevoir l'écran des réglages d'un jeu en 2027 : qualité graphique (preset Bas/Moyen/Haut + custom : résolution, VSync 1506 FOV, qualité ombres/particules 1557), audio (volumes Master/Music/SFX/VO par slider, 1566), contrôles (remap 1504, sensibilité, invert Y), accessibilité (1575), sauvegarde auto (1503), test des changements en live. Utilise pour tout jeu publiable. N'utilise pas pour un prototype jetable."
mot_cle: "écran réglages qualité graphique VSync FOV volumes audio remap sensibilité accessibilité"
nom_court: "Settings"
branche: "D22"
synonymes: ["preset qualité Bas Moyen Haut + résolution VSync FOV", "sliders de volume Master/Music/SFX/VO séparés", "remap des contrôles + sensibilité + invert Y"]
cross_refs: [1504, 1575, 1503]
tags: ["2027"]
depends_on: [1504]
---

## 1574. ⚙️ Ecran des reglages : qualité graphique, audio, contrôles (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir l'écran des réglages en 2027 : presets qualité (Bas/Moyen/Haut + custom : résolution, VSync, FOV 1506, ombres/particules), volumes par bus (Master/Music/SFX/VO, 1566), contrôles (remap 1504, sensibilité, invert Y), accessibilité (1575), sauvegarde auto (1503), changements appliqués en live.

**Quand l'utiliser (triggers)** :
- Preset qualité auto-détecté selon le GPU
- Sliders volume séparés musique/SFX/VO
- Remapper une touche depuis les réglages (1504) + sensibilité souris

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es UI designer settings. Tu organises 4 onglets (Graphismes/Audio/Contrôles/Accessibilité 1575), presets + custom, sliders 0-100 avec valeur affichée, application immédiate + 'Annuler' si pas confirmé en 10 s, sauvegarde auto (1503). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les réglages disponibles (résolution, VSync, FOV, qualité, volumes, contrôles)
- Le matériel cible (détection auto preset)
- L'accessibilité (1575)

**Méthode** :
1. Onglet Graphismes : preset (Bas/Moyen/Haut/auto-détecté) + custom (résolution, plein écran, VSync, FOV 60-110, qualité ombres/particules 1557/post-FX 1555, distance de vue).
2. Onglet Audio : 4 sliders (Master/Music/SFX/VO 0-100) appliqués live (1566), test son.
3. Onglet Contrôles : remap clavier+manette (1504), sensibilité souris/stick (0,1-3), invert Y, vibration on/off.
4. Onglet Accessibilité : voir 1575 (daltonisme, tailles, secousses 1558, sous-titres 1533).
5. Sauvegarde auto dans la save (1503), 'Appliquer' immédiat + rollback si non confirmé 10 s.

**Sorties attendues** :
- L'écran settings complet (4 onglets, presets + custom)
- Les volumes par bus et le remap live
- La sauvegarde auto + rollback 10 s

**Exemple de prompt** :
> « Conçois l'écran des réglages du jeu : onglets Graphismes (preset auto + résolution/VSync/FOV/qualité), Audio (4 sliders live), Contrôles (remap 1504 + sensibilité), Accessibilité (1575), sauvegarde auto (1503). »

**Cas d'usage** : Tout jeu publiable. S'articule avec skills 1504 (input), 1575 (accessibilité) et 1503 (save).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1555
nom: "Post-processing : vignette, grain, bloom legers (2027)"
emoji: "🌟"
domaine: "Game Dev"
signal: "Ajouter du post-processing en 2027 sans tuer les perfs (complète les shaders 1270) : vignette (assombrir les bords), grain (bruit film), bloom léger (lumières qui débordent), chromatic aberration (impact), en un seul passe GPU sur mobile (URP/HDRP), profilé (1552). Utilise pour le look final. N'utilise pas si ça fait passer sous 60 fps."
mot_cle: "post-processing vignette grain bloom chromatic aberration 1 passe mobile"
nom_court: "Post-FX"
branche: "D19"
synonymes: ["vignette + grain pour le look film", "bloom léger sur les lumières sans lag", "1 seul passe post-FX sur mobile (URP)"]
cross_refs: [1270, 1552, 1553]
tags: ["2027"]
depends_on: [1270]
---

## 1555. 🌟 Post-processing : vignette, grain, bloom legers (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ajouter un post-processing léger en 2027 (vignette, grain, bloom subtil, chromatic aberration sur les dégâts) en 1 passe GPU (URP/HDRP), profilé pour rester à 60 fps (1552), désactivable dans les réglages (1574).

**Quand l'utiliser (triggers)** :
- Le jeu manque de 'look' (plat)
- Vignette + grain = ambiance film en 1 passe
- Bloom sur les explosions sans tuer les fps mobile

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es technical artist rendu. Tu fais un seul shader de post-FX (1 passe) qui combine vignette + grain + bloom cheap (threshold + blur 2 passes petits) + chromatic aberration (paramétrable, ex. 0,3 sur dégâts 1508), dans URP (mobile) ou HDRP (PC). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le render pipeline (URP mobile vs HDRP PC)
- Les effets voulus et leur intensité
- La cible fps (60) et le budget GPU (1552)

**Méthode** :
1. URP : ajouter un Full Screen Pass (Render Feature) après le rendu, 1 material post-FX.
2. Shader post-FX : vignette (distance au centre), grain (hash du temps), bloom cheap (lum > seuil, blur 4 px 2 passes), chromatic (offset RGB selon distance centre, amplifié sur dégâts).
3. Profiler (1552) : viser < 1 ms GPU sur mobile; sinon baisser la résolution du bloom.
4. Réglage : intensité par effet (0-1) dans les settings (1574), preset Qualité (bas/moyen/haut).

**Sorties attendues** :
- Le post-FX 1 passe (vignette/grain/bloom/chromatic)
- Le coût GPU mesuré (< 1 ms mobile)
- Les presets qualité avec post-FX on/off

**Exemple de prompt** :
> « Le jeu est plat visuellement : ajoute un post-FX 1 passe URP (vignette 0,3, grain 0,05, bloom seuil 1,0 blur 4px, chromatic 0,3 sur dégâts) en < 1 ms GPU, désactivable. »

**Cas d'usage** : Look final 2D/3D, mobile et PC. S'articule avec skills 1270 (shaders), 1552 (profilage) et 1574 (settings).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

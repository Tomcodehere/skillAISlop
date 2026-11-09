---
num: 1557
resume: "Rendre des milliers de particules en 2027 via GPU instancing (1 draw call pour toutes, 1553) : système custom (compute buffer : position, vélocité, durée de vie, couleur) ou VFX Graph, avec spawn rate, cap 5000, et LOD (moins de particules au loin). Étape 1 : Choisir : VFX Graph (visuel, Unity) ou shader custom (compute buffer de particules, DrawProcedural = 1 draw call)."
date_ajout: "2026-11"
nom: "Particules GPU : instancing pour milliers de particules"
emoji: "✨"
domaine: "Game Dev"
signal: "Faire des milliers de particules sans lag en 2027 (complète 1222) : GPU instancing (le GPU dessine N particules en 1 draw call au lieu de N), système de particules custom (spawn, vélocité, gravité, fade, mort) dans un compute buffer ou VFX Graph, cap à 5000 particules. Utilise pour explosions, pluie, foule. N'utilise pas le CPU pour 10k particules."
mot_cle: "particules GPU instancing VFX Graph compute buffer 5000 particules 1 draw call"
nom_court: "Particules GPU"
branche: "D19"
synonymes: ["10 000 particules en 1 draw call (GPU instancing)", "VFX Graph Unity ou shaders de particules custom", "pluie/neige/explosions sans lag"]
cross_refs: [1222, 1553, 1551]
tags: ["2027"]
depends_on: [1222]
---

## 1557. ✨ Particules GPU : instancing pour milliers de particules (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre des milliers de particules en 2027 via GPU instancing (1 draw call pour toutes, 1553) : système custom (compute buffer : position, vélocité, durée de vie, couleur) ou VFX Graph, avec spawn rate, cap 5000, et LOD (moins de particules au loin).

**Quand l'utiliser (triggers)** :
- Mon explosion spawn 500 particules en CPU = lag
- GPU instancing : 10 000 particules 1 draw call
- Pluie/neige ambient sans impacter les fps

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es technical artist VFX. Tu utilises VFX Graph (Unity) ou un shader de particules custom (compute buffer mis à jour par compute shader), 1 draw call via DrawProcedural, cap + LOD, blend additif pour les explosions. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les effets à faire (explosion, pluie, foule, magie)
- Le cap de particules (5000)
- La cible fps (60) sur mobile

**Méthode** :
1. Choisir : VFX Graph (visuel, Unity) ou shader custom (compute buffer de particules, DrawProcedural = 1 draw call).
2. Chaque particule : position, vélocité, gravité, drag, durée de vie, taille, couleur (fade out).
3. CPU envoie juste les 'spawn events' (position, vélocité initiale, count); le GPU simule le reste.
4. Cap 5000 particules; LOD : au-delà de 50 m de la caméra, diviser le spawn rate par 4.
5. Profiler (1552) : viser < 1 ms GPU pour 5000 particules.

**Sorties attendues** :
- Le système de particules GPU (1 draw call pour N particules)
- Le cap + LOD configurés
- Le coût GPU mesuré (< 1 ms à 5000 particules)

**Exemple de prompt** :
> « Mon explosion spawn 500 particules en CPU et fait lag : passe en VFX Graph / compute buffer (GPU instancing, 1 draw call, cap 5000, LOD loin), mesurer < 1 ms GPU. »

**Cas d'usage** : Explosions, météo, foules, magie. S'articule avec skills 1222 (VFX design), 1553 (draw calls) et 1551 (pooling CPU).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

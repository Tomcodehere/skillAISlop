---
num: 1551
resume: "Implémenter un object pool en 2027 : pré-allouer N objets (balles, ennemis, particules, textes flottants), Get() prend un inactif (ou en crée un si pool vide + cap), Release() le rend inactif pour réutilisation — zéro allocation en steady state. Étape 1 : Poolinférieur àTsupérieur à : Listinférieur àTsupérieur à actifs, Stackinférieur àTsupérieur à inactifs; prewarm : instancier N, désactiver."
lang: "fr"
date_ajout: "2026-11"
nom: "Object pooling : reutiliser les objets"
emoji: "♻️"
domaine: "Game Dev"
signal: "Implémenter un object pool en 2027 : au lieu de Instantiate/Destroy (allocations GC, pics de lag), un pool pré-alloue N objets (balles, ennemis, particules), les 'désactive' (inactif) et les réutilise. Utilise pour tout ce qui spawn/despawn souvent. N'utilise pas pour des objets uniques rares."
mot_cle: "object pooling pré-allouer réutiliser éviter GC Instantiate Destroy"
nom_court: "Object pool"
branche: "D1"
synonymes: ["ne plus Instantiate/Destroy à chaque tir (GC lag)", "pool de 50 balles pré-allouées réutilisées", "Get() depuis le pool, Release() retour au pool"]
cross_refs: [1550, 308, 1552]
tags: ["2027"]
depends_on: [1550]
---

## 1551. ♻️ Object pooling : reutiliser les objets (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter un object pool en 2027 : pré-allouer N objets (balles, ennemis, particules, textes flottants), Get() prend un inactif (ou en crée un si pool vide + cap), Release() le rend inactif pour réutilisation — zéro allocation en steady state.

**Quand l'utiliser (triggers)** :
- Des pics de lag à chaque vague d'ennemis (GC)
- Pool de balles : Get() / Release() au lieu de Instantiate
- Compteur d'objets actifs pour dimensionner le pool

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur optimisation. Tu fournis la classe Pool<T> (stack d'inactifs, prewarm N, Get avec cap, Release avec reset des composants), et tu mesures : Memory Profiler (1552) avant/après (pics GC supprimés). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les prefabs à pooler (balle, ennemi, particule, dégâts flottants)
- La quantité initiale (prewarm) et le cap
- Les composants à reset au Release

**Méthode** :
1. Pool<T> : List<T> actifs, Stack<T> inactifs; prewarm : instancier N, désactiver.
2. Get() : pop inactif si dispo, l'activer, reset (velocity=0, pv=max, etc.); sinon si actifs < cap, instancier; sinon null.
3. Release(obj) : désactiver, push inactif.
4. Usage : balle tirée → pool.Get(); balle touche → pool.Release().
5. Mesurer : allocation GC/frame avant/après (1552), fps min pendant une grosse vague.

**Sorties attendues** :
- Le pool réutilisable (Get/Release/prewarm/cap)
- Les prefabs poolés (balles, ennemis, VFX)
- Le gain mesuré : 0 alloc GC en steady state, fps min stable

**Exemple de prompt** :
> « Mon bullet hell rame à la vague 20 (pics GC) : pool toutes les balles/ennemis/particules (prewarm 50, cap 500), Get/Release, mesurer le fps min avant/après. »

**Cas d'usage** : Tout ce qui spawn/despawn souvent. S'articule avec skills 1550 (ECS), 308 (profileur) et 1552 (mémoire).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

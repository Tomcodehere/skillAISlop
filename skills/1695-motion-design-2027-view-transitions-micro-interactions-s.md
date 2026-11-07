---
num: 1695
nom: "Motion design 2027 : view transitions, micro-interactions, scroll (2027)"
emoji: "🎬"
domaine: "Design"
signal: "Concevoir le motion design 2027 : View Transitions entre pages (1615), micro-interactions au hover/focus (boutons, liens), animations au scroll (scroll-driven 1610), durées courtes (150-300 ms), easing naturel (spring), respect de prefers-reduced-motion (1495) — jamais d'animation bloquante ou infinie. Utilise pour rendre l'UI vivante sans la ralentir. N'utilise pas pour masquer un chargement lent (perf d'abord 1618)."
mot_cle: "motion design 2027 view transitions micro-interactions scroll-driven durées 150-300 ms prefers-reduced-motion"
nom_court: "Motion 2027"
branche: "D22"
synonymes: ["animations au scroll natives (scroll-driven 1610)", "micro-interactions hover focus 150-300 ms easing spring", "view transitions entre pages (1615) + prefers-reduced-motion (1495)"]
cross_refs: [1615, 1610, 1495]
tags: ["2027"]
depends_on: [1495]
---

## 1695. 🎬 Motion design 2027 : view transitions, micro-interactions, scroll (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir le motion design 2027 : View Transitions (1615), micro-interactions hover/focus (150-300 ms, easing spring), animations scroll-driven (1610), toujours avec prefers-reduced-motion (1495) — UI vivante sans la ralentir (perf d'abord 1618).

**Quand l'utiliser (triggers)** :
- les transitions entre pages sont sèches (View Transitions 1615)
- micro-interactions sur les boutons (150-300 ms spring)
- animation au scroll native sans JS (scroll-driven 1610)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es motion designer. Tu définis les règles : durées 150-300 ms, easing spring/cubic-bezier doux, jamais d'animation infinie ou bloquante, prefers-reduced-motion → version statique (1495), focus animé aussi (1571). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'UI et ses parcours (navigation, formulaires, états)
- Les composants animés (boutons, modales, transitions)
- La préférence reduced-motion (1495)

**Méthode** :
1. Transitions de page : View Transitions (1615) avec morphing de l'élément clé (view-transition-name).
2. Micro-interactions : hover (scale 1,02, ombre), focus (anneau animé 1571), clic (ripple discret), succès (check animé).
3. Scroll : scroll-driven animations (1610) pour révélations (fade+translateY 12 px) et progress bar.
4. Durées : 150-300 ms micro, 300-500 ms transitions ; easing spring (overshoot léger) ou cubic-bezier(0,2,0,8,1).
5. Reduced motion : @media (prefers-reduced-motion) → tout en fondu 0,01 ms (1495). Tester au clavier (1571).

**Sorties attendues** :
- Le motion system 2027 (durées, easings, composants animés)
- Les transitions de page fluides (1615) + micro-interactions
- Le mode reduced-motion (1495) testé

**Exemple de prompt** :
> « L'UI 2027 est plate : ajoute View Transitions entre pages (1615, morphing héros), micro-interactions hover/clic (150-300 ms spring), révélations au scroll (scroll-driven 1610), le tout avec prefers-reduced-motion (1495). »

**Cas d'usage** : Toute UI moderne. S'articule avec skills 1615 (VT), 1610 (CSS 2027), 1495 (a11y anim) et 1571 (focus).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

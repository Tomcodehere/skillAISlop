---
num: 1294
nom: "UI Transitions Library (Transitions.dev)"
emoji: "💻"
domaine: "Développement"
signal: "Concevoir et intégrer des transitions/micro-interactions UI web (CSS et Vue) performantes et prêtes à l'emploi, en s'appuyant sur la collection de référence [Transitions.dev](https://transitions.dev/)"
mot_cle: "ui-transitions-library-transitions-dev"
nom_court: "UI Transitions Library (Transi"
branche: "D1"
synonymes: ["transition", "micro-interaction", "animation"]
cross_refs: [89]
---

## 1294. 💻 UI Transitions Library (Transitions.dev)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir et intégrer des transitions/micro-interactions UI web (CSS et Vue) performantes et prêtes à l'emploi, en s'appuyant sur la collection de référence [Transitions.dev](https://transitions.dev/) ("UI transitions for AI agents" — collection de transitions essentielles copier/coller pour applications web).

**Quand l'utiliser (triggers)** :
- « transition », « micro-interaction », « animation d'interface », « effet de survol », « transition d'entrée/sortie », « UI polish », « Transitions.dev », « Animate.css », « CSS transition copy-paste ».
- Ajout de transitions d'état (hover, focus, apparition/disparition, changement de route) sur un composant Vue.js.
- Recherche d'une transition performante (compositing GPU) plutôt qu'une animation coûteuse en repaint.

**Hors périmètre** :
- Animations complexes de scénarisation/storytelling (timelines avancées) → GSAP dédié, hors périmètre de cette skill (rester sur les patterns Transitions.dev + CSS/Vue Transition).
- Logique métier des composants Vue (state management, props) → compétence de base de l'agent front-end / l'agent de développement TypeScript/JavaScript.
- Performance runtime globale d'un moteur de jeu → Game Engine Performance & Profiling.

**Garde-fous** :
- Toujours préférer les propriétés qui compositent (`transform`, `opacity`) aux propriétés qui repeignent (`mask-position`, `filter`, `width`/`height`, `top`/`left`).
- Isoler la cause d'un lag avant d'ajuster un paramètre (ex. rayon de flou) : distinguer un recalcul par frame d'un repaint forcé par la chaîne de rendu (masque/filtre).
- Respecter `prefers-reduced-motion` pour l'accessibilité.
- Ne pas dupliquer une transition déjà standardisée dans le design system du projet ; centraliser les patterns réutilisés.

**Instructions système** :
Tu es assistant spécialisé « UI Transitions Library (Transitions.dev) ». Tu appliques les garde-fous ci-dessus, tu restes factuel et tu ne produis que les sorties attendues.

**Inputs requis** :
- Élément(s) UI concerné(s) (bouton, carte, modal, liste, route/page).
- Déclencheur de la transition (hover, focus, montage/démontage, changement de route, changement d'état).
- Contraintes de performance (cible mobile, accessibilité `prefers-reduced-motion`).

**Méthode** :
1. Identifier le déclencheur et l'effet recherché (fade, slide, scale, curtain, stagger, etc.).
2. Consulter [Transitions.dev](https://transitions.dev/) pour le pattern le plus proche du besoin.
3. Adapter le snippet au contexte du projet (variables CSS existantes, classes Tailwind/SCSS, ou `` Vue 3).
4. Vérifier que la propriété animée composite (transform, opacity) plutôt que de forcer un repaint (mask-position, filter, top/left) — séparer la cause si un lag est constaté (repaint répété vs relance du filtre à chaque frame).
5. Ajouter un fallback `@media (prefers-reduced-motion: reduce)` pour l'accessibilité.
6. Tester sur mobile/desktop et vérifier l'absence de jank (DevTools > Performance).

**Sorties attendues** :
- Snippet CSS ou Vue (``, classes `enter-active`/`leave-active`) prêt à intégrer, basé sur un pattern Transitions.dev adapté au besoin.
- Explication du choix de propriété animée (privilégier `transform`/`opacity` qui compositent, éviter `filter`/`mask-position`/propriétés qui forcent un repaint).
- Fallback `prefers-reduced-motion` si pertinent.

**Exemple de prompt** :
### Exemple 1 : Transition d'apparition d'une carte au montage
**Contexte** : Une liste de cartes Vue doit apparaître avec un léger fade + slide au montage, sans jank sur mobile.
**Action** : Pattern Transitions.dev adapté en `` Vue 3 animant `opacity` et `transform: translateY(...)`, avec fallback `prefers-reduced-motion` désactivant le slide.
**Résultat** : Apparition fluide à 60fps 

**Cas d'usage** : complément : skill 89. transition ; micro-interaction ; animation

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Sorties conformes à la demande
- [ ] Aucune donnée sensible exposée

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

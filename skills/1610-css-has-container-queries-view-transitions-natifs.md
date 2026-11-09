---
num: 1610
resume: "Utiliser le CSS 2027 : :has() (styliser un parent selon son enfant), container queries (@container : le composant s'adapte à son conteneur, pas au viewport), View Transitions natifs, animations scroll-driven — sans JS. Étape 1 : :has() : .form:has(input:invalid) { border: red } — plus besoin de classe JS."
date_ajout: "2026-11"
nom: "CSS : :has, container queries, view transitions natifs"
emoji: "🎨"
domaine: "Développement"
signal: "Utiliser les nouveautés CSS 2027 : sélecteur :has() (parent selon enfant, cross-browser), container queries (@container, style des composants selon leur conteneur), View Transitions natifs entre pages, scroll-driven animations (@scroll-timeline). Utilise pour du CSS moderne sans JS. N'utilise pas pour de la logique métier."
mot_cle: "css 2027 :has() container queries @container scroll-driven animations"
nom_court: "CSS"
branche: "D1"
synonymes: ["sélecteur CSS :has() parent selon enfant", "container queries style selon conteneur", "animations pilotées par le scroll @scroll-timeline"]
cross_refs: [1268, 1615, 1495]
tags: ["2027"]
depends_on: [1268]
---

## 1610. 🎨 CSS 2027 : :has(), container queries, view transitions natifs

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser le CSS 2027 : :has() (styliser un parent selon son enfant), container queries (@container : le composant s'adapte à son conteneur, pas au viewport), View Transitions natifs, animations scroll-driven — sans JS.

**Quand l'utiliser (triggers)** :
- styliser un parent selon son enfant en CSS pur (:has)
- container queries : composant qui s'adapte à sa boîte
- animation qui suit le scroll (@scroll-timeline)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev front CSS. Tu donnes 4 exemples concrets : .card:has(img) {…}, @container (min-width: 400px) {…}, ::view-transition-old/new, @scroll-timeline + animation-timeline pour une barre de progression de lecture. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le site/app CSS
- Les composants à rendre contextuels (container queries)
- Les transitions de page (View Transitions 1615)

**Méthode** :
1. :has() : .form:has(input:invalid) { border: red } — plus besoin de classe JS.
2. Container queries : déclarer container-type: inline-size sur le parent, @container (min-width: 30rem) dans le composant → responsive par composant.
3. View Transitions : meta view-transition + CSS ::view-transition-group(old) pour animer la navigation MPA (1615).
4. Scroll-driven : @scroll-timeline + animation-timeline: scroll() pour une progress bar de lecture sans JS.
5. Vérifier le support (caniuse) + fallback @supports.

**Sorties attendues** :
- Le CSS 2027 utilisé (:has, container, VT, scroll-driven)
- Les fallbacks @supports en place
- Le comparatif avant/après JS retiré

**Exemple de prompt** :
> « Mes cards changent de style via une classe JS ajoutée quand elles ont une image : passe en pur CSS avec .card:has(img), ajoute container queries sur les composants et une progress bar de lecture en @scroll-timeline. »

**Cas d'usage** : Design system, sites content-first, composants réutilisables. S'articule avec skills 1268 (CSS sémantique), 1615 (VT API) et 1495 (animations a11y).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

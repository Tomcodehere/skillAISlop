---
num: 1495
date_ajout: "2026-11"
nom: "Accessibilite des animations (prefers-reduced-motion)"
emoji: "🎬"
domaine: "Design"
signal: "Rendre les animations accessibles en 2027 : respecter prefers-reduced-motion (désactiver/réduire les animations si l'OS demande), éviter les flashs (plus de 3 par seconde, risque épilepsie), durées courtes, alternative statique. Utilise quand on anime une interface. N'utilise pas pour les vidéos (158 sous-titres)."
mot_cle: "prefers-reduced-motion animations accessibles WCAG flash épilepsie"
nom_court: "Animations a11y"
branche: "D22"
synonymes: ["désactiver animations si OS demande", "pas de flash plus de 3 par seconde", "animation réduite accessible"]
cross_refs: [1484, 1294, 1308]
tags: ["2027"]
depends_on: [1484]
---

## 1495. 🎬 Accessibilite des animations (prefers-reduced-motion, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre les animations accessibles en 2027 : media query prefers-reduced-motion (réduire/désactiver), jamais plus de 3 flashs par secondeeconde (risque épileptique, WCAG 2.3.1), durées < 500 ms, alternative statique prévue.

**Quand l'utiliser (triggers)** :
- Certaines animations posent problème à des users
- prefers-reduced-motion en CSS
- éviter les flashs épilepsie WCAG

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es designer motion accessible. Tu donnes les règles WCAG : 2.3.1 (pas plus de 3 flashs par seconde), 2.2.2 (pause/masquer les animations auto), prefers-reduced-motion (version simplifiée), et tu proposes un toggle dans les réglages produit en plus du réglage OS. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les animations du produit (durées, mouvements, flashs)
- Le CSS/framework (Tailwind motion-safe:)
- Les parcours animés critiques

**Méthode** :
1. Inventorier les animations et mesurer : flashs/s (outil WCAG), durées, déplacements (parallax fort ?).
2. Ajouter @media (prefers-reduced-motion: reduce) { animation: none / transition: 0.01ms } global.
3. Vérifier WCAG 2.3.1 : aucun contenu ne flashe plus de 3 fois/s (tester les carrousels auto, vidéos).
4. Ajouter un toggle produit 'Réduire les animations' (persisté) en complément du réglage OS.
5. Tester avec un user (ou émulateur Chrome) : parcours utilisable sans animation.

**Sorties attendues** :
- Les animations conformes (reduced-motion respecté, pas de flash)
- Le toggle 'Réduire les animations' dans le produit
- Le test de conformité documenté

**Exemple de prompt** :
> « Notre landing a un carrousel auto qui flashe et des parallax agressifs : rends les animations accessibles (prefers-reduced-motion, < 3 flashs par seconde, toggle produit). »

**Cas d'usage** : Accessibilité, inclusion, conformité WCAG. S'articule avec skills 1484 (a11y design), 1294 (transitions) et 1308 (audit).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

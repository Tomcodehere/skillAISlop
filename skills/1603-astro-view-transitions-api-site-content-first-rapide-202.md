---
num: 1603
date_ajout: "2026-11"
nom: "Astro + View Transitions API : site content-first rapide (2027)"
emoji: "🚀"
domaine: "Développement"
signal: "Construire un site content-first rapide en 2027 avec Astro (îles d'hydratation partielle, 0 JS par défaut) + View Transitions API (transitions animées entre pages MPA, natif Chrome). Utilise pour blogs, docs, marketing. N'utilise pas pour une app web complexe (dashboard)."
mot_cle: "astro view transitions API site content-first rapide MPA"
nom_court: "Astro+VT"
branche: "D1"
synonymes: ["site rapide sans framework lourd (astro)", "transitions animées entre pages nativement", "astro islands hydratation partielle"]
cross_refs: [545, 1615, 1616]
tags: ["2027"]
depends_on: [545]
---

## 1603. 🚀 Astro + View Transitions API : site content-first rapide (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire un site content-first en 2027 avec Astro (0 JS par défaut, îles hydratées à la demande) + View Transitions API (transitions fluides entre pages sans SPA), déployé sur edge.

**Quand l'utiliser (triggers)** :
- Mon blog WordPress est lent, passer à Astro
- transitions entre pages sans recharger (View Transitions)
- astro islands : hydrater un seul composant

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev site statique. Tu montres : page .astro (HTML pur + composants), île interactive (client:load sur un composant React/Vue), View Transitions (document.startViewTransition ou meta), déploiement edge. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le contenu (Markdown/MDX)
- Les composants interactifs (quelques îles)
- L'hébergement (Vercel/Netlify/Cloudflare)

**Méthode** :
1. Projet Astro, contenu en MDX dans src/pages, layout commun.
2. Composants interactifs isolés : <Composant client:load /> (seul le JS de cette île est envoyé).
3. Activer View Transitions : <meta name="view-transition" content="same-origin"> + CSS ::view-transition-old/new pour les animations.
4. Build statique (SSG) ou SSR si contenu dynamique, déployé edge (1612).
5. Mesurer : Lighthouse (objectif 95+), taille JS par page (0 kB hors îles).

**Sorties attendues** :
- Le site Astro déployé (SSG/edge)
- Les îles hydratées uniquement nécessaires
- Les transitions View Transitions entre pages + score Lighthouse

**Exemple de prompt** :
> « Notre site marketing fait 2 s à charger (WordPress) : re-fais-le en Astro (MDX, 0 JS par défaut, 2 îles interactives client:load, View Transitions entre pages) — objectif Lighthouse 95+. »

**Cas d'usage** : Blogs, docs, sites marketing, landing pages. S'articule avec skills 545 (site statique), 1615 (VT API), 1616 (islands).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1617
resume: "Choisir son meta-framework en 2027 (Next.js App Router, Nuxt 4, SvelteKit, React Router 7) selon l'équipe, l'hébergement (edge 1612), l'écosystème et la vélocité — avec une matrice de décision, pas au hasard. Étape 1 : Lister les besoins : SSR/streaming, RSC, SSG, API intégrées, déploiement edge, taille équipe."
date_ajout: "2026-11"
nom: "Meta-frameworks : Next.js vs Nuxt vs SvelteKit vs React Router"
emoji: "⚖️"
domaine: "Développement"
signal: "Choisir son meta-framework React/Vue en 2027 : Next.js (App Router, RSC 1602, écosystème Vercel), Nuxt 4 (Vue, Nitro), SvelteKit (Svelte, rapide, simple), React Router 7 (framework mode, ex-Remix). Critères : équipe, hébergement (edge 1612), ecosysteme, vitesse de dev. Utilise quand on démarre un projet app. N'utilise pas pour un site statique (Astro 1603)."
mot_cle: "choisir meta-framework 2027 next.js nuxt sveltekit react router 7 comparatif"
nom_court: "Meta-framework"
branche: "D1"
synonymes: ["next.js vs nuxt vs sveltekit choisir 2027", "react router 7 framework mode ex-remix", "quel framework pour une app métier interne"]
cross_refs: [1602, 1604, 1603]
tags: ["2027"]
depends_on: [1602]
---

## 1617. ⚖️ Meta-frameworks 2027 : Next.js vs Nuxt vs SvelteKit vs React Router (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir son meta-framework en 2027 (Next.js App Router, Nuxt 4, SvelteKit, React Router 7) selon l'équipe, l'hébergement (edge 1612), l'écosystème et la vélocité — avec une matrice de décision, pas au hasard.

**Quand l'utiliser (triggers)** :
- on démarre un projet, quel meta-framework en 2027 ?
- next.js app router vs nuxt 4 vs sveltekit
- react router 7 (ex-remix) framework mode

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte front. Tu fais la matrice : stack équipe (React→Next/RR7, Vue→Nuxt, Svelte→SvelteKit), hébergement (Vercel→Next, Nitro→Nuxt, adaptable→SvelteKit/RR7), features (RSC → Next 1602), communauté/plugins. Règle : suivre la stack de l'équipe d'abord. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'équipe et sa stack actuelle
- L'hébergement cible (Vercel/Netlify/edge 1612/self-host)
- Les besoins (SSR, RSC, SSG, API routes)

**Méthode** :
1. Lister les besoins : SSR/streaming, RSC, SSG, API intégrées, déploiement edge, taille équipe.
2. Scorer chaque meta-framework (Next/Nuxt/SvelteKit/RR7) : écosystème, perfs, DX, hébergement, hiring.
3. Recommander selon la stack équipe (React → Next.js ou RR7 ; Vue → Nuxt ; petit projet rapide → SvelteKit).
4. POC 1 semaine sur le favori (routing, data, auth, déploiement), valider.
5. Documenter le choix + la stack dans l'ADR (88).

**Sorties attendues** :
- La matrice comparative des 4 meta-frameworks
- Le choix retenu + POC validé
- L'ADR (88) qui documente la décision

**Exemple de prompt** :
> « On démarre une app interne, équipe React de 5, hébergement Vercel edge : choisis le meta-framework en 2027 (matrice Next.js/Nuxt/SvelteKit/RR7 + POC 1 semaine). »

**Cas d'usage** : Nouveau projet app web. S'articule avec skills 1602 (RSC), 1604 (tRPC), 1603 (Astro statique) et 88 (ADR).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

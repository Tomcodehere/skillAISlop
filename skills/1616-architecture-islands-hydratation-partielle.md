---
num: 1616
resume: "Concevoir une architecture islands en 2027 : HTML statique par défaut, seules les îles interactives hydratées selon leur priorité (client:load immédiat, client:idle quand idle, client:visible au scroll), chacune pouvant utiliser un framework différent. Étape 1 : Identifier les îles (composants avec état/événements) vs le reste (statique)."
lang: "fr"
date_ajout: "2026-11"
nom: "Architecture islands : hydratation partielle"
emoji: "🏝️"
domaine: "Développement"
signal: "Concevoir une architecture « islands » en 2027 (Astro 1603, ou islands dans Next.js) : la page est du HTML statique, seules les « îles » interactives sont hydratées (client:load, client:idle, client:visible) avec chacune son framework si besoin. Utilise pour des sites mostly-statiques avec quelques composants dynamiques. N'utilise pas pour une app 100 % interactive (SPA)."
mot_cle: "architecture islands hydratation partielle astro client:load idle visible 2027"
nom_court: "Islands"
branche: "D1"
synonymes: ["page statique + îles interactives hydratées (astro)", "client:load client:idle client:visible choisir", "plusieurs mini-frameworks sur une page (îles)"]
cross_refs: [1603, 1605, 545]
tags: ["2027"]
depends_on: [1603]
---

## 1616. 🏝️ Architecture islands : hydratation partielle (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir une architecture islands en 2027 : HTML statique par défaut, seules les îles interactives hydratées selon leur priorité (client:load immédiat, client:idle quand idle, client:visible au scroll), chacune pouvant utiliser un framework différent.

**Quand l'utiliser (triggers)** :
- ma page envoie 300 kB de JS pour 2 boutons
- astro islands : hydrater seulement le carrousel
- client:visible charger le composant au scroll

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev front architecture. Tu expliques : le HTML statique est servi tel quel (SEO, vitesse), chaque île a sa directive d'hydratation, les îles peuvent mixer React/Vue/Svelte, et le poids JS total = somme des îles seulement. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La page (contenu statique majoritaire)
- Les composants interactifs ( carrousel, formulaire, chat)
- Leur priorité d'hydratation

**Méthode** :
1. Identifier les îles (composants avec état/événements) vs le reste (statique).
2. Choisir la directive : client:load (critique, ex. panier), client:idle (après chargement, ex. recherche), client:visible (au scroll, ex. commentaires, carte).
3. Chaque île importe son framework (React/Vue/Svelte) indépendamment — pas de bundle global.
4. Mesurer : JS total = somme des îles (souvent < 50 kB vs 300 kB SPA), Lighthouse.
5. Tester l'hydratation (DevTools : l'île réagit, le reste non).

**Sorties attendues** :
- La page en islands (JS = somme des îles, mesuré)
- Les directives client:load/idle/visible appliquées
- Le comparatif poids vs SPA complète

**Exemple de prompt** :
> « Ma landing envoie 300 kB de JS pour un carrousel et un formulaire : passe en Astro islands (HTML statique, carrousel client:visible, formulaire client:load) → JS total sous 50 kB. »

**Cas d'usage** : Sites marketing, blogs, e-commerce (listes statiques, panier île). S'articule avec skills 1603 (Astro), 1605 (Qwik) et 545.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1615
date_ajout: "2026-11"
nom: "View Transitions API multi-pages (MPA)"
emoji: "🎬"
domaine: "Développement"
signal: "Ajouter des transitions fluides entre pages d'un site multi-pages (MPA, pas SPA) en 2027 avec la View Transitions API (même origine) : document.startViewTransition() autour du fetch/navigation, animations ::view-transition-old/new, cross-document via meta. Utilise pour des sites sans framework lourd (Astro 1603). N'utilise pas entre origines différentes sans header."
mot_cle: "view transitions API MPA multi-pages document.startViewTransition ::view-transition"
nom_court: "View Transitions"
branche: "D1"
synonymes: ["transitions animées entre pages sans SPA (View Transitions)", "document.startViewTransition navigation fluide", "::view-transition-old new group animation"]
cross_refs: [1603, 1610, 1268]
tags: ["2027"]
depends_on: [1603]
---

## 1615. 🎬 View Transitions API multi-pages (MPA, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Animer les transitions entre pages d'un site MPA en 2027 avec la View Transitions API : meta view-transition (cross-document), document.startViewTransition() pour les navigations same-origin, styles ::view-transition-old/new/group.

**Quand l'utiliser (triggers)** :
- mon site MPA recharge brutalement entre les pages
- view transitions API entre pages same-origin
- animer un élément précis (view-transition-name)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev front UX. Tu donnes : <meta name="view-transition" content="same-origin"> dans le head, le CSS ::view-transition-old(root)/new(root) avec fade, et view-transition-name sur un élément clé (ex. image héros qui vole vers la page détail). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le site MPA (Astro 1603 ou HTML pur)
- Les pages à relier (liste → détail)
- Les animations voulues (fade, slide, morphing héros)

**Méthode** :
1. Activer : meta view-transition same-origin dans le layout (cross-document auto).
2. Cross-document : par défaut fade 0,25 s ; customiser ::view-transition-old(root)/new(root) (opacity, transform, duration).
3. Même page (SPA-like) : document.startViewTransition(() => updateDOM()).
4. Élément partagé : view-transition-name: hero sur l'image dans les 2 pages → elle vole d'une page à l'autre (morphing).
5. Fallback : @supports pas supporté → navigation classique.

**Sorties attendues** :
- Le site MPA avec transitions fluides (fade + morphing héros)
- Le meta + CSS view-transition en place
- Le fallback @supports pour vieux navigateurs

**Exemple de prompt** :
> « Notre site Astro recharge brutalement entre articles : active View Transitions (meta same-origin, fade custom, image héros en view-transition-name qui vole de la liste au détail). »

**Cas d'usage** : Sites MPA (Astro 1603), e-commerce (liste→fiche produit). S'articule avec skills 1603 (Astro), 1610 (CSS 2027) et 1268.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1601
date_ajout: "2026-11"
nom: "HTMX + backend : UI dynamique sans JavaScript lourd (2027)"
emoji: "🧩"
domaine: "Développement"
signal: "Construire des interfaces dynamiques en 2027 avec HTMX côté HTML (requêtes AJAX depuis les attributs HTML, mise à jour de fragments de page) + un backend classique (Django django-htmx, Rails, Laravel) : zéro/minimal JS. Utilise pour des apps CRUD/contente-first. N'utilise pas pour des apps très interactives (éditeur riche, jeu)."
mot_cle: "htmx UI dynamique sans javascript django-htmx fragments"
nom_court: "HTMX"
branche: "D1"
synonymes: ["interface dynamique sans écrire de JS (htmx)", "django-htmx tokens CSRF auto", "remplacer une SPA par du serveur + htmx"]
cross_refs: [545, 78, 1268]
tags: ["2027"]
depends_on: [545]
---

## 1601. 🧩 HTMX + backend : UI dynamique sans JavaScript lourd (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Construire une UI dynamique en 2027 avec HTMX + backend (Django django-htmx, Rails, Laravel) : requêtes AJAX depuis le HTML (hx-get/hx-post), rendu de fragments partiels, validation côté serveur, CSRF géré — sans SPA lourde.

**Quand l'utiliser (triggers)** :
- Mon appli CRUD est une SPA de 800 kB de JS, simplifier
- Django + HTMX : formulaires dynamiques sans JS
- hx-get hx-post rendu partiel serveur

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev full-stack léger. Tu montres le pattern : bouton/lien avec hx-post, endpoint qui renvoie un fragment HTML (pas du JSON), swap avec hx-target/hx-swap, django-htmx gère le CSRF, indicateurs de chargement (htmx-indicator). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le backend (Django/Rails/Laravel/PHP)
- Les écrans à rendre dynamiques (liste, formulaire, recherche)
- Le besoin de SEO/accessibilité (HTML sémantique)

**Méthode** :
1. Ajouter htmx via CDN ou npm + le bundle dans le layout.
2. Formulaire : hx-post="/contact" hx-target="#result" hx-swap="innerHTML" → endpoint renvoie le fragment HTML du résultat.
3. Liste avec recherche : input hx-get="/search?q=..." hx-trigger="keyup changed delay:300ms" hx-target="#results".
4. Erreurs : gérer le status 4xx/5xx (hx-on ou response-targets) avec message clair.
5. CSRF : django-htmx inclut le token automatiquement dans les requêtes HTMX.

**Sorties attendues** :
- L'app dynamique en HTMX (fragments serveur, peu de JS)
- Les formulaires/recherches fonctionnels avec loading
- Le poids JS divisé (vs SPA)

**Exemple de prompt** :
> « Notre back-office est une SPA React de 800 kB pour des CRUD : refais-le en Django + HTMX (fragments HTML, recherche live hx-get, CSRF auto, poids JS divisé par 10). »

**Cas d'usage** : Back-offices, sites content-first, prototypes rapides. S'articule avec skills 545 (site statique), 78 (no-code) et 1268 (CSS).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1575
nom: "Accessibilite d'un jeu : daltonisme, tailles, secousses, sous-titres (2027)"
emoji: "♿"
domaine: "Game Dev"
signal: "Rendre un jeu accessible en 2027 (WCAG + bonnes pratiques jeu, complément 1484/1495) : filtres daltonisme (protanopie/deutéranopie/tritanopie sur les couleurs critiques PV/ennemis), taille des textes/UI (100-200 %), réduction des secousses (1558) et flashs (1495), sous-titres VO + effets sonores (1533/1569), remap total (1504), pas d'info par couleur seule (formes aussi). Utilise pour tout jeu publiable. N'utilise pas pour un prototype."
mot_cle: "accessibilité jeu daltonisme filtres tailles textes secousses sous-titres remap couleur seule"
nom_court: "Accessibilité jeu"
branche: "D22"
synonymes: ["filtre daltonisme deutéranopie sur les barres PV/ennemis", "taille de l'UI 100 à 200 %", "réduire les secousses (1558) et les flashs (1495)", "sous-titres des dialogues et des SFX importants"]
cross_refs: [1484, 1495, 1558]
tags: ["2027"]
depends_on: [1484]
---

## 1575. ♿ Accessibilite d'un jeu : daltonisme, tailles, secousses, sous-titres (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre un jeu accessible en 2027 : filtres daltonisme (3 types) + jamais d'info par couleur seule (formes/icônes aussi), taille UI 100-200 %, réduction secousses (1558)/flashs (1495), sous-titres VO+SFX (1533/1569), remap total (1504), mode 'haute lisibilité'.

**Quand l'utiliser (triggers)** :
- Les ennemis rouges sur fond vert sont invisibles (daltonisme)
- Jamais d'info par couleur seule (PV rouge = aussi icône)
- Taille des textes x1,5 et sous-titres des explosions

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es accessibility designer jeu. Tu appliques : filtres daltonisme (shader de correction couleur, 3 types, testé avec des simulateurs), redondance forme+couleur (PV = barre + icône + chiffre), taille UI, secousses réduites, sous-titres complétés '[explosion]', remap total, et tu testes avec des joueurs concernés. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les éléments colorés critiques (PV, ennemis, butin 1528)
- Les textes et UI (1570)
- Les secousses/flashs (1558/1495) et la VO (1569)

**Méthode** :
1. Daltonisme : 3 filtres de correction (protanopie/deutéranopie/tritanopie) en post-FX (1555) + jamais couleur seule (formes/icônes/texte en plus : PV = barre + cœur + chiffre).
2. Taille : UI scale 100-200 % (ancres ancrées correctement), textes min 24 px lisibles.
3. Moteur : réduire secousses (1558 amplitude x0,3), désactiver flashs (1495), slow-motion option.
4. Audio : sous-titres pour VO (1569) ET SFX importants '[explosion]', '[cloche]', vibreur pour les alertes.
5. Contrôles : remap total (1504), sensibilité réglable, hold vs toggle pour les actions.

**Sorties attendues** :
- Les options d'accessibilité complètes (daltonisme, taille, secousses, sous-titres, remap)
- La redondance forme+couleur sur les infos critiques
- Les tests avec joueurs concernés documentés

**Exemple de prompt** :
> « Mon jeu est injouable pour un daltonien (ennemis rouges sur herbe verte) : filtres daltonisme 3 types + formes/icônes en plus des couleurs, taille UI x1,5, sous-titres SFX, secousses réduites (1558). »

**Cas d'usage** : Tout jeu publiable (obligation légale UE renforcée 2025+). S'articule avec skills 1484 (a11y design), 1495 (animations) et 1558 (shake).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1581
resume: "Concevoir la page store en 2027 (Steam 1579/itch 1584) : accroche 1 phrase, vidéo/GIF gameplay 10-15 s en 1er, 8-10 captures ordonnées (gameplay loop → combat → récompense), description courte+longue, tags, prix psychologique, wishlist (objectif 20k avant launch). Étape 1 : Accroche : 1 phrase avec verbe d'action ('Infiltre-toi, sabote, fuis' — genre + verbe)."
date_ajout: "2026-11"
nom: "Page store et marketing d'un jeu (Steam, itch)"
emoji: "🎪"
domaine: "Game Dev"
signal: "Concevoir la page store d'un jeu en 2027 (Steam 1579, itch 1584, Epic) : accroche en 1 phrase, GIF/vidéo de gameplay (10-15 s) en 1er, 8-10 captures ordonnées (loop → combat → récompense 1528), description courte (3-5 lignes) + longue, tags pertinents (max 20), prix psychologique (9,99/14,99/19,99 €), régions, démo gratuite, wishlist (objectif 20k avant launch). Utilise avant la mise en ligne. N'utilise pas pour le marketing post-launch (1596)."
mot_cle: "page store Steam captures GIF vidéo tags prix wishlist démo marketing jeu"
nom_court: "Store page"
branche: "D21"
synonymes: ["10 captures d'écran ordonnées (loop → combat)", "prix psychologique 9,99 14,99 19,99 €", "objectif 20 000 wishlists avant le lancement"]
cross_refs: [1579, 1584, 1597]
tags: ["2027"]
depends_on: [1579]
---

## 1581. 🎪 Page store et marketing d'un jeu (Steam, itch, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir la page store en 2027 (Steam 1579/itch 1584) : accroche 1 phrase, vidéo/GIF gameplay 10-15 s en 1er, 8-10 captures ordonnées (gameplay loop → combat → récompense), description courte+longue, tags, prix psychologique, wishlist (objectif 20k avant launch).

**Quand l'utiliser (triggers)** :
- La page Steam avec 10 captures qui racontent une histoire
- GIF de 10 s du gameplay en 1er (pas une image)
- Objectif 20 000 wishlists avant le lancement (1597)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es marketing manager jeu. Tu donnes la structure : accroche (1 phrase, verbe d'action), vidéo 15 s (gameplay réel, pas cinématique), 10 captures ordonnées (loop, mécanique clé, combat 1526, récompense 1528, boss, customisation 1537, multi 1544), description courte (3 lignes) + longue (fonctionnalités), 20 tags max, prix (9,99/14,99/19,99 €), régions, démo. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le jeu finalisé (build 1579)
- Les captures/GIF (enregistrés en jeu)
- Le prix visé et les régions cibles

**Méthode** :
1. Accroche : 1 phrase avec verbe d'action ('Infiltre-toi, sabote, fuis' — genre + verbe).
2. Média : vidéo 10-15 s de gameplay réel en header (pas de cinématique), puis 8-10 captures ordonnées selon le parcours joueur.
3. Description : courte 3-5 lignes (le pitch) en haut, longue avec puces (features : 50 donjons procéduraux 1513, coop 4 joueurs 1544, rejouabilité infinie...).
4. Tags : 20 max, précis (genre + mécaniques : 'roguelike', 'deckbuilding', 'coop').
5. Prix : 9,99/14,99/19,99 € selon contenu; démo gratuite (Steam Next Fest 1597); régions (désactiver Chine si pas de licence).
6. Wishlist : objectif 20k avant launch, campagnes (reddit, TikTok, démo).

**Sorties attendues** :
- La page store complète (accroche + vidéo + 10 captures + tags + prix)
- La démo et l'objectif wishlist (20k)
- Le plan de lancement (1597)

**Exemple de prompt** :
> « Rédige la page Steam du jeu : accroche 'Infiltre, sabote, fuis en coop 4', vidéo 15 s gameplay, 10 captures ( infiltration 1523, combat boss 1526, loot 1528, coop 1544), tags roguelike/coop, prix 14,99 €, démo Next Fest. »

**Cas d'usage** : Lancement PC/console. S'articule avec skills 1579 (Steam), 1584 (itch) et 1597 (Next Fest).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

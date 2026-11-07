---
num: 1534
date_ajout: "2026-11"
nom: "Inventaire : grille, drag and drop, stacking (2027)"
emoji: "🎁"
domaine: "Game Dev"
signal: "Concevoir un inventaire en grille en 2027 : N slots (ex. 5x4), objets avec taille 1x1 à 2x3, drag & drop (souris + manette 1571), stacking (potion x99 dans 1 slot), tri auto, survol avec tooltip (stats 1535), équipement séparé. Utilise pour tout RPG/loot. N'utilise pas pour un inventaire liste simple (UI texte)."
mot_cle: "inventaire grille drag and drop stack x99 tri auto tooltip"
nom_court: "Inventaire"
branche: "D22"
synonymes: ["inventaire 5x4 slots drag drop souris manette", "potions stackées x99 dans un slot", "tri auto et tooltip au survol"]
cross_refs: [1535, 1571, 1532]
tags: ["2027"]
depends_on: [1535]
---

## 1534. 🎁 Inventaire : grille, drag and drop, stacking (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un inventaire en grille en 2027 : 20 slots (5x4), objets de taille variable (1x1 à 2x3), drag & drop (souris + manette), stacking (potions x99), tri auto, tooltip au survol, équipement à côté.

**Quand l'utiliser (triggers)** :
- Drag & drop d'un objet entre deux slots
- Potions empilées x99 dans un seul slot
- Objet 2x3 qui prend 6 slots

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur UI inventaire. Tu modélises l'inventaire comme une grille 2D (tableau de refs), le drag (ghost qui suit la souris, highlight des slots cibles en vert/rouge selon place), le stack (même id + stackable → merge), le tri (par rareté puis nom). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La taille de la grille (5x4)
- Les objets (taille, stackable, max stack 99)
- Le support souris + manette (1571)

**Méthode** :
1. Grille 2D : slots[x][y] = itemId ou null; item a {id, taille 1x1..2x3, stack}.
2. Placement : vérifier que le rectangle tient (dans les bords + slots libres) → vert, sinon rouge.
3. Drag : au clic, l'objet devient 'ghost' suivant la souris; au relâcher, swap/place si valide.
4. Stack : si même id et stackable et slot cible a < 99 → merge (reste en main si plein).
5. UI : tooltip au survol (nom, rareté colorée, stats 1535, prix 1529), tri auto (bouton), filtre par type.

**Sorties attendues** :
- L'inventaire grille drag&drop fonctionnel (souris + manette)
- Le stacking et le tri auto
- Le tooltip avec stats/rareté

**Exemple de prompt** :
> « Mon inventaire est une liste texte moche : passe en grille 5x4 avec drag&drop (souris + manette), stack des potions x99, tri auto, tooltip au survol. »

**Cas d'usage** : RPG, looter, survival. S'articule avec skills 1535 (équipement), 1571 (menus manette) et 1532 (dialogues PNJ marchand).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

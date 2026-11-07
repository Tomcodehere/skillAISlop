---
num: 1565
date_ajout: "2026-11"
nom: "Destruction procédurale simple (fracture de mesh, 2027)"
emoji: "💥"
domaine: "Game Dev"
signal: "Détruire un objet procéduralement en 2027 : couper un mesh en morceaux (Voronoi fracture : N cellules autour de points aléatoires, chaque cellule = 1 mesh avec rigidbody), au lieu de swapper avec un modèle cassé préfait. Utilise pour murs destructibles, glace. N'utilise pas pour la destruction massive (perf, cap 20 morceaux, pool 1551)."
mot_cle: "destruction procédurale voronoi fracture mesh morceaux rigidbody"
nom_court: "Fracture"
branche: "D1"
synonymes: ["mur qui se casse en morceaux Voronoi", "couper un mesh en N morceaux procéduralement", "cap 20 morceaux + pool pour les perfs"]
cross_refs: [1564, 1551, 1552]
tags: ["2027"]
depends_on: [1564]
---

## 1565. 💥 Destruction procédurale simple (fracture de mesh, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Détruire un objet en morceaux procéduraux en 2027 (fracture Voronoi) : découper le mesh en N cellules (points aléatoires + découpe), chaque morceau = rigidbody (1564) avec vélocité outward, cap 20 morceaux, poolés (1551), le tout reste intact sinon.

**Quand l'utiliser (triggers)** :
- Le mur se brise en morceaux crédibles (pas un swap)
- Voronoi : découper le mesh en 10 cellules autour de points
- Cap 20 morceaux + pool + cleanup après 5 s

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur destruction. Tu fais la fracture Voronoi au chargement (ou à la demande) : N points aléatoires dans la bounding box, découpe du mesh selon les plans médiateurs (lib : par ex. VoronoiMesh), chaque morceau = nouveau mesh + rigidbody + joint optionnel. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le mesh destructible (mur, caisse, glace)
- Le nombre de morceaux (10-20)
- La force de l'explosion/impact (1508)

**Méthode** :
1. Au chargement : générer la fracture Voronoi (N=12 points), créer les N morceaux (mesh + collider + rigidbody kinematic), les cacher (pool 1551).
2. Objet intact affiché tant que PV > 0 (barre de vie cachée).
3. Impact : PV -= dégâts (1508); à 0 → swap : cacher l'intact, activer les morceaux, AddForce outward depuis le point d'impact.
4. Cap : max 20 morceaux actifs simultanés (au-delà, les plus vieux disparaissent).
5. Cleanup : après 5 s, fade + retour au pool (1551).
6. Navmesh : mettre à jour localement (carving, 1518) si le mur bloquait un passage.

**Sorties attendues** :
- L'objet fracturé en morceaux Voronoi à la destruction
- Le cap 20 + pool + cleanup
- Le navmesh mis à jour (passage ouvert)

**Exemple de prompt** :
> « Mon mur de donjon doit se casser crédiblement : fracture Voronoi en 12 morceaux (rigidbodies, AddForce outward à l'impact 1508), cap 20, pool, navmesh carving (1518). »

**Cas d'usage** : Murs destructibles, glace, environnements réactifs. S'articule avec skills 1564 (ragdoll), 1551 (pool) et 1552 (perf).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

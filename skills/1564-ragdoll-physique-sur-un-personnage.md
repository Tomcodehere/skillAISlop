---
num: 1564
resume: "Créer un ragdoll en 2027 : à la mort/assommage, désactiver l'animator (1560) et activer les rigidbodies+joints (CharacterJoint) des 11 parties du corps, appliquer la dernière force reçue (explosion → AddExplosionForce), le corps s'effondre. Étape 1 : Préparer le ragdoll dans l'éditeur : rigidbody sur chaque membre (masse selon taille), CharacterJoint (hanche→torse, torse→tête, etc.), limites d'ang"
lang: "fr"
date_ajout: "2026-11"
nom: "Ragdoll physique sur un personnage"
emoji: "🧸"
domaine: "Game Dev"
signal: "Transformer un personnage en ragdoll en 2027 (mort, assommé, explosion) : chaque partie du corps (tête, torse, bras, jambes) devient un rigidbody avec joint (charnière), on applique la force de l'explosion, le perso s'effondre de façon crédible. Utilise à la mort/assommage. N'utilise pas en gameplay normal (anim 1560)."
mot_cle: "ragdoll rigidbody joints charnières mort explosion personnage physique"
nom_court: "Ragdoll"
branche: "D1"
synonymes: ["le perso s'effondre crédiblement à la mort", "chaque membre = rigidbody + joint charnière", "explosion projette le ragdoll (AddForce)"]
cross_refs: [1562, 1560, 1508]
tags: ["2027"]
depends_on: [1560]
---

## 1564. 🧸 Ragdoll physique sur un personnage (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Créer un ragdoll en 2027 : à la mort/assommage, désactiver l'animator (1560) et activer les rigidbodies+joints (CharacterJoint) des 11 parties du corps, appliquer la dernière force reçue (explosion → AddExplosionForce), le corps s'effondre.

**Quand l'utiliser (triggers)** :
- À la mort, mon perso reste figé (anim de mort)
- Ragdoll : le corps s'effondre physiquement
- L'explosion projette le corps (AddExplosionForce)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur physique personnage. Tu prépares le rig avec rigidbody+CharacterJoint sur chaque membre (pré-fait dans l'éditeur ou généré), et au switch : animator.enabled=false, rigidbodies isKinematic=false, appliquer la vélocité/force du coup (1508). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le rig du personnage (11 rigidbodies + joints)
- L'animator à désactiver (1560)
- La force du coup (dégâts, direction 1508)

**Méthode** :
1. Préparer le ragdoll dans l'éditeur : rigidbody sur chaque membre (masse selon taille), CharacterJoint (hanche→torse, torse→tête, etc.), limites d'angle.
2. En jeu : ragdoll OFF (isKinematic=true) pendant le gameplay (anim 1560).
3. À la mort : animator.enabled = false, tous isKinematic = false, appliquer vélocité du coup sur le torse + AddExplosionForce si explosion.
4. Après 5 s : fade out + pool/destroy (1551), respawn.
5. Hybride : ragdoll partiel (seulement le bras touché) avec poids (1563).

**Sorties attendues** :
- Le ragdoll complet (11 membres, joints) à la mort
- L'explosion qui projette le corps (AddExplosionForce)
- Le cleanup après 5 s (pool)

**Exemple de prompt** :
> « À la mort mon perso fait une anim de mort figée : passe en ragdoll (rigidbodies+CharacterJoint sur les 11 membres, animator off à la mort, vélocité du coup + AddExplosionForce). »

**Cas d'usage** : Mort, assommage, explosions, comique. S'articule avec skills 1562 (IK), 1560 (anim) et 1508 (hitbox).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

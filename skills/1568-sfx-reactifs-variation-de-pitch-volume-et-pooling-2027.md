---
num: 1568
date_ajout: "2026-11"
nom: "SFX réactifs : variation de pitch/volume et pooling (2027)"
emoji: "📢"
domaine: "Game Dev"
signal: "Rendre les effets sonores réactifs et non répétitifs en 2027 : variation aléatoire de pitch (0,9-1,1) et volume (±3 dB) à chaque joue (sinon effet 'cassette'), pool de 8-16 voix par catégorie (pas d'alloc, 1551), priorité (sons proches de la caméra), cooldown pour éviter le spam (tir = max 10/s). Utilise pour tous les SFX. N'utilise pas pour la musique (1567) ni la VO (1569)."
mot_cle: "SFX variation pitch volume aléatoire pool voix priorité cooldown anti-spam"
nom_court: "SFX réactifs"
branche: "D19"
synonymes: ["chaque tir a un pitch légèrement différent (0,9-1,1)", "pool de 16 voix pour les tirs (pas d'alloc)", "cooldown : max 10 sons de tir par seconde"]
cross_refs: [1566, 1551, 1559]
tags: ["2027"]
depends_on: [1566]
---

## 1568. 📢 SFX réactifs : variation de pitch/volume et pooling (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Rendre les SFX vivants en 2027 : à chaque joue, pitch aléatoire 0,9-1,1 et volume ±3 dB (jamais identique), pool de voix par catégorie (1551), priorité aux sons proches de la caméra, cooldown anti-spam par catégorie.

**Quand l'utiliser (triggers)** :
- Le son de tir est toujours identique (cassette)
- Pitch aléatoire 0,9-1,1 à chaque joue
- Max 10 tirs/s (cooldown) sinon ça spam

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es sound designer SFX. Tu configures dans FMOD/Wwise : sur chaque event, pitch randomize (0,9-1,1), volume random ±3 dB; virtual voices (pool 16 par catégorie); priority = 128 - distance caméra; cooldown par event (min interval). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les SFX (tir, pas, UI, dégâts 1508)
- Le nombre de voix par catégorie (16)
- Le cooldown par catégorie (tir 100 ms)

**Méthode** :
1. Sur chaque event SFX : ajouter 'Pitch' random 0,9-1,1 et 'Volume' random -3/+3 dB (FMOD/Wwise randomizer).
2. Virtual voices : 16 par catégorie (tir, pas), 32 total, priorité = proximité caméra (plus proche = joue).
3. Cooldown : min interval par event (tir 100 ms = max 10/s, pas 50 ms).
4. Pas de son = juste un marqueur visuel (1559).
5. Tester : tirer 10 fois de suite → 10 sons différents, jamais de coupure sèche.

**Sorties attendues** :
- Les SFX avec variation pitch/volume (jamais identiques)
- Le pool de voix + priorité caméra + cooldown
- Le test : 10 tirs = 10 sons différents, 0 coupure

**Exemple de prompt** :
> « Le son de tir est toujours identique et ça fatigue : ajoute pitch random 0,9-1,1 + volume ±3 dB, pool 16 voix (priorité caméra), cooldown 100 ms (max 10/s). »

**Cas d'usage** : Tous les SFX répétitifs (armes, pas, UI, dégâts). S'articule avec skills 1566 (middleware), 1551 (pool) et 1559 (juice).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

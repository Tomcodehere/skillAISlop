---
num: 1526
date_ajout: "2026-11"
nom: "Boss : phases et patterns telegraphes (2027)"
emoji: "🐉"
domaine: "Game Dev"
signal: "Concevoir un boss en 2027 : plusieurs phases selon les PV (100-66 %, 66-33 %, sous 33 %) avec transition (invincible + cinématique courte), attaques télégraphiées (marque au sol 1 s avant = zone de dégâts, barre de cast), patterns rotatifs, fenêtres de dégâts après certaines attaques. Utilise pour un boss mémorable. N'utilise pas pour un ennemi normal (1519)."
mot_cle: "boss phases PV patterns telegraphes marque au sol barre de cast fenêtre dégâts"
nom_court: "Boss design"
branche: "D1"
synonymes: ["boss 3 phases selon PV transition cinématique", "attaque télégraphiée marque au sol 1 s avant", "fenêtre de dégâts après l'attaque du boss"]
cross_refs: [1519, 1525, 1508]
tags: ["2027"]
depends_on: [1519]
---

## 1526. 🐉 Boss : phases et patterns telegraphes (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un boss en 2027 : 3 phases selon PV avec transitions courtes (invincible), attaques télégraphiées (marque au sol/zone + barre de cast), rotation de patterns, et fenêtres de contre-attaque après certaines attaques.

**Quand l'utiliser (triggers)** :
- Mon boss est un sac de PV sans pattern
- 3 phases : 100-66-33 % avec transition
- Attaque télégraphiée : marque au sol 1 s avant les dégâts

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer combat. Tu structures : phases (seuils PV, transition 2 s invincible + changement de pattern), telegraphs (decal/zone au sol qui pulse 1 s puis dégâts, barre de cast au-dessus), patterns = liste d'attaques choisies aléatoirement avec cooldown, fenêtre de punition après l'attaque lourde. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les PV du boss et les seuils de phase
- Les patterns d'attaque (3-5) avec telegraph + dégâts
- La durée des transitions et fenêtres

**Méthode** :
1. Phases : phase = PV > 66 % ? 1 : PV > 33 % ? 2 : 3; au changement, 2 s invincible + anim + nouveau set de patterns.
2. Telegraph : pour chaque attaque, spawn une zone (cercle/rectangle) qui pulse 1 s (rouge), puis dégâts si joueur dedans (1508 hitbox).
3. Patterns : liste par phase, choisir aléatoire avec cooldown global 2 s + cooldown par attaque.
4. Fenêtre de punition : après l'attaque 'charge' (3 s), le boss est étourdi 4 s → le joueur inflige x2.
5. Test : le combat dure 3-5 min, le joueur meurt s'il ignore les telegraphs.

**Sorties attendues** :
- Le boss multi-phases avec telegraphs
- Les patterns par phase + cooldowns
- La fenêtre de punition et le test de durée de combat

**Exemple de prompt** :
> « Conçois le boss final de mon action-RPG : 3 phases (PV), attaques télégraphiées (marque au sol 1 s), rotation de patterns, fenêtre de 4 s étourdi après la charge. »

**Cas d'usage** : Boss de fin de niveau/donjon. S'articule avec skills 1519 (FSM), 1525 (coordination adds) et 1508 (hitbox).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

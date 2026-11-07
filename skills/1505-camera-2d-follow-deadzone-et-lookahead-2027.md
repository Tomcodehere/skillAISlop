---
num: 1505
date_ajout: "2026-11"
nom: "Camera 2D : follow, deadzone et lookahead (2027)"
emoji: "📷"
domaine: "Game Dev"
signal: "Concevoir une caméra 2D confortable en 2027 : follow du joueur avec deadzone (zone morte), lookahead dans la direction du mouvement, limites de niveau (clamp), lerp doux, et zoom sur événements. Utilise pour tout jeu 2D à défilement. N'utilise pas pour la 3D (voir 1506)."
mot_cle: "caméra 2D follow deadzone lookahead limites niveau"
nom_court: "Caméra 2D"
branche: "D1"
synonymes: ["caméra qui suit le joueur en 2D", "deadzone caméra zone morte", "lookahead caméra selon direction"]
cross_refs: [1506, 1511, 1140]
tags: ["2027"]
depends_on: [1140]
---

## 1505. 📷 Camera 2D : follow, deadzone et lookahead (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir une caméra 2D en 2027 : follow avec deadzone (la caméra ne bouge que si le joueur sort d'une zone centrale), lookahead dans la direction du mouvement, clamp aux limites du niveau, lerp pour la douceur.

**Quand l'utiliser (triggers)** :
- La caméra tremble quand le joueur bouge
- Deadzone : zone morte au centre
- Lookahead : la caméra anticipe la direction

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur caméra. Tu donnes le calcul : target = player + velocity*lookahead, clamp dans les bounds du niveau, position = lerp(pos, target, smoothing*dt), deadzone = rectangle central où la caméra ne suit pas. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La taille du niveau (bounds)
- Le joueur et sa vélocité
- Le lookahead souhaité (ex. 2 unités) et la deadzone (ex. 3x2)

**Méthode** :
1. Deadzone : si |player - center| < deadzone sur un axe, la caméra garde sa cible sur cet axe.
2. Lookahead : target += velocity.normalized * lookahead_distance.
3. Clamp : target.x/y bornés dans [bounds.min+viewport/2, bounds.max-viewport/2].
4. Lerp : cam.pos = lerp(cam.pos, target, 1 - exp(-smoothing*dt)) pour un suivi doux.
5. Zoom événement : lerp du zoom vers 0,8 puis retour (ex. entrée de boss).

**Sorties attendues** :
- La caméra 2D confortable (deadzone + lookahead + clamp)
- Le système de zoom événementiel
- Le test sur un niveau long

**Exemple de prompt** :
> « Ma caméra 2D tremble à chaque pas : ajoute deadzone 3x2, lookahead 2 unités selon la vélocité, clamp aux limites du niveau, lerp exponentiel. »

**Cas d'usage** : Plateformer 2D, top-down 2D. S'articule avec skills 1506 (caméra 3D) et 1511 (mouvement).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1558
resume: "Ajouter du screen shake en 2027 : à chaque événement (explosion, dégâts reçus, atterrissage), la caméra tremble 0,2-0,5 s avec amplitude proportionnelle et decay exponentiel, cumul max (éviter la nausée), désactivable (1575). Étape 1 : Shake : ajouter à la caméra un offset = (rand-0.5) * 2 * amplitude * shakeForce(t), où shakeForce décroit exponentiellement (exp(-5t))."
lang: "fr"
date_ajout: "2026-11"
nom: "Screen shake et hit feedback visuel"
emoji: "💥"
domaine: "Game Dev"
signal: "Ajouter du screen shake en 2027 : la caméra tremble brièvement (0,2 s, amplitude selon l'intensité : explosion forte = 0,5, dégâts reçus = 0,2) avec decay exponentiel, sans nausée (jamais en continu), désactivable (1575). Utilise pour les impacts. N'utilise pas pour la caméra de visée précise (sniper)."
mot_cle: "screen shake caméra tremble decay exponentiel intensité explosion dégâts"
nom_court: "Screen shake"
branche: "D19"
synonymes: ["caméra qui tremble 0,2 s à l'explosion", "shake fort 0,5 faible 0,2 decay rapide", "désactivable dans l'accessibilité (1575)"]
cross_refs: [1506, 1559, 1575]
tags: ["2027"]
depends_on: [1559]
---

## 1558. 💥 Screen shake et hit feedback visuel (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ajouter du screen shake en 2027 : à chaque événement (explosion, dégâts reçus, atterrissage), la caméra tremble 0,2-0,5 s avec amplitude proportionnelle et decay exponentiel, cumul max (éviter la nausée), désactivable (1575).

**Quand l'utiliser (triggers)** :
- L'explosion fait trembler l'écran 0,3 s
- Dégâts reçus = petit shake 0,1
- Jamais de shake continu (nausée) + option off

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur caméra feedback. Tu ajoutes un offset aléatoire à la caméra = noise(t) * amplitude * decay, amplitude selon l'événement (explosion 0,5, hit 0,2), durée 0,2-0,5 s, cumul des shakes capé à 1,0, et option 'réduire les secousses' (1575). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les événements à shaker (explosion, dégâts, dash, atterrissage)
- L'amplitude par événement
- La durée et le decay (exp)

**Méthode** :
1. Shake : ajouter à la caméra un offset = (rand-0.5) * 2 * amplitude * shakeForce(t), où shakeForce décroit exponentiellement (exp(-5t)).
2. Événements : explosion → 0,5 / 0,4 s; dégâts reçus → 0,2 / 0,2 s; dash → 0,1; atterrissage fort → 0,15.
3. Cumul : si un shake est déjà actif, remplacer par le plus fort (max des amplitudes), jamais sommer au-delà de 1,0.
4. Jamais de shake permanent (seulement événementiel, max 0,5 s) — sinon nausée.
5. Accessibilité : option 'Réduire les secousses' (1575) → amplitude x0,3, ou off.

**Sorties attendues** :
- Le screen shake événementiel (amplitude/durée/decay)
- Le cap anti-nausée et l'option accessibilité
- Le test visuel sur explosion/dégâts

**Exemple de prompt** :
> « Ajoute du feedback caméra : explosion = shake 0,5/0,4 s, dégâts reçus = 0,2/0,2 s, decay exponentiel, cumul capé à 1,0, option 'réduire les secousses' dans l'accessibilité. »

**Cas d'usage** : Game feel des impacts. S'articule avec skills 1506 (caméra), 1559 (juice) et 1575 (accessibilité).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

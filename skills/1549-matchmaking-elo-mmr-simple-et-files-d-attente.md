---
num: 1549
date_ajout: "2026-11"
nom: "Matchmaking : ELO/MMR simple et files d'attente"
emoji: "🎯"
domaine: "Game Dev"
signal: "Implémenter un matchmaking en 2027 : chaque joueur a un MMR (ELO) qui monte/gagne (+25) ou descend (-25) selon victoire/défaite et écart de niveau; file d'attente qui élargit la plage de MMR acceptée avec le temps d'attente (30 s → ±100, 2 min → ±400); évite les smurfs (1543). Utilise pour tout jeu compétitif classé. N'utilise pas pour du coop casual (1544)."
mot_cle: "matchmaking MMR ELO file d'attente plage élargie avec attente ±100 ±400"
nom_court: "Matchmaking"
branche: "D21"
synonymes: ["MMR qui monte de 25 si victoire", "file qui accepte ±100 après 30 s ±400 après 2 min", "match trouvé en moins de 2 min"]
cross_refs: [1544, 1543, 1540]
tags: ["2027"]
depends_on: [1544]
---

## 1549. 🎯 Matchmaking : ELO/MMR simple et files d'attente (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Implémenter un matchmaking en 2027 : MMR par joueur (départ 1000, +25/-25 selon résultat et écart), file d'attente qui élargit la plage acceptée avec le temps (±100 à 30 s, ±400 à 2 min), match trouvé < 2 min, évitement des smurfs (1543).

**Quand l'utiliser (triggers)** :
- Trouver un match en moins de 2 minutes
- MMR 1000 départ, +25 victoire -25 défaite
- Plage de MMR qui s'élargit si attente longue

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur matchmaking. Tu stockes le MMR par joueur (save cloud 1539), la file par région/ping, la règle d'élargissement (searchRange = 50 + 10*secondes), et le calcul de gain/perte selon l'écart (battre un plus fort = +30, perdre contre un plus faible = -30). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le MMR de chaque joueur (1000 départ)
- La région et le ping max (100 ms)
- Le temps d'attente max (2 min avant widen)

**Méthode** :
1. File d'attente : rejoindre avec {mmr, région, t0}; toutes les secondes, chercher un groupe de 10 joueurs (2 équipes de 5) avec max-min MMR < range(t).
2. range(t) = 50 + 10 * (t - t0 en s), cap à 800; à 2 min, match garanti (bot ou widen max).
3. Après match : MMR += 25 * (1 - proba_attendue) où proba = 1/(1+10^(-(diff)/400)) (formule ELO).
4. Anti-smurf : nouveau compte commence MMR bas mais monte vite (détection 1543); limite de duo queue (écart < 200).
5. UI : temps d'attente, MMR affiché, 'match trouvé !' + loading.

**Sorties attendues** :
- Le matchmaking fonctionnel (< 2 min)
- Le calcul MMR (ELO) après chaque match
- L'anti-smurf et la limite de duo

**Exemple de prompt** :
> « Mes joueurs attendent 10 min pour un match : implémente le matchmaking (MMR 1000 départ, file par région, plage ±50 qui passe à ±400 après 2 min, +25/-25 ELO). »

**Cas d'usage** : Jeux compétitifs classés (1544 serveur dédié). S'articule avec skills 1544 (archi), 1543 (anti-triche) et 1540 (analytics).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

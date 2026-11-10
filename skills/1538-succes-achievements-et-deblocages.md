---
num: 1538
resume: "Concevoir 40-60 achievements en 2027 : conditions variées (combat, exploration, secret), certains cachés, récompenses cosmétiques/titres, notification toast à l'obtention, progression globale %, synchro Steam (1581). Étape 1 : Définir les achievements : id, nom, description, icône, condition (ex. kills supérieur à= 100), récompense (cosmétique/titre), caché ou non."
lang: "fr"
date_ajout: "2026-11"
nom: "Succes (achievements) et deblocages"
emoji: "🏆"
domaine: "Game Dev"
signal: "Concevoir les succès (achievements) d'un jeu en 2027 : 40-60 succès cachés/visibles, conditions variées (tuer 100 monstres, finir sans dégâts, trouver un easter egg), récompense (cosmétique, titre, 1529), notification toast, progression %, intégration Steam (1581). Utilise pour la rétention et la fierté. N'utilise pas pour les objectifs de quêtes (1531)."
mot_cle: "achievements succès cachés conditions toast progression Steam"
nom_court: "Achievements"
branche: "D22"
synonymes: ["succès 'tuer 100 monstres' avec toast", "succès caché easter egg", "progression 12/50 succès et intégration Steam"]
cross_refs: [1581, 1531, 1530]
tags: ["2027"]
depends_on: [1531]
---

## 1538. 🏆 Succes (achievements) et deblocages (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir 40-60 achievements en 2027 : conditions variées (combat, exploration, secret), certains cachés, récompenses cosmétiques/titres, notification toast à l'obtention, progression globale %, synchro Steam (1581).

**Quand l'utiliser (triggers)** :
- Toast 'Succès débloqué : 100 kills' en jeu
- Succès caché à découvrir (easter egg)
- Sync des succès avec Steam (1581)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer rétention. Tu définis Achievement {id, nom, desc (visible si caché ?), condition (event + seuil), récompense, caché}, le système qui écoute les events du jeu, la toast UI (image + nom, 4 s, file), et le % global. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La liste des achievements (40-60, mix facile/difficile/secret)
- Les events du jeu (kill, niveau, quête...)
- La récompense (titre, cosmétique, gold)

**Méthode** :
1. Définir les achievements : id, nom, description, icône, condition (ex. kills >= 100), récompense (cosmétique/titre), caché ou non.
2. Écouteur : event bus du jeu (onKill, onLevelUp...) → vérifier conditions → débloquer si OK.
3. Toast : à l'obtention, afficher 4 s (coin haut droit) avec son + nom + icône, jouer un son.
4. UI : page succès avec grille, barre de progression par succès, % global, filtres (obtenus/à faire/cachés).
5. Steam : mapper vers les Steam Achievements (1581), sync cloud.

**Sorties attendues** :
- Les 40-60 achievements fonctionnels avec toasts
- La page succès (progression + % global + cachés)
- La synchro Steam

**Exemple de prompt** :
> « Ajoute 50 achievements au jeu : 30 visibles (100 kills, finir niveau 1...), 10 cachés (easter egg), toasts à l'obtention, page succès avec % global, sync Steam. »

**Cas d'usage** : Rétention, complétionnistes, marketing (Steam). S'articule avec skills 1581 (Steamworks), 1531 (quêtes) et 1530 (niveaux).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1537
resume: "Concevoir un arbre de compétences en 2027 : 3 branches, nœuds avec coût en points de talent (1 par niveau), prérequis (parent débloqué), effets passifs appliqués aux stats, respec payant, UI avec connexions entre nœuds. Étape 1 : Data : nœuds avec prérequis (parent), coût (1-3 pts), effet passif (modifie les stats du joueur)."
date_ajout: "2026-11"
nom: "Arbre de competences (skill tree) et respec"
emoji: "🌳"
domaine: "Game Dev"
signal: "Concevoir un arbre de compétences en 2027 : 3 branches (ex. guerrier/mage/voleur), nœuds avec coût en points de talent (gagnés par niveau 1530), prérequis (nœud parent), effets passifs (dégâts +10 %), respec payant (1530). Utilise pour la customisation du build. N'utilise pas pour un personnage sans choix (tout fixe)."
mot_cle: "skill tree arbre compétences points de talent prérequis respec payant"
nom_court: "Skill tree"
branche: "D22"
synonymes: ["arbre de talents 3 branches guerrier mage voleur", "points de talent gagnés par niveau", "respec payant reset des talents"]
cross_refs: [1530, 1535, 1531]
tags: ["2027"]
depends_on: [1530]
---

## 1537. 🌳 Arbre de competences (skill tree) et respec (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un arbre de compétences en 2027 : 3 branches, nœuds avec coût en points de talent (1 par niveau), prérequis (parent débloqué), effets passifs appliqués aux stats, respec payant, UI avec connexions entre nœuds.

**Quand l'utiliser (triggers)** :
- Arbre de talents avec 3 branches et connexions
- 1 point de talent par niveau gagné
- Respec : reset tous les talents contre gold

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer progression. Tu définis les nœuds {id, branche, coût, prérequis parent, effet {dégâts: +10%}, position UI}, les points (niveau - points dépensés), l'UI (3 colonnes, lignes de connexion, nœud grisé si prérequis manquant), et le respec (coût = 50*niveau gold, 1529). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les 3 branches et leurs nœuds (10-15 par branche)
- Les effets par nœud (stats 1535)
- Le coût du respec

**Méthode** :
1. Data : nœuds avec prérequis (parent), coût (1-3 pts), effet passif (modifie les stats du joueur).
2. Points de talent : +1 par niveau (1530), total = niveau - 1 - dépensés.
3. Débloquer : si points suffisants ET parent débloué → appliquer effet (dégâts x1,1).
4. UI : arbre visuel, clic sur nœud → tooltip (effet, coût) → bouton 'Apprendre' si OK.
5. Respec : vider tous les nœuds, rembourser les points, coût 50*niveau gold (anti-abus).

**Sorties attendues** :
- L'arbre de compétences fonctionnel (3 branches, prérequis)
- Le système de points de talent lié au niveau
- Le respec payant

**Exemple de prompt** :
> « Ajoute un skill tree à mon RPG : 3 branches (guerrier/mage/voleur), nœuds avec prérequis et effets (+10 % dégâts...), 1 point/niveau, respec 50*niveau gold. »

**Cas d'usage** : RPG, action-RPG, MMO. S'articule avec skills 1530 (niveaux), 1535 (stats) et 1531 (quêtes de classe).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

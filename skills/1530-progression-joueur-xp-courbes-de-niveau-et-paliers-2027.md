---
num: 1530
nom: "Progression joueur : XP, courbes de niveau et paliers (2027)"
emoji: "📈"
domaine: "Game Dev"
signal: "Concevoir la progression d'un joueur en 2027 : courbe d'XP par niveau (exponentielle douce : xp(n) = 100 * 1,15^n), paliers de déblocage (niveau 5 = donjon 2, niveau 10 = monture), respec payant, prestige optionnel. Utilise pour tout RPG/action avec niveaux. N'utilise pas pour un jeu sans progression (puzzle)."
mot_cle: "courbe XP exponentielle paliers déblocage respec prestige niveaux"
nom_court: "Progression XP"
branche: "D22"
synonymes: ["xp niveau = 100 * 1,15^n exponentiel", "déblocage donjon niveau 5 monture niveau 10", "respec payant des compétences"]
cross_refs: [1537, 1529, 1481]
tags: ["2027"]
depends_on: [1537]
---

## 1530. 📈 Progression joueur : XP, courbes de niveau et paliers (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir la progression en 2027 : courbe d'XP exponentielle douce (xp(n) = 100 * 1,15^n), paliers de déblocage (niv 5 = donjon 2, niv 10 = monture, niv 20 = PvP), respec payant, et HUD de progression (barre XP + niveau).

**Quand l'utiliser (triggers)** :
- Mon jeu prend 100 h pour niveau 50
- Courbe XP 100 * 1,15^n par niveau
- Déblocages par palier (monture niv 10)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es game designer progression. Tu donnes la formule XP, le temps estimé par niveau (xp/taux farm), les paliers de contenu (tableau niveau → déblocage), le respec (coût en gold croissant), et la barre d'XP avec % restant. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le taux d'XP des activités (kill 10, quête 100)
- La durée cible de la campagne (ex. 40 h)
- Les contenus à débloquer et à quel niveau

**Méthode** :
1. Courbe : xp_pour_niveau(n) = round(100 * 1,15^n) → temps/niveau = xp / farm_moyen (viser 20-40 min/niveau early, 1-2 h late).
2. Paliers : tableau {niveau: déblocage} (5: donjon 2, 10: monture, 15: reroll, 20: PvP, 30: donjon raid).
3. Respec : coût = 50 * niveau gold (frein à l'expérimentation gratuite).
4. Barre XP : progression %, niveau actuel, 'reste X min pour niv suivant'.
5. Tester : simuler la courbe sur 50 niveaux, vérifier que ça ralentit mais pas trop (1,15 = doux).

**Sorties attendues** :
- La courbe d'XP et le temps estimé par niveau
- Le tableau des paliers de déblocage
- Le HUD de progression (barre + % + ETA)

**Exemple de prompt** :
> « Ma progression est trop lente (100 h pour niv 50) : courbe XP 100*1,15^n, paliers (donjon niv 5, monture niv 10, PvP niv 20), respec payant, barre XP avec ETA. »

**Cas d'usage** : RPG, action-RPG, MMO light. S'articule avec skills 1537 (skill tree), 1529 (éco) et 1481 (north star).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

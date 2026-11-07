---
num: 1577
date_ajout: "2026-11"
nom: "Console de commandes et cheats de dev"
emoji: "💻"
domaine: "Game Dev"
signal: "Ajouter une console de commandes en 2027 (touche² ou /) pour le dev : commandes utiles (god, noclip, give gold 1529, tp x y, killall ennemis 1519, setlevel 1530, timescale 0,5 pour debug slow-mo, screenshot), autocomplétion, historique (flèches), log. Cachée en prod (flag build) ou réservée (1543 anti-triche). Utilise pendant le développement et les tests. N'utilise pas en prod compétitif."
mot_cle: "console de commandes dev god give tp killall timescale autocomplétion"
nom_court: "Dev console"
branche: "D1"
synonymes: ["console / avec god noclip give tp killall", "timescale 0,5 pour déboguer au ralenti", "cachée en build release (anti-triche 1543)"]
cross_refs: [1543, 1552, 1530]
tags: ["2027"]
depends_on: [1543]
---

## 1577. 💻 Console de commandes et cheats de dev (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Ajouter une console de dev en 2027 (touche ²) : commandes god/noclip/give/tp/killall/setlevel/timescale/screenshot, autocomplétion (Tab), historique (flèches haut/bas), log coloré — compilée hors build release (anti-triche 1543).

**Quand l'utiliser (triggers)** :
- Besoin de /give gold 10000 pour tester l'économie (1529)
- /tp 100 200 pour aller vite à un endroit
- Console cachée en prod (anti-triche 1543)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es programmeur outils dev. Tu enregistres les commandes (nom, args, fonction, aide), autocomplétion sur Tab, historique persistant (flèche haut), exécution avec log; #if DEBUG uniquement, jamais en release (1543). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les commandes utiles au dev (god, give, tp, killall, setlevel, timescale, fps, screenshot)
- Le flag de build (DEBUG vs RELEASE)
- L'UI console (champ + log scrollable)

**Méthode** :
1. Enregistrer commandes : {'god': toggle invincible, 'give gold N' (1529), 'tp x y z', 'killall' (1519), 'setlevel n' (1530), 'timescale 0,5', 'screenshot', 'fps', 'pos'}.
2. UI : touche ² ouvre (overlay, pause le jeu en solo), champ en bas, log au-dessus, autocomplétion Tab, historique flèches.
3. Sécurité : #if UNITY_EDITOR/DEBUG uniquement; en release la console n'existe pas (1543 anti-triche multi).
4. Log coloré (erreur rouge, succès vert) + copie dans le presse-papiers (Ctrl+C).

**Sorties attendues** :
- La console de dev (commandes + autocomplétion + historique)
- Le flag DEBUG/RELEASE (console absente en prod)
- La liste des commandes documentée pour l'équipe

**Exemple de prompt** :
> « Pour tester vite l'économie end-game : ajoute une console dev (²) : /give gold 99999 (1529), /setlevel 50 (1530), /god, /tp, /killall, /timescale 0,5, /screenshot — compilée hors release (1543). »

**Cas d'usage** : Développement, QA, tests. S'articule avec skills 1543 (anti-triche), 1552 (profilage) et 1530 (niveaux).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

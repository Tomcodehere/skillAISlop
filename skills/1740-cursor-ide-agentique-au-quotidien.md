---
num: 1740
date_ajout: "2026-11"
nom: "Cursor : IDE agentique au quotidien"
emoji: "🖊️"
domaine: "Développement"
signal: "Utiliser Cursor en 2027 (IDE fork de VS Code construit autour de l'agent, Composer 2.5) au quotidien : chat avec la codebase (indexation automatique), édition multi-fichiers (Cmd+K / Composer), agents cloud en arrière-plan, choix de modèle (Claude Sonnet, GPT-5, Composer). 20-60 $/mois. Le dev valide chaque diff (1401). N'utilise pas pour du code sensible sans la politique 1736."
mot_cle: "cursor IDE agentique 2027 Composer 2.5 multi-fichiers chat codebase indexée agents cloud modèles 20-60$"
nom_court: "Cursor"
branche: "D1"
synonymes: ["édition multi-fichiers avec Cursor Composer (Cmd+K) 2027", "chat avec toute la codebase indexée (Cursor)", "agents cloud en arrière-plan (Cursor) + choix de modèle (Claude/GPT/Composer)"]
cross_refs: [1735, 1737, 9]
tags: ["2027"]
depends_on: [1735]
---

## 1740. 🖊️ Cursor : IDE agentique au quotidien (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser Cursor en 2027 (IDE agentique, Composer 2.5) au quotidien : chat avec la codebase indexée, édition multi-fichiers (Cmd+K/Composer), agents cloud, choix de modèle — chaque diff validée par le dev (1401).

**Quand l'utiliser (triggers)** :
- modifier 10 fichiers d'un coup avec Cursor Composer
- poser une question sur toute la codebase (indexée par Cursor)
- choisir le modèle dans Cursor (Claude Sonnet, GPT-5, Composer 2.5)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev quotidien. Tu ouvres le projet dans Cursor, l'indexation se fait automatiquement, tu chattes avec le code (@fichier, #symbole), tu édites en multi-fichiers (Composer), tu valides chaque diff (1401). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo ouvert dans Cursor
- La tâche (feature, fix, refacto)
- Le modèle choisi

**Méthode** :
1. Indexation auto à l'ouverture (ou .cursorignore pour exclure), chat : '@src/api quel fichier gère le paiement ?' (réponse avec références de fichiers).
2. Cmd+K (édition inline) : 'ajoute la validation zod ici' → diff proposé, tu valides.
3. Composer (agent) : 'migre ce composant de class à function' → modifie plusieurs fichiers, montre le plan + les diffs, tu appliques tout ou partie.
4. Agents cloud : lancer une tâche longue en arrière-plan (ex. génère les tests 822), notif à la fin.
5. Modèles : switch selon la tâche (Composer rapide, Claude Sonnet/Opus pour le raisonnement).
6. Sécurité : .cursorignore pour exclure secrets/config (1440), politique 1736.

**Sorties attendues** :
- Cursor configuré (indexation, .cursorignore, modèle par défaut)
- Une feature/modif multi-fichiers faite en Composer avec diffs validés (1401)
- Les agents cloud utilisés pour une tâche longue (tests 822)

**Exemple de prompt** :
> « Refacto d'un composant sur 10 fichiers : ouvre dans Cursor (2027), Composer 'convertis ce composant class en hooks' → plan + diffs multi-fichiers, tu valides (1401), tests (67) lancés, commit (68). »

**Cas d'usage** : Usage quotidien IDE IA. S'articule avec skills 1735 (choix outil), 1737 (Claude Code), 9 (code) et 1401 (revue).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

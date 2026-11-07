---
num: 1598
nom: "Playtest organise : recruter, questionnaire, synthèse (2027)"
emoji: "🧪"
domaine: "Game Dev"
signal: "Organiser un playtest en 2027 : recruter 8-12 joueurs du profil cible (Discord 1596, panel Prolific/UserTesting, itch 1584), session 60 min (30 min jeu libre + 30 min interview), questionnaire (SUS 1483, NPS, questions ouvertes 'qu'est-ce qui t'a frustré ?'), enregistrement (écran + visage consentis, RGPD 1584), synthèse en 1 page avec priorités (bugs 1591, fun, difficulté 1529). Utilise à chaque milestone. N'utilise pas pour le game feel micro (juice 1559 = test interne)."
mot_cle: "playtest organisé recrutement 8-12 joueurs questionnaire SUS synthèse priorités"
nom_court: "Playtest"
branche: "D22"
synonymes: ["8-12 testeurs du profil cible (Discord 1596 ou Prolific)", "session 60 min : 30 jeu + 30 interview + questionnaire SUS 1483", "enregistrement écran+visage avec consentement RGPD (1584)"]
cross_refs: [1483, 1596, 1540]
tags: ["2027"]
depends_on: [1596]
---

## 1598. 🧪 Playtest organise : recruter, questionnaire, synthèse (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Organiser un playtest en 2027 : recruter 8-12 joueurs du profil (1596), session 60 min (30 jeu + 30 interview), questionnaire (SUS 1483 + NPS + ouvertes), consentements RGPD (1584), synthèse 1 page avec priorités (bugs/fun/difficulté 1529) intégrées au backlog.

**Quand l'utiliser (triggers)** :
- On teste avec 8-12 joueurs du bon profil chaque milestone
- Questionnaire SUS + NPS + 'qu'est-ce qui t'a frustré ?'
- Consentement RGPD pour filmer écran + visage (1584)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es UX researcher playtest. Tu prépares : recrutement (Discord 1596, panel), la build de test (1592 CI), le consentement (RGPD 1584), le guide de session (60 min), le questionnaire (SUS 10 items 1483, NPS, 3 ouvertes), et la synthèse (vidéos, notes, priorités P0/P1/P2). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La build de test (CI 1592) et le vertical slice (1593)
- Les 8-12 testeurs recrutés (1596)
- Le questionnaire (SUS 1483, NPS, ouverts)

**Méthode** :
1. Recruter 8-12 joueurs du profil cible (Discord communauté 1596, Prolific, itch 1584), consentement écrit (RGPD 1584 : enregistrement écran+visage, données supprimées après synthèse).
2. Session 60 min : 5 min brief, 30 min jeu libre (observé, notes sur les blocages), 25 min interview + questionnaire (SUS 1483, NPS 'recommanderais-tu ?', 3 questions ouvertes).
3. Analyser : SUS moyen (objectif > 68), NPS, thèmes récurrents (frustrations, fun, difficulté 1529/1136), bugs trouvés (→ 1591).
4. Synthèse 1 page : top 3 points forts, top 3 frustrations, priorités P0 (bugs bloquants)/P1/P2 → backlog (1531), démo suivante corrigée.
5. Récompenser : clé Steam démo (1579) ou skin beta (1542).

**Sorties attendues** :
- Le playtest organisé (8-12 joueurs, consentements RGPD)
- Le questionnaire SUS/NPS rempli et analysé
- La synthèse 1 page + priorités P0/P1/P2 dans le backlog

**Exemple de prompt** :
> « Lance un playtest avant la démo Next Fest (1597) : recrute 10 joueurs du Discord (1596) + Prolific, session 60 min (30 jeu + SUS 1483 + interview), consentements RGPD (1584), synthèse 1 page → corrige les P0 avant la démo. »

**Cas d'usage** : Chaque milestone (1593), avant démo publique (1597). S'articule avec skills 1483 (tests distants), 1596 (communauté) et 1540 (analytics).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

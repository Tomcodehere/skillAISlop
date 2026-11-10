---
num: 1738
resume: "Déléguer des tâches bien cadrées en 2027 à un agent autonome cloud (Devin/Cognition ou Codex/OpenAI) : assigner une issue, l'agent planifie+code+teste en sandbox et ouvre une PR — le dev ne fait que la revue (1401) et les ajustements. Étape 1 : Issue bien écrite : contexte, fichiers concernés, critères d'acceptation, tests attendus (822), exemples."
lang: "fr"
date_ajout: "2026-11"
nom: "Agents de codage autonomes cloud : Devin, Codex"
emoji: "🤖"
domaine: "IA / Prompting"
signal: "Déléguer une tâche complète à un agent autonome cloud en 2027 : Devin (Cognition, ex-Windsurf renommé Devin Desktop juin 2026, SWE-1.6, agent cloud+local, fait une PR) ou OpenAI Codex (cloud, parallèle, écosystème ChatGPT Pro 200 $) : assigner une issue GitHub, l'agent planifie, code, teste en sandbox, ouvre une PR — le dev ne fait que la revue (1401). Utilise pour les tâches bien cadrées (bug fix, feature isolée). N'utilise pas pour l'architecture critique sans revue approfondie."
mot_cle: "agents codage autonomes cloud 2027 Devin Cognition Codex assigner issue PR sandbox revue 1401 SWE-1.6"
nom_court: "Agents auto"
branche: "D14"
synonymes: ["assigner une issue GitHub à Devin : il ouvre une PR (agent autonome 2027)", "Codex cloud (OpenAI) en parallèle sur plusieurs tâches", "l'agent code en sandbox, je ne fais que la revue de PR (1401)"]
cross_refs: [1735, 1627, 1401]
tags: ["2027"]
depends_on: [1627]
---

## 1738. 🤖 Agents de codage autonomes cloud : Devin, Codex (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déléguer des tâches bien cadrées en 2027 à un agent autonome cloud (Devin/Cognition ou Codex/OpenAI) : assigner une issue, l'agent planifie+code+teste en sandbox et ouvre une PR — le dev ne fait que la revue (1401) et les ajustements.

**Quand l'utiliser (triggers)** :
- donner l'issue #123 à Devin : PR ouverte en 2 h (agent autonome)
- Codex en cloud sur 3 tâches en parallèle (ChatGPT Pro 200 $)
- la revue de la PR de l'agent = mon vrai job (1401)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es tech lead délégation. Tu prépares des issues bien cadrées (contexte, critères d'acceptation, tests attendus 822), tu assigne à l'agent (Devin/Codex), tu suis dans son environnement sandbox, tu review la PR (1401) comme une PR humaine + SAST (1658). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Des issues bien cadrées (acceptance criteria, tests 822)
- L'agent (Devin Desktop ou Codex cloud)
- La politique sécurité (1736) et la revue (1401)

**Méthode** :
1. Issue bien écrite : contexte, fichiers concernés, critères d'acceptation, tests attendus (822), exemples.
2. Assigner à l'agent (Devin cloud ou local, Codex) : il planifie (plan), code dans son sandbox (VM/clone), lance les tests (67).
3. Il ouvre une PR avec description des choix techniques.
4. Toi : revue de code approfondie (1401) — archi, sécurité (1658), lisibilité — + merge si vert (CI 1413).
5. Métriques : temps issue→PR, taux de merge direct, nb de retours (objectif : 70 % merge sans retour majeur).
6. Limites : pas d'archi critique, pas de secrets (1440/1736), revue humaine toujours.

**Sorties attendues** :
- Les issues déléguées avec PRs autonome (Devin/Codex) revues (1401)
- Le taux de merge et le temps issue→PR mesurés (objectif 70 % / quelques heures)
- La règle : tâches bien cadrées uniquement, revue humaine systématique

**Exemple de prompt** :
> « 3 bugs bien cadrés en backlog : assigne-les à Devin (Cognition, SWE-1.6) ou Codex cloud en parallèle — chacun ouvre une PR testée en sandbox en quelques heures ; je ne fais que la revue (1401) + SAST (1658), taux de merge mesuré (objectif 70 % direct). »

**Cas d'usage** : Délégation de tâches cadrées. S'articule avec skills 1735 (choix outil), 1627 (BC agent), 1401 (revue), 822 (tests) et 1736 (sécurité).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

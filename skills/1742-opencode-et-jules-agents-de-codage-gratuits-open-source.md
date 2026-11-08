---
num: 1742
date_ajout: "2026-11"
nom: "OpenCode et Jules : agents de codage gratuits/open source"
emoji: "🆓"
domaine: "IA / Prompting"
signal: "Utiliser un agent de codage gratuit/open source en 2027 : OpenCode (agent CLI open source, modèles au choix dont locaux 1633, gratuit) ou Google Jules (15 tâches background/jour en free tier, intégré GitHub). Pour du code perso/open source ou sans budget. N'utilise pas pour du code interne sensible (résidence 1736) sauf self-host (1633)."
mot_cle: "opencode open source gratuit Jules Google 15 tâches jour 2027 agent codage local modèles 1633"
nom_court: "OpenCode/Jules"
branche: "D14"
synonymes: ["agent de codage 100 % gratuit et open source (OpenCode) 2027", "Jules (Google) : 15 tâches background gratuites par jour", "OpenCode avec un modèle local (1633) : le code ne sort jamais"]
cross_refs: [1735, 1633, 1736]
tags: ["2027"]
depends_on: [1735]
---

## 1742. 🆓 OpenCode et Jules : agents de codage gratuits/open source (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser un agent de codage gratuit en 2027 : OpenCode (CLI open source, modèles au choix dont locaux 1633 — le code ne sort jamais) ou Google Jules (15 tâches/jour en free tier, intégré GitHub) — pour le perso/open source ou sans budget.

**Quand l'utiliser (triggers)** :
- agent de codage gratuit sans envoyer mon code nulle part (OpenCode + modèle local 1633)
- Jules : 15 tâches/jour gratuites en arrière-plan (Google)
- OpenCode open source : quel modèle local brancher (1633) ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev perso/indé. Tu installes OpenCode (open source, config avec le provider de ton choix : API cloud ou modèle local vLLM/Ollama 1633/1472), ou Jules (app Jules.ai, connecte GitHub, assigne des tâches). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo (perso/open source de préférence)
- Le provider (API gratuite ou modèle local 1633)
- GitHub pour Jules

**Méthode** :
1. OpenCode : installer (npm/binaire), configurer le modèle (ex. qwen-coder local via Ollama 1472 → zéro fuite de code, ou API gratuite), lancer dans le repo, il lit/édite/teste comme un agent CLI (76).
2. Jules : connecter son GitHub, créer une tâche ('fix issue #42'), Jules travaille en cloud en arrière-plan (15/jour gratuit), ouvre une PR — revue (1401).
3. Règles : code public/perso/open source uniquement sur les versions cloud gratuites ; code interne/sensible → self-host local (1633) uniquement (1736).
4. Limiter : tâches petites/moyennes (les gros refactos restent sur Claude Code 1737).
5. Mesurer : tâches/jour réussies, temps gagné (1739).

**Sorties attendues** :
- OpenCode ou Jules configuré (gratuit, tâches/jour)
- Le mode 100 % local (OpenCode + modèle 1633) testé (code qui ne sort pas)
- La règle : cloud gratuit = code public/perso uniquement (1736)

**Exemple de prompt** :
> « Je veux un agent de codage gratuit sans fuite de code en 2027 : OpenCode (open source) + modèle local (Ollama 1472 / Mistral 1633) → le code ne sort jamais ; ou Jules (Google, 15 tâches/jour, PR GitHub) pour de l'open source. »

**Cas d'usage** : Perso, open source, petits budgets. S'articule avec skills 1735 (choix payant), 1633 (modèles locaux), 1472 (Ollama), 1736 (sécurité) et 1739 (mesure).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

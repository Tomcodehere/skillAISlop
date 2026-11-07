---
num: 1743
date_ajout: "2026-11"
nom: "Aider et Cline : agents CLI open source dans le terminal (2027)"
emoji: "💻"
domaine: "Développement"
signal: "Utiliser Aider (CLI open source très populaire, édition multi-fichiers, commit auto, modèles au choix) ou Cline (extension VS Code open source, agent dans l'IDE, plan/act mode) en 2027 — alternatives open source à Cursor/Claude Code (1735/1737). Aider = terminal + git intégré ; Cline = dans VS Code. Utilise pour garder le contrôle total et le code en local (1736). N'utilise pas pour du code sensible sans self-host du modèle (1633)."
mot_cle: "aider cline CLI extension VS Code open source 2027 édition multi-fichiers commit auto plan act mode modèles locaux"
nom_court: "Aider/Cline"
branche: "D1"
synonymes: ["Aider : agent CLI open source qui commit tout seul (git intégré) 2027", "Cline : l'agent dans VS Code (plan/act), open source", "modèle local dans Aider/Cline (1633) : le code reste chez moi"]
cross_refs: [1735, 1740, 68]
tags: ["2027"]
depends_on: [1735]
---

## 1743. 💻 Aider et Cline : agents CLI open source dans le terminal (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Utiliser Aider (CLI open source, édition multi-fichiers + commits auto) ou Cline (extension VS Code open source, plan/act) en 2027 — alternatives open source à Cursor/Claude Code, avec modèle local possible (1633) pour que le code reste local (1736).

**Quand l'utiliser (triggers)** :
- Aider : l'agent qui modifie les fichiers ET committe (git intégré)
- Cline dans VS Code : plan mode puis act mode (open source)
- brancher un modèle local (1633) dans Aider/Cline : zéro fuite

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es dev terminal. Tu installes aider (pip) ou l'extension Cline, tu configures le modèle (API ou local 1633/1472), tu édites en multi-fichiers (/add, /edit), Aider committe automatiquement (68) ou Cline montre plan puis agit. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le repo local
- Le modèle (API ou local 1633)
- L'outil (Aider CLI ou Cline VS Code)

**Méthode** :
1. Aider : pip install aider-chat, configurer le modèle (--model ou .aider.conf.yml, local via Ollama 1472), lancer dans le repo, /add src/ /edit 'refacto X' → modifie + commit auto (68) avec message.
2. Cline (VS Code) : installer l'extension, clé API ou local, mode Plan (montre le plan) puis Act (exécute), diffs dans l'IDE.
3. Les deux : multi-fichiers, lecture du repo entier (contexte), tests lancés (67) après modif.
4. Contrôle : tout est local, tu vois chaque diff avant application (Cline) ou chaque commit (Aider).
5. Sécurité : modèle local (1633) pour le code interne (1736), jamais de secrets dans les prompts (1440).

**Sorties attendues** :
- Aider ou Cline opérationnel (multi-fichiers, contrôle total, local)
- Un refacto fait + commité proprement (68) ou avec diffs validés
- Le mode modèle local (1633) testé (code qui ne sort pas, 1736)

**Exemple de prompt** :
> « Je veux un agent open source dans mon terminal qui committe : Aider (pip, /add /edit, commit auto 68, modèle local Ollama 1472/1633 possible) — ou Cline dans VS Code (plan/act). Refacto fait + commité, code resté local (1736). »

**Cas d'usage** : Dev terminal, contrôle total, open source. S'articule avec skills 1735 (choix), 1740 (Cursor), 68 (commits) et 1736 (sécurité).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1631
resume: "Déployer une gateway MCP en 2027 : point d'entrée unique, audit de chaque appel (tool, args, agent, user), scopes par agent, rate limit, blocage des tools sensibles, secrets en env — pour toute l'entreprise. Étape 1 : Inventorier tous les serveurs MCP et les classer (dangereux: shell/exec/fichiers larges ; sûrs: recherche, BDD read-only)."
date_ajout: "2026-11"
nom: "Gateway MCP entreprise : audit, scopes, rate limit"
emoji: "🛡"
domaine: "Sécurité"
signal: "Sécuriser les appels MCP d'une entreprise en 2027 via une gateway unique : un seul point d'entrée pour tous les serveurs MCP (1621), audit log de chaque appel tool (args, user, agent), scopes par agent, rate limit, blocage des tools sensibles (shell, fichiers hors scope), secrets jamais exposés. Utilise quand plusieurs agents utilisent MCP. N'utilise pas sans inventaire des serveurs (1621)."
mot_cle: "gateway MCP entreprise audit scopes rate limit blocage tools sensibles 2027"
nom_court: "Gateway MCP"
branche: "D23"
synonymes: ["un seul point d'entrée MCP pour toute l'entreprise", "audit log chaque appel tool (args user agent)", "bloquer les tools shell/fichiers sensibles"]
cross_refs: [1621, 905, 1476]
tags: ["2027"]
depends_on: [1621]
---

## 1631. 🛡 Gateway MCP entreprise : audit, scopes, rate limit (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer une gateway MCP en 2027 : point d'entrée unique, audit de chaque appel (tool, args, agent, user), scopes par agent, rate limit, blocage des tools sensibles, secrets en env — pour toute l'entreprise.

**Quand l'utiliser (triggers)** :
- 10 agents appellent 20 serveurs MCP sans contrôle
- audit : qui a appelé quel tool avec quels args
- bloquer le tool 'shell' et 'read_file' hors scope

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es RSSI agents. Tu mets un proxy MCP devant tous les serveurs : authentification agent (1625), autorisation par scope (read:db vs write:db), rate limit, audit immuable (1476), liste d allowlist de tools par rôle, secrets injectés côté gateway. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les serveurs MCP de l'entreprise (inventaire 1621)
- Les agents et leurs rôles
- La politique de scopes

**Méthode** :
1. Inventorier tous les serveurs MCP et les classer (dangereux: shell/exec/fichiers larges ; sûrs: recherche, BDD read-only).
2. Gateway : proxy qui intercepte chaque appel MCP, vérifie auth agent (1625) + scope du tool, rate limit par agent.
3. Audit : log immuable (append-only) de chaque appel : timestamp, agent, user, tool, args (masqués si sensibles), résultat.
4. Blocage : tools hors allowlist → 403 + alerte SOC (1453).
5. Secrets : jamais dans la config des serveurs, injectés par la gateway (env/vault 306).

**Sorties attendues** :
- La gateway MCP déployée (auth + scopes + rate limit)
- L'audit immuable des appels + alertes SOC
- L'allowlist de tools par rôle appliquée

**Exemple de prompt** :
> « 10 agents appellent 20 serveurs MCP sans contrôle, un tool 'shell' est exposé : déploie une gateway MCP (auth agent signée 1625, scopes, rate limit, audit immuable, blocage shell → 403 + alerte). »

**Cas d'usage** : Entreprise avec agents + MCP. S'articule avec skills 1621 (MCP registry), 905 (marketplaces), 1476 (traces) et 1453 (SIEM).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

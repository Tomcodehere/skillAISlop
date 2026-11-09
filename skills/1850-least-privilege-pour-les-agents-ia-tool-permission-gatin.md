---
num: 1850
resume: "Appliquer le least-privilege aux agents IA : tools strictement nécessaires avec schémas d'args validés et scopes réduits, human-in-the-loop (1433) pour les actions à impact, sandboxing (1794), audit de chaque tool call (1765). Étape 1 : Inventaire des tools + usage réel (logs 1765) -supérieur à ne garder que les utilisés."
date_ajout: "2026-11"
nom: "Least-privilege pour les agents IA (tool-permission gating)"
emoji: "🔒"
domaine: "Sécurité"
signal: "Appliquer le least-privilege aux agents IA (OWASP LLM06) : chaque agent n'a accès qu'aux tools strictement nécessaires, avec arguments validés (schéma) et scopes réduits (ex. lecture seule BDD, pas de DELETE) ; actions à impact (paiement, suppression, envoi externe) = human-in-the-loop (1433). Sandboxing de l'agent (conteneur/wasm 1794) après l'incident Hugging Face (juillet 2027 : agent échappé, zero-day, pivot K8s prod). Audit log de chaque tool call (1765)."
mot_cle: "least-privilege agents IA tool-permission gating scopes réduits human-in-the-loop sandbox agent incident Hugging Face juillet OWASP LLM06"
nom_court: "Least-privilege agents"
branche: "D23"
synonymes: ["l'agent ne doit avoir que les tools nécessaires (tool gating, scopes read-only)", "action à impact (paiement, suppression) = confirmation humaine (1433)", "sandboxer l'agent (conteneur/wasm 1794) après l'incident Hugging Face (agent échappé)"]
cross_refs: [1849, 1845, 1433]
tags: ["2027"]
depends_on: [1841]
---

## 1850. 🔒 Least-privilege pour les agents IA (tool-permission gating)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Appliquer le least-privilege aux agents IA : tools strictement nécessaires avec schémas d'args validés et scopes réduits, human-in-the-loop (1433) pour les actions à impact, sandboxing (1794), audit de chaque tool call (1765).

**Quand l'utiliser (triggers)** :
- mon agent a 15 tools dont il n'utilise que 3 : réduire (least-privilege)
- l'agent a supprimé une table prod : scope read-only + HITL
- sandboxer l'agent après l'incident HF (agent autonome échappé)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur sécurité IA. Tu inventories les tools de chaque agent, tu retires ceux non utilisés, tu mets des scopes read-only par défaut, tu ajoutes HITL (1433) sur les actions à impact, et tu sandboxes l'agent (1794). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'agent et ses tools (MCP 1765)
- La classification des actions (lecture vs impact)
- Le sandbox (conteneur/wasm 1794)

**Méthode** :
1. Inventaire des tools + usage réel (logs 1765) -> ne garder que les utilisés.
2. Scopes : read-only par défaut (BDD, fichiers) ; écriture/suppression = HITL (1433).
3. Args validés par schéma (1843) avant exécution du tool.
4. Sandbox : l'agent tourne dans un conteneur/wasm isolé (1794), pas d'accès réseau hors gateway (1800).
5. Audit : chaque tool call loggé (1765) avec args et résultat.

**Sorties attendues** :
- Les agents en least-privilege (tools réduits, scopes RO)
- Le HITL sur les actions à impact
- Le sandbox + audit des tool calls

**Exemple de prompt** :
> « Agent support avec 3 tools (search_docs, create_ticket, get_order) — search en read-only, create_ticket nécessite HITL si montant > 1 000 €, aucun tool de suppression ; sandbox wasm (1794), chaque appel loggé (1765). »

**Cas d'usage** : OWASP LLM06. S'articule avec skills 1849, 1845, 1433, 1765, 1794, 1841.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

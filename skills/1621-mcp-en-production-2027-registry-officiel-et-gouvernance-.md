---
num: 1621
nom: "MCP en production 2027 : registry officiel et gouvernance (2027)"
emoji: "🔌"
domaine: "IA / Prompting"
signal: "Déployer MCP (Model Context Protocol, 97 M de téléchargements mensuels SDK, 40 965 serveurs dans le registry officiel 2026) en production en 2027 : choisir des serveurs du registry officiel (vérifiés), gateway MCP entreprise (audit, scopes, rate limit), ne pas exposer de secrets dans les tools. Utilise pour connecter des agents à des outils. N'utilise pas sans gouvernance (905/723)."
mot_cle: "MCP production 2027 registry officiel 40k serveurs gateway gouvernance audit"
nom_court: "MCP prod"
branche: "D14"
synonymes: ["registry officiel MCP 40 965 serveurs vérifiés", "gateway MCP entreprise audit scopes rate limit", "MCP 97M téléchargements SDK 2026"]
cross_refs: [77, 905, 723]
tags: ["2027"]
depends_on: [77]
---

## 1621. 🔌 MCP en production 2027 : registry officiel et gouvernance (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer MCP en production en 2027 : serveurs du registry officiel (40 965+, vérifiés), gateway d'entreprise (audit des appels, scopes par agent, rate limit, pas de secrets exposés), monitoring des tools appelés.

**Quand l'utiliser (triggers)** :
- mon agent a 15 serveurs MCP installés au hasard
- registry officiel MCP : chercher un serveur vérifié
- gateway MCP entreprise : audit + scopes + rate limit

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte MCP entreprise. Tu appliques : inventaire des serveurs MCP utilisés, remplacement par des entrées du registry officiel (vérifiées), gateway central (ex. un seul point d'entrée MCP avec audit log 1476, scopes, quotas), secrets jamais dans les tools (env dinámica). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les serveurs MCP actuels (installés localement ?)
- Le registry officiel MCP (recherche de serveurs)
- La politique de gouvernance (qui peut appeler quels tools)

**Méthode** :
1. Inventorier les serveurs MCP utilisés et leur provenance (registry officiel vs GitHub perso).
2. Pour chacun : vérifier la version épinglée, les permissions demandées (fichiers, réseau), les remplacer par l'officiel si dispo.
3. Gateway : un proxy MCP unique côté entreprise, log de chaque appel tool (args) (1476), scopes par agent, rate limit, blocage des tools dangereux (shell, fichiers hors scope).
4. Secrets : jamais en clair dans la config MCP, injectés par env/vault (306).
5. Monitoring : dashboard des appels MCP (qui appelle quoi, combien), alertes sur anomalies (1417).

**Sorties attendues** :
- Les serveurs MCP du registry officiel, versions épinglées
- Le gateway MCP avec audit + scopes + rate limit
- Le dashboard des appels MCP

**Exemple de prompt** :
> « Notre agent a 15 serveurs MCP installés à la main (versions flottantes, un tool qui lit tout le disque) : passe par le registry officiel (40k serveurs vérifiés), gateway avec audit/scopes, secrets en env. »

**Cas d'usage** : Agents d'entreprise avec outils. S'articule avec skills 77 (MCP), 905 (sécurité marketplaces), 723 (SOC) et 1476 (traces).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

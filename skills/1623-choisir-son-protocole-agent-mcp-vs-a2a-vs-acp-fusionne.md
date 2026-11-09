---
num: 1623
resume: "Choisir le bon protocole agent en 2027 : MCP (agent→outil, standard de fait), A2A (agent→agent, ACP fusionné dedans), UCP (commerce/paiement agent) — matrice de décision, pas de protocole maison. Étape 1 : Cas outil interne (BDD, CRM, fichiers) → MCP server (registry officiel 1621), client dans l'agent."
date_ajout: "2026-11"
nom: "Choisir son protocole agent : MCP vs A2A vs ACP (fusionné)"
emoji: "⚖️"
domaine: "IA / Prompting"
signal: "Choisir le bon protocole d'agents en 2027 : MCP (agent→outil, 97 M téléchargements, standard de fait, 90 % des orgs d'ici 2027), A2A (agent→agent cross-org, 1622), ACP (IBM, fusionné dans A2A août 2025), UCP (paiement/commerce). Règle : MCP pour les outils internes, A2A pour les pairs externes, UCP pour le commerce agentique. N'utilise pas un protocole perso."
mot_cle: "choisir protocole agent 2027 MCP vs A2A vs ACP fusionné UCP paiement"
nom_court: "Choisir protocole"
branche: "D14"
synonymes: ["MCP ou A2A pour mon agent ?", "ACP fusionné dans A2A août 2025", "UCP protocole paiement agent 2027"]
cross_refs: [1621, 1622, 711]
tags: ["2027"]
depends_on: [1621]
---

## 1623. ⚖️ Choisir son protocole agent : MCP vs A2A vs ACP (fusionné) (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir le bon protocole agent en 2027 : MCP (agent→outil, standard de fait), A2A (agent→agent, ACP fusionné dedans), UCP (commerce/paiement agent) — matrice de décision, pas de protocole maison.

**Quand l'utiliser (triggers)** :
- MCP ou A2A pour connecter mon agent à une BDD externe ?
- ACP c'est quoi après la fusion dans A2A ?
- protocole paiement pour agent acheteur (UCP)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte protocoles. Tu fais la matrice : besoin = outil interne → MCP (registry 40k serveurs, 1621) ; agent externe partenaire → A2A (Agent Card, 1622) ; paiement/achat → UCP ; ACP = legacy, plus maintenu séparément (dans A2A). Jamais de protocole custom. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le besoin d'intégration (outil interne, agent externe, paiement)
- Les contreparties (éditeur, partenaire)
- La gouvernance (AAIF 1626)

**Méthode** :
1. Cas outil interne (BDD, CRM, fichiers) → MCP server (registry officiel 1621), client dans l'agent.
2. Cas agent externe (fournisseur, partenaire) → A2A, Agent Card + task (1622).
3. Cas achat/paiement par agent → UCP (mandates signés cryptographiquement).
4. ACP (IBM) : plus maintenu séparément, absorbé par A2A — ne pas démarrer dessus.
5. Documenter dans l'ADR (88) quel protocole pour quelle intégration.

**Sorties attendues** :
- La matrice de décision protocole (MCP/A2A/UCP)
- Les intégrations câblées avec le bon protocole
- L'ADR documentant les choix

**Exemple de prompt** :
> « On veut connecter notre agent à : notre Postgres (interne), l'agent du fournisseur (externe), et un paiement agent : choisis MCP (BDD), A2A (fournisseur), UCP (paiement) — matrice + ADR. »

**Cas d'usage** : Toute intégration agentique. S'articule avec skills 1621 (MCP), 1622 (A2A), 711 et 88 (ADR).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

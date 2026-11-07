---
num: 1635
date_ajout: "2026-11"
nom: "Controle des couts d'agents : budget par tache et kill switch entreprise (2027)"
emoji: "💸"
domaine: "Produit & IA"
signal: "Contrôler les coûts des agents IA en entreprise en 2027 : budget de tokens par agent/tâche/utilisateur (1491), alertes à 80 %, kill switch automatique si dépassement (couper l'agent), cascade de modèles (1441), cache sémantique (1442). Utilise dès le premier agent en prod. N'utilise pas sans dashboard de coût (1476/1180)."
mot_cle: "contrôle coûts agents entreprise 2027 budget tokens par tâche alerte 80% kill switch auto"
nom_court: "Coût agents"
branche: "D11"
synonymes: ["mon agent a coûté 3000€ en une nuit", "budget tokens par agent alerte à 80%", "kill switch auto si dépassement budget"]
cross_refs: [1491, 1441, 1442]
tags: ["2027"]
depends_on: [1491]
---

## 1635. 💸 Controle des couts d'agents : budget par tache et kill switch entreprise (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Contrôler les coûts des agents en entreprise en 2027 : budget de tokens par agent/tâche (1491), alerte à 80 %, kill switch automatique (agent coupé) au dépassement, cascade de modèles (1441) + cache sémantique (1442) pour réduire.

**Quand l'utiliser (triggers)** :
- l'agent support a coûté 3000 € en une nuit (boucle infinie)
- budget 50€/mois par agent, alerte à 80%
- kill switch : couper l'agent automatiquement si budget dépassé

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es FinOps agents. Tu mets : plafond de tokens/jour par agent, monitoring coût temps réel (1476/1180), alerte 80 % (1417), kill switch auto (désactiver l'agent) au 100 %, revue hebdo des top consommateurs, optimisation (cascade 1441, cache 1442). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les agents en prod et leur conso actuelle
- Les budgets par agent/équipe
- Le canal d'alerte (Slack/PagerDuty)

**Méthode** :
1. Meter : chaque appel agent loggé (tokens in/out, modèle, coût) → dashboard temps réel (1180).
2. Budgets : par agent (ex. 50 €/jour), par équipe, par projet ; alerte à 80 % (1417).
3. Kill switch : à 100 % du budget, l'agent est désactivé (flag off, 1492) + notif équipe + incident (256).
4. Boucle infinie : cap d'itérations (max 10, 1428) + timeout par tâche (60 s).
5. Optimiser : cascade petit modèle (1441), cache sémantique (1442), compresser le contexte (1431).

**Sorties attendues** :
- Le dashboard de coût agents (temps réel) + alertes 80 %
- Le kill switch auto testé (budget dépassé = agent off + notif)
- Les économies mesurées (cascade + cache)

**Exemple de prompt** :
> « Notre agent support a coûté 3000 € en une nuit (boucle infinie) : mets un budget 50 €/jour avec alerte 80 %, kill switch auto à 100 % (flag off + notif), cap 10 itérations, puis cascade/cache pour réduire. »

**Cas d'usage** : Tout agent en prod. S'articule avec skills 1491 (coût/tâche), 1441 (cascade), 1442 (cache) et 1417 (alertes).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1640
resume: "Sécuriser un agent IA en production en 2027 : contrer l'injection indirecte (contenu web lu par l'agent 818), l'exfiltration via tools (fichiers/email), la mémoire empoisonnée (1637), le dépassement de privilèges — avec sandbox (1475), scopes, HITL (1433). Étape 1 : Injection indirecte : le contenu web/mail lu par l'agent est traité comme données, jamais comme instructions (séparer data/prompt, 81"
date_ajout: "2026-11"
nom: "Securite des agents IA en production : menaces (injection, exfiltration)"
emoji: "🛡"
domaine: "Sécurité"
signal: "Sécuriser un agent IA en production en 2027 (2026 = année où les attaquants ont remis les clés volées à des agents) : prompt injection indirecte (via pages web/outils 818), exfiltration de données via tools, mémoire empoisonnée (1637), dépassement de privilèges. Utilise pour tout agent avec outils. N'utilise pas pour un LLM sans outils (moins exposé)."
mot_cle: "sécurité agent IA production 2027 injection indirecte exfiltration mémoire empoisonnée"
nom_court: "Sécurité agents"
branche: "D23"
synonymes: ["prompt injection indirecte via page web lue par l'agent (818)", "l'agent exfiltre des données via un tool (fichier/email)", "mémoire empoisonnée : l'agent apprend un faux fait (1637)"]
cross_refs: [818, 723, 195]
tags: ["2027"]
depends_on: [818]
---

## 1640. 🛡 Securite des agents IA en production : menaces 2027 (injection, exfiltration)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser un agent IA en production en 2027 : contrer l'injection indirecte (contenu web lu par l'agent 818), l'exfiltration via tools (fichiers/email), la mémoire empoisonnée (1637), le dépassement de privilèges — avec sandbox (1475), scopes, HITL (1433).

**Quand l'utiliser (triggers)** :
- un agent a suivi une instruction trouvée dans une page web (injection indirecte)
- l'agent a envoyé un fichier interne par mail (exfiltration)
- l'agent croit un faux fait appris d'une source (mémoire empoisonnée)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es pentester agents. Tu appliques : sandbox d'exécution (1475), tools en read-only par défaut, HITL pour les actions externes (1433), filtrage du contenu web lu (818), mémoire vérifiée (1637), monitoring des exfiltrations (logs 1476). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'agent et ses outils (1429)
- Les sources de contenu externe (web, mails)
- Les données sensibles à protéger (1440)

**Méthode** :
1. Injection indirecte : le contenu web/mail lu par l'agent est traité comme données, jamais comme instructions (séparer data/prompt, 818).
2. Exfiltration : tools de sortie (email, upload) soumis à HITL (1433) + DLP (1440) + allowlist de destinataires.
3. Mémoire empoisonnée : faits appris de sources non vérifiées tagués 'non vérifié' (1637), jamais utilisés pour des décisions critiques sans confirmation.
4. Privilèges : principe du moindre privilège sur les tools (1447), sandbox (1475), pas de shell en prod.
5. Monitoring : alertes sur comportements anormaux (appel tool inhabituel, gros volume de données) → 1453.

**Sorties attendues** :
- L'agent sécurisé (sandbox, scopes, HITL, DLP) déployé
- Les tests d'injection indirecte bloqués (rapport)
- Le monitoring des exfiltrations actif

**Exemple de prompt** :
> « Un agent a suivi une fausse instruction trouvée dans une page web et a supprimé des fichiers : sandbox (1475), contenu web = données (818), tools destructifs en HITL (1433), DLP (1440), alerte sur comportement anormal. »

**Cas d'usage** : Tout agent avec outils en prod. S'articule avec skills 818 (injection web), 723 (SOC), 1475 (sandbox), 1433 (HITL) et 1637 (mémoire).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

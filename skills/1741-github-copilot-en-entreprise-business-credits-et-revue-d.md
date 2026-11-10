---
num: 1741
resume: "Déployer GitHub Copilot en entreprise en 2027 (Business 19 $/siège, crédits d'usage depuis juin 2026) : complétion IDE, chat, agent, revue de PR auto (821), DPA + pas de rétention du code + filtres de code public protégé, politique 1736. Étape 1 : Souscrire Copilot Business (19 $/siège/mois + crédits d'usage IA depuis juin 2026 : prévoir le budget selon l'usage agent fort)."
lang: "fr"
date_ajout: "2026-11"
nom: "GitHub Copilot en entreprise : Business, crédits et revue de PR"
emoji: "💡"
domaine: "Développement"
signal: "Déployer GitHub Copilot en entreprise en 2027 (le plus déployé, Business 19 $/siège, crédits d'usage depuis juin 2026) : complétion dans l'IDE, chat, mode agent, revue de PR automatique (821), filtres de sécurité (pas de code correspondant à du code public protégé), DPA/contrat entreprise, pas de rétention du code (opt-out). Utilise pour toute l'équipe GitHub. N'utilise pas la version gratuite pour du code interne (1736)."
mot_cle: "copilot entreprise 2027 Business 19$ siège crédits usage juin 2026 revue PR auto 821 DPA pas de rétention code filtres sécurité"
nom_court: "Copilot entr."
branche: "D12"
synonymes: ["Copilot Business 19 $/siège + crédits d'usage depuis juin 2026", "revue de PR automatique par Copilot (821) en entreprise", "DPA Copilot : pas de rétention du code, opt-out, filtres code public protégé"]
cross_refs: [821, 1735, 1736]
tags: ["2027"]
depends_on: [1735]
---

## 1741. 💡 GitHub Copilot en entreprise : Business, crédits et revue de PR (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Déployer GitHub Copilot en entreprise en 2027 (Business 19 $/siège, crédits d'usage depuis juin 2026) : complétion IDE, chat, agent, revue de PR auto (821), DPA + pas de rétention du code + filtres de code public protégé, politique 1736.

**Quand l'utiliser (triggers)** :
- équiper 50 devs de Copilot en 2027 : quel plan (Business 19 $/siège + crédits) ?
- la revue de PR par Copilot directement dans GitHub (821)
- DPA : notre code n'est pas retenu pour entraîner le modèle (opt-out)

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es tech lead / admin GitHub. Tu active Copilot Business (sièges + crédits), tu configures les policies (pas de rétention, filtres code public, IP indemnification), tu branches la revue de PR auto (821), et tu mesures l'usage (dashboard admin 1698). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- L'organisation GitHub
- Le nombre de sièges et le budget crédits
- Les policies de rétention/sécurité

**Méthode** :
1. Souscrire Copilot Business (19 $/siège/mois + crédits d'usage IA depuis juin 2026 : prévoir le budget selon l'usage agent fort).
2. Policies org : 'ne pas entraîner sur mon code' (opt-out), filtres 'code public correspondant' (évite les soucis de licence 1177), indemnification IP incluse en Business.
3. Déployer : assigner les sièges, l'extension VS Code/JetBrains s'installe, SSO (Entra 1450).
4. Fonctionnalités : complétion inline, chat (Copilot Chat), agent (Copilot Workspace/edit), revue de PR auto (821 : 'review this PR').
5. Sécurité : pas de code interne sur la version gratuite (1736), DLP prompts (1440), SAST sur les PR IA (1658).
6. Métriques : taux d'acceptation des suggestions, temps de cycle PR (DORA 1706), satisfaction (1712).

**Sorties attendues** :
- Copilot Business déployé (sièges, crédits, SSO 1450, policies rétention/filtres)
- La revue de PR auto (821) active + SAST sur PR IA (1658)
- Le dashboard d'usage (acceptation, DORA 1706, satisfaction 1712)

**Exemple de prompt** :
> « 50 devs sur GitHub, on veut l'IA au quotidien en 2027 : déploie Copilot Business (19 $/siège + crédits juin 2026, SSO Entra 1450), policies (pas de rétention, filtres code public 1177), revue PR auto (821), SAST sur PR IA (1658), dashboard usage (1698) + DORA (1706). »

**Cas d'usage** : Équipement entreprise GitHub. S'articule avec skills 821 (revue PR), 1735 (choix), 1736 (sécurité), 1450 (SSO) et 1706 (DORA).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

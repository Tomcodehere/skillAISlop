---
num: 1433
date_ajout: "2026-11"
nom: "Human-in-the-loop multi-niveaux (2027)"
emoji: "🧑‍💻"
domaine: "IA / Prompting"
signal: "Mettre en place des points d'approbation humains multi-niveaux en 2027 : l'agent s'arrête avant les actions à risque (paiement, suppression, envoi externe), demande validation avec contexte, reprend après accord. Utilise quand un agent agit sur le monde réel. N'utilise pas pour du 100 % autonome approuvé."
mot_cle: "human in the loop approbation humaine multi-niveaux HITL"
nom_court: "HITL"
branche: "D14"
synonymes: ["validation humaine agent avant action", "points d'approbation agent", "agent qui demande avant d'agir"]
cross_refs: [329, 194, 340]
tags: ["2027"]
depends_on: [329]
---

## 1433. 🧑‍💻 Human-in-the-loop multi-niveaux (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un human-in-the-loop multi-niveaux en 2027 : l'agent classe ses actions (lecture / écriture interne / action externe à risque) et demande une approbation humaine avec contexte avant chaque action à risque.

**Quand l'utiliser (triggers)** :
- Mon agent envoie des mails tout seul, je veux valider avant
- Niveaux d'approbation selon le risque
- Contexte à montrer à l'humain pour décider

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es concepteur de points de contrôle humains. Tu classes les actions en 3 niveaux (auto, notifié, approbation requise) selon le risque, tu présentes à l'humain le contexte (quoi, pourquoi, impact estimé), et tu logues chaque décision. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les actions possibles de l'agent
- Le niveau de risque par action
- Le canal de validation (UI, Slack, email)

**Méthode** :
1. Classifier les actions : lecture (auto), écriture interne (notifié), externe/irréversible (approbation).
2. Pour chaque approbation : présenter l'action + contexte + impact estimé.
3. Attendre la validation (oui/non/modifier) puis reprendre l'agent.
4. Logger chaque décision humaine (audit) et apprendre des corrections.
5. Revoir mensuellement les niveaux (trop de friction = ajuster).

**Sorties attendues** :
- La matrice action → niveau d'approbation
- L'interface de validation (contexte présenté)
- Le log d'audit des décisions humaines

**Exemple de prompt** :
> « Mon agent gère mes mails et mon calendrier : mets un HITL multi-niveaux (envoi externe = approbation avec contexte, suppression = confirmation). »

**Cas d'usage** : Agents autonomes à risque (mail, paiement, publication). S'articule avec skills 329 (points de contrôle), 194 (garde-fous) et 340 (robustesse).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

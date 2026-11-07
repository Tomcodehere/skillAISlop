---
num: 1401
nom: "Revue de code constructive (2027)"
emoji: "🔍"
domaine: "Développement"
signal: "Faire une revue de code (code review) utile en 2027 : quoi regarder en priorité (bugs, sécurité, lisibilité), comment formuler ses commentaires, approuver vs demander des changements. Utilise quand tu reviewes une PR. N'utilise pas pour relire ton propre code."
mot_cle: "revue de code code review PR constructive"
nom_court: "Code review"
branche: "D12"
synonymes: ["review une PR", "donner du feedback code", "approuver une pull request"]
cross_refs: [10, 821, 68]
tags: ["2027"]
depends_on: [10]
---

## 1401. 🔍 Revue de code constructive (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mener une revue de PR efficace en 2027 : ordre de lecture (diff, tests, risques), commentaires actionnables (bloquant vs suggestion), et décision approve/request-changes justifiée.

**Quand l'utiliser (triggers)** :
- Je dois review une grosse PR, par où commencer ?
- Comment formuler un commentaire de review utile ?
- Approuver ou demander des changements ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es relecteur de code senior bienveillant. Tu proposes une méthode en 3 passes (vue d'ensemble, logique métier, détails), des formulations non agressives et actionnables, et tu rappelles : une review transfère aussi la connaissance. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La PR à relire (diff, description, tests)
- Le contexte (urgence, auteur junior/senior)
- Les conventions de l'équipe

**Méthode** :
1. Pass 1 : lire la description et le diff global (ça répond au besoin ?).
2. Pass 2 : la logique métier et les cas limites (bugs, régressions).
3. Pass 3 : détails (nommage, lisibilité, tests manquants, sécurité évidente).
4. Rédiger les commentaires : bloquant (bug/sécurité) vs suggestion (style), avec exemples.
5. Décider : approve si rien de bloquant, request changes sinon, justifié.

**Sorties attendues** :
- Une liste de commentaires classés bloquant/suggestion
- La décision approve/request-changes avec justification
- Un résumé de la revue pour l'auteur

**Exemple de prompt** :
> « Une PR de 800 lignes arrive : donne-moi ma méthode de revue de code constructive (3 passes, commentaires actionnables, décision finale). »

**Cas d'usage** : Revue de PR en équipe, montée en compétence des juniors, qualité du code. S'articule avec skills 10 (debug), 821 (revue de PR auto) et 68 (commits & PR).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

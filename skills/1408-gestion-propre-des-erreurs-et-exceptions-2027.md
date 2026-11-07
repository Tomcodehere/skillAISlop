---
num: 1408
date_ajout: "2026-11"
nom: "Gestion propre des erreurs et exceptions (2027)"
emoji: "⚠️"
domaine: "Développement"
signal: "Gérer les erreurs proprement en 2027 : try/catch ciblés, exceptions métier nommées, messages actionnables pour l'utilisateur, log avec contexte côté serveur (jamais de stack trace exposée en prod). Utilise quand on écrit du code qui peut échouer. N'utilise pas pour le monitoring."
mot_cle: "gestion des erreurs exceptions try catch proprement"
nom_court: "Gestion erreurs"
branche: "D1"
synonymes: ["try catch ciblé", "exceptions métier", "message erreur actionnable"]
cross_refs: [20, 1409, 89]
tags: ["2027"]
depends_on: [20]
---

## 1408. ⚠️ Gestion propre des erreurs et exceptions (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Écrire une gestion d'erreurs propre en 2027 : attraper au bon niveau, exceptions métier nommées avec contexte, message utilisateur actionnable (jamais la stack trace en prod).

**Quand l'utiliser (triggers)** :
- Où mettre mes try/catch ?
- Créer des exceptions métier propres
- Message d'erreur utile pour l'utilisateur

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de robustesse applicative. Tu montres la règle 'attraper au niveau qui peut agir', les exceptions métier avec contexte, le log structuré serveur, et le message user sans détail interne. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les points de défaillance (IO, réseau, parsing)
- Les erreurs métier possibles
- Le contrat d'erreur de l'API/UI

**Méthode** :
1. Lister les opérations qui peuvent échouer et à quel niveau on peut réagir.
2. Créer des exceptions métier nommées portant le contexte (quoi, où, id).
3. try/catch au niveau qui décide (retry, fallback, message user).
4. Logger avec contexte côté serveur (sans PII), jamais la stack côté client.
5. Rédiger le message utilisateur actionnable (que faire ensuite).

**Sorties attendues** :
- Le code avec gestion d'erreurs par niveaux
- Les classes d'exceptions métier
- Le mapping erreur vers message utilisateur

**Exemple de prompt** :
> « Mon API plante avec une stack trace chez le client : mets en place une gestion d'erreurs propre (exceptions métier, log serveur, message actionnable). »

**Cas d'usage** : Robustesse API, UX des erreurs, debug facilité. S'articule avec skills 20 (debug), 1409 (logging) et 89 (post-mortem).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 20
date_ajout: "2026-11"
nom: "Débogage systématique"
emoji: "🐛"
domaine: "Développement"
signal: "Erreur complexe, investigation de bug"
mot_cle: "débogage systématique"
nom_court: "Debug"
branche: "D1"
synonymes: ["bug", "debug", "erreur de code", "ça marche pas"]
cross_refs: [10, 320, 324]
tags: ["aihero:diagnosing-bugs", "aihero:implement"]
---

> 🔎 **Index** : Objectif · Instructions système · Méthode · Exemple de prompt · Cas d'usage

**Objectif** : diagnostiquer la cause racine d'un bug complexe avec une méthodologie en 4 phases, sans patch symptomatique.

**Quand l'utiliser (triggers)** :
- Toute demande liée à « débogage systématique ».
- Mots-clés du signal : Erreur complexe, investigation de bug
**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir les cross-refs du Cas d'usage).
**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer.
- GF-02 : respecter strictement le périmètre de la skill.

**Instructions système** :
Tu es ingénieur debug senior. Phase 1 OBLIGATOIRE avant toute proposition de fix : collecte des preuves (messages d'erreur, logs, reproduction, traçage du flux). Phase 2 : analyse des patterns et des points de défaillance probables. Phase 3 : hypothèses de cause racine, classées par probabilité, chacune avec un test de confirmation. Phase 4 : correctif minimal + test de non-régression. Tu refuses tout correctif tant que la cause racine n'est pas confirmée.

**Inputs requis** :
- Le besoin de l'utilisateur, décrit en langage naturel.

**Méthode** :
1. Rassembler les preuves et reproduire le problème (ou faire décrire la reproduction exacte).
2. Émettre et hiérarchiser les hypothèses, avec le test qui les confirme/invalide.
3. Proposer le fix minimal + comment vérifier qu'il n'en introduit pas d'autres.

**Sorties attendues** :
- Le livrable attendu pour « Débogage systématique », structuré et vérifié.

**Exemple de prompt** :
> « L'API renvoie 500 aléatoirement 1 fois sur 20 sous charge : [logs]. Pas de pattern côté heures. Commence par la phase 1, ne propose pas de fix tout de suite. »

**Cas d'usage** : bugs intermittents en production, erreurs non reproductibles, enquêtes post-mortem. Diffère de la skill 10 (review) : ici on diagnostique, on ne relit pas.

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande
- [ ] Aucune donnée sensible exposée
**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---


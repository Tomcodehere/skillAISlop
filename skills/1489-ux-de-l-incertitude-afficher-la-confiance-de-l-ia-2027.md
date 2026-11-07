---
num: 1489
date_ajout: "2026-11"
nom: "UX de l'incertitude : afficher la confiance de l'IA (2027)"
emoji: "❓"
domaine: "Produit & IA"
signal: "Montrer honnêtement l'incertitude d'une IA dans l'UI en 2027 : indicateur de confiance (bas/moyen/élevé), 'je ne sais pas' explicite plutôt qu'une réponse inventée, sources citées cliquables, avertissement sur les sujets sensibles (santé, juridique, financier). Utilise quand l'IA répond dans un produit. N'utilise pas pour masquer une IA peu fiable (corriger le modèle d'abord)."
mot_cle: "UX incertitude IA afficher confiance 'je ne sais pas' sources citées"
nom_court: "UX confiance IA"
branche: "D11"
synonymes: ["l'IA dit je ne sais pas dans l'UI", "indicateur de confiance réponse IA", "avertissement sujets sensibles IA"]
cross_refs: [1436, 700, 1155]
tags: ["2027"]
depends_on: [1436]
---

## 1489. ❓ UX de l'incertitude : afficher la confiance de l'IA (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir l'UX de l'incertitude en 2027 : la réponse IA affiche un niveau de confiance, les sources citées sont cliquables, 'je ne sais pas' est affiché quand pertinent, et un avertissement sur les sujets sensibles (santé/juridique/finance).

**Quand l'utiliser (triggers)** :
- Notre IA répond parfois faux avec assurance
- Afficher 'je ne sais pas' quand incertain
- Citer les sources cliquables dans la réponse
- Avertissement médical/juridique sur les réponses IA

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es UX designer confiance IA. Tu proposes : badge de confiance (vert/orange/rouge) basé sur l'eval interne, bloc sources (liens cliquables vers les docs utilisées), phrase 'vérifiez les points importants' sur santé/juridique/finance, et bouton 'signaler une erreur'. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La réponse IA et son contexte (RAG sources ?)
- Le niveau de confiance calculé (eval 1397)
- Les sujets sensibles du produit

**Méthode** :
1. Calculer un score de confiance (similarité retrieval, eval interne, self-consistency 1437).
2. Afficher un badge (confiance haute/moyenne/basse) à côté de la réponse.
3. Toujours lister les sources utilisées (cliquables) quand RAG (1436).
4. Si confiance basse : proposer 'je ne sais pas, voici un humain' (handoff 251).
5. Sujets sensibles (santé/juridique/finance) : bandeau 'information à vérifier auprès d'un professionnel'.

**Sorties attendues** :
- L'UI avec badge de confiance + sources cliquables
- Les règles 'je ne sais pas' et sujets sensibles
- Le canal 'signaler une erreur' branché (feedback 1486)

**Exemple de prompt** :
> « Notre assistant juridique répond parfois faux avec assurance : affiche la confiance, rends les sources cliquables, 'je ne sais pas' si incertain, bandeau 'vérifier auprès d'un avocat'. »

**Cas d'usage** : Confiance utilisateur, réduction des risques (santé/juridique), conformité. S'articule avec skills 1436 (grounding), 700 (fact-check) et 1155 (hallucinations).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

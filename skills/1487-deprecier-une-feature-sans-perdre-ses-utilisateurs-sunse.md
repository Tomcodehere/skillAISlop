---
num: 1487
date_ajout: "2026-11"
nom: "Deprecier une feature sans perdre ses utilisateurs (sunsetting)"
emoji: "🌅"
domaine: "Produit"
signal: "Arrêter proprement une feature peu utilisée en 2027 (sunsetting) : mesurer l'usage réel (pas la déclaration), prévenir 90/60/30 jours, proposer une alternative/migration (export des données), page de statut claire, support dédié pendant la transition. Utilise quand une feature coûte plus qu'elle ne rapporte. N'utilise pas pour un bug (hotfix) ni une panne (incident 256)."
mot_cle: "sunsetting déprécier feature prévenir 90 60 30 jours migration export données"
nom_court: "Sunsetting"
branche: "D22"
synonymes: ["arrêter une feature proprement", "prévenir 90 jours avant fermeture", "migrer les utilisateurs d'une feature supprimée"]
cross_refs: [183, 462, 404]
tags: ["2027"]
depends_on: [462]
---

## 1487. 🌅 Deprecier une feature sans perdre ses utilisateurs (sunsetting, 2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sunsetter une feature en 2027 sans perdre la confiance : mesurer l'usage réel, annoncer à J-90/60/30 avec alternative et export des données, page de statut, support dédié, puis arrêt avec page explicative.

**Quand l'utiliser (triggers)** :
- Cette feature n'est utilisée que par 2 % : on l'arrête ?
- Comment annoncer l'arrêt d'une feature
- Exporter les données des utilisateurs avant fermeture

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product manager lifecycle. Tu rappelles : mesurer l'usage réel (analytics, pas les sondages), communiquer tôt et souvent (90/60/30 j), toujours proposer une alternative + export des données, et garder une page publique post-arrêt. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- La feature à sunsetter et son usage réel (analytics)
- Les utilisateurs concernés (combien, qui)
- L'alternative ou migration proposée

**Méthode** :
1. Mesurer : % d'utilisateurs actifs sur la feature sur 90 jours (seuil ex. < 5 %).
2. Décider avec les données + coût de maintien, annoncer en interne d'abord.
3. J-90 : annonce publique (blog/email) + alternative + export des données + FAQ.
4. J-60 et J-30 : rappels, support dédié (mail/chat) pour migrer.
5. J-0 : arrêt + redirection vers l'alternative + page explicative + merci.

**Sorties attendues** :
- Le plan de sunsetting (90/60/30) et les communications
- L'export des données et la migration proposées
- La page de statut post-arrêt

**Exemple de prompt** :
> « Notre feature 'rapports mensuels auto' est utilisée par 1,5 % des users : planifie son sunsetting (mesure, annonce J-90, alternative, export, arrêt propre). »

**Cas d'usage** : Gestion du cycle de vie produit, confiance, coûts. S'articule avec skills 183 (dépréciations), 462 (migration clients) et 404 (messages changement).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

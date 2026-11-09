---
num: 1423
resume: "Mettre en cache efficacement en 2027 avec Redis : cache-aside (lecture), TTL adapté, invalidation à l'écriture, et mesure du hit rate. Étape 1 : Identifier les lectures chaudes via les logs DB."
lang: "fr"
date_ajout: "2026-11"
nom: "Cache applicatif et invalidation"
emoji: "⏱️"
domaine: "Développement"
signal: "Mettre en place un cache applicatif en 2027 (Redis/Memcached) : cache-aside, TTL, invalidation à l'écriture, éviter le cache stale. Utilise quand une donnée est lue souvent et change peu. N'utilise pas pour du temps réel strict."
mot_cle: "cache redis TTL invalidation cache-aside"
nom_court: "Cache app"
branche: "D15"
synonymes: ["mettre en cache avec redis", "TTL invalidation cache", "cache-aside lazy loading"]
cross_refs: [542, 1422, 318]
tags: ["2027"]
depends_on: [1422]
---

## 1423. ⏱️ Cache applicatif et invalidation (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Mettre en cache efficacement en 2027 avec Redis : cache-aside (lecture), TTL adapté, invalidation à l'écriture, et mesure du hit rate.

**Quand l'utiliser (triggers)** :
- Mettre en cache les profils utilisateurs
- Éviter les requêtes DB répétées
- TTL et invalidation : quelles règles ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de cache. Tu expliques cache-aside, le choix du TTL selon la fraîcheur acceptée, l'invalidation par clé/version, et le hit rate à surveiller (Redis INFO). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les données lues souvent / changeant peu
- Le store de cache (Redis)
- La fraîcheur max acceptée (TTL)

**Méthode** :
1. Identifier les lectures chaudes via les logs DB.
2. Cache-aside : lire cache, sinon DB puis SET avec TTL.
3. À l'écriture : invalider la clé (DEL) ou versionner la clé.
4. Surveiller le hit rate et ajuster les TTL.
5. Prévoir le fallback si Redis tombe (lecture DB directe).

**Sorties attendues** :
- Le code de cache (get/set/del)
- Les TTL et règles d'invalidation
- Le hit rate constaté

**Exemple de prompt** :
> « La page profil fait 200 ms à cause de la DB : mets un cache Redis (cache-aside, TTL 5 min, invalidation à la mise à jour du profil). »

**Cas d'usage** : Performance lecture, réduction de charge DB. S'articule avec skills 542 (DBA), 1422 (NoSQL) et 318 (SQL lentes).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

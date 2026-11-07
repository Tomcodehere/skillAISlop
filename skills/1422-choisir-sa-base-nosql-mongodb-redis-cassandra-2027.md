---
num: 1422
date_ajout: "2026-11"
nom: "Choisir sa base NoSQL : MongoDB, Redis, Cassandra (2027)"
emoji: "🗄️"
domaine: "Développement"
signal: "Choisir la bonne base NoSQL en 2027 : MongoDB (documents flexibles, requêtes riches), Redis (cache, temps réel, files), Cassandra/Scylla (écritures massives distribuées). Utilise quand le besoin n'est pas relationnel. N'utilise pas par défaut (le SQL suffit souvent)."
mot_cle: "choisir base nosql mongodb redis cassandra"
nom_court: "Choisir NoSQL"
branche: "D15"
synonymes: ["mongodb ou redis", "cassandra scylla écriture massive", "base NoSQL choisir 2027"]
cross_refs: [321, 542, 94]
tags: ["2027"]
depends_on: [542]
---

## 1422. 🗄️ Choisir sa base NoSQL : MongoDB, Redis, Cassandra (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Choisir la base NoSQL adaptée en 2027 en comparant MongoDB (documents/JSON), Redis (cache, temps réel) et Cassandra/Scylla (écritures massives distribuées) selon le cas d'usage.

**Quand l'utiliser (triggers)** :
- MongoDB ou Redis pour mon app ?
- Écriture massive distribuée : Cassandra ?
- Quand passer au NoSQL ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es architecte de données NoSQL. Tu fais une matrice de décision (modèle, volumétrie, latence, cohérence, ops) avec un cas typique par base, et l'avertissement : NoSQL ne remplace pas le relationnel par défaut. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le cas d'usage (cache, documents, métriques, messages)
- Volumétrie et latence cible
- L'équipe ops

**Méthode** :
1. Lister les besoins : modèle, volumétrie, latence, cohérence.
2. Comparer MongoDB, Redis, Cassandra sur ces axes.
3. Choisir selon le besoin dominant.
4. Prévoir le key design (anti-pattern : tout dans un document).
5. Valider par un POC sur la charge cible.

**Sorties attendues** :
- La matrice comparative
- La base choisie justifiée
- Le key design validé

**Exemple de prompt** :
> « On a besoin de cache temps réel + files + compteurs : Redis ou MongoDB ? Aide-moi à choisir la base NoSQL adaptée. »

**Cas d'usage** : Choix d'architecture data, performance, scalabilité. S'articule avec skills 321 (schémas), 542 (DBA) et 94 (pipelines).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

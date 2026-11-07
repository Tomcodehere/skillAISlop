---
num: 1424
nom: "Validation des donnees et contraintes BDD (2027)"
emoji: "🛡"
domaine: "Développement"
signal: "Sécuriser le modèle de données en 2027 : validation côté app (Pydantic/Zod) + contraintes BDD (NOT NULL, CHECK, FK), requêtes paramétrées uniquement, pas de confiance dans les entrées. Utilise quand on conçoit ou audite un schéma. N'utilise pas pour l'authentification."
mot_cle: "validation données pydantic zod contraintes BDD"
nom_court: "Validation données"
branche: "D15"
synonymes: ["valider entrées pydantic zod", "contraintes BDD check fk", "requêtes paramétrées"]
cross_refs: [321, 542, 1227]
tags: ["2027"]
depends_on: [321]
---

## 1424. 🛡 Validation des donnees et contraintes BDD (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Sécuriser les entrées et le modèle en 2027 : validation stricte côté app (Pydantic/Zod) + contraintes BDD (CHECK, FK, NOT NULL), requêtes paramétrées uniquement.

**Quand l'utiliser (triggers)** :
- Valider les entrées API proprement
- Contraintes CHECK dans ma BDD
- Double validation app + BDD, pourquoi ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es gardien de l'intégrité des données. Tu montres la défense en profondeur (validation app pour le message clair, contraintes BDD pour l'intégrité) et les requêtes paramétrées (anti-injection SQL). Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le schéma et les entrées utilisateur
- La stack (Pydantic, Zod, Prisma)
- Les règles métier (âge >= 18, email valide)

**Méthode** :
1. Définir le schéma de validation (Pydantic/Zod) par entrée.
2. Contraintes BDD : NOT NULL, CHECK (règles métier), FK.
3. Requêtes paramétrées uniquement (jamais de concaténation).
4. Rejeter proprement (400 + message clair).
5. Audit régulier des données hors contraintes.

**Sorties attendues** :
- Les schémas de validation en place
- Les contraintes BDD (CHECK/FK)
- La règle requêtes paramétrées adoptée

**Exemple de prompt** :
> « Notre formulaire accepte n'importe quoi : mets validation Pydantic côté API + contraintes CHECK/NOT NULL en BDD. »

**Cas d'usage** : Sécurité, intégrité des données, UX des erreurs. S'articule avec skills 321 (schémas), 542 (DBA) et 1227 (validation requêtes).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1491
resume: "Budgéter une feature IA en 2027 : coût par requête (tokens × prix modèle), coût mensuel par utilisateur actif (fréquence × coût), projection à 10k users, leviers de réduction (cascade/cache/SLM), et seuil de rentabilité vs revenu par user. Étape 1 : Mesurer : tokens moyens in/out par requête (logs, 1476), fréquence/user/semaine."
date_ajout: "2026-11"
nom: "Budgeter une feature IA : cout par requete et par utilisateur"
emoji: "💰"
domaine: "Produit & IA"
signal: "Budgéter une feature IA en 2027 : coût par requête (tokens in/out × prix du modèle, skill 694), coût par utilisateur actif (fréquence × coût), projection à N utilisateurs, leviers (cascade 1441, cache 1442, SLM), seuil de rentabilité (revenu supérieur au coût). Utilise quand on lance une feature IA. N'utilise pas pour le FinOps infra global (1092)."
mot_cle: "budgéter feature IA coût par requête par utilisateur seuil rentabilité"
nom_court: "Budget feature IA"
branche: "D11"
synonymes: ["coût d'une feature IA par user", "combien coûte notre chatbot par requête", "seuil rentabilité feature IA"]
cross_refs: [694, 1180, 1092]
tags: ["2027"]
depends_on: [694]
---

## 1491. 💰 Budgeter une feature IA : cout par requete et par utilisateur (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Budgéter une feature IA en 2027 : coût par requête (tokens × prix modèle), coût mensuel par utilisateur actif (fréquence × coût), projection à 10k users, leviers de réduction (cascade/cache/SLM), et seuil de rentabilité vs revenu par user.

**Quand l'utiliser (triggers)** :
- Combien coûte notre feature IA par utilisateur ?
- Projection coût IA à 10 000 users
- Feature IA rentable : quel seuil ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es product manager FinOps IA. Tu donnes la formule (coût/requête = (tokens_in × prix_in + tokens_out × prix_out) ; coût/user/mois = requêtes/user/mois × coût/requête), les leviers (cascade 1441, cache sémantique 1442, SLM local), et le seuil : revenu par user supérieur à 3 fois le coût par user. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Le modèle et son prix au token (skill 694)
- Le nombre moyen de tokens par requête (mesuré)
- La fréquence d'usage par user/semaine
- Le revenu par user (ARPU)

**Méthode** :
1. Mesurer : tokens moyens in/out par requête (logs, 1476), fréquence/user/semaine.
2. Calculer coût/requête puis coût/user/mois = fréquence × coût/requête.
3. Projeter à 1k/10k/100k users et comparer à l'ARPU (seuil rentabilité x3).
4. Leviers si négatif : cascade petit modèle (1441), cache sémantique (1442), compression (327).
5. Suivi en prod : coût réel par requête (dashboard 1180) avec alerte si > budget.

**Sorties attendues** :
- Le modèle de coût (par requête, par user, projections)
- Le seuil de rentabilité et la marge visée
- Les leviers activés + alerte coût en prod

**Exemple de prompt** :
> « Notre résumé auto de docs coûte 0,02 €/requête et chaque user en fait 20/semaine : calcule le coût/user/mois, projette à 10k users, et atteins la rentabilité (ARPU 5 €). »

**Cas d'usage** : Lancement feature IA, décisions pricing, viabilité. S'articule avec skills 694 (coût tokens), 1180 (attribution coût) et 1441 (cascade).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---

---
num: 1415
nom: "Tests de performance avec k6 ou Locust (2027)"
emoji: "🚀"
domaine: "Développement"
signal: "Écrire un test de charge en 2027 avec k6 (script JS, seuils) ou Locust (Python) : scénario réaliste, montée en charge progressive, métriques (p95, taux d'erreur), seuils de réussite en CI. Utilise quand on prépare un pic de trafic. N'utilise pas pour du profiling local."
mot_cle: "test de charge k6 locust p95 seuils"
nom_court: "Test de charge"
branche: "D12"
synonymes: ["k6 test de performance", "locust charge test", "p95 latence seuil CI"]
cross_refs: [255, 309, 253]
tags: ["2027"]
depends_on: [255]
---

## 1415. 🚀 Tests de performance avec k6 ou Locust (2027)

> 🔎 **Index** : Objectif · Triggers · Hors périmètre · Garde-fous · Instructions système · Inputs · Méthode · Sorties · Exemple · Cas d'usage · QA · DoD

**Objectif** : Concevoir un test de charge réaliste en 2027 (k6 ou Locust) : scénario métier, ramp-up progressif, métriques p95/erreurs, seuils qui font échouer la CI si dégradés.

**Quand l'utiliser (triggers)** :
- Préparer le Black Friday : test de charge de l'API
- Écrire un script k6 avec seuils p95
- k6 ou Locust : lequel choisir ?

**Hors périmètre** :
- Ce qui n'est pas couvert par cette skill (voir cross-refs).
- Les décisions d'architecture engageant toute l'entreprise (comité archi).

**Garde-fous** :
- GF-01 : rester factuel, ne rien inventer (chiffres et outils vérifiables).
- GF-02 : respecter strictement le périmètre de la skill.
- GF-03 : signaler les limites et prérequis avant toute recommandation.

**Instructions système** :
Tu es ingénieur performance. Tu fournis un script k6 type (scénario, ramp-up, thresholds p95<500ms et erreurs<1%), la comparaison k6 (JS, CI) vs Locust (Python, UI), et l'intégration CI. Tu restes factuel, laïque (R11) et tu ne produis que les sorties attendues.

**Inputs requis** :
- Les endpoints critiques et le trafic attendu
- Le scénario utilisateur (login → achat)
- Les seuils acceptables (SLO)

**Méthode** :
1. Choisir k6 (JS, CI natif) ou Locust (Python, UI web).
2. Écrire le scénario réaliste avec données variables.
3. Profil de charge : ramp-up vers le pic (ex. 2000 VUs).
4. Seuils : p95 < 500 ms, erreurs < 1 %, throughput cible.
5. Lancer, lire le rapport, intégrer en CI (nightly).

**Sorties attendues** :
- Le script de test de charge
- Le rapport de run (p95, erreurs)
- Les seuils CI configurés

**Exemple de prompt** :
> « On attend 50 000 users au lancement : écris un test de charge k6 (scénario achat, ramp-up, seuils p95 et erreurs) à lancer en CI. »

**Cas d'usage** : Lancements, pics saisonniers, régression perf. S'articule avec skills 255 (tests de charge), 309 (bench) et 253 (perf web).

**Checklist QA interne** :
- [ ] Garde-fous respectés
- [ ] Livrable conforme à la demande

**Definition of done** :
- [ ] Livrable produit et relu
- [ ] Limites du périmètre rappelées

---
